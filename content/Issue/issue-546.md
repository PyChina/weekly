Title: PyCoder 546
Slug: issue-546
Date: 2022-10-12 11:42
Tags: Weekly,Python,pycoders,ZH


> Matrix 直播


原文: [PyCoder's Weekly - Issue #546](https://pycoders.com/issues/546)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221012 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221012 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [在 Python 折腾内存分析器能带教给我们什么?](https://pycoders.com/link/9660/web)
    + REAL PYTHON 
    + PODCAST

Have you used a memory profiler to gauge the performance of your Python application? Maybe you’re using it to troubleshoot memory issues when loading a large data science project. What could running a profiler show you about a codebase you’re learning? This week on the show, Pablo Galindo Salgado returns to talk about Memray, a powerful tracing memory profiler.


(`是也乎:`


![Profiler](https://ipic.zoomquiet.top/2022-10-12-zshot%202022-10-12%2008.46.36.jpg)

)


- [Python 中 assert 有危险](https://pycoders.com/link/9670/web)
    + DHRUV PATEL 
    + • Shared by Randall Degges

Did you know Python’s assert statement can lead to runtime security vulnerabilities? While there are safe ways to use assert, there are lots of unsafe ways to use it that can lead to a variety of convoluted problems.


(`是也乎:`

和 goto 类似...反正, 语法设计不可能杜绝人为问题,
Rust 都不行

)


- [关于 asyncio.Semaphore 推理](https://pycoders.com/link/9680/web)
    + GUIDO VAN ROSSUM

Guido walks you through a single-table restaurant analogy to explain the complexity of semaphores in asyncio. Details include the TaskGroup context manager added in Python 3.11.

(`是也乎:`

![GUIDO](https://ipic.zoomquiet.top/2022-10-12-%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_3e97099a-82dd-4a15-ace2-6ef73f5d7eff.png)

老爹的官方 blog, 

[Neopythonic: About This Blog](https://neopythonic.blogspot.com/2008/10/about-this-blog.html)

08年从 Artima 迁移到 blogspot 上,
是的, 就是那个 google 收购的 blog 引擎...
当年也跟风注册过, 然后, 和谐了...

)


- [Django 安全版本已发布: 4.1.2, 4.0.8, and 3.2.16](https://pycoders.com/link/9675/web)
    + DJANGO SOFTWARE FOUNDATION





-----------------------------------------
## 探讨/吐糟
> Discussions

NIL 




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Minimax in Python: 学习如何输掉 Nim 游戏](https://pycoders.com/link/9692/web)
    + REAL PYTHON

The minimax algorithm can be used to find optimal strategies in many different games. In this tutorial, you’ll learn how to implement minimax in Python while playing the game of Nim. You’ll also learn how you can make the algorithm more efficient with alpha-beta pruning.


(`是也乎:`

![Minimax](https://ipic.zoomquiet.top/2022-10-12-zshot%202022-10-12%2008.40.24.jpg)

类似数学游戏很多都是伯来

)


- [用 Python 的 Enum 构建常量枚举](https://pycoders.com/link/9671/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to create and use enumerations of semantically related constants in Python. To do this, you’ll use the Enum class and other related tools and types from the enum module, which is available in the Python standard library.


(`是也乎:`

![Enumerations](https://ipic.zoomquiet.top/2022-10-12-zshot%202022-10-12%2008.39.52.jpg)

)



- [如何在 Django 模板中安全地将数据传递给 JavaScript](https://pycoders.com/link/9678/web)
    + ADAM JOHNSON

You want to pass your data from your Django view to JavaScript in your template and you want to do it securely. This post shows several ways of doing it without the risk of allowing malicious code injection.

- [设计安全 API](https://pycoders.com/link/9673/web)
    + PEDRO ARAVENA

This article is an introduction to REST APIs. It describes five levels of implementation, versioning, query parameters, how your design effects the server side, and how to secure your end-points.

(`是也乎:`

并给出考核级别...
简单说, 协议早已设计好, 只是看是否都用足...
HTTP 毕竟要向下兼容, 只是没想到大家没什么底线...

)


- [用 Python 构建可扩展数据流](https://pycoders.com/link/9677/web)
    + MUHAMMAD HASEEB

This step-by-step guide shows you the tools and tech you need to build a highly scalable data streaming pipeline in Python. It covers the use of Scrapy with Redis and a JSON based data flow.

- [Python 决策树: 预测糖尿病](https://pycoders.com/link/9672/web)
    + JOLEEN BOTHMA

This post shows you how to use the decision-trees algorithm with real-world data to predict cases of diabetes. Examples include the use of numpy, pandas, and sklearn.

- [关于类型提示的 12 个初学者概念](https://pycoders.com/link/9684/web)
    + AHMED BESBES

This article gives an overview of type hints: what they are and when you should use them. It starts with simple types and builds up to more complex definitions.

(`是也乎:`

反正就是好, 
毕竟程序员不应该难为程序员,
自己麻烦点, 就可以帮助编译器进行各种优化, 虽然这种优化自己看不懂,
但是, 值得的...

最好再加上生命周期/所有权/...各种深层控制声明,
`pyrs` 可能是个方向

)


- [在运行时自省 Python 对象的方法](https://pycoders.com/link/9691/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Tips and tricks for inspecting Python objects and getting information about your code at runtime. Learn about built-in object methods and the inspect module.


(`是也乎:`

反正没有什么是 print() 无法 print 的...

)

- [以 Python 开发人员视角来探索 Rust](https://pycoders.com/link/9663/web)
    + KARIM JEDDA

Karim writes about trying Rust programming as a 10+ years Python developer. He describes how to do common programming tasks and what the tooling looks like.

- [探索 SQLAlchemy: 带有示例的初学者教程](https://pycoders.com/link/9667/web)
    + ABID ALI AWAN

In this SQLAlchemy tutorial, you will learn to access and run SQL queries on all types of relational databases using Python objects.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [matrix-webcam: 来自 Matrix 内部的视频会议 ](https://pycoders.com/link/9668/web)
    + GITHUB.COM/JOSCHUCK

(`是也乎:`


![Matrix](https://ipic.zoomquiet.top/2022-10-12-zshot%202022-10-12%2009.07.44.jpg)

光 opencv-contrib-pytho 就要 150Mb, 
整体所有依赖都嗯哼好, 得2G 以上,
不过, 这样一来, 直播时可以更加从容了吧...


)


- [DocArray: 嵌套的非结构化数据](https://pycoders.com/link/9679/web)
    + JINA.AI

(`是也乎:`

叕一个完美数据结构, 就看大厂谁先支持了

![DocArray](https://ipic.zoomquiet.top/2022-10-12-zshot%202022-10-12%2009.13.18.jpg)


)


- [awesome-diagramming: 软件图表工具列表](https://pycoders.com/link/9665/web)
    + GITHUB.COM/SHUBHAMGRG04

(`是也乎:`

叕一个 awesome 列表, 刚刚开始,
graphviz 都没有...

)


- [semantic-python-overview: 语义技术索引](https://pycoders.com/link/9669/web)
    + GITHUB.COM/PYSEMTEC


- [Django 一致性模型](https://pycoders.com/link/9662/web)
    + GITHUB.COM/OCCIPITAL 
    + • Shared by Alex Liabakh




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Smart Iterator Challenge (Week 2)](https://pycoders.com/link/9674/web)
    + October 8 to October 17, 2022

- [PyCon MEA @ Global DevSlam 2022](https://pycoders.com/link/9688/web)
    + October 10 to October 14, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9681/web)
    + October 12, 2022

- [PyCon Ghana 2022](https://pycoders.com/link/9682/web)
    + October 13 to October 16, 2022

- [PyCon ZA 2022](https://pycoders.com/link/9689/web)
    + October 13 to October 15, 2022

- [PyCon JP 2022](https://pycoders.com/link/9686/web)
    + October 14 to October 17, 2022


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

- 首发: [Issue 546 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-546.html)
- 修订: [issue-546.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-546.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF546D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF546D4Q90XdDA7g):



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





