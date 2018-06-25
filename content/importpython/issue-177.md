Title: 蠎加载 177
Slug: importpython-177
Date: 2018-06-25 20:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 177](http://importpython.com/newsletter/no/177/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Python 惯用: Multiline Strings](https://amir.rachum.com/blog/2018/06/23/python-multiline-idioms/)
    + core-python

I rarely see Multiline strings used in Python code outside of docstrings, but they can be very useful, especially when you need to create a very specifically structured string, like a code snippet, help section to print to the screen or ASCII art for a snake. The problem is that it’s just ugly, because indenting the strings actually inserts the indentation into the string.

(`是也乎:`

这个形式什么都好, 就是一嵌套就乱了...

)



- [PEP 572 和 decision-making in Python](https://lwn.net/SubscriberLink/757713/2118c7722d957926/)
    + BDFL

The "PEP 572 mess" was the topic of a 2018 Python Language Summit session led by benevolent dictator for life (BDFL) Guido van Rossum. PEP 572 seeks to add assignment expressions (or "inline assignments") to the language, but it has seen a prolonged discussion over multiple huge threads on the python-dev mailing list—even after multiple rounds on python-ideas. Those threads were often contentious and were clearly voluminous to the point where many probably just tuned them out. At the summit, Van Rossum gave an overview of the feature proposal, which he seems inclined toward accepting, but he also wanted to discuss how to avoid this kind of thread explosion in the future.

(`是也乎:`

BDFL 说了算

)



- [直想要可视化 Python 调试器由 Jupyter notebook 赋予](https://medium.com/ibm-watson-data-lab/the-visual-python-debugger-for-jupyter-notebooks-youve-always-wanted-761713babc62)
    + jupyter

Some would rightfully point out that Jupyter already supports pdb for simple debugging, where you can manually and sequentially enter commands to do things like inspect variables, set breakpoints, etc.?—?and this is probably sufficient when it comes to debugging simple analytics. To raise the bar, the PixieDust team is happy to introduce the first (to the best of our knowledge) visual Python debugger for Jupyter Notebooks.

(`是也乎:`

Jupyter 的潜力刚刚开始嗯哼

)



- [BuzzFeed 如何将微服务从 Perl Monolith 迁移到 Go 和 Python](https://www.infoq.com/articles/buzzfeed-microservices-migration)
    + migration

BuzzFeed have recently migrated from a monolithic Perl application to a set of around 500 microservices written in a mixture of Python and Go.

(`是也乎:`

从 perl 到 go+py...

)



- [Python 中常见10种安全漏洞，以及如何避免它们](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03)
    + security

Here are my top 10, in no particular order, common gotchas in Python applications.


(`是也乎:`

avoid 是重点

)


- [嗯哼 Python 中 lambda 表达式的异常](http://baruchel.github.io/python/2018/06/20/python-exceptions-in-lambda/)
    + codesnippets

The following piece of code can certainly claim being the most insane Python expression ever written.

(`是也乎:`

其实,所以,因为,那么...

)


- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
    + cheatsheet

Anyone can forget how to make character classes for a regex, slice a list or do a for loop. This cheatsheet tries to provide a basic reference for beginner and advanced developers, lower the entry barrier for newcomers and help veterans refresh the old tricks.

(`是也乎:`

每个大版本发布后, 都得对应嗯哼一下

)


- [Decorators](https://pythonbasics.org/Decorators/)
    + core-python

Learn Python Decorators in this tutorial.

(`是也乎:`

叕一则内建功能的教程

)


- [GCP(Google Cloud Platform)上 Apache Beam 的 Python 开发环境](https://medium.com/google-cloud/python-development-environments-for-apache-beam-on-google-cloud-platform-b6f276b344df)
    + apache beam

These instructions will show you how to set up a development environment for Python Dataflow jobs. By the end you’ll be able to run a Dataflow job locally in debug mode, and execute code in a REPL to speed your development cycles.

(`是也乎:`

Dataflow 任务?

)


- [Python 的类型提示状态](https://www.bernat.tech/the-state-of-type-hints-in-python/)
    + core-python

One of the main selling points for Python is that it is dynamically-typed. There is no plan to change this. Nevertheless, in September 2014 Guido van Rossum (Python BDFL) created a python enhancement proposal (PEP-484) to add type hints to Python. It has been released for general usage a year later, in September 2015, as part of Python 3.5.0. Twenty-five years into its existence now there was a standard way to add type information to Python code. In this blog post, I'll explore how the system matured, how you can use it and what's next for type hints.


(`是也乎:`

反正老爹说了算

)


- [Vibora - Python Web 框架/服务器](https://vibora.io/)
    + webframework

Vibora APIs were heavily inspired by the awesome Flask. Builtin features were also based on many famous libraries as jinja2, marshmallow, websockets by aaugustin, werkzeug and many others.

(`是也乎:`

![Vibora](https://raw.githubusercontent.com/vibora-io/vibora/master/docs/logo.png)

Py3.6+ only...

)


- [理解任意一头 Python 程序猿 – Notes By A Nerd](http://notesbyanerd.com/2017/12/29/essential-reads-for-any-python-programmer/)

- [fairseq](https://github.com/pytorch/fairseq)
    + pytorch

Fairseq(-py) is a sequence modeling toolkit that allows researchers and developers to train custom models for translation, summarization, language modeling and other text generation tasks. It provides reference implementations of various sequence-to-sequence models, including:

(`是也乎:`

sequence-to-sequence 模型的 pytorch 嗯哼

)

## 好物
~ 包/模块/库/片段...



- [learn_math_fast](https://github.com/llSourcell/learn_math_fast)
    + 820 Stars, 114 Fork

This is the Curriculum for "How to Learn Mathematics Fast" By Siraj Raval on Youtube

(`是也乎:`

叕一个 Awesome

![CC](https://camo.githubusercontent.com/c5160f944848828fa33126d9a697e9abe43ea98f/687474703a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f702f7a65726f2f312e302f38387833312e706e67)

)


- [kconfig-hardened-check](https://github.com/a13xp0p0v/kconfig-hardened-check)
    +   69 Stars, 9 Fork

A script for checking the hardening options in the Linux kernel config

(`是也乎:`

好象各种配置检验/自动生成/部署/... 相关重要文本控制的工具
都是 py 来嗯哼的

)


- [sentry-python](https://github.com/getsentry/sentry-python)
    +  24 Stars, 0 Fork

Up and coming but not yet usable new Python client

(`是也乎:`

![logo](https://camo.githubusercontent.com/2dfeafbee0904d6df16ddf7200993dace1629e60/68747470733a2f2f73656e7472792d6272616e642e73746f726167652e676f6f676c65617069732e636f6d2f73656e7472792d6c6f676f2d626c61636b2e706e67)

logo 正经, 项目就有希望


)


- [captcha-breaker](https://github.com/dominhhai/captcha-breaker)
    + 10 Stars, 1 Fork

High Accuracy Captcha Breaker with Tensorflow and Node.js

(`是也乎:`

动用 TF 的反Captcha 工具

![breaker](https://camo.githubusercontent.com/d3f6413ef14ba1e6c26b8bb6ff7654e485cc8d0a/68747470733a2f2f692e7974696d672e636f6d2f76692f707275616f472d4d536f342f687164656661756c742e6a7067)

日本程序猿作品

)


- [python-string-similarity](https://github.com/luozhouyang/python-string-similarity)
    + 8 Stars, 1 Fork

A library implementing different string similarity and distance measures using Python.

(`是也乎:`

叕一则字串距离工具,但是...

)


- [modin](https://github.com/modin-project/modin)
    + 5 Stars, 3 Fork

Modin: Pandas on Ray - Make your pandas code faster by changing one line of code

(`是也乎:`

Pandas 的叕一则次级工具

> import modin.dataframe as pd

单行提速

)


- [textpipe](https://github.com/textpipe/textpipe) 
    + 5 Stars, 0 Fork

Clean and extract metadata from text.




- [Fifa-world-cup](https://github.com/SoumitraAgarwal/Fifa-world-cup)   
    + 2 Stars, 0 Fork

Analyses of faces of fifa world cup 2018




- [molten: modern API framework](https://moltenframework.com/v0.1.0/index.html)
    + 0 Stars, 0 Fork

molten is a minimal, extensible, fast and productive framework for building HTTP APIs with Python. 

(`是也乎:`

叕一 API 框架

)




### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180625 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180625 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


