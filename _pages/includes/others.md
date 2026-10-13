<section id="education" class="home-section" aria-labelledby="education-title">
  <span id="-education" class="legacy-anchor" aria-hidden="true"></span>
  <span id="-educations" class="legacy-anchor" aria-hidden="true"></span>
  <h2 id="education-title">Education</h2>
  <div class="timeline">
    {% for item in site.data.academic_profile.education %}
    <article class="timeline__entry">
      <p class="timeline__date">{{ item.dates }}</p>
      <div>
        <h3>{{ item.institution }}</h3>
        <p>{{ item.degree }}</p>
        {% if item.advisors.size > 0 %}
        <p class="education-advisors">Advisors: {% for advisor in item.advisors %}<a href="{{ advisor.url }}">{{ advisor.name }}</a>{% unless forloop.last %} and {% endunless %}{% endfor %}.</p>
        {% endif %}
      </div>
    </article>
    {% endfor %}
  </div>
</section>
