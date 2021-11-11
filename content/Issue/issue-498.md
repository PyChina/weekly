Title: PyCoder 498
Slug: issue-498
Date: 2021-11-11 11:42
Tags: Weekly,Python,pycoders,ZH


> 和 Guido 一起讨论加速 Python 


原文: [PyCoder's Weekly - Issue #498](https://pycoders.com/issues/498)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211111 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211111 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [银行 Python 的口述历史](https://pycoders.com/link/7360/web)
    + CAL PATERSON

Interesting read about the strange world of Python, as used by big investment banks: “Bank Python implementations are effectively proprietary forks of the entire Python ecosystem which are in use at many (but not all) of the biggest investment banks.”

- [CPython Developer 每周报告, November 1–7](https://pycoders.com/link/7394/web)
    + ŁUKASZ LANGA

“Python 3.9.8 got released this week! At this point in the 3.9 lifecycle this should be a relatively uneventful release. Instead, it took us a few days of work to get it out of the door. I still managed to squeeze in 51 closed PRs and even organized a meeting between the core developers and Daan Leijen, the author of mimalloc.”





- [用 Python 和 typer 构建 CLI-TODO 应用程序](https://pycoders.com/link/7373/web)
    + REAL PYTHON

Follow along this step-by-step project to create a to-do application for your command line using Python and Typer. While you build this app, you’ll learn the basics of Typer, a modern and versatile library for building command-line interfaces (CLI).


(`是也乎:`

![Typer](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.55.04.jpg)
Typer ~ CLI 版 FastAPI, 值得享用.

)


- [Python 软件基金会: 2021 年度筹款结束](https://pycoders.com/link/7391/web)
    + PYTHON SOFTWARE FOUNDATION

“The PSF launched its end-of-the-year fundraiser. There are two ways to donate: 1. donate directly to the PSF or 2. purchase a discounted PyCharm license, with all proceeds going to the PSF. Contributing to the PSF financially helps sustain programs that support the larger Python community.”

- [Python 3.9.8 and 3.11.0a2 可用ed](https://pycoders.com/link/7371/web)
    + CPYTHON DEV BLOG





-----------------------------------------
## 探讨/吐糟
> Discussions


- [缺乏经验的 Python 开发最显著迹象是什么?](https://pycoders.com/link/7389/web)
    + REDDIT

(`是也乎:`


这对面试非常重要哪...


)

- [str.isdigit , isnumeric and isdecimal 有什么区别?](https://pycoders.com/link/7370/web)
    + STACK OVERFLOW

(`是也乎:`

差之毫厘,失之千里...

)




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [探索 Django 模板/标签和过滤器](https://pycoders.com/link/7375/web)
    + REAL PYTHON 
    + podcast

Are you getting the most out of the Django framework? It’s a powerful web framework if you’re not interested in reinventing the wheel. Django includes a useful template system with inheritance for composing reusable HTML. This week on the show, Real Python author Christopher Trudeau shares his Django tips and tricks.

(`是也乎:`


![podcast](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.48.30.jpg)

)


- [用 Python 构建内容聚合器](https://pycoders.com/link/7372/web)
    + REAL PYTHON

In this project-based tutorial, you’ll build a content aggregator from scratch with Python and Django. Using custom management commands, feedparser, and django-apscheduler, you’ll set up an app to periodically parse RSS feeds for Python podcasts and display the latest episodes to your users.

(`是也乎:`


![Aggregator](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.49.07.jpg)


用 Django 构造一个节目发布网站.

)


- [Guido and Mark 聊如何令 Python 更快](https://pycoders.com/link/7382/web)
    + TALK PYTHON 
    + podcast


“This episode is the first of several that dive into some of the active efforts to increase the speed of Python while maintaining compatibility with existing code and packages. Who better to help kick this off than Guido van Rossum and Mark Shannon?”

(`是也乎:`


![Guido](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.45.16.jpg)


Links from the show

Guido van Rossum: @gvanrossum


Faster Python Plan: github.com/faster-cpython

The “Shannon Plan”: github.com/markshannon


Watch this episode on YouTube: [youtube.com](https://www.youtube.com/watch?v=_r6bFhl6wR8)

Episode transcripts: [Episode #339 Making Python Faster with Guido and Mark - \[Talk Python To Me Podcast\]](https://talkpython.fm/episodes/show/339/making-python-faster-with-guido-and-mark)

)


- [在 Python 中用 plt.scatter() 可视化数据](https://pycoders.com/link/7368/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn how to create scatter plots in Python, which are a key part of many data visualization applications. You’ll get an introduction to plt.scatter(), a versatile function in the Matplotlib module for creating scatter plots.

(`是也乎:`

![scatter](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.44.34.jpg)

)


- [如何保护您的 Python 软件供应链](https://pycoders.com/link/7390/web)
    + BENOÎT GOUJON 
    + • Shared by Benoît Goujon

A new kind of cyber threat has come to light recently: software supply chain attacks. While rare, they have massive impacts. This article describes the most common attacks in the Python ecosystem and gives hints on how to prevent them.

(`是也乎:`


高端话题,
一般还是确保链路上都是靠谱开源项目就好,
这也是为什么 Django 越来越大的原因吧

)


- [理解 Django: 命令您的应用程序](https://pycoders.com/link/7393/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

With this Understand Django article, you’ll learn about commands. Commands are the way to execute scripts that interact with your Django app. Learn about built-in commands and how to build your own.


(`是也乎:`

值得是个系列了,
关键看目标领域任务,
理解到什么程度足够就怼.

)


- [管理Python项目中的依赖项](https://pycoders.com/link/7374/web)
    + JACEK KOŁODZIEJ 
    + • Shared by Jacek Kołodziej

A high-level overview of managing dependencies in a Python project, why there’s more than one way to do it and what are the tradeoffs between them.

(`是也乎:`

好东西就是要自推荐;

这种依赖, 没有充足理由 -> 嫑动


)



- [PEP 672: Python 中 Unicode相关 安全注意事项](https://pycoders.com/link/7387/web)
    + PYTHON.ORG

“This document explains possible ways to misuse Unicode to write Python programs that appear to do something else than they actually do.”




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [pyheat: Python 用热力图进行性能分析](https://pycoders.com/link/7381/web)
    + GITHUB.COM/CSURFER


(`是也乎:`



![pyheat](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.34.20.jpg)


赞哪, Openresty 那种运行时 `火焰图`
的进一步优化:

直接对应使用代码行的用时分析了...


)


- [angle:  Python 最新可读语法支持](https://pycoders.com/link/7369/web)
    + GITHUB.COM/PANNOUS


(`是也乎:`

![angle](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.32.07.jpg)

面向郎读编程?

这种将自然英文自动转化为 JS 的开发语言,
毫无使用场景哪,
即便是常用语法可读了,
可真正调用的各种框架可都是不可读函式名呢...

)


- [sneklang: 嵌入式设备的语言受Python 启发](https://pycoders.com/link/7376/web)
    + SNEKLANG.ORG

- [Pyjion: A Drop-in JIT Compiler for Python 3.10](https://pycoders.com/link/7366/web)
    + TRYPYJION.COM


(`是也乎:`

加速计划成果之一?

)

- [cog: Python 文件生成工具](https://pycoders.com/link/7378/web)
    + NED BATCHELDER

(`是也乎:`


![cog](https://ipic.zoomquiet.top/2021-11-11-ScreenShot%202021-11-11%2010.24.00.jpg)

所以, Python 是万能胶水


)


- [django-simple-deploy: Django App 部署用配置生成](https://pycoders.com/link/7379/web)
    + GITHUB.COM/EHMATTHES 
    + • Shared by Eric Matthes

(`是也乎:`

Django 当年也是号称敏捷的,
现在要工具来加速部署了...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Miami](https://pycoders.com/link/7361/web)
    + November 13 to November 14, 2021

- [⋅ Django Girls Groningen](https://pycoders.com/link/7388/web)
    + November 13, 2021
    + 荷兰

- [⋅ PyCon Japan 2021](https://pycoders.com/link/7396/web)
    + November 15 to November 16, 2021

- [⋅ deploy by DigitalOcean](https://pycoders.com/link/7399/web)
    + November 16 to November 17, 2021

- [⋅ Women Who Code CONNECT Forward 2021](https://pycoders.com/link/7367/web)
    + November 18 to November 20, 2021


(`是也乎:`

`向前编码的女性`?

)

- [⋅ PyCon APAC 2021](https://pycoders.com/link/7377/web)
    + November 19 to November 24, 2021




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 498 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-498.html)
- 修订: [issue-498.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-498.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF498D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF498D4Q90XdDA7g):



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





