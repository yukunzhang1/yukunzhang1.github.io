<section id="about-me" class="introduction" aria-labelledby="name">
  <h1 id="name">Yukun Zhang</h1>
  <p class="research-line">AI Economics · Language Models · Interpretability &amp; Alignment</p>
  {% for paragraph in site.data.academic_profile.bio %}
  <p>{{ paragraph }}</p>
  {% endfor %}
</section>
