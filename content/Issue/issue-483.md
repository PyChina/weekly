Title: Issue 483
Slug: issue-483
Date: 2021-07-28 11:42
Tags: Weekly,Python,pycoders,ZH


> 给问题自动生成代码...


原文: [PyCoder's Weekly - Issue #483](https://pycoders.com/issues/483)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210728 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210728 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python’s 集合: 专门数据类型自助餐](https://pycoders.com/link/6744/web)
    + REAL PYTHON

Python has a number of useful data types beyond the built-in lists, tuples, dicts, and sets. In this tutorial, you’ll learn all about the series of specialized container data types in the collections module from the Python standard library. Learning the collections module is a great way to level up your Python programming knowledge!


(`是也乎:`


![collections](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2011.18.17.jpg)

)




- [将 Scipy 迁移进 Meson 构建系统](https://pycoders.com/link/6760/web)
    + RALF GOMMERS

In accordance with PEP 632, distutils will be deprecated in Python 3.10 and in Python 3.12 it will be removed. This posed a big problem for SciPy, since it’s build system depends on NumPy’s distutils module — an extension of Python’s built-in distutils. The SciPy maintainers set out to find a new build system and settled on Meson, which solves a number of build issues and even scores a 4x speed-up on build times!



- [Python’s Operator 模块的未知功能](https://pycoders.com/link/6755/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Have you heard of Python’s operator module? It includes functions for common operators, including mathematical operators like +, -, *, and /, and well as operators for getting items from dictionaries and accessing object attributes. The operator module might seem confusing at first glance. This article explores why it exists, what benefits you get from it, and when it makes sense to use it in your code.

- [Python Software Foundation Fellow 2021/Q2 成员](https://pycoders.com/link/6761/web)
    + PYTHON SOFTWARE FOUNDATION




-----------------------------------------
## 探讨/吐糟
> Discussions



- [嫑将可变对象用作 Python 默认参数](https://pycoders.com/link/6749/web)
    + REDDIT

Ah, mutable default arguments. If you haven’t come across them in your Python journey yet, this Reddit thread is full of examples of Python developers that lost time debugging functions with a mutable default argument. Avoiding mutable defaults is good advice in general, but blanket absolute statements are dangerous. To counter this discussion, here’s a Twitter thread exploring some genuine use cases.



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks

- [Pandas 的 DataFrame: 有效地使用数据](https://pycoders.com/link/6759/web)
    + REAL PYTHON 
    + course

In this tutorial, you’ll get started with Pandas DataFrames, which are powerful and widely used two-dimensional data structures. You’ll learn how to perform basic operations with data, handle missing values, work with time-series data, and visualize data from a Pandas DataFrame.

(`是也乎:`

![DataFrame](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2011.15.57.jpg)

)



- [测试差异](https://pycoders.com/link/6746/web)
    + FILIPE XIMENES 
    + • Shared by Filipe Ximenes

How do you write good tests? It’s a challenging problem because there are a number of layers involved. You need to write good test code that follows best practices. But you also need to write tests that aren’t fragile and make sure tests really test what you expect them to. This article gives an example of a seemingly harmless test that turns out to be pretty fragile. You’ll learn one technique for making a test more robust called “testing the diff.”




- [编程中的美好思想: Generators 和 Continuations](https://pycoders.com/link/6764/web)
    + HSIN-HAO YU

This article explores how generators, which you can create in Python using the yield keyword in a function, are special cases of a more powerful construct called “continuations.” The author compares Python’s generator syntax to creating continuations in Scheme, a modern LISP dialect. The idea isn’t so much to learn how to write generators and continuations, but rather to explore how the ideas are related and to appreciate the elegance and beauty of both concepts.

(`是也乎:`

    想法虽好,
    但嫑贪杯...

)



- [可以用python做什么/ 使用计数器计算对象](https://pycoders.com/link/6742/web)
    + REAL PYTHON 
    + podcast

How is Python being used today, and what can you do with the language? Do you want to develop software, dive into data science and math, automate parts of your job and digital life, or work with electronics? This week on the Real Python Podcast, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.

(`是也乎:`

![podcast](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2011.08.59.jpg)

)


- [用 Django 和 Postgres 高效分页](https://pycoders.com/link/6740/web)
    + RYAN WESTERBERG 
    + • Shared by Manuel Weiss

Pagination breaks up results from a query into chunks called “pages” so that only a few results are returned to the user at a time. In many cases, using native SQL tools like LIMIT and OFFSET can get you up and running with pagination quickly and work fairly well. But on datasets with millions of rows, this method breaks down. This helpful article shows you three methods for efficiently handling pagination using Django and Postgres.

(`是也乎:`

虽然没人提 MySQL 了,
但是, 日常还是首选 MySQL ...

)


- [用 Django 的第一步/ 设置 Django 项目](https://pycoders.com/link/6753/web)
    + REAL PYTHON

This tutorial provides a walkthrough and a reference for starting a Django project and app. You can use it as a quick setup guide for any future Django project and tutorial you’ll work on.

(`是也乎:`


![Django](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2011.06.24.jpg)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [qmsolve: 用于解决和可视化 Schrödinger 方程的模块](https://pycoders.com/link/6765/web)
    + GITHUB.COM/QUANTUM-VISUALIZATIONS



- [jupyter-text2code: 概念验证 jupyter 扩展/将英文查询转换为 python 代码](https://pycoders.com/link/6769/web)
    + GITHUB.COM/DEEPKLARITY


(`是也乎:`

充分利用现有资源,
在 Jupter 中营造出智能自动写代码的效果...


)

- [dlib: 用于制作真实世界机器学习和数据分析应用的 C++/Python 工具包](https://pycoders.com/link/6737/web)
    + GITHUB.COM/DAVISKING



- [aptus: Mandelbrot Set Explorer 和 渲染器](https://pycoders.com/link/6766/web)
    + GITHUB.COM/NEDBAT

- [hook-slinger: 发送/重试/管理 Webhooks 的通用服务](https://pycoders.com/link/6748/web)
    + GITHUB.COM/REDNAFI • Shared by Redowan Delowar

(`是也乎:`

![slinger](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2010.59.04.jpg)

专注解决 web-hook 小领域问题:

FastAPI 提供服务,
RQ/Redis 作为任务队列,
rqmonitor 监控;
rich 提供彩色终端日志输出...

毫无意外的组合.

![rich](https://ipic.zoomquiet.top/2021-07-28-ScreenShot%202021-07-28%2011.01.56.jpg)

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6762/web)
    + July 28, 2021

- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021

- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021

- [⋅ PyOhio 2021 (Virtual)](https://pycoders.com/link/6767/web)
    + July 31 — August 1, 2021


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:

- 首发: [Issue 483 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-483.html)
- 修订: [issue-483.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-483.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 创始组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------





