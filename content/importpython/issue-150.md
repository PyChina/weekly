Title: 蠎加载 150
Slug: importpython-150
Date: 2017-11-11 21:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 150](http://importpython.com/newsletter/no/150/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [十个 Sublime 插件值得用于日常 Python/Django 开发](https://medium.com/@MicroPyramid/ten-sublime-plugins-useful-for-your-daily-python-django-development-448f9407499b)
    + sublime

Sublime text editor comes with its basic setup as a normal text editor. We need some set of plugins to make it useful for any real-time development. In this blog post we list ten plugins that will be useful for your daily python/Django development.

- [加速 SQLite 和 Python](http://charlesleifer.com/blog/going-fast-with-sqlite-and-python/)
    + sqlite

In this post I'd like to share with you some techniques for effectively working with SQLite using Python.



- [你应该使用哪个 Python 包管理器 ?](https://towardsdatascience.com/which-python-package-manager-should-you-use-d0fd0789a250)
    + package manager

Everyone who touches code has different preferences when it comes to their programming environment. Vim versus emacs. Tabs versus spaces. Virtualenv versus Anaconda. Today I want to share with you my environment for working with data and doing machine learning.

(`是也乎:`

无论哪种都应该配合 pyenv
)


- [用 tmtoolkit 在 Python 进行主题模型评估](https://datascience.blog.wzb.eu/2017/11/09/topic-modeling-evaluation-in-python-with-tmtoolkit/)
    + topic modeling

I introduce the Python package tmtoolkit which allows to utilize all availabel CPU cores in your machine by computing and evaluating the models in parallel. We will use topic models based on the Latent Dirichlet Allocation (LDA) approach by Blei et al., which is the most popular topic model to date.


(`是也乎:`

基于 LDA 技术来突破 Py 应用的CPU 限制.

)


- [Python 类的特殊方法或魔术方法](https://medium.com/@MicroPyramid/python-class-special-methods-or-magic-methods-33668c0ce79e)
    + core-python

What happens when we create an object in python class ?

(`是也乎:`

叕一个 Python 内部机制解析嗯哼

)


- [以 Flask 和 Asyncio 构建 Quart](https://medium.com/@pgjones/building-quart-from-flask-and-asyncio-60a833a87e6b)
    + flask, asyncio

I recently gave a talk at PyCon UK in Cardiff about building Quart from Flask and Asyncio. The talk itself is on youtube (linked below) and I’ve made the slides available via google slides (also linked below).

- [jardin, a dataframe-based ORM for Python](https://tech.instacart.com/jardin-a-dataframe-based-orm-for-python-178e02e1c21)
    + pandas

Pandas can be fed a SQL query as a string to return a dataframe.

(`是也乎:`

SQL 实在是无法绕过的一个生产力工具

)


- [Python 来嗯哼 YouTube 数据](https://medium.com/greyatom/youtube-data-in-python-6147160c5833)
    + youtube

The YouTube Data api v3 gives us the access to YouTube videos, channels, search, captions, comments and playlists.

(`是也乎:`

非常好,只是...
)


- [Restful API 测试](https://taverntesting.github.io/)
    + testing

Tavern is a pytest plugin, command-line tool and Python library for automated testing of RESTful APIs, with a simple, concise and flexible YAML-based syntax. It’s very simple to get started, and highly customisable for complex tests.

(`是也乎:`

叕一个 RESTful 测试工具,
基于 Yaml?!

)


- [pyschemes](https://github.com/shivylp/pyschemes)
    + awesome project

PySchemes is a library for validating data structures in Python. PySchemes is designed to be simple and Pythonic.

(`是也乎:`

那什么, 这种面向编程过程, 而不是编译过程的,应该嗯哼的...

)


- [从头开始编写基本的 x86-64 JIT 编译器](https://csl.name/post/python-jit/)
    + cpython

In this post I'll show how to write a rudimentary, native x86-64 just-in-time compiler (JIT) in CPython, using only the built-in modules.

(`是也乎:`

JIT 是另外一个优化姿势了...

)


- [Don Jayamanne, creator of the Python extension for Visual Studio Code, joins Microsoft – Python Engineering at Microsoft](https://blogs.msdn.microsoft.com/pythonengineering/2017/11/09/don-jayamanne-joins-microsoft/)
    + Visual Studio

I'm delighted to announce that Don Jayamanne, the author of the most popular Python extension for Visual Studio Code, has joined Microsoft! Starting immediately, Microsoft will be publishing and supporting the extension. You will receive the update automatically, or visit our Visual Studio Marketplace page and click "Install".


- [构建一个 Python Autocompleter](https://anvil.works/blog/python-autocompleter-pycon17)
    + autocompleter

Why do you need autocompletion, and how does it work? My talk at PyCon UK 2017 explains how – and why – we built an in-browser autocompleter for Anvil.

(`是也乎:`

最新的浏览器内自动完成能力...

)

- [tt - 布尔表达式工具箱](http://tt.brianwel.ch/en/latest/)
    + boolean

tt (truth table) is a library aiming to provide a Pythonic toolkit for working with Boolean expressions and truth tables. Please see the project site for guides and documentation, or check out bool.tools for a simple web application powered by this library.


(`是也乎:`

专注 boolean 运算支持的工具

![tt](http://tt.brianwel.ch/en/latest/_static/logo.png)

PS: t.tt 不相干的

)


## 好物
~ 包/模块/库/片段...

- [phishing_catcher](https://github.com/x0rz/phishing_catcher)
    - 344 Stars, 67 Fork

Phishing catcher using Certstream.

(`是也乎:`

少见的安全工具
)

- [cryptocoin-price](https://github.com/techstar-inc/cryptocoin-price)
    - 17 Stars, 8 Fork

An Ubuntu desktop indicator displays prices of Bitcoin, Ethereum, Litecoin etc.

(`是也乎:`

![cryptocoin](https://github.com/techstar-inc/cryptocoin-price/raw/master/img/screen.png)

内什么中国已经取缔了...

)

- [Arbor](https://github.com/radding/Arbor)
    - 10 Stars, 1 Fork

A toy programming language for web assembly.

(`是也乎:`

玩具语言?

)

- [sentry-kubernetes](https://github.com/getsentry/sentry-kubernetes)
    - 9 Stars, 0 Fork

Kubernetes event reporter for Sentry.

(`是也乎:`

K8s 越来越有正统的气象了

)

- [docker_eventer](https://github.com/vfxGer/docker_eventer)
    - 0 Stars, 0 Fork

A Docker container to notify about Docker events written in Python

(`是也乎:`

叕一个 Docker 容器管理工具

)


-[athena](https://github.com/apas/athena)
    - 0 Stars, 0 Fork

athena is an elegant, minimalist, light-weight static blog generator written in Python. It is based on Flask, Pandoc, and Tufte CSS.

(`是也乎:`

> 雅典娜

这项目名实在...

![athena](https://github.com/apas/athena/raw/master/static/athena.png)

叕一个静态网站生成器, 只是基于 Flask 这种巨型框架?

)


- [reobject](https://github.com/onyb/reobject)
    - 0 Stars, 0 Fork

reobject is an ORM layer for your objects. It allows you to track and query objects at runtime using a familiar query langauge inspired by Django ORM. 

(`是也乎:`

叕一个 ORM , 在 SQLAlchemy 之后, 还有机会嘛?
)


### (￣▽￣)

- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

关键响应非常敏捷, 10.1 长徦期间嗯哼了一下, 立即追加了两个功能:
[pyheatmap/test.py at 31d80c89529e194e743e3125d56a189712186c55 · oldj/pyheatmap](https://github.com/oldj/pyheatmap/blob/31d80c89529e194e743e3125d56a189712186c55/examples/test.py#L49)

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)

- [Calysto/calysto_scheme: A Scheme kernel for Jupyter that can use Python libraries](https://github.com/Calysto/calysto_scheme)
    + scheme.ipynb

屌炸天的 Jupyter 能力扩展思路...


## 是也乎

- 171111 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171111 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


