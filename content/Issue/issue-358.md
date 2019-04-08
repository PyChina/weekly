Title: Issue 358
Slug: issue-358
Date: 2019-03-06 10:01
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #358](https://pycoders.com/issues/358)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------


- [PEP 584: 在内置 Dict 类中添加+和 - 运算符](https://pycoders.com/link/1124/web)
    + PYTHON.ORG

This PEP suggests adding merge + and difference - operators to the built-in dict class. The merge operator will have the same relationship to the dict.update method as the list concatenation operator has to list.extend, with dict difference being defined analogously. I think this is a pretty cool feature suggestion. Related discussion here.

(`是也乎:`

简单说, 用直觉计算符号来操作最常用的 dict 对象...

    >>> d = {'spam': 1, 'eggs': 2, 'cheese': 3}
    >>> e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
    >>> d + e
    {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
    >>> e + d
    {'cheese': 3, 'aardvark': 'Ethel', 'spam': 1, 'eggs': 2}

)


- [重构Python应用程序以实现简单性](https://pycoders.com/link/1122/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn how to refactor your Python application to be simpler and more maintainable and have fewer bugs. You'll cover code metrics, refactoring tools, and common anti-patterns.

(`是也乎:`

以往也总是搜索出来 realpython 的文章,
这次挖掘了一下, 发现真心是好公司, 文章扎实, 配图可爱...

)

- [在 Django 中管理 Elasticsearch](https://pycoders.com/link/1147/web)
    + HARSH BHIMJYANI • Shared by Harsh Bhimjyani

A small tutorial on how to manage Elasticsearch efficiently in a Django project. It uses elasticsearch-dsl as an ORM and a custom management system similar to django-haystack (which uses outdated ES).

(`是也乎:`

Django 的生态终于直接扎入搜索了...

)

- [pydis: Python 3 的 Redis 克隆/以反驳一些关于性能的错误](https://pycoders.com/link/1143/web)
    + GITHUB.COM/BORAMALPER

An experiment to disprove some of the falsehoods about performance and optimisation regarding software and interpreted languages in particular. In short, this is a Redis clone, written in < 250 lines of idiomatic Python code, providing a subset of Redis' functionality for which there are official benchmarks. Pydis is ~60% as fast as the compiled C version of Redis, as measured in number of operations per second.

(`是也乎:`

250行以内作品, 来证明解释型语言可以比肩 C...
只是, 数量级呢?


)


- [Python Bytes Episode 119 录制于 Seattle 的 PyCascades](https://pycoders.com/link/1152/web)
    + PYTHON BYTES podcast

Together with Trey Hunner and Eric Chou, I was a guest on Mike and Brian's excellent Python Bytes podcast. We recorded this episode "live" and together in the same room at the PyCascades conference in Seattle.


- [EditorConfig: 在不同的编辑器和 IDE 之间保持编码样式的一致](https://pycoders.com/link/1120/web)
    + EDITORCONFIG.ORG

This is super handy if you're switching between editors or if you want to make sure your team uses the same indentation settings no matter which editor each developer uses.

(`是也乎:`

等等...为毛哪...一个团队统一编辑器是反人权?

)

## 讨论
> Discussions


- [Python Multiprocessing: 了解 chunksize 背后的逻辑](https://pycoders.com/link/1132/web)
    + STACK OVERFLOW • Shared by Christian Long

An amazing, thorough, readable answer on Stack Overflow about the multiprocessing module.

(`是也乎:`

SO 中神品回答:

![7nT9z.png(PNG 图像,712x417 像素)](https://i.stack.imgur.com/7nT9z.png)


![githubusercontent](https://user-images.githubusercontent.com/32203938/53185266-f337da80-35fe-11e9-9eb6-0b04f35a5263.gif)


甚至于制作了内存分析动画...镇住了其它回答

)


- [有用的 Python 技巧](https://pycoders.com/link/1159/web)
    + REDDIT

"What are some cool uses for Python for maybe younger people or just people without office jobs in general?"

(`是也乎:`

针对 OL 的?
)


- [from mylibrary import * 😉](https://pycoders.com/link/1140/web)
    + TWITTER.COM/REALPYTHON

(`是也乎:`
没毛病

![Dy46_opW0AARDM1.jpg(JPEG 图像,1080x1098 像素) - 缩放 (82%)](http://101.zoomquiet.top/res/geek/Dy46_opW0AARDM1.jpg?imageView2/2/w/420)


)

## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [使用 Python 进行传统人脸检测](https://pycoders.com/link/1114/web)
    + REAL PYTHON

In this article on face detection with Python, you'll learn about a historically important algorithm for object detection that can be successfully applied to finding the location of a human face within an image.

(`是也乎:`

等等, 有非传统的?

)


- [如何编写 Python Web 框架 - 第三部分](https://pycoders.com/link/1134/web)
    + JAHONGIR RAHMONOV

The third post of the series where you'll be writing our own Python framework just like Flask and Django.

(`是也乎:`

叕一系列分享如何 造轮子,
但是,很多领域不自己造一遍, 永远不知道有什么具体坑的...

)


- [Python 怪癖:隐式回归](https://pycoders.com/link/1141/web)
    + PHILIP TRAUNER

Python functions always have to return something, right? Well, it's complicated... 

- [VS Code 为 Python 添加带自动发现的新测试资源管理器](https://pycoders.com/link/1113/web)
    + DAN TAYLOR

Pretty cool: This release includes the ability to visualize, navigate and run unit tests through a visual test explorer. Supports unittest, pytest and nose.


- [Python 安全最佳实践备忘单](https://pycoders.com/link/1145/web)
    + SNYK.IO

Covers some best practices for securely using Python.

- [Bleach: 维护者下台自述](https://pycoders.com/link/1115/web)
    + WILL KAHN-GREENE

Bleach is a Python library for sanitizing and linkifying text from untrusted sources for safe usage in HTML. In this post the author explains why he's stepping down as a maintainer for the library and gives a retrospective on OSS project maintenance.


(`是也乎:`

> ...It's so crazy what browsers are doing
> ...20年维护经验的结论: continuing to maintain something because of internal obligations long after they're getting any value from the project.
>> 所有维护者都在最初获益后, 义务嗯哼了很多很多年. 
> ...PyCon 2019 maintainers summit



)


- [Contributing to Classiness (In Django)](https://pycoders.com/link/1163/web)
    + JAMES BENNETT

Django's contribute_to_class() is an undocumented part of the ORM's internal API that allows you to attach to/hook into a model.



- [理解 Python Slices](https://pycoders.com/link/1121/web)
    + REUVEN M. LERNER • Shared by Reuven M. Lerner

"Slices are both common and convenient ways to extract portions of Python data structures — usually with builtin objects, but also on your own. Once you get used to slices, you'll see lots of uses for them, and wonder how you got along without them."

(`是也乎:`

常用, 也难用...甚至到 Pandas 也一样
)

- [重温PEP 394:类Unix系统上的"python"命令](https://pycoders.com/link/1153/web)
    + JAKE EDGE

With the uptake of Python 3 (and the imminent end of life for Python 2.7), there is a question of which version of Python a user should get when they type "python" at the command line or have it as part of a shebang ("#!") line in a script.

- [我与 Python / Django 社区](https://pycoders.com/link/1125/web)
    + PAOLO MELCHIORRE

Paolo is an open-source contributor to Django. In this article he talks about his involvement in the Python community, how he got started using Python in the first place, and how he ended up contributing to the Django web framework.

(`是也乎:`

相比公司, 社区总是能更好的加速个人成长...
当然, 前提是....嗯哼

)


- [使用 Azure 工件托管私有 Pip 包](https://pycoders.com/link/1142/web)
    + ZEROWITHDOT.COM

Marry science code with operations? How to organize your Python code as private Pip package with Azure Artifacts and integrate it using modified virtual environments.



## 好物
> Interesting Projects, Tools and Libraries

- [subsync: Automagically Synchronize Subtitles With Video](https://pycoders.com/link/1139/web)
    + GITHUB.COM/SMACKE

(`是也乎:`

利用 FFmpeg 来协助分析帧, 并对齐字幕
)


- [Python-Prolog-Interpreter: Mini-Prolog Interpreter Written in Python 3](https://pycoders.com/link/1160/web)
    + GITHUB.COM/PHOTONLINES

(`是也乎:`

嗯哼? 又模拟 Prolog? 为毛?
)


- [Hy: A Lisp Dialect Embedded in Python](https://pycoders.com/link/1157/web)
    + HYLANG.ORG


(`是也乎:`

嗯哼? 叕一个 Lisp 嵌入?
哈, 之前报道过,只是在生产中无人使用.
)

- [accessify: Python Class Members Accessibility Levels (Private, Protected)](https://pycoders.com/link/1149/web)
    + GITHUB.COM/DMYTROSTRILETSKYI


- [automat: Self-Service Finite-State Machines for the Programmer on the Go](https://pycoders.com/link/1123/web)
    + GITHUB.COM/GLYPH

- [codebraid: Live Code in Pandoc Markdown (Python, Julia, Rust, R)](https://pycoders.com/link/1165/web)
    + GITHUB.COM/GPOORE • Shared by Geoffrey Poore

(`是也乎:`

叕一个 Jupter 增强方向

)

- [lazynlp: Scrape and Clean Web Pages to Create Massive Monolingual Datasets](https://pycoders.com/link/1144/web)
    + GITHUB.COM/CHIPHUYEN

(`是也乎:`

    git+https://github.com/jaybaird/python-bloomfilter/
    justext
    unidecode
    tldextract
    requests

依赖很少

)

- [pygram11: Simple and Fast Histogramming in Python via Pybind11 (C++ Interop) and OpenMP](https://pycoders.com/link/1136/web)
    + GITHUB.COM/DRDAVIS

- [pytest-azurepipelines: Formatting PyTest Output for Azure Pipelines UI](https://pycoders.com/link/1162/web)
    + PYPI.ORG

(`是也乎:`

Azure 越来越积累了...

)


## 📆🐍 活动/大会
> Events

- [Reunión Python Valencia](https://pycoders.com/link/1131/web)
    + March 7, 2019
    + 瓦伦西亚...
- [Canberra Python Meetup](https://pycoders.com/link/1117/web)
    + March 7, 2019
    + 堪培拉...
- [Sydney Python User Group (SyPy)](https://pycoders.com/link/1155/web)
    + March 7, 2019
    + 悉尼...这是叫劲儿?
- [Python Miami](https://pycoders.com/link/1129/web) 
    + March 9 to March 10, 2019
    + 又是美国的
- [Leipzig Python User Group Meeting](https://pycoders.com/link/1138/web)
    + March 12, 
    + 德国中部城市
- [TuPLE (Tucson Python Language Enthusiasts)](https://pycoders.com/link/1137/web)
    + March 12, 2019
    + 美国 Arizona 州的...



## DAMA
> ❤️ Happy Pythoning!

(`大妈私人无责任播报`)

过年前后断更了几期, 对比之前坚持,
感觉, 类似技术周刊的翻译, 还是值得的:

- 保持原文阅读量, 语言就是得用, 否则嗯哼了...
- 保持最新嗯哼接触面, 其它技术媒体先不论翻译水平, 光是第2/3/4 手资料传播过程中的损耗...唉
    + 光知道自己不知道什么, 就非常值得了
- 积累自己的内容池...社会资产, 就是这么慢慢嗯哼起来的



# 是也乎

- 190306 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190306 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
