Title: Issue 468
Slug: issue-468
Date: 2021-04-14 11:42
Tags: Weekly,Python,pycoders,ZH


> PyPy v7.3.4 发布ed


原文: [PyCoder's Weekly - Issue #468](https://pycoders.com/issues/468)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210414 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210414 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python 3 Types 在野外: 两种类型的系统的故事](https://pycoders.com/link/6112/web)
    + INGKARAT RAK-AMMOUTKIY ET AL.

This academic paper from researchers at the Rensselaer Polytechnic Institute and IBM TJ Watson Research Center examines the MyPy and PyType tools and explores how Python developers use type annotations. The researchers collected over 70,000 Python GitHub repositories and found that only 2,678 had Python 3-style type annotations, most of which fail to type-check with either of the two tools. The paper’s third section is quite accessible and has a lot of interesting analysis.

- [如何在 2021 年制作出色的 Python 程序包](https://pycoders.com/link/6126/web)
    + ANTON ZHIYANOV

The headache often associated with Python packaging is starting to fade away. Don’t believe me? Check out this step-by-step guide to creating and setting up a package repository. You’ll learn how to create a test package on [TestPyPI](https://pycoders.com/link/6124/web), create a [pyproject.toml](https://pycoders.com/link/6127/web) file with [flit](https://pycoders.com/link/6129/web), set-up linters and tests, GitHub Actions workflows, and more.

(`是也乎:`

无论 2021 还是 1842,
只有实用的认真的好的模块,
才可能 Awsome.

当然,
前提是已经在自己和小伙伴的工程中大规模使用了.

)





- [为 Python 开始贡献力量: 您的第一步](https://pycoders.com/link/6118/web)
    + REAL PYTHON

In this quick introduction, you’ll see how you can take your first steps toward contributing to Python. You’ll discover various ways you can contribute and get to know some of the resources that will help you along the way.

(`是也乎:`


![Contributing](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.20.15.jpg)

普通人参与 Python 社区贡献,
最简易的还是从文档贡献开始,
rST 是领先 Markdown 10多年的好东西,
值得使用.



)



- [用 pyenv 管理多个 Python 版本](https://pycoders.com/link/6130/web)
    + REAL PYTHON 
    + course

Learn how to install multiple Python versions and switch between them with ease, including project-specific virtual environments, with pyenv.

(`是也乎:`

![pyenv](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.19.00.jpg)

多版本多项目混合运行时环境管理,
真的没有 PyENV 这么自如的了.


)


- [PyCharm 2021.1 来了!](https://pycoders.com/link/6114/web)
    + JETBRAINS.COM 
    + • Shared by Bartosz Zaczyński

This release includes faster indexing, enhanced WSL 2 support, and an exciting new collaboration tool called Code With Me.

- [PDFx V1.4.1 已经可用](https://pycoders.com/link/6100/web)
    + METACHRIS.COM

PDFx is a tool to extract text, links, references, and metadata from PDF files and URLs. This release doesn’t include many new features but is rather a full update of the package repository to current Python standards, including testing and coverage, linting and static checks, GitHub workflows, and more.

- [Wing Python IDE 7.2.9 发布](https://pycoders.com/link/6125/web)
    + WINGWARE.COM

This release includes remote development for 64-bit Raspberry Pi, improved auto-closing of quotes, optimized change tracking, and more.


(`是也乎:`

这么古老的 IDE 还在努力...

![Wing](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.15.57.jpg)


为了象 VSCode 们而努力....

)


- [PyPy v7.3.4 发布ed](https://pycoders.com/link/6109/web)
    + PYPY.ORG

This release includes two interpreters supporting the syntaxes for Python 2.7 and 3.7.





-----------------------------------------
## 探讨/吐糟
> Discussions

- [为毛 Pandas None | True 返回 False 可 Python None or True 返回 True ?](https://pycoders.com/link/6104/web)
    + STACK OVERFLOW

| represents the “or” operation, but when used in a boolean index in Pandas, it doesn’t behave the same way as Python’s or as you might expect — if you go off of name alone. The | operator is a bitwise operator, which only works on integer values. In fact, one could say that Python doesn’t really have a true logical “or” operator, since technically or is a short-circuit operator.

(`是也乎:`

想不通哪想不通,

但是, 不影响日常使用,
就象为什么不用 { } 非要用缩进?

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 PyTorch + NumPy? 你误解了什么?](https://pycoders.com/link/6110/web)
    + TANEL PÄRNAMAA

There’s a subtle bug that’s easy to introduce when using these packages, and it’s likely that many projects suffer from the bug. The issue has to do with how data is loaded, pre-processed, and augmented in PyTorch. If your training pipeline is bottlenecked by data pre-processing, you might decide to load the data in parallel. The canonical way of achieving this results in identical augmentations and can lead to performance degradation, but there’s a way to fix the problem.


(`是也乎:`


嫑误解嫑误解...


)


- [Python 字典如何运作](https://pycoders.com/link/6120/web)
    + VICTOR SKVORTSOV

Dictionaries are an important part of Python — not just because Python programmers use them a lot, but also because they are used internally by the Python interpreter to run Python code. In this in-depth article, you’ll learn about hash tables and hash functions as well as how Python dictionaries work behind the scenes.



- [电脑视觉与刺绣](https://pycoders.com/link/6111/web)
    + ANDREW HEALEY

Andrew Healey’s wife wanted to find out what thread colors were used in some of the embroidery hoop images posted to the r/embroidery subreddit, so he embarked on a weekend project to solve the problem using the OpenCV computer vision library. Learn how he did it in this short, fun read, and then check out the source code over on his GitHub repository.


(`是也乎:`

![wife](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.16.51.jpg)

为了识别老婆的手艺...也是拼了

)


- [Python 代码重构入门](https://pycoders.com/link/6095/web)
    + REAL PYTHON 
    + podcast

Do you think it’s time to refactor your Python code? What should you think about before starting this task? Listen Brendan Maginnis and Nick Thapen from discuss Sourcery in this episode of the Real Python Podcast. Sourcery is an automated refactoring tool that integrates into your IDE and suggests improvements to your code.

(`是也乎:`

重构也是门手艺...

![podcast](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.11.41.jpg)

)



- [k最近邻/kNN 算法 在 Python](https://pycoders.com/link/6099/web)
    + REAL PYTHON

k-Nearest Neighbors (kNN) is a non-linear supervised machine learning algorithm suitable for both classification and regression problems. In this tutorial, you’ll learn all about the kNN algorithm in Python, including how to implement kNN from scratch, kNN hyperparameter tuning, and improving kNN performance using bagging.


(`是也乎:`


![kNN](http://ydlj.zoomquiet.top/ipic/2021-04-14-ScreenShot%202021-04-14%2010.10.18.jpg)


真蟒开始这种高价值教程了...


)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [superset: 数据可视化和数据探索平台](https://pycoders.com/link/6121/web)
    + GITHUB.COM/APACHE


(`是也乎:`

可以视为免费 BI 平台.

)


- [Python-Raytracer: 一种基本的 Ray Tracer/可利用 NumPy 数组和函数来快速工作](https://pycoders.com/link/6113/web)
    + GITHUB.COM/RAFAEL-FUENTE

- [layout-parser: 一个用于理解文档结构的Python库 ](https://pycoders.com/link/6105/web)
    + GITHUB.COM/LAYOUT-PARSER

- [jurigged: Python 的热重装](https://pycoders.com/link/6102/web)
    + GITHUB.COM/BREULEUX

- [github-actions-updater: 与 GitHub 的 Dependabot 类似/但适用于 GitHub Actions](https://pycoders.com/link/6123/web)
    + GITHUB.COM/SAADMK11 
    • Shared by Maksudul Haque

(`是也乎:`

gh-action 一出来,
就被挖矿党盯住了,
现在看马上要凉了...

)






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6116/web)
    + March 31, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

-[⋅ GeoPython 2021](https://pycoders.com/link/6119/web)
    + April 22 – 24, 2021



- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)



- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021



- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



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
- 首发: [Issue 468 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-468.html)
- 修订: [issue-468.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-468.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



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
>> NN 4341


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/468)






