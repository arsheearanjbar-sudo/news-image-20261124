import { createHash } from "node:crypto";
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry image missing next to main.ts: ${source}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

const wanted = createHash("sha256").update(readFileSync(source)).digest("hex");
const got = createHash("sha256").update(readFileSync(target)).digest("hex");
if (wanted !== got) {
  throw new Error(`copy mismatch: source ${wanted} vs output ${got}`);
}
const bytes = readFileSync(target).length;

console.log(`wrote ${target} (${bytes} bytes) sha256=${got}`);
