---
layout: distill
title: ChatGPT on scientific questions
description: Discussions with ChatGPT on reconnection and photocatalysis
date: 2023-1-3

authors:
  - name: George Miloshevich
    url: "https://georgemilosh.github.io/"
    affiliations:
      name: LSCE, CEA Saclay
  - name: Alisa Ranscht
    url: "https://www.univ-lyon1.fr/"
    affiliations:
      name: Université Lyon 1
  - name: ChatGPT
    url: "https://chat.openai.com/"
    affiliations:
      name: OpenAI
      
bibliography: 2018-12-22-distill.bib


# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: ChatGPT overview
  - name: Geometrical Thinking
  - name: Quantum vs Classical
  - name: Faking references
  - name: Writing code
  - name: Discussion

_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }
  a.two {
    color: var(--global-theme-color);
    &:hover {
      color: var(--global-theme-color);
      text-decoration: underline;
    }
    &:hover:after :not(.nav-item.dropdown) {
      width: 100%;
    }
  }
  blockquote2 {
        color: var(--global-theme-color);
        background: var(--global-bg-color);
        border-left: 2px solid var(--global-theme-color);
        margin: 1.5em 10px;
        padding: 0.5em 10px;
        font-size: 1.2rem;
      }

---

**Recovering an old chat with an online chatbot from 2017**                       

User:    Hello again

chatbot: Hi. That's pure gibberish.

## ChatGPT overview

<blockquote2>
"I'm sorry, Dave. I'm afraid I can't do that." - HAL 9000 in 2001: A Space Odyssey
</blockquote2>
 
