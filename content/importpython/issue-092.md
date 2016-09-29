Title: 蠎加载 92
Slug: importpython-92
Date: 2016-09-29 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 9](http://importpython.com/newsletter/no/92/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Python 别名命令配合 virtualenv 玩的更好](https://notoriousno.blogspot.com/2016/09/python-alias-commands-that-play-nice.html)

Over the years, I’ve come up with my own Python aliases that play nice with virtual environments. For this post, I tried to stay as generic as possible such that any alias here can be used by every Pythonista.

(`是也乎:`

使用 bash 中的配置别名也一样
)

- [保持 Django 应用性能的详细记录.](https://github.com/YPlan/django-perf-rec)
    + django, performance

"Keep detailed records of the performance of your Django code.". django-perf-rec is like Django's assertNumQueries on steroids. It lets you track the individual queries and cache operations that occur in your code. This blog post explains the workings of this project https://tech.yplanapp.com/2016/09/26/introducing-django-perf-rec/ .

- [上周未工程师的实用  ML 分享 #pyconuk](http://ianozsvald.com/2016/09/23/practical-ml-for-engineers-talk-at-pyconuk-last-weekend/)
    + machine learning

Last weekend I had the pleasure of introducing Machine Learning for Engineers (a practical walk-through, no maths) at PyConUK 2016 ( Video link on page ). My talk covered a practical guide to a 2 class classification challenge (Kaggle’s Titanic) with scikit-learn, backed by a longer Jupyter Notebook (github) and further backed by Ezzeri’s 2 hour tutorial from PyConUK 2014.

- [Python 中的 Mocks 和 Monkeypatching ](https://semaphoreci.com/community/tutorials/mocks-and-monkeypatching-in-python)
    + testing

This tutorial will help you understand why mocking is important, and show you how to mock in Python with Mock and Pytest monkeypatch.

- [Abu Ashraf Masnun: 介绍 Django Channels](http://masnun.rocks/2016/09/25/introduction-to-django-channels/)

Yet another introduction to Django Channels. This one is a lot more clear and step by step tutorial. If you still don't know what Django channels is / how to get started, read this.

(`是也乎:`

又一篇 Django Channels 的介绍, 可想是个多么复杂难言的功能点
)

- [Python Mocks: 温柔的介绍 - 部分1和2](http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/)
    + testing, mock

In this series of posts I am going to review the Python mock library and exemplify its use. I will not cover everything you may do with mock, obviously, but hopefully I'll give you the information you need to start using this powerful library. Note it's a two part series as of now, here is the second part's url http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/#.V-ysf9HhXQo

- [Decorators: 函式的功能 - 周末和 Trey Hunner 聊 Python ](http://ccst.io/e/decorators)
    + webcast, video

Decorators are one of those features in Python that people like to talk about. Why? Because they're different. Because they're a little weird. Because they're a little mind-bending. Let's talk about decorators: how do you make them and when should you use them?

- [简洁的图表和数据集  REST APIs](http://moderndata.plot.ly/simple-rest-apis-for-charts-and-datasets/)
    + charts

The Plotly V2 API suite is a simple alternative to the Google Charts API. Make a request to a Plotly URL and get a link to a dataset or D3.js chart. Python code snippet are included on the page.

(`是也乎:`

Plot.ly 如日中天时,高调开源后,依然猛烈...
)

- [Python 代码复审: Unplugged – 第 2 集 - Daniel Bader](https://dbader.org/blog/python-code-review-unplugged-episode-2)
    + code review

Daniel is doing a series of code review sessions with Python developers. Have a look at the accompanied video where he gives his opinion on a open source project by Milton.

- [Python 的 C 面](https://www.paypal-engineering.com/2016/09/22/python-by-the-c-side/)
    + c binding

CPython, the primary implementation of Python used by millions, is written in C. Python core developers embraced and exposed Python’s strong C roots, taking a traditional tack on portability, contrasting with the “write once, debug everywhere” approach popularized elsewhere. The community followed suit with the core developers, developing several methods for linking to C. This has given us a lot of choices for interfacing with c, let us look at them.

(`是也乎:`

又是 paypal 团队的分享, 看来 Py 在 paypal 家折腾的不轻...
)

- [Django 技巧 #15 基于 Mixins 使用 Class-Based Views](https://simpleisbetterthancomplex.com/tips/2016/09/27/django-tip-15-cbv-mixins.html)
    + django

General rules to use mixins to compose your own view classes with code examples.

- [如何设置 tab completion 来用 django-admin.py 和 manage.py ?](https://www.mikesdjangotutorials.co.uk/blog/blog/make-your-command-line-life-easier/)
    + django

In this short article Mike shows us how to set auto complete for django-admin.py / manage.py arguments. Specially helpful if you have tons of management commands.

- [M$ 中的 Python 工程](https://blogs.msdn.microsoft.com/pythonengineering/2016/09/27/microsofts-participation-in-the-2016-python-core-sprint/)
    + core python

That’s the opening paragraph from the Python Insider blog post discussing the 2016 Python core sprint that recently took place. In the case of Microsoft’s participation in the sprint, both Steve Dower and I (Brett Cannon) were invited to participate (which meant Microsoft had one of the largest company representations at the sprint). Between the two of us we spent the week completing work on four of our own PEPs for Python 3.6: Adding a file system path protocol (PEP 519), Adding a frame evaluation API to CPython (PEP 523), Change Windows console encoding to UTF-8 (PEP 528), Change Windows filesystem encoding to UTF-8 (PEP 529).

(`是也乎:`

发明了软件的 M$ ,好象没有哪个领域不掺合的
)

- [GitHub - beanbaginc/django: 非官方安全后端 Django: The Web framework for perfectionists with deadlines.](https://github.com/beanbaginc/django)
    + security

This is an unofficial fork of Django, which focuses entirely on backporting official, publicly-announced security fixes to Django 1.6.11. It does not contain any other bug fixes or features, and any branches other than security-backports/1.6.x are unlikely to be up-to-date. 



## 活动
    ~ Upcoming Conference / User Group Meet

- [Reunión Python Valencia](https://plus.google.com/communities/111688142997890939713/events)
- [Sydney Python User Group](http://sypy.org/)
- [PyConES - Almería](http://2016.es.pycon.org/es/)
- [Edmonton Python User Group](http://edmontonpy.com/)
- [IndyPy Monthly Meetup](http://www.meetup.com/python-182/)
- [Python Brasil [12]](http://2016.pythonbrasil.org.br/)
- [Santa Cruz Python Meetup](http://www.meetup.com/Santa-Cruz-Python-Meetup/)


## 项目
~ 包/模块/库/片段...



- [fmap](https://github.com/sminez/fmap)
    - 6 Stars, 0 Fork

fmap.py - a single dispatch version of fmap for Python3. While there are multiple Haskellesque 'lets put monads in Python!' style libraries out there, most don't seem to focus on taking the nice bits of Haskell's functional approach and giving them a nice Pythonic interface. fmap.py is a very simple take on fmap that lets you remove some unnecesary boiler plate when you are applying a function to each element of a collection. I hope you like it!

- [fbtftp](https://github.com/axbaretto/fbtftp)
    - 5 Stars, 0 Fork

fbtftp is Facebook's implementation of a dynamic TFTP server framework. It lets you create custom TFTP servers and wrap your own logic into it in a very simple manner. Facebook currently uses it in production, and it's deployed at global scale across all of our data centers.

(`是也乎:`

神奇的实用库, 基于 epoll 的纯 py 实现 ftp 服务器,来自 脸书.
)

- [unfurl](https://github.com/crutchcorn/unfurl)
    - 4 Stars, 0 Fork

Python utility to move items in a directory tree to the topmost level possible

(`是也乎:`

自动调节批量嵌套子目录中分散文件到顶层目录
)

- [chalk](https://github.com/dhill0n/chalk)
    - 2 Stars, 1 Fork

简单易学的又一个 py 解释的开发语言

- [human-to-geojson](https://github.com/pveugen/human-to-geojson)
    - 2 Stars, 1 Fork

Convert raw Human exports to geoJSON

![human](https://raw.githubusercontent.com/pveugen/human-to-geojson/master/mapbox-studio.png)

## DAMA
~ 无责任推荐

- [GitHub Octoverse 2016](https://octoverse.github.com/)

Github 年度报吿, 值得关注的是: [rdpeng (Roger D. Peng)](https://github.com/rdpeng)
这位华人,个人仓库有两个在 top10 名单中!
你猜为毛!?



# 是也乎

- 160929 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160929 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


