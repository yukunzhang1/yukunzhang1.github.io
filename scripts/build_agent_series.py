from pathlib import Path
from html import escape as E
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/ai-agent-series.json').read_text())
BASE='/research/ai-agent-economics/'
ORIGIN='https://yukunzhang1.github.io'
def lang(en,zh):return f'<span data-lang="en">{E(en)}</span><span data-lang="zh" lang="zh-Hans">{E(zh)}</span>'
def revision(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:12]
def head(title,path,description,citations=''):
    suffix='Yukun Zhang' if title=='AI Agent Economics' else 'AI Agent Economics'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{E(title)} — {suffix}</title>
  <meta name="description" content="{E(description,quote=True)}">
  <meta name="theme-color" content="#fbf8f6">
  <meta property="og:title" content="{E(title,quote=True)}">
  <meta property="og:description" content="{E(description,quote=True)}">
  <meta property="og:type" content="{'article' if citations else 'website'}">
  <meta property="og:url" content="{ORIGIN}{path}">
  <link rel="canonical" href="{ORIGIN}{path}">
  {citations}
  <link rel="stylesheet" href="/assets/css/ai-agent-series.css?v={revision('assets/css/ai-agent-series.css')}">
  <script src="/assets/js/ai-agent-series.js?v={revision('assets/js/ai-agent-series.js')}" defer></script>
</head>'''

NAV=f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar"><nav class="wrap" aria-label="Research navigation"><a class="home-link" href="/">Yukun Zhang</a><div class="toplinks"><a href="/Generative-AI-Economic-Series/">Generative AI Economics</a><a href="/research/llm-paper-series/">LLM Paper Series</a><button class="language" type="button" hidden>中文</button></div></nav></header>'''
FOOT=f'''<footer><div class="wrap"><span>AI Agent Economics</span><a href="/">{lang('Academic homepage ↗','个人学术主页 ↗')}</a></div></footer>'''
DIALOG=f'''<dialog class="image-dialog" aria-labelledby="figure-title"><div class="dialog-head"><p class="dialog-title" id="figure-title"></p><button class="close-dialog" type="button" aria-label="Close figure">×</button></div><img alt=""><p class="figure-source"><a href="{BASE}#papers" target="_blank" rel="noopener noreferrer">{lang('View the source paper ↗','查看原论文 ↗')}</a></p></dialog>'''

def external(url,label):return f'<a href="{E(url,quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>'
def links(p,details=True):
    result=external('https://arxiv.org/pdf/'+p['arxiv_id'],'PDF')+external(p['arxiv'],'arXiv')
    if details: result+=f'<a href="{BASE}{p["slug"]}/">{lang("Details & figures","详情与图表")}</a>'
    result+=external(p['hf'],'Hugging Face')
    return result

def row(p):
    title=E(p['title']);pid=p['slug'];image=p['image']
    return f'''<article class="paper" id="{pid}" aria-labelledby="title-{pid}">
  <a class="paper-image" href="{image}" data-figure data-title="{E(p['title'],quote=True)}" data-source="{p['arxiv']}" aria-label="Enlarge figure: {E(p['title'],quote=True)}"><img src="{image}" alt="{E(p['image_alt'],quote=True)}" width="200" height="138" loading="lazy" decoding="async"></a>
  <div class="paper-content">
    <p class="paper-meta"><span class="topic">{lang(p['topic']['en'],p['topic']['zh'])}</span></p>
    <h3 id="title-{pid}">{external(p['arxiv'],title)}</h3>
    <p class="summary-label">{lang('Research summary','研究概述')}</p>
    <p class="summary">{lang(p['summary']['en'],p['summary']['zh'])}</p>
    <div class="paper-links">{links(p)}</div>
  </div>
</article>'''

def front(title,path):return f'---\nlayout: null\ntitle: {json.dumps(title)}\npermalink: {path}\n---\n'

