Title: 蠎周刊(PyCoder)577
Slug: issue-577
Date: 2023-05-17 11:42
Tags: Weekly,Python,pycoders,ZH


> 上更快的 CPython


原文: [PyCoder's Weekly - Issue #577](https://pycoders.com/issues/577)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230517 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230517 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [PyCon 上更快的 CPython](https://pycoders.com/link/10805/web)
    + JAKE EDGE

This article summarizes the report the Faster CPython team gave at PyCon 2023. It gives information on PEP 659 Specializing Adaptive Interpreter and other performance improvements on the roadmap.


(`是也乎:`


> Faster CPython 团队的两名成员是应 Guido van Rossum 的要求在微软组建的 ...


... 这不也是对 CRISC 系统的描述吗？

然后, 有各种吐糟, 不过, 有专人长期思考如何加速运行, 也是好事儿,
或是说开发语言社区成熟的一个标志?

)

- [可信发布: 使用 Github Actions 发布到 PyPI](https://pycoders.com/link/10818/web)
    + PHILIP JONES

PyPI recently introduced a method to publish using GitHub Actions without the need for usernames and passwords. This post shows you Philip’s set-up for his own projects using this new feature.

(`是也乎:`

来自 github 就可信了?

)



- [虚拟环境结构和包装生态系统调查](https://pycoders.com/link/10819/web)
    + REAL PYTHON 
    + PODCAST

How do Python virtual environments work under the hood? How does understanding these concepts help you with managing them for your projects? This week on the show, CPython core developer Brett Cannon returns to discuss his recent articles about virtual environments and the Python packaging landscape.


(`是也乎:`


![PODCAST](https://ipic.zoomquiet.top/2023-05-17-zshot%202023-05-17%2008.33.25.jpg)
)


- [2023 年 Python 软件基金会董事会选举日期](https://pycoders.com/link/10798/web)
    + PYTHON SOFTWARE FOUNDATION

- [Hacker Initiative 2023 年拨款周期:申请征集](https://pycoders.com/link/10801/web)
    + HACKERINITIATIVE.ORG





-----------------------------------------
## 探讨/吐糟
> Discussions




None...





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [如何编写需要大量数据的测试？](https://pycoders.com/link/10812/web)
    + SANDER KOOIJMANS

Imagine you work on a Django project. You want to test your application with unit tests and integrations tests. Your application has lots of database tables, which need to be filled with realistic data for each test case. This article explains 3 techniques that will help you to fill the database with a lot of data for each test case.

- [充分利用 Python 标准 REPL](https://pycoders.com/link/10802/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to use the Python standard REPL (Read-Eval-Print Loop) to run your code interactively. This tool will allow you to test new ideas, explore and experiment with new tools and libraries, refactor and debug your code, try out examples, and more.


(`是也乎:`

![REPL](https://ipic.zoomquiet.top/2023-05-17-zshot%202023-05-17%2008.27.08.jpg)

Jupyter 就是加强又加强的 REPL 


)


- [如何从微服务中恢复](https://pycoders.com/link/10821/web)
    + DAVID HANSSON


The frenzy of mircoservices-all-the-things has calmed somewhat and you may find yourself with a microservice architecture to maintain that probably shouldn’t be. This article details how to wrangle that network based architecture into a well modularized monolith.

(`是也乎:`


哈, 这可能是微服务另外一个头大的问题所在了...

)


- [与 Docker 的朋友们一起构建强大的持续集成](https://pycoders.com/link/10813/web)
    + REAL PYTHON

In this tutorial, you’ll use Docker and GitHub Actions to build a robust continuous integration pipeline for a multi-container web application consisting of Flask and Redis. Along the way, you’ll learn how to dockerize a Python web application.


(`是也乎:`


![CD](https://ipic.zoomquiet.top/2023-05-17-zshot%202023-05-17%2008.22.40.jpg)

)


- [使用 WebAssembly 和 Python 扩展 Web 应用程序](https://pycoders.com/link/10824/web)
    + ASEN ALEXANDROV

“This article shows how you can run a Python program within another application that uses a Wasm runtime (host) and have the Python program talk to the host and vice versa.”

(`是也乎:`

![WASM](https://ipic.zoomquiet.top/2023-05-17-zshot%202023-05-17%2008.19.38.jpg)


可能还得在 rust 的帮助下, Py 才能更加 Pythonic 的融合到 WASM 生态中

)



- [VardaGPT: 关于使用 ChatGPT 编码的故事](https://pycoders.com/link/10822/web)
    + IXAXAAR

Ixaxxar walks you through the step by step process he used to build and test a piece of code using ChatGPT as his guide. TL;DR: it isn’t quite ready to replace him yet.


(`是也乎:`

类似都市传说还在爆发, 何时不在关注这种内容之时,
才是 GPT 们融入日常的时刻...

> ...让 ChatGPT 修复特定代码时感到非常沮丧

是的, 感觉在和一位非常认真又非常轴的毕业生在对话,
嘦提示语给定的运行时条件一致, 最后总是绕到一个固定的回答中, 对代码改进无帮助的方向...

)


- [pytz: 西方最快的步兵枪](https://pycoders.com/link/10797/web)
    + PAUL GANSSLE

The pytz library and its interactions with datetime are a source of misunderstandings and ultimately bugs. This article points out the problem cases.


(`是也乎:`

> ...意思是说 pytz 是一个优化得很好的库


好吧, 作者的梗儿不知道从哪儿来的,
反正, 日期处理在 Python 一向是感觉很容易又很复杂,
原因, 还是当初根本没这么多复杂的时间变化任务...所以, 各种改良能力模块就出现了...

)

- [“Python之禅”中的矛盾](https://pycoders.com/link/10823/web)
    + DAVID CASSEL

This is a summary of Christopher Neugebauer’s talk at PyCascades reminding attendees how foolish consistency can be a hobgoblin to productivity.


(`是也乎:`

一致性也有坑...毕竟是30+年前的一机灵...

)


- [Why Mojo?](https://pycoders.com/link/10808/web)
    + MODULAR.COM

“A backstory and rationale for why we created the Mojo language.”

(`是也乎:`

Mojo 的初心是什么?

全程没提及 Rust, 其它 Julia 之类语言倒是说了不少,
关键就是想偷懒,
明明当前 ML 世界主要都是 Py 代码了,
但是, 涉及到计算密集场景就有各种其它语言任务,
干脆一起兼容了吧...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [atbswp: 极简主义的宏记录器](https://pycoders.com/link/10814/web)
    + GITHUB.COM/RMPR

(`是也乎:`

叕一个可以将 键鼠行为录制为一个宏的工具...

)


- [fastnumpyio: 加速 NumPy I/O](https://pycoders.com/link/10816/web)
    + GITHUB.COM/DIVIDECONCEPT

- [依赖问题检查器](https://pycoders.com/link/10817/web)
    + GITHUB.COM/FPGMAAS 
    + • Shared by Florian


(`是也乎:`

`*try` 家族叕一个工具,
应该是对 Poetry 依赖探查速度不满?

)

- [pandas-ai: 将生成 AI 集成到 Pandas 中](https://pycoders.com/link/10803/web)
    + GITHUB.COM/GVENTURI

(`是也乎:`

反正现在和 GPT 粘点儿边就爆 star

)


- [roadmapper: 将路线图作为代码库](https://pycoders.com/link/10799/web)
    + GITHUB.COM/CSGOH


(`是也乎:`


![roadmapper](https://ipic.zoomquiet.top/2023-05-16-zshot%202023-05-17%2007.46.51.jpg)


甘特图的第101种绘制姿势...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [Kx Con](https://pycoders.com/link/10804/web)
    + May 17 to May 21, 2023

- [PyCon LT 2023](https://pycoders.com/link/10820/web)
    + May 17 to May 21, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10825/web)
    + May 17, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/10806/web)
    + May 18, 2023

- [Python Northwest](https://pycoders.com/link/10815/web)
    + May 18, 2023

- [PyLadies Dublin](https://pycoders.com/link/10811/web)
    + May 18, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/10826/web)
    + May 19 to May 20, 2023

- [PyCon Italia 2023](https://pycoders.com/link/10827/web)
    + May 25 to May 29, 2023


-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 525](https://weekly.pychina.org/issue/issue-525.html)
- 2021: [蠎周刊 473](https://weekly.pychina.org/issue/issue-473.html)
    + [pythonista-weekly : Pyw 499](https://weekly.pychina.org/python-weekly/pyw-499.html)
- 2020: [蠎周刊 419](https://weekly.pychina.org/issue/issue-419.html)
    + [pythonista-weekly : Pyw 449(https://weekly.pychina.org/python-weekly/pyw-449.html)
- 2019: [蠎周刊 368](https://weekly.pychina.org/issue/issue-368.html)
- 2018: [蠎加载 175](https://weekly.pychina.org/importpython/importpython-175.html)
- 2017: [蠎加载 124](https://weekly.pychina.org/importpython/importpython-124.html)
- 2016: [蠎周刊 212](https://weekly.pychina.org/issue/issue-212.html)
    + [蠎加载 73](https://weekly.pychina.org/importpython/importpython-73.html)
- 2015: [蠎周刊 166](https://weekly.pychina.org/issue/issue-166.html)
    + [蠎加载 32](https://weekly.pychina.org/importpython/importpython-32.html)
- 2014: [Issue 115](https://weekly.pychina.org/issue/issue-115.html)
- 2013: 空缺
- 2012: [Issue 13 ~ Explicit is better than implicit.](https://weekly.pychina.org/issue/issue-13.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...
- [Chaos42 - YouTube](https://www.youtube.com/watch?v=fPQ6piLqMXE&list=PLToFpvpg6EgRo6naYOp-BX4So-DxOCne8&index=1)
    + VLog
    + 恢复各种嗯哼...



```
      _~^-^~_
  \/ /  ♡ ◷  \ \/
    '_   ⏝   _'
    ( '-----' <

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 577 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-577.html)
- 修订: [issue-577.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-577.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

## PPS:
> 不觉中蟒周刊快译已经到了第10+2个年头

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

所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF577D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF577D4Q90XdDA7g):



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



