Title: PyCoder 567
Slug: issue-567
Date: 2023-03-08 11:42
Tags: Weekly,Python,pycoders,ZH


> 为毛 Python 还在增长?


原文: [PyCoder's Weekly - Issue #567](https://pycoders.com/issues/567)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230308 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230308 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [PEP 709: 内联理解](https://pycoders.com/link/10435/web)
    + PYTHON.ORG

Python Enhancement Proposal 709 covers a change to how comprehensions are handled. Currently they are compiled as nested functions. Benchmarking shows that treating list, dict, and set comprehensions as in-line code can result in a 2x speedup on the comprehension.

- [Python 中的迭代器和可迭代对象: 运行高效的迭代](https://pycoders.com/link/10430/web)
    + REAL PYTHON

In this tutorial, you’ll learn what iterators and iterables are in Python. You’ll learn how they differ and when to use them in your code. You’ll also learn how to create your own iterators and iterables to make data processing more efficient.


(`是也乎:`

![Iterations](https://ipic.zoomquiet.top/2023-03-08-zshot%202023-03-08%2010.38.41.jpg)

嗯哼, 怎么说呢? 同样是迭代处理,对比一下 Rust 最常见的:

![rs](https://ipic.zoomquiet.top/2023-03-08-zshot%202023-03-08%2010.42.17.jpg)

这种链式闭包联级处理, 也是 Elixir/Haskell/LISP/...函数式语言常见的形式,
这在 Python 中还很难日用起来...

)


- [Pandas 2.0 和 Arrow Revolution（上）](https://pycoders.com/link/10432/web)
    + MARC GARCIA

This article details the changes in the Pandas 2.0 release, with emphasis on the underlying adoption of Apache Arrow.



-----------------------------------------
## 探讨/吐糟
> Discussions


- [Python 的多处理性能问题](https://pycoders.com/link/10453/web)
    + HACKER NEWS

Last week’s issue of PyCoders included a link to Python’s multiprocessing performance problem which now has a Hacker News conversation to go along with it.

- [为什么 Python 持续增长](https://pycoders.com/link/10440/web)
    + HACKER NEWS

(`是也乎:`

![Why](https://ipic.zoomquiet.top/2023-03-08-zshot%202023-03-08%2010.31.57.jpg)

好问题哪, 老爹都退休了...其它同期语言都佛了...

作为 GitHub: Codespaces + Copilot 的硬广是没问题的,

只是囧的,没好意思说 Ruby ...

~> [GitHub Codespaces Documentation - GitHub Docs](https://docs.github.com/zh/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account)
... [GitHub工程团队已经转移到Codespaces：实现开发环境的秒级启用_架构_Cory Wilkerson_InfoQ精选文章](https://www.infoq.cn/article/wivsohwds5lnipwikquy)

PS:
Codespaces 这么火, 国内的 Coding 应该发财了?


)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Python 的速度: 还不错!](https://pycoders.com/link/10439/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

The articles discusses whether Python is as slow as so many authors claim. When doing so, it mentions highly optimized Python frameworks for numerical computation, efficient compilers - but also coding time as opposed to execution time. All in all, Python is much faster than most think.

- [您的第一个循环神经网络 (RNN)](https://pycoders.com/link/10452/web)
    + RODRIGO GIRÃO SERRÃO 
    + • Shared by Rodrigo Girão Serrão

In this introductory tutorial, you will build a recurrent neural network (RNN) with PyTorch. The RNN will be trained to read names and it will output the natural language they belong to. This is a modern spin on a tutorial from the PyTorch documentation.

(`是也乎:`

可惜没办法拿来当成礼物送女神们哪...

)

- [用 namedtuple 编写干净的 Pythonic 代码](https://pycoders.com/link/10448/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn what Python’s namedtuple is and how to use it in your code. You’ll also learn about the main differences between named tuples and other data structures, such as dictionaries, data classes, and typed named tuples.


(`是也乎:`

![namedtuple](https://ipic.zoomquiet.top/2023-03-08-zshot%202023-03-08%2010.27.08.jpg)

不是, 听起来已经不象是真人讲解的了...

不过, 这个低调的模块: [collections — Container datatypes — Python 3.11.2 documentation](https://docs.python.org/3/library/collections.html#collections.namedtuple)

早已在 sqlite3 等等其它关键模块中深入用起来了...


)

- [用 NumPy reshape() 改变数组的"形状"](https://pycoders.com/link/10424/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use NumPy reshape() to rearrange the data in an array. You’ll learn to increase and decrease the number of dimensions and to configure the data in the new array to suit your requirements.


(`是也乎:`


![NumPy](https://ipic.zoomquiet.top/2023-03-08-zshot%202023-03-08%2010.25.28.jpg)

)


- [现代 Flask 应用程序的 13 个技巧和技巧](https://pycoders.com/link/10442/web)
    + PHILIP JONES

Flask is approaching its 13th birthday, and to celebrate, Phillip has written 13 tips for writing modern Flask apps. It covers dealing with JSON, environment based configuration, auto-generated docs, and more.



- [Python 3.11 更快, 但 Pyston 和 PyPy 仍有优势](https://pycoders.com/link/10450/web)
    + MICHAEL LARABEL

There are many speed improvements in CPython 3.11, but that doesn’t mean the Python alternatives don’t still have some advantages. Pyston and PyPy are still better in some cases.


(`是也乎:`

Pyston & PyPy 又没有历史包袱...怎么浪怎么来就好...

)


- [用 OpenAI 和 Python 来提升你的简历](https://pycoders.com/link/10437/web)
    + PIERO PAIALUNGA

This tutorial shows you how to build a system that takes a question template and writes a resume as output. The example is built on Streamlit and OpenAI.


(`是也乎:`


等于自动帮你对比全球成功获得 offer 的简历, 进行对应优化...

)


- [为已经懂 Python 的介绍 Elixir](https://pycoders.com/link/10445/web)
    + RICH JONES

Elixir is a functional based programming language with similarities to Ruby and Python. This article is an intro guide for programmers who know Python.


(`是也乎:`

所以? Python 其实成了IT世界的英语?
先会 Python ,然后, 其它的水到渠成?

)


- [Python 现在已经是两种语言...这真的很棒](https://pycoders.com/link/10444/web)
    + TIN TVRTKOVIĆ

Python’s addition of typing has created “two” languages: typed and untyped Python. Tin tells you why that’s a great thing.


(`是也乎:`

> c'est la vie (´-ι_-｀)

不过, 不用类型提示的应该永远支持, 
这毕竟是更加直觉的一类...


)



- [用 Rust 构建 Python CLI 工具](https://pycoders.com/link/10436/web)
    + MAKSUDUL HAQUE' 
    + • Shared by Maksudul Haque

This step-by-step tutorial shows you how to build a rust tool and deliver it through Python packaging mechanisms.


(`是也乎:`

嗯哼? 这个赞的哪...刚刚学会如何用 Rust 快速开发 CLI,
和 invoke/Click/... 相比, 还是复杂了点儿..

已经发布的小工具: [ZoomQuiet crates.io: Rust Package Registry](https://crates.io/users/ZoomQuiet)

部分根本就是照着原先 Python 版本逐行迁移过去的...



)


- [用 nox 和 pyenv 测试多个 Python 版本](https://pycoders.com/link/10426/web)
    + SETH LARSON

Quick instructions on using nox with parameters to test multiple versions of Python against your test suite.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [30-Days-Of-Python: Python 编程学习指南](https://pycoders.com/link/10433/web)
    + GITHUB.COM/ASABENEH


(`是也乎:`

这种教程的趋势是先越来越短,现在不行不越来越长?
21天精通XXXX 流行了几年,
后来就是一天掌握XXX...


)


- [高性能内存缓存](https://pycoders.com/link/10423/web)
    + GITHUB.COM/YILING-J • Shared by yiling

(`是也乎:`

实话, 都在内存里了,想性能低一点儿, 反而难的卟?

)


- [RWKV-LM: 具有 Transformer 级 LLM 性能的 RNN](https://pycoders.com/link/10449/web)
    + GITHUB.COM/BLINKDL


(`是也乎:`


LLVM 成名后, LL 也变成了热词...

)


- [nosqlapi: NOSQL Database API](https://pycoders.com/link/10454/web)
    + NOSQLAPI.READTHEDOCS.IO • Shared by Matteo Guadrini

(`是也乎:`

所以, 和 OpenAPI 有什么差别?

)


- [paperless-ngx: 扫描、索引和存档您的物理文档](https://pycoders.com/link/10425/web)
    + GITHUB.COM/PAPERLESS-NGX


(`是也乎:`

嗯哼? 还以为是对物质世界进行索引,
没想到只是扫描进来再管理...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Santa Cruz Python Meetup](https://pycoders.com/link/10441/web)
    + March 8, 2023

- [Heidelberg Python Meetup](https://pycoders.com/link/10443/web)
    + March 8, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10421/web)
    + March 8, 2023

- [pyCologne User Group Treffen](https://pycoders.com/link/10446/web)
    + March 8, 2023

- [Python North East](https://pycoders.com/link/10447/web)
    + March 8, 2023

- [DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/10427/web)
    + March 11, 2023

- [Python Web Conf 2023](https://pycoders.com/link/10451/web)
    + March 13 to March 18, 2023

- [PyCascades](https://pycoders.com/link/10456/web)
    + March 18 to March 20, 2023 in Vancouver, BC + Remote




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 567 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-567.html)
- 修订: [issue-567.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-567.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF567D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF567D4Q90XdDA7g):



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



