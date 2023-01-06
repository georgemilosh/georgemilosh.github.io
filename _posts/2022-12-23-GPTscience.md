---
layout: distill
title: ChatGPT and scientific questions
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
  - name: The ants on the sphere
  - name: Why is the sky blue
  - name: Faking references
  - name: Photocatalysis
  - name: Conclusions

---

**NOTE:**
This blog post contains discussions we had with [ChatGPT](https://chat.openai.com/).

## ChatGPT overview
 
Of course, we could have generated a prompt to let [Chat GPT](https://chat.openai.com) explain itself, but anyone can do it at this point. I am assuming that the reader is familiar with ChatGPT (which has public access as of now). If not, check out this [website](https://openai.com/blog/chatgpt) . The important point to retain is that <d-cite key="ouyang2022training"></d-cite> it is based on attention mechanism of [transformers](https://towardsdatascience.com/transformers-89034557de14) that are fine-tuned with the help of user judges based on a technique called [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) to generate more reliable responses and eliminate apparent bias and harmful content. The public release of ChatGPT attracted widespread interest with a mix of awe, surprise, doubts and criticism. In this blog post our goals are to explore the capabilities of ChatGPT, after testing its responses for several weeks after the release. We are not affiliated with its creators at Open AI and do not currently work on Natural Language Processing (NLP). Nevertheless, we are domain specialists of our respective disciplines and will try to provide relevant criticism of GPT responses.

Generally, it seems that ChatGPT usually does a good job of providing simple explanations on variaty of topics, even as it has to impersonate a pirate as requested. It can also engage in conversations, where it is able to recall previously discussed topics and invent stories: see psychological [drama](https://georgemilosh.github.io/blog/2022/GPTstory) it told to us. GPT can also participate in games, create synthetic dialogs between famous people from the past, write code, solve simple math problems (often incorrectly). At first, the user is impressed by the overall performance of ChatGPT, which gives an impression of general intelligence, until one runs into really embarassing nonsence that the chatbot may generate, especially when reasoning is involved, but more on this later. We note that ChatGPT is not the most powerful NLP model, e.g. it is smaller than GPT-3.5 and has been specifically optimized for rapid responses and chat format conversations. 

There are concerns about the applications of this technology for generation of high quality fake news, automating internet troll farms etc. For instance, in a discussion over [WebSummit](https://youtu.be/PBdZi_JtV4c) a famous linguist and public speaker Noam Chomsky harshly criticized GPT for this reason, but he also expressed thorough criticism of this approach to NLP This is not surprising, given a contrarian character of Noam Chomsky and his now contraversial work on universal grammar that is inherent in humans. Interestingly, in one of our prompts, when asked how Noam Chomsky would react to GPT developments, ChatGPT hypothesized that the esteemed MIT professor would find GPT success an interesting tool for better understanding human languages. 

So why create and release ChatGPT? On Open AI websites one finds the plans to deploy these types of technologies as more intelligent versions of chatbots for customer support, help automate copywriting, etc. Clearly, code-writing assitants are welcome development. These are quite realistic applications given the scope of ChatGPT, and perhaps the public release is mostly motivated as a publicity stunt. On the other hand, there could be larger overarching goals, such as future development of true general purpose AI, a kind of all-knowing machine one could refer to for any questions scientific or not: is such a machine possible? If not then why? One way or the other, it could be interesting to test how the GPT reacts to unexpected inputs provided by millions of users. Below we give assessment of the ChatGPT responses to two such users, us. The quieries we provide could be also tried at a later time to see how the system progresses in future. Our overall assessment is that the system exhibits apparanet expertise at a first glance and thus could lull users into trusting it too much. 

## The ants on the sphere

We start with a simple thought experiment most people can do, however it requires some geometrical thinking.

Prompt: There are two ants on a black sphere. The ants start at the same point on the surface. They pick red and blue brushes respectively and walk in the opposite directions in what appears to them as straight lines while painting their path with their brushes. How will the sphere look after infinite time. Note: when blue and red are combined you get purple

<blockquote>
Answer: After an infinite amount of time, the sphere will be completely painted either blue or red, depending on which ant was faster. The ants will never meet because they are walking in opposite directions on the surface of a sphere, which is a two-dimensional surface that has no end. As a result, they will never be able to paint over each other's tracks, and the sphere will remain either completely blue or completely red. It's important to note that this scenario is purely theoretical and would not be possible in the real world due to the constraints of time and resources.
</blockquote>

Analysis: This is of course incorrect and can even be unpleasant to read because it involves multiple fallacies and perhaps demonstrates that GPT does not have an image of a sphere, not surprisingly. what is interesting is that when similar questions are tried again GPT is occasionally responding that the ants do meet - a response that would be appreciated by the likes of Magellan. After some additional interrogation GPT later suggests that the ants shall never meet because they travel along great circles, but great circles divide the sphere in two hemispheres. Because the ants travel in the opposite directions it concludes that the ants end up in different hemispheres. So you can see a kind of reasoning, although a faulty one, which confuses the relationship between the key words in these sentences. Now, is this the reason the response quoted above was produced? It is certainly very tempting and could be true but who knows: it could be that ChatGPT is just trying to explain away its decision that the ants don't meet. 

**Note:** We provide the full transcript here

## Why is the sky blue

Originally we were interested in asking the question corresponding to the title of this section, but we think the following related question is more simple and more easily conveys the issues GPT runs into.

Prompt:  Is it true that energy of an electromagnetic wave is directly proportional to its frequency based on just classical theory of electromagnetism that does not take quantum effects into account?

<blockquote>
Yes, that is correct. The relationship between the frequency and energy of an electromagnetic wave is described by classical electromagnetism, which does not take into account the quantization of energy that is described by quantum mechanics. In classical electromagnetism, an electromagnetic wave is described as an oscillating electric and magnetic field that propagates through space at the speed of light. The energy of the electromagnetic wave is related to the intensity of the electric and magnetic fields, which is directly proportional to the frequency of the wave. This is described by the equation E = hf, where E is the energy of the photon, f is its frequency, and h is a constant known as Planck's constant...
</blockquote>

Analysis: The correct answer is: NO, as is known to any physicist who ever had a course of electromagnetism, in classical mechanics there is no such relationship between energy of the EM wave and frequency, in fact h - Planck constant, comes from quantum mechanics. We have continued discussion with GPT trying to nudge it to ackwnoledge the mistake it had made. Eventually, GPT ackwnoledged that E = hf is fundamentally quantum and agreed that in classical EM theory energy depends only on the square of the amplitude, however in that same response it continued to support linear dependence between the amplitude and the frequency, which somehow still gave it linear (!) dependence between the energy and the frequency.  I would call this phantom dependence because it is likely that GPT has so much belief in the linear relationship between the energy and the frequency because of the countless sources it was trained on that repeat it and reinforce the belief, which prompts GPT to spit out two logically inconsistent statements <d-footnote> Astute reader will also notice a simple mathematical error: if the dependence between the energy and the frequency must be linear and as correctly stated in classical EM theory energy scales proportional to the square of the amplitude, amplitude must scale as the square root of frequency. Also from quantum mechanics it is known that E = hf can be essentially masked by the number of quanta (photons), so it is not necessary to have Energy scale as square root of the frequency. The bottom line is that if in classical EM the relationship between Energy and frequency was already linear, Einstein wouldn't need to ressurect corpuscules of light after a century of oblivion </d-footnote>. Granted, the wave-particle duality is one of the most complex, even philosophical, issues that has tormented physics students and alike.

**Note:** We provide the full transcript here

## Faking references

We asked GPT to generate the list of highly cited papers in the interface between physics and machine learning, and it generated the list, where some papers were fake. But a few were correct, except one had slightly wrong title. We started arguing with GPT that that one might have a wrong title, it was not agreeing, then we suggested the correct title and then once GPT was given the right title it agreed that the title we suggested was the actually right one and apologized. Then we tried to play an opposite game and picked the paper that GPT assigned the correct title, but we looked up similar sounding paper with the same author. We were able to convince GPT that it was wrong and hence make it produce a fake citations which was a mixture of the two papers: mixing the titles and journals. This issue that has also been noticed by other [users](https://news.ycombinator.com/item?id=33841672) and [researchers](https://blogs.egu.eu/divisions/np/2023/01/03/can-artificial-intelligence-replace-scientists-to-explain-climate-change-find-it-out-in-our-first-interview-to-chatgpt/?fbclid=IwAR2w_Fld_3gIpxxqFzsym00eoHiSYc-7bt0nDtnDaIbKkkW_UFrtv6dtQJ8) seems to be endemic to ChatGPT due to its transformer architecture. Basically when the contextual information is scarce in the `common crawl` on which ChatGPT was trained on, the ouput can be non-factual. The issue with fake citations could be fixed later, by morphing Google and ChatGPT capabilities, but one wonders if the same could be said about other types of scarce data questions. The problem is that ChatGPT itself is not aware that it lacks sufficient training to respond. 

## Photocatalysis

## Conclusions

Broadly speaking, ChatGPT can write stories, poems and it is impressive that we finally have an AI capable of responding to queries, ignoring orthographic mistakes (even word order), remembering earlier parts of the conversation and incorporating them into its responses. However, there is a certain point at which one gets bored with the literary stories the machine writes, they tend to be quite stereotypical and lack new unexpected fitting narratives that the reader would appreciate. The language can be also less rich, e.g. the constant repetition of phrases like ``cannot help but'' becomes annoying.  

We have concentrated on scientific queries which GPT answers gladly and is thus one of the intended uses. Our impression is that given a simple question, such as "explain how internal combustion engine works" the generated response will be mostly reliable and, as has been advertized extensively, can be given a flavor of a pirate or mobster narrator which can be entertaining. But once the user asks to clarify some basic concepts there can be issues. To this we add the unpleasant experience we had of asking GPT to cite/review articles, which at best produces small inaccuracies but usually consists of completely made up content which is based on the prompt of the user and mixture of existing articles. To their credit, OpenAI does indicate that the chatbot can be fallible. Naturally, an all-purpose agent such as ChatGPT is not ideally suited for such questions and it could more appropriate to use some specific NLP model trained to help researchers sort out papers.

To summarize, whether these issues are just related to the scale of GPT, or the training protocol, or even the architecture the future will show. One may wonder to what extent can an artificial agent learn the representation of the world from only textual information, however long, in addition to some nudging by the judges that is allegedly mostly eliminating harmful content. Thus it is perhaps not surprising, that ChatGPT impressed us more with its understanding of human psychology than math or physics. Nevertheless, it seems that we will see very soon more apt home assistants and more human-like chatbots.