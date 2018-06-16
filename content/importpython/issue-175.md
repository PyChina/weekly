Title: 蠎加载 175
Slug: importpython-175
Date: 2018-06-16 15:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 175](http://importpython.com/newsletter/no/175/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [基础 Pandas 数据分析练习 – Machine Learning Plus](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)
    + pandas

101 python pandas exercises are designed to challenge your logical muscle and to help internalize data manipulation with python’s favorite package for data analysis. The questions are of 3 levels of difficulties with L1 being the easiest to L3 being the hardest.

- [2018 Python 语言峰会](https://lwn.net/Articles/754152/)
    + community

Over the past three years, LWN and its readers have gotten a yearly treat in the form of coverage of the Python Language Summit; this year is no exception. The summit is a yearly gathering of around 40 or 50 developers from CPython, other Python implementations, and related projects. It is held on the first day of PyCon, which is two days before the main PyCon talk tracks begin. This year, the summit was held on May 9 in Cleveland, Ohio. The summit consists of a dozen or so main "talks", which are usually more open-ended and discussion-oriented, rather than simply straight presentations, and a handful of lightning talks, all of which is meant to be crammed into five hours or so. As might be guessed, spillover is inevitable; this year it went three hours beyond its appointed slot. Topics ranged all over the Python landscape: development process issues, performance ideas, deprecations of various sorts, diversity in the development community, static typing, and more.

(`是也乎:`

![group](https://static.lwn.net/images/2018/pls-group-sm.jpg)

简单说: 老爹很佛系, 发展很稳, 老鉄很兴奋

)

- [应该知道的 Python 中的 Multiprocessing vs. Multithreading](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/)
    + multiprocessing, multithreading

TLDR: If you don't want to understand the under-the-hood explanation, here's what you've been waiting for: you can use threading if your program is network bound or multiprocessing if it's CPU bound.

(`是也乎:`

    简单说面向网络上多线
    针对 CPU 就得多进

可惜...

)



- [PyNaiveChain - Python 实现 BlockChain](https://technokeeda.com/programming/python-blockchain-implementation-toy/)
    + blockchain

Blockchain has been in the news for quite sometime now Though I think it might be a little early to believe people hyping it as the next internet, it is an excellent tool for asset/ownership management. . There are a number of implementations in different languages(and in Python as well) .However there isn’t a Python BlockChain implementation which simple enough to understand while being fully functional.

- [Episode #164 Allen Institute 中用 Python 搞脑研究 - [Talk Python To Me Podcast]](https://talkpython.fm/episodes/show/164/python-in-brain-research-at-the-paul-allen-institute)
    + podcast

The brain is truly one of the final frontiers of human exploration. Understanding how brains work has vast consequences for human health and computation. Imagine how computers might change if we actually understood how thinking and even consciousness worked. On this episode, you'll meet Justin Kiggins and Corinne Teeter who are research scientists using Python for their daily work at the Allen Institute for Brain Science. They are joined by Nicholas Cain who is a software developer supporting scientists there using Python as well.

- [在 Python 中开始用 Elasticsearch](http://blog.adnansiddiqi.me/getting-started-with-elasticsearch-in-python/)
    + elasticsearch

In this post, I am going to discuss Elasticsearch and how you can integrate with different Python apps.

- [Temporal Difference Learning in Python](https://harderchoices.com/2018/06/07/temporal-difference-learning-in-python/)
    + reinforcement learning

Temporal-Difference Learning (or TD Learning) is quite important and novel thing around. It’s the first time where you can really see some patterns emerging and everything is building upon a previous knowledge. Hop in for some theory and Python code.

(`是也乎:`

    DP + MC = TD

只能说, 又一轮全新缩写袭来

)

- [Python Sets 和集合论 – Towards Data Science](https://towardsdatascience.com/python-sets-and-set-theory-2ace093d1607)
    + core-python

Learn about Python sets: what they are, how to create them, when to use them, built-in functions, and their relationship to set theory operations.

- [自动特征工程在 Python](https://towardsdatascience.com/automated-feature-engineering-in-python-99baf11cc219)
    + machine learning

How to automatically create machine learning features

(`是也乎:`

调参和多模式融合才需要人工,
传统的特征提取,真心是体力活儿而已

)


## 好物
~ 包/模块/库/片段...

- [mlflow](https://github.com/databricks/mlflow)
    - 445 Stars, 44 Fork

Open source platform for the complete machine learning lifecycle


(`是也乎:`

![mlflow](https://mlflow.org/images/MLflow-header-pic@2x.png)

生命周期?简单的说, 就是 ML 项目专业管理...

)


- [keras-applications](https://github.com/keras-team/keras-applications)
    - 143 Stars, 11 Fork

Reference implementations of popular deep learning models.

- [keras-preprocessing](https://github.com/keras-team/keras-preprocessing)
    - 122 Stars, 22 Fork

Utilities for working with image data, text data, and sequence data.

(`是也乎:`

Keras 也开始爆点了...

)


- [Face-tracking-with-Anime-characters](https://github.com/Aditya-Khadilkar/Face-tracking-with-Anime-characters)
    - 73 Stars, 10 Fork

Hello! I have made a Python project where YURI from the game doki doki literature club accesses the webcam and stares directly into the players soul. Hope you enjoy!

(`是也乎:`

![YURI](https://user-images.githubusercontent.com/35966791/41169627-3358001c-6b67-11e8-98f1-32f721e609af.png)

有点儿污...

)


- [object-tracking](https://github.com/ankurg22/object-tracking)
    - 29 Stars, 11 Fork

Object tracking by colour and drawing its path.

(`是也乎:`


![object-tracking](https://github.com/ankurg22/object-tracking/raw/master/demo.gif)

印度程序猿小哥哥们, 最近有很多 CV 作品发布呢...



)


- [nvidia-docker-keras](https://github.com/idealo/nvidia-docker-keras)
    - 22 Stars, 11 Fork

Workflow that shows how to train neural networks on EC2 instances with GPU support and compares training times to CPUs

- [Shout_At_Netflix_To_Continue](https://github.com/esdalmaijer/Shout_At_Netflix_To_Continue)
    - 17 Stars, 0 Fork

Literally the worst way to make Netflix continue when it asks you whether you're still watching: Make noise to click the mouse

(`是也乎:`

囧rz...人民的需求就是正义

)


- [PyPad](https://github.com/Fuchsiaff/PyPad)
    - 9 Stars, 5 Fork

A simple customizable cross-platform notepad

(`是也乎:`

![PyPad](https://raw.githubusercontent.com/Fuchsiaff/csgo_wallhack/master/2018-06-04-174804_1920x1025_scrot.png)


Qt 实现的嗯哼, 在 linux 平台上完成主要开发...;
为了调色...简直了...

)


- [pyradio](https://github.com/sdushantha/pyradio)
    - 7 Stars, 0 Fork

Play your favorite radio station from the terminal 

(`是也乎:`

叕一实用 CLI 工具;
基于 vlc 的流媒体功能...

)


### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180616 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180616 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


