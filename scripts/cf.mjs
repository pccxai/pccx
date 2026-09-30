#!/usr/bin/env node
// cf project commands with the existing release-policy selector and a scoped
// Windows delegate workaround for https://github.com/cloudflare/cf/issues/19.
import { existsSync, mkdirSync, cpSync } from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

export function parseArguments(input, cwd = process.cwd()) {
  const args = [...input], options = {};
  for (let i = 0; i < args.length;) {
    const match = /^(--config|-c|--env|-e|--outdir|--name)(?:=(.*))?$/.exec(args[i]);
    if (!match) { i++; continue; }
    const count = match[2] === undefined ? 2 : 1;
    const value = match[2] ?? args[i + 1];
    if (value === undefined || value.startsWith('--')) throw new Error(`Missing value for ${match[1]}`);
    const key = ({ '-c': 'config', '-e': 'env' })[match[1]] ?? match[1].slice(2);
    if (Object.hasOwn(options, key)) throw new Error(`Duplicate ${match[1]}`);
    options[key] = ['env', 'name'].includes(key) ? value : resolve(cwd, value);
    args.splice(i, count);
  }
  if (args[0] === 'versions' && args[1] === 'upload') args.splice(0, 2, 'workers', 'versions', 'create');
  // cf 1.0.0-beta.5 always sets strict:true in its deploy and upload delegate.
  if (args.includes('--strict')) args.splice(args.indexOf('--strict'), 1);
  if (!['build', 'dev', 'deploy', 'workers', 'versions'].includes(args[0])) throw new Error('Use cf directly for resource commands; this entry point handles project builds and deployments.');
  let project = options.config ? dirname(options.config) : cwd;
  while (!existsSync(join(project, 'cloudflare.config.ts'))) {
    const parent = dirname(project);
    if (parent === project) {
      // Some reviewed release builders put the policy in RUNNER_TEMP.
      // Resolve the project from cwd; do not change the policy's relative paths.
      if (options.config && project !== cwd) {
        let candidate = cwd;
        while (!existsSync(join(candidate, 'cloudflare.config.ts'))) {
          const next = dirname(candidate);
          if (next === candidate) throw new Error(`No migrated cloudflare.config.ts for ${options.config}`);
          candidate = next;
        }
        project = candidate;
        break;
      }
      throw new Error(`No migrated cloudflare.config.ts for ${options.config ?? cwd}`);
    }
    project = parent;
  }
  if (options.config && !existsSync(options.config)) throw new Error(`Missing release policy: ${options.config}`);
  return { args, options, project };
}

export function versionPromotion(input, worker) {
  const versions = [], annotations = {};
  let dryRun = false;
  for (let i = 0; i < input.length; i++) {
    const arg = input[i];
    if (arg === '--yes') continue;
    if (arg === '--dry-run') { dryRun = true; continue; }
    if (arg === '--message') {
      const message = input[++i];
      if (!message || message.startsWith('--') || Object.hasOwn(annotations, 'workers/message')) throw new Error('Expected one explicit promotion message');
      annotations['workers/message'] = message;
      continue;
    }
    const match = /^([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})@(\d+(?:\.\d+)?)%?$/.exec(arg);
    if (!match) throw new Error(`Unsupported promotion argument: ${arg}`);
    if (versions.some(version => version.version_id === match[1])) throw new Error('Duplicate promotion version');
    versions.push({ version_id: match[1], percentage: Number(match[2]) });
  }
  if (!versions.length || versions.some(version => version.percentage > 100) || Math.abs(versions.reduce((sum, version) => sum + version.percentage, 0) - 100) > 1e-9) throw new Error('Explicit version percentages must total 100');
  const body = { strategy: 'percentage', versions, ...(Object.keys(annotations).length ? { annotations } : {}) };
  return ['workers', 'deployments', 'create', '--worker', worker, '--body', JSON.stringify(body), ...(dryRun ? ['--dry-run'] : [])];
}

export function windowsDelegateArguments(args) {
  const operation = args[0] === 'dev' ? 'dev' : 'build';
  const result = [operation];
  for (let i = 1; i < args.length; i++) {
    const match = /^(--mode|-m|--port|--host)(?:=(.*))?$/.exec(args[i]);
    if (match) {
      const flag = match[1] === '-m' ? '--mode' : match[1];
      if (operation !== 'dev' && flag !== '--mode') throw new Error(`Unsupported build option: ${flag}`);
      const value = match[2] ?? args[++i];
      if (!value || value.startsWith('-')) throw new Error(`Missing value for ${flag}`);
      result.push(flag, value);
    } else if (args[i] === '--local' && operation === 'dev') result.push('--local');
    else if (args[0] === 'dev' || args[0] === 'build') throw new Error(`Unsupported Windows ${operation} option: ${args[i]}`);
  }
  return result;
}

export function main(input = process.argv.slice(2)) {
  const { args, options, project } = parseArguments(input);
  const require = createRequire(join(project, 'package.json'));
  const cfPackage = require.resolve('cf/package.json');
  const cf = join(dirname(cfPackage), 'bin', 'cf');
  const env = { ...process.env, ...(options.config ? { ALTI_CF_CONFIG: options.config } : {}),
    ...(options.env !== undefined ? { ALTI_CF_ENV: options.env } : {}) };
  if (args[0] === 'versions') {
    if (!options.config && !options.name) throw new Error('Version promotion/readback requires an explicit release policy or Worker name');
    const policy = options.name ? { name: options.name } : require('wrangler').unstable_readConfig({ config: options.config, ...(options.env ? { env: options.env } : {}) }, { hideWarnings: true });
    if (!policy.name) throw new Error('Release policy has no Worker name');
    if (args[1] === 'deploy') {
      args.splice(0, args.length, ...versionPromotion(args.slice(2), policy.name));
    } else throw new Error('Use cf workers versions get --worker-id for new readbacks; legacy release evidence readers retain their existing JSON schema.');
  } else if (options.name) throw new Error('Worker names must come from the reviewed project policy');
  const run = (file, argv) => {
    const child = spawnSync(process.execPath, [file, ...argv], { cwd: project, env, stdio: 'inherit' });
    if (child.error) throw child.error;
    if (child.status !== 0) process.exit(child.status ?? 1);
  };
  const builds = args[0] === 'build' || args[0] === 'deploy' || args.slice(0, 3).join(' ') === 'workers versions create';
  if (process.platform === 'win32' && ((builds && !args.includes('--prebuilt')) || args[0] === 'dev')) {
    const delegate = join(dirname(require.resolve('wrangler/package.json')), 'bin', 'cf-wrangler.js');
    run(delegate, windowsDelegateArguments(args));
    if (args[0] === 'dev') return;
    if (args[0] !== 'build') args.push('--prebuilt');
  } else if (args[0] === 'build') {
    run(cf, args);
  }
  if (args[0] !== 'build') run(cf, args);
  if (options.outdir) {
    const output = join(project, '.cloudflare/output/v0');
    const bundle = join(output, 'workers/default/bundle');
    if (!existsSync(bundle)) throw new Error('cf Build Output contains no Worker bundle to export');
    mkdirSync(options.outdir, { recursive: true });
    cpSync(bundle, options.outdir, { recursive: true });
  }
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
