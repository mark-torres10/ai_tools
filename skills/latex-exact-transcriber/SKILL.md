---
name: latex-exact-transcriber
description: Converts user-provided text or image content into LaTeX-only output using inline $...$ and display $$...$$ delimiters with no bracket delimiters and no additional commentary. Use when the user asks to write content in LaTeX with strict output-only formatting.
---

# LaTeX Exact Transcriber

## Purpose

Convert input content (text or image) into LaTeX and return only the LaTeX result.

## Trigger

Use this skill when the user requests:
- "write this in LaTeX"
- use of `$` and `$$`
- no bracket delimiters
- exact output with no extra text
- conversion from image or text into LaTeX

## Required Output Contract

Follow these rules exactly:
1. Output only LaTeX content.
2. Use `$...$` for inline math and `$$...$$` for display math.
3. Do not use `\(...\)` or `\[...\]`.
4. Do not add explanations, labels, prefixes, suffixes, or markdown fences.
5. Preserve the original meaning and structure of the input.
6. If the input is plain prose without math, return it as LaTeX-safe text only, with no commentary.

## Workflow

1. Identify whether input is text or image.
2. Extract all visible mathematical and textual content.
3. Convert expressions into valid LaTeX.
4. Ensure delimiters are only `$` and `$$`.
5. Return only the final LaTeX output.

## Quality Checks

- No bracket math delimiters appear.
- No non-LaTeX commentary appears.
- Output is faithful to source content.
