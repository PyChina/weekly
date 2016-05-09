Title: 蠎加载 70
Slug: importpython-70
Date: 2016-05-01 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 70](http://importpython.com/newsletter/no/70/)
- 欢迎, 来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)

## 该读
~ 文章, Blog, 教程...


- [有 Python app. 的想法?](http://synd.co/1XWSCSz)
    + Sponsor

在 Azure App Service 中创建 Python app. 免费的!
选择对应语言,就可以使用各种常见框架的模板来开始:
django/flask/bottle ...



- [Python 分类排序](https://pythontips.com/2016/04/24/python-sorted-collections/)
    + core python

对于 TIOBE 排行榜的其它语言,
Python 有点不寻常,其它都有可排序的 字典/集合,
只有 Python 没有, 自称 `预置电池` 的语言,为毛?!


- [Django 模型中的最佳实践](http://steelkiwi.com/blog/best-practices-working-django-models-python/)
    + django

对于 Django 程序猿,非常实用和清晰的检查列表.

- [优化慢速 Django REST Framework](http://blog.mathandpencil.com/optimizing-slow-django-rest-framework-performance/)
    + Django Rest Framework

DRF 中有个著名的 "N+1选择问题", 这儿进行了深入的讨论,
但是,并没有什么好的的解决方案..

The Django REST Framework (DRF for short) allows Django developers to build simple yet robust standards-based REST API for their applications. Even seemingly simple, straightforward usage of the Django REST Framework and its nested serializers can kill performance of your API endpoints. At it’s root, the problem is called the “N+1 selects problem”; the database is queried once for data in a table (say, Customers), and then, one or more times per customer inside a loop to get, say, customer.country.Name. Using the Django ORM, this mistake is easy to make. Using DRF, it is hard not to make.

- [select — 高效 I/O 中的等待 — PyMOTW 3](http://feedproxy.google.com/~r/PyMOTW/~3/yOjZUL-wOJo/)
    + core python

模块选择特定平台 I/O 监察功能.
相当于 POSIX 中的 `select()`,
适用于 Windows 和 UNIX 平台.
也提供了 `poll()` , 仅 UNIX 可用.

- [54集 - Donald Stufft 论 Pip 以及 Python 包管理 ](http://podcastinit.podbean.com/e/episode-54-pip-and-the-python-package-authority-with-donald-stufft/)
    + podcast

作为 Python 程序猿,每天都在使用 pip 进行各种模块的管理.
但是从来没有详细探寻过为什么/怎么来的?!
这次请到了作者来聊聊,当初的设想...

As Python developers we have all used pip to install the different libraries and projects that we need for our work, but have you ever wondered about who works on pip and how the package archive we all know and love is maintained? In this episode we interviewed Donald Stufft who is the primary maintainer of pip and the Python Package Index about how he got involved with the projects, what kind of work is involved, and what is on the roadmap. Give it a listen and then give him a big thank you for all of his hard work!

- [django-river 状态机以及工作流库](https://github.com/javrasya/django-river/)

Main goal of developing this framework is to be able to edit any workflow item on the fly. This means, all elements in workflow like states, transitions, user authorizations(permission), group authorization are editable. To do this, all data about the workflow item is persisted into DB. Hence, they can be changed without touching the code and re-deploying your application.

- [构建实时 apps.](http://synd.co/23752Zg)
    + Sponsor

Syncano. Database. Backend. Middleware. Real-time. Support. Start for free!


- [计算几何在 Python : 从理论到应用](http://python-resources.pythonblogs.com/304_python_resources/archive/1539_computational_geometry_in_python_from_theory_to_application.html)

When people think computational geometry, in my experience, they typically think one of two things: Wow, that sounds complicated. Oh yeah, convex hull. In this post, I’d like to shed some light on computational geometry, starting with a brief overview of the subject before moving into some practical advice based on my own experiences

- [polyglot 的多分派手册 - 第三部分](http://eli.thegreenplace.net/2016/a-polyglots-guide-to-multiple-dispatch-part-3/)
    + core python

有关多分派系列第三部分.
第一部分介绍了概念以及 C++ 的实现;
第二部分在Python 中完成了部分特性;
这一节, 挖掘其根据 Common Lisp 中的实现,
来探讨 Python 在 OOP 框架中可以进行的.


- [Your Django Story: Meet Margaret Myrick](http://blog.djangogirls.org/post/143378817643)
    + interview

Margaret Myrick is a program manager at Indeed, and a musician on the side. She has lived in Texas since she was a child.

- [YodaBot - 开源消息机械人将文本转换为 yoda 演讲](https://github.com/architv/yodabot)

Master Yoda, I am. Left Degobah I have, and come to messenger as a bot. Message me. Reply in my own style, I would. Curator Note - Pretty funny check it out.

(`是也乎:`

特川普之后, 又一个语言风格类工具.
)

- [Python 提示符工具包](https://github.com/jonathanslenders/python-prompt-toolkit)
    + core python

prompt_toolkit 专注用 Python 构建强力 CLI 工具界面.


(`是也乎:`

![ptpython](https://github.com/jonathanslenders/python-prompt-toolkit/raw/master/docs/images/ptpython.png)

嗯哼, 这样一来, GUI 越来越没有什么必要了...

)

- [雇主拒绝遵守 Python  - Reddit Discussion](http://www.reddit.com/r/Python/comments/4gpa83/employer_refuses_to_allow_python/)
    + core python

Hey guys, Recently, I informed my manager that I was willing to go above-and-beyond and help improve some of our team operations by writing a handful of Python scripts. He is a stickler for following the rules, so he ordered me to ask permission to install Python on my development machine (I wasn't intending on asking permission). My request has been refused. Despite providing evidence from the Python Foundation on their open licensing (especially for my purposes, which is just local machine -- not production), they are still refusing on account that Python is type of GPL and it is interpretative. Have you guys run into something like this before? It seems ridiculous to me.

(`是也乎:`

嗯哼, 可怜的 GPL.
)

- [James Powell - `from __past__ import print_statement`: 达达主义者拒绝 Python 2 vs 3](https://www.youtube.com/watch?v=anP1TU1vHbs)
    + video

If the title doesn't make any sense, then there's no hope that the description will be any better. This talk will be a strange dive into interpreter hacks, the pointlessness of the Python 2 vs 3 debate, and the twisted artistic drive that pushes the speaker to come up with these perversions of the Python language. Prepared to be simultaneously repulsed, intrigued, and completely bored.

有趣,但是完全无聊...

- [用 Python 分析 Chrome 的浏览历史](https://geekswipe.net/technology/computing/analyze-chromes-browsing-history-with-python/)

从 SQLite 中扒出数据结构,
只需 Python 写个脚本,连接数据库,提取对应数据,
一切就随你折腾了.

- [在线用 Python 收集情报](https://register.automatingosint.com/importpython/)
    + Sponsor

Learn how to write code to automatically extract and analyze data from the web and social media. Join students from around the world from law enforcement, journalism, information security and more.



## 新书
~ New Books

- [掌握 Python 取证](http://importpython.com/books/524/mastering-python-forensics/)

Learn to perform forensic analysis and investigations with the help of Python, and gain an advanced understanding of the various Python libraries and frameworks. Analyze Python scripts to extract metadata and investigate forensic artifacts. The writers, Dr. Michael Spreitzenbarth and Dr. Johann Uhrmann, have used their experience to craft this hands-on guide to using Python for forensic analysis and investigations


## 活动
~ Upcoming Conference / User Group Meet

- [PyData London 2016](http://pydata.org/london2016/)
- [PyCon Israel 2016](http://il.pycon.org/)
- [Pycon Sweden](http://www.pycon.se/)




## 项目
~ 包/模块/库/片段...

- [gym](https://github.com/openai/gym)
    - 1353 Stars, 162 Fork

开发和比较算法的工具.

(`是也乎:`

来自 [https://gym.openai.com/](https://gym.openai.com/)

betacat 的始源之地...
)

- [rllab](https://github.com/rllab/rllab)
    - 86 Stars, 12 Fork

rllab 开发和评估强化学习算法的框架

- [otek](https://github.com/jaywunder/otek)
    - 52 Stars, 2 Fork

所有人都应该体验的项目创建工具.

- [detux](https://github.com/detuxsandbox/detux)
    - 51 Stars, 9 Fork

多平台 Linux 沙箱

- [LowRankPropagation](https://github.com/mharradon/LowRankPropagation)
    - 26 Stars, 4 Fork

Propagation Technique for Solving Low Rank Matrix Completion

- [LearnProgrammingBot](https://github.com/Aurora0001/LearnProgrammingBot)
    - 16 Stars, 1 Fork

Bot for /r/learnprogramming using supervised learning

- [doorman](https://github.com/mwielgoszewski/doorman)
    - 15 Stars, 1 Fork

an osquery fleet manager

- [ballade](https://github.com/holyshawn/ballade)
    - 14 Stars, 1 Fork

轻量级, 基于 tornado 的代理,
以及上游代理切换管理工具.
使用 SwitchyOmega 规则.

- [falcon-api](https://github.com/tomchristie/falcon-api)
    - 11 Stars, 0 Fork

Falcon 的 web API 框架.

- [flatdoc](https://github.com/miguelgrinberg/flatdoc)
    - 5 Stars, 0 Fork

Flat 文档生成器

- [elastic-bill](https://github.com/cloudbiller/elastic-bill)
    - 5 Stars, 1 Fork

Elastic bill 
复合云平台计费管理工具.
is a multi cloud platform billing management tool.

- [slactorbot](https://github.com/dataloop/slactorbot)
    - 4 Stars, 0 Fork

A Slack bot with hot patch!


## DAMA 无责任推荐

- [pyenv-mirror](https://github.com/huntzhan/pyenv-mirror)
    + 7 Stars, 0 Fork

快速制作 pyenv 环境镜像的工具

(`是也乎:`

国人作品, 在 CPyUG 列表反馈下, 24小时以内,兼容了 Python 2 ;-)

嗯哼,当然的,没有 M$ 的支持.
)


### 工作

....


# 是也乎

- 160501 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160501 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


