Title: PyCoder 493
Slug: issue-493
Date: 2021-10-06 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.10 中值得尝试的新特性...


原文: [PyCoder's Weekly - Issue #493](https://pycoders.com/issues/493)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 211006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 3.10: 炫酷特性值得尝试](https://pycoders.com/link/7151/web)
    + REAL PYTHON

Explore some of the coolest and most useful features in Python 3.10. You’ll appreciate more user-friendly error messages, learn about how you can handle complicated data structures with structural pattern matching, and explore new enhancements to Python’s type system.

(`是也乎:`

![Cool](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.55.00.jpg)

改进了 error message,
加强了模式匹配,
拓展了 pattern, 比如:


    def greet(name):
        match name:
            case "Guido":
                print("Hi, Guido!")
            case _:
                print("Howdy, stranger!")

嗯哼, Elixir 们的语法;

    def fizzbuzz(number):
        mod_3 = number % 3
        mod_5 = number % 5

        match (mod_3, mod_5):
            case (0, 0):
                return "fizzbuzz"
            case (0, _):
                return "fizz"
            case (_, 0):
                return "buzz"
            case _:
                return str(number)


)


- [Python 3.10: 官方下载链接以及变更说明](https://pycoders.com/link/7161/web)
    + PYTHON.ORG

- [Data Elixir: 数据科学新闻组](https://pycoders.com/link/7121/web)
    + DATA ELIXIR
    + sponsor

Data Elixir is an email newsletter that keeps you on top of the tools and trends in Data Science. Covers machine learning, data visualization, analytics, and strategy. 
[Curated weekly with top picks from around the web →](https://pycoders.com/link/7121/web)

(`是也乎:`


![ELIXIR](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.50.53.jpg)


串行了...
继 go+ 立志取代 R/Python 作为数据科学主力语言后,
Elixir 也开始进入这一领域...

)



- [Python 3.10 发布 Party Stream](https://pycoders.com/link/7156/web)
    + YOUTUBE.COM video

A recording of the Python 3.10 Release Stream with Pablo Galindo, CPython Core Developer and Python 3.10 Release Manager, and Leon Sandøy.



- [Python 3.10 释放值得现在使用嘛?](https://pycoders.com/link/7155/web)
    + ITAMAR TURNER-TRAURING opinion

- [Python 3.11 将有 “零成本” Exception Handling](https://pycoders.com/link/7153/web)
    + PYTHON.ORG

With “Zero-cost” exceptions the cost of try statements is almost eliminated when no exception is raised.

- [Coverage 6.0 已发布](https://pycoders.com/link/7154/web)
    + NED BATCHELDER

- [Django 3.2.8 已发布](https://pycoders.com/link/7159/web)
    + DJANGO SOFTWARE FOUNDATION





-----------------------------------------
## 探讨/吐糟
> Discussions



- [是什么定义了 Python 中的数字? 问题可能出乎我们的意料...](https://pycoders.com/link/7137/web)
    + STACK OVERFLOW 
    + • Shared by Alex Waygood

Static type-checkers such as Mypy have grown increasingly popular in recent years in the Python community, yet it’s surprisingly difficult to write a type hint that will accept any number. This answer on Stack Overflow digs into why.

- [为毛总是感觉大家都在玩代码 Glof ?](https://pycoders.com/link/7146/web)
    + REDDIT

Why explicit is better than implicit, or in Martin Fowler’s words: “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”

(`是也乎:`

只有 NB 的程序猿才写得出人类可以理解的代码.

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks

- [使您的 Python 应用通过文本用户界面进行交互式](https://pycoders.com/link/7158/web)
    + REAL PYTHON 
    + podcast

Have you wanted to create a Python application that goes further than a command-line interface? You would like it to have a friendly interface but don’t want to make a GUI (Graphical User Interface) or web application. Maybe a TUI (Text User Interface)would be a perfect fit for the project. This week on the show, it’s Will McGugan talking about his projects Textual and Rich.


(`是也乎:`

![TUI](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.42.45.jpg)

对于日常生活在 CLI 中的,
TUI 才是王道哪...

![TUI](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.48.00.jpg)
)


- [多队列与django celery:  何时以及如何使用它们](https://pycoders.com/link/7135/web)
    + APPLIKU.COM

How to work with multiple queues in Celery, when you need it and how to set it up. The tutorial includes file processing and DNS lookups for domains of email addresses. Also, docker-compose.yml is covered for local development.



- [将 Django 项目运行在 Heroku](https://pycoders.com/link/7162/web)
    + REAL PYTHON

In this step-by-step project, you’ll learn about hosting Django projects in the cloud using Heroku, a platform-as-a-service (PaaS) provider used by many startups and developers.

(`是也乎:`

Heroku ? 远古的呼唤...

)



- [比例字体和 YAPF vs 黑色](https://pycoders.com/link/7160/web)
    + NELSON MINAR

How to set up VSCode to deal nicely with proportional fonts and set up automated code formatting that leads to a visually pleasing result.

(`是也乎:`

![Yapf](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.40.03.jpg)

等等, 难道不是必须等宽嘛?

)


- [Code Style 很重要](https://pycoders.com/link/7132/web)
    + RODRIGO GIRÃO SERRÃO

An article about the importance of having a consistent Python coding style and tools that can help you achieve this goal.

- [介绍 Python Editors](https://pycoders.com/link/7127/web)
    + MIKE DRISCOLL

Learn about some of the most popular Python editors in this tutorial. Includes info on PyCharm, WingIDE, VSCode, and IDLE

(`是也乎:`

其实, 还是 Leo 最赛高,
如果真的理解并习惯 文学化编辑...

)

- [PostgreSQL vs Python 进行数据评估: 什么/为什么以及如何](https://pycoders.com/link/7163/web)
    + MIRANDA AUHL

A primer on using PostgreSQL to more efficiently perform your data evaluation tasks done in Excel, R, or Python.



- [Python Developers 的 Docker 最佳实践 ](https://pycoders.com/link/7131/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

A look at several best practices to make your Dockerfiles and images cleaner, leaner, and more secure.

(`是也乎:`

Docker 作为缝合怪,
也是有专有使用技巧的,
得熟练, 然后就自然不过脑了...


)


- [用 borb 在 python 中创建惊人的 PDF 传单](https://pycoders.com/link/7123/web)
    + JORIS SCHELLEKENS 
    + • Shared by Joris Schellekens

This guide shows you how to create a nice-looking PDF flyer in Python using the borb PDF library.

- [用 Assembly 编写 Python Extensions](https://pycoders.com/link/7136/web)
    + ANTHONY SHAW

How to write a CPython Extension in 100% assembly.


(`是也乎:`

![Assembly](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.30.55.jpg)


)

- [如何探索 SQL 注入: 用 IBM 和 Python 为例](https://pycoders.com/link/7138/web)
    + GUILHERME LATROVA 
    + • Shared by Guilherme Latrova



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [MagInkCal: E-Ink Magic Calendar Powered by a Raspberry Pi Zero](https://pycoders.com/link/7152/web)
    + GITHUB.COM/SPEEDYG0NZ

(`是也乎:`

![MagInkCal](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.26.21.jpg)


等等,这么大电子墨水屏就不少銭了哈...
Raspberry Pi Zero 的实用化作品.

)


- [sqlfluff: SQL Linter, Written in Python](https://pycoders.com/link/7143/web)
    + SQLFLUFF.COM 
    + • Shared by Python Bytes FM

(`是也乎:`

SQL 标准其实也很复杂,
静态分享工具, 果断有Python 一份儿

)


- [Confusables: Unicode Normalizing Library to Parse Attacker Text as English](https://pycoders.com/link/7157/web)
    + GITHUB.COM/WANDERINGSTAN

- [runtype: Utilities for Run-Time Type Validation and Multiple Dispatch](https://pycoders.com/link/7150/web)
    + GITHUB.COM/EREZSH

- [Jupytext: Jupyter Notebooks as Markdown Documents or Python Scripts](https://pycoders.com/link/7149/web)
    + MATT WRIGHT

- [wonk: Combine AWS Policy Files Into Smaller Compiled Policy Sets](https://pycoders.com/link/7126/web)
    + GITHUB.COM/AMINOHEALTH 
    + • Shared by Kirk Strauser

- [pyan: Static Call Graph Generator for Python 3](https://pycoders.com/link/7145/web)
    + GITHUB.COM/TECHNOLOGICAT


(`是也乎:`


![pyan](https://ipic.zoomquiet.top/2021-10-06-ScreenShot%202021-10-06%2009.24.01.jpg)


叕一个基于 Graphviz 的图形脚本工具,
用 Python 完成说明,
自动生成优化后的 .dot 脚本,
然后使用 Graphviz 标准工具生成目标图形,
简直就是 Python 作为胶水语言的天然用法...


)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



⋅ PyCon ZA 2021 October 7 to October 9, 2021

⋅ Canberra Python Meetup October 7, 2021

- [⋅ Sydney Python User Group (SyPy)](https://pycoders.com/link/7133/web)
    + October 7, 2021
    + 澳洲

- [⋅ Reunión Python Valencia](https://pycoders.com/link/7130/web)
    + October 7, 2021

- [⋅ Python Miami](https://pycoders.com/link/7142/web)
    + October 9 to October 10, 2021

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/7140/web)
    + October 9, 2021




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

- 首发: [Issue 493 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-493.html)
- 修订: [issue-493.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-493.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF493D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF493D4Q90XdDA7g):



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





