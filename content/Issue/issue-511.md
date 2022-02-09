Title: PyCoder 511
Slug: issue-511
Date: 2022-02-09 11:42
Tags: Weekly,Python,pycoders,ZH


> 简单将GraphQL接口添加到DRF应用程序


原文: [PyCoder's Weekly - Issue #511](https://pycoders.com/issues/511)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220209 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220209 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------






- [用可选参数定义Python函数](https://pycoders.com/link/7994/web)
    + REAL PYTHON 
    + COURSE

Learn about Python optional arguments and how to define functions with default values. You’ll also see how to create functions that accept any number of arguments using *args and **kwargs.


(`是也乎:`

![Optional](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2012.04.32.jpg)


其实, 默认值本身也是一种漏洞...

)


- [typing.Protocol 支持不同 Python版本](https://pycoders.com/link/7993/web)
    + HYNEK SCHLAWACK

How to seamlessly support typing.Protocol on Python versions older and newer than 3.8. At the same time.


(`是也乎:`


    import sys

    if sys.version_info >= (3, 10):
        from typing import ParamSpec
    else:
        from typing_extensions import ParamSpec


这类补丁何时是个头?

)


- [更好的Pygame主循环](https://pycoders.com/link/7982/web)
    + GLYPH LEFKOWITZ

Improving your game’s main loop for smoother gameplay that takes less battery power: “Now your players’ laptops run cool while playing, and the graphics don’t have ugly tearing artifacts any more!”


(`是也乎:`



)


- [GitHub 语言和其它开发事务调查](https://pycoders.com/link/7968/web)
    + GITHUB.COM 
    + • Shared by Ian Currie

JavaScript retains the top spot, Python keeps 2nd place gained in 2019 over Java, which holds in 3rd. Typescript continues 4th after racing up from 2017 from 10th to 4th in 2020. JavaScript + TypeScript seem to put that way ahead in terms of amount of code on GitHub.


(`是也乎:`


![排名](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2012.00.55.jpg)

top5 里有三个都是 微软 一家的...

![人数](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2012.02.14.jpg)

猜中国有多少?


)



- [Python 新闻/2022年1月新增了什么？?](https://pycoders.com/link/7974/web)
    + REAL PYTHON

In January 2022, Black came out of Beta, IPython 8.0 was released, PEP 665 was rejected, and last but not least, a fifteen-year-old bug was fixed. In this article, you’ll get the details on these important happenings in the world of Python.


(`是也乎:`

![New](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2011.58.54.jpg)

)


- [Python in Visual Studio Code – February 2022 发布](https://pycoders.com/link/7969/web)
    + MICROSOFT.COM

This release includes: smart selection, folding support, improvements to the Python interpreters list, improvements when using Anaconda.

(`是也乎:`

反正, 俺是关闭的

)



- [CPython 3.11.0a5 可用](https://pycoders.com/link/7999/web)
    + CPYTHON DEV BLOG

“We needed to tame some angry buildbots, but after a small fight, we won with just some scratches! Here you have a shiny new alpha release: Python 3.11.0a5.”



-----------------------------------------
## 探讨/吐糟
> Discussions



- [Python Core Dev Says “现在是时候弃用 STDLIB URLLIB 模块了”](https://pycoders.com/link/7992/web)
    + TWITTER.COM/VICTORSTINNER

“I propose to deprecate the urllib module in Python 3.11. It would emit a DeprecationWarning which warn users, so users should consider better alternatives like urllib3 or httpx: well known modules, better maintained, more secure, support HTTP/2 (httpx), etc.”


(`是也乎:`

是时候了...很多是时候, 一般都不是时候


)


- [Python’s IDLE 编辑器现在要好很多](https://pycoders.com/link/7987/web)
    + HACKER NEWS

“People used to say all kinds of things about Python’s native IDLE editor, but lately it has become a viable alternative for me to other editors like Notepad++.”


(`是也乎:`


IDLE 和 Notepad++
两大上古神器, 
真的没想到一直在改进, 
这都多少年了...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [在 Python 中操纵和分析音频](https://pycoders.com/link/7998/web)
    + REAL PYTHON 
    + PODCAST

Would you like to experiment with analyzing or manipulating audio with Python? This week on the show, we have Braden Riggs from DolbyIO to discuss extracting audio features and Python libraries for reshaping audio. Braden shares techniques from his recent talk at PyData Global, “Unlocking More From Your Audio Data!”

(`是也乎:`

![Audio](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2011.53.37.jpg)

音频分析和图像分析基本一致,
比视频分析要弱一个级别


)



- [用Python 异常HOOKs 创建美丽的回溯](https://pycoders.com/link/7957/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

“We all spend a good chunk of our time debugging, sifting through logs, or reading tracebacks. Each of these can be difficult and time-consuming and in this article, we will focus on making the last one—dealing with tracebacks and exceptions—as easy and efficient as possible.”


(`是也乎:`


![Beautiful](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2011.52.23.jpg)


是否漂亮, 关键不在颜色, 而在真正按逻辑的给出陈述

)


- [Python 中过载函数的正确方法](https://pycoders.com/link/7986/web)
    + MARTIN HEINZ

“Function overloading is a common programming pattern which seems to be reserved to statically-typed, compiled languages. Yet there’s an easy way to implement it in Python with help of multimethods or, as it’s called in Python, Multiple Dispatch.”

- [Only Python: 试图领先于 IPython 的友好 Traceback](https://pycoders.com/link/7965/web)
    + ANDRÉ ROBERGE

“I’m writing this blog post in the hope that some people will be encouraged to test friendly/friendly-traceback with IPython/Jupyter and make suggestions as to how it could be even more useful.”


(`是也乎:`


没有对比就没有伤害,
![Friendly](https://ipic.zoomquiet.top/2022-02-09-image.png)

通过追加的 what()/why()/where() 专用函式来丰富/合理化 traceback 的输出

其实, 真能作到的话,
反过来, 人工撰写 what/why/when/where 之类的要求, 
也应该能生成对应正确代码了?

)


- [Python’s len() Function](https://pycoders.com/link/7976/web)
    + REAL PYTHON 
    + COURSE

Learn how to find the length of built-in data types using len(), use len() with third-party data types, and provide support for len() with user-defined classes.


(`是也乎:`

![len](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2011.46.14.jpg)


len() 也是一个细思恐极的函式

)


- [Python 中通用类型的差异](https://pycoders.com/link/7983/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

Explaining generics that are—covariant, contravariant or invariant in types, and why it matters while working with type annotations in Python.


(`是也乎:`

对 types 执着的, 
都是复杂大系统中, 多团队协同时

)



- [Django 中使用静态和媒体文件](https://pycoders.com/link/7973/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

A look at how to work with static and media files in a Django project, locally and in production.

(`是也乎:`


现在基本都得依托某种 CDN 了...

)



- [用 PyPy 针对 冰岛 进行自然语言处理:案例研究](https://pycoders.com/link/7989/web)
    + VILHJÁLMUR ÞORSTEINSSON

(`是也乎:`

嗯哼? 冰岛?

)


- [在 Python 中反转二叉树的不同方法](https://pycoders.com/link/7970/web)
    + MISHA BEHERSKY 
    + • Shared by Misha Behersky



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [BeeWare: 用 Python 撰写基于本地UI 能到处运行](https://pycoders.com/link/7991/web)
    + BEEWARE.ORG

(`是也乎`:

![BeeWare](https://ipic.zoomquiet.top/2022-02-09-zshot%202022-02-09%2011.29.23.jpg)
叕被推荐, iOS, Android, Windows, MacOS, Linux, Web...
全面兼容, 这是怎样的一种野心哪...

)


- [sqladmin: SQLAlchemy Admin for Starlette/FastAPI](https://pycoders.com/link/7984/web)
    + GITHUB.COM/AMINALAEE 
    + • Shared by Amin Alaee

(`是也乎:`

PHP 世界中的 `*admin` 系列作品可都是神品,
就看 Python 世界中的了

)


- [etna: 用于时间序列预测的 Python 模块](https://pycoders.com/link/7958/web)
    + GITHUB.COM/TINKOFF-AI 
    + • Shared by Andrey

- [ChemicalX: Deep Learning Library  用以药理分析](https://pycoders.com/link/7967/web)
    + GITHUB.COM/ASTRAZENECA 
    + • Shared by Benedek Rozemberczki

- [GraphWrap: 将GraphQL接口添加到DRF应用程序](https://pycoders.com/link/7979/web)
    + GITHUB.COM/PAULGILMARTIN 
    + • Shared by Paul Gilmartin

(`是也乎:`

实用的, 就看是否能内置解决性能问题了.

)


- [strongtyping-pyoverload: 运行时方法过载装饰器](https://pycoders.com/link/7966/web)
    + PYPI.ORG







-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [⋅ Python Atlanta](https://pycoders.com/link/7964/web)
    + February 10, 2022

- [⋅ Python Miami](https://pycoders.com/link/7975/web)
    + February 12 to February 13, 2022

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/7971/web)
    + February 12, 2022

- [⋅ PyCon Iran 2022](https://pycoders.com/link/7980/web)
    + February 16 to February 19, 2022

- [⋅ Python Web Conference 2022 (Virtual)](https://pycoders.com/link/8002/web)
    + March 21 to March 25, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 511 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-511.html)
- 修订: [issue-511.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-511.md)


## PPS:
> 不觉中蟒周刊快译已经到了第10个年头

去年开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF511D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF511D4Q90XdDA7g):



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





