# AI Agent Economics

The series is hosted at `/research/ai-agent-economics/` in the personal homepage repository. It is a standalone page without the personal profile sidebar. The previous redirect to the CrewMoon website has been replaced with local content.

## Sources and content

The summaries, bilingual abstracts, findings, and figures were transferred from `CrewMoon/ai-agent-economics` at commit `6efa5860db3c329cf29f629f6875ef8cb311c984`, at the author's request. The original website remains unchanged. Provenance is retained in `data/ai-agent-series.json`.

- The homepage uses the original site's adapted research summaries, not verbatim abstracts.
- The four detail pages retain the original bilingual abstracts, findings, and figure captions.
- Figure files are uncropped WebP copies of the existing PNG figures. No scientific content was redrawn or generated.
- The page layout and interactions follow the LLM Paper Series: warm background, muted rose accents, figure-and-text rows, bilingual toggle, and image enlargement.
- Authors, dates, Working Paper labels, Poster, and BibTeX controls are omitted from the visible paper listings. Citation metadata retains the original authors and publication dates for indexing.

## Maintenance

Edit `data/ai-agent-series.json`, `assets/css/ai-agent-series.css`, or `assets/js/ai-agent-series.js`, then run:

```sh
python scripts/build_agent_series.py
```

The generator also keeps links from the personal homepage and LLM series pointed at the local Agent series. The generator uses only the Python standard library. Validate all five pages, their internal links and anchors, the language toggle, and image enlargement before publishing. GitHub Pages performs the Jekyll build.
