# Maintaining LLM Paper Series

The standalone page at `/research/llm-paper-series/` uses `layout: null`: it does not inherit the personal photograph, biography, or sidebar. The page's name is **LLM Paper Series**.

Edit `data/llm-paper-series.json`, then run `python scripts/build_llm_series.py`. CSS and JavaScript live in `assets/css/llm-paper-series.css` and `assets/js/llm-paper-series.js`; their content hashes are added to the generated page to prevent stale cached assets.

Keep the accepted conference papers first: CausalMix (NeurIPS 2026) and Hierarchical Alignment (EMNLP 2026), as confirmed by the site owner; Continuous-Time Attention (EMNLP 2025), documented in the ACL Anthology. These conference labels do not claim that the 2026 proceedings links are already available. Do not label the remaining papers Working Paper or add prospective submission statuses.

Titles and author ordering were checked against arXiv and the ACL Anthology on 13 October 2026. The two May 2025 papers use their revised titles from the May 2026 versions. For arXiv:2505.18244, the arXiv author metadata spells the first name “Yukin”; the paper's HTML title block and the author's profile spell it “Yukun”, which is used here. Other author names follow the bibliographic metadata.

The short bilingual descriptions are editorial research summaries, not verbatim abstracts. Links take readers to the complete source papers. Only show project and code links supported by the source.

The seven thumbnail figures come from the respective papers or their official project page; no plots or results were generated for decoration. `data/llm-paper-series-figures.json` records their source URLs. WebP copies retain the entire figure. Clicking a thumbnail opens an accessible dialog; without JavaScript, it opens the image directly.

The visual reference is https://beccabai.github.io/: small paper figures, topic/venue metadata, title and authors in compact horizontal rows, a warm neutral background, and muted rose links. The page uses original implementation and the site owner's own research assets.
