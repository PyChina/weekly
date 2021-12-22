Title: PyCoder 504
Slug: issue-504
Date: 2021-12-22 11:42
Tags: Weekly,Python,pycoders,ZH


> 有 GC 的 LISP/436 字节


原文: [PyCoder's Weekly - Issue #504](https://pycoders.com/issues/504)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [引发和处理 Python 异常](https://pycoders.com/link/7695/web)
    + REAL PYTHON 
    + COURSE

In this course, you’ll learn what an exception is and how it differs from a syntax error. You’ll learn about raising exceptions, making assertions, and catching exceptions to change the control flow of your program using the try, except, else, and finally keywords.


(`是也乎:`


![Raising](https://ipic.zoomquiet.top/2021-12-22-zshot%202021-12-22%2010.11.38.jpg)

)



- [带有 GC 的 LISP，436 字节](https://pycoders.com/link/7682/web)
    + JUSTINE TUNNEY

This one isn’t about Python specifically, but worth a read because it’s so mindblowingly cool: A LISP interpreter that’s tiny enough to fit in a 512-byte master boot record.

(`是也乎:`


![GC](https://ipic.zoomquiet.top/2021-12-22-zshot%202021-12-22%2010.12.33.jpg)

淦...是的, 这世界总是会被 LISP 重写一下..


)

- [用 Poetry 嗯哼依赖管理](https://pycoders.com/link/7688/web)
    + REAL PYTHON

Learn how Poetry will help you start new projects, maintain existing ones, and master dependency management.


(`是也乎:`


![Poetry](https://ipic.zoomquiet.top/2021-12-22-zshot%202021-12-22%2010.08.27.jpg)

叕一则硬广...

)


- [2022 年 Python 指导委员会选举结果](https://pycoders.com/link/7672/web)
    + PYTHON.ORG






-----------------------------------------
## 探讨/吐糟
> Discussions



- [py4jshell: 模拟 Log4j 远程代码执行](https://pycoders.com/link/7673/web)
    + REDDIT

Simulating the Log4j Remote Code Execution (RCE) vulnerability in a Flask web server using Python’s logging library with custom formatter that simulates lookup substitution by executing remote exploit code. (This is not a vulnerability in Python’s logging library. It’s a simulation of the Log4j vulnerability meant as a teaching tool.)


(`是也乎:`

不是, 模拟这儿有什么用?

)


- [函数和局部变量可以同名吗?](https://pycoders.com/link/7677/web)
    + STACK OVERFLOW

(`是也乎:`

不是, 为什么哪...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [A Python 巡游: 网络安全/自动化 AWS, and TDD](https://pycoders.com/link/7687/web)
    + REAL PYTHON 
    + PODCAST

The Python community continually grows, with many users coming from different languages and backgrounds. This week on the show, developer Hugh Tipping talking about his Python journey. Hugh is also a member of the Real Python community.


(`是也乎:`

![Cyber](https://ipic.zoomquiet.top/2021-12-22-zshot%202021-12-22%2010.05.17.jpg)

)


- [作为专业软件工程师/我在一周内 Google 搜索的所有内容](https://pycoders.com/link/7696/web)
    + SOPHIE KOONIN

“In an attempt to dispel the idea that if you have to google stuff you’re not a proper engineer, this is a list of nearly everything I googled in a week at work, where I’m a software engineer with several years’ experience.”

(`是也乎:`

扎心了...老铁

)

- [用 Ipycanvas 和 Box2D 的 Jupyter 游戏案例](https://pycoders.com/link/7700/web)
    + THORSTEN BEIER

“While Jupyter is widely used as a scientific and educational tool, Jupyter is seldom used as a platform for game development. In this blog post, we show how Jupyter can be used to develop tiny games based on Box2D.”

(`是也乎:`

物理引擎才是大头

)


- [用 Ergast API 和 Seaborn 在 Python 中可视化 F1 结果](https://pycoders.com/link/7678/web)
    + JASPER 
    + • Shared by Python Bytes FM

“For those wanting to get into Formula 1 data analysis, the Ergast API is a very good starting point. It provides you with clean, easily accessible data that can relatively easily be processed.”

- [用 Python 编写 Minecraft 服务器脚本](https://pycoders.com/link/7691/web)
    + GRAHAM KING

“Minecraft has an API. If you run your own server you can program it from Python. Here are notes from how I set it up. It’s a lot of fun to make things happen in Minecraft with Python.”

(`是也乎:`

有接口的地方就有 Py 包装

)



- [Wikipedia 作为数据来源: 驯服不规则](https://pycoders.com/link/7681/web)
    + VICTOR SHEPELEV

On challenges of designing the “query language” for a human-readable encyclopedia.

(`是也乎:`

嘦公开接口, 并稳定支持, 
无论哪个网站都是数据源,
这原本就是 WWW 设计目标, 只是被后人玩儿坏了...

)


- [拓展 Pandas](https://pycoders.com/link/7693/web)
    + BRYAN P WOOD 
    + • Shared by Bryan P Wood

An introduction to extension mechanisms in the Pandas library.

- [在 Python 中使用 JavaScript 风格的异步 Promises](https://pycoders.com/link/7683/web)
    + MIGUEL GRINBERG

(`是也乎:`

不是, 原本自己有等效形式的哪...

)


- [从头开始在 Python 中实现 RSA](https://pycoders.com/link/7670/web)
    + CODEROASIS.COM

(`是也乎:`

手造纯 Python 的 RAS 加密

)


- [修复流行 Python 库中的内存泄漏](https://pycoders.com/link/7686/web)
    + PAUL BROWN

(`是也乎:`

这可是大工程...

)


- [David Beazley’s dataklasses 来注释说明](https://pycoders.com/link/7676/web)
    + SIMON WILLISON





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [fiber: 启用任意深尾/非尾递归的装饰器](https://pycoders.com/link/7680/web)
    + GITHUB.COM/TYLERHOU

- [dataklasses: 数据类的不同 Spin](https://pycoders.com/link/7674/web)
    + GITHUB.COM/DABEAZ

(`是也乎:`

嗯哼? 这几乎就是自制语法糖了, 当年 UliWeb 中包含类似的自制模块;

    from dataklasses import dataklass

    @dataklass
    class Coordinates:
        x: int
        y: int

然后就可以:

    >>> a = Coordinates(2, 3)
    >>> a
    Coordinates(2, 3)
    >>> a.x
    2
    >>> a.y
    3
    >>> b = Coordinates(2, 3)
    >>> a == b
    True
    >>>



)


- [tqdm: 用于 Python CLI 应用程序的智能进度表](https://pycoders.com/link/7697/web)
    + TQDM.GITHUB.IO

(`是也乎:`

叕一个 CLI 下进度条模块;
Arabic (taqadum, تقدّم)

)


- [pixray: 图像生成系统](https://pycoders.com/link/7684/web)
    + GITHUB.COM/PIXRAY


(`是也乎:`

![pixray](https://ipic.zoomquiet.top/2021-12-22-zshot%202021-12-22%2009.02.45.jpg)

像素级

)


- [drgn: 可编程调试器](https://pycoders.com/link/7702/web)
    + GITHUB.COM/OSANDOV





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ PythOnRio Meetup](https://pycoders.com/link/7675/web)
    + December 25, 2021

- [⋅ Inland Empire Pyladies (CA, USA)](https://pycoders.com/link/7694/web)
    + December 27, 2021

- [⋅ Introduction to the Python Programming Language (In Persian)](https://pycoders.com/link/7690/web)
    + December 28, 2021

⋅ Weekly Real Python Office Hours Q&A (Virtual) January 5, 2021


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅
- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 504 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-504.html)
- 修订: [issue-504.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-504.md)


## PPS:
> 不觉中蟒周刊快译已经到了第10个年头

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF504D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF504D4Q90XdDA7g):



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





