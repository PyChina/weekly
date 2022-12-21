Title: PyCoder 556
Slug: issue-556
Date: 2022-12-21 11:42
Tags: Weekly,Python,pycoders,ZH


> 在 ChatGPT 中运行 Python


原文: [PyCoder's Weekly - Issue #556](https://pycoders.com/issues/556)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221221 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221221 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [在 Python 中使用构建系统和持续集成](https://pycoders.com/link/10051/web)
    + REAL PYTHON 
    + PODCAST

What advantages can a build system provide for a Python developer? What new skills are required when working with a team of developers? This week on the show, Benjy Weinberger from Toolchain is here to discuss the Pants build system and getting started with continuous integration (CI).

(`是也乎:`


![Integration](https://ipic.zoomquiet.top/2022-12-21-zshot%202022-12-21%2009.38.41.jpg)

又见 InfluxDB

)


- [PEP 701: F-Strings 的句法形式化](https://pycoders.com/link/10038/web)
    + PYTHON.ORG

This Python Enhancement Proposal describes the formalization of a grammar for f-strings, allowing a reduction in the underlying parser code complexity and providing future features like comments in multi-line f-strings.

(`是也乎:`

这样发展下去就变成闭包了
)


- [在 ChatGPT 中运行 Python](https://pycoders.com/link/10043/web)
    + RODRIGO GIRÃO SERRÃO 
    + • Shared by Rodrigo Girão Serrão

Did you know that ChatGPT knows Python? It knows Python so well, you can even run a Python REPL inside ChatGPT and it supports non-trivial features like decorators, properties, and asynchronous programming.

- [PyTexas 2023 提案征集](https://pycoders.com/link/10028/web)
    + PRETALX.COM

- [PyCon US 2023 注册启动](https://pycoders.com/link/10029/web)
    + PYCON.BLOGSPOT.COM


(`是也乎:`

PyCon中国 刚刚举行...

)



-----------------------------------------
## 探讨/吐糟
> Discussions




- [PyPI 升级到 Python 3.11 并将 CPU 占用减半](https://pycoders.com/link/10040/web)
    + TWITTER.COM/PYPI

(`是也乎:`

![Halved](https://ipic.zoomquiet.top/2022-12-21-zshot%202022-12-21%2009.35.49.jpg)

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [您可能没有听说过的 Python 魔术方法](https://pycoders.com/link/10056/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Python classes support operations through the definition of magic methods, also known as dunder-methods. To enable to support for len(), you define `__len__()` on your class. There are many Python magic methods, read on to learn about some of the less common ones.

(`是也乎:`


从作者官网中发现在这个有趣的图书:
[Elegant Objects](https://www.elegantobjects.org/)

)


- [用 SMT 求解器和模糊测试查找 JIT 优化器错误](https://pycoders.com/link/10030/web)
    + PYPY.ORG

Finding bugs can be a challenging exercise, but when your code is a Just-In-Time compiler, your bugs create bugs for other people. PyPy has recently added new techniques to find errors in the JIT optimizer. Dive deep into Z3 theory and using fuzzing to find errors.



- [测试 AWS Chalice 应用程序](https://pycoders.com/link/10053/web)
    + AUTH0.COM 
    + • Shared by Robertino

“AWS Chalice is a Python-based web micro-framework that leverages on the AWS Lambda and API Gateway services. It is used to create serverless applications.” Learn how to write unit and integration tests in the AWS Chalice space.


(`是也乎:`

Lambda 已经有了自己的专用框架 `Chalice` ,那么在此基础上的标准工程化操作也就应该有对应规范了...

)

- [在 Python 中使用类型提示的 8 个级别](https://pycoders.com/link/10048/web)
    + YANG ZHOU

This article introduces the reader to eight separate levels of type-hint use in Python, starting with annotating basic data types and going all the way up to compound and types for classes.

(`是也乎:`

周同学, 将 Type Hints 内卷姿势已经分好类了..


)


- [用 FastAPI 在 Python 中实现并发](https://pycoders.com/link/10036/web)
    + HORACE GUY

FastAPI is an asyncio friendly library, which means you can dive deep into your concurrency needs. This article shows you how to get high performance out of FastAPI using co-routines.

(`是也乎:`

简而言之 gunicorn YYDS

)


- [Django 领域驱动设计指南](https://pycoders.com/link/10050/web)
    + PHALT.GITHUB.IO

“This style guide combines domain-driven design principles and Django’s apps pattern to provide a pragmatic guide for developing scalable API services with the Django web framework.”


(`是也乎:`


**DDD** 也是可以应用万物的...

)


- [Guido van Rossum 访谈摘要](https://pycoders.com/link/10052/web)
    + DAVID CASSEL

In case you missed the three hour interview by Lex Fridman, or decided that it was a bit too long, this article summarizes key points.

(`是也乎:`

Summary 还是必要的...

)


- [上下文管理器和 Python 的 with 语句](https://pycoders.com/link/10039/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn what the Python with statement is and how to use it with existing context managers. You’ll also learn how to create your own context managers.


(`是也乎:`

![Context](https://ipic.zoomquiet.top/2022-12-21-zshot%202022-12-21%2009.19.31.jpg)

)

- [我从默认结对中学到了什么](https://pycoders.com/link/10057/web)
    + EVE RAGINS

Eve recently worked on a client site where pair programming was the default. She outlines the pros and cons of her experience and what she learned.


(`是也乎:`

结对编程之真实世界?

)

- [如何正确使用 Async Python](https://pycoders.com/link/10046/web)
    + GUI LATROVA 
    + • Shared by Gui Latrova

See some common mistakes when writing Python Async and learn how to avoid them to increase your code’s performance.






-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [Nuitka 优化 Python 编译器](https://pycoders.com/link/10055/web)
    + NUITKA.NET

(`是也乎:`

![Nuitka](https://ipic.zoomquiet.top/2022-12-21-zshot%202022-12-21%2009.13.19.jpg)

非常实用的项目,
> Nuitka 将 Python 模块翻译成 C 级程序，然后使用 libpython 和自己的静态 C 文件，以 CPython 的方式执行...目前支持:操作系统：Linux、FreeBSD、NetBSD、macOS X 和 Windows（32/64 位）...架构：x86、x86_64（amd64）和 arm，可能还有更多的架构

)


- [import-linter: 定义和执行导入规则](https://pycoders.com/link/10054/web)
    + GITHUB.COM/SEDDONYM

- [codon: 高性能、可扩展的 Python 编译器](https://pycoders.com/link/10035/web)
    + GITHUB.COM/EXALOOP

- [num2words: 将数字转换为单词。 42 –> 四十二](https://pycoders.com/link/10037/web)
    + GITHUB.COM/SAVOIRFAIRELINUX


(`是也乎:`

就这么实现了 `42` 好机智

```
$ num2words 10001
ten thousand and one
$ num2words 24,120.10
twenty-four thousand, one hundred and twenty point one
$ num2words 24,120.10 -l es
veinticuatro mil ciento veinte punto uno
$num2words 2.14 -l es --to currency
dos euros con catorce céntimos
```

暂时不支持中文

)

- [faqtory: 生成 GitHub 风格的 FAQ.md 文档](https://pycoders.com/link/10047/web)
    + GITHUB.COM/WILLMCGUGAN


(`是也乎:`

SSG 已经特化到只针对一个文件进行生成了?

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Python Web Conf 2023 (Virtual)](https://pycoders.com/link/10033/web)
    + March 13 to March 17, 2023

- [An Introduction to Model Drift](https://pycoders.com/link/10034/web)
    + December 21, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10027/web)
    + December 21, 2022

- [Heidelberg Python Meetup](https://pycoders.com/link/10044/web)
    + December 21, 2022

- [XtremePython 2022](https://pycoders.com/link/10041/web)
    + December 27 to December 28, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 556 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-556.html)
- 修订: [issue-556.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-556.md)


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

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF556D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF556D4Q90XdDA7g):



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





