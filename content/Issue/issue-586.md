Title: 蠎周刊(PyCoder)586
Slug: issue-586
Date: 2023-07-19 11:42
Tags: Weekly,Python,pycoders,ZH


> 如何组织近3万个模块?


原文: [PyCoder's Weekly - Issue #586](https://pycoders.com/issues/586)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230719 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230719 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [Python 中的迷宫第 2 部分：存储和求解](https://pycoders.com/link/11130/web)
    + REAL PYTHON 
    + COURSE

In part two of this two-part project, you’ll define a specialized binary file format to store a maze on disk, transform the maze into a traversable weighted graph, and use a graph search algorithm in the NetworkX library to find the solution.

(`是也乎:`

![迷宫](https://ipic.zoomquiet.top/2023-07-19-zshot%202023-07-19%2012.21.34.jpg)

)


- [如何组织我们非常大的 Python 巨石](https://pycoders.com/link/11132/web)
    + DAVID SEDDON

Kraken Technologies is an environmental tech company that does a lot of Python development. One of their applications is a monolith with over 27k modules. This article outlines how they keep all this organized and running.


(`是也乎:`


2万7千个模块的 Python 系统运营...

)


- [进程间共享 NumPy 数组的 7 种方法](https://pycoders.com/link/11122/web)
    + JASON BROWNLEE

If you’re doing multi-processing with NumPy you will need to pass arrays between processes. This article covers different ways of doing just that.

- [Python 3.12.0 Beta 4 发布](https://pycoders.com/link/11141/web)
    + CPYTHON DEV BLOG






-----------------------------------------
## 探讨/吐糟
> Discussions




- [希望明天的 CPython 构建系统具备什么功能？](https://pycoders.com/link/11149/web)
    + PYTHON.ORG


(`是也乎:`

自动转化为 Rust 编译出二进制?

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks






- [为您的编码之旅解锁 IPython 的神奇工具箱](https://pycoders.com/link/11151/web)
    + REAL PYTHON

IPython is a powerful tool that can prove useful on your journey to mastering Python. Its friendly interface will enable you to comfortably take control of your learning. In this tutorial, you’ll cover the basic concepts of using IPython and learn how its features can make coding efficient.

(`是也乎:`


![IPython](https://ipic.zoomquiet.top/2023-07-19-zshot%202023-07-19%2012.15.59.jpg)

)


- [Django: 通过随机排序查询集查找测试脆弱性](https://pycoders.com/link/11137/web)
    + ADAM JOHNSON

Sometimes code depends on the order of a QuerySet while not specifying an order. This can lead to random, flaky test failures because databases can return rows in any order when none is specified. Learn how to randomly order your QuerySet when under test to detect this weird problem.



- [Python 和 Rust 异步 Web 服务器性能](https://pycoders.com/link/11153/web)
    + JOHN LOCKWOOD

This post compares asynchronous web performance between a Python application using Uvicorn and a Rust application using Axum. A similar data-serving program is written in both applications with very little performance difference.


(`是也乎:`


初步测试 Rust 只领先 7% ?

当然, 最后的挽尊说明也很中肯,
如果你的服务要持续运行几年呢?
...但是,公司可能都活不了这么长时间呢?

)


- [驻场安全开发人员：每周报告 #2](https://pycoders.com/link/11125/web)
    + SETH LARSON

The new Security Developer-in-Residence at the Python Software Foundation writes about the Software Bill of Materials and how it can programmatically tell you exactly what is in a distribution, including compiled libraries.


(`是也乎:`

嗯哼? 这就是经典的在公开场合工作了...

)


- [用 anywidget 让 Jupyter 小部件变得简单](https://pycoders.com/link/11148/web)
    + TREVOR MANZ

“anywidget is a Python library that makes it simple and enjoyable to create custom Jupyter Widgets.” It allows for quick prototyping, and because it is Python can be used across environments.

- [向 Python 添加尾部调用优化](https://pycoders.com/link/11147/web)
    + JONAS OTTEN

Tail call optimization is a technique provided in some languages to avoid growing the stack with recursive algorithms. Python doesn’t have it, but this article shows how you can build it.

- [Python 如何使用垃圾收集](https://pycoders.com/link/11140/web)
    + KARISHMA SHUKLA

This article outlines how Python stores variables as references and how that relates to memory management.


(`是也乎:`

源代码中有一切魔法,
当年 老爹是认真思考过的...

)


- [WASI 对 CPython 的支持状况：2023 年 6 月](https://pycoders.com/link/11136/web)
    + BRETT CANNON

This post from Brett covers the current state of WebAssembly targets in Python.



- [Ode to Ptyon](https://pycoders.com/link/11150/web)
    + MEDIUM.COM/@PETEFISON 
    + • Shared by Pete Fison

A lighthearted poem about a certain well-known programming language.

(`是也乎:`

叕一封给 Python 的诗
```
My love is a language so fine,
Created by Guido. Divine!
Duck typing and whitespace,
She runs with sublime grace.
Now coding flows freer than wine…

With one simple import, you see,
I mastered `antigravity`.
Just one line of code
And off we both rode,
Flying higher, and further for free.

List comprehensions, [oh my],
Make coding as easy as .py!
With one simple line
My code can now shine
And make other languages sigh.

So thank you dear Guido, I say,
For siring this language so bae.
I now understand
She’s the best in the land
And I earnestly hope she will stay.

© Pete Fison MMXXIII
```


忒直白了...

)


- [LangChain的问题](https://pycoders.com/link/11154/web)
    + MAX WOOLF

LangChain is a Python and JavaScript library for interfacing with OpenAI’s GPT and other models for text generation. But, it “is complicated, so it must be better. Right?”


(`是也乎:`


哈, ChatGPT 插件一出, LangChain 就坐腊了...
一直有人出招想拯救...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [Neurokernel: 模拟果蝇大脑的平台](https://pycoders.com/link/11145/web)
    + NEUROKERNEL.GITHUB.IO


(`是也乎:`


单单 果蝇大脑 真能模拟明白, 那也是足以在很多场景中发挥作用的了...

)


- [panflute: Pandoc 过滤器](https://pycoders.com/link/11152/web)
    + GITHUB.COM/SERGIOCORREIA

- [GPTerm: 将纯文本转换为 Shell 命令](https://pycoders.com/link/11138/web)
    + GITHUB.COM/ADEMAKDOGAN 
    + • Shared by ADEM AKDOGAN

(`是也乎`:

不保证可用哪,
就好奇, 如何让 GPT 知道何时值得推荐 `sudo rm -rf . /` 这种指令?

)



- [litechain: 构建强大的、可组合的 LLM 应用程序](https://pycoders.com/link/11142/web)
    + GITHUB.COM/ROGERIOCHAVES


(`是也乎:`

`*Chain` 这个名字就看何时出个杀手级的平台了...

)


- [quart: 异步 Python 微型 Web 框架](https://pycoders.com/link/11134/web)
    + GITHUB.COM/PALLETS

(`是也乎:`

叕一个异步 web 应用框架,
其实认真使用过诸如 FastAPI 之类的异步框架就知道,
单异步 web 请求并没什么作用,
得将数据链上所有环节都异步了才可能有整体效能涌现...

不由想起来 沈游侠 原创的系列框架...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心





- [EuroSciPy Aug 14-18, Early Bird Tickets Available](https://pycoders.com/link/11133/web)
    + Until July 28, 2023

- [PyStaDa](https://pycoders.com/link/11123/web)
    + July 19, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11156/web)
    + July 19, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/11127/web)
    + July 20, 2023

- [Python Northwest](https://pycoders.com/link/11124/web)
    + July 20, 2023

- [PyLadies Dublin](https://pycoders.com/link/11128/web)
    + July 20, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/11129/web)
    + July 21 to July 22, 2023

- [PyHEP.dev 2023](https://pycoders.com/link/11144/web)
    + July 25 to July 29, 2023


-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 534](https://weekly.pychina.org/issue/issue-534.html)
- 2021: [蠎周刊 481](https://weekly.pychina.org/issue/issue-481.html)
    + [pythonista-weekly : Pyw 508](https://weekly.pychina.org/python-weekly/pyw-508.html)
- 2020: [蠎周刊 428](https://weekly.pychina.org/issue/issue-428.html)
    + [pythonista-weekly : Pyw 458](https://weekly.pychina.org/python-weekly/pyw-458.html)
- 2019: [蠎周刊 377](https://weekly.pychina.org/issue/issue-377.html)
- 2018: [蠎周刊 326](https://weekly.pychina.org/issue/issue-326.html)
- 2017: [蠎加载 133](https://weekly.pychina.org/importpython/importpython-133.html)
- 2016: [蠎加载 82](https://weekly.pychina.org/importpython/importpython-82.html)
- 2015: [蠎周刊 175](https://weekly.pychina.org/issue/issue-175.html)
    + [蠎加载 41](https://weekly.pychina.org/importpython/importpython-41.html)
- 2014: [Issue 124](https://weekly.pychina.org/issue/issue-124.html)
- 2013: 空缺
- 2012: [Issue 23 Guido](https://weekly.pychina.org/issue/issue-23.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [@Chaos42DAMA - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + VLog
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...




```
           _~-*-~_
       \/ /  - #  \ ()
         '_   V   _'
         \ '--⌄--' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 586 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-586.html)
- 修订: [issue-586.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-586.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF586D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF586D4Q90XdDA7g):



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



