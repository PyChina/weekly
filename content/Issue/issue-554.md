Title: PyCoder 554
Slug: issue-554
Date: 2022-12-07 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 和未来的编程 ~ 老爹3小时访谈


原文: [PyCoder's Weekly - Issue #554](https://pycoders.com/issues/554)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221207 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221207 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [使用 Python 的 pathlib 模块](https://pycoders.com/link/9966/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to effectively work with file system paths in Python 3 using the pathlib module in the standard library.

- [comprehensions 和 generators 速成班](https://pycoders.com/link/9975/web)
    + PETE FISON 
    + • Shared by Pete FIson

A great collection of code snippets that showcase the power and flexibility of list comprehensions, generators and related constructs.



- [Guido van Rossum: Python 和编程的未来](https://pycoders.com/link/9959/web)
    + LEX FRIDMAN 
    + PODCAST

An in-depth, 3 hour interview with Guido van Rossum by Lex Fridman.






-----------------------------------------
## 探讨/吐糟
> Discussions



- [PEP 683: 不朽对象，使用固定的 Refcount](https://pycoders.com/link/9980/web)
    + PYTHON.ORG

Currently all CPython objects have some memory allocated to maintain state, even those that are immutable. PEP 683 proposes “Immortal Objects” and this thread discusses the proposal.






- [Python 能做什么而 R 不能的?](https://pycoders.com/link/9984/web)
    + REDDIT

(`是也乎:`

好问题,其实对等问题也存在...

)




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 中的 Multiprocessing 竞争条件](https://pycoders.com/link/9982/web)
    + JASON BROWNLEE

A race condition happens when parallel tasks attempt to execute code at the same time and the results are dependent on order of execution. Finding race conditions can be challenging, this article gives some hints as to how to find the different kinds of race conditions when coding with the multiprocessing module.

- [准备数据以衡量 ML 模型性能](https://pycoders.com/link/9960/web)
    + REAL PYTHON 
    + PODCAST

How do you prepare a dataset for machine learning (ML)? How do you go beyond cleaning the data and move toward measuring how the model performs? This week on the show, Jodie Burchell, developer advocate for data science at JetBrains, returns to talk about strategies for better ML model performance.

(`是也乎:`

![ML](https://ipic.zoomquiet.top/2022-12-07-zshot%202022-12-07%2009.17.29.jpg)

)



- [如何使用 Python 获取目录中所有文件的列表](https://pycoders.com/link/9961/web)
    + REAL PYTHON

In this tutorial, you’ll be examining a couple of methods to get a list of files and folders in a directory with Python. You’ll also use both methods to recursively list directory contents. Finally, you’ll examine a situation that pits one method against the other.

(`是也乎`:

传统艺能...

![Directory](https://ipic.zoomquiet.top/2022-12-07-zshot%202022-12-07%2009.16.14.jpg)

)



- [Python 类型提示: parsy 案例研究](https://pycoders.com/link/9958/web)
    + LUKE PLANT

This deep article talks about Luke’s journey to try to add type checking and why he often gives up. It walks through what was needed to add types to parsy, one of the libraries he maintains and how it compared to other similar libraries.

(`是也乎:`

深入分析类型提示在实际使用过程中,为什么经常放弃...

)


- [用 update_fields 保存以获得更好的 Django 性能](https://pycoders.com/link/9970/web)
    + REDOWAN DELOWAR

The update_fields argument to the .save() call restricts the underlying SQL to just the named fields. For some conditions this can mean a performance boost. This article shows where it can be helpful and when it might lead to bugs.

- [应该在下一个项目中使用的 7 个有用的 Python 库](https://pycoders.com/link/9979/web)
    + FARHAN TANVIR

This article introduces you to 7 useful Python libraries: PySnooper, schedule, MechanicalSoup, ftfy, rpyc, pyglet, and rope. Read on to learn how these can help you with your next project.




- [Python Linter 比较 2022](https://pycoders.com/link/9963/web)
    + AL SWEIGART

There are many linter choices for Python, this article covers a lot of them: Pylint, Pyflakes, Flake8, autopep8, Bandit, Prospector, Pylama, Pyroma, Black, Mypy, Radon, and mccabe.

(`是也乎:`

理论上应该是官方出的最靠谱,
但是,看市场反应,还是UX 作的好的为先?

)


- [开发人员的 Mastodon 机会](https://pycoders.com/link/9955/web)
    + ANDY PIPER

As the article starts: “There’s a lot of interest in Mastodon at the moment, For Reasons.” This article talks about how to play with the Mastodon API to embed content.

(`是也乎:`

Mastodon ~ 又一种 IM 平台,每一种平台发布时,
都宣布过自己是最靠谱的开发社交平台...

)


- [Python 和 .NET，行进中的传奇](https://pycoders.com/link/9974/web)
    + NIKOS VAGGALIS

Python.NET has released a new version, so Nikos has written an article that explores the history of Microsoft, .NET, and Python including the state of Iron Python.

(`是也乎:`

.NET 为了自救...

)


- [用 Python 监控 Reddit](https://pycoders.com/link/9972/web)
    + LEON WEI

A step-by-step tutorial on creating a Reddit keyword monitoring tool with Python and praw. Learn how to run a Python script to watch keywords on a subreddit.





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [jupyterlite: 在浏览器中运行 Wasm 来驱动 Jupyter](https://pycoders.com/link/9985/web)
    + GITHUB.COM/JUPYTERLITE

(`是也乎:`

这样 BI 又多出一个选择...

)


- [torchscale: Transformers at Any Scale](https://pycoders.com/link/9967/web)
    + GITHUB.COM/MICROSOFT

- [python-easter-eggs: Python 中的复活节彩蛋和隐藏的笑话](https://pycoders.com/link/9978/web)
    + GITHUB.COM/ORKOHUNTER

- [lumi: 将函数转换为 REST API 极简框架](https://pycoders.com/link/9968/web)
    + GITHUB.COM/TANMOY741127

(`是也乎:`

所以,这种浅框架和 FastAPI 相比有什么优势呢?

)


- [django-relativity: 更具表现力的 ORM 关系](https://pycoders.com/link/9956/web)
    + GITHUB.COM/ALEXHILL






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [STL Python](https://pycoders.com/link/9969/web)
    + December 7, 2022

- [NZPUG-Auckland Coding Evening](https://pycoders.com/link/9981/web)
    + December 7, 2022

(`是也乎:`

新西兰 的气氛也随着中国工程师的到来开始热烈了...

)



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9976/web)
    + December 7, 2022

- [Python Atlanta](https://pycoders.com/link/9971/web)
    + December 8, 2022

- [PyCon Bolivia 2022](https://pycoders.com/link/9957/web)
    + December 9 to December 11, 2022

(`是也乎:`

玻利维亚 ~ 很久没见过这词儿了...

)




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 554 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-554.html)
- 修订: [issue-554.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-554.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF554D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF554D4Q90XdDA7g):



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





