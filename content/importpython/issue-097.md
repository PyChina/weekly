Title: 蠎加载 97
Slug: importpython-97
Date: 2016-11-05 15:51
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 97](http://importpython.com/newsletter/no/97/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [Pyvisgraph - Python 可见性图表](https://github.com/TaipanRex/pyvisgraph)
    + visualization, opensource project

This is a super cool project build by Christian. Pyvisgraph builds a visibility graph given a set of simple obstacle polygons and find the shortest path between two points. Christian uses it at work for mapping vessel voyages.( Vessel as in ships ). Here are two blog post by him talking about the algorithm behind his code 

https://taipanrex.github.io/2016/09/17/Distance-Tables-Part-1-Defining-the-Problem.html 

and 

https://taipanrex.github.io/2016/10/19/Distanlogce-Tables-Part-2-Lees-Visibility-Graph-Algorithm.html .


(`是也乎:`

![example](https://github.com/TaipanRex/pyvisgraph/raw/master/docs/images/example.png)

可见性,以往用来寻找可以看见灯塔的安全航线的技术,
现在可以自动完成了.

)

- [Chat bots 以及如何在 Alexa 上构建](https://medium.com/@krishnateja_182/chat-bots-and-how-to-build-one-on-alexa-35772e429631#.hsod1cwhi)
    + chatbots

Talking to technology has taken a whole new level since Amazon has announced their voice assistant Alexa and opened up their platform for developers to build custom bots just like when Apple announced about app store for developers to create and sell apps. Here I wanted to talk about the ease of building an Alexa skill using python which could be used as information provider to a attendee for a conference.

(`是也乎:`

Amazon 的语音助理 Alexa 平台化后,
当然就可以任性的调教了...
)


- [6 个快速调试技巧](https://ironboundsoftware.com/blog/2016/10/31/6-quick-python-debugging-tips/)
    + debugging

Nick gives us quick tour of debugging in Python. print statements, logging, pdb, pdb++, Debugging from the REPL and more.


(`是也乎:`

再多的调试技巧,也无法弥补混乱的头脑写出的代码,
所以,亲!最重要的调试技巧就是保持充分的睡眠哪!
)

- [俺就是整不明白 Python 的 Asyncio](http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio)
    + async-io

Armin Ronacher's creator of Flask takes at length candidly about How it's difficult for him to grasp Asyncio , it's shortcomings, how David Beazley's live demo hacked up asyncio replacement is twice as fast as it. Curator's Note - Personally I learned Asyncio from the book Fluent Python. However once I went beyond the simple examples and try building something non trivial I ended up switching to golang and getting my job done faster. One key reason is the benchmark showed my asyncio's throughput was an order of magnitude slower, code required a lot of hand holding for a new developer.

(`是也乎:`

创造者分享了为什么人们理解了异步都都去用 golang 了...
这真是一个悲伤的故事.
)

- [避免被 Python 咬屎](https://medium.com/rmotr-com/avoiding-being-bitten-by-python-161b063e7da2#.exz387rth)
    + core python

Common pitfalls to avoid when writing Python software

(`是也乎:`

py coding 时常见的错误
)

- [django-sql-explorer](https://github.com/groveco/django-sql-explorer)
    + django

Easily share data across your company via SQL queries. From Grove Collab.


- [用 Daphne 部署 Django Channels](http://masnun.rocks/2016/11/02/deploying-django-channels-using-daphne/)
    + django channels

Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI, and developed to power Django Channels. It supports automatic negotiation of protocols; there’s no need for URL prefixing to determine WebSocket endpoints versus HTTP endpoints. In this blog post Abu Ashraf shows us how to Deploy Django channels using Daphne.

(`是也乎:`

Channels 如此重要,又如此难用,所以,
Django 创建了: ASGI 协议的专用服务器 Daphne
)


- [每周聊 Python: Dates 和 Times 在 Python](http://ccst.io/e/datetime)
    + video

Let's chat about working with dates and times in Python! We'll talk about parsing, formatting, timezones, and date arithmetic.

(`是也乎:`

简单的说,就是心塞,每次总感觉厂商有更加简洁的日期/时间处理手段的,,,
然而...
)


- [Jupyter Notebook 教程](https://medium.com/@deniskasyanov/jupyter-notebook-tutorial-9c0ffa5ae9a1#.85l75dx3t)
    + jupyter

I want to share some concepts and ideas about using Jupyter Notebook that I would like to know when I started.

(`是也乎:`

medium 越来越好用了,所以,也早已被 功夫网 认证了...
)


- [如何在 Django 管理中追加自制按钮 - By Haki Benita](https://medium.com/@hakibenita/how-to-add-custom-action-buttons-to-django-admin-8d266f5b0d41#.6mo5v8pe1)
    + django admin panel

In this post Haki Benita shows us how he extended Django admin to include two Button which perform action on a record/row. It's a well written step by step article to accomplish the task.



- [将媒体内容从 Linux 折腾到 Chromecast](https://andreafortuna.org/streaming-media-contents-from-linux-to-chromecast-e938dec695f6#.lphwph8ri)
    + opensource project

Are you searching for an easy way to stream media files from your LinuxBox to a Chromecast ? You can use Stream2chromecast, a simple Python script that makes the task of streaming media files to a Chromecast device ridiculously easy.

(`是也乎:`

WIDI 世界中,怎么可以少 Python 脚本?!
)

- [Pandas 教程: Python 中的 DataFrames](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)
    + pandas

Karlijn has written good article explaning what dataframes is and it's workings. If you don't know about Pandas and want to get a sense of what it's ?, then have a read.


- [用 Kafka 来构建 Python 中的简单 Job Queue](https://github.com/joowani/kq)
    + kafka, opensource project

KQ (Kafka Queue) is a light-weight Python library which provides a simple API to queue and process jobs asynchronously in the background. It is backed by Apache Kafka and designed primarily for ease of use.

(`是也乎:`

KQ 一个专用模块,可以 Pythonic 化的使用 Kafka
)

- [从 NumPy 榨取更多性能 ](http://ipython-books.github.io/featured-01/)
    + numpy

This is the first featured recipe from the IPython Cookbook, the definitive guide to high-performance scientific computing and data science in Python.

(`是也乎:`

来自 [IPython Cookbook](http://ipython-books.github.io/cookbook/) 的经典技巧
)

- [C++ vs. Python vs. PHP vs. Java vs. Others 性能评测 (2016 Q3)](https://blog.famzah.net/2016/09/10/cpp-vs-python-vs-php-vs-java-vs-others-performance-benchmark-2016-q3/)
    + benchmark

The benchmarks here do not try to be complete, as they are showing the performance of the languages in one aspect, and mainly: loops, dynamic arrays with numbers, basic math operations.

(`是也乎:`

看起来 Py3 已经快过 Py2.7 了...
)

- [Pycon Pune 2017](https://pune.pycon.org/)
    + pycon

Pycon Pune 2017 is announced. To be held on February 16-19 2017. Visit the website to know more.

(`是也乎:`

又是一月就开始的...总结去年的当然早点开始好,
但是, PyConChian 的筹备节奏,我们只能程序猿节前后才可能折腾
)


## 项目
~ 包/模块/库/片段...

- [predicting_stock_prices](https://github.com/llSourcell/predicting_stock_prices)
    - 29 Stars, 14 Fork

This is the code for the Stock Price Prediction challenge for 'Learn Python for Data Science #3' by @Sirajology on YouTube. The code uses the scikit-learn machine learning library to train a support vector regression on a stock price dataset from Google Finance to predict a future price. In the video, I use scikit-learn to build an ML model, but for the challenge you'll use the Keras library.

(`是也乎:`

基于 Keras 和 Google 财经的数据,
使用 scikit-learn 来完成预测
)

- [altair_widgets](https://github.com/altair-viz/altair_widgets)
    - 25 Stars, 1 Fork

Interactive data exploration with Altair. Altair Widgets are a tool to easily allow to interact with Altair graphs in the Jupyter notebook.

(`是也乎:`

对 Altair 图表在 Jupyter 进行交互探索的工具

![examples](https://github.com/altair-viz/altair_widgets/raw/master/examples/iris-basic.gif)

)

- [py-vm](https://github.com/afiskon/py-vm)
    - 19 Stars, 0 Fork

Simple CLI wrapper for VirtualBox. Could be considered a Vagrant replacement in many cases.

(`是也乎:`

又一个对 VirtualBox 进行 CLI 包装的工具
)

- [django-traffic](https://github.com/koslibpro/django-traffic)
    - 8 Stars, 0 Fork

A Django middleware that helps visualize your app's traffic in Kibana. In a nutshell, by using this middleware you need no more effort to stream your app's traffic in your ElasticSearch host(s) and use Kibana for visualizations around it.

(`是也乎:`

又一个重量级中间件,
可视化 Kibana 的工作流
)

- [algorithms](https://github.com/thecodershub/algorithms)
    - 7 Stars, 46 Fork

Collection of algorithms in multiple programming languages. Including Python. 

(`是也乎:`

算法的对比学习
)

# 是也乎

- 161106 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161106 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


