Title: 蠎周刊(PyCoder)596
Slug: issue-596
Date: 2023-09-27 11:42
Tags: Weekly,Python,pycoders,ZH


> 绕过 GIL 进行并行处理


原文: [PyCoder's Weekly - Issue #596](https://pycoders.com/issues/596)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230927 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230927 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [设计和指导：Python 中的面向对象编程](https://pycoders.com/link/11492/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn about the SOLID principles, which are five well-established standards for improving your object-oriented design in Python. By applying these principles, you can create object-oriented code that is more maintainable, extensible, scalable, and testable.


(`是也乎:`


![OOP](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2010.06.07.jpg)

)


- [用 Radon 了解 Python 中的代码度量](https://pycoders.com/link/11505/web)
    + MIKE DRISCOLL

Radon is a code metrics tool. This article introduces you to it and teaches you how you can improve your code based on its measurements.

(`是也乎:`

氡 ~ 真的是个好名字

)


- [当多核不可行时加快代码速度](https://pycoders.com/link/11480/web)
    + ITAMAR TURNER-TRAURING

Parallelism isn’t the only answer: often you can optimize low-level code to get significant performance improvements.

- [Django 5.0 Alpha 1 发布](https://pycoders.com/link/11486/web)
    + DJANGO SOFTWARE FOUNDATION

- [Python 3.12.0 候选版本 3 可用](https://pycoders.com/link/11503/web)
    + CPYTHON DEV BLOG



-----------------------------------------
## 探讨/吐糟
> Discussions


NULL


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [如何在 Python 中捕获多个异常](https://pycoders.com/link/11508/web)
    + REAL PYTHON

In this how-to tutorial, you’ll learn different ways of catching multiple Python exceptions. You’ll review the standard way of using a tuple in the except clause, but also expand your knowledge by exploring some other techniques, such as suppressing exceptions and using exception groups.


(`是也乎:`

![多个异常](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2010.02.15.jpg)


嗯哼...不过, 一般值得抓的只有第一个?

)


- [用 GZIP 在 10 行以下代码中实现 78% 的 MNIST 准确率](https://pycoders.com/link/11482/web)
    + JAKOBS.DEV

MNIST is a collection of hand-written digits that is commonly used to play with classification algorithms. It turns out that some compression mechanisms can double as classification tools. This article covers a bit of why with the added code-golf goal of a small amount of code.


- [在 Python 中绕过 GIL 进行并行处理](https://pycoders.com/link/11496/web)
    + REAL PYTHON

In this tutorial, you’ll take a deep dive into parallel processing in Python. You’ll learn about a few traditional and several novel ways of sidestepping the global interpreter lock (GIL) to achieve genuine shared-memory parallelism of your CPU-bound tasks.


(`是也乎:`

![GIL](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2009.59.44.jpg)


)


- [创建一个出色的 Python DevX](https://pycoders.com/link/11493/web)
    + SCOTT HOUSEMAN

This article talks about the different tools you commonly come across as part of the Python development experience. It gives an overview of black, nox, ruff, Mypy, and more, covering why you should use them when you code your own projects.


(`是也乎:`

WoW 如何发现并构建流行工具库,

> ...创建愉快且有意义的 Python 开发人员体验

前题是你本身必须是一名高强度开发者,
但是,在你已经习惯某些操作的同时,
又得敏锐的发现, 哪些操作值得进一步优化...

这就得有种自我撕裂的技巧了...


)


- [为什么有这么多 Python Dataframes?](https://pycoders.com/link/11506/web)
    + MAHESH VASHISHTHA

Ever wonder why there are so many ways libraries that have Dataframes in Python? This article talks about the different perspectives of the popular toolkits and why they are what they are.


(`是也乎:`


![Dataframes](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2009.56.10.jpg)

没办法, 名字太好了, 无论谁都想用

)


- [The Protocol Class/协议类](https://pycoders.com/link/11491/web)
    + PEPIJN BAKKER

typing.Protocol enables type checking in a Java-esque interface like mechanism. Using it, you can declare that a duck-typed class conform to a specific protocol. Read on for details.

- [if __name__ == "__main__" 在 Python 中意味着什么？](https://pycoders.com/link/11488/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn all about Python’s name-main idiom. You’ll learn what it does in Python, how it works, when to use it, when to avoid it, and how to refer to it.


(`是也乎:`


![__main__](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2009.54.55.jpg)


老梗儿...

)


- [为什么以及如何在字符串处理中使用Python 布隆过滤器](https://pycoders.com/link/11512/web)
    + ABHINAV UPADHYAY

Dive into Python’s clever use of Bloom filters in string APIs for speedier performance. Find out how CPython’s unique implementation makes it more efficient.

- [用 Python 模拟 Monty Hall 问题](https://pycoders.com/link/11507/web)
    + DATASCHOOL.IO 
    + • Shared by Kevin Markham

Write a Python simulation to solve this classic probability puzzle that has stumped mathematicians and Nobel Prize winners!

(`是也乎:`

[About Data School](https://www.dataschool.io/about/)
这居然是独立站, 可以看为海外版本 寥雪峰 ...

)


- [一千个微服务的死亡](https://pycoders.com/link/11504/web)
    + ANDREI TARANCHENKO

The software industry is learning once again that complexity kills and trending back towards monoliths and larger services.

(`是也乎:`


宁可内部复杂, 也没办法控制外部复杂...

)


- [如何使用 Pytest 和 Nbmake 测试 Jupyter 笔记本](https://pycoders.com/link/11502/web)
    + SEMAPHORECI.COM 
    + • Shared by Larisa Ioana

Tutorial on how to use the pytest plugin nbmake to automate end-to-end testing of notebooks.

(`是也乎:`

这可是 Jupter 成为生产工具的重大一关哪...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [panther: 用于构建异步 API 的 Web 框架](https://pycoders.com/link/11481/web)
    + GITHUB.COM/ALIRN76

(`是也乎:`

![panther](https://ipic.zoomquiet.top/2023-09-27-zshot%202023-09-27%2009.49.24.jpg)

赞助方不得了...

)


- [Clientele: 来自 OpenAPI 模式的可爱 Python API 客户端](https://pycoders.com/link/11499/web)
    + GITHUB.COM/PHALT 
    + • Shared by Paul Hallett

- [mpire: 简单但更快的多处理](https://pycoders.com/link/11497/web)
    + GITHUB.COM/SYBRENJANSEN

- [leaky_ledger: 练习查找漏洞的假银行](https://pycoders.com/link/11498/web)
    + GITHUB.COM/ZCHTODD

- [reader: Python Feed 阅读器库](https://pycoders.com/link/11485/web)
    + GITHUB.COM/LEMON24 
    + • Shared by Adrian


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11487/web)
    + September 27, 2023

- [SPb Python Drinkup](https://pycoders.com/link/11510/web)
    + September 28, 2023

- [PyCon India 2023](https://pycoders.com/link/11489/web)
    + September 29 to October 3, 2023

- [PythOnRio Meetup](https://pycoders.com/link/11483/web)
    + September 30, 2023

- [PyConZA 2023](https://pycoders.com/link/11495/web)
    + October 5 to October 7, 2023

- [PyCon ES Canarias 2023](https://pycoders.com/link/11500/web)
    + October 6 to October 9, 2023

- [Django Day Copenhagen 2023](https://pycoders.com/link/11501/web)
    + October 6 to October 7, 2023

- [DjangoCongress JP 2023](https://pycoders.com/link/11490/web)
    + October 7 to October 8, 2023


-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 544](https://weekly.pychina.org/issue/issue-544.html)
- 2021: [蠎周刊 491](https://weekly.pychina.org/issue/issue-491.html)
    + [pythonista-weekly : Pyw 518](https://weekly.pychina.org/python-weekly/pyw-518.html)
- 2020: [蠎周刊 438](https://weekly.pychina.org/issue/issue-438.html)
    + [pythonista-weekly : Pyw 468](https://weekly.pychina.org/python-weekly/pyw-468.html)
- 2019: [蠎周刊 387](https://weekly.pychina.org/issue/issue-387.html)
- 2018: [蠎周刊 336](https://weekly.pychina.org/issue/issue-336.html)
- 2017: [蠎加载 143](https://weekly.pychina.org/importpython/importpython-143.html)
- 2016: [蠎加载 92](https://weekly.pychina.org/importpython/importpython-92.html)
- 2015: [蠎周刊 185](https://weekly.pychina.org/issue/issue-185.html)
    + [蠎加载 51](https://weekly.pychina.org/importpython/importpython-51.html)
- 2014: [Issue 134](https://weekly.pychina.org/issue/issue-134.html)
- 2013: 空缺
- 2012: 空缺


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + @Chaos42DAMA
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊



```
         _~^|~~_
     () /  ◷ ^  \ ()
       '_   v   _'
       ( '--~--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 596 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-596.html)
- 修订: [issue-596.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-596.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.
    
## PPS:
> 不觉中蟒周刊快译已经到了第10+2个年头

开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
从来没提醒过, 可就这么默默坚持下来了...

问为什么:

    [皱眉]每周新闻资讯 怎么能错过 
    看看有什么新东西 
    当有新的发现时：
        what f**k 还能这样玩？ 还有这东西？
        每周开彩蛋[吃瓜]

`无法同意更多`...
很多社区贡献看起来辛苦,
其实受益最多的,
就是主动承担者也.

所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF596D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF596D4Q90XdDA7g):



```python
全职嗯哼: 大妈的多重宇宙 - https://www.youtube.com/@Chaos42DAMA
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开社群: 蟒营 (订阅号: Mainium)

as 创始组织者:
    CPyUG (mailling-list: python-cn@googlegroups.com)
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        AIGC珠海 

```

-------------



