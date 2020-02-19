Title: Issue 391
Slug: issue-391
Date: 2019-10-23 11:42
Tags: Weekly,Python,pycoders,ZH

> 最后一个官方 Py2 版本 2.7.17 发布

原文: [PyCoder's Weekly - Issue #391](https://pycoders.com/issues/391)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------


- [Arduino 微控制嘼 + Python: 入门](https://pycoders.com/link/2735/web)
    + REAL PYTHON

Discover how to use Arduino microcontrollers with Python to develop your own electronic projects. You'll learn how to set up circuits and write applications with the Firmata protocol. You'll control Arduino inputs and outputs and integrate the board with higher-level apps.

(`是也乎:`

Arduino 比 树莓派 其实不差...

![Arduino](http://ydlj.zoomquiet.top/ipic/2019-10-23-ScreenShot%202019-10-23%2009.45.00.jpg)

只是, 上手嵌入系统, 电工一系列工具就得先准备并熟练了..

)


- [为 Python 编写个 LLVM 专业工具](https://pycoders.com/link/2721/web)
    + STEPHEN DIEHL

"We're going to build a single module Numba-like compiler for Python. It won't be nearly as featureful or complete, but should demonstrate how you can go about building your own little LLVM specializer for a subset of Python or your own custom DSL expression compiler; and integrating it with the standard NumPy/SciPy stack for whatever scientific computing domain you work."


- [Python 2.7.17 发布](https://pycoders.com/link/2731/web)
    + PYTHON.ORG

Python 2.7.17 is a bug fix release in the Python 2.7.x series. It is expected to be the penultimate release for Python 2.7. [详细变更说明....](https://pycoders.com/link/2722/web)

- [Python 代码复杂性瀑布](https://pycoders.com/link/2738/web)
    + NIKITA SOBOLEV

What can be done to prevent your Python code from getting too complex? A good linter setup does much more than finding missing commas and bad quotes. A good linter allows you to rely on it with architecture decisions and help you with the refactoring process.

(`是也乎:`

还是得靠 linter 工具,
因为工程师总是不自主的在工程中将代码越写越复杂...

)


- [在 Python 中重新实现 Solaris 命令使 C 语言的性能提高了17倍](https://pycoders.com/link/2742/web)
    + DARREN MOFFAT

"As a result of fixing a memory allocation issue in the /usr/bin/listusers command, that had caused issues when it was converted to 64 bit, I decided to investigate if this ancient C code could be improved by conversion to Python."


(`是也乎:`

涉及性能, 古老的锅/坑总是 C 挖的...
现在, Python 也有机会来填/挖了...

)


- [Y组合器的简单本质(用Python解释)](https://pycoders.com/link/2726/web)
    + LIONEL PARREAUX

"The Y combinator is a central concept in lambda calculus, which is the formal foundation of functional languages. Y allows one to define recursive functions without using self-referential definitions."

(`是也乎:`

经典思想总是值得反复嗯哼的...
反正无论怎么推导,虽然总是能成功, 但是, 就是无法相信自己的眼睛...
直觉上中间一定有谁偷走了什么...

)


- [大规模 Python: 严格的模块](https://pycoders.com/link/2716/web)
    + CARL MEYER

The Instagram engineering team is experimenting with a technique for writing Python modules that are side-effect-free on import to reduce server startup time and unexpected global state changes.

(`是也乎:`

好吧, 什么事儿数量一多都不容易....

)


- [Python 属性访问和描述符协议](https://pycoders.com/link/2712/web)
    + AMIR RACHUM

A deep dive into Python attribute access and the descriptor protocol. What exactly happens when we say foo.bar?



## 讨论
> Discussions

- [Matplotlib 能以 xkcd 漫画风格创建图](https://pycoders.com/link/2736/web)
    + REDDIT

(`是也乎:`

早就支持了,还是官方文档中的...

![190218gl](http://ydlj.zoomquiet.top/ipic/2019-10-23-190218gl-act.png?imageView2/2/h/200)

)


- [最喜欢的 Python 3.8 特性是什么?](https://pycoders.com/link/2740/web)
    + TWITTER.COM/DBADER_ORG


(`是也乎:`

应该是不变的 `import this`

)


## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [time.sleep() : 如何在代码中添加时间延迟](https://pycoders.com/link/2732/web)
    + REAL PYTHON

Learn how to add time delays to your Python programs. You'll use decorators and the built-in time module to add Python sleep() calls to your code. Then, you'll discover how time delays work with threads, asynchronous functions, and graphical user interfaces.

(`是也乎:`

![Delays](http://ydlj.zoomquiet.top/ipic/2019-10-23-ScreenShot%202019-10-23%2009.36.40.jpg)

延迟制造...

)


- [Django 开发常犯的 7个错误](https://pycoders.com/link/2733/web)
    + TOMASZ BĄK 
    + • Shared by Tomasz Bąk

"Django is powerful web framework, but with power comes responsibility. In this article, we will cover common mistakes that are even seasoned Django developers make, yet most successful Django projects need to deal with these sooner or later."


(`是也乎:`

一切常见错误, 都是对 Django 设计思想误解造成的...

> ... with power comes responsibility

>> 能力带来责任


)


- [超越cProfile: 采样分析器和日志记录以优化性能](https://pycoders.com/link/2713/web)
    + ITAMAR TURNER-TRAURING

"Your Python program is too slow. Maybe your web application can't keep up, or certain queries are taking a long time. Maybe you have a batch program that takes hours or even days to run. How do you speed it up?"

(`是也乎:`

叕一个尝试辅助分析代码来提高速度的工具,
其实, 最根本的, 还是改进编译工具,
自动完成优化吧...

)


- [Vaex 助您一臂之力: 用Python分析30多年的飞行数据](https://pycoders.com/link/2734/web)
    + JOVAN VELJANOSKI

"Using the Python DataFrame library Vaex, I present the analysis of nearly 200 million flights made by U.S. carriers. Vaex uses fast out-of-core algorithms, making memory issues a thing of the past."

(`是也乎:`



)

- [将HTML转换为 Jupyter Notebook](https://pycoders.com/link/2730/web)
    + ERIK MARSJA

"Learn how to scrape code from a webpage and save it as a Jupyter notebook. In this post, we'll use Beautifulsoup4, urllib, and json, to save HTML to .ipynb."


(`是也乎:`

嗯哼?这个反操作思路很清奇了...
只是 -> Beautifulsoup4 ?
那可累...

)


- [Python 用 Matplotlib 进行绘图](https://pycoders.com/link/2707/web)
    + REAL PYTHON 
    + video

Want to make beautiful plots? Learn about plotting in Python with matplotlib by looking at the theory and following along with practical examples.

(`是也乎:`

![Matplotlib](http://ydlj.zoomquiet.top/ipic/2019-10-23-ScreenShot%202019-10-23%2009.32.12.jpg)


其实吧...其它图表库比 Matplotlib 轻便多了...

)


- [Keras vs tf.keras : TensorFlow 2.0有什么区别?](https://pycoders.com/link/2744/web)
    + ADRIAN ROSEBROCK

In this tutorial you'll discover the difference between Keras and tf.keras. You'll also learn what's new in TensorFlow 2.0.

(`是也乎:`

可以说, tf 在拼命将 Keras 吸收, 然后,不兼容 PyTorch 们...

)


- [设计 CI/CD 系统: GitHub拉取请求中的无痛状态报告](https://pycoders.com/link/2723/web)
    + CRISTIAN MEDINA 
    + • Shared by Cristian Medina

How to report status from Docker containers in an automated CI/CD system into GitHub pull requests using Python.

- [Pylint: 使您 Python 代码风格一致](https://pycoders.com/link/2725/web)
    + MOSHE ZADKA

How to configure the Pylint code linter to avoid arguing about code complexity.

(`是也乎:`

老牌工具, 总是要反复说怎么用的...

)

- [分治算法 的 Python 示例](https://pycoders.com/link/2714/web)
    + BRANDON SKERRITT

- [简易并发在 Python](https://pycoders.com/link/2709/web)
    + PHILIPP JUNG

- [Roll Your Own GUI Automation Library With Python](https://pycoders.com/link/2728/web)
    + ASRPO.COM


- [PyCon 2019: PyCon 上的人民群众](https://pycoders.com/link/2719/web)
    + CHRIS MAY

(`是也乎:`

国外 PyCon 每件都产生海量的参会笔记...
中国的, 基本都是吐糟...少有笔记,

到现在就收集到一篇今年的:
[PyCon China 2019 深圳站,看起来很水但实际并不水!](https://mp.weixin.qq.com/s/abbT0saaX4Wi9x_O1BHMhw)

)


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [ancient-text-restoration: 用深度学习还原古文字](https://pycoders.com/link/2720/web)
    + GITHUB.COM/SOMMERSCHIELD

(`是也乎:`

![Ancient](https://camo.githubusercontent.com/30a1b46d30199e57dd9326a89f17a622545b6d36/687474703a2f2f79616e6e697361737361656c2e636f6d2f70726f6a656374732f7079746869612f6570696772617068795f7472616e73702e706e67)

)


- [diff-match-patch: 高性能库,用于同步纯文本](https://pycoders.com/link/2718/web)
    + GITHUB.COM/GOOGLE

(`是也乎:`

google 出品,果断大气,
一上来就支持一堆语言:

    C++
    C#
    Dart
    Java
    JavaScript
    Lua
    Objective-C
    Python

06年就在内部使用了, 今天才开源
)


- [reloading: 用重新加载循环在运行时更改Python代码](https://pycoders.com/link/2743/web)
    + GITHUB.COM/JULVO


- [ssis_validator: 验证SQL Server集成服务(SSIS)程序包](https://pycoders.com/link/2741/web)
    + GITHUB.COM/MAHDI-HOSSEINI 
    + • Shared by Mike

- [BrachioGraph: 易于构建的笔式绘图仪,由Python提供支持](https://pycoders.com/link/2737/web)
    + GITHUB.COM/EVILDMP

(`是也乎:`

![BrachioGraph](https://github.com/evildmp/BrachioGraph/raw/master/docs/images/readme_combined_image.png)

低成本模拟签名...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Brasil 2019](https://pycoders.com/link/2739/web)
    + October 23 to October 29, 2019

- [⋅ PythOnRio Meetup](https://pycoders.com/link/2729/web)
    + October 26, 2019
    + 巴西

- [⋅ PyCon Sweden 2019](https://pycoders.com/link/2708/web)
    + October 31 to November 2, 2019
    + 瑞典

- [⋅ PyCon Fr](https://pycoders.com/link/2710/web)
    + October 31 to November 4, 2019
    + 法国

## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
    + 第3期
    + 101camp3py

> 第3期已开课, 为期6周;
**191103** 按时结束, 
到时再约 4py ;-)



# 是也乎
>> NN 3809

- 首发: [Issue 391 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-391.html)
- 改进: [issue-391.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-391.md)


