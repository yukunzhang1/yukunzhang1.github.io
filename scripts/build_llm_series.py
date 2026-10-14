from pathlib import Path
from html import escape as E
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/llm-paper-series.json').read_text())
def lang(en,zh):return f'<span data-lang="en">{E(en)}</span><span data-lang="zh" lang="zh-Hans">{E(zh)}</span>'
def version(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:12]
def paper(p):
 authors=', '.join('<strong>'+E(a)+'</strong>' if a=='Yukun Zhang' else E(a) for a in p['authors'])
 venue='<span class="venue">'+E(p['venue'])+'</span>' if p['venue'] else ''
 links=''.join(f'<a href="{E(url,quote=True)}" target="_blank" rel="noopener noreferrer">{E(label)}</a>' for label,url in p['links'])
 return f'''<article class="paper" id="{p['slug']}" aria-labelledby="title-{p['slug']}">
  <a class="paper-image" href="{p['image']}" data-source="{E(p['source'],quote=True)}" aria-label="Enlarge figure: {E(p['title'],quote=True)}"><img src="{p['image']}" alt="Research figure from {E(p['title'],quote=True)}" width="200" height="138" loading="lazy" decoding="async"></a>
  <div class="paper-content">
    <p class="paper-meta"><span class="topic">{lang(p['topic'],p['topic_zh'])}</span>{venue}</p>
    <h3 id="title-{p['slug']}"><a href="{p['source']}" target="_blank" rel="noopener noreferrer">{E(p['title'])}</a></h3>
    <p class="authors">{authors}</p>
    <p class="summary">{lang(p['summary'],p['summary_zh'])}</p>
    <div class="paper-links">{links}</div>
  </div>
</article>'''

html=f'''---
layout: null
title: "LLM Paper Series"
permalink: /research/llm-paper-series/
---
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>LLM Paper Series — Yukun Zhang</title>
  <meta name="description" content="Research on language-model training, architecture, interpretability, and alignment by Yukun Zhang and collaborators.">
  <meta name="theme-color" content="#fbf8f6">
  <meta property="og:title" content="LLM Paper Series">
  <meta property="og:description" content="Seven papers on understanding and improving language models.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://yukunzhang1.github.io/research/llm-paper-series/">
  <link rel="stylesheet" href="/assets/css/llm-paper-series.css?v={version('assets/css/llm-paper-series.css')}">
  <script src="/assets/js/llm-paper-series.js?v={version('assets/js/llm-paper-series.js')}" defer></script>
</head>
<body id="top">
<a class="skip-link" href="#papers">Skip to papers</a>
<main class="wrap">
  <section class="hero" aria-labelledby="page-title">
    <button class="language series-language" type="button" aria-label="切换至中文" hidden>中文</button>
    <h1 id="page-title">LLM Paper Series</h1>
    <p class="lead">{lang('Understanding and improving language models: how they learn, organize information, and generate reliable responses.','理解并改进语言模型：它们如何学习、组织信息，以及生成可靠的回答。')}</p>
    <div class="hero-links"><a href="#papers">{lang('Explore the papers','阅读系列论文')}</a><a href="mailto:215010026@link.cuhk.edu.cn">{lang('Contact','联系')}</a></div>
    <div class="interests">{''.join('<span>'+lang(en,zh)+'</span>' for en,zh in [('Data & Training','数据与训练'),('Model Architecture','模型架构'),('Interpretability','可解释性'),('Alignment','对齐')])}</div>
  </section>
  <section id="papers" aria-labelledby="papers-title">
    <div class="section-head"><h2 id="papers-title">{lang('Research papers','研究论文')}</h2><p>{lang('Seven papers · 2025–2026','七篇论文 · 2025–2026')}</p></div>
    <div class="paper-list">{''.join(paper(p) for p in DATA['papers'])}</div>
  </section>
  <section class="contact" id="contact" aria-labelledby="contact-title"><h2 id="contact-title">{lang('Research & collaboration','研究交流与合作')}</h2><p>Yukun Zhang · <a href="mailto:215010026@link.cuhk.edu.cn">215010026@link.cuhk.edu.cn</a></p></section>
</main>
<footer><div class="wrap"><span>LLM Paper Series · Yukun Zhang</span><a href="/">{lang('Academic homepage ↗','个人学术主页 ↗')}</a></div></footer>
<dialog class="image-dialog" aria-labelledby="figure-title"><div class="dialog-head"><p class="dialog-title" id="figure-title"></p><button class="close-dialog" type="button" aria-label="Close figure">×</button></div><img alt=""><p class="figure-source"><a href="#papers" target="_blank" rel="noopener noreferrer">{lang('View the source paper ↗','查看原论文 ↗')}</a></p></dialog>
</body>
</html>
'''
out=ROOT/'_pages/llm-paper-series.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(html)
print('Generated',out,'with',len(DATA['papers']),'papers.')
