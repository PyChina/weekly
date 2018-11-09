Title: 蠎加载 187
Slug: importpython-187
Date: 2018-11-09 11:42
Tags: Weekly,ImportPython,Zh


![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 187](http://importpython.com/newsletter/no/187/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**
- 最近官方更新的不规律, 俺也不好按时自造...

## 该读
~ 文章, Blog, 教程...


- [优化 Django Admin Paginator](https://medium.com/@hakibenita/optimizing-django-admin-paginator-53c4eb6bfca3)
    + admin

In almost every project we work on, we use Django admin for support and operations. Over time we experienced an influx of new users and the amount of data we had stored grew rapidly. With a large dataset we started to experience the real cost of some Django admin features.

(`是也乎:`

是的, 这么多年了, Django 后台依然是无法令人满意的 UX 重灾区

)


- [Python 中的文本预处理: 步骤，工具和示例](https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908)
    + text preprocessing

In this paper, we will talk about the basic steps of text preprocessing. These steps are needed for transferring text from human language to machine-readable format for further processing. We will also discuss text preprocessing tools.

- [桌面 Python 应用程序中的崩溃报告](https://blogs.dropbox.com/tech/2018/11/crash-reporting-in-desktop-python-applications/)
    + python, desktop

One of the greatest challenges associated with maintaining a complex desktop application like Dropbox is that with hundreds of millions of installs, even the smallest bugs can end up affecting a very large number of users. Bugs inevitably will strike, and while most of them allow the application to recover, some cause the application to terminate. These terminations, or “crashes,” are highly disruptive events: when Dropbox stops, synchronization stops. To ensure uninterrupted sync for our users we automatically detect and report all crashes and take steps to restart our application when they occur.

(`是也乎:`

DropBox 选择 Py 来开发桌面软件, 
结果现在有了世界最大 Py 桌面应用崩溃样本库..

)

- [介绍用 Pandas 在 Python 中进行数据分析的温和视觉](https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/)
    + panfas

If you’re planning to learn data analysis, machine learning, or data science tools in python, you’re most likely going to be using the wonderful pandas library.

- [Algojammer](https://github.com/ChrisKnott/Algojammer)
    + editor

Algojammer is an experimental, proof-of-concept code editor for writing algorithms in Python. It was mainly written to assist with solving the kind of algorithm problems that feature in competitions like Google Code Jam, Topcoder and HackerRank.

(`是也乎:`

专门为了几大定期竞赛, 嗯哼出来的算法理解工具

![Algojammer](https://github.com/ChrisKnott/Algojammer/raw/master/README/Algojammer.gif)

可视化过程...

)


- [CSI: Python 类型系统](https://blog.daftcode.pl/csi-python-type-system-episode-2-baf5168038c0)
    + mypy

In the first episode, we got to the bottom of the error reported by mypy: we understood exactly what was wrong with the initial code and why it wasn’t type-safe. Now, we need to do something about it. The goal of this episode is not to give the ultimate solution to the problem, but to approach it from different perspectives and provide some (fairly simple) suggestions. Choosing and implementing the right one depends on the specific use case.

(`是也乎:`

为了性能, Python 一头扎向 C# 的方向

)


- [Vespene](http://docs.vespene.io/)
    + build server

Vespene is a modern, streamlined build and self-service automation platform. Vespene is designed to combat chaos in complex software development and operations environments. Our mission is simple: get great people together to build the ultimate system we all want to use.


(`是也乎:`

![vespene_logo](http://docs.vespene.io/_images/vespene_logo.png)

> ... 让伟大的人们共同建立我们都想要使用的终极系统.

叕一个构建平台.


)


- [经济学诺贝尔奖获得者 Paul Romer 是位转变过来的 Pythoneer](https://qz.com/1417145/economics-nobel-laureate-paul-romer-is-a-python-programming-convert/)
    + adoption

Bragging rights?

(`是也乎:`

够拿来吹牛了...

)


- [Michelangelo PyML: 推出优步快速 Python ML 模型开发平台 - 优步工程博客](https://eng.uber.com/michelangelo-pyml/)
    + machine learning

As a company heavily invested in AI, Uber aims to leverage machine learning (ML) in product development and the day-to-day management of our business. In pursuit of this goal, our data scientists spend considerable amounts of time prototyping and validating powerful new types of ML models to solve Uber’s most challenging problems (e.g., NLP based smart reply systems, ticket assistance systems, fraud detection, and financial and marketplace forecasting). Once a model type is empirically validated to be best for the task, engineers work closely with data science teams to productionize and make it available for low latency serving at Uber-scale. This cycle of prototyping, validating, and productionizing is central to ML innovation at Uber, and the less friction at each stage of this process, the faster Uber can innovate.

(`是也乎:`

> 米开朗基罗PyML

名字起的好.
)


- [国际象棋比赛的 ChessViz 图表](https://medium.com/@andreasstckl/chessviz-graphs-of-chess-games-7ebd4f85a9b9)
    + chess, game

ChessViz reads a chess game as pgn-file and generates a visual representation of the game as chart. The chart shows how the game developed, who was in front, which moves were critical, which moves were forced and different sections (like rookending) of the game are marked. ChessViz is implemented in Python with the packages “python-chess” (https://pypi.org/project/python-chess/) and “plotly” (https://plot.ly/python/).



## 好物
~ 包/模块/库/片段...


- [kamerka](https://github.com/woj-ciech/kamerka)
    - 416 Stars, 48 Fork

Build interactive map of cameras from Shodan

(`是也乎:`

> ꓘamerka

![kamerka](https://camo.githubusercontent.com/28b92f2a21254307f4b674fc306d6c3901278e04/68747470733a2f2f692e696d6775722e636f6d2f3653486a5564492e706e67)


)


- [waveglow](https://github.com/npuichigo/waveglow)
    - 132 Stars, 21 Fork

A PyTorch implementation of the WaveGlow: A Flow-based Generative Network for Speech Synthesis


(`是也乎:`

语音识别的 PyTorch 嗯哼

)


- [mpDNS](https://github.com/nopernik/mpDNS)
    - 60 Stars, 11 Fork

Multi-Purpose DNS Server

(`是也乎:`

神奇的兼容 Py2/3 原生 DNS 服务
)


- [StarGAN-Voice-Conversion](https://github.com/hujinsen/StarGAN-Voice-Conversion)
    - 25 Stars, 0 Fork

This is a tensorflow implementation of the paper: StarGAN-VC: Non-parallel many-to-many voice conversion with star generative adversarial networks https://arxiv.org/abs/1806.02169


(`是也乎:`

叕一则根据论文撸出来的嗯哼

)


- [instadp](https://github.com/sdushantha/instadp)
    - 19 Stars, 5 Fork

Download any users Instagram display picture/profile picture in full quality

(`是也乎:`

Ins. 生态也越来越有王者之风了,,,
可惜 Flickr ...

)


- [XanXSS](https://github.com/Ekultek/XanXSS)
    - 14 Stars, 0 Fork

A simple XSS finding tool

(`是也乎:`

![XanXSS](https://user-images.githubusercontent.com/14183473/48165682-f1dede00-e2ab-11e8-8c33-4cd8d909b760.png)

)

- [lswriteups](https://github.com/mzfr/lswriteups)
    - 12 Stars, 1 Fork

CLI tool to get the links of original writeups from ctftime.org

(`是也乎:`


好象上期嗯哼过, 类似专门网站的专用工具,
其实, 嘦接口稳定, 任何一个服务网站都应该有 CLI 工具...
至少方便自己工程师运维了.

)


- [tfmodel](https://github.com/tobegit3hub/tfmodel)
    - 4 Stars, 0 Fork

Command-line tool to inspect TensorFlow models

(`是也乎:`

叕一则 TF 工具.

)

- [django-find](https://github.com/knipknap/django-find)
    - 9 Stars, 0 Fork

Easily add search functionality to Django projects

(`是也乎:`

好象其它 web 框架都沉默了, 就 Django 在狂热的积累生态...

)

- [djangohunter](https://github.com/6IX7ine/djangohunter)
    - 12 Stars, 6 Fork

Tool designed to help identify incorrectly configured Django applications that are exposing sensitive information.


- [django-auth-tutorial-example](https://github.com/sibtc/django-auth-tutorial-example)
    - 5 Stars, 2 Fork

Django Authentication Video Tutorial


- [django-postgres-unlimited-varchar](https://github.com/jacobian/django-postgres-unlimited-varchar)
    - 4 Stars, 0 Fork

A tiny app adding support unlimited varchar fields (no specified max length) in Django/Postgres. 

(`是也乎:`

postgres 在 MySQL 嗯哼后, 越来越嗯哼...

)


### (￣▽￣)

- [PyCon 2018 China](http://cn.pycon.org/2018/)
    + 来了, 真的来了


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...

- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)

## 是也乎

- 181109 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 181109 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


