---
layout: page
title: Artigos publicados
description: Artigos do 2ex-lab sobre dupla excepcionalidade, neurodiversidade, aprendizagem, educação inclusiva, criatividade, tecnologia e acessibilidade.
permalink: /artigos/
---

Uma biblioteca de conteúdos produzidos pelo 2ex-lab. Os artigos são organizados por data, área editorial e assuntos relacionados, com fontes e limites explicitados ao longo de cada publicação.

{% assign published_posts = site.posts | sort: "date" | reverse %}
{% if published_posts.size > 0 %}
<p class="articles-count"><strong>{{ published_posts.size }}</strong> {% if published_posts.size == 1 %}artigo publicado{% else %}artigos publicados{% endif %}</p>

<div class="published-articles">
  {% for post in published_posts %}
    {% assign primary_category = post.categories | first %}
    {% assign category_info = site.data.taxonomy.categories | where: "slug", primary_category | first %}
    <article class="published-article">
      <p class="published-article-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d/%m/%Y" }}</time>
        {% if category_info %}
          <span aria-hidden="true"> · </span><span>{{ category_info.title | escape }}</span>
        {% elsif primary_category %}
          <span aria-hidden="true"> · </span><span>{{ primary_category | replace: "-", " " | capitalize }}</span>
        {% endif %}
      </p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h2>
      {% if post.description %}
        <p>{{ post.description | escape }}</p>
      {% else %}
        <p>{{ post.excerpt | strip_html | normalize_whitespace | truncate: 220 | escape }}</p>
      {% endif %}
      <p class="published-article-link"><a href="{{ post.url | relative_url }}" aria-label="Ler artigo: {{ post.title | escape }}">Ler artigo →</a></p>
    </article>
  {% endfor %}
</div>
{% else %}
  <p>Os primeiros artigos estão em preparação. Volte em breve para acompanhar as publicações do laboratório.</p>
{% endif %}
