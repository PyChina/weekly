Title: 蠎周刊(PyCoder)575
Slug: issue-575
Date: 2023-05-03 11:42
Tags: Weekly,Python,pycoders,ZH


> 原创Raspberry Pi 手表


原文: [PyCoder's Weekly - Issue #575](https://pycoders.com/issues/575)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230503 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230503 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [Python 类: OOP 的力量](https://pycoders.com/link/10723/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to create and use full-featured classes in your Python code. Classes provide a great way to solve complex programming problems by approaching them through models that represent real-world objects.


(`是也乎:`

可能就是能涨工资...对生产效率帮助不大?


)

- [跟我聊 Python：PyCon 2023 直播](https://pycoders.com/link/10750/web)
    + KENNEDY, 
    + MUNOZ, 
    + MUOH, 
    + WILLIAMS, 
    + MCLENDON, 
    + TIBOR PODCAST

Talk Python to Me interviews a host of people at PyCon US 2023. Guests include Mario Munoz, Nick Muoh, Chris Williams, Ray McLendon, and Sean Tibor all talking about their experience at the conference.


(`是也乎:`

这篇报道丰富了...
大型群口相声...

)


- [用 Python 创建 Mastodon 机器人](https://pycoders.com/link/10735/web)
    + TIAGO RANGEL DE SOUSA

“With a Mastodon bot, you can automate tasks such as posting updates, replying to mentions, or even creating interactive chatbots.” This tutorial teaches you how to build such a bot.

- [PEP 713: 可调用模块](https://pycoders.com/link/10724/web)
    + PYTHON.ORG

- [PEP 712: dataclasses.field  的“Converter”参数](https://pycoders.com/link/10734/web)
    + PYTHON.ORG

- [Program—PyCon AU 2023](https://pycoders.com/link/10721/web)
    + PYCON.ORG.AU

- [urllib3 v2.0.0 Is 正式发布](https://pycoders.com/link/10748/web)
    + SETHMLARSON.DEV


(`是也乎:`

requests 自己作死...现在其它优秀模块已经上位...

SEE: [Why I'm not collaborating with Kenneth Reitz — njs blog \-\-\- 为什么我不与 Kenneth Reitz 合作 — njs 博客](https://vorpus.org/blog/why-im-not-collaborating-with-kenneth-reitz/)

)


-----------------------------------------
## 探讨/吐糟
> Discussions

- [好像没有足够的包装工具: Rye](https://pycoders.com/link/10737/web)
    + REDDIT


(`是也乎:`

> poetry/pip/pipenv/pyenv/venv/virtualenv/pdm/hatch/… 的实验性替代品


all-in-one 式的日常工具,
果断用 rust 构建出来了,
解决以往一堆又一堆 Python 工具没解决的根本问题...


就等 1.0 发布了...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [使用 Python 的 assert 调试和测试你的代码](https://pycoders.com/link/10738/web)
    + REAL PYTHON 
    + COURSE

In this course, you’ll learn how to use Python’s assert statement to document, debug, and test code in development. You’ll learn how assertions might be disabled in production code, so you shouldn’t use them to validate data. You’ll also learn about a few common pitfalls of assertions in Python.


(`是也乎:`


![assert](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.53.27.jpg)

)


- [同步还是异步? 揭开 Django 信号的神秘面纱](https://pycoders.com/link/10727/web)
    + MATT LAYMAN

Django signals provide a powerful way to trigger actions when specific events occur, but are they asynchronous or synchronous? In this article, we’ll explore the answer to this question and discuss the pros and cons of using Django signals in your web applications.





- [调试 Python 和 C 混合语言堆栈](https://pycoders.com/link/10729/web)
    + ENTSCHEV & ZAITLEN

Debugging is difficult. Debugging across multiple languages is especially challenging, and debugging across devices often requires a team with varying skill. This article describes the process one team uses to debug across a mixed Python/C stack.

(`是也乎:`


只用 GDB 也可以, 就是要追加更多的脑汁儿...


![Mixed](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.37.33.jpg)


PS: [Excalidraw](https://excalidraw.com/) 是真流行...

)


- [用 Tkinter 程序验证用户输入](https://pycoders.com/link/10730/web)
    + KHUMBO KLEIN

When writing GUI applications you often need to accept data from users. Reliable applications need to validate the input. This article outlines some strategies for dealing with it in the world of Tkinter GUI programming.


(`是也乎:`


Tk 界面现在一点儿也不原始了哪...
![Apps](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.35.25.jpg)

)


- [PyTorch 性能特性及其交互方式](https://pycoders.com/link/10740/web)
    + PAUL BRIDGER

PyTorch in 2023 is a complex beast, with many great performance features hidden away. This article goes through a series of empirically tested tuning techniques and settings in all combinations.

(`是也乎:`

PyTorch 已经 beast ...
这个形容很精当, 简直突然就翻盘了...

)


- [如何构建自己的 Raspberry Pi 手表](https://pycoders.com/link/10749/web)
    + ASHLEY WHITTAKER

Using a 1.28-inch TFT display and a watch board, these folks were able to make a wearable out of the Raspberry Pi RP2040. Read on for where they found the parts and how they did it.

(`是也乎:`


![Watch](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.30.55.jpg)

使用 Pico 控制板的芯片 RP2040 自己设计的 PCB 构建...
当然, 控制代码是 Python ;-)


)


- [华尔街从 Excel 到 Python 的转变](https://pycoders.com/link/10741/web)
    + JACOB DIAMON-REIVICH

Excel isn’t going away, but increasingly financial institutions are turning to Python for their calculation needs. Learn why and what tools are involved.


(`是也乎:`


![Wall](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.29.24.jpg)

Wall 街的金蛇...

)


- [eCharts for Python](https://pycoders.com/link/10745/web)
    + MARK LITWINTSCHIK

Apache eCharts is a web-based charting library built using TypeScript. This post shows you how to use eCharts through a Python wrapper.


(`是也乎:`

国产 eCharts , 就是那个 [Ovilia \(Wenli Zhang\)](https://github.com/Ovilia) 小姐姐主创的模块,
现在也有次级拓展了...

)

-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [msgspec: 编写/验证 JSON、MessagePack、YAML 和 TOML](https://pycoders.com/link/10733/web)
    + GITHUB.COM/JCRIST 
    + • Shared by Jim Crist-Harif

(`是也乎:`

![msgspec](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.24.09.jpg)

神级logo...

有四成 C 代码...
目测这个模块火了的话, 一定有人拿来用 rust 重写...


)

- [python-build-standalone: Python 的可再发行版本](https://pycoders.com/link/10731/web)
    + GITHUB.COM/INDYGREG

(`是也乎:`


Rust 含量不小...
是 PyOxidizer 的 姐妹项目: PyOxy ...

)


- [polyfactory: 模拟数据生成工厂](https://pycoders.com/link/10726/web)
    + GITHUB.COM/LITESTAR-ORG

(`是也乎:`

测试工程中的 mock 艺术, 简直可以出很多书了...


)


- [markdown-code-runner: 执行 Markdown 代码块](https://pycoders.com/link/10736/web)
    + GITHUB.COM/BASNIJHOLT


(`是也乎:`

![markdown](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.20.05.jpg)


网红脸式 README ....

)


- [griptape: 用于 AI 工作流和管道的 Python 框架](https://pycoders.com/link/10743/web)
    + GITHUB.COM/GRIPTAPE-AI

(`是也乎:`

Python 生态, 以 大数据出圈, AI 为本命, 真.搭上了时代的暴风口...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [STL Python](https://pycoders.com/link/10751/web)
    + May 3, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10742/web)
    + May 3, 2023

(`是也乎:`

![Office](https://ipic.zoomquiet.top/2023-05-03-zshot%202023-05-03%2009.17.09.jpg)

一晃这个公开活动也已经第四年了,
而真蟒, 也因为自己不懈的积累原创好文章,
活下来了....

)


- [Canberra Python Meetup](https://pycoders.com/link/10728/web)
    + May 4, 2023

- [PyDelhi User Group Meetup](https://pycoders.com/link/10744/web)
    + May 6, 2023

- [IndyPy Monthly Meetup](https://pycoders.com/link/10746/web)
    + May 9, 2023

- [JupyterCon 2023](https://pycoders.com/link/10732/web)
    + May 10 to May 13, 2023



-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 523](https://weekly.pychina.org/issue/issue-523.html)
- 2021: [蠎周刊 471](https://weekly.pychina.org/issue/issue-471.html)
    + [pythonista-weekly : Pyw 497](https://weekly.pychina.org/python-weekly/pyw-497.html)
- 2020: [蠎周刊 417](https://weekly.pychina.org/issue/issue-417.html)
    + [pythonista-weekly : Pyw 447](https://weekly.pychina.org/python-weekly/pyw-447.html)
- 2019: [蠎周刊 366](https://weekly.pychina.org/issue/issue-366.html)
- 2018: [蠎加载 173](https://weekly.pychina.org/importpython/importpython-173.html)
- 2017: [蠎加载 122](https://weekly.pychina.org/importpython/importpython-122.html)
- 2016: [蠎周刊 210](https://weekly.pychina.org/issue/issue-210.html)
    + [蠎加载 71](https://weekly.pychina.org/importpython/importpython-71.html)
- 2015: [蠎周刊 164](https://weekly.pychina.org/issue/issue-164.html)
    + [蠎加载 30](https://weekly.pychina.org/importpython/importpython-30.html)
- 2014: [Issue 113: Friday](https://weekly.pychina.org/issue/issue-113.html)
- 2013: 空缺
- 2012: [Issue 12 ~ Beautiful is Better than Ugly](https://weekly.pychina.org/issue/issue-12.html)


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
            _~--^~_
        \) /  - ^  \ \/
          '_   v   _'
          > '-----' <

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```




-----------------------------------------
# PS:

- 首发: [Issue 575 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-575.html)
- 修订: [issue-575.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-575.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF575D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF575D4Q90XdDA7g):



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



