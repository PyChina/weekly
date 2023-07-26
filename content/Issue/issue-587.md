Title: 蠎周刊(PyCoder)587
Slug: issue-587
Date: 2023-07-26 11:42
Tags: Weekly,Python,pycoders,ZH


> Cython 3.0.0 发布


原文: [PyCoder's Weekly - Issue #587](https://pycoders.com/issues/587)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230726 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230726 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [用 Python Folium 根据数据创建 Web 地图](https://pycoders.com/link/11175/web)
    + REAL PYTHON 
    + COURSE

You’ll learn how to create web maps from data using Folium. The package combines Python’s data-wrangling strengths with the data-visualization power of the JavaScript library Leaflet. In this video course, you’ll create and style a choropleth world map showing the ecological footprint per country.

(`是也乎:`

![Folium](https://ipic.zoomquiet.top/2023-07-26-zshot%202023-07-26%2011.28.15.jpg)


真蟒 将通用知识说光了,
也就进入了专项知识点解说状态,
现在也早已开放投稿分成机制,
只是不支持中文版本...

)


- [Writing a 6502 Emulator in Python
用 Python 编写 6502 模拟器](https://pycoders.com/link/11187/web)
    + DAILYSTUFF

The 6502 processor from Motorola was quite popular and could be found in the Nintendo and Sega consoles as well as the Commodore 64. This very detailed article shows you how to build an emulator for the processor in Python.

(`是也乎:`


神奇哪...叕一个专门领域知识

)



- [用 PyStack 调试 Python 中的崩溃和死锁](https://pycoders.com/link/11171/web)
    + MARTINHEINZ.DEV 
    + • Shared by Martin Heinz

Using PyStack’s “forbidden magic” to debug deadlocks, segmentation faults, crashes and other difficult bugs in Python


(`是也乎:`

相比 print 以及 GDB 可能就是观赏性提高了?

)


- [Cython 3.0.0 发布](https://pycoders.com/link/11182/web)
    + CYTHON.READTHEDOCS.IO


(`是也乎:`

可是大家都开始期待 Ruthon 了...

)






-----------------------------------------
## 探讨/吐糟
> Discussions


- [PEP 722: 单文件脚本的依赖关系规范](https://pycoders.com/link/11173/web)
    + PYTHON.ORG




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [Python 分析：如何查找性能瓶颈](https://pycoders.com/link/11165/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to profile your Python programs using numerous tools available in the standard library, third-party libraries, as well as a powerful tool foreign to Python. Along the way, you’ll learn what profiling is and cover a few related concepts.

- [python-mastery: 高级 Python 掌握](https://pycoders.com/link/11163/web)
    + DAVID BEAZLEY

This exercise-driven course is built on top of a GitHub repo, getting you to work along with the provided exercises. The course is aimed at Python programmers who are comfortable with the language basics and want to add depth to their practice.


(`是也乎:`


嗯哼? 这非常 [rust\-lang/rustlings: :crab: Small exercises to get you used to reading and writing Rust code\!](https://github.com/rust-lang/rustlings)

)



- [Netflix 如何在 7 分钟内完成故障转移](https://pycoders.com/link/11189/web)
    + AMJITH RAMANUJAM

Netflix decreased the time it takes to respond to an outage from 45 minutes to seven with no additional cost. This article talks about how they hot-swap processes and reserve compute time to ensure a quick response to outages.


(`是也乎:`

一遍一遍的练习哪...

)


- [浅尝 Python 中的迭代](https://pycoders.com/link/11161/web)
    + BITE CODE

Any object that implements the iterator interface can be used in a for loop, but just how does that work? This article shows you how the iterator protocol is used and how you can write your own compatible objects.


(`是也乎:`

一样的, Python 提供了迭代的自由,
但是, 是否以及如何迭代还是看场景...

)


- [Python 元编程实用指南](https://pycoders.com/link/11178/web)
    + KARISHMA SHUKLA

This article is a high-level overview of the various types of meta-programming available in Python, including decorators, metaclasses, built-in introspection keywords, and dynamic code generation.

(`是也乎:`

高级技巧, 如果业务没复杂到一定得定义子语言时,
可以先知道, 别轻易用...

)



- [高级 Python 开发技巧](https://pycoders.com/link/11169/web)
    + SCOFIELD IDEHEN

You’re starting out in Python and you think you’ve got the language basics down. Where next? This article introduces you to comprehensions. generators, zip, context managers, and more.


(`是也乎:`

注意适用场景, 并不是越高级越值得多用的...

)


- [用 VScode 和 Docker 编写 Python](https://pycoders.com/link/11166/web)
    + GITHUB.COM/RAMIKRISPIN

A step-by-step guide on how to set up a Python environment using VSCode and Docker. It explains why you’d use these tools at all, and walks you through what you need to get them going.


(`是也乎:`

至少10核,64G 以上内存才玩的起;
这种开发流程, 主要是面向直接 Docker 部署的项目;
对应的运营时集群管理也复杂很多, 是否合适要自行定夺...

)


- [Ruff 的 Linting 综合指南](https://pycoders.com/link/11186/web)
    + ZOO CODES

The ruff linter is growing in popularity, partially because of its speed. This article walks you through all its flags and how to use it to improve your Python code quality.




- [如何在 Python 中使用时间序列](https://pycoders.com/link/11176/web)
    + ANBER ARIF

A look at why Python is a great language for time-series analysis with tips on how to get started.

(`是也乎:`

Timescale 的软广...

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [lets-plot: 统计数据绘图库](https://pycoders.com/link/11164/web)
    + GITHUB.COM/JETBRAINS

- [joypy: Python 中的欢乐方言](https://pycoders.com/link/11180/web)
    + GITHUB.COM/CALROC

(`是也乎:`


```
§ Simple Combinators

    joy? 23 [0 >] [dup --] while

    -> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

```

这..不叕是一个 LISP 的 Python 简化版本?

)


- [awesome-python-htmx: Python / HTMX 精选列表](https://pycoders.com/link/11183/web)
    + GITHUB.COM/PYHAT-STACK


(`是也乎:`


真的是轮回, 当年 XML 包含调用服务端的机制,
但是, 服务端口吞吐能力不行,
现在变身为 HTMX 又回来了...

> ...在 PyCon US 2023 上突发灵感，一劳永逸地挑战并击败 JS！

)


- [pytest-cov: Pytest 的覆盖率插件](https://pycoders.com/link/11167/web)
    + GITHUB.COM/PYTEST-DEV

- [tinyvector: 小型最近邻嵌入数据库](https://pycoders.com/link/11177/web)
    + GITHUB.COM/0HQ





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [PyKla Monthly Meetup](https://pycoders.com/link/11174/web)
    + July 26, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11159/web)
    + July 26, 2023

- [SPb Python Drinkup](https://pycoders.com/link/11160/web)
    + July 27, 2023

- [North Bay Python](https://pycoders.com/link/11179/web)
    + July 29 to July 31, 2023

- [PyCon PL 2023](https://pycoders.com/link/11172/web)
    + July 29 to August 3, 2023

- [PyCamp Leipzig 2023](https://pycoders.com/link/11168/web)
    + July 29 to July 31, 2023

- [PyDelhi User Group Meetup](https://pycoders.com/link/11170/web)
    + July 29, 2023

- [PythOnRio Meetup](https://pycoders.com/link/11181/web)
    + July 29, 2023




-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 535](https://weekly.pychina.org/issue/issue-535.html)
- 2021: [蠎周刊 482](https://weekly.pychina.org/issue/issue-482.html)
    + [pythonista-weekly : Pyw 509](https://weekly.pychina.org/python-weekly/pyw-509.html)
- 2020: [蠎周刊 429](https://weekly.pychina.org/issue/issue-429.html)
    + [pythonista-weekly : Pyw 459](https://weekly.pychina.org/python-weekly/pyw-459.html)
- 2019: [蠎周刊 378](https://weekly.pychina.org/issue/issue-378.html)
- 2018: [蠎周刊 327](https://weekly.pychina.org/issue/issue-327.html)
- 2017: [蠎加载 134](https://weekly.pychina.org/importpython/importpython-134.html)
- 2016: [蠎加载 83](https://weekly.pychina.org/importpython/importpython-83.html)
- 2015: [蠎周刊 176](https://weekly.pychina.org/issue/issue-176.html)
    + [蠎加载 42](https://weekly.pychina.org/importpython/importpython-42.html)
- 2014: [Issue 125](https://weekly.pychina.org/issue/issue-125.html)
- 2013: 空缺
- 2012: [Issue 24 Untitled](https://weekly.pychina.org/issue/issue-24.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [@Chaos42DAMA - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + VLog
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...





```
       _~~*~~_
   \/ /  ^ ◵  \ ()
     '_   ♢   _'
     | '--~--' <

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 587 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-587.html)
- 修订: [issue-587.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-587.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF587D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF587D4Q90XdDA7g):



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



