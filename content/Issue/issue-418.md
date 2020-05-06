Title: Issue 418
Slug: issue-418
Date: 2020-04-29 11:42
Tags: Weekly,Python,pycoders,ZH

> Pandas DataFrame: 使处理数据令人愉快



原文: [PyCoder's Weekly - Issue #418](https://pycoders.com/issues/418)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200429 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200429 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Python 2 最后的发布标志叕一个时代的终结](https://pycoders.com/link/4044/web)
    + RYAN DONOVAN

The final version of Python 2 has been released. As the Python community looks forward to the new era, Ryan Donovan from the Stack Overflow Blog takes some time to reflect on the transition and points out that, while support for Python 2 from official channels may be gone, the language isn’t dead. In fact, there’s reason to believe it will live on for decades to come.


(`是也乎:`

再次: 不会的, Python 2.x 足以用到下个10年...

)


- [你应该了解的 Python 3.9 新特性](https://pycoders.com/link/4045/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Python 3.9 is scheduled for release on May 10, 2020, and it’s packed full of new goodies. Explore these new features in this overview by Martin Heinz, including new dict operators, updates to the math module, new string methods, a functools.ToplogicalSorter class, and more!


(`是也乎:`

实话, 并不想知道...

一个语言不是靠追加越来越多特性存活的...

)

- [Python pickle 模块: 如何在 Python 中保存对象](https://pycoders.com/link/4032/web)
    + REAL PYTHON

In this tutorial, you’ll learn how you can use the Python pickle module to convert your objects into a stream of bytes that can be saved to a disk or sent over a network. You’ll also learn the security implications of using this process on objects from an untrusted source.


(`是也乎:`

![pickle](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.36.55.jpg)

pickle 绝对是 Python 内建模块中最迷人的一个, 
谁都忍不住溢用她...

)

- [收集指导委员会问答的问题](https://pycoders.com/link/4035/web)
    + PYTHON.ORG

As part of PyCon US 2020, the Python Steering Council will record a Q&A. They are soliciting questions from the community, so here’s your chance to get your burning questions answered!

(`是也乎:`

很认真, 也很无奈...

)

- [构造 Python 应用 (通用布局)](https://pycoders.com/link/4034/web)
    + REAL PYTHON 
    + course

This course is a reference guide to common Python application layouts and project structures for command-line applications, web applications, and more.


(`是也乎:`

![Structuring](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.33.59.jpg)

的确, Python 程序其实,非常 八股文的...

输入->处理->输出, 
没了...


)




















## 讨论
> Discussions

- [处理失败](https://pycoders.com/link/4049/web)
    + REDDIT

It’s not that professional programmers never fail. They’ve just learned how to deal with failure and recover from it—most of the time, anyway. What coping mechanisms have you come up with?

(`是也乎:`

这不就是调试嘛?

制造失败来检验正确.

)


- [俺想用一整专注 Python, 应该设定哪些目标?](https://pycoders.com/link/4048/web)
    + REDDIT

Lots of great advice for new Python programmers in this thread!

(`是也乎:`

哭述...无尽的...

其实, 最基础的, 一年以内可以用 Python 赚到钱, 那么一切目标都达到了.


)









































## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [Python 中的数字](https://pycoders.com/link/4024/web)
    + MOSHE ZADKA

Quick quiz: how many numeric data types are there in Python? If you answered “two, duh” then you might be surprised to learn that there are actually four! In addition to int and float, the fractions and decimal standard library modules implement data types used to represent fraction and decimal numbers exactly. Learn about all of Python’s numeric data types, their strengths and weakness, and how to choose the right one in this short-but-informative article from Moshe Zadka.




- [在坚实的基础上构建: 确保可复用的Docker构建Python](https://pycoders.com/link/4014/web)
    + ITAMAR TURNER-TRAURING

Docker is a popular tool for distributing applications bundled with their environments. It’s often sold as a cure to the “it worked on my machine” conundrum, but you’re not alone if you’ve found this to be a bit oversold. The issue isn’t with Docker, though. Chances are your images aren’t completely reproducible. In this tutorial, you’ll learn some best practices for creating reproducible Docker builds.


- [在 Python 中使用警告(或:什么时候例外/不是例外?)](https://pycoders.com/link/4017/web)
    + RUEVEN LERNER

Imagine you’re maintaining an open-source Python package and you’re going to release a new version with breaking changes. You warn users about those changes in documentation and even blast the info on social media channels. But wouldn’t it be great if you could warn users right in their terminal as their using your tool? Well, with Python’s warnings module, you can! How are warnings different from Python exceptions? Learn how to send and filter warnings, and why you would want to do so.

- [Python 应用中有关配置的最佳实践](https://pycoders.com/link/4023/web)
    + TOBIAS PFEIFFER

Users love being able to configure an application. But dealing with user configuration means parsing untrusted input, validating that input, and figuring out how to access it safely in all the layers of your applications. Python has a rich configuration ecosystem. Lots of articles focus on how to use various configuration formats in your Python programs but skip out on the finer details of how and when configuration should be validated. This tutorial fills in some of those gaps.

(`是也乎:`


又来...配置的确是软件工程中比较纠结的一个方面,
不过, 用好 Python 本身就足以在配置上非常自在了;

关键是克制. 嫑在配置文件中包含过多计算/判定/摄取/... 之类行为.

)

- [Python 的 Sets 简介](https://pycoders.com/link/4033/web)
    + MIKE DRISCOLL

Have you heard about Python’s set data type? A set is an unordered collection of distinct objects that support fast membership tests and can be used to remove duplicates from a sequence. Learn all about this handy data type in this beginner-friendly article from Mike Driscoll.

- [Pandas DataFrame: 使处理数据令人愉快](https://pycoders.com/link/4029/web)
    + REAL PYTHON

In this tutorial, you’ll get started with Pandas DataFrames, which are powerful and widely used two-dimensional data structures. You’ll learn how to perform basic operations with data, handle missing values, work with time-series data, and visualize data from a Pandas DataFrame.


(`是也乎:`

使用 Pandas 最大的技巧, 可能就是别怕浪费内存,
能复制时, 一定要复制, 以免纠缠

![DataFrame](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.28.12.jpg)

)


- [用 Python 和 Redis 进行速率限制](https://pycoders.com/link/4016/web) 
    + ANDREA STAGI 
    + • Shared by Andrea Stagi

This article explores rate limiting algorithms using Python and Redis, starting from a naive approach and culminate at an advanced one called Generic Cell Rate Algorithm (GCRA).




- [手动验证 DKIM签名](https://pycoders.com/link/4041/web)
    + GITHUB.COM/KMILLE

“We take an email and verify the the DKIM-Signature step by step using Python. We also take care about the signing itself (RSA). Source code included.”


(`是也乎:`

by hand 就是从头撸, 将 邮件的 DKIM 签名详细刷了一遍

)

- [用 NumPy 和 Pandas 在 Python 中创建相关矩阵](https://pycoders.com/link/4018/web)
    + ERIK MARSJA

In this tutorial, you’ll learn how to create a correlation matrix in Python with NumPy and Pandas. Plus upper & lower triangular (tables).

- [用 Docker 和 GitLab 将 Django 持续部署到 AWS EC2](https://pycoders.com/link/4038/web)
    + MICHAEL HERMAN 
    + • Shared by Michael Herman


(`是也乎:`

gitlab 在长年陪跑情况下, 终于发现了自己最大的优势,
开始加强 CI/CD 方面的功能, 
所以, 大家都来了...

)


- [在 Django 中 Roll 基于类的视图](https://pycoders.com/link/4036/web)
    + JAMES TIMMINS 
    + • Shared by James Timmins

(`是也乎:`

嗯哼? 坚持了8年, 周刊终于有越来越多来自社区的自发推荐了...
不容易.

)


- [用 Python 的 difflib 自制文件比较工具](https://pycoders.com/link/4019/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz


(`是也乎:`


嵌入在 CI/CD 过程中就很香了...

)


- [Python Context Manager 奇特案例](https://pycoders.com/link/4030/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar































## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [flpc: Forth Lisp Python 连续体](https://pycoders.com/link/4031/web)
    + GITHUB.COM/ASRP

(`是也乎:`

为了证明这一断言:

> Python is Lisp with syntactic sugar and Lisp is Forth with syntactic sugar.

于是发现了叕一个新语言;
Forth 是比 Lisp 更加极端的一门小众开发语言.

这样的代码:
```
fib <- fun[i]:
    if i < 3:
        return(1)
    return(fib(x - 1) + fib(x - 2))
```

也可以这么表达:

```
F'
[ pick1 pushi: 3 < [ drop1 1 return ] if
  pick1 1 - fib pick2 - fib + s21 drop1 return ] bind: fib
'F

```


)


- [astropy: 天文学的通用 Python 核心软件包](https://pycoders.com/link/4042/web)
    + GITHUB.COM/ASTROPY

- [twitter-ticker-tape: Raspberry Pi 通过收据打印机读取推文](https://pycoders.com/link/4043/web)
    + GITHUB.COM/HEALEYCODES

(`是也乎:`


自动读取Twitter 并打印成发票以便晚上慢慢读...

)

- [BentoML: 简化模型服务](https://pycoders.com/link/4027/web)
    + GITHUB.COM/BENTOML

- [taichi: 便携式/高性能/稀疏和可微计算的语言](https://pycoders.com/link/4020/web)
    + GITHUB.COM/TAICHI-DEV


(`是也乎:`


![太极](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.14.10.jpg)

全新语言, 专注高效完成物理引擎/粒子系统/...等等需要海量计算的动画自动生成....

已经有丰富的案例, 是的国货.
基于 Python 深度定制.


)


- [LibreLingo: 社区驱动的语言学习平台](https://pycoders.com/link/4046/web)
    + GITHUB.COM/KANTORD

(`是也乎:`

![LibreLingo](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.11.36.jpg)

这个很牛了...GPLv3;
可以拿来作各种好玩儿的东西了.

)


- [3d-photo-inpainting: 使用上下文感知的分层深度修补进行3D摄影](https://pycoders.com/link/4021/web)
    + GITHUB.COM/VT-VL-LAB


(`是也乎:`

![inpainting](http://ydlj.zoomquiet.top/ipic/2020-04-29-ScreenShot%202020-04-29%2010.09.09.jpg)

从 3D 空间的理解上自动化处理照片,
华人主力团队成果, PyTorch 为核心.

)




















## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Montréal-Python Online Hackathon](https://pycoders.com/link/4025/web)
    + May 1st to May 3rd, 2020

(`(￣▽￣):`

COVID-19 威能之下, 
大会都线上了..连 Hackathon 也在线了...
可是没有一起熬夜的小伙伴在身边, 这种连续开发就没味道了哪...

)






## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp8py 已经开始报名(能开发票 ;-)

![报名](http://ydlj.zoomquiet.top/ipic/2020-04-21-camp8py-barnner-zip.jpg)

```

课程规划:
    报名截止 2020.5.24
    正式开课 2020.5.31
    课程结束 2020.7.12

```
详情 => [蟒营™ Python 入门班第8期](https://py.101.camp/)





# PS:
- 首发: [Issue 418 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-418.html)
- 修订: [issue-418.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-418.md)


-------------
>> NN 3998

好文笔,感叹号年度配额: **1/3**

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

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```



-------------



