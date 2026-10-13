# Personal homepage

The root page uses `_layouts/academic-home.html` and `assets/css/academic-home.css`. It does not load the legacy theme stylesheet or menu script. The three standalone research series remain separate pages.

## Content

- `_data/academic_profile.json`: biography, experience, education, and update date.
- `_pages/includes/pub.md`: the research directory and other economics publication.
- `_data/navigation.yml`: main navigation.
- `_config.yml`: author name, contact links, and site metadata.

The homepage retains legacy publication and education anchors where content still exists. Empty News, Honors, Talks, and Internships menu entries have been removed. No CV file or CV link is included.

Employment and education dates follow the pre-existing homepage. The current affiliation follows the existing introduction's Alipay wording. The former claim that the CUHK research assistantship took place after graduation has been removed because the listed dates overlap the master's degree. Degree and role labels should be updated only with the author's confirmed information.

Keep conference acceptances, awards, and presentations in their corresponding research series. Do not add them as standalone homepage sections or label unaccepted LLM papers as working papers or forthcoming submissions.

## Validation

Before publishing, check JSON/YAML, internal anchors, relative file targets, the series links, and the absence of duplicate IDs. GitHub Pages performs the authoritative Jekyll build. Inspect the published page for desktop layout, navigation, image loading, and contact URLs. The responsive stylesheet changes the layout at 1000px and 700px; assess narrow layouts when a supported browser viewport control is available.
