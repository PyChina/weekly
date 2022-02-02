Title: PyCoder 509
Slug: issue-509
Date: 2022-01-26 11:42
Tags: Weekly,Python,pycoders,ZH


> PEP 646+679 已接受


原文: [PyCoder's Weekly - Issue #509](https://pycoders.com/issues/509)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220126 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220126 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [PEP 646: 可变参数泛型被接受](https://pycoders.com/link/7883/web)
    + PYTHON.ORG

This PEP introduces TypeVarTuple, enabling parameterisation with an arbitrary number of types. For example, it allows the type of array-like structures in numerical computing libraries such as NumPy and TensorFlow to be parameterised with the array shape, enabling static type checkers to catch shape-related bugs. The PEP was recently accepted by the Steering Council.

- [用 Python 构建 骰子 应用程序](https://pycoders.com/link/7895/web)
    + REAL PYTHON

In this step-by-step project, you’ll build a dice-rolling simulator app with a minimal text-based user interface using Python. The app will simulate the rolling of up to six dice. Each individual die will have six sides.

(`是也乎:`


![Dice-Rolling](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.43.20.jpg)


关键还是随机数, 如何真正随机

![ASCII](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.44.46.jpg)

)

- [PEP 679: 允许在断言语句中使用括号](https://pycoders.com/link/7870/web)
    + PYTHON.ORG

“It is a common user mistake when using the form of the assert statement that includes the error message to surround it with parentheses. Unfortunately, this mistake passes undetected as the assert will always pass, because it is interpreted as an assert statement where the expression is a two-tuple, which always has truth-y value.”

- [严格的 Python 函数参数](https://pycoders.com/link/7898/web)
    + SETH MICHAEL LARSON

Learn about keyword-only and positional-only parameters and see how using strict function signatures can help you write more resilient code.

- [科学 Python 的指导设计原则](https://pycoders.com/link/7887/web)
    + NSLS-II.GITHUB.IO

Tips on how to design and organize scientific Python code.

(`是也乎:`

还是最佳实践, 叕一组

)



-----------------------------------------
## 探讨/吐糟
> Discussions



None




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 Django 为设计和构建社交网络](https://pycoders.com/link/7882/web)
    + REAL PYTHON 
    + PODCAST

Are you looking for a project to practice your Django skills? Designing the fundamental interactions of a social network is an instructive way to explore models and relationships while learning advanced Django skills. This week on the show, previous guest Martin Breuss talks about his new four-part tutorial series, “Build a Social Network With Django.”


(`是也乎:`



![SNS](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.40.53.jpg)

SNS 哪, 当年 RoR 起家的本事

)


- [用 Python 解决 Wordle](https://pycoders.com/link/7896/web)
    + SIMON SOTAK

“Wordle seems to be trending and it got me thinking of what would be the best algorithm to solve it. I decided to do a naive implementation in Deepnote with Python that only uses NLTK’s list of all english words and base letter frequencies in english texts. This way, I was able to solve the January 18 challenge, but I used up all available attempts.”

(`是也乎:`

拼写游戏哪, 对中文无感


)

- [教程/从 Python IDLE 开始](https://pycoders.com/link/7886/web)
    + REAL PYTHON 
    + COURSE

In this course, you’ll learn how to use the development environment included with your Python installation. Python IDLE is a small program that packs a big punch! You’ll learn how to use Python IDLE to interact with Python directly, work with Python files, and improve your development workflow.


(`是也乎:`


![IDLE](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.38.26.jpg)


IDLE 真的上古神器, 除了中文支持不好,其它没什么毛病...

)


- [Python 中的 模字符串格式](https://pycoders.com/link/7893/web)
    + REAL PYTHON

You can use the % modulo operator for string formatting in Python. It’s a commonly used technique in older Python versions, especially in Python 2. Therefore, you might see it when digging into existing code bases, and it can be helpful to understand how it works.


(`是也乎:`


![String](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.36.37.jpg)

虽然提供了越来越多格式化形式, 还是传统的好懂些.

![传统](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.37.06.jpg)


)


- [理解 Django: 快速用起 Django](https://pycoders.com/link/7875/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

How do you make your Django app fast? You measure what is slow, scale your system when necessary, and use a combination of fast database queries and strategic caching. This artcile explores those topics and more to help you get a performant Django app.


(`是也乎:`

多数情况都是 数据库拖慢了 Django


)

- [Python 装饰器的静态类型](https://pycoders.com/link/7900/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

Accurately static typing decorators in Python is tricky. The wrapper function obfuscates type information required to statically determine the types of the wrapped function parameters. Here’s how you can circumnavigate that.


(`是也乎:`


Decorators 几乎成了Python 的作弊器...

)


- [Python Type Hints: 如何给入描述符](https://pycoders.com/link/7906/web)
    + ADAM JOHNSON

“The descriptor protocol allow us to completely customize attribute access. Python’s documentation describes the protocol with types involved described with words. Let’s look at how we can write those as type hints.”

- [Python 描述符的威力](https://pycoders.com/link/7878/web)
    + PICCOLO-ORM.COM

An introduction to the Python descriptor protocol, with some example use cases. The descriptor protocol allows you to implement custom logic when a variable is accessed, or assigned a new value.



- [在 Python 中使用任意标签处理 YAML](https://pycoders.com/link/7885/web)
    + ANDGRAVITY.COM

Using the PyYAML library to safely read and write YAML with any tags, in a way that’s as straightforward as interacting with built-in types.


(`是也乎:`


TOML 还是有机会的...

)


- [Mypy 的 @overload 简介](https://pycoders.com/link/7879/web)
    + PATRICK NSUKAMI 
    + • Shared by Patrick Nsukami

“Sometimes the type of the returned value in a function depend on the type of the arguments in ways that can’t be captured with a Union.”


(`是也乎:`

几个独立发行版 Python 都折腾出自己独有的高招

![overload](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.32.47.jpg)

不过, 整体趋势都是越来越象 C++


)


- [矢量化如何加速你的 Python 代码](https://pycoders.com/link/7874/web)
    + ITAMAR TURNER-TRAURING

Vectorization allows you to speed up processing of homogeneous data in Python. Learn what it means, when it applies, and how to do it.


(`是也乎:`

矢量加速?

)

- [在 Python 使用任意中缀运算符的技巧](https://pycoders.com/link/7897/web)
    + TOMER FILIBA

Discussing an interesting trick which adds support for infix operators in Python, e.g. 5 |add| 6

- [DIY 自动驾驶: 一个任性的假期项目](https://pycoders.com/link/7901/web)
    + TRISTAN RICE


(`是也乎:`


![Holiday](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.27.22.jpg)


假期无事儿造个神经网络...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code





- [pyccolo: Declarative Instrumentation for Python](https://pycoders.com/link/7890/web)
    + GITHUB.COM/SMACKE

- [Qtile: 用 Python 编写可破解的平铺窗口管理器](https://pycoders.com/link/7888/web)
    + QTILE.ORG

(`是也乎:`

窗口管理器?
果断得通过 C 接口兼容所有系统...

)


- [sonora: Python 的 gRPC-Web 实现](https://pycoders.com/link/7905/web)
    + GITHUB.COM/PUBLIC


(`是也乎:`


![sonora](https://ipic.zoomquiet.top/2022-01-26-zshot%202022-01-26%2010.24.08.jpg)

)

- [EasyRPC: 在进程和应用程序之间共享 Python 函数](https://pycoders.com/link/7871/web)
    + GITHUB.COM/CODEMATION 
    + • Shared by Joshua Jamison


(`是也乎:`

还没发布 1.0, 如果兼容 gRPC 那就爽快了

)




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



⋅ PyCamp Leipzig 2022 January 29 to January 31, 2022

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/7880/web)
    + January 29, 2022
    + 印度

- [⋅ PythOnRio Meetup](https://pycoders.com/link/7902/web)
    + January 29, 2022

- [⋅ Introduction to the Python Programming Language (In Persian)](https://pycoders.com/link/7873/web)
    + February 1, 2022

- [⋅ PyCon Iran Conference (Virtual)](https://pycoders.com/link/7884/web)
    + February 1 to February 2, 2022

- [⋅ DjangoCon Europe 2022](https://pycoders.com/link/7907/web)
    + September 21 to 25, 2022 
    + in Porto, 葡萄牙


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 509 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-509.html)
- 修订: [issue-509.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-509.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF509D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF509D4Q90XdDA7g):



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





