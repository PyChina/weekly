Title: 蠎周刊(PyCoder)595
Slug: issue-595
Date: 2023-09-20 11:42
Tags: Weekly,Python,pycoders,ZH


> 可视化 CPython 发布过程


原文: [PyCoder's Weekly - Issue #595](https://pycoders.com/issues/595)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230920 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230920 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------


- [继承和内部原理：Python 中的面向对象编码](https://pycoders.com/link/11452/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn about the various types of inheritance that you can use to write object-oriented code in Python. These include class inheritance, multilevel inheritance, and multiple inheritance, along with special methods and abstract base classes.


(`是也乎:`

![OOP](https://ipic.zoomquiet.top/2023-09-20-zshot%202023-09-20%2011.55.25.jpg)

)


- [可视化 CPython 发布过程](https://pycoders.com/link/11444/web)
    + SETH LARSON

This blog post covers how the release process of CPython works and includes a diagram documenting each step. It also highlights supply chain threat spots.


(`是也乎:`

几十年过去, 现在的发布工程早已没那么简洁了...
![CPython](https://ipic.zoomquiet.top/2023-09-20-zshot%202023-09-20%2011.54.06.jpg)
)

- [Python 和 Folium 可视化我的户外活动](https://pycoders.com/link/11450/web)
    + LUKAS KRIMPHOVE 
    + • Shared by Lukas Krimphove

Embark on an expedition of exploration and mapping! Learn how to breathe life into your GPX files and create interactive maps using Python and Folium.


(`是也乎:`

![Folium](https://ipic.zoomquiet.top/2023-09-20-zshot%202023-09-20%2011.52.16.jpg)

自动包含这么多种语言的版本...

)


- [适用于 Linux 的 Mojo SDK 发布](https://pycoders.com/link/11462/web)
    + MODULAR.COM

- [PEP 713: “可调用模块”被拒绝](https://pycoders.com/link/11441/web)
    + PYTHON.ORG


-----------------------------------------
## 探讨/吐糟
> Discussions


NULL


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [迈向新的 SyPy](https://pycoders.com/link/11454/web)
    + OSCAR BENJAMIN

SymPy is a Computer Algebra System, meaning it does math on symbolic concepts. This can provide for a lot more accuracy than typical floating point mathematics found in numeric based systems. This is part 1 of a multi-part article, explaining SymPy along with its recent improvements. Part 2 discusses how SymPy handles polynomials

- [用Scalene 衡量性能的多个方面](https://pycoders.com/link/11469/web)
    + REAL PYTHON 
    + PODCAST

When choosing a tool for profiling Python code performance, should it focus on the CPU, GPU, memory, or individual lines of code? What if it looked at all those factors and didn’t alter code performance while measuring it? This week on the show, we talk about Scalene with Emery Berger, Professor of Computer Science at the University of Massachusetts Amherst.


(`是也乎:`

![Performance](https://ipic.zoomquiet.top/2023-09-20-zshot%202023-09-20%2011.50.01.jpg)

)


- [用 Python Stdlib 实现并发的简单方法](https://pycoders.com/link/11451/web)
    + BITE CODE

Although writing concurrent programs can be challenging, certain kinds of parallelism aren’t that bad. This article introduces you to the ThreadPoolExecutor and shows you how to deal with I/O bound processing. Associated HN discussion.

- [Python （大部分）是由语法糖组成的](https://pycoders.com/link/11455/web)
    + JAKE EDGE

“Programming languages are often made up of a (mostly) irreducible core, with lots of sugary constructs sprinkled on top—the syntactic sugar.” This article summarizes a lot of Brett Cannon’s recent work exploring just what is sugar in Python and what is fundamental.

(`是也乎:`

被发现了?

)


- [改变模块的 Python 属性处理](https://pycoders.com/link/11448/web)
    + JAKE EDGE

There have been a couple of PEPs proposing additions to how imports look for members of a module. This article discusses their meaning and why some aren’t making it into the language. Associated HN discussion.

- [Python 安全响应团队处理建议](https://pycoders.com/link/11445/web)
    + SETH LARSON

Seth Larson is the Python Security Developer-in-Residence and he recently participated in his first publication of an advisory from end-to-end. This blog post talks about the process involved and how it gives him thoughts on what to improve.

- [在 Django 中构建博客](https://pycoders.com/link/11460/web)
    + SIMON WILLISON

Very little code is needed to get a blog working using the Django framework. This post highlights what you need, including each of the key code components. Associated HN discussion.

(`是也乎:`

关键还是 DB 结构设计哪...

)


- [Python 的 in 和 not in 运算符：检查成员资格](https://pycoders.com/link/11458/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to check if a given value is present or absent in a collection of values using Python’s in and not in operators, respectively. This type of check is known as membership test in Python.


(`是也乎:`

![not in](https://ipic.zoomquiet.top/2023-09-20-zshot%202023-09-20%2011.40.16.jpg)

)


- [为什么 Python 代码在函数中运行得更快？](https://pycoders.com/link/11463/web)
    + SCOTT ROBINSON

Python is not necessarily known for its speed, but there are certain things that can help you squeeze out a bit more performance from your code. Surprisingly, putting your code in a function might be one of them.

- [工程师如何评估产品路线图](https://pycoders.com/link/11446/web)
    + STEPHEN PUISSZIS

As a software developer you’re often at the whim of what features your product managers decide are next. This article gives pointers on how to evaluate whether the roadmap is on track.

- [Python 数据帧交换协议](https://pycoders.com/link/11447/web)
    + OLSON & MUKHOPADHYAY

The Python Dataframe Interchange Protocol is a mechanism for switching between Dataframes in different libraries that use them. It supports Vaex, cuDF, Modin, pandas, Polars, and more.


- [自定义您的 Tkinter 应用程序窗口](https://pycoders.com/link/11471/web)
    + KHUMBO KLEIN

In this tutorial, you’ll learn how to tweak and customize windows and forms in your Tkinter apps. It shows you how to modify the title bar, change zoom levels, and add transparency.

- [46 行 Python 中的有符号距离函数](https://pycoders.com/link/11449/web)
    + THEIA VOGEL

A walkthrough of 46 lines of code that renders a 3D ASCII donut using signed distance functions.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [pysentation: 用于显示 Python 演示文稿的 CLI](https://pycoders.com/link/11453/web)
    + GITHUB.COM/MIMSEYEDI

- [toml-bench: 在 Python 中使用哪个 Toml 包？](https://pycoders.com/link/11476/web)
    + GITHUB.COM/PWWANG

- [Python 有状态流处理OSS框架](https://pycoders.com/link/11474/web)
    + GITHUB.COM/BYTEWAX 
    + • Shared by Oli Makhasoeva

- [将经度/纬度转换为时区](https://pycoders.com/link/11477/web)
    + GITHUB.COM/RINGSATURN 
    + • Shared by ringsaturn

- [words-tui: 用于日常写作的 TUI 应用程序](https://pycoders.com/link/11457/web)
    + GITHUB.COM/ANZE3DB


(`是也乎:`

包含一定的 CSS 含量?

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11466/web)
    + September 20, 2023

- [PyCon Uganda](https://pycoders.com/link/11461/web)
    + September 21 to September 24, 2023

- [Swiss Python Summit 2023](https://pycoders.com/link/11442/web)
    + September 21 to September 22, 2023

- [NZPUG-Auckland Workshop: Terminal-Based User Interfaces (TUIs) With Ease Using Textual](https://pycoders.com/link/11475/web)
    + September 21, 2023

- [PyCon UK 2023](https://pycoders.com/link/11459/web)
    + September 22 to September 26, 2023

- [PyCon India 2023](https://pycoders.com/link/11443/web)
    + September 29 to October 3, 2023



-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 543](https://weekly.pychina.org/issue/issue-543.html)
- 2021: [蠎周刊 490](https://weekly.pychina.org/issue/issue-490.html)
    + [pythonista-weekly : Pyw 517](https://weekly.pychina.org/python-weekly/pyw-517.html)
- 2020: [蠎周刊 437](https://weekly.pychina.org/issue/issue-437.html)
    + [pythonista-weekly : Pyw 467](https://weekly.pychina.org/python-weekly/pyw-467.html)
- 2019: [蠎周刊 386](https://weekly.pychina.org/issue/issue-386.html)
- 2018: [蠎周刊 335](https://weekly.pychina.org/issue/issue-335.html)
- 2017: [蠎加载 142](https://weekly.pychina.org/importpython/importpython-142.html)
- 2016: [蠎加载 91](https://weekly.pychina.org/importpython/importpython-91.html)
- 2015: [蠎周刊 184](https://weekly.pychina.org/issue/issue-184.html)
    + [蠎加载 50](https://weekly.pychina.org/importpython/importpython-50.html)
- 2014: [Issue 133](https://weekly.pychina.org/issue/issue-133.html)
- 2013: 空缺
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
        _~~&~~_
    \/ /  = ^  \ ()
      '_   ⏡   _'
      / '--.--' )

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 595 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-595.html)
- 修订: [issue-595.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-595.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF595D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF595D4Q90XdDA7g):



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



