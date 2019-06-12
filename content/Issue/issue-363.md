Title: Issue 363
Slug: issue-363
Date: 2019-04-10 23:15
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #363](https://pycoders.com/issues/363)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------


- [PEP 570 (仅位参数)已被接受](https://pycoders.com/link/1389/web)
    + PYTHON.ORG

This PEP introduces a new syntax, /, for specifying positional-only parameters in Python function definitions. Looks useful for getting tighter control over how a library API can be called (i.e. preventing positional params from being called as keyword arguments). This will also allow for some function call speed optimizations in the future.

(`是也乎:`

严格参数传输,以便优化...反正就是越来越 C++ 呗...

老爹一退休就乱来.
)


- [惯用式 Pandas: 你可能不知道的技巧和特征](https://pycoders.com/link/1408/web)
    + REAL PYTHON video

In this series you'll see how to use some lesser-used but idiomatic Pandas capabilities that lend your code better readability, versatility, and speed.

(`是也乎:`

    忘记的就是不重要的
    不知道的就是不必要
    当然世界并不是这样
    (￣▽￣)

)


- [用 PyCharm 成为 Python 大狮](https://pycoders.com/link/1341/web)
    + JETBRAINS
    + sponsor

PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development. Be more productive and save time while PyCharm takes care of the routine.


(`是也乎:`

通过 IDE 变成 guru ?

喝多了...

)


- [本地 LRU 缓存](https://pycoders.com/link/1415/web)
    + MOSHE ZADKA

How to avoid shared global state when using the functools.lru_cache decorator from the standard library.

- [Python 3.7 使用慢加载](https://pycoders.com/link/1412/web)
    + INADA NAOKI

CPython 3.7 has a new feature (-X importtime) for profiling import time and this article gives you a good overview on how to use this to reduce application startup time.

- [AvantPy: 友好的追溯](https://pycoders.com/link/1385/web)
    + ANDRÉ ROBERGE

AvantPy provides friendlier Python tracebacks, translated into various languages, to help beginners learn programming. Right now the project is still in its early stages and the maintainer is looking for contributors.

(`是也乎:`

早期...寻求志愿者...

只是, 这种追踪代码运行状态, 对于初学有什么帮助?

)


## 讨论
> Discussions


- [佛罗里达自然保护区捕获到巨大 Python ](https://pycoders.com/link/1392/web)
    + CNN.COM

17 feet and 140 pounds! Have we hit Peak Python? I don't think so... 

(`是也乎:`

17英尺, 140磅...嗯哼, 没有州厂重
)


- [将我的 Python 代码转换为 C 丫慢了30倍...](https://pycoders.com/link/1403/web)
    + REDDIT

(`是也乎:`

肿么肥四?

)


- [Python 心愿: 迭代文件中的块内容](https://pycoders.com/link/1419/web)
    + TWITTER.COM/TREYHUNNER


## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [咩是Pip? 给新鲜 Pythonist 的指南](https://pycoders.com/link/1400/web)
    + REAL PYTHON


In this beginner-friendly tutorial, you'll learn how to use pip, the standard package manager for Python, so that you can install and manage additional packages that are not part of the Python standard library.

- [如何将额外数据保存到 Django REST Framework Serializer](https://pycoders.com/link/1413/web)
    + VITOR FREITAS

Short & sweet article where you'll learn a handy pattern for passing extra data to your DRF serializers before saving them to the database.


- [新手的 Python 模块管理](https://pycoders.com/link/1409/web)
    + WOJCIECH KULIKOWSKI

A quick overview on Python dependency management with PYTHONPATH and virtual environments, and how this approach compares with Golang.

(`是也乎:`

拿 golang 的经验嗯哼 Python?

现在看来:

用 Pyenv 管理版本

用 miniconda 安装大型模块

pipenv 统一管理模块依赖


可以解决主要问题.

)


- [将 Python 和 wxPython 应用程序引入 Ubuntu App Store](https://pycoders.com/link/1417/web)
    + ANDY BULKA

How the author got his own Python app on the Ubuntu/Snapcraft app store.

- [终极指南 -> 令人难忘的技术讲座](https://pycoders.com/link/1401/web)
    + TEST & CODE 
    + podcast

Nina Zakharenko gives some great advice about giving tech talks. This episode is full of great help and encouragement for your own public speaking adventures.

- [在生产中运行 Django](https://pycoders.com/link/1402/web)
    + TALK PYTHON 
    + podcast

Mike Kennedy and Mike Herman talk about running Django in production in episode #206 of the Talk Python Podcast.

- [用 Dask 指挥 Python 开展并行计算](https://pycoders.com/link/1407/web)
    + MOSHE ZADKA

Dask is a library that scales Python computation to multiple cores or multiple machines. Setups running Dask on thousands of machines are not unheard of. This short article gives you a couple of usage examples.

(`是也乎:`

其实 Jupter 本身也可以

)


- [在 Visual Studio Code 进行 Python 开发(配置指南)](https://pycoders.com/link/1411/web)
    + REAL PYTHON 
    + video

Learn how to set up Visual Studio Code for Python development. By following examples, you'll cover everything from installing and configuring VSCode, to running tests and debugging Python apps.




## 好物
> Interesting Projects, Tools and Libraries


- [AmpliGraph: Representation Learning on Knowledge Graphs](https://pycoders.com/link/1387/web)
    + GITHUB.COM/ACCENTURE

- [Cog: Generate Text With Embedded Python Code](https://pycoders.com/link/1390/web)
    + NED BATCHELDER


(`是也乎:`

神奇, 自动转化为其它语言代码

)

- [qutebrowser: Web Browser Written in Python](https://pycoders.com/link/1404/web)
    + QUTEBROWSER.ORG

(`是也乎:`

浏览器的话, 没有插件体系, 
是只能给机器用的...

)


- [pgcli v2.1.0 Released](https://pycoders.com/link/1391/web)
    + PGCLI.COM

(`是也乎:`

神奇的作品.


)


- [plantz: Python-Powered Backyard IOT Greenhouse](https://pycoders.com/link/1405/web)
    + GITHUB.COM/FHK


(`是也乎:`

![...](https://github.com/fhk/plantz/raw/master/assets/img/IMG_1213.JPG)

真的是绿屋...
还以为是什么代号呢...

结果一看, 是原创自动化暖棚...

用 Python 控制各种传感器以及水肥温度什么的...

>>> 村会玩儿

)


- [Mypy 0.700 Released: Up to 4x Faster](https://pycoders.com/link/1398/web)
    + MYPY-LANG.BLOGSPOT.COM

Mypy now ships a mypy binary compiled with mypyc by default, which is up to 4x faster than the previous interpreted version. Very cool!

(`是也乎:`

叕一个死也不 1.0 的

)


## 📆🐍 活动/大会
> Events

- [⋅ PyCon Africa](https://pycoders.com/link/1388/web)
    +  August 6 to August 11 
    +  加纳 Accra, Ghana

(`是也乎:`

网站根本打开不能

)


- [⋅ Python North East](https://pycoders.com/link/1418/web)
    +  April 10, 2019
- [⋅ DjangoCon Europe 2019](https://pycoders.com/link/1399/web)
    + April 10 to April 15, 2019
    + 荷兰
- [⋅ Python Atlanta](https://pycoders.com/link/1406/web) 
    + USA April 11, 2019
- [⋅ Python Miami](https://pycoders.com/link/1414/web)
    + USA April 13 to April 14, 2019
- [⋅ PyTexas 2019](https://pycoders.com/link/1384/web)
    + USA 德州
    + April 13 to April 15, 2019
- [⋅ PythonCamp.de 2019](https://pycoders.com/link/1386/web) 
    + April 13 to April 15, 2019



## DAMA
> ❤️ Happy Pythonic!

(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 36小时以内截止

# 是也乎

- 190411 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190410 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
