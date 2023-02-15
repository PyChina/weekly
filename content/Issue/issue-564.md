Title: PyCoder 564
Slug: issue-564
Date: 2023-02-15 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 中的单体仓库


原文: [PyCoder's Weekly - Issue #564](https://pycoders.com/issues/564)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230215 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230215 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------




- [Python 中的单体仓库](https://pycoders.com/link/10340/web)
    + KENNEDY & VUJIC PODCAST

A monorepo is a source control pattern in some organizations where a single code repository is shared for many or all projects. This interview with David Vujic discusses monorepos and the set of Python tools that can help you succeed with this pattern.

(`是也乎:`


![Monorepos](https://ipic.zoomquiet.top/2023-02-15-zshot%202023-02-15%2010.15.24.jpg)


也就是巨大石仓库,Google 引发的潮流...
其实吧,如果没有合理的配套商业模型以及基础设施和对应专业运维团队,
这么搞....囧的

)


- [用 Python 和 SpiffWorkflow 的业务流程模型](https://pycoders.com/link/10338/web)
    + REAL PYTHON 
    + PODCAST

Can you describe your business processes with flowcharts? What if you could define the steps in a standard notation and implement the workflows in pure Python? This week on the show, Dan Funk from Sartography is here to discuss SpiffWorkflow.


(`是也乎:`

![Business](https://ipic.zoomquiet.top/2023-02-15-zshot%202023-02-15%2010.14.32.jpg)

支持多种工作流描述语言的引擎...


)


- [函数式 Python，第二部分: Dial M for Monoid](https://pycoders.com/link/10320/web)
    + CHRISTOPHER HARRISON

This article is about “commandeering techniques from richly typed, functional languages into Python for fun and profit.” The focus is on Typeclasses and continuation-passing style.

- [SQLAlchemy 2.0 发布](https://pycoders.com/link/10321/web)
    + SQLALCHEMY.ORG

(`是也乎:`

淦...2.0 了

)


- [DjangoCon Europe 2023 (Edinburgh) 征集参与](https://pycoders.com/link/10337/web)
    + PRETALX.COM

- [Python 3.11.2, Python 3.10.10 and 3.12.0 Alpha 5 可用](https://pycoders.com/link/10322/web)
    + CPYTHON DEV BLOG

- [Mypy 1.0 发布](https://pycoders.com/link/10342/web)
    + MYPY-LANG.BLOGSPOT.COM

(`是也乎:`

嗯哼?
以为永远不会有 1.0 了呢...

)





-----------------------------------------
## 探讨/吐糟
> Discussions



- [用 Python 变得越来越困难](https://pycoders.com/link/10344/web)
    + LOBSTERS

This discussion is based on Avinash’s article of the same name, where he describes his journey from type-less to typed languages and why he is finding it harder to refactor his Python.


(`是也乎:`

这时, 其实可以退回 Py 2.7 继续使用的...

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python Parquet 和 Arrow: 将 PyArrow 与 Pandas 结合使用](https://pycoders.com/link/10343/web)
    + JOHN LOCKWOOD

Parquet and Arrow are two Apache projects available in Python via the PyArrow library. Parquet is column-oriented storage format for arrays and tables of data, while Arrow is an in-memory columnar format for data analysis. This article describes how to use them and how they compare to Pandas DataFrames.

- [如何将 Python 列表或可迭代对象拆分为块](https://pycoders.com/link/10350/web)
    + REAL PYTHON

This tutorial provides an overview of how to split a Python list into chunks. You’ll learn several ways of breaking a list into smaller pieces using the standard library, third-party libraries, and custom code. You’ll also split multidimensional data to synthesize an image with parallel processing.


(`是也乎:`


![Split](https://ipic.zoomquiet.top/2023-02-15-zshot%202023-02-15%2010.10.52.jpg)
)


- [避免使用 Cython 的一些原因](https://pycoders.com/link/10341/web)
    + ITAMAR TURNER-TRAURING

Cython lets you seamlessly merge Python syntax with calls into C or C++ code, making it easy to write high-performance extensions, but it is not the best tool in all circumstances. This article goes over some of the limitations and problems with Cython, and suggests alternatives.

(`是也乎:`

绕了一圈, 结果还是 Rust 的广告...

)


- [Pandas Illustrated: Pandas 权威视觉指南](https://pycoders.com/link/10325/web)
    + LEV MAXIMOV

“Pandas is an industry standard for analyzing data in Python. With a few keystrokes, you can load, filter, restructure, and visualize gigabytes of heterogeneous information.” Learn all about Pandas with key illustrations to help understand the core concepts.

- [Django 4.2 中的突出特性](https://pycoders.com/link/10348/web)
    + MARIUSZ FELISIAK

Django 4.2 is slated for April and is currently in alpha release. This article covers some standout features that are coming, including psycopg v3 support, database comments, and lookups on field instances.

- [GitHub 新代码搜索背后的技术](https://pycoders.com/link/10330/web)
    + TIMOTHY CLEM

For the last year, GitHub has been making large changes to how you can search for code on their site. This article describes what went into building the world’s largest public code search index.


(`是也乎:`

是的, 开始采用 rust 了.

)



- [Python 测试工具分类/Taxonomy](https://pycoders.com/link/10349/web)
    + PYTHON.ORG

This entry in the Python wiki is an exhaustive list of testing tools and libraries. Content includes unit testing, mocking, fuzz testing, web testing, coverage tools, and much more.

(`是也乎:`

-> wiki.python.org/moin/PythonTestingToolsTaxonomy

是的, 官方维基 moinmoin 一直在使用,20多年了吧...


)


- [用 NGINX 和 Gunicorn 安全部署 FastAPI 应用程序](https://pycoders.com/link/10335/web)
    + DYLAN CASTILLO

In this tutorial, you’ll learn how to use NGINX, and Gunicorn+Uvicorn to deploy a FastAPI app, and generate a free SSL certificate for it.


(`是也乎:`

FastAPI+Gnuicorn+NGNIX 简直是最新最流行 API 构建套件了

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [rtx: 运行时执行器（asdf Rust 克隆）](https://pycoders.com/link/10347/web)
    + GITHUB.COM/JDXCODE


(`是也乎:`

asdf 也被 rust 重写了,
这一下,运行时环境的快速部署又多一个选择,
当然, 得是在真正互联网环境中,大局域网就算了..

)


- [django-admin-confirm: 用于确认更改的 Mixin](https://pycoders.com/link/10333/web)
    + GITHUB.COM/TRANGPHAM

- [tidypolars: tidyverse (R) Clone in Polars](https://pycoders.com/link/10326/web)
    + TIDYPOLARS.READTHEDOCS.IO

- [jupyter-scheduler: 将 Jupyter 笔记本作为作业运行](https://pycoders.com/link/10323/web)
    + GITHUB.COM/JUPYTER-SERVER

(`是也乎:`

这绝对是生产化 Jupyter 的方向,
真正可以作到思考/探索/开发/调试/运行/控制...
统一界面, 那开发体验可就完全不同了.

)


- [pynimate: 用于统计数据动画的 Python 包](https://pycoders.com/link/10318/web)
    + GITHUB.COM/JULKAAR9

(`是也乎:`

哈, 就是那种100年里,中国 GDP 是如何慢慢追赶上来的那种动画,
现在能自动生成了...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Dash and Data Visualisation, New Zealand Python User Group](https://pycoders.com/link/10319/web)
    + February 15, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10345/web)
     + February 15, 2023

- [PyConFr 2023](https://pycoders.com/link/10339/web)
    + February 16 to February 20, 2023

- [Python Northwest](https://pycoders.com/link/10346/web)
    + February 16, 2023

- [PyLadies Dublin](https://pycoders.com/link/10331/web)
    + February 16, 2023

(`是也乎:`

PyLadies ~ 老爹都点过赞的活动,
只是在中国没能流行起来...为什么呢?

)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 564 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-564.html)
- 修订: [issue-564.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-564.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

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

好文笔,感叹号年度配额: **0/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF564D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF564D4Q90XdDA7g):



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



