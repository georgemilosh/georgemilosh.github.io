---
layout: page
permalink: /publications/
title: publications
description: my publications. here you can also view abstracts, pdfs, slides... etc
image: papers.jpeg
years: [2024, 2023, 2022, 2021, 2019, 2018, 2017, 2016, 2015, 2013, 2009]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
