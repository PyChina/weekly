Title: Issue 472
Slug: issue-472
Date: 2021-05-12 11:42
Tags: Weekly,Python,pycoders,ZH


> Github 中那些最佳实践+良好架构的项目


原文: [PyCoder's Weekly - Issue #472](https://pycoders.com/issues/472)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210512 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210512 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [寻求更快的 Python](https://pycoders.com/link/6297/web)
    + TIM ANDERSON

There seems to be a lot going on in the Python JIT compiler space. Facebook recently open-sourced Instagram’s Cinder runtime, Pyston 2 returned as an open-source project, and the Pyjion project from Microsoft continues to grow. But Python creator Guido van Rossum has suggested that Python developers in need of more performance should consider writing parts of their code as C extensions, or use the PyPy runtime. This article explores Pythons turbulent history with performance optimization.


(`是也乎:`

对运行时性能的追求,
在 Python 宇宙引发了一系列有益的动荡...

)


- [性能如何成为安全 Python 代码的克星](https://pycoders.com/link/6288/web)
    + DIMA KOTIK

While JIT compilers compete for Python performance improvements and some teams rush into asyncio adoption, one has to wonder what the outcome of additional complexity will be. This opinion piece argues that the cost of hurried and potentially unnecessary performance optimization is unstable and insecure code. It’s a good reminder that decisions about project dependencies should be thoroughly researched and made deliberately.

(`是也乎:`

高级语言的宿命

)


- [堆栈和队列: 选择理想的数据结构](https://pycoders.com/link/6285/web)
    + REAL PYTHON 
    + course

Learn about three of Python’s data structures: stacks, queue and priority queues. You’ll look at multiple types and classes for all of these and learn which implementations are best for your specific use cases.

- [德州仪器/TI 将发布使用 Python 的新型 TI-84 计算器](https://pycoders.com/link/6292/web)
    + TI.COM

- [EuroPython 2021 征集提案的时间延长至5月16日](https://pycoders.com/link/6273/web)
    + EUROPYTHON.EU


- [Pylance 现在是 VS Code 的默认 Python 语言服务器](https://pycoders.com/link/6298/web)
    + MICROSOFT.COM

(`是也乎:`

反正和官方的不同,
怪不得最好使用另外的运行时...

)




-----------------------------------------
## 探讨/吐糟
> Discussions


- [您是否将Python控制台和Python数学库用作计算器?](https://pycoders.com/link/6299/web)    
    + REDDIT

With Python installed, you’ve got a quick and easy-to-use calculator accessible from any terminal window!


(`是也乎:`

Never, 直到有 Jupyter 后...

)


- [Github 中有哪些 Python 项目是最佳实践+良好架构的示例](https://pycoders.com/link/6289/web)
    + REDDIT

This Reddit thread is full of GitHub repos that might make for some good code reading.

(`是也乎:`

这可能是价值最高的一则讨论了...

[thuijskens/production\-tools: A bare\-bones repository demonstrating how to set up tools for data science projects that will help you write higher quality code\.](https://github.com/thuijskens/production-tools)

[psf/requests: A simple, yet elegant HTTP library\.](https://github.com/psf/requests)

[Design Patterns in Python](https://refactoring.guru/design-patterns/python)


[The Architecture of Open Source Applications](http://aosabook.org/en/index.html)

[Reading Great Code — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/reading/)

[API Evolution the Right Way](https://emptysqua.re/blog/api-evolution-the-right-way/)

![Evolution](http://ydlj.zoomquiet.top/ipic/2021-05-12-ScreenShot%202021-05-12%2010.40.28.jpg)


[cosmicpython/code: Example application code for the python architecture book](https://github.com/cosmicpython/code)


)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 Python 的 NLTK 软件包进行自然语言处理](https://pycoders.com/link/6271/web)
    + REAL PYTHON

In this beginner-friendly tutorial, you’ll take your first steps with Natural Language Processing (NLP) and Python’s Natural Language Toolkit (NLTK). You’ll learn how to process unstructured data in order to be able to analyze it and draw conclusions from it.


(`是也乎:`


![NLP](http://ydlj.zoomquiet.top/ipic/2021-05-12-ScreenShot%202021-05-12%2010.35.32.jpg)

NLTK 应该是最易用的 NLP 处理模块了.


)


- [流利的 Django: 更好理解 Django 模型](https://pycoders.com/link/6290/web)
    + GIRLTHATLOVESTOCODE 
    + • Shared by GirlThatLovesToCode

Django models are the single, definitive source of information about data in a Django application. That means that all the logic about your data should be located in the model—not in a view as too often can be seen. In this article, you’ll get to know Django models better including things like UUID fields, enumeration types, Meta classes, and custom .save() methods.

(`是也乎:`


Fluent 是这两年热门词.

)


- [FastAPI 和 Celery 的异步任务](https://pycoders.com/link/6302/web)
    + MICHALE HERMAN 
    + • Shared by Michael Herman

Many web apps require long-running tasks, such as resizing image thumbnails or generating PDFs. Background tasks allow a web app to continue to process incoming requests while a task is executing. This tutorial walks you through setting up Celery and Redis to handle background tasks in a FastAPI application. You’ll learn how to containerize everything with Docker, save Celery logs to files, and monitor background tasks with Flower.

(`是也乎:`

FastAPI 替代 Flask 成为新的网红...

)



- [Python 中的递归/简介](https://pycoders.com/link/6293/web)
    + REAL PYTHON

In this tutorial, you’ll learn about recursion in Python. You’ll see what recursion is, how it works in Python, and under what circumstances you should use it. You’ll finish by exploring several examples of problems that can be solved both recursively and non-recursively.


(`是也乎`:


![Recursion](http://ydlj.zoomquiet.top/ipic/2021-05-12-ScreenShot%202021-05-12%2010.33.43.jpg)

递归是最烧脑, 又最简洁的循环形式了.


)


- [Bite My Shiny, 带类型注释的库!](https://pycoders.com/link/6277/web)
    + JUGMAC00.GITHUB.IO 
    + • Shared by Jürgen Gmach

If you’re a package maintainer and want to make type annotations available to all users of your library, how can you go about doing this? Just add the type annotations to your library, right? Well, no! Learn how type annotations are handled in package distributions in this short but informative article with links to a number of helpful resources.

- [我忘记了拼写检查](https://pycoders.com/link/6278/web)
    + VICTOR SHEPELEV

Throughout 2020, Victor Shepelev worked on porting the 
[hunspell](https://pycoders.com/link/6296/web) spellchecker to Python in a project called spylls. In this post he shares his thoughts on 
[spylls](https://pycoders.com/link/6286/web) checking, noting that it is much more difficult than just comparing strings to an established dictionary. While the article is not technical, it’s a great read exploring some of the assumptions made by hunspell and how they fail in the real world.

(`是也乎:`

少有的分享失败经历的文章

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [pudb: 适用于 Python 的全屏控制台调试器](https://pycoders.com/link/6301/web)
    + GITHUB.COM/INDUCER

(`是也乎:`


![pudb](http://ydlj.zoomquiet.top/ipic/2021-05-12-ScreenShot%202021-05-12%2010.27.44.jpg)


多熟悉的布局哪,
简直就是 Vim 的再造.

)


- [cinder: Instagram 基于性能的 CPython 分支](https://pycoders.com/link/6291/web)
    + GITHUB.COM/FACEBOOKINCUBATOR

(`是也乎:`

是的,  Python 是开源的,
如果真心不满意运行时效率, 
随时可以自行 fork 加强的.

)


- [zxpy: 使 Shell 脚本变得简单](https://pycoders.com/link/6303/web)
    + GITHUB.COM/TUSHARSADHWANI

- [typeshed: Collection of Library Stubs for Python, With Static Types](https://pycoders.com/link/6304/web)
    + GITHUB.COM/PYTHON

- [flower: Celery 分布式任务队列的实时监控器和 Web Admin](https://pycoders.com/link/6276/web)
    + GITHUB.COM/MHER

- [reviews:终端UI仪表板，用于监视代码审阅请求](https://pycoders.com/link/6295/web)
    + GITHUB.COM/APOCLYPS 
    + • Shared by kyle harrison

(`是也乎:`

![reviews](http://ydlj.zoomquiet.top/ipic/2021-05-12-ScreenShot%202021-05-12%2010.22.28.jpg)

为什么大家都在 CLI 中折腾,
却不愿意在原生桌面上发布复杂的面板?

可以认为 MFC 立功了,
没人愿意将有限的精力投入到无限的隐藏接口挖掘上.

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6294/web)
    + April 28, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021


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
- 首发: [Issue 472 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-472.html)
- 修订: [issue-472.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-472.md)


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
>> NN 4376


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/472)






