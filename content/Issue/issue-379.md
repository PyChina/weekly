Title: Issue 379
Slug: issue-379
Date: 2019-08-01 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #379](https://pycoders.com/issues/379)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [什么是 Python 3.8 将带来的?](https://pycoders.com/link/2129/web)
    + JAKE EDGE

"The Python 3.8 beta cycle is already underway, with Python 3.8.0b1 released on June 4, followed by the second beta on July 4. That means that Python 3.8 is feature complete at this point, which makes it a good time to see what will be part of it when the final release is made."

(`是也乎:`

已经开始期待 Py 4 了...
在老爹有生之年..应该规划好 Python 42 前所有开发呢.

)


- [PyLint 误报...](https://pycoders.com/link/2138/web)
    + LUKE PLANT

"In some recent discussion on Reddit, I claimed that, for cases where I'm already using flake8, it seemed as though 95% of Pylint's reported problems were false positives. Others had very different experiences, so I was intrigued enough to actually do some measurements."


- [理解 Python Traceback](https://pycoders.com/link/2108/web)
    + REAL PYTHON

Learn how to read and understand the information you can get from a Python traceback. You'll walk through several examples of tracebacks and see how to handle some of the most common types of exceptions in Python.

(`是也乎:`

![Traceback](https://ipic.zoomquiet.top/2019-07-31-ScreenShot%202019-08-01%2007.24.52.jpg)


正如其名...倒追...


)



- [Django vs Flask in 2019: 框架之选](https://pycoders.com/link/2122/web)
    + MICHAEL HERMAN 
    + • Shared by Michael Herman


In this article, you'll take a look at the best use cases for Django and Flask along with what makes them unique, from an educational and development standpoint.

(`是也乎:`

Bottle 一生推...

不过,商业项目, Django 没问题.

)


- [字典在 Python](https://pycoders.com/link/2112/web)
    + REAL PYTHON 
    + video

In this course on Python dictionaries, you'll cover the basic characteristics of dictionaries and learn how to access and manage dictionary data. Once you've finished this course, you'll have a good sense of when a dictionary is the appropriate data type to use and know how to use it.

- [Python 3.8.0b3 可用于测试](https://pycoders.com/link/2137/web)
    + PYTHON.ORG



## 讨论
> Discussions


- [Pipenv 已死? 为何停更?](https://pycoders.com/link/2127/web)
    + REDDIT



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [4种将 Python 应用打包单一可执行文件的尝试](https://pycoders.com/link/2111/web)
    + CHRISTIAN MEDINA 
    + • Shared by Christian Medina

Interesting recap of the author's experience creating a single-file executable of a Python application using four different tools: Cython, Nuitka, PyOxidizer, and PyInstaller.

(`是也乎:`

除了 PyOxidizer , 都是传统的 Py 应用打包思路;
PyOxidizer 比较清奇, 将核心运行时, 用 Rust 包装起来, 
获得更加安全和高效...

只是, 还在早期, 尝试过, mac 下都编译不过,
win10 更加没戏...

远没有 golang build 支持树来的嗯哼...


)


- [从头开始嗯哼神经网络,用Python](https://pycoders.com/link/2130/web)
    + VICTOR ZHOU

A 4-post series that provides a fundamentals-oriented approach towards understanding Neural Networks.





- [适 Python Docker 包装指南](https://pycoders.com/link/2104/web)
    + ITAMAR TURNER-TRAURING

A detailed guide to creating production-ready Docker images for your Python applications.

(`是也乎:`

无论是否在 Docker , Python 运行时环境都应该和系统 Python 运行时区分,
又合理调用

)


- [你爱 Python 的 35 个单词](https://pycoders.com/link/2105/web)
    + MICHAEL MOREHOUSE

"I'm going to try, in this post and the ones that follow, to shed some light on the meaning of – and a little of the etymological history behind – the fundamental units of Python fluency. In this first part we will start with the most basic of those units, Python's 35 keywords."




- [Keras 和深度学习的周期性学习率](https://pycoders.com/link/2146/web)
    + ADRIAN ROSEBROCK

In this tutorial, you will learn how to use Cyclical Learning Rates (CLR) and Keras to train your own neural networks. Using Cyclical Learning Rates you can dramatically reduce the number of experiments required to tune and find an optimal learning rate for your model.

- [深入挖掘 Migrations](https://pycoders.com/link/2126/web)
    + REAL PYTHON

In this step-by-step Python tutorial, you'll not only take a closer look at the new Django migrations system that is integrated into Django but also walk through the migration files themselves.


(`是也乎:`

![django](https://ipic.zoomquiet.top/2019-07-31-ScreenShot%202019-08-01%2007.12.39.jpg)


Migrations 工具桟可以说是 Django 的命门, 
一直修炼的非常 NB 了...

当然, Django only,
想提取出来单独用, 不现实.

)



- [PySpark ETL 项目的最佳实践](https://pycoders.com/link/2107/web)
    + ALEX IOANNIDES 
    + • Shared by Alex Ioannides

A tutorial on how best to reason about and structure ETL jobs written for PySpark, so that they are robust, reusable, testable, easy to debug and ready for production.

- [有效地生成 Python 哈希冲突](https://pycoders.com/link/2148/web)
    + LEE HOLMES

"While this research demonstrates a fundamental break in the Python 3.2 (or below) hash algorithm, Python fixed this issue 7 years ago. It's time to upgrade."

(`是也乎:`

Python 3.2 之后解决了...

)


- [Python 教学用最佳编辑器/IDE](https://pycoders.com/link/2118/web)
    + TEACHINGPYTHON.FM podcast

In this episode of Teaching Python, Sean and Kelly discuss their top 5 favorite editors for teaching (and learning) Python.

(`是也乎:`

注意, 教学用...

    Mu Editor
    Visual Studio Code
    PyCharm Edu
    python.microbit.org
    Repl.it
    Jupyter

嗯嗯嗯...怎么说呢...
能和生产环境一致是最合算的事儿...


)



- [超越"Hello World": Kubernetes 中的现代异步 Python](https://pycoders.com/link/2131/web)
    + SEAN STEWART 
    + • Shared by Sean Stewart


(`是也乎:`

K8s 是 google 叕一次统一领域技术思想的杀手...

)


- [用 Python 构建空间站跟踪器,从头开始](https://pycoders.com/link/2142/web)
    + DANIEL COHEN


- [如何配置和优化 Python 应用程序](https://pycoders.com/link/2120/web)
    + MARK KELLER


(`是也乎:`

同下, 最重要的总是:

    知道何时住手

)


- [实例嗯哼 Python List Comprehension](https://pycoders.com/link/2115/web)
    + DEEPANSHU BHALLA

(`是也乎:`


其实, 列表推导式, 最重要的技巧是:

    知道, 何时应该不用

)




## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [Wait Wait...  Don't Tell Me! Stats and Show Details](https://pycoders.com/link/2103/web)
    + WWDT.ME

Here, you will find almost everything you might want to know about the NPR news quiz show. Project is written in Python and partially open-source.




- [PyCharm 2019.2 Has Been Released](https://pycoders.com/link/2121/web)
    + JETBRAINS.COM

(`是也乎:`

这则消息, 很难变成赞助消息...

)


- [aioquic: QUIC and HTTP/3 Implementation in Python](https://pycoders.com/link/2117/web)
    + GITHUB.COM/AIORTC

- [grapheneX: Automated System Hardening Framework](https://pycoders.com/link/2139/web)
    + GITHUB.COM/GRAPHENEX 
    + • Shared by keylo99

(`是也乎:`


自动 `淬火` ...

![Hardening](https://user-images.githubusercontent.com/24392180/60549923-02f2c880-9d2f-11e9-9ee2-b3f58afeb5fd.gif)


叕一个概念和产品的绑定...

将安全和鲁棒融合的嗯哼...

)



- [scaraplate: Update Already Created Cookiecutter Projects](https://pycoders.com/link/2113/web)
    + GITHUB.COM/RAMBLER-DIGITAL-SOLUTIONS 
    + • Shared by Alexander Shorin

- [python-fire 0.2.0 Released: Generate CLI From Any Python Object](https://pycoders.com/link/2150/web)
    + GITHUB.COM/GOOGLE


(`是也乎:`

有句什么话来的?...

反正有老爹给出方向, 大家就乱冲乱打先...

)


- [Grid Studio: Python Spreadsheet App to Make Data Science Easier](https://pycoders.com/link/2144/web)
    + RICK LAMERS

(`是也乎:`

又句什么话来的? 叫什么什么...志在千里?

)


- [PyDist: Your Own Private PyPI](https://pycoders.com/link/2140/web)
    + PYDIST.COM

(`是也乎:`

叕一个私人 PyPI 实现...

但是, 对于中国, 要的是高速镜像...

)


- [Lahja: Pure Python Event Bus for Multi-Process Apps That Supports Asyncio and Trio](https://pycoders.com/link/2123/web)
    + GITHUB.COM/ETHEREUM

- [Pyrasite: Tools for Injecting Code Into Running Python Processes](https://pycoders.com/link/2116/web)
    + PYRASITE.COM


(`是也乎:`

等等, 这个事儿, 可大可小哪...

)




## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ DjangoCon AU 2019](https://pycoders.com/link/2110/web)
    + August 2 to August 3, 2019
    + 澳洲




- [⋅ PyCon AU 2019](https://pycoders.com/link/2119/web)
    + 2019 August 2 to August 7, 2019
    + 澳洲

- [⋅ PyBay 2019](https://pycoders.com/link/2149/web) 
    + August 15 to 16 
    + in San Francisco, California

## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 第2期
    + 101camp2py

报名结束, 进入 ch1,下期 190901 左右启动...



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

- 190801 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190801 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
