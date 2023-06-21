Title: 蠎周刊(PyCoder)582
Slug: issue-582
Date: 2023-06-21 11:42
Tags: Weekly,Python,pycoders,ZH


> 只用pip才是最好的...


原文: [PyCoder's Weekly - Issue #582](https://pycoders.com/issues/582)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230621 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230621 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [更快的 Python 3.13 计划](https://pycoders.com/link/10997/web)
    + GITHUB.COM/FASTER-CPYTHON

This brief outline highlights the plan for the faster CPython project for the 3.13 release. Includes PEP 669, PEP 554, improved memory management, and more. Associated Hacker News discussion.

- [志愿服务、组织和寻找 Python 社区](https://pycoders.com/link/10996/web)
    + REAL PYTHON 
    + PODCAST

Have you thought about getting more involved in the Python community? Are you interested in volunteering for an event or becoming an organizer? This week on the show, we speak with organizers from this year’s PyCascades conference about making connections, learning new skills, and rationing your time.


(`是也乎:`

![Volunteering](https://ipic.zoomquiet.top/2023-06-21-zshot%202023-06-21%2010.52.42.jpg)

构建自己的最重要...

)

- [AsyncIO: Why I Hate It

AsyncIO：为什么我讨厌它](https://pycoders.com/link/10987/web)
    + CHARLES LEIFER OPINION

Charles is the creator of Peewee ORM and often gets the question “when will it support asyncio?” In this opinion piece he talks about why he doesn’t like asyncio and the alternatives he prefers.

(`是也乎:`


> threading.Thread + gevent


足够好了

)


- [PyPy v7.3.12 发布](https://pycoders.com/link/10991/web)
    + PYPY.ORG

-----------------------------------------
## 探讨/吐糟
> Discussions


- [并行编程难吗？](https://pycoders.com/link/11004/web)
    + HACKER NEWS

(`是也乎:`

Yes & NOT 

)


- [创建有效文档的技巧？](https://pycoders.com/link/10998/web)
    + ASK SLASHDOT


(`是也乎:`

写好了,自己读一遍

)

-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [迁移到 .readthedocs.yaml 配置](https://pycoders.com/link/10984/web)
    + READTHEDOCS.COM

The Read the Docs site has announced the new requirement that all builds must move to using a .readthedocs.yaml configuration file, version 2. There are some test windows where they will be temporarily enforcing the change, but the final release date is September 25, 2023. Read on for details on how to migrate your project.

- [在 Python 函数中使用和创建全局变量](https://pycoders.com/link/10988/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use global variables in Python functions using the global keyword or the built-in globals() function. You’ll also learn a few strategies to avoid relying on global variables because they can lead to code that’s difficult to understand, debug, and maintain.


(`是也乎:`


![全局](https://ipic.zoomquiet.top/2023-06-21-zshot%202023-06-21%2010.43.45.jpg)

)


- [Python 函数调用的依赖跟踪](https://pycoders.com/link/10995/web)
    + ALEX MAKELOV

Tracking the code and data accessed by a function call can be used to draw dependency graphs, for debugging and profiling, and for cache invalidation. This article shows you a variety ways of doing it, as well as some initial ideas that don’t work very well.

- [从多列 PDF 中提取文本](https://pycoders.com/link/10990/web)
    + ARTIFEX.COM 
    + • Shared by Harald Lieder

Learn how to use a PyMuPDF utility for detecting multiple columns in pages and extracting text along these columns. This can be useful for processing documents that have complex layouts, such as reports, newspapers, magazines, or academic papers.

- [pytest Fixtures 很神奇！](https://pycoders.com/link/10989/web)
    + FRANK WILES

Fixtures are building blocks for good tests and can increase development speed. The main issue with writing tests is setting up necessary data before the test, but pytest fixtures make it easier by injecting necessary data into your tests.

- [嫑说“简单”使用 Pyenv、Poetry 或 Anaconda](https://pycoders.com/link/11003/web)
    + BITE CODE

This article talks about the issues often introduced to newer Python coders by adapting more complicated package management mechanisms, and why sticking with pip is often the better choice.

(`是也乎:`

> ...Python 2 => 3 经历了 15 年的愤怒。

淦, 扎到心里了...

)


- [Cython vs CPython: 比较速度差异](https://pycoders.com/link/10999/web)
    + SIDDIQI

This article does a speed comparison between Cython and CPython using eleven different benchmarks. And although, as expected, Cython is faster, it isn’t in every scenario.

- [Django Views: 正确的方法](https://pycoders.com/link/10992/web)
    + SPOOKYLUKEY.GITHUB.IO

An opinionated guide on how to write views in Django by one of the core Django devs. Spoiler alert: he isn’t very fond of class-based-views.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [Shreddit: 删除您在 Reddit 上的评论历史记录](https://pycoders.com/link/10977/web)
    + GITHUB.COM/X89

(`是也乎:`

为了不给 GPT 们?

)


- [pymg: 堆栈跟踪的更好显示](https://pycoders.com/link/10981/web)
    + GITHUB.COM/MIMSEYEDI


(`是也乎:`


![pymg](https://ipic.zoomquiet.top/2023-06-21-zshot%202023-06-21%2010.28.42.jpg)

大显示器的动力...

)

- [faker-file: 用虚假数据创建文件](https://pycoders.com/link/10994/web)
    + GITHUB.COM/BARSEGHYANARTUR

(`是也乎:`

专门分析了许可证兼容情况...

)

- [jsonformer: 从语言模型生成结构化 JSON](https://pycoders.com/link/10985/web)
    + GITHUB.COM/1RGS

- [pyvibe: 从 Python 生成样式化的 HTML 页面](https://pycoders.com/link/10978/web)
    + GITHUB.COM/PYCOB




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [围绕 Python 编程语言构建微型技术社区](https://pycoders.com/link/11000/web)
    + June 20 to June 21, 2023

- [PyStaDa](https://pycoders.com/link/10982/web)
    + June 21, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11002/web)
    + June 21, 2023

- [PythOnRio Meetup](https://pycoders.com/link/11001/web)
    + June 24, 2023

- [World Conference on Data Science & Statistics](https://pycoders.com/link/10980/web)
    + June 26 to June 29, 2023



-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 530](https://weekly.pychina.org/issue/issue-530.html)
- 2021: [蠎周刊 477](https://weekly.pychina.org/issue/issue-477.html)
    + [pythonista-weekly : Pyw 504](https://weekly.pychina.org/python-weekly/pyw-504.html)
- 2020: [蠎周刊 424](https://weekly.pychina.org/issue/issue-424.html)
    + [pythonista-weekly : Pyw 454](https://weekly.pychina.org/python-weekly/pyw-454.html)
- 2019: [蠎周刊 373](https://weekly.pychina.org/issue/issue-373.html)
- 2018: [蠎周刊 322](https://weekly.pychina.org/issue/issue-322.html)
- 2017: [蠎加载 129](https://weekly.pychina.org/importpython/importpython-129.html)
- 2016: [蠎加载 78](https://weekly.pychina.org/importpython/importpython-78.html)
- 2015: [蠎周刊 171](https://weekly.pychina.org/issue/issue-171.html)
    + [蠎加载 37](https://weekly.pychina.org/importpython/importpython-37.html)
- 2014: [Issue 120](https://weekly.pychina.org/issue/issue-120.html)
- 2013: 空缺
- 2012: [Issue 18 Complex is better than complicated.](https://weekly.pychina.org/issue/issue-18.html)


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
           _~∽+`~_
       \/ /  → ♡  \ (/
         '_   ♢   _'
         / '--~--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 582 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-582.html)
- 修订: [issue-582.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-582.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF582D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF582D4Q90XdDA7g):



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



