Title: PyCoder 486
Slug: issue-486
Date: 2021-08-18 11:42
Tags: Weekly,Python,pycoders,ZH


> NVIDIA 发布 CUDA Python


原文: [PyCoder's Weekly - Issue #486](https://pycoders.com/issues/486)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210818 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210818 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [给 UNIX 介绍 Python 加载器](https://pycoders.com/link/6853/web)
    + BRETT CANNON

Python Core Developer and Steering Council member Brett Cannon recently released his Python Launcher for UNIX project. In a nutshell, the Python Launcher for UNIX gives you a command that always launched the latest version of Python that you have installed. Learn the motivation behind the project and some of its bonus features in this introductory article.

(`是也乎:`

![Python](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.27.53.jpg)

Python 迷宫之一, 也是最基础的,
现在看, 将来可能变成最有力的武器之一...

)


- [Python 新闻: 2021年7月有什么新闻?](https://pycoders.com/link/6858/web)
    + REAL PYTHON

The Python community saw some great changes in July 2021. In this article, you’ll get up to speed on the big-ticket items that happened this past month, including some news about the CPython Developer-in-Residence position at the Python Software Foundation.

(`是也乎:`

![News](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.29.28.jpg)

)



- [PyCharm 2021.2.1 候选发布已经释放](https://pycoders.com/link/6862/web)
    + JETBRAINS.COM

Curious about what the next version of PyCharm will bring? Check out the latest release candidate!

(`是也乎:`

嗯哼, 就看 JETBAIN 能在 VSCoode 注视下生存多久了...

)


- [NVIDIA 发布 CUDA Python](https://pycoders.com/link/6873/web)
    + NVIDIA.GITHUB.IO

(`是也乎:`

黄大仙赛高...

)



-----------------------------------------
## 探讨/吐糟
> Discussions

- [“Python Packaging” 的问题](https://pycoders.com/link/6860/web)
    + TWITTER.COM/GLYPH

This Twitter thread from Glyph, the creator of the 
[Twisted framework](https://pycoders.com/link/6857/web)
, explores some common misconceptions about Python packaging and its exosystem.

(`是也乎:`


Twisted 终于升格为框架了...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Pyodide 可行性/用户用例/限制](https://pycoders.com/link/6851/web)
    + LUCIANA DE MELO E ABUD

The Pyodide project brings Python to the browser by compiling the interpreter, and 75 built-in packages such as NumPy and Pandas, to Web Assembly. Pyodide is being explored at Microsoft as a way to allow VS Code users to run Python scripts without a local Python installation. This case study explores Pyodide’s feasibility for this project and outlines some of the limitations the team encountered. You’ll also learn about some other features of VS Code for which Pyodide is being considered.


(`是也乎:`


Web Assembly 先在 VSCode 中完成运行,
很聪明哪...不用和浏览器大战...

预集成75+数据科学相关库的浏览器 Python 运行时,
也只有 VSCode 能带的动吧...

)


- [Python 中的可视化和交互式仪表板](https://pycoders.com/link/6852/web)
    + SOPHIA YANG

Have you ever heard of HoloViz? It’s a set of Python visualization and plotting tools for browser-based data visualization and presentation. In this article, Sophia Yang — a senior data scientist at Anaconda — explains why she loves HoloViz and what her workflow looks like when using it.

(`是也乎:`

![Dashboard](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.20.59.jpg)


Jupyter yyds

)

- [Pythonic Monotonic](https://pycoders.com/link/6856/web)
    + NED BATCHELDER

After someone shared some code from a technical interview book and asked if it was “Pythonic,” Ned Batchelder rewrote the code to see if he could come up with something better. See the problem and his solution, and check out the comments in the article and on Hacker News for more implementations. What can you come up with?

- [支持 Python 开源项目和维护者](https://pycoders.com/link/6865/web)
    + REAL PYTHON 
    + podcast

How do you define open source software? What are the challenges an open source project and maintainers face? How do maintainers receive financial, legal, security, or other types of help? This week on the Real Python Podcast, we have Josh Simmons from Tidelift and the Open Source Initiative to help answer these questions.


(`是也乎:`

![podcast](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.17.56.jpg)

)


- [用 Pandas 读写(各类)文件](https://pycoders.com/link/6859/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn about the Pandas IO tools API and how you can use it to read and write files. You’ll use the Pandas read_csv() function to work with CSV files. You’ll also cover similar methods for efficiently working with Excel, CSV, JSON, HTML, SQL, pickle, and big data files.


(`是也乎:`

虽然没人宣传过, 不过 Pandas 就象表弟兄: Pandoc 一样,
对文件格式都是海量支持...

![Pandas](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.11.02.jpg)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [Python 的高性能/高精度 CPU/GPU和内存分析器](https://pycoders.com/link/6868/web)
    + GITHUB.COM/PLASMA-UMASS

(`是也乎:`

当然, 前提是指定厂商的 GPU ...


![scalene](https://ipic.zoomquiet.top/2021-08-18-ScreenShot%202021-08-18%2012.10.22.jpg)

)


- [cuda-python: CUDA Python 底层绑定](https://pycoders.com/link/6867/web)
    + GITHUB.COM/NVIDIA

(`是也乎:`

嗯哼?
俺是从什么时候开始自动对 `Low-Level` 感觉高级的呢?
)

- [pycm: 多类混淆矩阵库 in Python](https://pycoders.com/link/6848/web)
    + GITHUB.COM/SEPANDHAGHIGHI


- [gpsdclient: 简单的 GPSD Client 和 Library](https://pycoders.com/link/6874/web)
    + GITHUB.COM/TFELDMANN 
    + • Shared by Thomas Feldmann

(`是也乎:`

反正北斗客户端模块是很难见到了...

)


- [borb: 叕一个 Python PDF库](https://pycoders.com/link/6870/web)
    + GITHUB.COM/JORISSCHELLEKENS 
    + • Shared by Joris Schellekens

(`是也乎:`

怎么感觉 pdf 相关模块越来越多?
这是什么情况触发的?

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

NIL
 
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

- 首发: [Issue 486 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-486.html)
- 修订: [issue-486.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-486.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF486D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF486D4Q90XdDA7g):



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