index=front('AI Agent Economics',BASE)+head('AI Agent Economics',BASE,'Four connected papers on delegation rights, AI production, execution control, and social welfare.')+f'''
<body id="top">{NAV}
<main class="wrap" id="main">
  <section class="hero" aria-labelledby="page-title">
    <p class="eyebrow">{lang('Research series','研究系列')}</p>
    <h1 id="page-title">AI Agent Economics</h1>
    <p class="lead">{lang('From Delegation Rights to Social Welfare','从委托权到社会福利')}</p>
    <p class="series-overview" id="question">{lang(DATA['overview']['en'],DATA['overview']['zh'])}</p>
    <div class="hero-links"><a href="#papers">{lang('Explore the papers','阅读系列论文')}</a><a href="mailto:215010026@link.cuhk.edu.cn">{lang('Contact','联系')}</a>{external('https://scholar.google.com/citations?user=w8XKACEAAAAJ&hl=en','Google Scholar')}</div>
    <div class="interests"><span>{lang('Delegation rights','委托权')}</span><span>{lang('Production organization','生产组织')}</span><span>{lang('Execution control','执行控制')}</span><span>{lang('Social welfare','社会福利')}</span></div>
  </section>
  <section id="papers" aria-labelledby="papers-title">
    <div class="section-head"><h2 id="papers-title">{lang('Research papers','研究论文')}</h2><p>{lang('Four connected papers','四篇相互关联的论文')}</p></div>
    <div class="paper-list">{''.join(row(p) for p in DATA['papers'])}</div>
  </section>
  <section class="contact" id="contact" aria-labelledby="contact-title"><h2 id="contact-title">{lang('Research & collaboration','研究交流与合作')}</h2><p>Yukun Zhang · <a href="mailto:215010026@link.cuhk.edu.cn">215010026@link.cuhk.edu.cn</a></p></section>
</main>{FOOT}{DIALOG}
</body></html>
'''
(ROOT/'_pages').mkdir(exist_ok=True)
(ROOT/'_pages/ai-agent-economics.html').write_text(index)

def figure_links(content,p):
    def wrap(match):
        image=match.group(0);src=re.search(r'src="([^"]+)"',image).group(1)
        return f'<a class="figure-link" href="{src}" data-figure data-title="{E(p["title"],quote=True)}" data-source="{p["arxiv"]}" aria-label="Enlarge research figure">{image}</a>'
    return re.sub(r'<img\b[^>]*>',wrap,content)

for p in DATA['papers']:
    path=BASE+p['slug']+'/'
    citations=p['citation_meta']+f'\n<meta name="citation_abstract_html_url" content="{ORIGIN}{path}">'
    details=front(p['title'],path)+head(p['title'],path,p['summary']['en'],citations)+f'''
<body id="top">{NAV}
<main class="wrap detail-page" id="main">
  <p class="breadcrumb"><a href="{BASE}">{lang('← AI Agent Economics','← AI Agent 经济学')}</a></p>
  <header class="detail-header">
    <p class="eyebrow">{lang(p['topic']['en'],p['topic']['zh'])}</p>
    <h1>{E(p['title'])}</h1>
    <div class="paper-links">{links(p,False)}</div>
  </header>
  {figure_links(p['hero_html'],p)}
  {figure_links(p['detail_html'],p)}
  <div class="detail-footer"><a href="{BASE}#papers">{lang('← All papers','← 返回论文列表')}</a></div>
</main>{FOOT}{DIALOG}
</body></html>
'''
    (ROOT/'_pages'/('agent-'+p['slug']+'.html')).write_text(details)

for path in ['_data/navigation.yml','_pages/includes/pub.md','_data/academic_profile.json','_pages/llm-paper-series.html','scripts/build_llm_series.py']:
    file=ROOT/path
    content=file.read_text().replace('https://crewmoon.github.io/ai-agent-economics/',ORIGIN+BASE)
    file.write_text(content)
print('Generated the series homepage and four detail pages; updated personal and LLM series navigation.')
