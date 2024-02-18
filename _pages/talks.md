---
layout: page
permalink: /talks/
title: talks
description: Talks at conferences and beyond, click `abs` to read abstract, `media` to watch the talk, `slides` to view the pdf of the presenatation etc.
image: talks.png
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014]
nav: true
---

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f talks -q @*[year={{y}}]* %}
{% endfor %}

</div>
