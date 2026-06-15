---
layout: page
permalink: /quotes/
title: quotes
description: A few aphorisms and quotes I keep coming back to.
nav: false
---

<!-- _pages/quotes.md — quotes are stored in _data/quotes.yml -->
<div class="quotes">
{% for q in site.data.quotes %}
  <blockquote>
    <p>{{ q.text }}</p>
    <footer>— <strong>{{ q.author }}</strong>{% if q.source %}, <em>{{ q.source }}</em>{% endif %}</footer>
  </blockquote>
{% endfor %}
</div>
