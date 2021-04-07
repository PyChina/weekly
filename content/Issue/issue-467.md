Title: Issue 467
Slug: issue-467
Date: 2021-04-07 11:42
Tags: Weekly,Python,pycoders,ZH


>  Django 3.2 发布ed


原文: [PyCoder's Weekly - Issue #467](https://pycoders.com/issues/467)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210407 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210407 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [如何用 Python 脚本打败柏林租赁市场](https://pycoders.com/link/6087/web)
    + GIAN SEGATO

Learn how one Python developer used a Python script to analyze the housing market in Berlin and predict when a property would be sold or when the price would be decreased. While the article doesn’t include a lot of technical details, it’s a great case study of how Python, its rich ecosystem, and a little creativity can turn solving a banal problem — like searching for a new house in a crowded market — into something fun and intellectually rewarding!


(`是也乎:`

15年, 就有程序猿通过 Python 脚本自动对比给出北京4环外最性价比商品房...

)



- [Python vs Java: 面向对象编程](https://pycoders.com/link/6059/web)
    + REAL PYTHON 
    + course

You may have heard that “everything is an object in Python.” But what does that mean for doing object oriented programming? If you’re coming to Python with a Java background, you’ll want to check out this course to learn how to reinterpret your understanding of Java objects to Python, and use objects in a Pythonic way.

(`是也乎:`

> 你全家才 OOP 呢.


Pythonic 一向是多范式嗯哼.

)


- [咩是 Werkzeug?](https://pycoders.com/link/6083/web)
    + PATRICK KENNEDY 
    + • Shared by Patrick Kennedy

Have you ever noticed that when you install Flask a dependency called Werkzeug is also installed? Werkzeug provides a set of utilities for building a WSGI interface in Python, which is an important part of any web application. This article will take you on a deep dive of Werkzeug and show you exactly how it works so you can have a deeper understanding of Flask applications.


(`是也乎:`

类似 Werkzeug 这种老而弥坚的项目,
还有 ZODB ~ 简直是宝藏.

)



- [Python 3.9.4 Hotfix 已经可用](https://pycoders.com/link/6071/web)
    + CPYTHON DEV BLOG

Python 3.9.3 has been recalled and a new hotfix released. All users are encouraged to upgrade. See the announcement for more information.

- [Django 3.2 发布](https://pycoders.com/link/6075/web)
    + DJANGO SOFTWARE FOUNDATION

The next version in the Django 3 series is now available and has been designated a long-term support (LTS) release.

- [Python 3.10.0a7 已经可用](https://pycoders.com/link/6069/web)
    + PYTHON.ORG

This is the last planned alpha release of Python 3.10.0! Next stop: The first beta, and a feature freeze… 🥶

- [CircuitPython 6.2.0 发布](https://pycoders.com/link/6060/web)
    + ADAFRUIT.COM

- [TLDR 通讯: 针对技术人员的字节大小新闻](https://pycoders.com/link/6091/web)
    + TLDRNEWSLETTER.COM

TLDR is a daily, curated newsletter with links and TLDRs of the most interesting stories in tech, science, and programming.

(`是也乎:`


> TL;DR

忒长嫑读

)





-----------------------------------------
## 探讨/吐糟
> Discussions

None




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [Python News: 2021年3月以来有什么新变化?](https://pycoders.com/link/6065/web)
    + REAL PYTHON

March 2021 was full of exciting Python news! Quickly get up to speed on what’s been happening in the world of Python in the past month. You’ll see everything from structural pattern matching to the 2020 Python Developers Survey.


(`是也乎:`


![News](http://ydlj.zoomquiet.top/ipic/2021-04-07-ScreenShot%202021-04-07%2010.15.25.jpg)


![Dj](http://ydlj.zoomquiet.top/ipic/2021-04-07-ScreenShot%202021-04-07%2010.16.28.jpg)

Django 3.2 新特性...

)


- [在内存不耗尽的情况下将 SQL 数据加载到 Pandas 中](https://pycoders.com/link/6088/web)
    + ITAMAR TURNER-TRAURING


If you need to load a bunch of SQL query results into a Pandas DataFrame, then you might run into a problem if there are enough rows in the SQL query’s results: it won’t fit in RAM. Panda’s read_sql() function has a batching option, but it loads all of the data into memory, too. So, how do you handle larger-than-memory queries with Pandas? This article will show you how!


(`是也乎:`


Pandas 在吞噬世界...

)



- [怪海象](https://pycoders.com/link/6076/web)
    + ARPIT BHAYANI

Python 3.8 introduced the world to the “walrus” operator, which is a colloquial term for the := operator used in the new assignment expressions. The expression a := 2 does two things: it assigns the value 2 to the name a and then returns the value 2. There’s something a little weird with assignment expressions, though. Try to execute a := 2 in a REPL and you’ll get a SyntaxError. But wrap the expression in parentheses (a := 2) and everything works like a charm. What? Why?

- [为 Python 项目编写 Makefile](https://pycoders.com/link/6063/web)
    + BASTIAN VENTHUR

Makefiles provide an entry point for project contributors to build, test, and deploy projects with simplified commands. Often, Makefiles in Python projects are written so that they expect a virtual environment to be activated before invoking any of the make targets. Read this article to see one way of getting around this, then check out this discussion for even more Makefile ideas.


(`是也乎:`


`沈游侠`曰过:

    每个程序猿
    一生都将拥有自己的
    Makefile


make 这个古老的工具,
其实早已终极解决程序猿日常核心问题了.

> 人间正道是 Make

)



- [日期时间更改在 Python 4.0](https://pycoders.com/link/6066/web)
    + TOMASZ WESOŁOWSKI

Have you heard about the newest backward-incompatible change planned for Python 4? Well, if you haven’t, you’ll want to get the inside scoop by reading what the core development team has planned for the datetime module. (And, as a side note, you might want to check the publication date after you’ve read the article and studied the PEP.)


(`是也乎:`

那什么, 将 Arrows 之类优秀时间处置模块内建进来就足够了,
有多少年没吸收任何第三方模块了?

)


- [用 %autoreload 加速 IPython 和 Jupyter](https://pycoders.com/link/6090/web)
    + MATT WRIGHT

One of the problems with working with a shell or notebook is that you have to restart the kernel before any changes made to an imported module or package are recognized. Thanks to IPython’s %autoreload magic, though, you don’t have to let kernel restarts slow down your development.


(`是也乎:`

其实吧,
最简单粗暴有效的就是追加内存条儿.

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [evalml: 用 Python 编写的 AutoML 库](https://pycoders.com/link/6080/web)
    + GITHUB.COM/ALTERYX

(`是也乎:`

AutoML ~ 嗯嗯嗯浪漫名字...

)


- [japronto: Screaming-Fast Python 3.5+ HTTP Toolkit](https://pycoders.com/link/6070/web)
    + GITHUB.COM/SQUEAKY-PL

- [result:类似 Rust 结果类型给 Python 3](https://pycoders.com/link/6073/web)
    + GITHUB.COM/DBRGN

- [Lunatic Python: LUA 在 Python and Vice Versa](https://pycoders.com/link/6084/web)
    + LABIX.ORG

- [server-text: 通过 短信 运行服务器命令](https://pycoders.com/link/6085/web)
    + GITHUB.COM/MTDEVSS


(`是也乎:`


基于 Flask;

![SMS](http://ydlj.zoomquiet.top/ipic/2021-04-07-ScreenShot%202021-04-07%2009.57.00.jpg)

以及各种短信网关,
当然, 没有中国的...

[Welcome to FreeCarrierLookup.com](https://www.freecarrierlookup.com/)

可以探索是否有兼容大陆的...

这简直就是电影桥段...


)





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6072/web)
    + March 31, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ Python for ML and AI Global Summit ‘21](https://pycoders.com/link/6021/web)
    + April 8 – 10, 2021



- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)



- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021



- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



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
- 首发: [Issue 467 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-467.html)
- 修订: [issue-467.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-467.md)


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
>> NN 4341


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/467)






