import { defineConfig } from "cf/config";

export default defineConfig(({ mode }) => ({
  accountId: "501a87290b94fa1f5bbfaad20399ef74",
  worker: {
    name: "pccx",
    compatibilityDate: "2026-09-30",
    workersDev: true,
    previewUrls: false,
    // Preview mode lets us verify Workers before transferring the public domain.
    domains: mode === "preview" ? [] : ["docs.pccx.ai"],
    assets: { htmlHandling: "auto-trailing-slash", notFoundHandling: "404-page" },
    observability: { enabled: true },
  },
}));
