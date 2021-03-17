Title: Issue 464
Slug: issue-464
Date: 2021-03-17 11:42
Tags: Weekly,Python,pycoders,ZH


> 模式匹配在 Pythonic


原文: [PyCoder's Weekly - Issue #464](https://pycoders.com/issues/464)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210317 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210317 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Pythonic 的模式匹配教程](https://pycoders.com/link/5971/web)
    + RODRIGO GIRÃO SERRÃO 
    + • Shared by Rodrigo Girão Serrão

Structural pattern matching is coming in Python 3.10. This article explores how to use it to write Pythonic code by searching for some of the best use cases for the match statement. Keep in mind that match is still in alpha, so, while unlikely, some things may still change before the final version of 3.10 is released.


(`是也乎:`

![Pattern](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.19.02.jpg)

在 Erlang 用老的形式,
终于进入 Python,
不过, 也只是刚刚开始,
远没浸入内核,
只能当成语法糖先.


)


- [PyQt6 vs PySide6: 两种 Python Qt 库间有什么区别?](https://pycoders.com/link/5970/web)
    + MARTIN FITZPATRICK

There is a new version of Qt (version 6) and with it new versions of PyQt and PySide — now named PyQt6 & PySide6 respectively. Take a look at the latest versions of the libraries to identify the differences between them and find solutions for writing portable code.

(`是也乎:`


表兄弟有什么不同?

)



- [用 Python/PyQt 和 SQLite 建立通讯录](https://pycoders.com/link/5960/web)
    + REAL PYTHON

In this step-by-step project, you’ll build a minimal contact book application using Python, with PyQt to build the application’s GUI and SQLite to handle the database.

(`是也乎:`


![Contact](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.14.04.jpg)


真正上手项目,
可以立即让你反感 GUI 编程...


)


- [用 Flask/htmx 和 Tailwind CSS 进行快速原型制作](https://pycoders.com/link/5945/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

Learn how to usee htmx and Tailwind CSS with Flask to quickly build interactive front-ends.

- [Mu 版本 1.1.0-Beta.2 已发布](https://pycoders.com/link/5969/web)
    + MADEWITH.MU

(`是也乎:`


![Mu](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.12.36.jpg)


最萌 IDE 发布新版了

)


-----------------------------------------
## 探讨/吐糟
> Discussions

- [为毛用 Python 生成的 tar.xz 文件比 MacOS Tar 小15倍?](https://pycoders.com/link/5958/web)
    + HACKER NEWS

(`是也乎:`

等等? tar 只是打包又不压缩哪...

)

- [如何快速获得4800万行的巨大CSV文件的最后一行?](https://pycoders.com/link/5966/web)
    + STACK OVERFLOW


(`是也乎:`

tail ?

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [如何用 Modin 加快 Pandas](https://pycoders.com/link/5963/web)
    + MICHAEL GALARNYK 
    + • Shared by Michael Galarnyk


The pandas library provides easy-to-use data structures like pandas DataFrames as well as tools for data analysis. One issue with pandas is that it can be slow with large amounts of data. It wasn’t designed for analyzing 100 GB or 1 TB datasets. Fortunately, there is the Modin library which has benefits like the ability to scale your pandas workflows by changing one line of code.


(`是也乎:`

其实追加内存是最快的加速

)


- [Navigating 用于部署 Python 应用程序的选项](https://pycoders.com/link/5965/web)
    + REAL PYTHON 
    + podcast

What goes into the decision of how to host your Python code or application in the cloud? Which technology stack is the right size for your project? This week on the show, we have Calvin Hendryx-Parker. Calvin talks about cloud hosting options, infrastructure choices, and deployment tools.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.09.17.jpg)
)


- [Interfaces 和 Protocols](https://pycoders.com/link/5948/web)
    + GLYPH LEFKOWITZ


Now that Python developers have Mypy and Python’s built-in Protocol, is zope.interface a thing of the past? Can you replace every zope.interface with a Protocol? See how these two approaches to abstract types compare, and when it might make sense to stick with zope.interface.


(`是也乎:`

界面和协议...嗯哼, 反转概念是习惯性动作了...

`zope.interface` 一直没过时,
可想当年 Zope 创造了多少好东西?
毕竟是 老爹亲自嗯哼的哈...
)


- [Python 三十岁: 对谈帮助 编程语言步入正轨的人](https://pycoders.com/link/5943/web)
    + MAYANK SHARMA

Pablo Galindo is a physicist, Python core-dev, and member of the Python steering council. He’s also the release manager for Python 3.10 and 3.11. Learn how he got involved with Python and read about his thoughts on the role of the steering council and Python’s future.


(`是也乎:`


![Galindo](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.11.01.jpg)
)



- [Python 布尔值: 利用真理的价值](https://pycoders.com/link/5964/web)
    + REAL PYTHON 
    + course

Learn about the built-in Python Boolean data type, which is used to represent the truth value of an expression. You’ll see how to use Booleans to compare values, check for identity and membership, and control the flow of your programs with conditionals.


(`是也乎:`

![Booleans](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.09.59.jpg)

中学知识..

等等, 真理的力量? 这个广告辞很力的.
)


- [性能比较: Python，Go，C ++，C，AWK，Forth 和 Rust 的单词计数](https://pycoders.com/link/5946/web)
    + BEN HOYT

This article is less of a “my language is better than your” rant and more of an exploration into what idiomatic vs. optimized code looks like in various languages and where surprising bottlenecks lurk.


(`是也乎:`


每年都有的对比,
不过, 这次有 Forth 很前沿哪...
)


- [介绍 Beanie: 异步 MongoDB ODM](https://pycoders.com/link/5968/web)
    + ROMAN

Beanie is a new asynchronous Python ODM (Object Document Mappter) for MongoDB based on Motor and Pydantic. Learn how Beanie’s data model works and see it in action in a minimal web application.

(`是也乎:`


```python

# Actual endpoint
@notes_router.get("/notes/{note_id}", response_model=Note)
async def get_note_by_id(
        # Helper usage with Depends annotation
        note: Note = Depends(get_note)
):
    return note


```

嗯哼, 这没什么变化哪...


)


- [Python 社区专访: Ewa Jodlowska](https://pycoders.com/link/5947/web)
    + REAL PYTHON

Learn how Ewa Jodlowska, the executive director of the Python Software Foundation (PSF), started her tech journey and how COVID-19 affected the PSF and plans for PyCon US 2021.

(`是也乎:`

![REAL](http://ydlj.zoomquiet.top/ipic/2021-03-17-ScreenShot%202021-03-17%2010.03.22.jpg)

)

-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [lucid-sonic-dreams: 将 GAN 生成的视觉效果同步到音乐](https://pycoders.com/link/5956/web)
    + GITHUB.COM/MIKAELALAFRIZ

- [python-fpe: Python 中的格式保留加密实现](https://pycoders.com/link/5967/web)
    + GITHUB.COM/MYSTO

- [Hyperactive: 超参数优化和数据收集工具箱](https://pycoders.com/link/5959/web)
    + GITHUB.COM/SIMONBLANKE

(`是也乎:`

超参 是调参日常中最耗时间的一坨

)

- [playback: 在生产中记录您的服务操作并在本地重播它们](https://pycoders.com/link/5941/web)
    + GITHUB.COM/OPTIBUS

(`是也乎:`

一般 deploy 工具都是反过来的哪...

)


- [beanie: 用于 MongoDB 的 Micro ODM](https://pycoders.com/link/5954/web)
    + GITHUB.COM/ROMAN-RIGHT

(`是也乎:`

ORM 之后的 ODM  ?

MongoDB 居然活过来了?

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5951/web)
    + March 10, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ An Introduction to Delivering Technical Presentations With Confidence](https://pycoders.com/link/5942/web)
    + March 25, 2021

- [⋅ PyCon Cameroon 2021](https://pycoders.com/link/5937/web)
    + March 18 to March 21, 2021
    + 喀麦隆
    + 非洲

(`是也乎:`

其实, 非洲有过发达国家的...
)


- [⋅ Python Web Conference 2021 (Virtual)](https://pycoders.com/link/5761/web)
    + March 22 – 26, 2021


- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)


- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

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

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:
- 首发: [Issue 464 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-464.html)
- 修订: [issue-464.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-464.md)


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
>> NN 4320


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/464)






