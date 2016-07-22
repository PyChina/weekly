Title: 蠎加载 82
Slug: importpython-82
Date: 2016-07-22 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 82](http://importpython.com/newsletter/no/82/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [对100万酒店进行机械学习后有趣的发现](https://blog.monkeylearn.com/machine-learning-1m-hotel-reviews-finds-interesting-insights/)

On this tutorial we learned how to scrape millions of reviews, analyze them with pre-trained classifiers within MonkeyLearn, indexed the results with Elasticsearch and visualize them using Kibana. Machine learning makes sense when you want to analyze big volumes of data in a cost effective way. The code repository is here - https://github.com/monkeylearn/hotel-review-analysis

(`是也乎:`

以 tripadvisor 为数据源! 也就是说这世界上部分信息早已经开放了...
)


- [Mike Driscoll: Python 进阶: 介绍 mock](http://www.blog.pythonlibrary.org/2016/07/19/python-201-an-intro-to-mock/)

The unittest module now includes a mock submodule as of Python 3.3. It will allow you to replace portions of the system that you are testing with mock objects as well as make assertions about how they were used. A mock object is used for simulating system resources that aren’t available in your test environment. In other words, you will find times when you want to test some part of your code in isolation from the rest of it or you will need to test some code in isolation from outside services.

(`是也乎:`

除非实在难以架构, 否则尽可能使用真实测试对象吧
)

- [Altair: 声明式 Python 统计可视化库, 基于 Vega-Lite](https://github.com/ellisonbg/altair)
    + pep8

Altair is a declarative statistical visualization library for Python.

(`是也乎:`

基于 Pandas 的数据表
)

- [又7个 Django Web 开发应知应会](http://www.allaboutweb.biz/best-practices-in-django-development/)
    + django

Set up Persistent Database Connections, Turn Cached Loading on, Store the Sessions in Cache, Keep the Application and Libraries Separate, Store All Templates in One Place, Install HTML5 Boilerplate, Monitor and Control Processes using Supervisor.

(`是也乎:`

随着 Django 的高速发展, 这类最佳实践将是永无止境的
)

- [DSF 发布开发行为守则](https://www.djangoproject.com/weblog/2016/jul/19/dsf-code-conduct-committee-releases-transparent-do/)
    + community

Today we're proud to open source the documentation that describes how the Django Code of Conduct committee enforces our Code of Conduct. This documentation covers the structure of Code of Conduct committee membership, the process of handling Code of Conduct violations, our decision making process, record keeping, and transparency.

- [为毛 Python 中有些行为函式就是不用下刬线? 比如: setdefault, makedirs, isinstance?](http://www.reddit.com/r/Python/comments/4stbtb/why_are_some_functions_in_python_spelled_with/)
    + discussion

I always wondered that. Here is a reddit discussion on the same.

(`是也乎:`

因为作者当初睡着了...
)

- [如何用Python 写一个能写 Python 的 AI](http://www.benjamintd.com/blog/spynet/)
    + AI

This post is about creating a machine that writes its own code. More or less. Introducing GlaDoS Skynet Spynet. More specifically, we are going to train a character level Long Short Term Memory neural network to write code itself by feeding it Python source code. The training will run on a GPU instance on EC2, using Theano and Lasagne. If some of the words here sound obscure to you, I will do my best to explain what is happening.

(`是也乎:`

简单的说, 这就是 西乔 的 beta cat 的构建方法
)

- [用 Flask-RESTful 写个 API](https://blog.restsecured.xyz/writing-an-api-with-flask-restful-part-1-61b0e26e0e5b#.1kmhfmkeo)
    + REST

This article will go over the details of how to create a RESTful API with Flask and Flask-RESTful. In Part 1 we will go over the API basics and how to implement a simple API. In Part 2 we will expand into advanced use cases powered by Flask-RESTful. All code that will be show is readily available on this repository.

(`是也乎:`

虽然 Flask 比 Django 轻便很多倍,但是,依然...
)

- [SciPy 2016 视频已经放](https://www.youtube.com/playlist?list=PLGB9meziqbzpRP7mVyihOihNzm_J2Kx9I&app=desktop)
    + video

Running Python Apps in the Browser by Almar Klein was a pretty interesting talk for me. See what interest you. Youtube channel.

(`是也乎:`

如何在 浏览器 中运行  Py 应用!?这个视频值得关注.
)

- [如何构建自制 Django Middleware](http://goo.gl/RlFfvx)
    + django

In a nutshell, a Middleware is a regular Python class that hooks into Django’s request/response life cycle. Those classes holds pieces of code that are processed upon every request/response your Django application handles.

- [Mike Driscoll: 介绍 coverage.py](http://www.blog.pythonlibrary.org/2016/07/20/an-intro-to-coverage-py/)
    + coverage

Coverage.py is a 3rd party tool for Python that is used for measuring your code coverage. It was originally created by Ned Batchelder. The term “coverage” in programming circles is typically used to describe the effectiveness of your tests and how much of your code is actually covered by tests. You can use coverage.py with Python 2.6 up to the current version of Python 3 as well as with PyPy.

(`是也乎:`

虽然没收入官方内建库, 但 coverage.py 已经是事实上最常用的覆盖测试模块
)

- [Django 的 Ajax 网站教程](https://bitbucket.org/drk4/website_example)
    + django

In this tutorial we'll see a trivial example of how to do a ajax website with django. Good for students looking to learn the basics of Django/Ajax and see how it works.

- [订阅 Gitter 上 Python & Django 频道吧.](https://medium.com/@gitter/best-gitter-channels-python-django-41a0a0b1aee6#.9r2hh96vn)
    + community

Gitter is like slack for developers. They have active Python, Django channels. Have a look.

- [介绍 Zipline](http://www.quantinsti.com/blog/introduction-zipline-python/)

Python has emerged as one of the most popular language for programmers in financial trading, due to its ease of availability, user-friendliness and presence of sufficient scientific libraries like Pandas, NumPy, PyAlgoTrade, Pybacktest and more. Zipline is a Python library for trading applications that powers the Quantopian service mentioned above. It is an event-driven system that supports both backtesting and live-trading. In this article we will learn how to install Zipline and then how to implement Moving Average Crossover strategy and calculate P&L, Portfolio value etc.

(`是也乎:`

可能是最好的股票交易管理平台
)



## 活动
~ Upcoming Conference / User Group Meet

- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [PyCon APAC 2016](https://www.pycon.kr/2016apac/)
- [EuroScipy 2016](https://www.euroscipy.org/2016)
- [PyCon MY 2016](http://pycon.my/)
- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon ZA 2016](https://za.pycon.org/)



## 项目
~ 包/模块/库/片段...

- [PokemonGo-DesktopMap](https://github.com/mchristopher/PokemonGo-DesktopMap)
    - 204 Stars, 36 Fork

Electron App around PokemonGo-Map

- [PokemonGo-Map](https://github.com/AHAAAAAAA/PokemonGo-Map)
    - 128 Stars, 55 Fork

Live visualization of all the pokemon in your area

- [asyncpg](https://github.com/MagicStack/asyncpg)
    - 69 Stars, 2 Fork

Python/asyncio 完成, 很快的 PostgreSQL Database 客户端库 

- [choronzon](https://github.com/CENSUS/choronzon)
    - 46 Stars, 16 Fork

An evolutionary knowledge-based fuzzer


(`是也乎:`

没看明白是作什么的, 但是,看起来很高级, 
又一个 AI 相关的开发库.
)

- [zhihu-terminal](https://github.com/duduainankai/zhihu-terminal)
    - 42 Stars, 2 Fork

zhihu-terminal using python2.7.

(`是也乎:`

'''...更重要的是以后在实验开着命令行就不会被老板和同学发现我是在刷知乎了哦。。'''
无法同意更多!

![TimeLine](https://github.com/duduainankai/zhihu-terminal/raw/master/img/TimeLine.png)

)

- [awesome-wagtail](https://github.com/springload/awesome-wagtail)
    - 14 Stars, 1 Fork

A curated list of awesome packages, articles, and other cool resources from the Wagtail community.

(`是也乎:`

Wagtail 就是 Django 实现的 wordpress...不过, 生态还早...
)

- [reddit_get_top_images](https://github.com/nagracks/reddit_get_top_images)
    - 10 Stars, 1 Fork

Get top images from any subreddit

- [aiosmtpd](https://github.com/aio-libs/aiosmtpd)
    - 6 Stars, 1 Fork

asyncio 基础上对标准库 smtpd.py 的替代

- [delft](https://github.com/rhiever/delft)
    - 6 Stars, 1 Fork

使用遗传程序自动优化深度学习管道



## DAMA
~ 无责任推荐

# 是也乎

- 160722 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160722 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


