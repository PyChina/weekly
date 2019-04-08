Title: Issue 360
Slug: issue-360
Date: 2019-03-21 17:17
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #360](https://pycoders.com/issues/360)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [如何使用 wxPython 构建 Python GUI 应用](https://pycoders.com/link/1244/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn how to create a cross-platform graphical user interface (GUI) using Python and the wxPython toolkit. A graphical user interface is an application that has buttons, windows, and lots of other widgets that the user can use to interact with your application.



- [简化您的 Python 开发环境](https://pycoders.com/link/1245/web)
    + MASON EGGER • Shared by Mason Egger

How three tools (pyenv, pipx, pipenv) make for smooth, isolated, reproducible Python developer and production environments.

(`是也乎:`

这,是非常重要的常用嗯哼哪...

只是, 一点儿也不简单..因为 Python 中一直就没有一个合理的工具一致性解决所有阶段的开发环境问题:

    本地开发时的版本和模块依赖管理
    测试时高速部署依赖模块
    运行时自动化同步版本和依赖模块版本

Docker 是一把将所有阶段的环境问题用虚拟机解决了,
只是带来空间无法控制, 以及必须理解并忍受越来越多的专用工具;

所以, 先用已有工具组合为一个合理可理解的工具箱来完成是好的:

    pyenv 进行本地/测试/生产 的运行时版本和模块依赖树隔离
    在 pyenv 之下..
        conda 负责部分大型编译型模块的预编译管理
        pipenv 进行模块的依赖/版本管理

嗯哼, 就是缺少一环:

    可以高速冻结本地模块依赖树, 
    并能自动化同步模块树镜像到任意指定主机上;
    以便从本地安装模块,而不依赖可怜的墙外网速...

> 再次感叹: dh-virtualenv, 已经解决了这一环的问题...
>> 可惜...Debain only ...

)


- [当 C扩展 崩溃时:更轻松来调试](https://pycoders.com/link/1226/web)
    + ITAMAR TURNER-TRAURING


Learn how to prepare for crashes in advance, so when they do occur you can quickly figure out which part of the codebase caused them: The standard library's faulthandler, verbose test runs, package listing, and catchsegv on Linux.

- [为什么 Operators 很有用](https://pycoders.com/link/1230/web)
    + GUIDO VAN ROSSUM • Shared by Ricky White

Latest blog post from Guido, related to the recent discussion about Python getting + and - operators for merging dictionaries (PEP 584).

(`是也乎:`

老爹叕发声挺新嗯哼了...

)


- [Python Decorators 101](https://pycoders.com/link/1242/web)
    + REAL PYTHON video

See step-by-step what Python decorators are and how you can use them to make your own code more Pythonic and expressive.

(`是也乎:`

![...](https://ipic.zoomquiet.top/2019-03-23-ScreenShot%202019-03-23%2009.46.29.jpg)

哈, 形式都一致...

)


- [Python 中元组排序和深度比较](https://pycoders.com/link/1232/web)
    + TREY HUNNER • Shared by Ricky White

Nice deep dive on comparison operators in Python.

- [urllib CRLF 注入漏洞](https://pycoders.com/link/1233/web)
    + PYTHON.ORG

The current Python 2.x and 3.x implementation of urllib does not encode the \r\n sequence in the query string, which allows an attacker to manipulate a HTTP header with the \r\n sequence in it, so the attacker can insert arbitrary content to the new line of the HTTP header.

(`是也乎:`

也就是说尽可能别用? 还是 cURL 之类老牌工具靠谱...

)


- [还俺的 Monolith](https://pycoders.com/link/1243/web)
    + CRAIG KERSTIENS opinion

"It feels like we're starting to pass the peak of the hype cycle of microservices." Interesting counterpoint to the "everything should be broken down into microservices" hypetrain. Not Python-specific, but worth a read nonetheless.

(`是也乎:`

>> If we can't debug them, maybe we can test them

微服务这波大嗯哼, 
回味一下, 非常象当年 GNU 投入所有力量来开始灵活/美好/简洁的微内核 OS ,
结果统一 自由/开源软件世界的, 是名大3学生开发的巨核 OS...

)

## 讨论
> Discussions

- [Guido 解释为什么 Python 的索引用 0开始](https://pycoders.com/link/1218/web)
    + GOOGLE.COM

Google Plus is shutting down soon, so here's a final hurrah.

(`是也乎:`

[I was asked on Twitter why Python uses 0\-based indexing,...](https://plus.google.com/115212051037621986145/posts/YTUxbXYZyfi)

老爹当年也很是积累使用 G+ 的,
公开回答了很多价值问题...
能看一眼少一眼了...

简单说, 就是为了切片时的语义合理性...

)

- [There Are Some Huge Speedups in Python 3.8. Will They Also Be Put Into the Older Versions?](https://pycoders.com/link/1219/web)
    + REDDIT



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [理解 Python Mock 对象库](https://pycoders.com/link/1256/web)
    + REAL PYTHON

In this tutorial, you'll learn how to use the Python mock object library, unittest.mock, to create and use mock objects to improve your tests. Obstacles like complex logic and unpredictable dependencies make writing valuable tests difficult, but unittest.mock can help you overcome these obstacles.

(`是也乎:`

![...](https://ipic.zoomquiet.top/2019-03-23-ScreenShot%202019-03-23%2009.28.10.jpg)

别的不说, 真蟒 的插图是非常走心的...

PS: 官网图片都是 webp 的了, 下载了根本没法直接看...

)

- [如何将 Mathematical 算法变成: TF-IDF 到 Python](https://pycoders.com/link/1247/web)
    + SILKE HENDERICKX • Shared by Silke Henderickx

Does your brain short-circuit when you see a mathematical algorithm? Don't worry, you're not alone. In this post you'll see how the author worked her way through an algorithm, namely TF-IDF, and got it up and running in Python. Nice writeup!

(`是也乎:`

为什么不直接来 MMA ?

)

- [10 个 Python 图像处理工具](https://pycoders.com/link/1220/web)
    + PARUL PANDEY

Nice overview of Python libraries that provide an easy and intuitive way to transform images and make sense of the underlying data.

(`是也乎:`

正如 RANA 老了, 图形图像处理这方面, 也已经很多年没什么新嗯哼了


)


- [用 Python 生成 LaTeX 论文的技巧](https://pycoders.com/link/1224/web)
    + VINCENT ETTER

Some nice tips and example code for writing scientific papers in LaTeX, with figures generated in Python.

(`是也乎:`

正如那位手打 1700+页课堂笔记的学生一样, 
这种事儿用个可定制 Editor 来的更快...

)


- [让 Python 定期删除不需要的电子邮件](https://pycoders.com/link/1257/web)
    + UDIT VASHISHT • Shared by Udit Vashisht

How to use the Gmail API to create a Python script which will automatically search & delete the messages matching your query.

(`是也乎:`

Gmail 积累这么多年, 再傻的 PM 也应该掌握人类最强 SPAM 识别库了,
只是, 对于我们是不存在的嗯哼...

)


- [Python's except Quirk](https://pycoders.com/link/1236/web)
    + ALEX BECKER

I don't know how Alex comes up with these, but that's a fun one :)

- [如何分发 wxPython 应用程序](https://pycoders.com/link/1248/web)
    + MIKE DRISCOLL

You finished up a wonderful GUI application using wxPython. How do you share it with the world? Read Mike's article to find out.

(`是也乎:`

wx 哪,,,很多年没见过有什么消息了, Electorn 以及 Flutter 们将统一桌面吧?

)


- [Django: 一个非官方 FAQ 集锦](https://pycoders.com/link/1234/web)
    + KRISTIAN GLASS

- [Python 标准库 Gems: collections.Counter](https://pycoders.com/link/1249/web)
    + IVAN SAGALAEV

- [How to Use Grouping Sets in Django](https://pycoders.com/link/1231/web)
    + HAKI BENITA

"How we cut a heavy admin dashboard response time in half with advanced SQL and some Django hackery."


## 好物
> Interesting Projects, Tools and Libraries


- [OWASP/CheatSheetSeries: High Value Information on Specific Application Security Topics](https://pycoders.com/link/1240/web)
    + GITHUB.COM/OWASP

(`是也乎:`

![...](https://github.com/OWASP/owasp-swag/raw/master/projects/cheat-sheet-series/owasp-1.png)

作弊条也可以变成流行嗯哼...

)


- [orm: An Async ORM](https://pycoders.com/link/1254/web)
    + GITHUB.COM/ENCODE

(`是也乎:`

**encode/orm** 这个项目名非常好哪...

支持 Postgres, MySQL, and SQLite.
非常早期, 嵌合多个成熟模块组合成的新工具.

)

- [namedzip: Extends zip() and itertools.zip_longest() to Generate Named Tuples](https://pycoders.com/link/1255/web)
    + GITHUB.COM/ERBERLIN



- [transistor: A Python Web Scraping Framework for Structured Web Pages](https://pycoders.com/link/1227/web)
    + GITHUB.COM/BOMQUOTE

(`是也乎:`

叕一 Scrapper

)

- [instaviz: Instant Visualization of Python AST and Code Objects](https://pycoders.com/link/1258/web)
    + ANTHONY SHAW

(`是也乎:`

![...](https://github.com/tonybaloney/instaviz/raw/master/screenshot.png)

可视化 AST ... Graphviz 无处不在...
)


## 📆🐍 活动/大会
> Events



- [⋅ PyData Bristol Meetup](https://pycoders.com/link/1246/web)
    + 英国 March 21, 2019
- [⋅ Python Northwest](https://pycoders.com/link/1241/web)
    + 斯洛伐克 March 21, 2019
- [⋅ PyLadies Dublin](https://pycoders.com/link/1235/web)
    + 德国大妈...March 21, 2019
- [⋅ IndyPy Automate Conf 2019](https://pycoders.com/link/1228/web)
    + FISHER USA March 22 -> March 23, 2019
    + 讨论 IoT 的 Python 嗯哼

![indypy](https://2019.indypy.org/static/images/logo.png)

- [⋅ PyCon SK 2019](https://pycoders.com/link/1238/web) 
    + 斯洛伐克 March 22 -> March 25, 2019
- [⋅ Inland Empire Pyladies (CA, USA)](https://pycoders.com/link/1252/web)
    + March 25, 2019



## DAMA
> ❤️ Happy Pythonic!

(`大妈私人无责任播报`)

- [元初 \- 101\.camp](https://101.camp/story/0_originating/)
    + 嗯哼...

# 是也乎

- 190321 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190321 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
