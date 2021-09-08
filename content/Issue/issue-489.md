Title: PyCoder 489
Slug: issue-489
Date: 2021-09-08 11:42
Tags: Weekly,Python,pycoders,ZH


> 全新姿势来告知你 Python 代码很糟糕


原文: [PyCoder's Weekly - Issue #489](https://pycoders.com/issues/489)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 210908 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210908 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [PEP 668: 外部和Python包管理人员之间的优雅合作](https://pycoders.com/link/6989/web)
    + PYTHON.ORG

This draft PEP proposes a way for resolving conflicts between OS package managers (e.g. apt) and Python-specific package management tools (e.g. pip).




- [学习Python需要多长时间?](https://pycoders.com/link/6964/web)
    + REAL PYTHON

How should someone assess whether or not learning Python is a good investment of their time, how long it will take them, and what background factors they need to consider when planning their learning journey? This article attempts to clarify these common beginner questions.


(`是也乎:`

![Learn](https://ipic.zoomquiet.top/2021-09-08-ScreenShot%202021-09-08%2011.14.47.jpg)

简单说, 42分钟到42年不等...


![学习阶段](https://ipic.zoomquiet.top/2021-09-08-four-stages.d678c620edb0.png)

嗯哼? 对比俺之前的断言

    Unknow Unknow 不知不知何 unconscious incompetence 无意识无能
    Unknow Know   不知己知何 conscious incompetence 有意识的无能
    Know Know     知己已知何 conscious competence 意识能力
    Know Unknow   知己不知何 unconscious competence 无意识能力

)


- [Track Python Application Performance With End-to-End Tracing With Datadog APM](https://pycoders.com/link/6954/web)
    + DATADOG
    + sponsor

With Datadog APM you can debug errors and bottlenecks in your code by tracing requests across web servers and services in your environment. Then correlate between distributed request traces, metrics, and logs to troubleshoot issues without switching tools or contexts. Try Datadog APM free →

- [如何用 Python 跟踪私人财务](https://pycoders.com/link/6973/web)
    + SIDDHANT GOEL

This post introduces readers to a workflow for tracking their personal finances using only the Python ecosystem. The end result is extremely focused on data privacy, uses only open-source software, and is 100% self-hosted.

(`是也乎:`

等等, 首先私人资金要多少, 才值得上手段来进行金融管理?

)



- [全新姿势来告知你 Python 代码很糟糕](https://pycoders.com/link/6993/web)
    + NICK DROZD

How and why the author added two new linter rules to Pylint: consider-ternary-expression and while-used.


(`是也乎:`

圈复杂度的另类使用...?

)

- [Forgiveness in Python 的成本要求](https://pycoders.com/link/6980/web)
    + WALID ZIOUCHE

A discussion of EAFP (“Easier to ask for forgiveness than permission”) vs LBYL (“Look before you leap”) code patterns in Python.

(`是也乎:`

嗯哼? 还有这种编程流派的?


)



- [Nuitka 0.6.15 发布](https://pycoders.com/link/6975/web)
    + NUITKA DEV BLOG

Nuitka is a Python compiler written in Python, compatible with Python2 (2.6, 2.7) and Python3 (3.3–3.9). You feed Nuitka your Python source code and it generates an executable or extension module.


(`是也乎:`


淦...非官方编译器

)


- [Credit-Card-Stealing, 在 PyPI 上发现的后门包](https://pycoders.com/link/6984/web)
    + CHRIS WILLIAMS




-----------------------------------------
## 探讨/吐糟
> Discussions



- [Is Django Rest Framework (DRF) 仍然活着吗?](https://pycoders.com/link/6956/web)
    + GITHUB.COM/ENCODE

- [如果由您来管理 Django 项目, 未来12个月会关注什么?](https://pycoders.com/link/6961/web)
    + REDDIT


(`是也乎:`

怎么都是 Django 相关的讨论?

Django 接下来重要问题和其它框架类似:
云原生, 开发速度, 运行速度

)


- [你开发的前五个程序是什么?](https://pycoders.com/link/6982/web)
    + REDDIT

(`是也乎:`


    hallo world
    hello world
    hollo world
    hillo world
    hullo world

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 Python 的数学模块并挖掘出实用的 Pandas 函数](https://pycoders.com/link/6963/web)
    + REAL PYTHON 
    + podcast

How well do you know Python’s math module? Maybe you’ve used a few of the constants or arithmetic functions. You may be surprised by the amount of functionality hiding within this built-in library, and perhaps you don’t need to reach for an additional outside library for common use cases.



(`是也乎:`

![podcast](https://ipic.zoomquiet.top/2021-09-08-ScreenShot%202021-09-08%2011.03.47.jpg)


老司机就是顺滑...

)

- [令 NumPy 易用: 指南和工具](https://pycoders.com/link/6983/web)
    + MARS LEE

“NumPy is now foundational to Python scientific computing. Our efforts reach millions of developers each month. As our user base grows, we recognize that we are neglecting the disabled community by not having our website and documentation up to modern accessibility standards.”




- [Type4Py 开发和发布: 基于机器学习, 为 Python 类型自动完成 ](https://pycoders.com/link/6981/web)
    + AMIR MIR

”[…] retrofitting types is a cumbersome and error-prone process. To address this, we propose Type4Py, an ML-based type auto-completion for Python. It assists developers to gradually add type annotations to their codebases.”

- [用 python 和 ggplot 绘制图表数据](https://pycoders.com/link/6991/web)
    + REAL PYTHON 
    + course

Learn how to use ggplot in Python to build data visualizations with plotnine. You’ll discover what a grammar of graphics is and how it can help you create plots in a very concise and consistent way.

(`是也乎:`

![ggplot](https://ipic.zoomquiet.top/2021-09-08-ScreenShot%202021-09-08%2011.00.03.jpg)

ggplot 和 matplotlib 简直天差地别,
完全两种思路/风格以及形式,
不过, 运行的快, 就象 Tk 和其它 GUI 框架的区别,
喜欢的值得深入;

)


- [Web Scraping 在 Python: 用分布式爬虫网进行缩放](https://pycoders.com/link/6969/web)
    + ANDER RODRÍGUEZ

“Build your own distributed crawler with custom parsers […] Discover new pages and store the exact content you need, all in less than 300 LOC.”


(`是也乎:`

其实多数是专项爬取,
并不值得上分布式..

)

- [用 neo4j 可视化 python 需要的模块和依赖](https://pycoders.com/link/6985/web)
    + ADNAN SIDDIQI

“A simple neo4j tutorial about a Python tool that ingests information about all installed Python modules on your computer and visualizes it.”

(`是也乎:`

其实除非要求网页交互,
否则一个静态图片, 或是系列图片更好管理和使用

)


- [介绍用 Python + Matplotlib 创建图表](https://pycoders.com/link/6966/web)
    + MIKE DRISCOLL

Learn how to create multiple types of graphs and add legends, titles and more in this tutorial about matplotlib and Python.

(`是也乎:`

其实, 官方教程就足够了, 
有个
[The Lifecycle of a Plot](http://matplotlib.org/3.3.3/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py)

简单道尽天机, 推荐常看
)



- [不用没有操作系统的 Python  \[2015\]](https://pycoders.com/link/6962/web)
    + JAKE EDGE

How Josh Triplett and his colleagues at Intel got the Python interpreter to run inside the GRUB boot loader.

- [attrs vs pydantic](https://pycoders.com/link/6978/web)
    + TIN TVRTKOVIĆ 
    • Shared by Python Bytes FM opinion

An account of why the author prefers using the attrs library over Pydantic.

- [什么是python的省略号（...）对象?](https://pycoders.com/link/6970/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [legendary: Epic 游戏加载器开源替代品](https://pycoders.com/link/6974/web)
    + GITHUB.COM/DERROD

- [freqtrade: Free, Open Source Crypto Trading Bot](https://pycoders.com/link/6968/web)
    + GITHUB.COM/FREQTRADE

- [xdoctest: Python的内置 doctest 模块的改进版本](https://pycoders.com/link/6960/web)
    + GITHUB.COM/EROTEMIC

(`是也乎:`

doctest 想法很神奇, 
只是真要规模化使用,
还是不如集中管理测试案例来的工程化.
不过, 这种贴切的感觉令人怀念,
所以, 当然有改进...

)


- [pint: 定义/操作和操纵物理量](https://pycoders.com/link/6965/web)
    + PINT.READTHEDOCS.IO

(`是也乎:`

各种仿真测试/模拟 必备模块

)

- [nntpserver.py: 无依赖性，单个文件 NNTP 服务器库](https://pycoders.com/link/6995/web)
    + GITHUB.COM/EPILYS

(`是也乎:`

叕一个单文件服务,
Bottle 早已证明, 一个文件也可以作到很爽


USENET/新闻组 服务, 
上古神器, 当年的8卦都在其中流传的...


)


- [prettymaps: 从 OpenStreetMap 数据绘制漂亮的地图](https://pycoders.com/link/6996/web)
    + GITHUB.COM/MARCELOPRATES

(`是也乎:`

![prettymaps](https://ipic.zoomquiet.top/2021-09-08-ScreenShot%202021-09-08%2010.29.07.jpg)

WoW 风格化地图绘制器

![MACAO](https://ipic.zoomquiet.top/2021-09-08-ScreenShot%202021-09-08%2011.46.39.jpg)
)


- [venv-kernel: 使用 Jupyter 笔记本中的虚拟环境](https://pycoders.com/link/6972/web)
    + PYPI.ORG • Shared by Björn Rüffer

(`是也乎:`

将环境管理提升到 jupyer 层面了...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyConline AU 2021](https://pycoders.com/link/6976/web)
    + September 10 to September 13, 2021

- [⋅ PyCon Odessa 2021](https://pycoders.com/link/6992/web)
    + September 11 to September 13, 2021

- [⋅ Python Miami](https://pycoders.com/link/6994/web)
    + September 11 to September 12, 2021

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/6959/web)
    + September 11, 2021

- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/6958/web)
    + September 14 to September 15, 2021

- [⋅ PyCon India 2021](https://pycoders.com/link/6986/web)
    + September 17 to September 21, 2021
 



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



-----------------------------------------
# PS:

- 首发: [Issue 489 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-489.html)
- 修订: [issue-489.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-489.md)


## PPS:
> 不觉中蟒周刊快译已经到了第9个年头

去年开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
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

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF489D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF489D4Q90XdDA7g):



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





