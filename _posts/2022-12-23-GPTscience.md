---
layout: distill
title: ChatGPT and scientific questions
description: Discussions with ChatGPT on reconnection and photocatalysis
date: 2022-10-29

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
  - name: Simple logic
  - name: Photocatalysis

# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
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

---

**NOTE:**
This blog post contains discussions we had with [ChatGPT](https://chat.openai.com/).

## ChatGPT overview

<blockquote>
    A curse of science, dark catalysis doth harness the power of the shadows, turning them into a force for ill. When a substance is shielded from the radiance of the sun, it doth absorb the energy of the darkness, causing chemical reactions to occur. These reactions can create harmful substances, contaminating the air and water and making them polluted and toxic once more. A horror to behold, dark catalysis doth bring the ugliness of nature and the horrors of science together, working in disharmony to ruin the world.
    —Chat GPT3 when prompted to ``produce an opposite text to a description of photocatalysis in the style of Shakespeare''
</blockquote>
 
Of course, we could have generated a prompt to let [Chat GPT](https://en.wikipedia.org/wiki/ChatGPT) explain itself, the reader is welcome to try asking it themselves. I am assuming that the reader is familiar with ChatGPT (which has public access as of now). If not, check out this website [ChatGPT](https://openai.com/blog/chatgpt/). The important point to retain is that <d-cite key="ouyang2022training"></d-cite> it is based on attention mechanism of [transformers](https://towardsdatascience.com/transformers-89034557de14) that are fine-tuned with the help of user judges based on a technique called [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) to generate more reliable responses and eliminate apparent bias and harmful content. The public release of ChatGPT attracted widespread interest with a mix of awe, surprise, doubts and criticism. In this blog post our goals are to explore the capabilities of ChatGPT, after testing its responses for several weeks after the release. We are not affiliated with GPT and do not currently work on Natural Language Processing (NLP). Nevertheless, we are domain specailists of our respective disciplines and will try to provide relevant criticism of GPT responses.

Generally, it seems that ChatGPT is advanced word processor and usually does a good job of summarizing the topic. It can also engage in conversations, where it is able to recall previously discussed topics, invent stories, participate in games, create synthetic dialogs between famous people from the past, write code, solve simple math problems. Often the user is impressed by the overall performance of ChatGPT, which gives an impression of general intelligence, until one runs into really embarassing nonsence that ChatGPT may generate, especially when reasoning is involved, but more on this later. We note that ChatGPT is not the most powerful NLP model, e.g. it is smaller than GPT-3.5 and has been specifically optimized for rapid responses and chat format conversations. 

There are concerns about the applications of this technology for generation of high quality fake news, automating internet troll farms etc. For instance, in a discussion over [WebSummit](https://youtu.be/PBdZi_JtV4c) a famous linguist and public speaker Noam Chomsky harshly criticized GPT for this reason, but he also expressed thorough criticism of this approach to Natural Language Processing. This is not surprising, given a contrarian character of Noam Chomsky and his view on inherent nature of grammar in humans. In other interviews available online he has expressed similar concerns on these black-box approaches that, in his words, ignore theoretical understanding of how language works. Interestingly, in one of our prompts, when asked how Noam Chomsky would react to GPT developments, ChatGPT hypothesized that the esteemed MIT professor would find GPT success an interesting tool in better understanding human languages. 

So why create and release ChatGPT? One finds on Open AI websites that they are planning to deploy these types of technologies as more intelligent versions of chatbots for customer support, help automate copywriting, etc. Clearly, code-writing assitants are weolcome development. These are quite realistic applications given the scope of ChatGPT, and perhaps the public release is mostly motivated as a publicity stunt. On the other hand, there could be larger overarching goals, such as future development of true general purpose AI, a kind of all-knowing machine one could refer to for any questions scientific or not: is such a machine possible? If not then why? One way or the other, it could be interesting to test how the GPT reacts to unexpected inputs provided by millions of users. 

Below we give assessment of the ChatGPT responses to two such users, us. It will be interesting to check how the responses of ChatGPT and similar chatbots evolve in future, thus the readers are encouraged to try repeating these experiments. Broadly speaking, ChatGPT can write stories, and it is impressive that we finally have an AI capable of responding correctly to quieries, ignoring orthographic mistakes (even word order), remembering earlier parts of the conversation and incorporating them into its responses. With that being said, there is a certain point at which one gets bored with the stories the machine writes, they tend to be quite stereotypical and lack new unexpected fitting narratives that the reader would appreciate. The language can be also poor, e.g. the constant repetition of phrases like ``cannot help but''. 

Here we will concentrate more on scientific quieries which GPT answers gladly and is thus one of the intended uses. OpenAI does indicate that the chatbot can be fallible. Our impression is that given a simple question, such as "explain how internal combustion engine works" the generated response will be mostly reliable. But once the user asks to clarify some basic concepts there can be issues. Whether these issues are just related to scale of GPT, or the training protocol, or even the architecture is not clear. One may wonder to what extent can an artificial agent learn the representation of the world from only textual information, however long, and some nudging by the judges that is allegedly mostly eliminating harmful content. Thus it is perhaps not surprising, that ChatGPT excelled more when it came to understanding human psychology (in our judgement) than math or physics. 

## Simple logic

**Note:** Below we will give more clear explanation 

## Photocatalysis
