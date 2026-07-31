---
name: pdf-to-png
description: Excelsior card-art conversion workflow. Use when the user invokes /pdf-to-png or asks to convert an image PDF to PNG, export card artwork from PDF, or batch-convert PDF images on Windows at native resolution without upscaling beyond embedded image DPI.
---

# PDF To PNG

Convert image PDFs, such as Photoshop card-art exports, to PNG files at the
highest resolution the source supports. Never upscale beyond embedded image PPI.

## Arguments

- Path ending in `.pdf`: required input PDF.
- Path starting with `/`: output directory.
- Name ending with `.png`: output filename.

Defaults:

- No output directory: use the input PDF folder.
- No output filename: use `{pdf-basename}.png` for single-page PDFs or `{pdf-basename}-{n}.png` for multi-page PDFs.
- Normalize `/c/Users/Kyle/Desktop` to `C:\Users\Kyle\Desktop` on Windows.

Reject output filenames that do not end in `.png`.

## Workflow

1. Parse arguments. Multiple PDFs are not supported in one call unless the user lists separate invocations.
2. Run the helper script from the Excelsior repo root; do not hand-roll Docker commands:

```powershell
& ".cursor/skills/pdf-to-png/scripts/Convert-PdfToPng.ps1" `
  -InputPdf "<input.pdf>" `
  [-OutputDir "<dir>"] `
  [-OutputFileName "<name.png>"]
```

3. Read the JSON output and report `dpi`, `pageCount`, and full `outputFiles` paths.
4. Show the single-page PNG result when possible; for multi-page output, list all files unless the user asks to inspect them.

## Resolution Policy

The script chooses DPI from embedded image metadata using Poppler
`pdfimages -list` x-ppi/y-ppi. If PPI is missing, it derives DPI from pixel
dimensions versus PDF page size. It requires Docker and the `minidocks/poppler`
image, which may be pulled on first run.

## Errors

- Docker not running: ask the user to start Docker Desktop, then retry.
- Input PDF not found: confirm and normalize the path.
- No PNG produced: inspect with `pdfinfo`; the PDF may be encrypted or empty.
- Output filename missing `.png`: reject and ask for a PNG filename.

## Completion Report

Report input, output paths, DPI with "no upscale", and page count. Display the
image for a single-page conversion when available.

## Related

- `add-card` skill.
- `docs/current/IMAGE_PIPELINE.md`.

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future image conversions:

- Record repeated PDF export, resolution, filename, or image-pipeline friction in the appropriate AgentOS memory or Excelsior context.
- Note helper-script improvements and recurring validation shortcuts as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
