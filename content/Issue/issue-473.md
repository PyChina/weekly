Title: Issue 473
Slug: issue-473
Date: 2021-05-19 11:42
Tags: Weekly,Python,pycoders,ZH


> SpaceX 如何控制星舰的?


原文: [PyCoder's Weekly - Issue #473](https://pycoders.com/issues/473)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210519 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210519 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [SpaceX 如何降落星舰/排序](https://pycoders.com/link/6324/web)
    + THOMAS GODDEN

While waiting for SN15 to launch, Thomas Goddard set out to pull together a 2-dimensional simulation of the Starship landing. Tying together knowledge of trajectory optimization, Thomas modeled the landing in Python with the CasADI library and used Matplotlib to generate an animation which, when played side-by-side with the footage of the landing, results in remarkable similarity to the actual landing dynamics.

(`是也乎:`

是的, JS/Py 反正以往 NASA 不用的,
SpaceX 都用上了,
关键是 多快好省,
至于现代语言/系统在太空的意外错误,
通过三主机协议选举也就解决了...

)


- [Flask 2.0中的异步](https://pycoders.com/link/6340/web)
    + PATRICK KENNEDY 
    + • Shared by Patrick Kennedy

This article looks at Flask 2.0’s new async functionality and how to leverage it in your Flask projects. You’ll learn how Flask processes requests asynchronously using a traditional WSGI server, instead of the ASGI server used by many other async web frameworks. You’ll also learn how to simulate Flask 2.0 async in Flask 1.X applications.


- [嵌入式Python/ 在BBC micro:bit上构建游戏](https://pycoders.com/link/6329/web)
    + REAL PYTHON

Learn about embedded development, an exciting area of programming that allows you to bring your code into the physical world. You’ll learn about your options for writing embedded Python code and build a basic game using the BBC micro:bit.

(`是也乎:`

![BBC](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2010.02.22.jpg)

是的, 就是那个 BBC

)



- [EuroPython 2021 议题投票已开放](https://pycoders.com/link/6341/web)
    + EUROPYTHON.EU

Planning on attending EuroPython this year? If you’re registered and have paid for a ticket, or if you’ve attended any of the past conferences, you can vote on talk submissions until May 23.

(`是也乎:`

其实, 很多都是从 US 复场过来的

)



- [所有 Pallets 项目主要版本发布](https://pycoders.com/link/6344/web)
    + PALLETSPROJECTS.COM

Flask 2.0, Werkzeug 2.0, Jinja 3.0, Click 8.0, ItsDangerous 2.0, and MarkupSafe 2.0

(`是也乎:`

全明星队...

)

- [PyCon US 2024 以及 2025 将在宾夕法尼亚州的匹兹堡举行](https://pycoders.com/link/6313/web)
    + PYCON.BLOGSPOT.COM




-----------------------------------------
## 探讨/吐糟
> Discussions


- [获取 k 个排序数组交集的 *最有效* 方法是什么?](https://pycoders.com/link/6323/web)
    + STACK OVERFLOW

For algorithm enthusiasts, this question-and-answer thread shows some interesting ways to approach a relatively simple-looking problem. The thread even got a nod from Python core developer Raymond Hettinger on Twitter.



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [The 2021 Python 语言峰会](https://pycoders.com/link/6335/web)
    + PYTHON SOFTWARE FOUNDATION

Every year the Python Software foundation hosts the Python Language Summit where a small group of core developers discusses the current state and future direction of the Python language. Check back regularly on this announcement to find links to writeups about the events from the summit, penned this year by Real Python’s Joanna Jablonski.

(`是也乎:`

老爹放卫星了...

)



- [在 2021 年为 PyPI 提供动力](https://pycoders.com/link/6319/web)
    + DUSTIN INGRAM

What does it take to power PyPI in this current day and age? Learn what technologies PyPI uses, who is involved, how much it costs, and how you can help support the package index.

(`是也乎:`

去年至少有两次不可用事故, 
而且长期无法 search ,
可见 PyPI 很成问题了...


)


- [用 Arcade 构建平台游戏并每月报道 Python 新闻](https://pycoders.com/link/6334/web)
    + REAL PYTHON 
    + podcast

Did you know the Python Software Foundation is hiring! With the recent support of three Visionary Sponsors, the PSF has been able to open positions for a developer-in-residence and a Python packaging project manager. Real Python now has a monthly Python news article. Frequent guest of the show, David Amos compiles and summarizes the biggest Python news from the past month.

(`是也乎:`

![Game](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2009.58.09.jpg)

卷轴游戏,永远的经典...

)


- [用DuckDB在 Pandas 上进行高效的SQL](https://pycoders.com/link/6320/web)
    + MARK RAASVELDT AND HANNES MÜHLEISEN 
    + • Shared by Alexander Monahan

pandas is an indispensable tool for Python data analysis. It’s also a standard for data transfer between elements of the Python data ecosystem. But sometimes you need some good ol’ SQL in your data workflow. With DuckDB, you can perform SQL queries directly against pandas data frames. DuckDB is faster than pandas in some cases and can even handle larger-than-memory data.

(`是也乎:`

无论 Pandas 将数据集操作折腾的多么 Pythonc,
对于广大财务人员而言,
还是 SQL 更加值得信赖.
)


- [Unravelling the pass Statement](https://pycoders.com/link/6312/web)
    + BRETT CANNON

When you need to indicate that a bit of code intentionally does nothing, then you need to reach for Python’s pass statement. In the latest installment of Brett’s “Syntactic Sugar” series, you’ll learn how pass works, when to use it, and why it’s a uniquely Python concept.


- [用 namedtuple 编写干净的 Pythonic 代码](https://pycoders.com/link/6316/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn what Python’s namedtuple is and how to use it in your code. You’ll also learn about the main differences between named tuples and other data structures, such as dictionaries, data classes, and typed named tuples.

(`是也乎:`

![namedtuple](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2009.51.11.jpg)

记得 Limodou 为了方便 UliEidtor 的开发,
还专门设计了一个类似的类...

)



- [使用 Python 或运算符](https://pycoders.com/link/6333/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn about how the Python or operator works and how to use it. You’ll get to know its special features and see what kind of programming problems you can solve by using or in Python.

(`是也乎:`

![or](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2009.49.27.jpg)

逻辑计算基础算子

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [telepath: 一个用于在 Python 和 JavaScript 之间交换数据的库](https://pycoders.com/link/6336/web)
    + GITHUB.COM/WAGTAIL

(`是也乎:`

嗯哼? WSAM.py 标准内置模块?

Django 专用...

)


- [spacestills:NASA电视静止画面查看器](https://pycoders.com/link/6315/web)
    + GITHUB.COM/PAMOROSO

(`是也乎:`

假装从火星直播

![NASA](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2010.47.47.jpg)

)

- [Strongtyping: 运行时键入检查的装饰器](https://pycoders.com/link/6311/web)
    + FELIX EISENMENGER

(`是也乎:`

运行时数据检查,
嗯哼, 更加常用

)

- [ward: 专注于生产力和可读性的现代Python测试框架](https://pycoders.com/link/6330/web)
    + GITHUB.COM/DARRENBURNS

(`是也乎:`

可读性 最重要了

![ward](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2010.49.53.jpg)



)


- [pymc3: 用 Aesara 进行贝叶斯建模和概率机器学习](https://pycoders.com/link/6348/web)
    + GITHUB.COM/PYMC-DEVS

(`是也乎:`

作者创建的模块,
原先只是在教学中,
现在看来可以投入生产了

![pymc3](http://ydlj.zoomquiet.top/ipic/2021-05-19-ScreenShot%202021-05-19%2010.54.57.jpg)

关键看是否有长期稳定的赞助商

)


- [duckdb: 进程内SQL OLAP数据库管理系统](https://pycoders.com/link/6310/web)   
    + GITHUB.COM/DUCKDB

(`是也乎:`

嘦看起来/走起来/听起来/叫起来 象DB ,
那丫的就一定是 DB
)


- [python-typing-koans: 在Python中学习可选静态键入的示例](https://pycoders.com/link/6347/web) 
    + GITHUB.COM/KRACEKUMAR 
    + • Shared by Kracekumar

- [djenv: 从环境变量加载Django设置](https://pycoders.com/link/6326/web)
    + GITHUB.COM/DANIELJDUFOUR

(`是也乎:`

其实, 静态编译型语言中有通用解,
可以一次性一致性的接入所有渠道的配置.

推荐 [ets-labs/python-dependency-injector: Dependency injection framework for Python](https://github.com/ets-labs/python-dependency-injector)

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6339/web)
    + April 28, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ Conf42 Python 2021](https://pycoders.com/link/6322/web)
    + May 27 to May 28, 2021

(`是也乎:`

这个大会关心的事儿比较大.
)


- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021


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
- 首发: [Issue 473 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-473.html)
- 修订: [issue-473.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-473.md)


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
>> NN 4376


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/473)






