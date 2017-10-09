Title: 蠎加载 145
Slug: importpython-145
Date: 2017-10-07 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 145](http://importpython.com/newsletter/no/145/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [用 Python 和条件随机字段进行拉丁语分词](https://medium.com/@felixmohr/using-python-and-conditional-random-fields-for-latin-word-segmentation-416ca7a9e513)
    + NLP

In this article, a CRF (Conditional Random Field) will be trained to learn how to segment Latin text. Using only very basic features and easily accessible training data, we are going to achieve a segmentation accuracy of 98 %.

- [Python 中的 K均值聚类](https://mubaris.com/2017-10-01/kmeans-clustering-in-python)
    + machine learning

Clustering is a type of Unsupervised learning. This is very often used when you don’t have labeled data. K-Means Clustering is one of the popular clustering algorithm. The goal of this algorithm is to find groups(clusters) in the given data. In this post we will implement K-Means algorithm using Python from scratch.

- [Lifelong Rubyist 使一些 Python 代码 5x 加速](https://www.schneems.com/2017/10/02/lifelong-rubyist-makes-some-python-code-5x-faster/)
    + performance

n this post I’m going to look at a bit of Python code I optimized recently, and then compare the process of making this code faster to the process of how I make Ruby code faster.



- [Alice 在 Python 项目中](https://veekaybee.github.io/2017/09/26/python-packaging/)
    + core-python

Python project structure and packaging can be intimidating, but, if you take it step by step, it doesn’t have to be. Look at other people’s code, particularly smaller, modular projects, break the work up into pieces, and work through it piece by piece, until you’re all the way down the rabbit hole.

(`是也乎:`

![alice_cards](https://raw.githubusercontent.com/veekaybee/veekaybee.github.io/master/images/alice_cards.jpg)

项目代码/结构的腐化速度和项目的活跃度是直接关联的

)


- [WSGI 还未够班 — 第一部分](https://medium.com/@amitn241/wsgi-is-not-enough-anymore-part-i-bc9713a79841)
    + wsgi

This is the first part of a multi-part series discussing the limitation of WSGI-based Python web applications and the ways to overcome these limitations.

- [WSGI 还未够班 — 第二部分](https://medium.com/@amitn241/wsgi-is-not-enough-anymore-part-ii-b78b4cfdd09)
    + wsgi

In the first part of this series we discussed the problems and limitations which inheres within WSGI-based Python web applications. In this part we will discuss what concurrency is and what is an event driven architecture

- [Go vs CPython: 并发和并行选项的可视化对决](https://labs.getninjas.com.br/go-vs-cpython-visual-comparison-of-concurrency-and-parallelism-d29a1ebec20a)
    + concurrency, parallelism

Using MPG diagrams to see the differences between Threading, Multiprocessing and Asyncio, the 3 official CPython options, and Go Runtime.


(`是也乎:`

对 [google/grumpy: Grumpy is a Python to Go source code transcompiler and runtime.](https://github.com/google/grumpy) 的强烈召唤..
)


- [用 Python 评估风险和返回事件的概率](https://medium.com/python-data/assessing-risks-and-return-with-probabilities-of-events-with-python-c564d9be4db4)
    + statistics, quant

There are various situations where quants look at different scenarios of an event when making investment decisions. Running simulated scenarios is an invaluable tool for all finance/investment managers as it allows them to measure likely performance for various states.

- [监视，记录和提醒 Linux 上 CPU 的过载](https://medium.com/@trstringer/monitor-log-and-alert-cpu-throttling-from-an-overheating-cpu-on-linux-256c28422c)
    + code snippets

I wrote a Python script (GitHub) that does a few things. First and foremost, I wanted to know every minute on the minute what my CPU core temps were regardless of whether I’m getting throttled or not so that I had the option to chart this (I haven’t done this, as I think I’ve found the culprit but I wanted to keep my options open). I also wanted to know if my laptop fan was functioning as desired in relation to the CPU temps, so I needed to grab fan RPM.


(`是也乎:`

Lenovo T420s 上运行的 Linux 中的自制监察脚本...
[tstringer/linux\-core\-temperature\-monitor: Script \(meant to run via cron\) to monitor, log, and alert when the CPU is throttled due to overheating](https://github.com/tstringer/linux-core-temperature-monitor)

可是 Glances 全部嗯哼了哪...

)

- [搞一个 BT Torrent 客户端：第1步](https://medium.com/@kimberly_mc/writing-a-bit-torrent-client-step-1-6cefb256fe87)
    + code snippets

- [介绍在 Python 中使用 NetworkX 进行图形优化](https://www.datacamp.com/community/tutorials/networkx-python-graph-tutorial)
    + networkx

This NetworkX tutorial will show you how to do graph optimization in Python by solving the Chinese Postman Problem in Python.

(`是也乎:`


![NetworkX](https://gist.githubusercontent.com/brooksandrew/2a70bbc88899791241cfb88be1372f44/raw/87d1a0ce438d6f4d9a23ce89df2984cbe30ba993/sleeping_giant_cpp_route_animation.gif)

是的, 完备的了...

)

- [设计 Python 固定大小的散列图](https://medium.com/@stephenslee0127/design-a-fixed-size-hash-map-in-python-bd579f57dc9c)
    + core-python, dict

implement a fixed-size hash map that associates string keys with arbitrary data object references.

- [Flask-SocketIO](http://flask-socketio.readthedocs.io/en/latest/)
    + flask

Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server. The client-side application can use any of the SocketIO official clients libraries in Javascript, C++, Java and Swift, or any compatible client to establish a permanent connection to the server.

- [Python Release Python 3.6.3](https://www.python.org/downloads/release/python-363/)
    + new release

Python 3.6.3 is the third maintenance release of Python 3.6. The Python 3.6 series contains many new features and optimizations. See the What’s New In Python 3.6 document for more information.

- [用 Spark 交互分析 100GB 的 JSON 数据](https://medium.com/towards-data-science/interactively-analyse-100gb-of-json-data-with-spark-e018f9436e76)
    + spark

Do you know what is the heaviest book ever printed? Let’s find out by exploring the Open Library data set using Spark in Python.

(`是也乎:`

港真, 100G 现在只是小数据了...
关键是 Open Library 数据集的存在, 用来找最重的书?
)

- [Parallel Processing in Python](http://stackabuse.com/parallel-processing-in-python/)
    + multiprocessing







## 好物
~ 包/模块/库/片段...


- [milksnake](https://github.com/getsentry/milksnake)
    - 69 Stars, 1 Fork

A setuptools/wheel/cffi extension to embed a binary data in wheels.

(`是也乎:`

奶蛇~将必要的二进制资源嗯哼到包中

)

- [pcap2curl](https://github.com/jullrich/pcap2curl)
    - 60 Stars, 12 Fork

Read a packet capture, extract HTTP requests and turn them into cURL commands for replay.

(`是也乎:`

叕一个 cURL 加强/转换工具

)

- [dockselpy](https://github.com/dimmg/dockselpy)
    - 59 Stars, 4 Fork

Dockerized Selenium and Python with support for Chrome and Firefox.

(`是也乎:`

Xfvb 的威力加载
)

- [python-plexlibrary](https://github.com/adamgot/python-plexlibrary)
    - 20 Stars, 0 Fork

Create and maintain dynamic Plex libraries based on recipes.

- [bigquery_fdw](https://github.com/gabfl/bigquery_fdw)
    - 11 Stars, 2 Fork

BigQuery Foreign Data Wrapper for PostgreSQL.

- [TeamFlowy](https://github.com/kingname/TeamFlowy)
    - 5 Stars, 1 Fork

A simple sync tool to sync task from Workflowy to Teambition.

(`是也乎:`

没有开放接口, 这种跨平台的嗯哼是不可想象的...

)

- [art](https://github.com/sepandhaghighi/art)
    - 5 Stars, 0 Fork

Simple ASCII Art Library For Python 

(`是也乎:`

叕一个 CLI 的艺术工具..


    >>> from art import *
    >>> aprint("butterfly")
    Ƹ̵̡Ӝ̵̨̄Ʒ 
    >>> aprint("happy")
     ۜ\(סּںסּَ` )/ۜ 
    >>> art_1=art("coffee")
    >>> print(art_1)
    c[_] 
    >>> tprint("art")

     .----------------.  .----------------.  .----------------.
    | .--------------. || .--------------. || .--------------. |
    | |      __      | || |  _______     | || |  _________   | |
    | |     /  \     | || | |_   __ \    | || | |  _   _  |  | |
    | |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |
    | |   / ____ \   | || |   |  __ /    | || |     | |      | |
    | | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |
    | ||____|  |____|| || | |____| |___| | || |   |_____|    | |
    | |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'


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

- 170922 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170922 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


