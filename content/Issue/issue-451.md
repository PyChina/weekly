Title: Issue 451
Slug: issue-451
Date: 2020-12-16 11:42
Tags: Weekly,Python,pycoders,ZH


> 通过练习学 Python 的生成器/协程


原文: [PyCoder's Weekly - Issue #451](https://pycoders.com/issues/451)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201216 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201216 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 位运算符](https://pycoders.com/link/5351/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use Python’s bitwise operators to manipulate individual bits of data at the most granular level. With the help of hands-on examples, you’ll see how you can apply bitmasks and overload bitwise operators to control binary data in your code.

(`是也乎:`


![Bitwise](http://ydlj.zoomquiet.top/ipic/2020-12-16-ScreenShot%202020-12-16%2016.40.28.jpg)

回到汇编 ;-)


)


- [用 mypy 进行详尽检查](https://pycoders.com/link/5347/web)
    + HAKI BENITA

What if mypy could warn you about possible problems at “compile time”? In this article, you’ll learn a little trick to get mypy to fail when a value in an enumeration type is left unhandled.

- [用 Python 安排各种定期作业](https://pycoders.com/link/5363/web)
    + TOWARDSDATASCIENCE.COM 
    + • Shared by Martin Heinz

Every software developer, data scientist, and sysadmin must, at some point, schedule jobs to run. In this article, you’ll learn how to do this with Python. You’ll encounter a number of methods for scheduling jobs, from using the standard library to leveraging third-party packages.


(`是也乎:`

嚓, 这口气大了, 也的确需要

)


- [Python 的对象物件系统如何运作](https://pycoders.com/link/5340/web)
    + VICTOR


The Python object system is one of the most important parts of the Python language. Mastering it is essential to mastering the Python language. Learn how the object system works by examining the CPython source code in this detailed tutorial.


(`是也乎:`

灵魂追问了,
从代码上看, 老爹也一直在纠结ing....

)


- [什么是数据工程/是否适合您?](https://pycoders.com/link/5368/web)
    + REAL PYTHON

In this article, you’ll get an overview of the discipline of data engineering. You’ll learn what is and isn’t part of a data engineer’s job, who data engineers work with, and why data engineers play a crucial role in many industries.


(`是也乎:`

![DataE](http://ydlj.zoomquiet.top/ipic/2020-12-16-ScreenShot%202020-12-16%2016.41.00.jpg)

扫盲贴 ;-)


)


- [Python 软件基金会 2020 募捐者](https://pycoders.com/link/5346/web)
    + PYTHON.ORG

Help the PSF recover funds lost due to COVID-19.

(`是也乎:`

等等, 哪儿?
俺也得捐.

)


- [PyTorch 1.7.1 发布: 更新 Python 3.9 二进制文件](https://pycoders.com/link/5348/web)
    + GITHUB.COM/PYTORCH

- [Python 3.9.1 最终版本](https://pycoders.com/link/5344/web)
    + PYTHON.ORG

- [Qt 6.0 发布](https://pycoders.com/link/5353/web)
    + QT.IO 
    + • Shared by Bartosz Zaczyński

(`是也乎:`

嚓了,
真.活久见

)


## 探讨/吐糟
> Discussions


- [为什么正等号适用于列表和字典?](https://pycoders.com/link/5361/web)
    + STACK OVERFLOW

The docs for the .__iadd__() special method don’t make it clear why it works for collections like lists and dictionaries. Time to peruse some CPython source code!

## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Python 结构模式再次匹配形态](https://pycoders.com/link/5338/web)
    + JAKE EDGE

Follow the saga of PEP 622 which proposes to add a new structural pattern matching feature to Python. There have been a number of updates to the PEP, as well as some animated discussion in the Python-dev mailing list.

- [通过练习学习Python 的生成器/协程](https://pycoders.com/link/5350/web)
    + REAL PYTHON 
    + podcast

Have you started to use generators in Python? Are you unsure why you would even use one over a regular function? How do you use the special “send” method and the “yield from” syntax? This week on the show, we have Reuven Lerner to talk about his PyCon Africa 2020 talk titled “Generators, coroutines, and nanoservices.”


(`是也乎:`


![podcast](http://ydlj.zoomquiet.top/ipic/2020-12-16-ScreenShot%202020-12-16%2016.36.12.jpg)
)

- [面向初学者的 Python Turtle](https://pycoders.com/link/5359/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn the basics of Python programming with the help of a simple and interactive Python library called turtle. If you’re a beginner to Python, then this course will definitely help you on your journey as you take your first steps into the world of programming.

(`是也乎:`

永远的小乌龟 ;-)

不过, 针对儿童吧, 对成人感觉没什么帮助,
刺激点不对.

)


- [俺的 Evolution Writing JSON-REST APIs](https://pycoders.com/link/5370/web)
    + PHILIP JONES

After writing JSON-REST APIs for a number of years, Philip Jones noticed that there were shortcomings with documenting API structure and validating data sent and received. In this article, Philip discusses how he solved both of these issues with the quart-schema package.

- [地图和 Django: GeoDjango, SpatiaLite 以及 Leaflet](https://pycoders.com/link/5364/web)
    + PAOLO MELCHIORRE

In part one of this series, you’ll get a quickstart guide to creating web maps with the Python-based web framework Django using its module GeoDjango, the SQLite database with its spatial extension SpatiaLite and Leaflet, a JavaScript library for interactive maps.


(`是也乎:`

虽然, Pg 们内置了强大的 GEO 系列能力,
但是, 反应到 Django 框架中,
还得有个反应时期...

)



- [在 Python 中实施 Rust 的 dbg! ](https://pycoders.com/link/5357/web)
    + RAPHAEL

Rust’s dbg macro is a useful expression printer that adds the source line to what is printed. In this article, Raphael shows you how to implement a similar function in Python and discusses many of the intricacies involved with inspecting code states.


(`是也乎:`

来了, 
反正流行什么, 
fans 就住 Python 中 mix 什么.
而且都成功了.

)


- [通过并发加速 Python](https://pycoders.com/link/5339/web)
    + REAL PYTHON 
    + course

Learn what concurrency means in Python and why you might want to use it. You’ll see a simple, non-concurrent approach and then look into why you’d want threading, asyncio, or multiprocessing.


(`是也乎:`

![Concurrency](http://ydlj.zoomquiet.top/ipic/2020-12-16-ScreenShot%202020-12-16%2016.32.33.jpg)

反正,就是要快...

)


- [用 Graphene,SQLAlchemy 和 oso 进行 GraphQL 授权](https://pycoders.com/link/5369/web)
    + DAVID HATCH 
    + • Shared by Stephie Glaser

Learn how to set up a GraphQL authorization layer between Graphene and SQLAlchemy using oso’s open-source authorization library and the sqlalchemy-oso package.


   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [dirsearch: Web 路径扫描程序](https://pycoders.com/link/5356/web)
    + GITHUB.COM/MAUROSORIA

(`是也乎:`

来自 `毛里求斯`

)

- [visidata: 用于发现和整理数据的终端电子表格复合工具](https://pycoders.com/link/5360/web)
    + GITHUB.COM/SAULPW

- [asv: 有 Web报告 的基准测试工具](https://pycoders.com/link/5349/web)
    + GITHUB.COM/AIRSPEED-VELOCITY

- [py-applescript: 用以 NSAppleScript 的易用 Python 包装器](https://pycoders.com/link/5345/web)
    + GITHUB.COM/RDHYEE

- [sqlalchemy-oso: 用于授权的开源策略工程](https://pycoders.com/link/5366/web)
    + GITHUB.COM/OSOHQ

(`是也乎:`

> 策略工程

哗, 这 Bigger 突破天际.

)

- [beartype: 纯 Python 实现的, 快到飞溅的 O(1) 运行时类型检查](https://pycoders.com/link/5342/web)
    + GITHUB.COM/BEARTYPE

- [quart-schema: Quart 的模式验证和自动文档](https://pycoders.com/link/5365/web)
    + GITLAB.COM/PGJONES



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

 - [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5352/web)
     + December 16, 2020

(`是也乎:`

硬广, 但是, 足够有趣 ;-)

)

- [⋅ BelPy](https://pycoders.com/link/5371/web)
    + January 30 – 31, 2021

- [⋅ PyCascades 2021](https://pycoders.com/link/5372/web)
    + February 19 – 21, 2021

- [⋅ PyCon 2021](https://pycoders.com/link/5373/web)
    + May 12 – 18, 2021


![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)

- [PyCon2020中国, 明年见](https://mp.weixin.qq.com/s/9u4NP0CAzZMqy96C9y-OHg)
    + 11.28~29
    + 在线

(`是也乎:`

[PyCon20深圳 大妈 暖场小单口](https://mp.weixin.qq.com/s/OrHA4vimeHUYDROQ9G75GA)

并实锤可用神器:
[NixOS - NixOS Linux](https://nixos.org/)

nix 可以跨语言非Docker 将开发和运行时环境精确锁定.

以及 PyCon19广州 的坑终于填上了:

- [欢迎使用 lightning ](https://gitmen.gitee.io/lightning-doc/)
    + [GitHub](https://github.com/git-men/lightning)
    + [OSC](https://gitee.com/gitmen/lightning)

基于Django的无代码Admin + 低代码开发框架


)


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

None 

# PS:
- 首发: [Issue 451 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-451.html)
- 修订: [issue-451.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-451.md)


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
>> NN 4229


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/451)






