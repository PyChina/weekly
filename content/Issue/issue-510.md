Title: PyCoder 510
Slug: issue-510
Date: 2022-02-02 11:42
Tags: Weekly,Python,pycoders,ZH


> Black 终于稳定了


原文: [PyCoder's Weekly - Issue #510](https://pycoders.com/issues/510)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220202 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220202 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [咩是 JIT, Pyjion 如何加速你的 Python?](https://pycoders.com/link/7941/web)
    + REAL PYTHON 
    + PODCAST

How can you can speed up Python? Have you thought of using a JIT (Just-In-Time Compiler)? This week on the show, we have Real Python author and previous guest Anthony Shaw to talk about his project Pyjion, a drop-in JIT compiler for CPython 3.10.


(`是也乎:`

![Pyjion](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2011.12.43.jpg)

叕一个加速器, 老爹有压力了...

)



- [Python 的 10 个未知安全陷阱](https://pycoders.com/link/7942/web)
    + DENNIS BRINKROLF

“In this blog post, we share 10 security pitfalls we encountered in real-world Python projects. We chose pitfalls that we believe are less known in the developer community.”



- [在 Python 中绘制 Mandelbrot Set](https://pycoders.com/link/7921/web)
    + REAL PYTHON

In this tutorial, you’ll visualize the famous Mandelbrot set using Python’s Matplotlib and Pillow libraries. You’ll learn how to draw the fractal in black and white, grayscale, and color.


(`是也乎:`


![Mandelbrot](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2011.12.32.jpg)

)


- [Apple 从 macOS Monterey 12.3 中删除了 Python 2.7](https://pycoders.com/link/7916/web)
    + APPLE.COM

“Python 2.7 was removed from macOS in this update. Developers should use Python 3 or an alternative language instead.” Also see the related discussion on Hacker News.

(`是也乎:`

不容易哪, macOS 系统中的 Python 代码也不少的

)



- [Black, Python 代码格式化器 稳了](https://pycoders.com/link/7918/web)
    + HACKER NEWS

The popular Python auto-formatter Black is finally non-beta software. Related discussion on Hacker News and Black’s stability policy doc.

- [Django Security 已经发布: 4.0.2, 3.2.12, and 2.2.27](https://pycoders.com/link/7950/web)
    + DJANGO SOFTWARE FOUNDATION
Includes fixes for a possible XSS via debug template tag and a denial-of-service possibility in file uploads.


- [Textual v0.1.14 追加 Windows 支持](https://pycoders.com/link/7937/web)
    + WILL MCGUGAN





-----------------------------------------
## 探讨/吐糟
> Discussions



- [PyPI 准备弃用 .egg 上传?](https://pycoders.com/link/7947/web)
    + DUSTIN INGRAM

.egg uploads make up less than 1% of built distribution uploads in Dec 2021. Do you still build or install eggs, or maintain a tool that supports eggs?


(`是也乎:`


卵胎生都要支持
)



- [GitHub 中最干净/漂亮的项目有哪些值得研究代码?](https://pycoders.com/link/7927/web)
    + REDDIT

(`是也乎:`


[psf/black: The uncompromising Python code formatter](https://github.com/psf/black)

![black](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2011.20.15.jpg)


官方出品, 老爹关注

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 Python enumerate() 来循环](https://pycoders.com/link/7944/web)
    + REAL PYTHON 
    + COURSE

Once you learn about for loops in Python, you know that using an index to access items in a sequence isn’t very Pythonic. So what do you do when you need that index value? In this course, you’ll learn all about Python’s built-in enumerate(), where it’s used, and how you can emulate its behavior.


(`是也乎:`


![enumerate](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2011.08.30.jpg)

)


- [PySide2 vs PySide6: 有什么区别? 该升级了吗?](https://pycoders.com/link/7931/web)
    + MARTIN FITZPATRICK

If you are already developing Python GUI apps with PySide2, you might be asking yourself whether it’s time to upgrade to PySide6 and use the latest version of the Qt library.

(`是也乎:`


关键看上游 Qt 的资源了...

)



- [Data Elixir: Data Science Newsletter](https://pycoders.com/link/7909/web)
    + DATA ELIXIR
    + SPONSOR

Data Elixir is a free newsletter that curates intermediate and advanced data science content from around the web. [Data Elixir: Data Science Newsletter](https://pycoders.com/link/7909/web)

(`是也乎:`

等等, Elixir 拿到投资了?
叕开始在 Python 社区刷广告...

)


- [Pandas 中读取 CSV 最快方法](https://pycoders.com/link/7943/web)
    + ITAMAR TURNER-TRAURING

This article covers: Pandas’ default CSV reading, the faster, more parallel CSV reader introduced in v1.4, and a different approach that can make things even faster.


(`是也乎:`

越基础的行为, 越难以优化...
因为, 历史中积累了太多嗯哼...

)



- [Executable Docs 可执行文件](https://pycoders.com/link/7953/web)
    + IVO HOUBRECHTS 
    + • Shared by Ivo Houbrechts

It’s common to include interactive Python sessions inside documentation. With a small script we can turn these docs into Jupyter notebooks and serve them instantly.


(`是也乎:`


可运行文档, 这是 LOTUS 最先提出的概念,
Jupyter 真正实用化,
然后, 变成了通用模块

)


- [外面下雨了? 用 Python 构建天气 CLI 应用程序](https://pycoders.com/link/7926/web)
    + REAL PYTHON

In this tutorial, you’ll write a nicely formatted Python CLI app that displays information about the current weather in any city you provide the name for.


(`是也乎:`

2002 年, 完成的第一个可用 Python 小工具, 就是天气自动播报器

![Weather](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2011.02.45.jpg)


那时还没什么 XML 分析器, 
是用 正则表达式 撸的...

)



- [用 Pyenv 和 Pyenv-Virtualenv 在 macOS 上安装 Python 并创建虚拟环境](https://pycoders.com/link/7917/web)
    + ANDREA GRANDI


(`是也乎:`


PyENV 是优雅和高效的, 只是:
编译环境得先有,
网络得靠谱,
另外, 还能清楚自动挂载的是什么...

所以, 对于通常情况, 还是 Anconda 更加显性, 可靠了...

)



- [理解 Python 的省略号文字 (...)](https://pycoders.com/link/7928/web)
    + BRETT CANNON



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [pip-secure-install: 在 CI 上安全安装 Python 依赖项的 GitHub 操作](https://pycoders.com/link/7934/web)
    + GITHUB.COM/MARKETPLACE


(`是也乎:`

对于 github 随时可以消失的地区, 这种工具...

)


- [mureq: Requests 的单文件替代方案](https://pycoders.com/link/7933/web)
    + GITHUB.COM/SLINGAMN


(`是也乎:`


一个普通程序猿对大问题的私人解决方案.

)


- [Python Graph Gallery: Python 制作的数百种图表的集合](https://pycoders.com/link/7932/web)
    + PYTHON-GRAPH-GALLERY.COM

(`是也乎:`


![Gallery](https://ipic.zoomquiet.top/2022-02-02-zshot%202022-02-02%2010.55.07.jpg)

真大全

)



- [Procrastinate: 基于 PostgreSQL 的 Python 任务队列](https://pycoders.com/link/7929/web)
    + PROCRASTINATE.READTHEDOCS.IO


(`是也乎:`

自从 MySQL 躲平后, 大家的热情都射逈 Pg 了///

不过, 这个项目名子已躺平了...

)


- [PyFlow: Python 中可视化和模块化块编程](https://pycoders.com/link/7935/web)
    + GITHUB.COM/BYCELIUM


(`是也乎:`

MAX 类似可视化计算流设计/调试器...

)



- [konsole: 可读、令人愉悦的控制台输出](https://pycoders.com/link/7924/web)
    + GITHUB.COM/APPAREBIT 
    + • Shared by Robert Grimm


(`是也乎:`

乍一看, 还以为是 KUbuntu 专用的呢...

)


- [django-plpy: PostgreSQL 中 Python 存储过程的 Django 工具包](https://pycoders.com/link/7948/web)
    + MEDIUM.COM/P 
    + • Shared by Thorin Schiffer

- [q: 为疲倦的程序员提供的快速调试输出](https://pycoders.com/link/7930/web)
    + PYPI.ORG

(`是也乎:`

等等, https://github.com/zestyping/q
吓俺一跳, 这要是

    https://github.com/q

那是真帬了..
不过, 先占住了 PyPi 中的 q 也非常不得了,
这是星际旅行中的 Q 先生哪...

    /tmp/q

永恒的逼叨逼...

而且有 golang/elixir 对应版本

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ Canberra Python Meetup](https://pycoders.com/link/7920/web)
    + February 3, 2022

- [⋅ Sydney Python User Group (SyPy)](https://pycoders.com/link/7925/web)
    + February 3, 2022

(`是也乎:`

SyPy 和 SyFy/SiFi 简直了, 绝对妙名.

)


- [⋅ Reunión Python Valencia](https://pycoders.com/link/7922/web)
    + February 3, 2022

- [⋅ PyCascades Remote 2020](https://pycoders.com/link/7938/web)
    + February 5 to February 7, 2022





-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 510 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-510.html)
- 修订: [issue-510.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-510.md)


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

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF510D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF510D4Q90XdDA7g):



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





