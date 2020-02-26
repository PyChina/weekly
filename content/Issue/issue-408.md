Title: Issue 408
Slug: issue-408
Date: 2020-02-19 14:42
Tags: Weekly,Python,pycoders,ZH

> 一起寻找完美的 Python 代码编辑器吧?



原文: [PyCoder's Weekly - Issue #408](https://pycoders.com/issues/408)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------



- [寻找完美的Python代码编辑器](https://pycoders.com/link/3565/web)
    + REAL PYTHON 
    + video

Find your perfect Python development setup with this review of Python IDEs and code editors. Writing Python using IDLE or the Python REPL is great for simple things, but not ideal for larger programming projects. With this course you'll get an overview of the most common Python coding environments to help you make an informed decision.

(`是也乎:`

真蟒引战技巧越来越好了,
无论计算机发展到哪儿, 嘦说最好的编辑器, 一定一地鳮毛的

![Editor](http://ydlj.zoomquiet.top/ipic/2020-02-19-ScreenShot%202020-02-19%2017.03.25.jpg)

Vim/Thonny/repl.it/Visual Studio Code/PyCharm/Jupyter

这都哪和哪儿比哪...根本比不到点儿上的...

)



- [Python 重载函数  ](https://pycoders.com/link/3575/web)
    + ARPIT BHAYANI

Python does not natively support function overloading (having multiple functions with the same name.) See how you can implement and add this functionality using common language constructs like decorators and dictionaries. Related discussion on Hacker News.


- [PEP 614 (草稿): 放宽装饰器语法限制](https://pycoders.com/link/3577/web)
    + PYTHON.ORG

"Python currently requires that all decorators consist of a dotted name, optionally followed by a single call. This PEP proposes removing these limitations and allowing decorators to be any valid expression." For example, this would become a valid decoration: @buttons[1].clicked.connect

(`是也乎:`

老爹支持的一则草案
希望将类似:


    button_1 = buttons[1]
    ...
    @button_1.clicked.connect
    def eggs():
        ...

合理化为:

    @buttons[1].clicked.connect
    def eggs():
        ...


)


- [建立良善的 Python 测试](https://pycoders.com/link/3569/web)
    + CHRIS NEJAME 
    + • Shared by Chris NeJame


A collection of testing maxims, tips, and gotchas, with a few pytest-specific notes. Things to do and not to do when it comes to writing automated tests.

(`是也乎:`

深切体会过, 好的测试, 必须有好的可测试代码配合.
否则, 太南了

)



- [Python 类型边缘](https://pycoders.com/link/3580/web)
    + STEVE BRAZIER

Adding more strict typing around the edges of a Python system for better error messages and design, using Pydantic and mypy. Interesting read!

- [Python 3.9 StatsProfile](https://pycoders.com/link/3582/web)
    + DANIEL OLSHANSKY


The author of the profiling API improvements coming to Python 3.9 demonstrates the feature and explains how it was added to CPython.

- [机器人/生成艺术和Python,我的天哪](https://pycoders.com/link/3563/web)
    + GEOFFREY BRADWAY

How to make cool looking plotter art with NumPy, SciPy, and Matplotlib.

(`是也乎:`

简直就是抖音课程营销必备展示小视频

)


- [PyCon US 2020 教程时间表](https://pycoders.com/link/3587/web)
    + PYCON.ORG

- [Python 3.8.2rc2 可用以测试](https://pycoders.com/link/3599/web)
    + PYTHON INSIDER





## 讨论
> Discussions



NIL



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks




- [Python 访谈 -> Brett Slatkin](https://pycoders.com/link/3574/web)
    + REAL PYTHON

Brett Slatkin is a principal software engineer at Google and the author of the Python programming book Effective Python. Join us as we discuss Brett's experience working with Python at Google, refactoring, and the challenges he faced when writing the second edition of his book.

(`是也乎:`


![Interview](http://ydlj.zoomquiet.top/ipic/2020-02-19-ScreenShot%202020-02-19%2016.55.31.jpg)

好久不见的访谈, 嗯哼?
说起来咱们自己的-> 捕蛇者说, 自从在 zhihu 被和谐后, 也再没更新?

)


- [对 Black Code Formatter 的不满意见](https://pycoders.com/link/3596/web)
    + LUMINOUSMEN.COM

"In this post, I will try to gather all my thoughts on the topic of automatic code formatting and why I personally don't like this approach."



- [用 WebSocket 上唯一管理测试执行资源](https://pycoders.com/link/3595/web)
    + CRISTIAN MEDINA

Learn about managing resources for test execution, while building an asynchronous WebSocket client-server application that tracks them using Python and Sanic.

(`是也乎:`

>  Uniquely Managing Test Execution Resources

为了分布式原子化测试事务?


)

- [重构并寻求宽恕](https://pycoders.com/link/3571/web)
    + CHRIS MAY

"Recently, I had a great interaction with one of my coworkers that I think is worth sharing, with the hope you may learn a bit about refactoring and Python."

(`是也乎:`

> Forgiveness

真的用了这词儿

)


- [Python 新近字符串格式技术指南](https://pycoders.com/link/3567/web)
    + REAL PYTHON

In the last tutorial in this series, you learned how to format string data using the string modulo operator. In this tutorial, you'll see two more items to add to your Python string formatting toolkit. You'll learn about Python's string format method and the formatted string literal, or f-string.


(`是也乎:`

又一个版本的字串格式化教程.

![Format](https://files.realpython.com/media/t.53be85450e90.png)

)


- [用Postgres和Django进行全文搜索[2017]](https://pycoders.com/link/3564/web)
    + SCOTT CZEPIEL

"In this post I will walk through the process of building decent search functionality for a small to medium sized website using Django and Postgres."


(`是也乎:`

虽然是老文章, 但是, 管用哪

)


- [用于记录链接和模糊匹配的 Python 工具](https://pycoders.com/link/3600/web)
    + CHRIS MOFFITT

Useful Python tools for linking record sets and fuzzy matching on text fields. These concepts can also be used to deduplicate data.




- [用 TensorFlow 和 Twilio 对情人节文本进行分类](https://pycoders.com/link/3601/web)
    + LIZZIE SIEGLE 
    + • Shared by Lizzie Siegle

Use TensorFlow and Machine Learning to classify Twilio texts into two categories: "loves me" and "loves me not."

- [Python Itertools 之旅](https://pycoders.com/link/3566/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Explore the itertools and more_itertools Python libraries and see how to leverage them for data processing.


(`是也乎:`

叕一则 itertools 模块的宣传稿, 只是为什么大家都没用起来?

)


- [Python 静态分析工具](https://pycoders.com/link/3605/web)
    + LUMINOUSMEN.COM

Find and fix the bugs and code smells in your Python code with the popular tools for analyzing code.


(`是也乎:`

之前针对 Py2 的代码静态分析工具, 现在都得重新嗯哼了..

![analyzing](http://ydlj.zoomquiet.top/ipic/2020-02-19-ScreenShot%202020-02-19%2017.21.12.jpg)

)


- [充分利用 Python 集合](https://pycoders.com/link/3585/web)
    + NICK THAPEN

A guide to comprehensions, generators and useful functions and classes.


- [含有 Keras/TensorFlow 和深度学习的自动编码器](https://pycoders.com/link/3604/web)
    + ADRIAN ROSEBROCK


(`是也乎:`

叕一个自动代码构造机, DL 的,,,
之前几个共同结论都是, 删除光代码就没 bug 了...

<-- 江湖传说
)


- [为什么 Python 是最佳项目启动语言](https://pycoders.com/link/3602/web)
    + GLEB PUSHKOV

(`是也乎:`

当年说 PHP/Ruby/Node.js 的文章, 一字不改, 就替换为 Python 也没什么大毛病的...

)


- [剖析 Web 堆栈](https://pycoders.com/link/3609/web)
    + LEONARDO GIORDANI

(`是也乎:`

叕一位 `莱昂纳多`

)


- [大型项目 Python->Go 迁移经验报告](https://pycoders.com/link/3607/web)
    + ERIC S. RAYMOND

(`是也乎:`

嗯哼?等等...

Eric S. Raymond 名家吐糟哪...
值得认真刷, 这位可是发明开源这个概念的牛人,
几篇 百万+ 的爆款文章, 流传至今.

)


- [Docker 和 Python 的 Kafka 简介](https://pycoders.com/link/3561/web)
    + DORON VAINRUB

- [在Python中读取Excel(xlsx)文件的指南](https://pycoders.com/link/3590/web)
    + ERIK MARSJA

(`是也乎:`

Excel 几乎是万能的, 所以想自动解读, 也是门艺术行为了

)


- [维护模块化](https://pycoders.com/link/3589/web)
    + GLYPH

(`是也乎:`

过犹不及, 哪儿都适行.

)


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code





- [pycharm-security: PyCharm插件, 在Python项目中查找安全漏洞](https://pycoders.com/link/3603/web)
    + GITHUB.COM/TONYBALONEY

(`是也乎:`

PyCharm 也有插件系统?
这真心很惊喜哪, 不过, 也晩了 VSCode 几年?

)


- [Deadsnakes PPA 为 Docker 中的 Debian 构建](https://pycoders.com/link/3581/web)
    + GITHUB.COM/JHERMANN 
    + • Shared by Jürgen Hermann

The Deadsnakes PPA project builds older and newer Python versions not found on a specific Ubuntu release. Originally based on the Debian source packages, they can still be built on Debian and not just on Ubuntu.

(`是也乎:`

大 Debian 生态, 工具主力还是 Python 哪

)


- [stdlib-property-tests: Python标准库(内置)基于属性的测试](https://pycoders.com/link/3572/web)
    + GITHUB.COM/ZAC-HD


(`是也乎:`

叕一个 Property-Based 工具, 看来 Py 3 新语言特性的味道被大家慢慢品出来了

)

- [django-guid: 向Django请求中的每个日志消息中注入](https://pycoders.com/link/3583/web)
    + GITHUB.COM/JONASKS

(`是也乎:`

Django 大生态已经有这么多扩展了,还是有创新机会的

)


- [ursina: 由Python和Panda3d驱动的游戏引擎](https://pycoders.com/link/3568/web)
    + GITHUB.COM/POKEPETTER


(`是也乎:`

叕一个游戏引擎, 疫情之下, 宅家最安全

)


- [VaultSSH: 用于使用 Vault SSH 端点签名 SSH 公钥的 CLI 工具](https://pycoders.com/link/3606/web)
    + GITHUB.COM/JMGILMAN



- [icalendar_light: iCalendar事件阅读器](https://pycoders.com/link/3612/web)
    + GITHUB.COM/IDLESIGN 
    + • Shared by pythonz

- [IRedis: 具有自动完成和语法突出显示功能的 Redis 终端客户端](https://pycoders.com/link/3579/web)
    + IREDIS.IO

(`是也乎:`

终于有了...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ PyCon Namibia 2020](https://pycoders.com/link/3611/web)
    + February 18 to February 21, 2020
    + 非洲

- [⋅ PyData Bristol Meetup](https://pycoders.com/link/3608/web)
    + February 20, 2020
    + 英国

- [⋅ Python Northwest](https://pycoders.com/link/3594/web)
    + February 20, 2020
    + 英国

- [⋅ PyLadies Dublin](https://pycoders.com/link/3591/web)
    + February 20, 2020
    + 爱尔兰

- [⋅ Open Source Festival](https://pycoders.com/link/3598/web)
    + February 20 to February 23, 2020
    + 尼日利亚

- [⋅ PyCon Belarus 2020](https://pycoders.com/link/3592/web)
    + February 21 to February 23, 2020
    + 白俄




## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
    + 5py 
    + 报名

(`(￣▽￣)`:

第五期已经开始报名:

    20.2.24 马上截止
    20.3.1  正式开课
    20.4.12 按时结束

)


- [Python开发者日,大妈线上嗯哼](https://fm.101.camp/2020/csdn-pydeveloper-dama.html)
    + fm.101.camp 蟒营™电台 
    + 勾陈各种值得探讨

(`是也乎:`

2020.2.15 CSDN 新年首次线上技术峰会,
抢鲜版, 本地单录音大妈 solo 版本播客节目 ;-)

)


- [2020新冠肺炎记忆](https://github.com/2019ncovmemory/nCovMemory)
    + github.com/2019ncovmemory/nCovMemory

报道,非虚构与个人叙述(持续更新) Memory of 2020 nCov: Media Coverage, Non-fiction Writings, and Individual Narratives (Continuously updating)

(`是也乎:`

可能是最考验 M$ 政府关系能力的项目,
这个开源新闻实录项目,
综合使用现有工具, 快速将 NCP 历史, 用普遍人的目光固化在版本历史海洋中,
但是,万一呢? 期望大家及时, 自觉分散 clone 到全球每一个硬盘中,
42年后, 我们才可能有真实的 snap 来回顾.

项目结构

    ├─archive                          文章的存档,目前提供jpg格式
    │  └─jpg
    │    ├─1.jpg
    │    └─...
    ├─data                             csv格式的文章数据
    │  └─data.csv
    ├─docs                             一个用于展示README的 Github Page
    ├─gh-page
    ├─template                         README模板
    │  └─README.handlebars
    ├─utils                            构建README的工具
    │  ├─generateReadmeFromCsv.js
    │  └─...
    └─README.md                        主文档


)


# 是也乎
> NN 3928

- 首发: [Issue 408 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-408.html)
- 修订: [issue-408.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-408.md)




