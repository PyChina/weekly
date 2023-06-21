Title: 蠎周刊(PyCoder)581
Slug: issue-581
Date: 2023-06-14 11:42
Tags: Weekly,Python,pycoders,ZH


> 什么是 Python 之禅？


原文: [PyCoder's Weekly - Issue #581](https://pycoders.com/issues/581)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230614 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230614 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [什么是 Python 之禅？](https://pycoders.com/link/10955/web)
    + REAL PYTHON

In this tutorial, you’ll be exploring the Zen of Python, a collection of nineteen guiding principles for writing idiomatic Python. You’ll find out how they originated and whether you should follow them. Along the way, you’ll uncover several inside jokes associated with this humorous poem.

- [JupyterLab 4.0 来了](https://pycoders.com/link/10956/web)
    + JASON WEILL

The Jupyter contributor community have announced JupyterLab 4.0. This blog post shows you some of the new features, including: performance improvements, editor upgrades, better search, and more.



- [Python 和塞尔达传说](https://pycoders.com/link/10959/web)
    + GAZ J

The Game Boy Color version of Legend of Zelda: Oracle of Ages contains a grid-based puzzle. Gaz writes about creating a brute force program to solve the challenge using Python.

- [Django 4.2.2 Bugfix 发布](https://pycoders.com/link/10957/web)
    + DJANGO SOFTWARE FOUNDATION

- [Python 3.11.4, 3.10.12, 3.9.17, 3.8.17, 3.7.17, 和 3.12.0 Beta 2 发布](https://pycoders.com/link/10954/web)
    + CPYTHON DEV BLOG


(`是也乎:`

WoW ... 这样一来, 气势不就有了?

)

- [PyCascades 2023 视频已上线](https://pycoders.com/link/10943/web)
    + YOUTUBE.COM

- [PyCon US 2023 视频已上线](https://pycoders.com/link/10967/web)
    + YOUTUBE.COM

- [Obfuscated Python 竞赛提交开放](https://pycoders.com/link/10972/web)
    + PYOBFUSC.COM

(`是也乎:`


对 [IOCCC](https://www.ioccc.org/index.html) 的戏仿大赛;

> IOPCC ~ International Obfuscated Python Code Competition

国际混乱Python代码大赛, 就比谁能写出可以运行, 但是, 人无法看明白的代码;

)

-----------------------------------------
## 探讨/吐糟
> Discussions


- [PEP 703 可选 GIL：时间表和问题](https://pycoders.com/link/10942/web)
    + PYTHON.ORG




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [为 Python 提出 Struct 语法](https://pycoders.com/link/10971/web)
    + BRETT CANNON

Bret has been pondering a new keyword that would tackle some of the limitations of data classes while offering syntax improvement over named tuples. This is still in the “what if” stage, but he is willing to write up a PEP if he thinks it will get traction.

- [使用 Django 4.2 的 async 功能聊天](https://pycoders.com/link/10952/web)
    + VÍÐIR VALBERG GUÐMUNDSSON


Django continues to add features to allow more and more asynchronous programming. This articles shows you how to use Django 4.2’s StreamingHttpResponse, Server-Sent Events, and PostgreSQL LISTEN/NOTIFY to build a chat application.



- [Python 中的迷宫第 1 部分：构建和可视化](https://pycoders.com/link/10946/web)
    + REAL PYTHON COURSE

In part one of this two-part project, you’ll design your maze and represent it in an object-oriented way. You’ll also visualize the maze and its solution using scalable vector graphics (SVG).

(`是也乎:`

![SVG](https://ipic.zoomquiet.top/2023-06-14-zshot%202023-06-14%2009.32.53.jpg)

)


- [将 Python 项目移植到 Rust](https://pycoders.com/link/10945/web)
    + JELMER VERNOOIJ

Jelmer has been working on porting some of his performance-constrained projects from Python to Rust. This blog post discusses how he’s approaching it and what is and isn’t working.

(`是也乎:`

一位 Haskell 粉丝推荐使用 PyO3 将 Py 模块向 crate 迁移,
不过, 发现很多 Py 特性很难简单的迁移到 Rust...

)


- [Python for Finance: Pandas Resample、Groupby 和 Rolling](https://pycoders.com/link/10948/web)
    + MATT HARRISON

When working with time series data such as financial information, the resample, grouping, and rolling features of Pandas can make your life easier. Read on to learn how.

- [从 Python 运行 Shell 命令的正确方法](https://pycoders.com/link/10960/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

These are all the options you have in Python for running other processes - the bad; the good; and most importantly, the right way to do it

(`是也乎:`


> ...但如果您需要将太多其他程序/命令串在一起，也许，也许您应该只编写 shell 脚本

扎心了, 不过, 的确如此, 否则, shell 没有存在的必要了...

)


- [6 月 1 日开始对 PyPI 实施 2FA](https://pycoders.com/link/10941/web)
    + PYPI.ORG

For those accounts that have two-factor authentication turned on for PyPI uploads, the use of 2FA is now required. Users with 2FA who were only using their password in the past will now have to perform 2FA as well. This is all part of the transition of PyPI to 2FA across the board.


(`是也乎:`


面对巨婴们...

)


- [了解 CPU 有助于加速 NumPy](https://pycoders.com/link/10968/web)
    + ITAMAR TURNER-TRAURING

With a little understanding of how CPUs and compilers work, you can speed up NumPy using Numba, the just-in-time compiler.


(`是也乎:`

所以, CPU 还是比 GPU 强?

)


- [Flask 认证指南](https://pycoders.com/link/10951/web)
    + AUTH0 DEVELOPERS 
    + • Shared by Robertino

This guide will help you learn how to secure a Flask web application using token-based authentication.

(`是也乎:`

可惜不是 Flask 能力认证, 
如果一个项目发展到可以颁发全网认可的能力认证书时...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [pystack: 检查正在运行或崩溃的 Python 中的堆栈帧](https://pycoders.com/link/10962/web)
    + GITHUB.COM/BLOOMBERG

(`是也乎:`

官方 tracback 的强化外挂

)


- [reactpy: 它是 React，但在 Python 中](https://pycoders.com/link/10958/web)
    + GITHUB.COM/REACTIVE-PYTHON

- [llm: 从命令行访问大型语言模型](https://pycoders.com/link/10966/web)
    + GITHUB.COM/SIMONW

(`是也乎:`

llm 这么好的名字就这么被占住了?

)


- [ADR-py: 创建架构决策记录](https://pycoders.com/link/10938/web)
    + GITHUB.COM/ALTOSTERINO 
    + • Shared by Daniel Różycki

(`是也乎:`

基于这书: [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
构建的对应工具;

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [Santa Cruz Python Meetup](https://pycoders.com/link/10949/web)
    + June 14, 2023

- [Python North East](https://pycoders.com/link/10964/web)
    + June 14, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10969/web)
    + June 14, 2023

- [pyCologne User Group Treffen](https://pycoders.com/link/10944/web)
    + June 14, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/10965/web)
    +June 15, 2023

- [Python Northwest](https://pycoders.com/link/10953/web)
    + June 15, 2023

- [PyLadies Dublin](https://pycoders.com/link/10947/web)
    + June 15, 2023

- [Django Girls Xai-Xai](https://pycoders.com/link/10939/web)
    + June 17 to June 18, 2023


(`是也乎:`

非洲 莫桑比克 的 Xai-Xai, 还以为是中国哪儿...

)

- [Building Micro Tech Communities Around Python Programming Language (June 20](https://pycoders.com/link/10973/web)
    + June 20 to June 21, 2023

- [Careers With Python: Volume 2](https://pycoders.com/link/10940/web)
    + June 20, 2023







-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 529](https://weekly.pychina.org/issue/issue-529.html)
- 2021: [蠎周刊 476](https://weekly.pychina.org/issue/issue-476.html)
    + [pythonista-weekly : Pyw 503](https://weekly.pychina.org/python-weekly/pyw-503.html)
- 2020: [蠎周刊 423](https://weekly.pychina.org/issue/issue-423.html)
    + [pythonista-weekly : Pyw 453](https://weekly.pychina.org/python-weekly/pyw-453.html)
- 2019: [蠎周刊 372](https://weekly.pychina.org/issue/issue-372.html)
- 2018: [蠎周刊 321](https://weekly.pychina.org/issue/issue-321.html)
- 2017: [蠎加载 128](https://weekly.pychina.org/importpython/importpython-128.html)
- 2016: [蠎加载 77](https://weekly.pychina.org/importpython/importpython-77.html)
- 2015: [蠎周刊 170](https://weekly.pychina.org/issue/issue-170.html)
    + [蠎加载 36](https://weekly.pychina.org/importpython/importpython-36.html)
- 2014: [Issue 119](https://weekly.pychina.org/issue/issue-119.html)
- 2013: 空缺
- 2012: [Issue 17 ~ 永远不晩](https://weekly.pychina.org/issue/issue-17.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [@Chaos42DAMA - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + VLog
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...



```
      _~-*`~_
  () /  ◶ #  \ ()
    '_   ∧   _'
    \ '--⌄--' /

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```




-----------------------------------------
# PS:

- 首发: [Issue 581 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-581.html)
- 修订: [issue-581.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-581.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF581D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF581D4Q90XdDA7g):



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



