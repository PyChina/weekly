Title: Issue 372
Slug: issue-372
Date: 2019-06-12 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #372](https://pycoders.com/issues/372)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------


- [Python 预测未来4年将超越 C 和 Java](https://pycoders.com/link/1809/web)
    + ZDNET.COM

"Python's ascent continues among software developers, bolstered by its usability compared with Java and C."

(`是也乎:`

Go 在 10年前就预测过自己将在10年以内超越 JAVA

)


- [CPython 3.8.0b1 可用于测试](https://pycoders.com/link/1791/web)
    + PYTHON.ORG

New features include: f-string debugging, "async REPL" mode, AsyncMock in unittest.mock, async-support for unittest, math.comb added, Python embedding got better, and more.


- [如何用 Tweepy 制作 Python Twitter 机器人](https://pycoders.com/link/1807/web)
    + REAL PYTHON

Learn how to make a Twitter bot in Python with Tweepy, which is a package that provides a very convenient way to use the Twitter API. You can use your Twitter bot to automate all or part of your Twitter activity.

(`是也乎:`

![Tweepy](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.47.32.jpg)

等等, 为什么那么多教程都在尝试向一个不存在的网站自动化收发不存在的嗯哼?


)


- [2019 目前 Python 打包势态](https://pycoders.com/link/1782/web)
    + STEFANO BORINI

"In this post, I will try to explain the intricate details of Python packaging. I spent the best part of my evenings in the past two months to gather as much information as possible about the problem, the current solutions, what is legacy and what is not." Related discussion on Hacker News

(`是也乎:`

Poetry 硬广, 但是, 也揭示至今, 有关部署 Py 环境, 还是没有统一靠谱方案.

)



- [macOS 未来版本将不包括 Python 2.7](https://pycoders.com/link/1781/web)
    + MICHAEL TSAI

The next macOS release deprecates built-in Python 2.7 and other system scripting languages, such as Ruby. The system scripting languages on macOS have always lagged behind the latest releases, for example, the macOS system Python is still on 2.7. You'll still be able to install Python 2 or Python 3 as you would most likely anyway today.

(`是也乎:`

虽然从来不用系统内置的 Python,
但是, 这又是一个不买新 MBP 的理由了...

)


- [解决 Python 编程难题 ~> 循序渐进](https://pycoders.com/link/1792/web)
    + DONNACHA OISÍN KIDNEY

"This post is a write-up of a solution to part of a programming puzzle I did yesterday. It's a little different than the usual 'solution + theory' approach, though: I'm going to talk about the actual steps you'd need to take to get to the solution (i.e. what to google, what intermediate code looks like, etc.)."

- [为 PyTorch 编写玩具后端编译器](https://pycoders.com/link/1783/web)
    + BRAM WASTI

"This tutorial is designed as an end-to-end walkthrough detailing all that is necessary for building and integrating a compiler into PyTorch's JIT."




## 讨论
> Discussions


- ["谁在我们的交换机上安装了 Python?"](https://pycoders.com/link/1789/web)
    + TWITTER.COM/PROGRAMERHUMOR

(`是也乎:`

![Switch](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.43.20.jpg)

上次相同图片标题是:

    真实 Python 升级

)


- [为毛 dict() 和 {} 竟然并不等同?](https://pycoders.com/link/1794/web)
    + REDDIT

(`是也乎:`

简单说历史梗:

`dict()` 是函式嗯哼, 
而 `{}` 则是语法解析.

    >>> import dis
    >>> def a():
    ...      b = dict()
    >>> dis.dis(a)
      2           0 LOAD_GLOBAL              0 (dict)
                  2 CALL_FUNCTION            0
                  4 STORE_FAST               0 (b)
                  6 LOAD_CONST               0 (None)
                  8 RETURN_VALUE
    >>> def c():
    ...    d = {}
    ...
     >>> dis.dis(c)
      2           0 BUILD_MAP                0
                  2 STORE_FAST               0 (d)
                  4 LOAD_CONST               0 (None)
                  6 RETURN_VALUE

)



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [Python中的OOP方法类型:@classmethod vs @staticmethod vs Instance Methods](https://pycoders.com/link/1805/web)
    + REAL PYTHON video

What's the difference between @classmethod, @staticmethod, and "plain/regular" instance methods in Python? You'll know the answer after watching this video series and playing with the accompanying code examples.

(`是也乎:`

![OOP](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.39.25.jpg)

不得不说, 真蟒 被蟒周刊发现后,
插图丰富了很多...

OOP 在编程实践中的确非常象用来陈列的精致画框...


)


- [中世纪手稿中的杀手兔](https://pycoders.com/link/1815/web)
    + OPENCULTURE.COM

Why so many drawings in the margins depict bunnies going bad... 

(`是也乎:`

![Killer Rabbits](http://cdn8.openculture.com/2019/03/28210146/BadRabbits1.jpg)

等等,这和 Python 有什么关系?

> ...一个历史问题仍然没有答案:他们在多大程度上影响了现代电影喜剧,Monty Python和圣杯的创作?


`ರ_ರ`...看来 蟒周刊 创作团队是放爬虫来收集文章的...


)


- [Windows 10 2010年5月将追加 Python ?](https://pycoders.com/link/1790/web)
    + STEVE DOWER (MICROSOFT)

Python might be hard to install on Windows, but with the latest Windows 10 update, you can type python to find it in the Microsoft Store.

(`是也乎:`

在 Linux 们内置发行20多年后?

当然 Microsoft Store 是个全新的混合嗯哼.

)


- [50,000,000个 Twisted's 下载不能出错](https://pycoders.com/link/1793/web)
    + AMBER BROWN

Twisted's release manager discusses decision to continue supporting Python 2.7.

(`是也乎:`

有 Twisted 在 Py2 还能再用10年.
)

- [PyCon 的冒名顶替者](https://pycoders.com/link/1810/web)
    + JIM ANDERSON

"I've been working more with beginning programmers recently and have heard them talking about feeling like an impostor on a frequent basis, so this time when the feeling struck, I paid attention to it."

(`是也乎:`

嗯哼? 还有这种操作?

其实, 就是 `顶替者效应` ~ 一种社会灌输的心理疾病.


)

- [如何在 Python 中实现堆栈数据结构](https://pycoders.com/link/1799/web)
    + REAL PYTHON

In this tutorial, you'll learn how to implement a stack in Python. You'll see how to recognize when a stack is a good choice for data structures, how to decide which implementation is best for a program, and what extra considerations to make about stacks in a threading or multiprocessing environment.


(`是也乎:`

![Stack](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.37.07.jpg)

嗯哼, 不是从 0 开始? 差评.

)


- [Python 的多元线性回归](https://pycoders.com/link/1813/web)
    + DAN NELSON

- [提高 Django Rest 框架中的序列化性能](https://pycoders.com/link/1812/web)
    + HAKI BENITA

- [Why Do Python Lists Let You += a Tuple, When You Can't + a Tuple?](https://pycoders.com/link/1804/web)
    + REUVEN LERNER




## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [kivyImageViewer: Kivy-Powered Image Viewer Using Python 3](https://pycoders.com/link/1816/web)
    + GITHUB.COM/OHLOGIC


(`是也乎:`

Kivy 框架哪, 竟然还没死...

)

- [firstcrack: A Simple Static Blog Engine in Python](https://pycoders.com/link/1806/web)
    + BITBUCKET.ORG/ZJSZEWCZYK

(`是也乎:L`

叕一个 SSG 引擎,
没上 PyPi, 在 bitbucket 发布...
怎么看都没试用的冲动哪...

)


- [opem: Open Source PEM Fuel Cell Simulation Tool](https://pycoders.com/link/1814/web)
    + GITHUB.COM/ECSIM • Shared by Sepand Haghighi

(`是也乎:`

![OPEM_BLOCK_DIAGRAM](https://github.com/ECSIM/opem/raw/master/otherfile/OPEM_BLOCK_DIAGRAM.jpg)

![ScreenShot](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.32.19.jpg)

那一堆嗯哼, 一看就知道是认真的...
)

- [qcircuits: Simulating Small-Scale Quantum Computers With Python](https://pycoders.com/link/1802/web)
    + GITHUB.COM/GREY-AREA

(`是也乎:`

叕一个量子计算框架...

)


- [graalpython: Python 3 Implementation Built on GraalVM](https://pycoders.com/link/1796/web)
    + GITHUB.COM/GRAALVM

(`是也乎:`

叕一个全新编译平台拿 Python 来练手了...
)

- [pyramid_openapi3: Validate Pyramid Views Against an OpenAPI 3.0 Document](https://pycoders.com/link/1811/web)
    + GITHUB.COM/PYLONS

(`是也乎:`

无论如何, Zope 系社区的韧劲是不得不佩服的...

)


- [Fragile: Office 365 VSTS-inspired Kanban Board as a Terminal Curses App](https://pycoders.com/link/1795/web)
    + GITHUB.COM/DMGOLEMBIOWSKI


(`是也乎:`

![Fragile](https://camo.githubusercontent.com/2db6a5b83619fdb2f95c3a373dad44221bd9aef3/68747470733a2f2f64676f6c656d62696f77736b692e636f6d2f63646e2f66726167696c656d656e752e706e67)

从截屏来看, 可以先不期待
)



## 📆🐍 活动/大会
> Events


- [⋅ PyMNTos](https://pycoders.com/link/1798/web)
    + June 13, 2019
    + (pronounced pie-min-tose)

(`是也乎:`

姊妹城市 MeetUP

)

- [⋅ Python Atlanta](https://pycoders.com/link/1784/web)
    + June 13, 2019
    + USA

- [⋅ PyLondinium](https://pycoders.com/link/1803/web)
    + June 14 to June 17, 2019
    + 英国

- [⋅ PyCon CZ 2019](https://pycoders.com/link/1797/web)
    + June 14 to June 17, 2019
    + 捷克

(`是也乎:`

<img src="https://cz.pycon.org/2019/static/img/pycon19-logo.a13af6437f36.svg"
 high="80"/>

)

- [⋅ PyCon Thailand](https://pycoders.com/link/1808/web)
    + June 15 to June 17, 2019
    + 泰国...

- [⋅ Dash Conference](https://pycoders.com/link/1819/web)
    + July 16–17 in NYC
    + $572/人


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 已开班, 进入 ch9
    + 下期可能 7月1


- [TechEmpower Framework Benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijmrj-7)
    + via Haskell
    + 黄毅🐾

(`是也乎:`
![benchmarks](https://ipic.zoomquiet.top/2019-06-12-ScreenShot%202019-06-12%2010.05.32.jpg)

> 看这个也比较有意思,fastapi是一个high level的web框架,其实在go里面找不到竞品,但是性能可以在一个段位.  

所以说, GC 什么的, 在 Py 世界, 其实并不是一个关键大坑...

)



[![PyScaffold](https://pyscaffold.org/en/latest/_images/logo.png)](https://pyscaffold.org/en/latest/)

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
> ...

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
    + 北京
    + anti-996


# 是也乎

- 190612 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190612 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
