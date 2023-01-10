---
layout: distill
title: ChatGPT on scientific questions
description: Discussions with ChatGPT on reconnection and photocatalysis
date: 2023-1-3

authors:
  - name: George Miloshevich
    url: "georgemilosh.github.io"
    affiliations:
      name: LSCE, CEA Saclay
  - name: Alisa Ranscht
    url: "https://www.univ-lyon1.fr/"
    affiliations:
      name: Université Lyon 1
      
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
  - name: Conclusions

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
  .d-article a {
  outline: none;
  text-decoration: none;
  padding: 2px 1px 0;
  }
  .d-article a:link {
    color: #00ab37;
  }
  d-article. a:hover {
    border-bottom: 1px solid;
    text-decoration: underline;
  }


---

**Recovering an old chat from 2017**

Short conversation with an online chatbot many years ago:                         

User: Hello again

Rose: Hi. That's pure gibberish.

## ChatGPT overview
 
I am assuming that the reader is familiar with ChatGPT (which has public access as of now). If not, check out this [website](https://openai.com/blog/chatgpt) . The important point to retain is that <d-cite key="ouyang2022training"></d-cite> it is based on recent developments in AI, in particular, [attention mechanism](https://towardsdatascience.com/transformers-89034557de14), trained on `common crawl`, essentially an archive of world wide web and fine-tuned with the help of user judges based on a technique called <a href="https://en.wikipedia.org/wiki/Reinforcement_learning">reinforcement learning</a> to generate more reliable responses and eliminate apparent bias and harmful content. The public release of ChatGPT attracted widespread interest with a mix of awe, surprise, doubts and criticism. In this blog post our goals are to explore the capabilities of ChatGPT, after testing its responses for several weeks after the release. 

Generally, it seems that ChatGPT usually does a good job of providing simple explanations on a variety of topics, even as it has to impersonate a pirate as requested. It can also engage in conversations, where it is able to recall previously discussed topics and invent stories. In one of our conversations we asked ChatGPT to write a psychological drama ([click the link to view](https://georgemilosh.github.io/blog/2022/GPTstory)) about a person who gets addicted and manipulated by the chatbot. After several prompts we were able to a rather sophisticated understanding of human psychology, at least, in our non-expert judgement. It is impressive that we finally have an AI capable of responding to queries, ignoring orthographic mistakes (even word order), remembering earlier parts of the conversation and incorporating them into its responses. However, whether one gets interesting narratives really depends on the *prompt* (a quiery to GPT), so it seems that creativity usually comes from the user. The writing style can be also less rich, e.g. the constant repetition of phrases like "cannot help but" becomes annoying. Of course, this particular issue can be improved with scale.

With that being said there are headlines like the death of creative essay that have emerged after the release of the ChatGPT. 
In this blog post we will rather address whether it is a good idea to use ChatGPT as a source for scientific knowledge. 

## Geometrical Thinking

Here the idea is to see if GPT can reason geometrically in an idealized environment. Because GPT is a generative model it is possible to try the same prompt several times and get different answers. 

<div class="d-flex justify-content-center">
  <div>{% responsive_image path: assets/img/DALLE_sphere.jpeg title: "example image" class: "img-fluid rounded z-depth-1" %}</div>
</div>
<div class="caption">
    DALLE when prompted "2 ants crawling on a sphere drawing a circle digital art"
</div>

Prompt: Say we have two ants crawling on the sphere in the opposite directions. How many times can they meet if they keep crawling forward?

First Response:
<blockquote>
Ants crawling on the surface of a sphere will never meet if they keep crawling forward in opposite directions because the surface of a sphere is a two-dimensional surface with no endpoints. This means that no matter how far the ants crawl, they will never reach the end of the surface of the sphere and will never meet.
</blockquote>

Analysis: Of course this response can be easily rejected if one has an image of the sphere in their mind. In full disclosure, this is not the most common response one gets from GPT with this kind of prompt, yet it is somewhat concerning (you should repeat the same query in multiple independent chats to get truly independent responses)

Second Response:
<blockquote>
It is possible for the ants to meet an infinite number of times if they keep crawling in opposite directions on the sphere. This is because the sphere is a closed surface and has no boundaries, so the ants can continue moving indefinitely without reaching the end of the sphere.

If the ants start at opposite points on the sphere and crawl in opposite directions, they will eventually meet at the point exactly opposite their starting points. They can then continue crawling and meet again at the point opposite their second meeting, and so on. This pattern will repeat indefinitely as long as the ants keep crawling...
</blockquote>

Analysis: This response starts in a way that could be appreciated by the likes of Magellan. But the second paragraph is a bit odd, since from opposite ends it is not well defined what "opposite directions" mean. When asked what it meant, GPT responded that the ants could be moving in the clockwise and counterclockwise directions around the circumference of a sphere (great circle). Then the response ignores the ants shall meet midway, prior to reaching the opposite ends (exchanging places). 

GPT fails quite often when dealing with geometric problems, but this prompt distills the issues that can be appreciated by the general public.  We note that ChatGPT is not the most powerful NLP model, e.g. it is smaller than GPT-3.5 and has been specifically optimized for rapid responses and chat format conversations.  Can these responses be fixed by a bigger model than ChatGPT and more reinforcement learning? Probably. But is there some systemic issue in the specific approach to NLP that OpenAI has taken that could prevent these larger models from producing nonsense in more complex problems?

## Quantum vs Classical

There are many references online where ChatGPT is asked to solve physics problems. Sometimes it gives the right solution, sometimes it is wrong. But here, instead, we would like to concentrate on conceptual questions that are perhaps better suited for procedural text generation. We are trying to see whether GPT can communicate how scientists understand the world through different theories. The point is that when physicists explain a certain phenomena they use theories that are adapted to the problem. For instance, when studying propagation of radio waves in the atmosphere quantum theory is often too complex and unnecessary and wave theory is sufficient. On the other hand, explanation of photoeffect rests on corpuscular nature of light. One crucial aspect of light which relates to the quantum nature is its the relationship between the energy of photons and their frequency. Classical theory ignores this dependence and there are many macroscopical processes where this relationship is irrelevant.

Prompt:  Is it true that energy of an electromagnetic wave is directly proportional to its frequency based on just classical theory of electromagnetism that does not take quantum effects into account?

<blockquote>
Yes, that is correct. The relationship between the frequency and energy of an electromagnetic wave is described by classical electromagnetism, which does not take into account the quantization of energy that is described by quantum mechanics. In classical electromagnetism, an electromagnetic wave is described as an oscillating electric and magnetic field that propagates through space at the speed of light. The energy of the electromagnetic wave is related to the intensity of the electric and magnetic fields, which is directly proportional to the frequency of the wave. This is described by the equation E = hf, where E is the energy of the photon, f is its frequency, and h is a constant known as Planck's constant...
</blockquote>

Analysis: The correct answer is: NO, in pre-quantum classical theory there is no such relationship between energy of the EM wave and frequency, in fact h - Planck constant, comes from quantum mechanics. We have continued discussion with GPT trying to nudge it to acknowledge the mistake it had made. Eventually, GPT acknowledged that E = hf is fundamentally quantum and agreed that in classical EM theory energy depends only on the square of the amplitude, however in that same response it continued to support linear dependence between the amplitude and the frequency, which somehow still gave it linear (!) dependence between the energy and the frequency.  I would call this phantom dependence because it is likely that GPT has so much belief in the linear relationship between the energy and the frequency because of the countless sources it was trained on that repeat it and reinforce the belief. It is not willing to give up this proportionality in the classical physics context even after agreeing that the source of it is quantum. <d-footnote> Astute reader will also notice a simple mathematical error: if, as correctly stated by GPT, in classical EM theory energy scales proportional to the square of the amplitude and assuming, as GPT insists, that dependence between the energy and the frequency must be linear then it follows that amplitude must scale as the square root of frequency. To be more precise quantum mechanics suggests E = N hf where N is the number of quanta (photons, corpuscules of light), so it is not necessary to have Energy scale as square root of the frequency, because N could compensate this effect. The bottom line is that if in classical EM the relationship between Energy and frequency was already linear, Einstein wouldn't need to resurrect corpuscules of light after a century of oblivion to explain photoeffect</d-footnote>. 

## Faking references

Inspired by an [article that was written by GPT 3](https://hal.science/hal-03701250/document), we asked GPT to generate the list of highly cited papers in the interface between physics and machine learning, and it generated the list, where some papers were fake. But a few were correct, except one had a slightly wrong title. We started arguing with GPT that that paper might have a wrong title. At first GPT was adamant it did not make a mistake, but after we suggested the correct title to the machine it agreed that the suggested title was actually the right one and apologized. Then we tried to play an opposite game and picked the paper (say #2) that GPT had previously assigned the correct title, but we looked up similar sounding paper (call it #3) with the same author and suggested that #2 should actually have a title of #3 . We were able to convince GPT that it was wrong (incorrectly) and hence make it produce a fake citations which was a mixture of the two papers: essentially paper #2 with the title #3. 

<div class="d-flex justify-content-center">
  <div>{% responsive_image path: assets/img/GPT_typing.jpeg title: "example image" class: "img-fluid rounded z-depth-1" %}</div>
</div>
<div class="caption">
    DALLE when prompted "photo of a robot typing in a library"
</div>

The  issue of fake citations has also been noticed by other [users](https://news.ycombinator.com/item?id=33841672) and [researchers](https://blogs.egu.eu/divisions/np/2023/01/03/can-artificial-intelligence-replace-scientists-to-explain-climate-change-find-it-out-in-our-first-interview-to-chatgpt/?fbclid=IwAR2w_Fld_3gIpxxqFzsym00eoHiSYc-7bt0nDtnDaIbKkkW_UFrtv6dtQJ8) and it seems to be endemic to ChatGPT due to its [transformer](https://towardsdatascience.com/transformers-89034557de14) architecture. Basically when the contextual information is scarce in the common crawl on which ChatGPT was trained on, the ouput can be non-factual. Perhaps, the issue with fake citations could be fixed later, either by restricting ChatGPT or somehow creating an interfrace between it and Google Scholar, but one wonders if the same could be said about other types of scarce data questions. The problem is that ChatGPT itself is not aware that it lacks sufficient training to respond. This issue is a fundamental problem of deep learning that is a current research topic. 

We should note that other versions of NLP have been used for meta studies more effectively, such as [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) in <d-cite key="zaki22"></d-cite>, so NLP, in general, is viewed as a promising tool.

## Writing code

While we have tested ChatGPT on its coding capabilities there is not much we can add to the conversation around this subject other than the one that is already available online. Yes, it can be helpful and even sometimes combine its mathematical/physical insight with the code for more abstract questions unlike Google or Stack Exchange, although given our previous sections one should be careful when blindly using the tool. The chatbot frequently makes small mistakes in the code, but when given the error message often comes up with the right solutions such as missing dependencies. Developing large code seems unfeasible also due to restrictions on output as well as the fact that ChatGPT may only retain around 3000 words in a given conversation. However, there are actually premium products trained specifically as coding assistants, sometimes free for students, which poses questions <d-cite key="ansley22"></d-cite> about how academia should adapt to these changes. 

## Conclusions

We have concentrated on scientific queries which GPT answers gladly and is thus one of the intended uses. Our impression is that given a simple question, such as "explain how an internal combustion engine works" the generated response will be mostly reliable and, as has been advertized extensively, can be given a humorous style. But once the user asks to clarify some basic concepts there can be issues. Thus our overall assessment is that the system exhibits apparent expertise at a first glance and thus could lull users into trusting it too much in its current state. To its credit, OpenAI does indicate that the chatbot can be fallible. Another thing that could be improved is when discussing science with ChatGPT it would be nice if it could apprehend the amount of expertise of the interrogator. In other words, if it could better adapt given the prompt to the level of knowledge of the human who is asking the questions. When one talks with someone who displays knowledge relevant for the topic, one adjusts the level of the difficulty: know your audience.

The toxic responses of the chatbot have been suppressed, it avoids talking about existing people, or responding to questions about how to make Molotov cocktails. For instance, impersonating a political leader who would criticize a current or a recent one will be flat out refused. However there are still ways of getting around the barriers (erected by OpenAI) by carefully wording the prompt, especially in the story mode, which reveal the inherent biases present in the training data. See the tweet post below on apparent sexism:

{% twitter https://twitter.com/spiantado/status/1599462375887114240 %}

So why create and release ChatGPT? On Open AI websites one finds the plans to deploy these types of technologies as more intelligent versions of chatbots for customer support, help automate copywriting, etc. Clearly, code-writing assistants are a welcome development. These are quite realistic applications given the scope of ChatGPT, and perhaps the public release is mostly motivated as a publicity stunt or further attempts to eliminate harmful content. On the other hand, there could be larger overarching goals, such as future development of true general purpose AI, a kind of all-knowing machine one could refer to for any questions scientific or not: is such a machine possible? If not then why?

To summarize, whether the issues we identified are just related to the scale of GPT, or the training protocol, or even the architecture the future will show. One may wonder to what extent  an artificial agent can learn the representation of the world from only textual information, however long. Thus it is perhaps not surprising, that ChatGPT impressed us more with its understanding of human psychology than geometry. Nevertheless, it seems that we will see very soon more apt intelligent assistants, perhaps even disruptive changes in the market and, hopefully, some new scientific tools.
