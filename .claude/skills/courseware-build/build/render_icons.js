#!/usr/bin/env node
// Render react-icons glyphs to transparent PNGs for the slide deck's icon circles.
// Usage: NODE_PATH=$(npm root -g) node render_icons.js <out_dir> <name:Pack/Icon:hex> ...
// e.g.  node render_icons.js icons robot:fa6/FaRobot:FFFFFF
const path = require("path");
const fs = require("fs");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");

const out = process.argv[2];
fs.mkdirSync(out, { recursive: true });
(async () => {
  for (const spec of process.argv.slice(3)) {
    const [name, ref, hex = "FFFFFF"] = spec.split(":");
    const [pack, icon] = ref.split("/");
    const mod = require(`react-icons/${pack}`);
    const Comp = mod[icon];
    if (!Comp) { console.error(`missing icon ${ref}`); process.exitCode = 1; continue; }
    const svg = renderToStaticMarkup(React.createElement(Comp, { size: 256, color: `#${hex}` }));
    const file = path.join(out, `${name}-${hex}.png`);
    await sharp(Buffer.from(svg)).resize(256, 256).png().toFile(file);
  }
})();
