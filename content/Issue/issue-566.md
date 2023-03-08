Title: PyCoder 566
Slug: issue-566
Date: 2023-03-01 11:42
Tags: Weekly,Python,pycoders,ZH


> MooS ~ 模型即服务?!


原文: [PyCoder's Weekly - Issue #566](https://pycoders.com/issues/566)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230301 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230301 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------





- [用 NumPy 和线性代数编写更快的 Python 代码](https://pycoders.com/link/10401/web)
    + REAL PYTHON 
    + PODCAST

Are you still using loops and lists to process your data in Python? Have you heard of a Python library with optimized data structures and built-in operations that can speed up your data science code? This week on the show, Jodie Burchell, developer advocate for data science at JetBrains, returns to share secrets for harnessing linear algebra and NumPy for your projects.


(`是也乎:`


![PODCAST](https://ipic.zoomquiet.top/2023-03-01-zshot%202023-03-01%2009.48.43.jpg)


简单的说使用数学工具,而不是编程工具.

)

- [Python 的 Multiprocessing 性能问题](https://pycoders.com/link/10411/web)
    + ITAMAR TURNER-TRAURING

While multiprocessing allows Python to scale to multiple CPUs, it has some performance overhead compared to threading. This article details why processes have performance issues that threads don’t, ways to work around it, and a sample bad solution.

(`是也乎:`


没事儿, 用 Rust 重写一遍就好...

)


- [在 Python 中将 XML 转换为 YAML](https://pycoders.com/link/10407/web)
    + ADITYA RAJ

XML and YAML are two of the most popular text based data formats. This article teaches you how to use third-party Python libraries to convert from one to the other.

- [攻击试图交付 Rust 可执行文件的 PyPI](https://pycoders.com/link/10394/web)
    + PHYLUM.IO

- [Django 4.2 Beta 1 发布](https://pycoders.com/link/10416/web)
    + DJANGO SOFTWARE FOUNDATION




-----------------------------------------
## 探讨/吐糟
> Discussions


None ...



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks





- [ 6 大文本注释工具](https://pycoders.com/link/10409/web)
    + NEWSCATCHER

Text annotation is the process of reading natural language data and adding additional information to it in a way your program can use it. This info can be used to train models or help process the data. This article describes 6 different tools that can help you annotate your text data.


(`是也乎:`

AI 饲料厂....

)


- [pip install 从来不简单](https://pycoders.com/link/10404/web)
    + IAN WOOTTEN

Find your favorite package and turn to the readme to get it installed - it seems dead simple just a ‘pip install’ away. Nothing could possibly go wrong. Right? If you’re used to it, it is easy to forget almost all the instructions are skipping a step: using a virtual environment.

(`是也乎:`

历史遗留问题, 一堆堆的可用方案, 每一个都有自己不适合的场景...

从气势来看 PDM 是个狠人: [pdm-project/awesome-pdm: A curated list of awesome PDM plugins and resources](https://github.com/pdm-project/awesome-pdm)

)


- [如何迭代 Pandas 中的行，以及为什么不应该这么搞](https://pycoders.com/link/10415/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to iterate over a pandas DataFrame’s rows, but you’ll also understand why looping is against the way of the panda. You’ll understand vectorization, see how to choose vectorized methods, and compare the performance of iteration against pandas.

- [App Fiddle: 学习 Flask/SQLAlchemy“实战”](https://pycoders.com/link/10396/web)
    + APILOGICSERVER.GITHUB.IO 
    + • Shared by Val Huber

App Fiddle is to apps what JSFiddle is to JavaScript. Use this instance to learn Flask/SQLAlchemy, running an app in Codespaces. You can browse and explore using VSCode on the web, customize, and debug a complete project, including a database.

- [一个自以为是的 Python 样板](https://pycoders.com/link/10412/web)
    + DUARTE O.CARMO

This is Duarte’s take on what tools and practices to use for a new Python project. Includes samples for pyproject.toml, details on using pip-tools, and even the occasional Makefile.

(`是也乎:`


和其它社区规定了统一的最佳工程模板相比,
Pythonic 世界每个人都可以打造自己最舒服的模板...
虽然舒服, 但是, 对于团队协作就有点...嗯嗯嗯了...

)


- [了解 Python 元类](https://pycoders.com/link/10405/web)
    + IONEL CRISTIAN MĂRIEȘ

Metaclasses are part of the darker corners of Python and many developers avoid them. This article dives deep into how you can use them to reduce boilerplate code and build APIs.





- [在 Python 中构建 CRUD REST API](https://pycoders.com/link/10398/web)
    + FRANCESCO CIULLA

This step-by-step guide shows you how to build a REST API with Create, Read, Update, and Delete methods using Flask, SQLAlchemy, Postgres, and Docker.

(`是也乎:`

Flask+Pg+Docker ....

全部是重型武器, 讲真一个 Nginx 套个 Pg 本身就可以完成这种服务的发布吧?

)


- [60 行 NumPy 的 GPT](https://pycoders.com/link/10391/web)
    + JAY MODY

Everybody is talking about GPT, this article is actually building one. Learn how to implement a GPT model from scratch in NumPy.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [Portable Django: Django 和 Python 在单一可执行 Zip 中](https://pycoders.com/link/10393/web)
    + DJNGO.COM


(`是也乎:`

虽然是玩具级别的, 但是, 相比 Docker 一个 .zip 文件是真友好那.

以及这个域名实在聪明...

)


- [pygwalker: 将 Pandas 变成 Tableau 风格的 UI](https://pycoders.com/link/10400/web)
    + GITHUB.COM/KANARIES

(`是也乎:`

不是, 这是为什么呢? 为了卖的更好?

)


- [feast: 机器学习的特征存储](https://pycoders.com/link/10414/web)
    + GITHUB.COM/FEAST-DEV

(`是也乎:`


感觉是上世纪磁鼓式海量数据存储的复辟?

)


- [RedditVideoMakerBot: 使用一个命令创建视频](https://pycoders.com/link/10390/web)
    + GITHUB.COM/ELEBUMM

(`是也乎:`

传统人力自动内容生成器,
不过,作者的 Youtube 宣传片儿制作的真顺溜...

很难相信, 这种可以海量自动生成的短视频内容, 就是很吸粉...

)


- [modelscope: 用于 ML 学习的模型即服务平台](https://pycoders.com/link/10413/web)
    + GITHUB.COM/MODELSCOPE

(`是也乎:`

MooS ~ Model-as-a-Service,
小破球的梗儿在这儿接住了...

--> [用户协议 · 魔搭社区](https://modelscope.cn/protocol/%E5%85%B3%E4%BA%8E%E6%88%91%E4%BB%AC)

... 由阿里巴巴达摩院，联合 CCF开源发展委员会，共同作为项目发起方;

)




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [STL Python](https://pycoders.com/link/10399/web)
    + March 1, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10402/web)
    + March 1, 2023

- [PyStaDa](https://pycoders.com/link/10403/web)
    + March 1, 2023

- [Canberra Python Meetup](https://pycoders.com/link/10389/web)
    + March 2, 2023

- [Global AI Bootcamp](https://pycoders.com/link/10410/web)
    + March 2, 2023

- [Django Girls CDO Workshop 2023](https://pycoders.com/link/10395/web)
    + March 4 to March 5, 2023

- [GeoPython 2023](https://pycoders.com/link/10397/web)
    + March 6 to March 9, 2023







-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 566 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-566.html)
- 修订: [issue-566.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-566.md)

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

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF566D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF566D4Q90XdDA7g):



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



