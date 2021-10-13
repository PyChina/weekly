Title: PyCoder 494
Slug: issue-494
Date: 2021-10-13 11:42
Tags: Weekly,Python,pycoders,ZH


>  TIOBE曰: Python 成为 #1 


原文: [PyCoder's Weekly - Issue #494](https://pycoders.com/issues/494)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211013 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 211013 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [TIOBE曰: 超越 C 和 Java, Python 成为 #1 最受欢迎的编程语言 ](https://pycoders.com/link/7186/web)
    + SLASHDOT.ORG

ZDNet reports that Python “is now the most popular language, according to one popularity ranking.” “For the first time in more than 20 years we have a new leader of the pack…” the TIOBE Index announced this month. “The long-standing hegemony of Java and C is over.”

(`是也乎:`

很久没见 SLASHDOT/. 的消息了...

)


- [Python C API: 添加函数以访问 pyObject](https://pycoders.com/link/7177/web)
    + VICTOR STINNER

“The PyObject structure prevents indirectly to optimize CPython. We will see why and how I prepared the C API to make this structure opaque. It took me 1 year and a half to add functions and to introduce incompatible C API changes (fear!)”



- Improve Inefficient App Code With Datadog Application Performance Monitoring
    + DATADOG
    + sponsor


Datadog’s Continuous Profiler allows you to measure code performance changes over time. Quickly identify and optimize the most time- and resource-consuming parts in your application code in order to improve MTTR and enhance user experience. 
[Give it a try with a free trial →](https://pycoders.com/link/7166/web)

- [用 Pygame 在 Python 中构建小行星游戏](https://pycoders.com/link/7196/web)
    + REAL PYTHON 
    + course

In this course, you’ll build a clone of the Asteroids game in Python using Pygame. Step by step, you’ll add images, input handling, game logic, sounds, and text to your program.


(`是也乎:`

![Pygame](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2011.05.21.jpg)

)

- [探索 Python 3.10 的新功能](https://pycoders.com/link/7185/web)
    + REAL PYTHON 
    + podcast

Python 3.10 is here! This week on the show, two former guests and Real Python authors return to talk about the new features and changes in Python 3.10.


(`是也乎:`


![podcast](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2010.59.19.jpg)


Py3.10 有组织的带节奏...

)


- [Python 3.10 有什么伟大?](https://pycoders.com/link/7176/web)
    + TREY HUNNER 
    + • Shared by Trey Hunner

- [Guido van Rossum on 提高Python的表现](https://pycoders.com/link/7178/web)
    + SOFTWARE AT SCALE podcast

(`是也乎:`

晚年就得修正年轻时挖的坑

)



-----------------------------------------
## 探讨/吐糟
> Discussions

NIL




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [Representing Rational Numbers With Python Fractions](https://pycoders.com/link/7181/web)
    + REAL PYTHON

In this tutorial, you’ll learn about the Fraction data type in Python, which can represent rational numbers precisely without the rounding errors in binary arithmetic. You’ll find that this is especially important in financial and other high-precision applications.

- [用 print() 调试的技艺](https://pycoders.com/link/7190/web)
    + ADAM JOHNSON

“If you’re embarrassed at debugging with print(), please don’t be - it’s perfectly fine! Many bugs are easily tackled with just a few checks in the right places. As much as I love using a debugger, I often reach for a print() statement first.”



- [Python’s sum() : 求 SUM 值的 Pythonic 方法](https://pycoders.com/link/7171/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to use Python’s sum() function to add numeric values together. You also learn how to concatenate sequences, such as lists and tuples, using sum().


(`是也乎:`

![sum](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2010.42.37.jpg)

)


- [理解 Python 的全部, 通过 Builtins](https://pycoders.com/link/7170/web)
    + TUSHAR SADHWANI

“Python has a whole lot of builtins that are unknown to most people. This guide aims to introduce you to everything that Python has to offer, through its seemingly obscure builtins.”

- [如何使用 Python 生成 pdf](https://pycoders.com/link/7179/web)
    + MIKE DRISCOLL

Learn how to create a PDF with Python and ReportLab. You’ll learn about Canvas methods, PLATYPUS, Paragraphs, Tables and more.


(`是也乎:`

很多人学 Python 就是想来操作 Word 以便生成 pdf,
其实可以直接来的.

)


- [用 lupa 将 LUA 代码集成到 Python 应用中](https://pycoders.com/link/7174/web)
    + MARTY B

(`是也乎:`

![lupa](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2010.37.31.jpg)

用 Lua 替代 C 变成 Python 的拓展组件来用.

)


- [New to Python: 如何管理架构选择?](https://pycoders.com/link/7193/web)
    + STEVEN LOTT

- [在 Python 3.10 中查找和报告 Asyncio 错误](https://pycoders.com/link/7173/web)
    + SIMON WILLISON

- [functools.partial() 在 Django 中三种姿势](https://pycoders.com/link/7184/web)
    + ADAM JOHNSON




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [videohash: Perceptual Video Hashing](https://pycoders.com/link/7175/web)
    + PYPI.ORG

(`是也乎:`

对视频内容完成 HASHing

)


- [darker: Apply Black Formatting Only in Regions Changed Since Last Commit](https://pycoders.com/link/7188/web)
    + PYPI.ORG

(`是也乎:`

![darker](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2011.14.43.jpg)

叒一个综合 PEP8 工具,
只是, 这次只是针对 git diff 来检验.
支持各种编辑环境的嵌入.


)


- [prospector: 检查 Python 源文件](https://pycoders.com/link/7172/web)
    + GITHUB.COM/PYCQA

(`是也乎:`

一个综合各种 PEP8 工具的代码检验服务...


)



- [maryjane:  只有30行 Async Python 代码的MJPEG Server](https://pycoders.com/link/7189/web)
    + GITHUB.COM/BOOTRINO

(`是也乎:`

配合:

    ffmpeg -y -re -stream_loop -1 -i monster-family-2-teaser_h480p.mov -f image2 -update 1 /dev/shm/img.jpeg

一键完成网页电影播放...

![maryjane](https://ipic.zoomquiet.top/2021-10-13-ScreenShot%202021-10-13%2010.33.39.jpg)

)



- [poly: 通用文本转换/处理工具](https://pycoders.com/link/7194/web)
    + GITHUB.COM/3DIGITDEV

(`是也乎:`

直接从 clipboard 中完成数据处理?

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyMNTos](https://pycoders.com/link/7183/web)
    + October 14, 2021

- [⋅ Python Atlanta](https://pycoders.com/link/7192/web)
    + October 14, 2021

- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/7182/web)
    + October 15, 2021

- [⋅ Chattanooga Python User Group](https://pycoders.com/link/7180/web)
    + October 15 to October 16, 2021

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

- 首发: [Issue 494 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-494.html)
- 修订: [issue-494.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-494.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF494D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF494D4Q90XdDA7g):



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





