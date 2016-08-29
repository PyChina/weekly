Title: 蠎加载 85
Slug: importpython-85
Date: 2016-08-29 22:22
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 85](http://importpython.com/newsletter/no/85/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Daniel Bader: Sublime Text 为 Python 开发 — 回顾2016](https://dbader.org/blog/sublime-text-for-python-development-2016-review)
    + sublime

When you ask for editor recommendations as a Python developer one of the top choices you’ll hear about is Sublime Text. In this post I’ll review the status of Python development with Sublime Text as of 2016.

(`是也乎:`

subl 从一开始就和 py 纠缠在一起...
)

- [69集 - PyCon Canada 和 Francis Deslauriers 以及 Peter McCormick](http://podcastinit.podbean.com/e/episode-69-pycon-canada-with-francis-deslauriers-and-peter-mccormick/)
    + podcast

This week we interviewed Peter McCormick and Francis Deslauriers about their work organizing PyCon Canada to provide a venue for Canadians to talk about how they are using the language. If you happen to be near Toronto in November then you should get a ticket and help contribute to their success.

- [1M rows/s 从 Postgres 到 Python](http://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python)
    + benchmark

asyncpg is a new fully-featured open-source Python client library for PostgreSQL. It is built specifically for asyncio and Python 3.5 async / await. asyncpg is the fastest driver among common Python, NodeJS and Go implementations.

(`是也乎:`

Pg 输出全新的 py 客户端库,包含了最新的 py/node/go 的支持
)


- [Package of the Week: Flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html)

Flake8 is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder’s McCabe script. It is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.

(`是也乎:`

包含圈复杂度检测的代码风格工期
)


- [Brett Cannon: 网络协议, sans I/O](http://www.snarky.ca/network-protocols-sans-i-o)

(Hopefully) the future of network protocols in Python. I think it's important to promote this approach to implementing network protocols, to the point that I have created a page at https://sans-io.readthedocs.io/ to act as a reference of libraries that have followed the approach I've outlined here. Basically what this means is that network protocol libraries will need to be rewritten so that they can be used by both synchronous and asynchronous I/O .

(`是也乎:`

为了异步网络, 又一个协议包在冲进!
)

- [用 django-admin-honeypot 建立蜜罐](http://feedproxy.google.com/~r/GoDjango/~3/HTZnuKgxemY/)
    + django

Security is something we often ignore until it is too late. However, there are some things you can do right now that are easy to increase your security. Using django-admin-honeypot is one of those things you can do. It is super easy and provides you with the means of tracking who is trying to access your site.

(`是也乎:`

Django 越来越全能了...
)

- [你应该知道的 Django Admin 作为应用更 Bigger](https://medium.com/@hakibenita/things-you-must-know-about-django-admin-as-your-app-gets-bigger-6be0b0ee9614#.gsi99mdu8)
    + django admin panel

The Django admin is a very powerful tool. We use it for day to day operations, browsing data and support. As we grew some of our projects from zero to 100K+ users we started experiencing some of Django’s admin pain points?—?long response times and heavy load on the database.

(`是也乎:`

其实, 很久以前 Django Admin 当现成的 app 来使用就已经不是黑科技了...
)


- [介绍用 Python 进行自然语言处理 - Asyncjs](https://www.youtube.com/watch?v=IMKweOTFjXw)
    + video

In this talk, Jess Bowden introduces the area of NLP (Natural Language Processing) and a basic introduction of its principles. She uses Python and some of its fundamental NLP packages, such as NLTK, to illustrate examples and topics, demonstrating how to get started with processing and analysing Natural Languages. She also looks at what NLP can be used for, a broad overview of the sub-topics, and how to get yourself started with a demo project.

(`是也乎:`

对的, 也是很久之前, Py 就是自然处理的重要参与力量了,
毕竟对于非程序猿的科学家, 用 py 的阻力小很多...
)

- [Simon: datetime vs Arrow vs Pendulum vs Delorean vs udatetime](https://aboutsimon.com/blog/2016/08/04/datetime-vs-Arrow-vs-Pendulum-vs-Delorean-vs-udatetime.html)
    + datetime

I setup a benchmark, which can be found here to compare Python datetime, Arrow, Pendulum, Delorean and udatetime on a performance level. I picked 4 typical performance critical operations to measure the speed of those libraries. Decode a date-time string, Encode (serialize) a date-time string, Instantiate object with current time in UTC, Instantiate object with current time in local timezone, Instantiate object from timestamp in UTC, Instantiate object from timestamp in local timezone.


(`是也乎:`

嗯哼, 日期处理是又常用又头痛的一件事儿...这么多年过去了,
依然没有什么完美的形式来打动 guido 收入标准库...
)

- [PyPy 获得 Mozilla 的资助用以支持 Python 3.5](http://feedproxy.google.com/~r/PyPyStatusBlog/~3/uTWeNBbKaCw/pypy-gets-funding-from-mozilla-for.html)
    + community

Mozilla recently decided to award $200,000 to Baroque Software to work on PyPy as part of its Mozilla Open Source Support (MOSS) initiative. This money will be used to implement the Python 3.5 features in PyPy. Within the next year, we plan to use the money to pay four core PyPy developers half-time to work on the missing features and on some of the big performance and cpyext issues.

(`是也乎:`

銭虽然不多, 但是可以看出 Mozilla 对 rust 并不放心, 还在继续确保其它可能性
)


- [你的 Django 故事: 遇见 Katerina Kampardi](http://blog.djangogirls.org/post/148639163968)
    + djangogirls

Katerina Kampardi is a Web Applications Developer from Greece who works as a freelancer. Like many aspiring developers, Katerina is self-taught and got her start with online tutorials. She later attended a Python Specialization. Today, she works on various Django projects as an independent developer.



## 活动
~ Upcoming Conference / User Group Meet

- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon ZA 2016](https://za.pycon.org/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon DE 2016](http://pycon.de/)




## 项目
~ 包/模块/库/片段...

- [colornet](https://github.com/pavelgonchar/colornet)
    - 1885 Stars, 67 Fork

使用 Neural Network 
来进行灰度图像上色


- [tflearn](https://github.com/tflearn/tflearn)
    - 1313 Stars, 50 Fork

深度学习库,
作为 TensorFlow 的一个高级接口

- [DeepDreamVideo](https://github.com/graphific/DeepDreamVideo)
    - 773 Stars, 94 Fork

implementing deep dream on video

- [dcgan-completion.tensorflow](https://github.com/bamos/dcgan-completion.tensorflow)
    - 54 Stars, 9 Fork

用 TensorFlow 的深度学习能力来图像修复


- [fastText.py](https://github.com/pyk/fastText.py)
    - 44 Stars, 3 Fork

Facebook fastText 的 py 接口


- [NBA-Player-Movements](https://github.com/linouk23/NBA-Player-Movements)
    - 37 Stars, 3 Fork

基于 SportVU 日志数据, 可视化 NBA 比赛

(`是也乎:`

![spurs](https://github.com/linouk23/NBA-Player-Movements/raw/master/examples/spurs.gif)
)

- [pic2text](https://github.com/winterfeel/pic2text)
    - 15 Stars, 12 Fork

又一个将图像转化为文字的工具


- [NaiveBayesClassifier](https://github.com/moushuai/NaiveBayesClassifier)
    - 3 Stars, 1 Fork

Naive bayes classifier implement with Python 2.7

Python 2.7 实现的 朴素贝叶斯分类器

(`是也乎:`

Naive bayes 原理很简单, 困难的是在现实情景中合理识别先验条件
)






## DAMA
~ 无责任推荐


# 是也乎

- 160829 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160829 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


