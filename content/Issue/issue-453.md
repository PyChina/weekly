Title: Issue 453
Slug: issue-453
Date: 2020-12-30 11:42
Tags: Weekly,Python,pycoders,ZH


> 从一千万Jupyter Notebooks中发现...


原文: [PyCoder's Weekly - Issue #453](https://pycoders.com/issues/453)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201230 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201230 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [用 nvc++ 和 Cython 在 GPU 上加速 Python](https://pycoders.com/link/5435/web)
    + ASHWIN SRINATH

Python on GPUs has become a big topic for processing big data and scientific computing. In this article from the NVIDIA Developer Blog, you’ll learn how to leverage C++ in Python using Cython and the nvc++ library. There’s even a real-world example that illustrates the Jacobi method to solve a heat equation.



- [从 Github 下载了 10,000,000 Jupyter 笔记本: 学到的东西](https://pycoders.com/link/5410/web)
    + ALENA GUZHARINA

The JetBrains Datalore team downloaded ten million Jupyter Notebooks and analyzed them to determine things like which languages were the most popular, what kinds of content are in notebook cells, and how consistently notebooks can be reproduced. It’s a fascinating look into trends in data science technology!


(`是也乎:`

千万级别的 Jupyter 流行度分析.

![Jupyter](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2012.41.52.jpg)

这很 JetBrain

![alert](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2012.45.28.jpg)
)




- [Django 管理员自定义](https://pycoders.com/link/5420/web)
    + REAL PYTHON 
    + course

Learn how to customize Django’s admin with Python. You’ll use AdminModel objects to add display columns, calculate values, link to referring objects, and search and filter results. You’ll also use template overriding to gain full control over the admin’s HTML.

- [解答布尔运算](https://pycoders.com/link/5428/web)
    + BRETT CANNON

In the latest entry to his series on syntactic sugar, Brett Cannon explores boolean expressions. You’ll learn how boolean expressions “short circuit” and, as an unexpected bonus, a peek into how CPython “cheats” at variables.

- [值得了解:2020年十大Python库](https://pycoders.com/link/5415/web)
    + ALAN DESCOINS

This listicle is full of Python projects that you really should know about! Each library on the lists was launched or popularized in 2020 and has seen steady maintenance since its launch. Lots of great projects here!

(`是也乎:`

Typer 绝对是惊喜,
作为 FastAPI 的 CLI 版本,
感觉只是游戏之作,
但是, 在 CLICK 之上, 融合 FastAPI 的气质,
立即大热...


当然, 俺还是用 Invoke(来自 Febric 的习惯...)

![Top 10](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2012.36.46.jpg)

tryolabs.com
每年总结 top10 模块, 已经有年头了,
品味没毛病.

)


- [2020 年 Real Python 创作回顾](https://pycoders.com/link/5424/web)
    + REAL PYTHON
    + podcast

It’s been quite the year! The Real Python team has written, edited, curated, illustrated, and produced a mountain of Python articles this year. This year-end wrap-up shares a collection of articles that showcase a diversity of Python topics.

(`是也乎:`

![Articles](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2012.33.24.jpg)

有妺 ;-)

真蟒年回顾...

Tkinter 居然还是主流...

)


- [Pandas 1.2.0的新功能](https://pycoders.com/link/5422/web)
    + PYDATA.ORG





## 探讨/吐糟
> Discussions


- [您如何发音 “Char”?](https://pycoders.com/link/5423/web)
    + REDDIT

Charcoal? Chair? Car? Tupple? Two Pull? Sequel? Squeal? Why not end the year with a hearty discussion about pronunciation? (By the way… it’s “care.”)

(`是也乎:`

今年 PyCon中国, 上海大会, 有专门纠正发音的主题:

[\[PyCon China 2020\] Python 技术名词发音指南 - 李辉_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/av500467054/)

)


- [30 年 Python 开发行为可视化](https://pycoders.com/link/5418/web)
    + REDDIT

(`是也乎:`

头些年, 老爹单人调用全球

![guido](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.18.20.jpg)

现在, 灿若星河...

![pythonista](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.21.00.jpg)


其中有多少中国人的身影呢?

)


## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [NumPy Illustrated: NumPy 视觉指南](https://pycoders.com/link/5416/web)
    + LEV MAXIMOV

This illustrated guide to NumPy is a great way to learn NumPy or brush up on the package. Full of great visual aides, this tutorial covers all the basics and more!

(`是也乎:`

NumPy 是隐身大佬,是否值得深入看场景.

)


- [隔离 Python 子解释器](https://pycoders.com/link/5442/web)
    + VICTOR STINNER

In this post, Victor Stinner takes a look back at the progress made on isolating Python subinterpreters in 2019 and 2020. You’ll learn about the technical challenges that have been solved, the current status of the project, and what the future holds.


- [蟒之禅: 深度文章](https://pycoders.com/link/5425/web)
    + ABDUR-RAHMAAN 
    + JANHANGEER

Claiming to be “the most in-depth article about the Zen of Python,” this post covers the history of the Zen as told through comments from Guido van Rossum, Tim Peters, Barry Warsaw, and other Python heavyweights.

(`是也乎:`

当年大家联合翻译过很多版本, 俺的

    美丽好过丑陋,
    浅显好过隐晦,
    简单好过复合,
    复合好过复杂,
    扁平好过嵌套,
    稀疏好过密集,
    可读性最重要,
    即使祭出实用性为理由,
        特例也不可违背这些规则.

    不应默认包容所有错误,
        得由人明确的让它闭嘴;

    面对太多的可能,不要尝试猜测;
    应该有一个(且唯一)直白的解决方法;
    当然,找到这个方法不是件容易的事
        ~谁叫你不是荷兰人呢?
    但是: 现在就做比永远不做要好;

    若实现方案很难解释,
    那么它就不是一个好方案;
    反之也成立;-)

    名称空间是个绝妙想法.

    --现在就来共同体验和增进这些吧!

)


- [Python 和MySQL数据库: 实用介绍](https://pycoders.com/link/5414/web)
    + REAL PYTHON

Learn how to connect your Python application with a MySQL database. You’ll design a movie rating system and perform some common queries on it. You’ll also see best practices and tips to prevent SQL injection attacks.

(`是也乎:`


![MySQL](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.51.16.jpg)


是的, 无论 ProstgreSQL 多强大,
日常还是 `俺的SQL` 最常见.


![scheme](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.52.55.jpg)

这种关系设计, 也是苦手之一

)


- [在 Pandas 中建立索引和选择](https://pycoders.com/link/5433/web)
    + MATT WRIGHT

Selecting and indexing items from pandas Series and DataFrame objects can be confusing. This article gives you a lucid breakdown of three ways to select elements from pandas objects and explains the differences between each one.

(`是也乎:`

Pandas 这方面作的最舒服了, 
异常直觉,
只是, 空间浪费太大了...

)



- [Web 身份验证方法比较](https://pycoders.com/link/5434/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

Take a look at commonly used methods for handling web authentication for Python web development including the pros and cons of each method. You’ll see how to apply different methods to the Flask, Django, and FastAPI frameworks.

(`是也乎:`

自举的文章, 一般都不错.

)


- [用 Cerberus 在 Python 中验证数据](https://pycoders.com/link/5439/web)
    + HECTOR CASTRO

Thanks to an Advent of Code challenge, author Hector Castro was exposed to the Cerberus Python package for data validation. Get a quick introduction to Cerberus and see Hector’s solution to an Advent of Code challenge in this quick-yet-informative read.

- [享受撰写 Python](https://pycoders.com/link/5436/web)
    + BALAJEE RAMACHANDRAN 
    + opinion

The mypy project brings static type checking to Python. This opinion piece explores the good and the bad of typed Python from the perspective of someone who wouldn’t grab Python for their day-to-day coding.

(`是也乎:`

不是 Joke 就好

)
   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [frigate: 用于 IP摄像头的实时本地对象检测 NVR](https://pycoders.com/link/5440/web)
    + GITHUB.COM/BLAKEBLACKSHEAR


(`是也乎:`

![Detection](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.39.07.jpg)


实时对象识别, 从低分辨率摄像头视频.

这是互联网视觉基础, 大规模上线时....

)



- [erpnext: SAP 的免费开源替代品](https://pycoders.com/link/5430/web)
    + GITHUB.COM/FRAPPE

(`是也乎:`

SAP ?

呵...

)


- [vit-pytorch: Single Transformer Encoder 的 SOTA 视觉分类](https://pycoders.com/link/5441/web)
    + GITHUB.COM/LUCIDRAINS

- [cerberus: 用于 Python 的轻量级和可扩展数据验证库](https://pycoders.com/link/5427/web)
    + GITHUB.COM/PYEVE

(`是也乎:`


    >>> v = Validator({'name': {'type': 'string'}})
    >>> v.validate({'name': 'john doe'})
    True

有效性检验库,
只是, JS 在入口已经完成了检验, 到 Python 这儿,
一般只有数据流水线时, 才需要?

那么, 这时, 吞吐量就是关键了.

)


- [Flask-Meld: Flask 的全栈框架](https://pycoders.com/link/5431/web)
    + GITHUB.COM/MIKEABRAHAMSEN

- [simple-graph: SQLite 中的图形数据库](https://pycoders.com/link/5437/web)
    + GITHUB.COM/DPAPATHANASIOU

(`是也乎:`

SQLite 作为内存数据库真,良心大物.

)



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5411/web)
    + December 30, 2020

(`是也乎:`

等视频流出, 
一直好奇 真蟒 团队中, 插画是专门设计师, 还是程序猿代劳?

目测, 后者可能性大.

)


- [⋅ Python Pizza New Year’s Party](https://pycoders.com/link/5432/web)
    + December 31 to January 1, 2021

(`是也乎:`


![Pizza](http://ydlj.zoomquiet.top/ipic/2020-12-30-ScreenShot%202020-12-30%2010.31.57.jpg)


我们有美好团, 很 easy 的.


)



- [⋅ BelPy](https://pycoders.com/link/5445/web)
    + January 30 – 31, 2021

(`是也乎:`

> BelPy is a conference where Python users, or people interested in Python, gather to learn from each other and meet other members of the community. This is the first edition of BelPy, and will be entirely virtual due to the present circumstances. The BelPy team is continuing to work hard on making a conference that will allow everyone to have a great time and unlock new possibilities through Python. We are really excited to have you with us!


也是在线虚拟大会...
毛里求斯 主办?

)


- [⋅ PyCascades 2021 (Virtual)](https://pycoders.com/link/5444/web)
    + February 19 – 21, 2021

- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5443/web)
    + May 12 – 18, 2021



## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

None 

# PS:
- 首发: [Issue 453 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-453.html)
- 修订: [issue-453.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-453.md)


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
>> NN 4243


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/453)






