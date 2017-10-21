Title: 蠎加载 146
Slug: importpython-146
Date: 2017-10-13 21:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 146](http://importpython.com/newsletter/no/146/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [通过在 python 中编 C 扩展来提高性能](https://medium.com/@abhijeetagorhe/performance-gain-by-writing-a-c-extension-in-python-12dda9aa8ee6)
    + cpython

Interpreted language will never match the performance of compiled languages . Ever since I moved on to python from C/C++ , I always wanted to combine best of both worlds by extending python in C .

(`是也乎:`

这事儿地球人都知道, M$ 还嫌 C 性能差在 C++ 代码中嵌汇编呢...

问题是, 首先功能稳定后, 还得找到性能瓶颈再针对性替代,
光这个工程就不简单了...

)

- [简介用 Pandas 进行数据清洗](https://medium.com/@madhavayyagari/introduction-to-data-cleaning-using-pandas-64102b97dd62)
    + pandas, excel

I’ve been using Excel for data cleaning until I discovered how powerful pandas are for data analysis and data cleaning. In this article I want to go over basics of how to use pandas for cleaning data in excel files.

(`是也乎:`
数据源是 excel 文件...细思恐极了..

)

- [从零开始在 Python 中实施 Fisher 的 LDA](http://goelhardik.github.io/2016/10/04/fishers-lda/)
    + machine learning, LDA

Fisher’s Linear Discriminant Analysis (LDA) is a dimension reduction technique that can be used for classification as well. In this blog post, we will learn more about Fisher’s LDA and implement it from scratch in Python.

- [Implementing Ethereum trading front-runs on the Bancor exchange in Python](https://hackernoon.com/front-running-bancor-in-150-lines-of-python-with-ethereum-api-d5e2bfd0d798)
    + cryptocurrency

This post is a deep-dive into programmatically trading on the Ethereum / Bancor exchange and exploiting a game-theoretic security flaw in Bancor, a high-profile smart contract on the Ethereum blockchain.



- [Python 方法解析顺序](https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc)
    + core-python, MRO

In Python, a class can inherit features and attributes from multiple classes and thus, implements multiple inheritance. MRO or Method Resolution Order is the hierarchy in which base classes are searched when looking for a method in the parent class.



- [怎么用 Python 发布 HTTP/2 ](https://medium.com/@pgjones/how-to-serve-http-2-using-python-5e5bbd1e7ff1) 
    + HTTP2

The simplest way to serve HTTP/2 is to use the Quart framework, furthermore Quart is the only Python framework to support server-push.



- [如何用 Python 搞出快速随机子集抽样](https://medium.freecodecamp.org/how-to-get-embarrassingly-fast-random-subset-sampling-with-python-da9b27d494d9)
    + machine learning

Imagine that you are developing a machine learning model to classify articles. You have managed to get an unreasonably large text file which contains millions of identifiers of similar articles that belong to the same class. You are unsure whether identifiers that are close to each other are independent.



- [迭代器和可迭代 - Agiliq Blog](http://agiliq.com/blog/2017/10/iterators-and-iterables/#.Wd9kLZkpcd0.twitter)
    + core-python

- [如何用 Python 在 Medium 中找到有趣的人来追踪](https://medium.freecodecamp.org/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0)
    + scraping, codesnippets

Medium has a large amount of content, a large number of users, and an almost overwhelming number of posts. When you try to find interesting users to interact with, you’re flooded with visual noise. I define an interesting user as someone who is from your network, who is active, and who writes responses that are generally appreciated by the Medium community.

(`是也乎:`

可惜, Medium 第一时间和谐掉了...

)


- [深度数学机器学习 learning.ai](https://medium.com/deep-math-machine-learning-ai) 
    + machine learning, math

(`是也乎:`

简单的说 .ai 的好域名已经抢光了..

)

Explained using Python code snippets.

- [livepython - 实时跟踪运行时 Python 代码](https://github.com/agermanidis/livepython)
    + tracing code execution

Watch your Python run like a movie.

(`是也乎:`

![livepython](https://camo.githubusercontent.com/85a3519050f3390662d93f529c548d3e72d0cae4/68747470733a2f2f692e696d6775722e636f6d2f33366f456833522e676966)

象看电影一样观察你的python 代码的运行...

好吧, 对新手很重要...

)


- [Facebook 中 Python  版本的状态](https://twitter.com/llanga/status/916460954128285696)
    + tweet

- [K均值聚类 在 Python](https://mubaris.com/2017-10-01/kmeans-clustering-in-python?ref=hn)
    + machine learning

Clustering is a type of Unsupervised learning. This is very often used when you don’t have labeled data. K-Means Clustering is one of the popular clustering algorithm. The goal of this algorithm is to find groups(clusters) in the given data. In this post we will implement K-Means algorithm using Python from scratch.


- [8 best languages to blog about](https://www.databrawl.com/2017/10/08/blog-analysis/)
    + web crawling

(`是也乎:`

叕一则 github 公开数据的嗯哼
)


## 好物
~ 包/模块/库/片段...

- [magic-the-gifening](https://github.com/minimaxir/magic-the-gifening)
    - 146 Stars, 6 Fork

A Twitter bot which tweets Magic: the Gathering cards with appropriate GIFs superimposed onto them.

(`是也乎:`

![howl_from_beyond](https://github.com/minimaxir/magic-the-gifening/raw/master/howl_from_beyond.gif)

是的, 就是专门用来对 Twitter 发射 gif 动画的工具.

)


- [mailproxy](https://github.com/kz26/mailproxy)
    - 94 Stars, 4 Fork

mailproxy is a simple SMTP proxy. It receives emails through an unencrypted, unauthenticated SMTP interface and retransmits them through a remote SMTP server that requires modern features such as encryption and/or authentication. mailproxy is primarily useful for enabling email functionality in legacy software that only supports plain SMTP.

(`是也乎:`

简单的说, 就是个简单的可内置的 SMTP 服务器?

)

- [RobinhoodShell](https://github.com/anilshanbhag/RobinhoodShell)
    - 30 Stars, 4 Fork

A command line shell for trading stocks using Robinhood

(`是也乎:`

![RobinhoodShell](https://camo.githubusercontent.com/f3ee537c42d878fc4186fe5e98a387b48d8ef534/68747470733a2f2f692e696d6775722e636f6d2f586a72745958422e706e67)
)

- [InstagramLib](https://github.com/OlegYurchik/InstagramLib)
    - 26 Stars, 4 Fork

Library for interaction with Instagram web-interface. If you haven't access to Instagram API, you can use this library

(`是也乎:`

为 Instagram 专门建立的自拍用博物馆都有了, 当然的 CLI 工具也越来越多了...
)


- [CSRF-tutorial](https://github.com/twtrubiks/CSRF-tutorial)
    - 17 Stars, 2 Fork

Use Django To Introduce CSRF and Cookies , Session

- [verpy](https://github.com/tstringer/verpy)
    - 6 Stars, 0 Fork

Python application versioning tool

(`是也乎:`

![verpy](https://github.com/tstringer/verpy/raw/master/demo.gif)

所以, 应用的版本查询器...

)

- [tably](https://github.com/narimiran/tably)
    - 0 Stars, 0 Fork

Python script for converting .csv data to LaTeX tables.

(`是也乎:`

一看就知道是论文党的嗯哼...

)

- [pythonrc](https://github.com/lonetwin/pythonrc/)
    - 0 Stars, 0 Fork

This is a python script intended to improve on the default Python interactive shell experience.

(`是也乎:`

参考演示视频: [asciicast:134711 - asciinema](https://asciinema.org/a/134711?speed=2)

基本上就是将 python 的默认交互提升到了普通的 shell 水平..
只是, 有了 ipynb 为毛要用普通的 REPL ?

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
- PyConChina2017 议题征集开始
    + 申报开始

申报表单: https://jinshuju.net/f/2ag6QB

中国的PyCon大会已经组织了6年，在第7年PyCon大会之际，Python3已经成熟，比如Instagram迁移到了Python3。而人工智能方兴未艾，区块链、物联网、AR、VR、机器人等领域创新不断涌现。

本大会以“大数据和人工智能技术的创新应用”为主题，将由丰富的内容和议题组成，着重探讨如何使用Python技术进行大数据和人工智能的技术开发和最佳实践，并结合具体的产品和行业发展趋势，分享不同类型的应用、场景下的开发和运营经验。

...

今年PyConChina2017将在两个城市举办，上海定档:

    2017年10月22日 8:30 ～ 17:00 

- [【上海场】PyConChina2017](http://www.huodongxing.com/event/3403439712600?td=8211933664158)
  + **[--> 主题申报](https://jinshuju.net/f/2ag6QB)** 
  + [---> 门票购买](http://www.huodongxing.com/event/3403439712600?td=8211933664158)

(`是也乎:`

结果立即在 CPyUG 列表中引发了各种嗯哼,
并有行者组织了议题问卷, 得到稍有不同的期待,
所以, 大会的举行真心得看坚持了.
)

## 是也乎

- 171013 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171013 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


