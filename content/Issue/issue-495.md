Title: PyCoder 495
Slug: issue-495
Date: 2021-10-20 11:42
Tags: Weekly,Python,pycoders,ZH


>  GIL-Free CPython 来了


原文: [PyCoder's Weekly - Issue #495](https://pycoders.com/issues/495)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211020 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211020 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [CPython No-GIL 分支](https://pycoders.com/link/7237/web)
    + GITHUB.COM/COLESBURY 
    + • Shared by Henry Schreiner

This is a proof-of-concept implementation of CPython that supports multithreading without the global interpreter lock (GIL), from Facebook research. An overview of the design is described in the Python Multithreading without the GIL Google doc. Also see the related discussions on LWN and Hacker News.


(`是也乎:`

活久见, 老爹当年的一闪年,
现在终于不在坚持.

)


- [为毛不应该直接调用 setup.py ?](https://pycoders.com/link/7209/web)
    + PAUL GANSSLE


“The setuptools team no longer wants to be in the business of providing a command line interface and is actively working to become just a library for building packages. What you should do instead depends on your use case, but if you want some basic rules of thumb, there is a table in the summary section.”


-  Data Elixir: Data Science Newsletter
    +  DATA ELIXIRsponsor

Data Elixir is an email newsletter that keeps you on top of the tools and trends in Data Science. Covers machine learning, data visualization, analytics, and strategy. [Curated weekly with top picks from around the web →](https://pycoders.com/link/7203/web)


(`是也乎:`

数据科学中 Py 的地位其它语言当然在努力追上

)


- [在哪儿观察努力?  查阅 Python 核心开发人员活动](https://pycoders.com/link/7210/web)
    + ŁUKASZ LANGA


“One of the tasks given me by the Python Software Foundation as part of the Developer in Residence job was to look at the state of CPython as an active software development project. What are people working on? Which standard libraries require most work? Who are the active experts behind which libraries?”


- [Python 3.10中很酷的新功能](https://pycoders.com/link/7228/web)
    + REAL PYTHON 
    + course


In this course, you’ll explore some of the coolest and most useful features in Python 3.10. You’ll appreciate more user-friendly error messages, learn about how you can handle complicated data structures with structural pattern matching, and explore new enhancements to Python’s type system.

(`是也乎:`

COOL 不 COOL 看用的人.

)


- [PyCascades 2022 CFP 在周日关闭 (Oct 24)](https://pycoders.com/link/7234/web)
    + PYCASCADES CONFERENCE

- [第3季度的PSF同事宣布](https://pycoders.com/link/7208/web)
    + PYTHON SOFTWARE FOUNDATION

- [参与 Python 开发者调查2021](https://pycoders.com/link/7219/web)  
    + PYTHON SOFTWARE FOUNDATION

- [Psycopg 3.0 发布](https://pycoders.com/link/7242/web)
    + PSYCOPG.ORG

- [PyPy 7.3.6 发布](https://pycoders.com/link/7216/web)
    + PYPY.ORG

(`是也乎:`

NB, 当年的一闪念, 今天变成独立大叉.

)


-----------------------------------------
## 探讨/吐糟
> Discussions

NIL




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [测试是不够的: 向 urllib3 添加类型提示后/案例研究](https://pycoders.com/link/7232/web)
    + SETH MICHAEL LARSON

“Since Python 3.5 was released in 2015 including PEP 484 and the typing module type hints have grown from a nice-to-have to an expectation for popular packages. To fulfill this expectation our team has committed to shipping type hints for the v2.0 milestone. What we didn’t realize is the amount of value we’d derive from this project in terms of code correctness.”

(`是也乎:`

嗯哼?这种基础库, 能不动就嫑动./
)



- [欢迎又一批 CPython Developer in Residence](https://pycoders.com/link/7238/web)
    + REAL PYTHON 
    + podcast

Earlier this year, the Python Software Foundation announced the creation of the Developer in Residence role. The first Visionary Sponsors of the PSF have provided funding for this new role for one year. What development responsibilities does this job address? This week on the show, Łukasz Langa talks about becoming the first CPython Developer in Residence.

(`是也乎:`

![CPython](https://ipic.zoomquiet.top/2021-10-20-ScreenShot%202021-10-20%2008.32.44.jpg)

)


- [Python 赋值表达式以及 Walrus/海象 运算符](https://pycoders.com/link/7246/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn about assignment expressions and the walrus operator. The biggest change in Python 3.8 was the inclusion of the := operator, which you can use to assign variables in the middle of expressions. You’ll see several examples of how to take advantage of this new feature.

(`是也乎:=`


![Walrus](https://ipic.zoomquiet.top/2021-10-20-ScreenShot%202021-10-20%2008.31.10.jpg)

)



- [Python XML解析器的路线图](https://pycoders.com/link/7214/web)
    + REAL PYTHON

In this tutorial, you’ll learn what XML parsers are available in Python and how to pick the right parsing model for your specific use case. You’ll explore Python’s built-in parsers as well as major third-party libraries.

(`是也乎:`

这世界上嘦 JAVA 存在, XML 就不会消亡.

![Parsers](https://ipic.zoomquiet.top/2021-10-20-ScreenShot%202021-10-20%2008.30.45.jpg)

)



- [APT 如何折腾其绚烂的进度条](https://pycoders.com/link/7213/web)
    + JULIEN PALARD

“Today while running an apt full-upgrade I asked myself how apt does this nice progress bar stuck at the bottom line while still writing scrolling text.” Python example code included.


(`是也乎:`

不是, 再有趣的进度条能给最终用户带来什么提升?
只是运维看着舒服哈?

)


- [配置是 API, 而非 SDK](https://pycoders.com/link/7247/web)
    + HERNAN LOZANO 
    + • Shared by Hernan Lozano

Guidelines for config management in general and for Python apps in particular. Why “Configuration is just another API of your app” might be a good philosophy to adopt.

(`是也乎:`

SDK 开发工具, 不写东西用不了;
配置 现成接口, 可以直接使用.

)


- [Python’s property() : 将托管属性添加到您的类](https://pycoders.com/link/7240/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to create managed attributes, also known as properties, using Python’s property() in your custom classes.


(`是也乎:`

![property](https://ipic.zoomquiet.top/2021-10-20-ScreenShot%202021-10-20%2008.24.26.jpg)

)



- [Pip vs Conda: 两种 包系统 的比较](https://pycoders.com/link/7235/web)
    + ITAMAR TURNER-TRAURING


“Python has two commonly used packaging systems, pip and Conda. Learn the differences between them so you can pick the right one for you.”

(`是也乎:`

硬盘够大, 项目部署时无所谓速度,
上 conda

)



- [在 Python 安全处置密码](https://pycoders.com/link/7220/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Protect and secure your passwords and credentials in Python with help of these techniques and tips.

(`是也乎:`

注意, Medium 文章,
如果超过 free 限额就只能付费才看得到

)


- [理解 np.where()](https://pycoders.com/link/7239/web)
    + BEN COOK

The NumPy where() function is like a vectorized switch that you can use to combine two arrays.


(`是也乎:`


NumPy 这种数学梗密集作品,
每个函式都不简单...

)



- [三个工具来配置 Django 应用](https://pycoders.com/link/7215/web)
    + KRACEKUMAR.COM

- [functools.partial() 在 Django 更多用途](https://pycoders.com/link/7222/web)
    + ADAM JOHNSON



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [kubernetes-client: Kubernetes 的官方 Python 客户端库](https://pycoders.com/link/7224/web)
    + GITHUB.COM/KUBERNETES-CLIENT

(`是也乎:`

等等,官方?
也就是说 Ymal 还是恶心到人了?
准备用 Py 来替代?

)


- [Lenia: Mathematical Life Forms Simulator](https://pycoders.com/link/7204/web)
    + GITHUB.COM/CHAKAZUL

(`是也乎:`


![Lenia](https://ipic.zoomquiet.top/2021-10-20-ScreenShot%202021-10-20%2008.15.52.jpg)

官方也提醒: 会很慢,
期望  M1max 可以流畅之?

)


- [troposphere: 构建 AWS CloudFormation 描述](https://pycoders.com/link/7225/web)
    + GITHUB.COM/CLOUDTOOLS

(`是也乎:`

反正给程序看的东西,
一定值得用程序生成

)


- [classyconf: 用于配置和代码分隔的 声明性/可扩展库](https://pycoders.com/link/7244/web)
    + GITHUB.COM/HERNANTZ

(`是也乎:`

反正就是不想多写代码,
又得保持可读性,
那么一组配置基本上可以完成主要声明了

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Inland Empire Pyladies](https://pycoders.com/link/7227/web)
    +  (CA, USA)
    + October 25, 2021

- [⋅ Introduction to the Python Programming Language (In Persian)](https://pycoders.com/link/7223/web)
    + October 26, 2021

- [⋅ Python Sheffield](https://pycoders.com/link/7226/web)
    + October 26, 2021

- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/7230/web)
    + October 26 to October 27, 2021

- [⋅ PyKla Monthly Meetup](https://pycoders.com/link/7211/web)
    + October 27, 2021

- [⋅ Python Meeting Düsseldorf](https://pycoders.com/link/7207/web)
    + October 27, 2021

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/7236/web)
    + October 27, 2021

- [⋅ PyData Global 2021](https://pycoders.com/link/7206/web)
    + 2021 October 28 to October 31, 2021


- [⋅ deploy by DigitalOcean](https://pycoders.com/link/7200/web)
    + November 16 to November 17, 2021




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

- 首发: [Issue 495 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-495.html)
- 修订: [issue-495.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-495.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF495D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF495D4Q90XdDA7g):



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





