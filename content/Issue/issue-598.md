Title: 蠎周刊(PyCoder)598
Slug: issue-598
Date: 2023-10-11 21:42
Tags: Weekly,Python,pycoders,ZH


> 给 个体企业家/Solopreneur 的建议


原文: [PyCoder's Weekly - Issue #598](https://pycoders.com/issues/598)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 231011 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 231011 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [Python的 tuple 数据类型：通过示例进行深入探讨](https://pycoders.com/link/11610/web)
    + REAL PYTHON

In Python, a tuple is a built-in data type that allows you to create immutable sequences of values. The values or items in a tuple can be of any type. This makes tuples pretty useful in those situations where you need to store heterogeneous data, like that in a database record, for example.

(`是也乎:`


![tuple](https://ipic.zoomquiet.top/2023-10-11-zshot%202023-10-11%2009.39.58.jpg)

)


- [学到的关于用 Python 构建 CLI 工具的知识](https://pycoders.com/link/11583/web)
    + SIMON WILLISON

In this blog post, Simon covers many of the things he has learned over the years when writing command-line tools in Python. He talks about the different kinds of command line arguments and tools that will help you process them.

(`是也乎:`


> ...一致性就是一切


是的, 嘦发现好的形式, 就一定要坚持应用在所有场景中...

> ...Click 使得构建遵循这些约定的 CLI 工具变得异常简单和高效

好框架已经为你准备好了一切.

)

- [Python 3.12: 有什么没在头条新闻](https://pycoders.com/link/11616/web)
    + BITE CODE

There has been plenty of coverage about the changes in Python 3.12, this article tries to show what fell through the cracks. It talks about performance, pathlib improvements, and a few other changes.

- [PSF 招聘兼职 Django 开发人员](https://pycoders.com/link/11609/web)
    + PYTHON SOFTWARE FOUNDATION

- [Python 3.11.6 发布](https://pycoders.com/link/11603/web)
    + CPYTHON DEV BLOG

- [Flask 3.0.0 发布](https://pycoders.com/link/11597/web)
    + PALLETSPROJECTS.COM

- [已发布 Django 安全版本：4.2.6、4.1.12 和 3.2.22](https://pycoders.com/link/11598/web)
    + DJANGO SOFTWARE FOUNDATION





-----------------------------------------
## 探讨/吐糟
> Discussions


- [给 个体企业家/Solopreneur 的建议？](https://pycoders.com/link/11585/web)
    + HACKER NEWS




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [类型提示：为未使用的测试参数传递 Any](https://pycoders.com/link/11605/web)
    + ADAM JOHNSON

When you create a function to match an interface, it often needs to accept parameters that it doesn’t use. Once you introduce type hints, testing such functions can become a little irksome as Mypy requires all arguments to have the correct types. This article covers a technique to avoid that work.

- [Python 基础：读取和写入文件](https://pycoders.com/link/11604/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to move data back and forth between your Python programs and external software by reading and writing files. You’ll practice reading and writing data stored in the CSV file format, one of the most widely supported file formats for transferring tabular data.


(`是也乎:`


![Python Basics](https://ipic.zoomquiet.top/2023-10-11-zshot%202023-10-11%2009.31.55.jpg)


Python Basics 已经是真蟒 的品牌图书+课程了...
)


- [Python 类型提示： pyastgrep 案例研究](https://pycoders.com/link/11602/web)
    + LUKE PLANT

Previously, Luke wrote an article about what was involved in adding Type Hints to parsy. This follow-on article tackles the effort on a project with different challenges: pyastgrep.

- [供应链安全角度看 Python 3.12.0](https://pycoders.com/link/11606/web)
    + SETH LARSON

Seth is the Security Developer-in-Residence at the Python Software Foundation and this article is part of his on-going effort to document and improve the release process and tools. Associated HN discussion.


(`是也乎:`


首位基金会驻场安全开发人员的报告...

)


- [抽象摘要的幻觉检测](https://pycoders.com/link/11607/web)
    + EUGENE YAN

Abstractive summary is an AI task that rephrases and condenses text content into a summary. This article is a deep dive into how to ensure correctness and the math involved in ensuring fluency, coherence, relevance, and consistency.

- [Data-Driven News Discourse Analysis With Python
使用 Python 进行数据驱动的新闻话语分析](https://pycoders.com/link/11614/web)
    + KARLIS KANDERS

This tutorial shows you how to do discourse analysis on news using Python through The Guardian’s API. You’ll see how to access content across years and perform topic analysis with sentence embedding.

- [测量 Python 执行时间的 5 种方法](https://pycoders.com/link/11613/web)
    + JASON BROWNLEE

There are several ways to measure the passing of time in Python, especially when determining the performance of your code. Read on to learn five functions from the time module and how to use them.


(`是也乎:`


分别基于...

```
    time.time()
    time.perf_counter()
    time.monotonic()
    time.process_time()
    time.thread_time()
```


)


- [Python-特定 设计模式](https://pycoders.com/link/11608/web)
    + DIMITRIJE STAMENIC

This is a third article in a series on design patterns in Python, with this one talking about a variation on singletons, a pattern that uses dynamic function binding, and sentinels.


(`是也乎:`

还是要对真正流畅的开发姿势抽象, 才能得到实用的模式

)


- [掌握使用 FastAPI 的集成测试](https://pycoders.com/link/11584/web)
    + ALEX JACOBS

This article shows you how to use MongoMock and MockS3 to power your integration tests on a FastAPI based project.


(`是也乎:`

各种 Mock 技巧...

)


- [Django 中使用 GeoDjango 和 PostGIS](https://pycoders.com/link/11611/web)
    + ADEYINKA ADEGBENRO 
    + • Shared by Manuel Weiss

This article shows how to use GeoDjango and PostGIS to work with geospatial data in Postgres.








-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code





- [perspective: 大型数据集的可视化组件](https://pycoders.com/link/11587/web)
    + GITHUB.COM/FINOS

- [shshsh: Python 和 Shell 之间的桥梁](https://pycoders.com/link/11601/web)
    + GITHUB.COM/ZQQQQZ2000

- [CardStock: 跨平台 GUI 构建工具](https://pycoders.com/link/11599/web)
    + GITHUB.COM/BENJIE-GIT 
    + • Shared by Mike McLeod

(`是也乎:`

反正, Flutter 们并没彻底解决这个问题...

)

- [reverse_argparse: 告诉用户他们运行了什么](https://pycoders.com/link/11593/web)
    + GITHUB.COM/SANDIALABS 
    + • Shared by Jason M. Gates

(`是也乎:`

好吧, 
这个简单要求其实真的不简单...

)

- [leaptable: 管理表格数据上由 LLM 支持的代理](https://pycoders.com/link/11615/web)
    + GITHUB.COM/PETERWNJENGA


(`是也乎:`

Excel 已经嵌入 Python 了,
马上 LLM 也一样...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyHEP 2023](https://pycoders.com/link/11588/web)
    + October 9 to October 13, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11612/web)
    + October 11, 2023

- [Python Atlanta](https://pycoders.com/link/11600/web)
    + October 12 to October 13, 2023

- [PyConnect Panama 2023](https://pycoders.com/link/11595/web)
    + October 13 to October 15, 2023

- [Django Girls Aba](https://pycoders.com/link/11590/web)
    + October 13 to October 14, 2023

- [DjangoCon US 2023](https://pycoders.com/link/11592/web)
    + October 16 to October 21, 2023

- [PyCon MEA & Data Science 2023](https://pycoders.com/link/11617/web)
    + October 16 to October 20, 2023

- [EduPy 2023](https://pycoders.com/link/11589/web)
    + October 21 to October 22, 2023







-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 546](https://weekly.pychina.org/issue/issue-546.html)
- 2021: [蠎周刊 493](https://weekly.pychina.org/issue/issue-493.html)
    + [pythonista-weekly : Pyw 520](https://weekly.pychina.org/python-weekly/pyw-520.html)
- 2020: [蠎周刊 440](https://weekly.pychina.org/issue/issue-440.html)
    + [pythonista-weekly : Pyw 470](https://weekly.pychina.org/python-weekly/pyw-470.html)
- 2019: [蠎周刊 389](https://weekly.pychina.org/issue/issue-389.html)
- 2018: [蠎周刊 338](https://weekly.pychina.org/issue/issue-338.html)
- 2017: [蠎加载 145](https://weekly.pychina.org/importpython/importpython-145.html)
- 2016: [蠎加载 94](https://weekly.pychina.org/importpython/importpython-94.html)
- 2015: [蠎周刊 187](https://weekly.pychina.org/issue/issue-187.html)
    + [蠎加载 53](https://weekly.pychina.org/importpython/importpython-53.html)
- 2014: [Issue 136](https://weekly.pychina.org/issue/issue-136.html)
- 2013: [Issue 88 ~ asyncio](https://weekly.pychina.org/issue/issue-88.html)
- 2012: 空缺


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + @Chaos42DAMA
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊





```
      _~-~∽~_
  \/ /  ◕ ♡  \ (/
    '_   △   _'
    \ '--+--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 598 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-598.html)
- 修订: [issue-598.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-598.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF598D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF598D4Q90XdDA7g):



```python
全职嗯哼: 大妈的多重宇宙 - https://www.youtube.com/@Chaos42DAMA
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开社群: 蟒营 (订阅号: Mainium)

as 创始组织者:
    CPyUG (mailling-list: python-cn@googlegroups.com)
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        AIGC珠海 

```

-------------



