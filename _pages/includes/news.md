<section id="experience" class="home-section" aria-labelledby="experience-title">
  <span id="-working-experience" class="legacy-anchor" aria-hidden="true"></span>
  <h2 id="experience-title">Experience</h2>
  <div class="timeline">
    {% for item in site.data.academic_profile.experience %}
    <article class="timeline__entry">
      <p class="timeline__date">{{ item.dates }}</p>
      <div>
        <h3>{{ item.organization }}{% if item.role != "" %}<span class="timeline__role"> · {{ item.role }}</span>{% endif %}</h3>
        {% if item.advisor %}
        <p>Researched machine learning applications in finance with <a href="{{ item.advisor.url }}">{{ item.advisor.name }}</a>.</p>
        {% else %}
        <p>{{ item.description }}</p>
        {% endif %}
      </div>
    </article>
    {% endfor %}
  </div>
</section>
