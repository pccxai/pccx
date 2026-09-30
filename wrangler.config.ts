import { defineWranglerConfig } from "wrangler/experimental-config";

export default defineWranglerConfig({
  assetsDirectory: "_build/html",
  types: { generate: false },
});
