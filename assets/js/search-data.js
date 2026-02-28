// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-talks",
          title: "talks",
          description: "Talks at conferences and beyond, click `abs` to read abstract, `media` to watch the talk, `slides` to view the pdf of the presenatation etc.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/talks/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "my publications. here you can also view abstracts, pdfs, slides... etc",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "A growing collection of your cool projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "dropdown-repositories",
              title: "repositories",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/repositories/";
              },
            },{id: "dropdown-teaching",
              title: "teaching",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/teaching/";
              },
            },{id: "post-ai-in-space-weather",
        
          title: "AI in Space Weather",
        
        description: "Scientific Outlooks for the Analysis of Space Weather Data in the Age of AI",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/TDM-ESWW/";
          
        },
      },{id: "post-whamp-tutorial-for-plasma-wave-dispersion-analysis",
        
          title: "WHAMP Tutorial for Plasma Wave Dispersion Analysis",
        
        description: "A comprehensive guide to using WHAMP for studying plasma instabilities with Python automation",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/whamp/";
          
        },
      },{id: "post-what-39-s-up-with-climate",
        
          title: "What&#39;s up with climate",
        
        description: "what I have learned from climate scientists",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/climate/";
          
        },
      },{id: "post-on-data-driven-equation-discovery",
        
          title: 'On Data-Driven Equation Discovery <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.open("https://medium.com/data-science/on-data-driven-equation-discovery-5069795d239d?source=rss-e846787fbdef------2", "_blank");
          
        },
      },{id: "post-deep-learning",
        
          title: "Deep learning",
        
        description: "useful resources for practical tutorials on deep learning",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/deep-learning/";
          
        },
      },{id: "post-chatgpt-on-scientific-questions",
        
          title: "ChatGPT on scientific questions",
        
        description: "Discussions with ChatGPT on science",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/GPTonscience/";
          
        },
      },{id: "post-chatgpt-on-manipulative-gpt",
        
          title: "ChatGPT on manipulative GPT",
        
        description: "psychological drama of a person talking to GPT",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/GPTstory/";
          
        },
      },{id: "post-tensorflow-tutorial-for-physics-informed-neural-networks",
        
          title: "Tensorflow tutorial for Physics Informed Neural Networks",
        
        description: "Some notes that explain how PINNs are implemented in tensorflow",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2022/distill/";
          
        },
      },{id: "post-our-work-presented-at-aps-dfd",
        
          title: "Our work presented at APS DFD",
        
        description: "Freddy Bouchet presents our work on learning how to predict heatwaves from data at APS DFD 2021",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2021/twitter/";
          
        },
      },{id: "post-academic-diagrams",
        
          title: "academic diagrams",
        
        description: "how to make pretty latex diagrams",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2015/diagrams/";
          
        },
      },{id: "post-standard-nontwist-map",
        
          title: "Standard Nontwist Map",
        
        description: "how to turn great science into art",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2015/images/";
          
        },
      },{id: "news-moving-to-france-sparkles-smile",
          title: 'Moving to France! 🇫🇷 🥐 🗼 🥖 :sparkles: :smile:',
          description: "",
          section: "News",},{id: "news-our-work-presented-at-aps-dfd",
          title: 'Our work presented at APS DFD!',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-moved-to-lsce-near-paris",
          title: 'Moved to LSCE near Paris',
          description: "",
          section: "News",},{id: "news-cnrs-promotes-our-prf-paper",
          title: 'CNRS promotes our PRF paper',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_4/";
            },},{id: "news-i-am-pleased-to-announce-that-i-started-a-position-of-project-manager-of-automatics-of-space-exploration-asap",
          title: 'I am pleased to announce that I started a position of Project Manager...',
          description: "",
          section: "News",},{id: "news-fwo-project-helioskill-is-looking-for-2-1-year-postdoc-s",
          title: 'FWO Project HELIOSKILL is looking for (2+1 year) postdoc(s)',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_7/";
            },},{id: "news-good-news-project-stride-was-awarded-5m-cpu-and-16k-gpu-hours-by-the-flemish-supercomputer-center-funded-by-the-research-foundation-flanders-fwo-and-the-flemish-government-department-ewi",
          title: 'Good news! Project STRIDE was awarded 5M CPU and 16k GPU hours by...',
          description: "",
          section: "News",},{id: "news-we-are-organizing-a-memorial-workshop-in-memory-of-giovanni-lapenta-at-ku-leuven-details-and-rsvp-amp-gt",
          title: 'We are organizing a memorial workshop in memory of Giovanni Lapenta at KU...',
          description: "",
          section: "News",},{id: "news-announcing-erc-starting-grant-award-d-surge-project",
          title: 'Announcing ERC Starting Grant Award (D-SURGE project)',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_ERC/";
            },},{id: "news-workshop-at-ku-leuven-for-on-board-ai-applications-october-7-details-and-rsvp-amp-gt",
          title: 'Workshop at KU Leuven for on-board AI applications, October 7: details and RSVP...',
          description: "",
          section: "News",},{id: "news-topical-discussion-meeting-at-esww-held-details-in-the-blog-post",
          title: 'Topical discussion meeting at ESWW held, details in the blog post.',
          description: "",
          section: "News",},{id: "projects-turbulence-in-plasmas",
          title: 'Turbulence in Plasmas',
          description: "Inverse cascade in gyrofluids",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-climate-learning",
          title: 'Climate-Learning',
          description: "Deep learning for Climate",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-equation-discovery",
          title: 'Equation Discovery',
          description: "Data-driven equation discovery",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-translating-khanacademy",
          title: 'Translating Khanacademy',
          description: "A time when I translated couple of videos into russian",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-asap",
          title: 'ASAP',
          description: "Automatics of SpAce exPloration",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project_asap/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%67%65%6F%72%67%65%64%6F%74%6D%69%6C%6F%73%68%65%76%69%63%68%61%74%6B%75%6C%65%75%76%65%6E%64%6F%74%62%65", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0001-9896-1704", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=QMFVv0AAAAAJ", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/georgemilosh", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/george-miloshevich-2b834212a", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/george_milosh", "_blank");
        },
      },{
        id: 'social-medium',
        title: 'Medium',
        section: 'Socials',
        handler: () => {
          window.open("https://medium.com/@georgemilosh", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
