Title: PyCoder 565
Slug: issue-565
Date: 2023-02-22 11:42
Tags: Weekly,Python,pycoders,ZH


> 为什么类型提示很烂...


原文: [PyCoder's Weekly - Issue #565](https://pycoders.com/issues/565)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------


- [如何刷新 Python 打印函数的输出](https://pycoders.com/link/10363/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to flush the output of Python’s print function. You’ll explore output stream buffering in Python using code examples and learn that output streams are block-buffered by default, and that print() with its default arguments executes line-buffered when interactive.


(`是也乎:`

![Flush](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.25.02.jpg)

制作进度条的关键技巧...

)

- [潜伏在异步代码中的 Heisenbug](https://pycoders.com/link/10368/web)
    + WILL MCGUGAN

When using the create_task() function in asyncio it is very important to maintain a reference to the created tasks. Although this requirement is documented, it is easy to forget and can have some very hard to understand consequences.






- [SQLAlchemy 2.0 有什么新功能?](https://pycoders.com/link/10376/web)
    + MIGUEL GRINBERG

SQLAlchemy 2.0 was launched in January. This article reviews the latest changes, whether it is worth the upgrade, and how to go about it.


(`是也乎:`

![SQLAlchemy](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.23.56.jpg)

书都准备好了...

)

- [PyCon US 2023 (犹他州盐湖城)时间表可用](https://pycoders.com/link/10367/web)
    + PYCON.BLOGSPOT.COM

- [Django Security 已发布: 4.1.7, 4.0.10, and 3.2.18](https://pycoders.com/link/10375/web)
    + DJANGO SOFTWARE FOUNDATION








-----------------------------------------
## 探讨/吐糟
> Discussions


- [为什么类型提示很烂!](https://pycoders.com/link/10379/web)
    + REDDIT


(`是也乎:`

可以说, 这是步向伟大的阵痛嘛?
作者列出了9种经典企图, 都失败了...

PS: 反正俺没开始用...

)




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [对 PyPI 用户的最新攻击, 骗子越来越厉害](https://pycoders.com/link/10353/web)
    + DAN GOODIN

Over 400 new malicious packages have been uploaded to PyPI that use a malicious JavaScript extension to monitor infected machines for crypto-currency interactions with the intent of stealing credentials. Packages are named based on typos of many of the most popular PyPI downloads.

(`是也乎:`

毕竟 PyPI 的用户比其它应用现场要多的多,
而且多数是自动部署,没有人关注...简直就是天然的后门池...

)


- [PySport 开源](https://pycoders.com/link/10371/web)
    + PYSPORT.ORG

This site is a collection of open source Python and R tools for sports analytics, including scrapers and API wrappers for a variety for sites, data plotting, and analysis. It is maintained by [PySport](https://pycoders.com/link/10385/web).


(`是也乎:`

运动数据学?
好象几部相关电影上映后, 对体育竞技进行大数据监理就变成了热门职业...

)



- [Python 中的 getter 和 setter](https://pycoders.com/link/10378/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn what getter and setter methods are, how Python properties are preferred over getters and setters when dealing with attribute access and mutation, and when to use getter and setter methods instead of properties in Python.


(`是也乎:`

![Setters](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.16.32.jpg)

)

- [Python Basics: 使用类构建系统](https://pycoders.com/link/10356/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to work with classes to build complex systems in Python. By composing classes, inheriting from other classes, and overriding class behavior, you’ll harness the power of object-oriented programming (OOP).


(`是也乎:`

![COURSE](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.15.29.jpg)

当然也可以不用...

)


- [基本 Django 部署指南](https://pycoders.com/link/10383/web)
    + SAAS PEGASUS

Going from “it works on my machine” to deploying to the public can be a daunting task. This guide details the choices between VPS and PaaS systems, how to choose, what the options are, and what you need to know to get your Django code live.

- [图像大小调整背后的危险](https://pycoders.com/link/10365/web)
    + ZURU.TECH

When training an ML model on image data you likely want smaller, consistently sized images. That means image processing in your pipeline, but the expectation that image resizing is the same across libraries can cause unforeseen problems.

- [你应该写一个没有 @dataclass 的类吗?](https://pycoders.com/link/10361/web)
    + GLYPH LEFKOWITZ

This article makes the argument that you should always use @dataclass for building classes in Python. Read on to understand why, and maybe respond to Glyph’s call-to-action to tell him if you think he’s wrong.

- [在 Python 中缓存大量方法](https://pycoders.com/link/10372/web)
    + ADRIAN

This article goes deep on functools.lru_cache() including all the arguments against using it, and how to argue with the arguments. Learn how to cache the results of your functions with a single line of code.

- [Google OSS 项目 Python 风格指南](https://pycoders.com/link/10364/web)
    + GOOGLE

This is the style guide for any Google-originated open-source projects and a conversation on [Hacker News](https://pycoders.com/link/10377/web) about its content.

(`是也乎:`

![Style](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.06.44.jpg)

暂时还没有 Rust 风格指南,
不过, Python 这版比当年推出时, 复杂了3倍...
怪不得 Guido 老爹当年都要学习几周才能通过自动化风格检查器。。。


)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [ApiLogicServer: 可定制的数据库 Web 应用程序项目](https://pycoders.com/link/10381/web)
    + GITHUB.COM/VALHUBER

(`是也乎:`


当年 WebLogic 的重制?
根据数据库自动生成管理应用界面/核心逻辑代码/JSON 接口

即: BaaS ~ 数据库即软件?


)


- [Pathfinding-Visualizer: 用 Pygame 可视化寻路](https://pycoders.com/link/10366/web)
    + GITHUB.COM/TAUSEEF-HILAL

(`是也乎:`

嗯哼?

![Pathfinding](https://ipic.zoomquiet.top/2023-02-22-zshot%202023-02-22%2009.01.55.jpg)

最佳路径分析器,
这是训练 AI 的关键辅助工具哪...

)


- [django-prose: Django 的精彩富文本编辑](https://pycoders.com/link/10354/web)
    + GITHUB.COM/WITHLOGICCO


(`是也乎:`

md 之后, 见富文本编辑框就想躲...
可事实是, 世界上多数人还是愿意见到象 Word 的东西的...

)

- [CausalPy: 准实验环境中的因果推理](https://pycoders.com/link/10362/web)
    + GITHUB.COM/PYMC-LABS




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyCon Namibia 2023](https://pycoders.com/link/10384/web)
    + February 21 to February 24, 2023

- [PyKla Monthly Meetup](https://pycoders.com/link/10370/web)
    + February 22, 2023

- [Heidelberg Python Meetup](https://pycoders.com/link/10374/web)
    + February 22, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10380/web)
    + February 22, 2023

- [SPb Python Drinkup](https://pycoders.com/link/10373/web)
    + February 23, 2023

- [PyLadies Amsterdam + MLOps.Community Meetup](https://pycoders.com/link/10355/web)
    + February 23, 2023

- [PyCon PH 2023](https://pycoders.com/link/10358/web)
    + February 25 to February 27, 2023

- [PyDelhi User Group Meetup](https://pycoders.com/link/10382/web)
    + February 25, 2023



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 565 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-565.html)
- 修订: [issue-565.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-565.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

## PPS:
> 不觉中蟒周刊快译已经到了第11个年头

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

-------------

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF565D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF565D4Q90XdDA7g):



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



