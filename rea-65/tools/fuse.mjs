import { flipFuses, FuseVersion, FuseV1Options } from "@electron/fuses";
await flipFuses("/workspace/re/lab65/electron/hardened/electron", {
  version: FuseVersion.V1,
  [FuseV1Options.RunAsNode]: false,
  [FuseV1Options.EnableNodeOptionsEnvironmentVariable]: false,
  [FuseV1Options.EnableNodeCliInspectArguments]: false,
  [FuseV1Options.EnableEmbeddedAsarIntegrityValidation]: true,
  [FuseV1Options.OnlyLoadAppFromAsar]: true,
});
console.log("flipped");
