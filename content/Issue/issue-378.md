Title: Issue 378
Slug: issue-378
Date: 2019-07-24 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #378](https://pycoders.com/issues/378)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [创建用 Google 登录的 Flask 应用程序](https://pycoders.com/link/2057/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll create a Flask application that lets users sign in using their Google login. You'll learn about OAuth 2 and OpenID Connect and also find out how to implement some code to handle user session management.

(`是也乎:`

![Login](https://ipic.zoomquiet.top/2019-07-24-ScreenShot%202019-07-24%2012.07.09.jpg)


如何基于一个不存在的网站完成用户登录检验?

)



- [Guido 有关 Python 上 PEG Parsers](https://pycoders.com/link/2086/web)
    + GUIDO VAN ROSSUM

"Some years ago someone asked whether it would make sense to switch Python to a PEG parser. [... ] I looked into it a bit and wasn't sure what to think, so I dropped the subject. Recently I've learned more about PEG (Parsing Expression Grammars), and I now think it's an interesting alternative to the home-grown parser generator that I developed 30 years ago when I started working on Python."

(`是也乎:`

老爹难得放话了...

有趣, 但是, 只能放弃.

)



- [Pip 决定前前兼容 Python 2.x](https://pycoders.com/link/2050/web)
    + PYPA.IO

"pip will continue to ensure that it runs on Python 2.7 after the CPython 2.7 EOL date. Support for Python 2.7 will be dropped, if bugs in Python 2.7 itself make this necessary (which is unlikely) or Python 2 usage reduces to a level where pip maintainers feel it is OK to drop support. The same approach is used to determine when to drop support for other Python versions."

(`是也乎:`

顺应民意...

无论 官方是否支持 Py2 代码,
海量 Py2 only 的包是应该长久支持的.

)


- [日志在 Python](https://pycoders.com/link/2054/web)
    + REAL PYTHON 
    + video

Python provides a logging system as a part of its standard library, so you can quickly add logging to your application. In this course, you'll learn why using this module is the best way to add logging to your application as well as how to get started quickly, and you will get an introduction to some of the advanced features available.

(`是也乎:`

视频教程,如何日志...
不过,这事儿, 在Python 不是太困难, 而是太容易, 
以至难以决定用哪种姿势...

)



- [通过构造复本来理解 Celery 如何工作](https://pycoders.com/link/2084/web)
    + KOMU WAIRAGU 
    + • Shared by Komu Wairagu

"A delayed job processor (also called a background processor, asynchronous task queue, etc.) is a software system that can run code at a later time. Examples of such software includes Celery, Resque, Sidekiq, and others. In this post we will try and understand how these things work by building a clone/replica of such software."

- [简化您的 Python 开发人员环境](https://pycoders.com/link/2067/web)
    + MASON EGGER 
    + • Shared by Python Bytes FM

Three tools (pyenv, pipx, pipenv) make for smooth, isolated, reproducible Python developer and production environments.

(`是也乎:`

混合这么多环境管理工具,
怎么叫简洁呢?

)



## 讨论
> Discussions


- [针对还没发布的 Python 3.8 特性的最佳实践来了](https://pycoders.com/link/2063/web)
    + RAYMOND HETTINGER

"As a Python 3.8 learning exercise, I'm using the walrus operator, / notation, and f= at every opportunity and then evaluating the result for clarity."

(`是也乎:`

也就是说, 现在的 Python 版本是

`OPP` ~ 面向最佳实践编程?

)


- [在没有导入 NumPy 的情况下从 Pandas 使用 NumPy](https://pycoders.com/link/2097/web)
    + TWITTER.COM/JUSTMARKHAM

"Want to use NumPy without importing it? You can access all of its functionality from within pandas... "

- [Writing the Digits of Pi Backwards... in Python?](https://pycoders.com/link/2082/web)
    + REDDIT

;-)



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [用 Mixins 使 Python 类更加模块化](https://pycoders.com/link/2072/web)
    + ALEKSEY BILOGUR 
    + • Shared by Aleksey Bilogur

"In this article I want to discuss mixins: what they are, how they work, and when they're useful. Hopefully after reading this brief article you will be ready to experiment with this pattern yourself in your own projects."

(`是也乎:`

别写类,就是纯粹模块了
)


- [Keras Learning Rate Schedules and Decay](https://pycoders.com/link/2088/web)
    + ADRIAN ROSEBROCK

In this tutorial, you will learn about learning rate schedules and decay using Keras. You'll learn how to use Keras' standard learning rate decay along with step-based, linear, and polynomial learning rate schedules.


- [如何用 np.arange()](https://pycoders.com/link/2076/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn how to use the NumPy arange() function, which is one of the routines for array creation based on numerical ranges. np.arange() returns arrays with evenly spaced values.

(`是也乎:`


![arange](https://ipic.zoomquiet.top/2019-07-24-ScreenShot%202019-07-24%2011.58.03.jpg)


![fig](https://files.realpython.com/media/fig-1.1d8bc9379e87.png)

可爱...


)



- [保卫 Python 的未来, by Hunting Black Swans](https://pycoders.com/link/2090/web)
    + PYTHONPODCAST.COM 
    + podcast

An interview with Russell Keith-Magee about identifying potential black swan events for the Python ecosystem and how to address them for the future of the language and its community.

- [编写可持续维护的 Python 脚本](https://pycoders.com/link/2049/web)
    + VINCENT BERNAT

A standalone Python script can come with a discoverable interface a documentation and some tests to keep it useful a year later.


(`是也乎:`


可维护? 写简单的代码, 确保自己20年后, 也看的懂;

当然配合上文档最好

)

- [从服务器启动中解耦数据库迁移: Why and How](https://pycoders.com/link/2046/web)
    + ITAMAR TURNER-TRAURING

Why running migrations on application startup are a bad idea (potential database corruption & downtime) and what to do instead.


- [来构建一个简单的解释器: 识别过程调用](https://pycoders.com/link/2078/web)
    + RUSLAN SPIVAK

Part 16 in Ruslan's amazing tutorial series on building a scripting language interpreter using Python, from scratch.


(`是也乎:`


![Interpreter](https://ruslanspivak.com/lsbasi-part16/lsbasi_part16_img01.png)

有手绘图的教程 ;-)

)


- [实用生产 Python 脚本](https://pycoders.com/link/2056/web)
    + DAN CONNOLLY

A step-by-step refactoring journey from simple fizzbuzz script to a cleaned up and "production-ready" piece of code.

(`是也乎:`

这点是 Python 永远的痛...
除非能象 go/rust 那样, 提供一键生成无依赖,独立运行应用文件

)


- [威胁佛罗里达, 巨型蟒蛇 入侵](https://pycoders.com/link/2051/web)
    + SMITHSONIANMAG.COM

Python is eating the world! Related discussion on Hacker News.



- [对 Travis CI 进行广泛的 Python 测试](https://pycoders.com/link/2055/web)
    + SHAY PALACHY

Testing open-source Python on several operating systems using Travis for continous integration.

- [Python 反模式和最差实践列表](https://pycoders.com/link/2068/web)
    + QUANTIFIEDCODE.COM

(`是也乎:`

反模式和坏实践, 值得收藏, 铭记

)


- [估计 Python 中的 Pi](https://pycoders.com/link/2061/web)
    + CHRIS WEBB

- [用 Python 完成多页 PDF 到 JPEG 图像转换](https://pycoders.com/link/2066/web)
    + M. TARIK YURT

(`是也乎:`

pdf->jpg?

然后再接入 OCR 就能完成对 PDF 内容的识别了

)


- [Python 初学者常见 5 种错误](https://pycoders.com/link/2081/web)
    + DEEPSOURCE.IO

(`是也乎:`

叕嗯哼一组初学者容易嗯哼的问题


)


- [用 Python 和 Google Maps API 按星巴克数量对首都排名](https://pycoders.com/link/2069/web)
    + ARTEM RYS



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [Pdb++: 更倩的 Pdb (调试器)](https://pycoders.com/link/2045/web)
    + GITHUB.COM/PDBPP

(`是也乎:`

![Pdb](https://github.com/antocuni/pdb/raw/master/screenshot.png?raw=true)


CLI 的潜力远没发挥

)

- [preper: 波斯语(波斯语)预处理Python模块](https://pycoders.com/link/2083/web)
    + GITHUB.COM/ALIIE62 
    + • Shared by Ali Hosseini

- [pyorbs: 方便的Python虚拟环境管理工具](https://pycoders.com/link/2095/web)
    + WBRP.CH


(`是也乎:`

叕一个虚拟环境管理工具,
这次用 `ord` 指令.

结合了 Pipenv 和 Pyenv 的优点.


)


- [pyon: Pythonic 方式来用 JSON](https://pycoders.com/link/2058/web)
    + GITHUB.COM/LAGMOELLERTIM

(`是也乎:`

其实, 只是想能稳定的兼容不标准 JSON 而已.

)


- [snoop: 调试库->旨在实现最大的便利性](https://pycoders.com/link/2096/web)
    + GITHUB.COM/ALEXMOJAKI


(`是也乎:`

![snoop](https://camo.githubusercontent.com/22f4ff7534e78d9e4f3b6e52214ca361401e0c5c/68747470733a2f2f692e696d6775722e636f6d2f456e75376b30682e706e67)

这勺子, 值得嗯哼


)


- [StanfordNLP: 适用于多种人类语言的Python NLP库](https://pycoders.com/link/2073/web)
    + STANFORDNLP.GITHUB.IO

(`是也乎:`

[Models | StanfordNLP](https://stanfordnlp.github.io/stanfordnlp/models.html#human-languages-supported-by-stanfordnlp)

仅支持繁体中文...

)


- [dlint: Python 代码 鲁棒性静态分析 ](https://pycoders.com/link/2089/web)
    + DUO.COM

(`是也乎`

不妥协之后, 专注 鲁棒性的分析器也来了...

)


- [pygraphblas: 用 Python 和 GraphBLAS 进行图形处理](https://pycoders.com/link/2094/web)
    + GITHUB.COM/MICHELP


(`是也乎:`

![pygraphblas](https://github.com/michelp/pygraphblas/raw/master/docs/ShortestPath.svg?sanitize=true)

叕一个 `图论计算` 框架


)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PythOnRio Meetup](https://pycoders.com/link/2060/web)
    + July 27, 2019
    + 巴西

- [⋅ Python Sheffield](https://pycoders.com/link/2070/web)
    + July 30, 2019
    + 大英

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/2093/web)
    + July 31, 2019
    + 德国

- [⋅ PiterPy Breakfast](https://pycoders.com/link/2085/web)
    + July 31, 2019
    + 早饭?

- [⋅ Reunión Python Valencia](https://pycoders.com/link/2062/web)
    + August 1, 2019
    + SPain

- [⋅ DjangoCon AU 2019](https://pycoders.com/link/2074/web)
    + August 2 to August 3, 2019
    + 澳大利亚

- [⋅ PyCon AU 2019](https://pycoders.com/link/2091/web)
    + August 2 to August 7, 2019
    + 悉尼国际会展中心 
    + 澳大利亚


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 第2期
    + 101camp2py

> 开始报名,
> 190725截止, 最后 42 小时
> 
> 课程: 0728~0908



<a href="https://pyscaffold.org">
    <img src="https://pyscaffold.org/en/latest/_images/logo.png"
 width="200"/>
</a>

~ helps you setup a new Python project


- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
    + FAQ

(`是也乎:`

![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)

总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...

其实, 本质上并不是对应技术是否有什么能力,
而是相反...

)




### Jobs:
> 必须 Pythonic 相关

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
    + 北京
    + anti-996


# 是也乎

- 190724 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190724 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
