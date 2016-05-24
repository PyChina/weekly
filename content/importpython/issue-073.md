Title: 蠎加载 73
Slug: importpython-73
Date: 2016-05-19 22:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 73](http://importpython.com/newsletter/no/73/)
- 欢迎, 来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)

## 该读
~ 文章, Blog, 教程...


- [Python 3: 加密介绍](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/Q917YZN0UrA/)
    + python3, encryption

Py 3 并没有增补更多加密相关的库,
本文专注第三方库: PyCrypto 和 cryptography,
展示如何进行加密以及对应的解密.

- [如何用 Python 为 Slack 构建短信机械人](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html)
    + bot

Bots can be a super useful bridge between Slack channels and external applications. Let’s code a simple Slack bot as a Python application that combines the Slack API with the Twilio SMS API so a user can send and receive Slack messages via SMS.

- [并发修饰器 - Python 并发真的很容易](https://www.peterbe.com/plog/deco)

全新得趣的库 deco, 专门进行并发运行的修饰,
作者是 Alex Sherman 和 Peter Den Hartog,
都在 Wisconsin Madison 大学.

- [Python 包索引的能量](https://caremad.io/2016/05/powering-pypi/)
    + pypi

介绍 `PyPI` 的真相.

The Python Package Index, or as most call it “PyPI” is a central part of the ecosystem of Python. It serves as a central registry of names, helping to prevent collision between different projects as well as the default repository that most Python users go to when looking for software.For most, what powers this service is largely opaque to them — it’s (usually) there when they need it and who or what powers it is largely a mystery to them, but what and who really powers PyPI?

- [在 AWS 上部署 Django 接口为 Docker 容器](http://www.restapibuilder.com/blog/deploying-your-django-api-in-one-docker-container-in-aws/)
    + django, docker

Docker is a wonderful technology revolutionazing how to run microservices. You may have some experience with it or may not. I will show in this short post how to run a Docker container in Amazon Web Services(EC2) with your whole API in it. This trick is only useful for APIs or django projects that doesn't need to scale and doesn't really have too much traffic.

- [扩展创业项目达到 200万点击/月 - 访谈 railwayapi.com 创始人 Kaustubh](http://blog.pythonanywhere.com/134/)

PythonAnywhere is a Python development and hosting environment that displays in your web browser and runs on our servers. They're already set up with everything you need. It's easy to use, fast, and powerful. There's even a useful free plan. In this interview Kaustubh talks about his experience of using PythonAnywhere.

- [Facebook 趋势 RSS 抓取 (w/ Python 3.5)](http://www.reddit.com/r/Python/comments/4j6g5g/facebook_trending_rss_feed_fetcher_w_python_35/)

快速构建的 py3 脚本,
处理来者 RSS 的 PDF 列表,监察 facebook 有关突发新闻.


- [Apache Spark 2.0: 结构化数据流介绍](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/in6nV8AcbMo/apache-spark-2-0--introduction-to-structured-streaming)
    + machine learning

Michael Armbrust and Tathagata Das explain updates to Spark version 2.0, demonstrating how stream processing is now more accessible with Spark SQL and DataFrame APIs. Video. Code snippets in Python.

- [Python 贴士列表 :: 提升清单](https://github.com/smoqadam/python-tips)
    + core python

Simple code snippets, stuff we need in everyday coding. Worth a quick glance.

- [Pygrunn: 微型 Python, Pythonic 的物联网 - Lars de Ridder](http://reinout.vanrees.org/weblog/2016/05/13/1_micropython.html)
    + core python

(嗯哼,为了 RAM 平台,我们不能使用 CPython)
micropython is a project that wants to bring python to the world of microprocessors. Micropython is a lean and fast implementation of python 3 for microprocessors. It was funded in 2013 on kickstarter. Originally it only ran on a special “pyboard”, but it has now been ported to various other microprocessors. Why use micropython? Easy to learn, with powerful features. Native bitwise operations. Ideal for rapid prototyping. (You cannot use cpython, mainly due to RAM usage.)

- [从 Python 直接加载 C++ 文件!](https://github.com/tbenthompson/cppimport)

Anyone looking to speed up critical regions of their script should have a look.

- [Python ASCII 动画生成器 : 也许有的人需要?](https://camo.githubusercontent.com/ee3229ce57687d4a804febe20140ab480efcbc72/68747470733a2f2f692e696d6775722e636f6d2f386d41586468752e676966)

Pretty cool decorator. Check out the gif screen-cast.

(`是也乎:`

将CLI 的输出,折腾为 gif 动画片;
嗯哼,不够科学...
)

- [Pygrunn: 理解 PyPy 并在生产中应用之 - Peter Odding/Bart Kroon](http://reinout.vanrees.org/weblog/2016/05/13/4_pypy.html)
    + pypy

pypy is “the faster version of python”. There are actually quite a lot of python implementation. cpython is the main one. There are also JIT compilers. Pypy is one of them. It is by far the most mature. PyPy is a python implementation, compliant with 2.7.10 and 3.2.5. And it is fast!.



- [Djangofriendly » Django 主机对比和资源](http://djangofriendly.com/hosts/)
    + django

Djangofriendly is a community resource for finding the friendliest Django hosting environments.

- [Asterix - 完备的 python 初始化系统 ](https://github.com/hkupty/asterix)
    + core python

Describe the initialization of your application and let asterix manage the startup for you. It will ensure that the correct dependencies are started in order, so you don't need any dirty hacks to have your initialization flow. Also, it allows you to build separate stacks for test/dev/production and even for web/batch applications, loading just what you need. 

## 新书
~ New Books

- [Python GUI Programming Cookbook](http://importpython.com/books/517/python-gui-programming-cookbook/)

Over 80 object-oriented recipes to help you create mind-blowing GUIs in Python.


## 活动
~ Upcoming Conference / User Group Meet

- [PyCon Singapore 2016](https://pycon.sg/)
- [GeoPython 2016](http://www.geopython.net/)
- [PyConTW 2016 in Taiwan](https://tw.pycon.org/2016/en-us/)
- [PyData Berlin 2016](http://pydata.org/berlin2016/)

## 项目
~ 包/模块/库/片段...


- [Facebook-Message-Bot](https://github.com/enginebai/Facebook-Message-Bot)
    + 78 Stars, 10 Fork

Flask 开发的 facebook 消息平台


- [expyre](https://github.com/lonetwin/expyre)
    + 50 Stars, 2 Fork

对 `atd` 的Python 包装,自动化删除 文件/目录

- [TranscriptBot](https://github.com/agermanidis/TranscriptBot)
    + 47 Stars, 0 Fork

实时转录你的 Slack 消息

- [leather](https://github.com/onyxfish/leather)
    + 35 Stars, 0 Fork

Python charting for 80% of humans.

- [pyconfig](https://github.com/samdmarshall/pyconfig)
    + 16 Stars, 0 Fork

以简洁的 DSL 来生成 xcconfig 文件

- [atom-python](https://github.com/ironSource/atom-python)
    + 13 Stars, 0 Fork

ironSource.atom SDK for Python

- [awesome-contributions](https://github.com/twinone/awesome-contributions)
    + 12 Stars, 3 Fork

AWESOME GitHub Contributions viewer!

- [2016_bop_semifinal](https://github.com/dyslove123/2016_bop_semifinal)
    + 10 Stars, 3 Fork

2016 bop senifinal python code

- [AnsibleRest](https://github.com/Kaydub00/AnsibleRest)
    + 6 Stars, 0 Fork

收集 Ansible 的 RESTful 框架

- [InstagramCrawler](https://github.com/iammrhelo/InstagramCrawler)
    + 4 Stars, 0 Fork

基于 Selenium 的图片下载脚本

- [rate-limit](https://github.com/titan-web/rate-limit)
    + 2 Stars, 0 Fork

Token bucket implementation for rate limiting (python recipe)


## DAMA 无责任推荐

- [Python 技巧总结 | Taotao's Zone](http://litaotao.github.io/python-materials)
    + 首次自我推荐 Py 原创好文章 ;-)
- [Top 10 Python libraries of 2015 — Medium](https://medium.com/@tryolabs/top-10-python-libraries-of-2015-4dc95f0a0ead#.szjzsyff1)

Jupyter ~ 神器之上的神器

retrying ~ 重试小仙器

aiohttp ~ 兼容 Py3 的更加简洁的 HTTP S/C

plumbum ~ 跨平台的 AppleScript

phonenumbers ~ 将 google libphonenumbers 人性化包装的电话检验库

networkx ~ graphviz 之后,更加好用的可视化库

influxdb ~ 时间序数据存储好物

elasticsearch-dsl ~ 嗯哼, Pythonic 操作小语言

keras ~ Theano 上的深度学习界面

gensim ~ NLP 必用品


以及: [20 Python libraries you can’t live without | Python Tips](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)


### 工作

....


# 是也乎

- 160524 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160524 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


