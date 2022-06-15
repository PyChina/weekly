Title: PyCoder 529
Slug: issue-529
Date: 2022-06-15 11:42
Tags: Weekly,Python,pycoders,ZH


> PyScript 飞翔在浏览器中吧 Python 君.


原文: [PyCoder's Weekly - Issue #529](https://pycoders.com/issues/529)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220615 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220615 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------





- [PyScript 初探: Web 浏览器中的 Python](https://pycoders.com/link/8891/web)
    + REAL PYTHON

In this tutorial, you’ll learn about PyScript, a new framework that allows for running Python in the web browser with few or no code modifications and excellent performance. You’ll leverage browser APIs and JavaScript libraries to build rich, highly interactive web applications with Python.


(`是也乎:`


![PyScript](https://ipic.zoomquiet.top/2022-06-15-zshot%202022-06-15%2009.46.58.jpg)

虽然是实验项目, 但是, 大家都很兴奋...


)


- [了解 Django: 调试技巧和技巧](https://pycoders.com/link/8905/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

Your Django app is up. You’ve got users. Your users are hitting bugs. How do you debug to fix the problems? This article dives deep into to how to find and squish the bugs in your Django code.


(`是也乎:`


Django 已经平台化了, 
此时的 debug 就得有新姿势了

)


- [Python 中的安全密码处理](https://pycoders.com/link/8885/web)
    + MARTIN HEINZ

Lots of applications require some form of authentication, password handling, or the use of secure credentials. What are the best practices in Python for dealing with this?


(`是也乎:`

安全口令在 Python 中管理的姿势...
![xkcd](https://imgs.xkcd.com/comics/password_strength.png)

最后给出的建议意味深长...

)


- [Python 3.10.5 Bug 发布](https://pycoders.com/link/8879/web)
    + CPYTHON DEV BLOG

- [2021 年 Python 开发人员调查结果](https://pycoders.com/link/8887/web)
    + PYTHON SOFTWARE FOUNDATION

(`是也乎:`

调查结果出来了: 到处都是 Pythoneer


)



- [EuroSciPy August 29-September 2, 瑞士巴塞尔](https://pycoders.com/link/8889/web)
    + EUROSCIPY.ORG 
    + • Shared by Darya Chyzhyk



-----------------------------------------
## 探讨/吐糟
> Discussions



- [在 Python 中引发异常或返回错误对象](https://pycoders.com/link/8890/web)
    + HACKER NEWS

Luke Plant’s article Raising exceptions or returning error objects in Python has folks weighing in.

- [MicroPython: 用于微控制器的 Python](https://pycoders.com/link/8899/web)
    + HACKER NEWS


(`是也乎:`

来了, 嵌入式系统终于出圈了

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 Python 构建 Quiz/测验 应用程序](https://pycoders.com/link/8914/web)
    + REAL PYTHON

In this step-by-step project, you’ll build a Python quiz application for the terminal. Your app will ask you multiple-choice questions that you can use to strengthen your own knowledge or challenge your friends to test theirs.


(`是也乎:`


![Quiz](https://ipic.zoomquiet.top/2022-06-15-zshot%202022-06-15%2009.21.43.jpg)

> ...quiz 这个词于 1781 年首次用于表示古怪的人;  如今，它主要用于描述对琐事或专业知识的简短测试...

嗯哼? MUD 游戏原型?
交互式测试题库...

)



- [Pandas 矢量化: 有时会因内存膨胀而变慢](https://pycoders.com/link/8913/web)
    + ITAMAR TURNER-TRAURING

When you’re processing data with Pandas, vectorized operations can speed up your code. In some cases though, they can actually make it slower, or at least no faster and memory hungry. Learn when it is helpful and when it is harmful to use vectorization.

(`是也乎:`


火焰图分析法

)


- [编写和测试 Python 函数/ 练习面试](https://pycoders.com/link/8884/web)
    + REAL PYTHON COURSE

In this interview practice session, you’ll tackle creating a function that will double every character within a string. This challenge is typical of what you might encounter in a Python job interview. You’ll explore how to add tests to your code.

(`是也乎:`


![Practice](https://ipic.zoomquiet.top/2022-06-15-zshot%202022-06-15%2009.20.03.jpg)
)


- [日期/时间和类型](https://pycoders.com/link/8874/web)
    + GLYPH LEFKOWITZ

Dates and times in code can be more complicated than they first appear. Consider how datetime and date interact and how incorrect use can result in a TypeError even though they’re considered correct by type annotations.


(`是也乎:`

主要是提供了太多对象种类?
其实对于日期时间, 从没见象 Python 这象提供一堆内建支持的语言

)


- [了解带替换和不带替换的采样](https://pycoders.com/link/8901/web)
    + MICHAEL GALARNY 
    + • Shared by Michael Galarnyk

Sampling can be done with and without replacement: when an item is sampled it may or may not be returned to the population for the next sample. Learn the differences and how it effects your statistical code.

- [交付至生产状态](https://pycoders.com/link/8888/web)
    + GERGELY OROSZ

“How you ship your code to production in a way that is fast and reliable, is a question more engineers and engineering leaders should educate themselves on.” Read on for a comparison between two extremes.

(`是也乎:`

分散开来看, 都是常识,
但是, 能在每个项目中将所有点都贯彻下来,
真. 不容易.

)


- [在 Python 中缓存连接对象](https://pycoders.com/link/8877/web)
    + REDOWAN DELOWAR

Three different mechanisms are common for having a single instance of a DB connection in your Python code: module level imports, the lru_cache decorator, or through singletons. See examples of each.

(`是也乎:`

从 dynamodb -> Redis , 
Python 运行时对象真的可以任性缓存到各种介质中...

)


- [Random Python: 让秘密和随机值变得简单](https://pycoders.com/link/8911/web)
    + JOHN LOCKWOOD

Needing a random value happens a lot when you’re coding. This article describes different ways of getting random information in Python and how to choose amongst them.

(`是也乎:`

真随机, Python 是认真的

)


- [无锁并发处理](https://pycoders.com/link/8882/web)
    + HAKI BENITA

Through the use of an example Django web application, this article illustrates a variety of concurrency issues and how to handle them without locks.





(`是也乎:`

好象很早 沈游侠 就发现, 如果整个数据桟都由  Python 完成,
就可以无锁高速, 彻底的...

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [python-syntax-errors: 版本特定的 No-Ops](https://pycoders.com/link/8917/web)
    + GITHUB.COM/JWILK

- [libgravatar: Gravatar API 的 Python 3 接口](https://pycoders.com/link/8894/web)
    + GITHUB.COM/PABLUK

(`是也乎:`


Gravatar 真的是解决了一个互联网中基础需求,
不知道在 Web 3 元宇宙中是否已经复制启用.
)


- [arsenal: 用于渗透测试的库存和启动器](https://pycoders.com/link/8880/web)
    + GITHUB.COM/ORANGE-CYBERDEFENSE

(`是也乎:`


叕一个复合指令提示/组织界面...

)

- [pikepdf: 读写 PDF/ 由 QPDF 提供支持](https://pycoders.com/link/8916/web)
    + GITHUB.COM/PIKEPDF

(`是也乎:`

叕一个 PDF 支持库,
自从发明以来, pdf 的确变成了一个事实的通用文档格式.

)


- [django-pgpubsub: 用 Postgres NOTIFY 的分布式任务](https://pycoders.com/link/8881/web)
    + GITHUB.COM/OPUS10 
    + • Shared by Paul Gilmartin

(`是也乎:`


Postgres 真.神通, 一个数据库完成所有的感觉.

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Software Craftsmanship](https://pycoders.com/link/8898/web)
    + June 15, 2022

- [PiterPy Breakfast](https://pycoders.com/link/8918/web)
    + June 15, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8919/web)
    + June 15, 2022

- [PyData Bristol Meetup](https://pycoders.com/link/8915/web)
    + June 16, 2022

- [PyLadies Dublin](https://pycoders.com/link/8875/web)
    + June 16, 2022

- [Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/8895/web)
    + June 17, 2022
    + 德国巴登-符腾堡州的非县辖城市

- [GeoPython 2022](https://pycoders.com/link/8883/web)
    + June 20 to June 23, 2022





-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅

![ACM-O](https://ipic.zoomquiet.top/2022-04-27-zshot%202022-04-27%2009.22.46.jpg)

(`是也乎:`


谈崩了, 之前通过 ACM 会员可以每年 $25 享受 O'REILLY 在线图书馆服务...现在没了

)

-----------------------------------------
# PS:

- 首发: [Issue 529 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-529.html)
- 修订: [issue-529.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-529.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF529D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF529D4Q90XdDA7g):



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





