Title: PyCoder 563
Slug: issue-563
Date: 2023-02-08 11:42
Tags: Weekly,Python,pycoders,ZH


> 2023 年 Python 三大趋势


原文: [PyCoder's Weekly - Issue #563](https://pycoders.com/issues/563)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230208 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230208 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [用 Python 和 Rich 构建 Wordle 游戏](https://pycoders.com/link/10298/web)
    + REAL PYTHON

In this step-by-step project, you’ll build your own Wordle clone with Python. Your game will run in the terminal, and you’ll use Rich to ensure your word-guessing app looks good. Learn how to build a command-line application from scratch and then challenge your friends to a wordly competition!

(`是也乎:`

![Rich](https://ipic.zoomquiet.top/2023-02-08-zshot%202023-02-08%2014.48.18.jpg)

Rich 这个项目名起的太好了...


)


- [将 Python WASI 支持添加到 Wasm 语言运行时](https://pycoders.com/link/10299/web)
    + ASEN ALEXANDROV

“This article provides an overview of how Python works in WebAssembly environments and provides a step by step guide on how to use it.” See also the associated Hacker News Conversation.



- [2023 年 Python 的三大趋势](https://pycoders.com/link/10288/web)
    + JERRY CODES

An opinion piece on three trends likely to attract attention in the Python world in 2023: Python/Rust co-projects, web apps, and more typing. Read on for examples in each category.


(`是也乎:`

```
2023.py

+ 为 rust 服务
+ Web apps
+ 加强安全
```

对了 CharGPT 也有自己的猜想...

好象现在写文章不带上 ChatGPT 就不完整一样...


)

- [Django Security 发布 Issued: 4.1.6, 4.0.9, and 3.2.17](https://pycoders.com/link/10297/web)
    + DJANGO SOFTWARE FOUNDATION

- [PSF 正在招聘一名驻场安全开发人员](https://pycoders.com/link/10302/web)
    + PYTHON SOFTWARE FOUNDATION






-----------------------------------------
## 探讨/吐糟
> Discussions


- [动态语言的优点和缺点](https://pycoders.com/link/10280/web)
    + HACKER NEWS

This conversation is around Luke Plant’s excellent article Python’s “Disappointing” Superpowers that describes specific uses of Python’s dynamic capabilities that wouldn’t be possible in a static typed language.


(`是也乎:`

很多功能在静态语言中是不可能实现的...

)

-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Django 部署的真正考虑](https://pycoders.com/link/10300/web)
    + JAMES WALTERS 
    + • Shared by James Walters

Beginners often stumble when it’s finally time to get their Django app online. Instead of another deployment recipe, this post seeks to explain the fundamental concepts of deploying a Django app and equip developers to think through the process for themselves when they’re ready to make the transition from their code editor to the web.


(`是也乎:`


反正没那么简单,
即便是有 docker 可以一把梭了...

)


- [为 Flask API 构建 JavaScript 前端](https://pycoders.com/link/10310/web)
    + REAL PYTHON

Most modern websites are powered by a REST API. That way, you can separate the front-end code from the back-end logic, and users can interact with the interface dynamically. In this step-by-step tutorial, you’ll learn how to build a single-page Flask web application with HTML, CSS, and JavaScript.


(`是也乎:`

![Frontend](https://ipic.zoomquiet.top/2023-02-08-zshot%202023-02-08%2014.44.45.jpg)

)

- [渐进的稳健性: 来自静态 Python 的经验教训](https://pycoders.com/link/10282/web)
    + LU, GREENMAN, MEYER, ET AL

A synopsis of a deep paper analyzing Static Python, a Python variant developed at Instagram to move from gradually-typed to statically-typed. Full paper available as PDF.

- [Python 中的字典调度模式](https://pycoders.com/link/10311/web)
    + MARTIN HEINZ

The dictionary dispatch pattern uses a dict to store references to functions, allowing you to replace long if/else statements or as an alternative to the match statement. Read on for how and where to use it.

(`是也乎:`

常用技巧哪, 之前只用过其中两种, 没想到可以玩出这么多花儿来...

)


- [Python 中的 5 个常见 Asyncio 错误（以及如何避免它们）](https://pycoders.com/link/10284/web)
    + JASON BROWNLEE

Asyncio is one of several methods of doing parallelism in Python. It uses a co-routine structure. This article describes five common errors people new to asyncio may make and how to avoid them.

- [在 Python 包中包含 Rust Crate](https://pycoders.com/link/10313/web)
    + PETER BAUMGARTNER

It is becoming increasingly common to ship Rust components as part of a Python package. This blog post is a dev journal on how Peter did just that with one of his packages.

(`是也乎:`

这个脑洞可以哪,
将 rust 的绘制库自动编译安装给 py 来用...

PS: 项目名称由 ChatGPT 建议而得, 这波秀到了

以往都是用 C 项目来包含的,现在迁移到 Rust 实现的原因是...

)


- [用计算机视觉玩 DS 游戏](https://pycoders.com/link/10285/web)
    + MEDIUM.COM/@NATHANCOOPERJONES 
    + • Shared by Nate Jones

This posting is about how to use an object detection model to control a DS emulator to become an expert in playing the Super Mario 64 DS minigame “Wanted!”



- [如何将 C 风格的 for 循环添加到 Python](https://pycoders.com/link/10292/web)
    + TUSHAR SADHWANI

Ever want a C-style for-loop in Python? No? Well you can have one anyway. See how Tushar implemented with for (i := var(0), i < 10, i + 2):

- [用 Protocol 修复 Python 中的循环导入](https://pycoders.com/link/10306/web)
    + BRIAN OKKEN

This article walks you through how to use typing.Protocol to help detect and problems caused through circular imports.

(`是也乎:`

基于思想: [再谈 Python 中的继承（译） | Frost's Blog](https://frostming.com/2021/07-30/python-subclassing-redux-cn/)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [gracy: 更好的 API 管理](https://pycoders.com/link/10312/web)
    + GITHUB.COM/GUILATROVA • Shared by Gui Latrova

(`是也乎:`

改变了整个儿开发流程,
就是为了自动化监察统计?

)


- [Xorbits: 兼容、可扩展的数据科学](https://pycoders.com/link/10303/web)
    + GITHUB.COM/XPROBE-INC 
    + • Shared by Chris Qin

- [flatliner-src: 将 Python 程序转换为一行代码](https://pycoders.com/link/10308/web)
    + GITHUB.COM/HHC97

(`是也乎`:


仅仅使用 lambda 就将可以将一切 Python 程序变成一行代码;
叕一次证明 Python 是多范式语言,
内部隐藏了很多语言,
最成功的就是 LISP.



)


- [anywidget: 轻松自定义 Jupyter 小部件](https://pycoders.com/link/10290/web)
    + GITHUB.COM/MANZT

- [pynecone: 纯 Python 中的 Web 应用程序](https://pycoders.com/link/10294/web)
    + GITHUB.COM/PYNECONE-IO




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [pyCologne User Group Treffen](https://pycoders.com/link/10293/web)
    + February 8, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10286/web)
    + February 8, 2023

- [Python Atlanta](https://pycoders.com/link/10295/web)
    + February 9, 2023

- [PyDelhi User Group Meetup](https://pycoders.com/link/10279/web)
    + February 11, 2023

- [DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/10309/web)
    + February 11, 2023

- [PyConFr 2023](https://pycoders.com/link/10305/web)
    + February 16 to February 20, 2023


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 563 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-563.html)
- 修订: [issue-563.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-563.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

## PPS:
> 不觉中蟒周刊快译已经到了第11个年头

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

-------------

好文笔,感叹号年度配额: **0/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF563D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF563D4Q90XdDA7g):



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



