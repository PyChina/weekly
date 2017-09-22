Title: 蠎加载 143
Slug: importpython-143
Date: 2017-09-22 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 143](http://importpython.com/newsletter/no/143/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [如何在一小时内建立书籍推荐系统第1部分 - 基础知识](https://medium.com/towards-data-science/how-did-we-build-book-recommender-systems-in-an-hour-the-fundamentals-dfee054f978e)
    + machine learning

Building recommender systems today requires specialized expertise in analytics, machine learning and software engineering, and learning new skills and tools is difficult and time-consuming. In this post, we will start from scratch, covering some basic fundamental techniques and implementations in Python. In the future posts, we will cover more sophisticated methods such as content-based filtering and collaborative based filtering.

(`是也乎:`

pandas->nb->k-Nearest->...

[Machine\-Learning\-with\-Python/Recommender Systems \- The Fundamentals\.ipynb at master · susanli2016/Machine\-Learning\-with\-Python](https://github.com/susanli2016/Machine-Learning-with-Python/blob/master/Recommender%20Systems%20-%20The%20Fundamentals.ipynb)

是的 jupyter 上直接撸的

)

- [我们如何在一小时内建立书籍推荐系统第2部分 - k最近的邻居和矩阵...](https://medium.com/towards-data-science/how-did-we-build-book-recommender-systems-in-an-hour-part-2-k-nearest-neighbors-and-matrix-c04b3c2ef55c)
    + machine learning

In the last post, we saw how we could use simple correlational techniques to create a measure of similarity between the books’ users based on their rating records. In this post, we will explain how you can use those same sort of similarity metrics to recommend books to a book’s readers.


- [Python Gem #19: 查找表 > if chain](https://medium.com/@adamshort/python-gem-19-look-up-table-if-chain-167d83ab1838)
    + core-python

What should be a really simple function has turned into a fifty-line gargantuan that’s too hard to read properly because of the sheer number of lines. The culprit; a seriously long if-elsif-else chain. But not to fear; there’s a better way!

- [最饭的可怕错误消息<- Python](http://blog.lerner.co.il/favorite-terrible-python-error-message/)
    + core-python

> TypeError: object() takes no parameters


- [在 Python 中构建微处理器模型的TDD方法](http://joaoventura.net/blog/2017/simple-microprocessor/)
    + simulator

Modern microprocessors are a very complex piece of machinery with a lot of different parts. I've learned assembler and microprocessors in my undergraduate course some years ago but, as I've been working on higher level software languages for quite some time now, I forgot many things. Lately I decided to revisit some of the topics on microprocessors and to build a very simple model of a microprocessor in Python for education purposes (I work as CS professor). You can find the final source code and some samples at https://github.com/joaoventura/simproc.

- [Python 中制作 4 种交互式 Sankey 图 – plotly – Medium](https://medium.com/@plotlygraphs/4-interactive-sankey-diagram-made-in-python-3057b9ee8616)
    + charts

Plotly has a new member of the Plotly.js chart family: The Sankey diagram. Jupyter notebook is at above the footnote of the blogpost.

(`是也乎:`

所谓蛇窝图...
)

- [大都会 Manila 的交通状态图](https://medium.com/@miguell.malacad/mapping-traffic-accidents-in-metro-manila-9a002eb0fa19)
    + data science

I got my hands on a dataset on traffic accidents in Metro Manila early this year, and decided to enter the realm of data science with a simple cleaning and visualization project. The primary goal: supplement the dataset’s human readable location data with geographic coordinates.

- [CPython 内部: 任意精度整数实现](https://rushter.com/blog/python-integer-implementation/)
    + cpython

Have you ever noticed that Python supports integers of any size? Here is a quick glance at it.


- [使用 webhooks 和 Python3 请求API 向 Slack 发送消息](https://notes.ayushsharma.in/2017/09/posting-messages-to-slack-using-incoming-webhooks-and-python-requests-api)
    + slack

I wanted to make a short post on using Slack’s incoming webhooks feature to post messages to Slack using the human-friendly Requests API in Python3.



- [DevS 不知不觉中使用“恶意”模块窃取到官方的 Python 存储库 | Ars Technica](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/)
    + pypi

Code packages available in PyPI contained modified installation scripts.

- [Jupyter, python, 图像压缩和 svd](https://medium.com/@rameshputalapattu/jupyter-python-image-compression-and-svd-an-interactive-exploration-703c953e44f6)
    + jupyter

In this short blogpost, I will explore few topics to illustrate the interactivity of the jupyter environment and the python availability of high quality libraries in the ecosystem.



- [用 python 构建桌面通知工具](https://www.codementor.io/dushyantbgs/building-a-desktop-notification-tool-using-python-bcpya9cwh)
    + desktop app

The term desktop notifications refer to a graphical control element that communicates certain events to the user without forcing them to react to this notification immediately. In other words, it is a simple application which produces a notification message in form of a pop-up message on desktop.


(`是也乎:`

关键是跨平台哪亲...notify 已经挫了,所以, notify2?

NotifyOSD,[takluyver / pynotify2 — Bitbucket](https://bitbucket.org/takluyver/pynotify2) ...

依赖 dbus 这个无法安装的模块....
)


- [用Python，GeoJSON 和 GeoPandas 开始地理空间分析](https://www.twilio.com/blog/2017/08/geospatial-analysis-python-geojson-geopandas.html)
    + geo

Geospatial analysis applies statistical analysis to data that has geographical or geometrical components. In this tutorial, we’ll use Python to learn the basics of acquiring geospatial data, handling it, and visualizing it. More specifically, we’ll do some interactive visualizations of the United States!


(`是也乎:`

[GeoPandas](http://geopandas.org/) 哗...

关键直接支持 中国地图...
)

- [用 Python 进行自动化 Web 分析](https://rrighart.github.io/GA/)
    + analytics

The current blog deals with the case how to implement web analytics in Python. I am enthusiastic about the options that are available inside Google Analytics. Google Analytics has a rich variety of metrics and dimensions available. It has a good visualization and an intuitive Graphic User Interface (GUI). However, in certain situations it makes sense to automate webanalytics and add advanced statistics and visualizations. In the current blog, I will show how to do that using Python.

- [TransitFlow — 用 Python 处理可视化区域转接频率](https://mapzen.com/blog/animating-transitland/)
    + geo

Transit networks with higher frequency and shorter waiting times will yield a more reliable and empowering experience for passengers than those with lower frequency and longer waiting times.

- [通过 Python 的 Telegram bot 远程控制 macOS](https://chatbotslife.com/remote-controlling-macos-with-a-python-telegram-bot-d656d2e00226)
    + macOS

I needed a quick way to remotely perform system operations: adjusting & muting the system volume, screen brightness, and putting the display to sleep. After exploring several options, I found none of them to be viable for me, and thus, I set out to develop my own solution.

(`是也乎:`

可惜已被和谐了, 只能借鉴思路,在其它 bot 上嗯哼了...

)


- [如何通过 Python 更好的嗯哼 GPU](https://weeraman.com/put-that-gpu-to-good-use-with-python-e5a437168c01)
    + GPU

In the example below, I’ve demonstrated how this can be done using Python in a way that doesn’t require deep knowledge of CUDA and its intricacies. For this example, I suggest using the Anaconda Python distribution, which makes managing different Python environments a breeze. Follow the download and setup instructions for Anaconda as given here for your specific operating system.

- [返回控制台：在Python中重建神奇宝贝](https://hackernoon.com/return-of-the-consoles-recreating-pok%C3%A9mon-in-python-94e0d7d860de)
    + Pokemon


(`是也乎:`

很久没有说这个游戏了...
)

- [用简单 Python 脚本创建一个 Github Gist](https://andreafortuna.org/create-a-github-gist-with-a-simple-python-script-26d3f21bb734)
    + github, gist

How to share code snippets from command line?

(`是也乎:`

一直有 API 的, 好象也有 subl 的扩展...
)


- [在运行任务时嫑弄乱俺的 芹菜](https://medium.com/@alexdaFy/dont-mess-with-the-celery-while-it-running-a-task-ec2c0808d9e0)
    + celery

Some time ago we decided to move part of our logic to celery. Several tasks was wrote and in one of them bash script was called, and this task never applied correct: first half of script was executed and then halted. I found that script running in processes, and can’t understand why it just stoped. Then I set some breakpoints in bash script and realised, that script stops at

- [在 python 机器学习中使用分类数据：从虚拟变量到深层类别...](https://blog.myyellowroad.com/using-categorical-data-in-machine-learning-with-python-from-dummy-variables-to-deep-category-66041f734512)
    + machine learning

From dummy variables to Deep category embedding and Cat2vec?—?Part 1 (Basic Methods).

- [GeoPandas 中的空间连接](https://medium.com/@bobhaffner/spatial-joins-in-geopandas-c5e916a763f3)
    + pandas

You can join two GeoPandas GeoDataFrames through conventional means with merge, but you can also use sjoin to capitalize on the spatial relationship between two frames.

- [文本向量化的初学者指南](https://monkeylearn.com/blog/beginners-guide-text-vectorization/)
    + text processing

(`是也乎:`

是的, 没中文什么事儿...

)



## 好物
~ 包/模块/库/片段...


- [face-alignment](https://github.com/1adrianb/face-alignment)
    - 165 Stars, 25 Fork

2D and 3D Face alignment library build using pytorch

(`是也乎:`

PyTorch 实例...

![alignment](https://github.com/1adrianb/face-alignment/raw/master/docs/images/face-alignment-adrian.gif)

直接完成方向识别的?

)

- [MetaDockers](https://github.com/vulhub/MetaDockers)
    - 44 Stars, 8 Fork

Responsible for visualization the vulhub or docker.

(`是也乎:`

> Vulhub Team做为以收集/制作docker漏洞靶场为基础，并发展Docker相关的开发，MetaDockers用于管理vulhub以及自实现的Docker可视化。build ing...


![Vulhub](https://camo.githubusercontent.com/8c0760882fdcc52d4d83abb5a924546d0a405ba8/687474703a2f2f3778697733312e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f337276796a61722e706e67)

所以,国货, 只是哪有命令行的自动化效能?这只是给习惯了 excel 的人员用的...

)

- [mygf-instagram](https://github.com/dzaytsev91/mygf-instagram)
    - 34 Stars, 1 Fork

Like posts of my girlfriend's Instagram using web api, don't need any api key and access tokens just login and password

(`是也乎:`

叕一个程序猿嗯哼不存在的铝朋友的好工具...
)


- [graphscii](https://github.com/etano/graphscii)
    - 3 Stars, 0 Fork

Print ASCII graphs in the terminal.

(`是也乎:`

![graphscii](https://github.com/etano/graphscii/raw/master/examples/simple.png)

怎么说呢...叕一个看图软件
只是对中文也是无解的...

)

- [xlsx2csv_gui](https://github.com/kerneltravel/xlsx2csv_gui)
    - 2 Stars, 0 Fork

Convert excel xlsx file's table to csv file, A GUI application on top of python/pyqt and other opensource softwares. 

(`是也乎:`

叕一个 office->csv 的工具, 只是这哪儿有头哪...
)


### (￣▽￣)

- [langserver\.org](http://langserver.org/)
    + 猛烈, 这才是语言和工具的正常关系吧...
- PyConChina2017 议题征集开始
    + 申报表单: https://jinshuju.net/f/2ag6QB

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


