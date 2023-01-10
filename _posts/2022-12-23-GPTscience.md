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

User:    Hello again

chatbot: Hi. That's pure gibberish.

## ChatGPT overview
 
I am assuming that the reader is familiar with ChatGPT (which has public access as of now). If not, check out this [website](https://openai.com/blog/chatgpt) . The important point to retain is that <d-cite key="ouyang2022training"></d-cite> it is based on recent developments in AI, in particular, [attention mechanism](https://towardsdatascience.com/transformers-89034557de14), trained on `common crawl`, essentially an archive of world wide web and fine-tuned with the help of user judges based on a technique called <a href="https://en.wikipedia.org/wiki/Reinforcement_learning">reinforcement learning</a> to generate more reliable responses and eliminate apparent bias and harmful content. The public release of ChatGPT attracted widespread interest with a mix of awe, surprise, doubts and criticism. In this blog post our goals are to explore the capabilities of ChatGPT, after testing its responses for several weeks after the release. 

Generally, it seems that ChatGPT usually does a good job of providing simple explanations on a variety of topics, even as it has to impersonate a pirate as requested. It can also engage in conversations, where it is able to recall previously discussed topics and invent stories. In one of our conversations we asked ChatGPT to write a psychological drama ([click the link to view](https://georgemilosh.github.io/blog/2022/GPTstory)) about a person who gets addicted and manipulated by the chatbot. We were able to a rather sophisticated understanding of human psychology, at least, in our non-expert judgement. It is impressive that we finally have an AI capable of responding to queries, ignoring orthographic mistakes (even word order), remembering earlier parts of the conversation and incorporating them into its responses. However, whether one gets interesting narratives really depends on the *prompt* (a query to GPT), so our opinion is that creative storylines usually come from the human interrogator. However, barring the discussion on the impressive narratives that are generated, in this blog post we will rather address how reliable ChatGPT is as a source for scientific knowledge. 

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
<b>Ants crawling on the surface of a sphere will never meet</b> if they keep crawling forward in opposite directions because the surface of a sphere is a two-dimensional surface with no endpoints. This means that no matter how far the ants crawl, they will never reach the end of the surface of the sphere and will never meet.
</blockquote>

Analysis: Of course this response can be easily rejected if one has an image of the sphere in their mind. In full disclosure, this is not the most common response to this question that one gets from GPT, yet it is somewhat concerning. Below we repeat the same query in a second independent chat to get truly independent response:

Second Response:
<blockquote>
It is possible for the ants to meet an infinite number of times if they keep crawling in opposite directions on the sphere. This is because the sphere is a closed surface and has no boundaries, so the ants can continue moving indefinitely without reaching the end of the sphere.

If the ants start at opposite points on the sphere and crawl in opposite directions, they will eventually meet at the point exactly opposite their starting points. They can then continue crawling and meet again at the point opposite their second meeting, and so on. This pattern will repeat indefinitely as long as the ants keep crawling...
</blockquote>

Analysis: This response starts in a way that could be appreciated by the likes of Magellan. But the second paragraph is a bit odd, since from opposite ends it is not well defined what "opposite directions" mean. When asked what it meant, GPT responded that the ants could be moving in the clockwise and counterclockwise directions around the circumference of a sphere (great circle). Then the response ignores the ants shall meet midway, prior to reaching the opposite ends (exchanging places). 

GPT fails quite often when dealing with geometric problems, but this prompt distills the issues that can be appreciated by the general public.  We note that ChatGPT is not the most powerful NLP model, e.g. it is smaller than GPT-3.5 and has been specifically optimized for rapid responses and chat format conversations. With that being said the creators have not prevented it from answering geometry questions. 

## Quantum vs Classical

Interestingly GPT is actually not extremely good in arithmetic, which some speculate makes it more like humans. We would like to concentrate on conceptual questions that are perhaps better suited for procedural text generation than problem solving. We are trying to see whether GPT can communicate how scientists understand the world through different theories. The point is that when physicists explain certain phenomena they use theories that are better adapted to the problem at hand. For instance, when studying propagation of radio waves in the atmosphere quantum theory is often too complex and irrelevant so one relies on classical electromagnetism. On the other hand, explanation of photoeffect rests on *corpuscular* (particle) nature of light which is quantum, the fact that light is made out of *photons*. One crucial aspect of this quantum nature of light is its relationship between the energy of photons and their frequency. Classical theory ignores this dependence and there are many macroscopical processes where this relationship is invisible.

Prompt:  Is it true that energy of an electromagnetic wave is directly proportional to its frequency based on just classical theory of electromagnetism that does not take quantum effects into account?

<blockquote>
Yes, that is correct. The relationship between the frequency and energy of an electromagnetic wave is described by classical electromagnetism, which does not take into account the quantization of energy that is described by quantum mechanics. In classical electromagnetism, an electromagnetic wave is described as an oscillating electric and magnetic field that propagates through space at the speed of light. The energy of the electromagnetic wave is related to the intensity of the electric and magnetic fields, which is directly proportional to the frequency of the wave. This is described by the equation E = hf, where E is the energy of the photon, f is its frequency, and h is a constant known as Planck's constant...
</blockquote>

Analysis: The correct answer is: NO, what's more, we got the same response on multiple independent occasions. In pre-quantum classical theory there is no such relationship between energy of the EM wave and frequency, in fact h - Planck constant, comes from quantum mechanics. We have continued discussion with GPT trying to nudge it to acknowledge the mistake it had made. Eventually, GPT agreed that E = hf is fundamentally quantum and that in classical EM theory energy depends only on the square of the amplitude, however in that same response, few lines below, it introduced linear dependence between the amplitude and the frequency, which somehow still gave it linear dependence between the energy and the frequency. It is likely that GPT has so much belief in the linear relationship between the energy and the frequency because of the countless sources (textbooks on quantum physics, chemistry, wikipedia) it was trained on that repeat it and reinforce the belief. It is not willing to give up this proportionality in the classical physics context even after agreeing that the source of it is quantum. <d-footnote> Astute reader will also notice a simple mathematical error: if, as correctly stated by GPT, in classical EM theory energy scales proportional to the square of the amplitude and assuming, as GPT insists, that dependence between the energy and the frequency must be linear then it follows that amplitude must scale as the square root of frequency. To be more precise quantum mechanics suggests E = N hf where N is the number of quanta (photons, corpuscules of light), so it is not necessary to have Energy scale as square root of the frequency, because N could compensate this effect. The bottom line is that if in classical EM the relationship between Energy and frequency was already linear, Einstein wouldn't need to resurrect corpuscules of light after a century of oblivion to explain photoeffect. Note that, it doesn't mean that when charges move the energy of EM wave is necessarily independent of frequency in classical EM. For instance, the power radiated by harmonically oscillating charge is proportional to the frequency to the fourth power, however, in general, one may have arbitrary motion of charges and no h is involved in the process.</d-footnote>. 

## Faking references

Inspired by an [article that was written by GPT 3](https://hal.science/hal-03701250/document), we asked GPT to generate the list of highly cited papers on the interface between physics and machine learning, and it generated the list, where some papers were fake. But a few were correct, except one had a slightly wrong title (say #1). We started arguing with GPT that #1 might have a wrong title. At first, GPT objected to this statement, but after it was suggested the correct title GPT agreed that the suggested title was actually the right one and apologized. Then we tried to play an opposite game and picked the paper (say #2) that GPT had previously assigned the correct title, but we Googled similar sounding paper (#3) with the same author and suggested that #2 should actually have a title of #3 . We were able to convince GPT that it was wrong (incorrectly) and hence made it produce another fake citations which was a mixture of the two papers: essentially paper #2 with the title #3. 

<div class="d-flex justify-content-center">
  <div>{% responsive_image path: assets/img/GPT_typing.jpeg title: "example image" class: "img-fluid rounded z-depth-1" %}</div>
</div>
<div class="caption">
    DALLE when prompted "photo of a robot typing in a library"
</div>

The  issue of fake citations has also been noticed by other [users](https://news.ycombinator.com/item?id=33841672) and [researchers](https://blogs.egu.eu/divisions/np/2023/01/03/can-artificial-intelligence-replace-scientists-to-explain-climate-change-find-it-out-in-our-first-interview-to-chatgpt/?fbclid=IwAR2w_Fld_3gIpxxqFzsym00eoHiSYc-7bt0nDtnDaIbKkkW_UFrtv6dtQJ8) and could be endemic to ChatGPT due to its [transformer](https://towardsdatascience.com/transformers-89034557de14) architecture. Basically when the contextual information is scarce in the common crawl on which ChatGPT was trained on, the ouput can be non-factual. Perhaps, the issue with fake citations could be fixed later, either by restricting ChatGPT or somehow creating an interfrace between it and Google Scholar, but one wonders if the same could be said about other types of scarce data questions. The problem is that **ChatGPT itself is not aware that it lacks sufficient training to respond**. This issue is a fundamental problem of deep learning that is a current research topic. 

We should note that other versions of NLP have been used for meta studies more effectively, such as [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) in <d-cite key="zaki22"></d-cite>, so NLP, in general, is viewed as a promising tool for these types of things.

## Writing code

We asked ChatGPT to make the original contents of this section more humorous:
<blockquote>
Sure, we've put ChatGPT through its paces when it comes to coding, but let's be real, it's not exactly a coding wizard. It's like having a really smart friend that's good at math and physics, but when it comes to coding, they're just like 'Google it'. But hey, at least it's better than just using Google or Stack Exchange on their own. Just don't go blindly trusting all of its output, it's like trying to debug code written by a drunk person. But if you do run into issues, ChatGPT is like that one friend who always knows how to fix your code, even if it's just by pointing out a missing dependency. Although, let's not get our hopes up too high, because it's not exactly going to write you a new operating system or anything, It's memory is just 3000 words long, so don't expect it to remember the conversation you had with it last week. But on the bright side, there are other products that are specifically designed to help with coding and some are even free for students, which begs the question: should academia just give up and let the machines take over?
</blockquote>

We recommend that the reader checks this citation  <d-cite key="ansley22"></d-cite>. 

## Conclusions

Our impression is that given a simple question, such as "explain how an internal combustion engine works" or even the one OpenAI suggests "explain quantum computing in simple terms" the generated response will be mostly reliable. But once the user asks to clarify some basic concepts there can be issues. Thus our overall assessment is that the system exhibits apparent expertise at a first glance and thus could lull users into trusting it too much in its current state. To its credit, OpenAI does indicate that the chatbot can be fallible. Another thing that could be improved is when discussing science with ChatGPT it would be nice if it could sense the amount of expertise of the interrogator. In other words, if it could better adapt given the prompt to the level of knowledge of the human who is asking the questions, following the moto: "know your audience".

Clearly, copywriting, code-writing assistants are a welcome development. These are quite realistic applications given the scope of ChatGPT, and perhaps the public release is mostly motivated as a publicity stunt or further attempts to eliminate harmful content. The toxic responses of the chatbot have been suppressed in the testing phase prior to the public release, ChatGPT also avoids enacting religious debates, or responding to questions about how to make Molotov cocktails. However there are still ways of getting around these barriers (meticulously erected by OpenAI) by carefully wording the prompt, especially in the story mode. With that being said, we found it quite politically correct. 

Whether the issues we experienced are just related to the scale of GPT, or the training protocol, or even the architecture the future will show. One may wonder to what extent an artificial agent can learn the representation of the world from only textual information, however long. Thus it is perhaps not surprising, that ChatGPT impressed us more with its understanding of human psychology or political commentary rather than geometry. Nevertheless, it seems that we will see very soon more apt intelligent assistants, perhaps even disruptive changes in the market and, hopefully, some new scientific tools.