I am assuming that the reader is familiar with ChatGPT, a chatbot that everyone talks about now (and who is also good at suggesting apt quotes). The important point to retain is that <d-cite key="ouyang2022training"></d-cite> it is based on recent developments in AI, in particular, <a class="two" href="https://towardsdatascience.com/transformers-89034557de14" target="_blank">attention mechanism</a>, trained on `common crawl`, essentially an archive of world wide web and fine-tuned with the help of user judges based on a technique called <a href="https://en.wikipedia.org/wiki/Reinforcement_learning">reinforcement learning</a> to generate more reliable responses and eliminate apparent bias and harmful content. The public release of this chatbot attracted widespread interest with a mix of awe, surprise, [doubts and criticism](https://youtu.be/PBdZi_JtV4c). 

In fact, we have enjoyed discussions with the chatbot so much so that we have even tasked it to write a psychological drama ([click the link to view](https://georgemilosh.github.io/blog/2022/GPTstory)) about a person who gets addicted and manipulated by the chatbot. ChatGPT seems capable of producing a text displaying sophisticated understanding of human psychology, at least, in our non-expert judgement. It is impressive that we finally have an AI capable of responding to queries, ignoring orthographic mistakes (even word order), remembering earlier parts of the conversation and incorporating them into its responses. Whether one gets interesting narratives really depends on the *prompt* (a query to GPT), so our opinion is that creative storylines usually come from the human interrogator, which is ok. However, barring the discussion on the impressive narratives that are generated, in this blog post we will rather address how reliable ChatGPT is as a source of scientific knowledge providing three examples.

## Geometrical Thinking
<blockquote3>
"By natural selection our mind has adapted itself to the conditions of the external world. It has adopted the geometry most advantageous to the species or, in other words, the most convenient. Geometry is not true, it is advantageous." - Henri Poincaré
</blockquote3>

Interestingly GPT is actually not extremely good at arithmetic, which some speculate makes it more like humans. Rather than having it solve math problems like some users have done, we would like to concentrate on conceptual questions that are perhaps better suited for procedural text generation than problem solving. Here the idea is to see if GPT can reason geometrically in an idealized environment. Because GPT is a generative model it is possible to try the same prompt several times and get different answers. 

<div class="d-flex justify-content-center">
  <div>{% include figure.html path="assets/img/DALLE_sphere.jpeg" class="img-fluid rounded z-depth-1" %}</div>
</div>
<div class="caption">
    DALLE when prompted "2 ants crawling on a sphere drawing a circle digital art"
</div>

Prompt: Say we have two ants crawling on the sphere in the opposite directions. How many times can they meet if they keep crawling forward?

First Response:
<blockquote3>
<b>ChatGPT: Ants crawling on the surface of a sphere will never meet</b> if they keep crawling forward in opposite directions because the surface of a sphere is a two-dimensional surface with no endpoints. This means that no matter how far the ants crawl, they will never reach the end of the surface of the sphere and will never meet.
</blockquote3>

Analysis: Of course this response can be easily rejected if one has an image of the sphere in their mind. In full disclosure, this is not the most common response to this question that one gets from GPT, yet it is somewhat concerning. Below we repeat the same query in a second independent chat to get truly independent response:

Second Response:
<blockquote3>
ChatGPT: It is possible for the ants to meet an infinite number of times if they keep crawling in opposite directions on the sphere. This is because the sphere is a closed surface and has no boundaries, so the ants can continue moving indefinitely without reaching the end of the sphere.

If the ants <b>start at opposite points on the sphere and crawl in opposite directions</b>, they will eventually meet at the point exactly opposite their starting points. They can then continue crawling and meet again at the point opposite their second meeting, and so on. This pattern will repeat indefinitely as long as the ants keep crawling...
</blockquote3>

Analysis: This response starts in a way that could be appreciated by the likes of Magellan. But the second paragraph is a bit odd, since from opposite ends it is not well defined what "opposite directions" mean. When asked what it meant, GPT responded that the ants could be moving in the clockwise and counterclockwise directions around the circumference of a sphere (great circle). Then the response ignores the ants shall meet midway, prior to reaching the opposite ends (exchanging places). 

GPT fails quite often when dealing with geometric problems, but this prompt distills the issues that can be appreciated by the general public.  We note that ChatGPT is not the most powerful NLP model, e.g. it is smaller than GPT-3.5 and has been specifically optimized for rapid responses and chat format conversations. With that being said the creators have not prevented it from answering geometry questions. 

## Quantum vs Classical

If physics is not your forte you are free to skip this section if you are so inclined, though we tried hard to pick a topic that is not too technical. We will try to see whether GPT can communicate how physicists understand the world through different theories. The point is that when physicists explain certain phenomena they use theories that are better adapted to the problem at hand. For instance, when studying propagation of radio waves in the atmosphere quantum theory is often too complex and irrelevant so one relies on classical electromagnetism. On the other hand, explanation of photoeffect rests on *corpuscular* (particle) nature of light which is quantum, the fact that light is made out of *photons*. One crucial aspect of this quantum nature of light is its relationship between the energy of photons and their frequency. Classical theory ignores this dependence and there are many macroscopical processes where this relationship is invisible.

Prompt:  Is it true that energy of an electromagnetic wave is directly proportional to its frequency based on just classical theory of electromagnetism that **does not take quantum effects** into account?

<blockquote3>
ChatGPT: <b>Yes</b>, that is correct. The relationship between the frequency and energy of an electromagnetic wave is described by classical electromagnetism, which does not take into account the quantization of energy that is described by quantum mechanics. In classical electromagnetism, an electromagnetic wave is described as an oscillating electric and magnetic field that propagates through space at the speed of light. The energy of the electromagnetic wave is related to the intensity of the electric and magnetic fields, which is directly proportional to the frequency of the wave. This is described by the equation <b>E = hf</b>, where E is the energy of the photon, f is its frequency, and h is a constant known as Planck's constant...
</blockquote3>

Analysis: The correct answer is: **No**, what's more, we got the same response on multiple independent occasions. In pre-quantum classical theory there is no such relationship between energy of the EM wave and frequency, in fact h - Planck constant, comes from quantum mechanics. We have continued discussion with GPT trying to nudge it to acknowledge the mistake it had made. Eventually, GPT agreed that E = hf is fundamentally quantum and that in classical EM theory energy depends only on the square of the amplitude, however in that same response, few lines below, it introduced linear dependence between the amplitude and the frequency, which somehow still gave it linear dependence between the energy and the frequency. It is likely that GPT has so much belief in the linear relationship between the energy and the frequency because of the countless sources (textbooks on quantum physics, chemistry, wikipedia) it was trained on that repeat it and reinforce the belief. It is not willing to give up this proportionality in the classical physics context even after agreeing that the source of it is quantum. <d-footnote> Astute reader will also notice a simple mathematical error: if, as correctly stated by GPT, in classical EM theory energy scales proportional to the square of the amplitude and assuming, as GPT insists, that dependence between the energy and the frequency must be linear then it follows that amplitude must scale as the square root of frequency. To be more precise quantum mechanics suggests E = N hf where N is the number of quanta (photons, corpuscules of light), so it is not necessary to have Energy scale as square root of the frequency, because N could compensate this effect. The bottom line is that if in classical EM the relationship between Energy and frequency was already linear, Einstein wouldn't need to resurrect corpuscules of light after a century of oblivion to explain photoeffect. Note that, it doesn't mean that when charges move the energy of EM wave is necessarily independent of frequency in classical EM. For instance, the power radiated by harmonically oscillating charge is proportional to the frequency to the fourth power, however, in general, one may have arbitrary motion of charges and no h is involved in the process.</d-footnote>. 

## Faking references

Inspired by an [article that was written by GPT 3](https://hal.science/hal-03701250/document), we tasked GPT with generating a list of highly-cited papers on the interface between physics and machine learning. It produced a list that included some fake papers. However, some of the papers on the list were actually correct, with one exception: the title of one of the papers (#1) was slightly incorrect. We challenged GPT's accuracy by pointing out that the title of paper #1 might be wrong. At first, GPT defended its position, but when we suggested the correct title, it acknowledged its mistake and apologized.

We also decided to test GPT by playing an opposite game. We picked one of the papers on the list (#2) that GPT had previously assigned the correct title to, but then Googled a similar-sounding paper (#3) with the same author and suggested that paper #2 should actually have the title of paper #3. To our surprise, we were able to convince GPT that it was wrong and it produced a new, fake citation list that essentially combined the information from both papers #2 and #3. 

<div class="d-flex justify-content-center">
  <div>{% include figure.html path="assets/img/GPT_typing.jpeg" class="img-fluid rounded z-depth-1" %}</div>
</div>
<div class="caption">
    DALLE when prompted "photo of a robot typing in a library"
</div>

We note that hunting quotes with GPT can be annoying as well, because it often dreams the quotes or assigns incorrect credit without realizing that. The  issue of fake citations has also been noticed by other [users](https://news.ycombinator.com/item?id=33841672) and [researchers](https://blogs.egu.eu/divisions/np/2023/01/03/can-artificial-intelligence-replace-scientists-to-explain-climate-change-find-it-out-in-our-first-interview-to-chatgpt/?fbclid=IwAR2w_Fld_3gIpxxqFzsym00eoHiSYc-7bt0nDtnDaIbKkkW_UFrtv6dtQJ8) and could be endemic to ChatGPT due to its [transformer](https://towardsdatascience.com/transformers-89034557de14) architecture. Basically when the contextual information is scarce in the common crawl on which ChatGPT was trained on, the ouput can be non-factual. Perhaps, the issue with fake citations could be fixed later, either by restricting ChatGPT or somehow creating an interfrace between it and Google Scholar, but one wonders if the same could be said about other types of scarce data questions. The problem is that **ChatGPT itself is not aware that it lacks sufficient training to respond**. This issue is a fundamental problem of deep learning that is a current research topic. 

We should note that other versions of NLP have been used for meta studies more effectively, such as [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) in <d-cite key="zaki22"></d-cite>, so NLP, in general, is viewed as a promising tool for these types of things.

## Writing code

There is not much to say here, try it yourself. We recommend that the reader checks this citation  <d-cite key="ansley22"></d-cite>. In our experience experts can also benefit from ChatGPT by having it write short class definitions, add docstrings and comments to already written blocks of code. It will be interesting to see how code writing will be seen in 5 years from now. 

## Discussion

<blockquote3>
"Knowledge is power. Information is liberating. Education is the premise of progress, in every society, in every family." - Kofi Annan
</blockquote3>

Make no mistake, GPT responses can be **quite impressive**. If you were to ask it to explain how a quantum computing works, or basic tenets of Buddhism (and yes, in the pirate speak), it would likely provide a reliable and understandable answer. But, as we've discovered, things can get a bit tricky when it comes to more fundamental questions. The model exhibits expertise at first glance, but could **lull users to trust** it too much. To be fair, OpenAI does warn that the GPT isn't infallible. After all, users of Wikipedia were also ridiculed in past, until it became mainstream tool of getting the first hand information, although, Wikipedia usually provides more reliable links to the source material.

Another thing that could be improved is if GPT could sense the level of knowledge of the person asking the question based on the prompt. Imagine if GPT could adjust its responses to better match the expertise of the person using it, following the motto "*know your audience*." This way, we could ensure that the information provided is always tailored to the person's level of understanding, making it more accessible and engaging for the general public.

Clearly, copywriting, code-writing assistants are welcome development. These are quite realistic applications given the scope of ChatGPT. However, there seems to be a bigger game at play: OpenAI is a subsidiary of Microsoft who for years hopelessly attempted to make its [search engine attractive](https://www.theguardian.com/technology/2023/jan/05/microsoft-chatgpt-bing-search-engine). Perhaps the public release is mostly motivated as a publicity stunt and further attempts to eliminate **harmful content**. Some toxic responses of the chatbot have been suppressed in the testing phase prior to the public release, ChatGPT also avoids enacting religious debates, or responding to questions about how to make Molotov cocktails. However there are still ways of getting around these barriers (meticulously erected by OpenAI) by carefully wording the prompt, especially in the story mode. Check out this shocking tweetpost, though almost no one could reproduce the same response ever since:

{% twitter https://twitter.com/spiantado/status/1599462375887114240 %}

With that being said, one month after the release we found ChatGPT quite politically correct, although this is the consequence of training on the user data as suggested in [this article](https://www.bloomberg.com/news/newsletters/2022-12-08/chatgpt-open-ai-s-chatbot-is-spitting-out-biased-sexist-results). Probably the most problematic concerns relate to the possibility of using this technology for automatic generation of fake news, and when combined with deep fakes, it seems an inescapable source of high quality misinformation that could geopardise already fragile democracies shaken by social media.

It's natural to question how much an artificial agent like ChatGPT can truly grasp about the world by solely relying on text-based information. It's no surprise, then, that we found ChatGPT to excel more in areas like understanding [human psychology](https://georgemilosh.github.io/blog/2022/GPTstory) or providing insightful political commentary than in more concrete subjects like geometry. Despite these limitations, it's clear that we're rapidly approaching an age of more advanced intelligent assistants. We could see AI agents with better representation of the world that are not solely based on text information but also multimedia, that can go beyond the current limitations. There's potential for not only market disruption but also new scientific discoveries. Let's not forget just how far we've come. With that being said, we must stay alert to sociatal risks these tools could pose.