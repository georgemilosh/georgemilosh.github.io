---
layout: distill
title: Tensorflow tutorial for Physics Inspired Neural Networks
description: Some notes that explain how PINNs are implemented in tensorflow
date: 2022-10-29

authors:
  - name: George Miloshevich
    url: "georgemilosh.github.io"
    affiliations:
      name: LSCE, CEA Saclay
 
 - name: Alisa Ranscht
    affiliations:
      name: Université Lyon 1


# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: GPT3 overview
  - name: Magnetic reconnection
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
This blog post contains discussions we had with  [ChatGPT](https://chat.openai.com/).


## GPT3 overview

<blockquote>
    A curse of science, dark catalysis doth harness the power of the shadows, turning them into a force for ill. When a substance is shielded from the radiance of the sun, it doth absorb the energy of the darkness, causing chemical reactions to occur. These reactions can create harmful substances, contaminating the air and water and making them polluted and toxic once more. A horror to behold, dark catalysis doth bring the ugliness of nature and the horrors of science together, working in disharmony to ruin the world.
    —Chat GPT3 when prompted to produce an opposite text to a description of photocatalysis in the style of Shakespeare
</blockquote>
 

Prompt: What is ChatGPT, how does it work and how is it different from GPT3?

<d-code block>
  ChatGPT is an open-source language model developed by OpenAI that is specifically designed for text-based conversational applications. It can be used to generate human-like text responses to prompts in real-time, making it ideal for use in chatbots, virtual assistants, and other conversational AI applications. ChatGPT is trained on a large dataset of human conversation, allowing it to understand and respond to natural language input in a way that is similar to how a human would. It can be used to create engaging and seamless conversational experiences for users in a variety of contexts, from customer service to language translation to entertainment.
</d-code>



***

## Magnetic reconnection



<d-code block language="python">
  # Import TensorFlow and NumPy
  import tensorflow as tf
  import numpy as np
  
  # Set data type
  DTYPE='float32'
  tf.keras.backend.set_floatx(DTYPE)
</d-code>

**Note:** Below we will give more clear explanation 

## Photocatalysis

<d-code block language="python">
  # Import TensorFlow and NumPy
  import tensorflow as tf
  import numpy as np
  
  # Set data type
  DTYPE='float32'
  tf.keras.backend.set_floatx(DTYPE)
</d-code>


