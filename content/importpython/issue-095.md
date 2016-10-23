Title: 蠎加载 95
Slug: importpython-95
Date: 2016-10-23 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 95](http://importpython.com/newsletter/no/95/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [用 Rust 修复 Python 性能](https://blog.sentry.io/2016/10/19/fixing-python-performance-with-rust.html)
    + performance

Excellent post from Armin Ronacher on tackling a CPython performance bottleneck with a custom Rust extension module.

(`是也乎:`

简单的说就是将 py 伪装成 Rust 来跑 ~ 城会玩儿~.~
)

- [在 Python 中如何创建只读属性和限制性值对象](http://howto.lintel.in/how-to-create-read-only-attributes-and-restrict-setting-attribute-values-on-object-in-python/)
    + core python

There are different way to prevent setting attributes and make attributes read only on object in python. We can use any one of the following way to make attributes readonly. 1) Property Descriptor 2) Using descriptor methods __get__ and __set__ 3) Using slots (only restricts setting arbitary attributes).

(`是也乎:`

使用内置的自省机制来防卫
)

- [如何将 Django 应用部署到 Digital Ocean](https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html)
    + deployment

In this tutorial we will be deploying https://github.com/sibtc/urban-train ,a empty Django project I created to illustrate the deployment process.

(`是也乎:`

一个 Heroku 一个 Digital Ocean, 文档好到经常被搜索出来独立使用
)

- [用 Python 进行异步抓取](http://www.gregreda.com/2016/10/16/asynchronous-scraping-with-python/)

Scraping is often an example of code that is embarrassingly parallel. With some slight changes, our tasks can be done asynchronously, allowing us to process more than one URL at a time. In version 3.2, Python introduced the concurrent.futures module, which is a joy to use for parallelizing tasks like scraping. The rest of this post will show how we can use the module to make our previously synchronous code asynchronous.

(`是也乎:`

使用 Py3 内置的库折腾
)

- [每周聊 Python: Class-Based Views in Django](http://ccst.io/e/cbv)
    + video

Most Django programmers use function-based views, but some use class-based views. Why? Special guest Buddy Lindsey will be joining us this week to talk about how class-based views are different.

- [和俺聊 Python : #80 TinyDB: 轻便的文档数据库](https://talkpython.fm/episodes/show/80/tinydb-a-tiny-document-db-written-in-python)
    + podcast

I'm excited to introduce you to Markus Siemens and TinyDb. This is a 100% pure python, embeddable, pip-installable document DB for Python.

(`是也乎:`

无论怎么折腾, 目前看还没有一种 NoSQL 数据库可以简单的替代 MySQL 
)

- [在 Django 处状态](http://eatsomecode.com/handling-statuses-django)
    + django, finite state machine

Whether you're building up a CMS or a bespoke application, chances are that you will have to handle some states / statuses. Let's discuss your options in Django.

- [JIRA](http://www.launchbit.com/taz/11284-6631-111)
    + Sponsor

IT Help Desk & Ticketing. Start a free trial of JIRA Service Desk and get your free Konami Code shirt.

(`是也乎:`

其它赞助商俺是不知道的, 这个非常赞的
)

- [升级 Django - Never Clever](http://thosecleverkids.com/thoughts/posts/upgrading-django)
    + django

General Guidelines when upgrading Django.

(`是也乎:`

人艰不拆,宁可另外起用个新网站,来替换部分接口,也别...

啊,多么也痛的领悟...)

- [Yoda on python dependency](https://twitter.com/getpy/status/788729906406514689)
    + humor

Check the tweet :)

(`是也乎:`

程序猿的幽默只有翻越后感知的到
)

- [lptrace](https://github.com/khamidou/lptrace)
    + opensource project

lptrace is strace for Python programs. It lets you see in real-time what functions a Python program is running. It's particularly useful to debug weird issues on production.

(`是也乎:`

又一个观察活体 Python 运行时变量情况的调试工具,
不过...
)

- [Python 的静态类型,嚓 my(py)!](http://blog.zulip.org/2016/10/13/static-types-in-python-oh-mypy/)
    + mypy

In this post, I’ll explain how mypy works, the benefits and pain points we’ve seen in using mypy, and share a detailed guide for adopting mypy in a large production codebase (including how to find and fix dozens of issues in a large project in the first few days of using mypy!).

- [sanic](https://github.com/channelcat/sanic)
    + web server

Python 3.5+ web server that's written to go fast 


## 活动
    ~ Upcoming Conference / User Group Meet

- [Inland Empire Pyladies](http://www.meetup.com/iepyladies/)
- [PyKla Monthly meetup](https://www.meetup.com/meetup-group-JpMXKzbv/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon Finland 2016](http://fi.pycon.org/2016/)
- [PyCon Ireland 2016](https://python.ie/pycon-2016/)
- [PyCon Canada 2016](https://2016.pycon.ca/)
- [PyHPC 2016](http://www.dlr.de/sc/pyhpc2016)
- [PyCon Jamaica 2016](http://pythonjam.org.jm/conference-2016)


## 项目
~ 包/模块/库/片段...


- [fast-neural-style.tf](https://github.com/junrushao1994/fast-neural-style.tf)
    - 17 Stars, 6 Fork

Feed-forward neural network for real-time artistic style transfer. Curator's Note - This is a pretty cool project.

(`是也乎:`

![cubist_style](https://github.com/junrushao1994/fast-neural-style.tf/raw/master/examples/outputs/cubist_style.jpg)

又一个实时风格分析/模拟 的库,功能类似正红的 `Prisma`

)


- [TextSum](https://github.com/surmenok/TextSum)
    - 8 Stars, 1 Fork

Preparing a dataset for TensorFlow text summarization (TextSum) model.

- [countrynames](https://github.com/occrp/countrynames)
    - 5 Stars, 0 Fork

实用库, 将国家名称转换为ISO双字母代码

- [celery-redundant-scheduler](https://github.com/MnogoByte/celery-redundant-scheduler)
    - 4 Stars, 0 Fork

Celery beat 调度器提供运行多个celerybeat实例的能力

- [SlackUptimeMonitor](https://github.com/AndreiD/SlackUptimeMonitor)
    - 3 Stars, 3 Fork

Receive notifications in Slack when your websites/api/services are down

- [confluence-dumper](https://github.com/siemens/confluence-dumper)
    - 3 Stars, 0 Fork

通过 API 能递归样的将 Confluence 空间和页页都导出

- [asyncio-nats-streaming](https://github.com/mackeyja92/asyncio-nats-streaming)
    - 3 Stars, 0 Fork

A asyncio library for NATS Streaming.


# 是也乎

- 161024 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161023 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


