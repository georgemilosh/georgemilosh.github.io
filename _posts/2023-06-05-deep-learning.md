---
layout: post
title:  Deep learning
date: 2023-06-05 

description: useful resources for practical tutorials on deep learning
tags: deep-learning machine-learning tutorials resources
categories: how-to
giscus_comments: true
related_posts: true
toc:
  sidebar: right
---

Below I list various sources that I found myself or through friends for people wishing to follow `pedagogical tutorials` on modern `deep learning` techniques.  

## General resources

Artificial Intelligence is highly dynamic and hyped field: [AI Index](https://aiindex.stanford.edu/report/){:target="\_blank"} is a good place to start if you want to get a sense of the field.

> ##### TIP
>
> Join a journal club, or start your own where you and your peers would review the latest papers to stay updated on the trends. 
{: .block-tip }

I recommend joining the [mailing list](https://listes.ipsl.fr/sympa/info/mljournalclub) of our journal club which brings together geophysicists interested in the applications of machine learning.

This one is quite nice but targets french speakers: [CNRS-Fidle](https://gricad-gitlab.univ-grenoble-alpes.fr/talks/fidle){:target="\_blank"}. They cover the basics and the modern tools of machine learning from A to Z with practical exercises and offerring a convenient docker or an option to use personal python environment. They also have a [youtube channel](https://www.youtube.com/@CNRS-FIDLE) with all the lectures.

## Transformers

[A gentle introduction](http://jalammar.github.io/illustrated-transformer/){:target="\_blank"} by Jay Alammar into how multi-head self-attention mechanism was implemented in the original paper on transformers. The jupyter notebook that is available is a bit dated since it is based on `tensorflow 1`. You will find other useful links in this introduction such as pytorch anotated code that goes with the famous article [Attention is all you need](https://arxiv.org/abs/1706.03762).

This course on [Natural Language Processing](https://huggingface.co/learn/nlp-course/chapter1/1) is recommended if you want practical tips on how to pick up pre-trained transformers from `Hugging Face` 🤗 repository and fine-tune them for your downstream task.

Interestingly some argue that transformers are a version of Graph Neural Network (GNN): [Source: Gradient website](https://thegradient.pub/transformers-are-graph-neural-networks/) 

## Diffusion models

A success of AI art such as DALL-E and Midjourney have made headlines. But what are they based on? Find out more about probabilistic denoising diffusion models:
- I really recommend the following repository for people who are interested in Langevin dynamics (which is at the heart of diffusion models), a tutorial by Prof. F. Rousseau on Diffusion Models: [part A](https://youtu.be/L6Ig_-ARtuo), [part B](https://youtu.be/2KXsNkkZmYk) supplied with a [jupyter notebook](https://github.com/CIA-Oceanix/ai4oac2023/tree/main/tutorial_DiffModel).
- Materials from the 🤗 [Huggingface Diffusion Models course](https://github.com/huggingface/diffusion-models-class/tree/main) have been recommended to me by [Redouane Lguensat](https://redouanelg.github.io/).


## Tutorials for physics applications

[MOOC Machine Learning in Weather & Climate](https://lms.ecmwf.int/course/index.php?categoryid=1) from European Centre of Medium Range Weather Forecast (ECMWF). An ecxellent introduction for Earth science practitioners willing to dive in to how geophysicists apply machine learning to their domain. From statistichal post-processing of weather forecasts to physics-guided data-driven parametrizations of climate.

This [paper](https://www.sciencedirect.com/science/article/pii/S0370157319300766) is also a bit dated now, but offers a brief intro to Machine Learning to Physicists.

