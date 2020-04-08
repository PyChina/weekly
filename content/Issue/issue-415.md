Title: Issue 415
Slug: issue-415
Date: 2020-04-08 14:42
Tags: Weekly,Python,pycoders,ZH

>  Python 编程令俺数学长进了...



原文: [PyCoder's Weekly - Issue #415](https://pycoders.com/issues/415)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200408 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200408 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Arduino 上 Python 如何开始?](https://pycoders.com/link/3897/web)
    + REAL PYTHON 
    + course

Discover how to use Arduino microcontrollers with Python to develop your own electronic projects. You’ll learn how to set up circuits and write applications with the Firmata protocol. You’ll control Arduino inputs and outputs and integrate the board with higher-level apps.

(`是也乎:`

其实有更加友好的 [MicroPython - Python for microcontrollers](https://micropython.org/) 生态哪...

)



- [最期望一早告诉俺的 有关 Python 中多进程处理的事情\[2019\]](https://pycoders.com/link/3874/web) 
    + PAMELA MCA'NULTY

Python’s multiprocessing module abstracts away a lot of the overhead involved in writing multiprocessing code in Python. But while it might be “easy” to implement multiprocessing in Python, it’s not always easy to do multiprocessing well. In this article, Pamela McA’Nulty shares five tips to help you write better multiprocessing code.

(`是也乎:`

相比多线程, 多进程已经少很多坑了..

但是, 那也比不上 Pyhton 自己不管任何 多XX ,
运行时管理丢给系统监管就好.

)



- [PyPI 新赞助计划](https://pycoders.com/link/3872/web)
    + PSF
    + PYTHON SOFTWARE FOUNDATION

The Packaging Working Group of the Python Software Foundation is launching an all-new sponsorship program to sustain and improve Python’s packaging ecosystem. Funds raised through this program will go directly towards improving the tools that your company uses every day and sustaining the continued operation of the Python Package Index.

- [pyproject.toml 到底是咩?](https://pycoders.com/link/3875/web)
    + BRETT CANNON

“I have seen setuptools users use pyproject.toml because they were ‘told to by ‘ without knowing the entire point behind the file. And so I decided to write this blog post to try and explain to setuptools users why pyproject.toml exists and what it does as it’s the future of packaging in the Python ecosystem.”

- [配置很糟? 尝试上真正的编程语言](https://pycoders.com/link/3906/web)
    + JESTEM KRÓLICZKIEM

“In this post, I’ll try to explain why I find most config formats frustrating to use and suggest that using a real programming language (i.e. general purpose one, like Python) is often a feasible and more pleasant alternative for writing configs.”

(`是也乎:`

配置和代码的边界太难以嗯哼了..
俺一直使用 .py 当配置文件使用,
直到交付其它人用时, 才发现这太容易引入无法预料的人为 bug 了...

然后, 开始各种专用配置文件的尝试...

然后... 当然又回到 .py 了哈.

)


- [2020 Q1 PSF 资深会员](https://pycoders.com/link/3909/web)
    + PSF
    + PYTHON SOFTWARE FOUNDATION

The PSF Fellow Members for Q1 2020 have been announced. Congratulations to all of the new fellows!

- [Python 2.7.18 候选版-1 已经发布](https://pycoders.com/link/3898/web)
    + PSF
    + PYTHON SOFTWARE FOUNDATION

“Python 2.7.18 will be the last release of the Python 2.7 series, and thus Python 2.” (It’s not dead, it’s resting!)
























## 讨论
> Discussions



- [Python 编程令俺数学长进了](https://pycoders.com/link/3894/web)
    + REDDIT

(`是也乎:`

广告.
)


- [完整的Python标点符号集?](https://pycoders.com/link/3881/web)
    + STACK OVERFLOW

The string module has a string called punctuation containing several different punctuation characters from the ASCII character set. But not all possible punctuation characters are contained in string.punctuation, such as fancy quotes. What’s the best way to check if any Unicode character is punctuation?

- [如何将数字四舍五入到下一个 Highest Power of 10?](https://pycoders.com/link/3900/web)
    + STACK OVERFLOW

math.ceil rounds a number to the next highest integer, but how could you round a number to the next highest power of 10 in pure Python?


(`是也乎:`

math.ceil 只能对 10进制整数作用,

)

















## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [加快 Python 异国期权定价](https://pycoders.com/link/3888/web)
    + YI DONG 
    + (NVIDIA)

“In finance, computation efficiency can be directly converted to trading profits sometimes. Quants are facing the challenges of trading off research efficiency with computation efficiency. Using Python can produce succinct research codes, which improves research efficiency. However, vanilla Python code is known to be slow and not suitable for production. In this post, I explore how to use Python GPU libraries to achieve the state-of-the-art performance in the domain of exotic option pricing.”

(`是也乎:`

简单说, 语言性能问题硬件来解决.

)



- [在 Python 中重做 StringIO 串联](https://pycoders.com/link/3903/web) 
    + JAKE EDGE

Building up a long string by repeatedly concatenating to the end of the “same” string has been considered an anti-Pattern in Python for quite some time. Since strings are immutable, each concatenation should create a new string and therefore incur a performance penalty. Learn how Python 3 optimizes this penalty away, as well as other thoughts on the topic of string concatenation, in this briefing of a recent discussion on the python-ideas mailing list.


- [3 种你应该从未用过的 Python 模板语言](https://pycoders.com/link/3886/web) 
    + MOSHE ZADKA

“Python has been around for a long time. In that time, deep in the corners of its system, it has accumulated some almost forgotten templating languages that are well worth poking at. Like cute koalas on top of a eucalyptus tree, happy in their ecological niche, and sometimes as dangerous to work with, these are the templating languages few have heard of—and even fewer should use.”


(`是也乎:`

俺总是嗯哼的:


    忘记的就是不重要的
    不知道就是不必要的

提及了 Quixote 这是豆瓣的灵魂哪...
以及: [寻找更好的模板系统记 - 魏中华 - 网易博客](http://pythonic.zoomquiet.top/data/20080923211423/index.html)

这个悬案一直没解决呢...

)


- [实效 Python 以及 Python 在 Google Scale](https://pycoders.com/link/3883/web) 
    + REAL PYTHON 
    + podcast

In this episode, Christopher interviews Brett Slatkin about the 2nd edition of his book Effective Python. Brett talks about the revisions he made for the book, and updating it for the newest versions of Python 3. Brett also discusses working on Google App Engine, and what it’s like to develop and maintain Python applications at Google Scale, and working with Guido van Rossum.

![podcast](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2012.47.30.jpg)



- [Unpacking 在 Python: 超越并行分配](https://pycoders.com/link/3871/web) 
    + LOEDANIS POZO RAMOS

“Unpacking in Python refers to an operation that consists of assigning an iterable of values to a tuple (or list) of variables in a single assignment statement. In this tutorial, [you’ll] learn what iterable unpacking is and how [you] can take advantage of this Python feature to make [your] code more readable, maintainable, and Pythonic.”

(`(￣▽￣)3:`

解包是比打包更加优雅的挑战

)



- [简介 Python 的 Linked Lists](https://pycoders.com/link/3882/web) 
    + REAL PYTHON

In this article, you’ll learn what linked lists are and when to use them, such as when you want to implement queues, stacks, or graphs. You’ll also learn how to use collections.deque to improve the performance of your linked lists and how to implement linked lists in your own projects.

(`是也乎:`

![Linked](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2012.46.36.jpg)

没有从 0 开始, 差评.


)



- [当 Python 最佳实践出错时](https://pycoders.com/link/3899/web)
    + BRANDON RHODES

“Just because a programming pattern or convention becomes popular doesn’t always mean that it’s a good idea. This talk digs into the consensus that the Python community has built around what constitutes ‘Pythonic’ code, with a focus on cases where the conventional wisdom may be wrong.”

(`是也乎:`

Pythonic 就是最好的模型...其它的都有走味儿的危险.

)


- [Python 整洁架构: 如何编写可测试的灵活代码](https://pycoders.com/link/3890/web) 
    + SEBASTIAN BUCZYŃSKI

“I wrote this blog post because I succeeded in applying the Clean Architecture in two Python projects – both of them reached production and are still being used and developed. This article contains python-specific techniques and tools helpful in embracing the Clean Architecture.”


(`是也乎:`

可测试的...这可能是 namming 之外, 最困难的一种设计目标了.

简单的说, 为了放屁,一定要事先在裤子上科学开洞.

)


- [用 Python 和 InstaPy 制作 Instagram Bot](https://pycoders.com/link/3892/web)
    + REAL PYTHON


Learn all about how to use InstaPy to create an Instagram bot that can increase your follower and like count with minimal effort on your end. Along the way, you’ll also learn about two tools that InstaPy uses under the hood: Selenium and the Page Object Pattern.

(`是也乎:`

![InstaPy](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2012.40.51.jpg)

是的, 得感激人家 ins. 一直以来的给力接口,
以及开源机制促的这么完备的模块...

)


- [面向中学生的 Python](https://pycoders.com/link/3904/web)
    + DANIEL LOWENGRUB

Stuck in quarantine with a middle schooler? Daniel Lowengrub has put together a fun lesson plan that teaches a beginner how to program in Python with numerous examples and small projects, culminating in an implementation of Tic-Tac-Toe.

(`是也乎:`

中学生的 Python ...
简化版 LPTHW ;


可能最大的困难就是如何在拥有了 Laptop 后不打游戏/刷剧/...
而来编程.

)


- [蒸蒸日上的远程开发环境](https://pycoders.com/link/3878/web)
    + TALK PYTHON 
    + podcast

“On this episode, I’ll exchange stories about working from home with Jayson Phillips. He’s been writing code and managing a team from his home office for years and has brought a ton of great tips to share with us all.”





- [理解 Django: 用户界面模板](https://pycoders.com/link/3905/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

When your Django application sends back a response with your user interface, templates are the tool you’ll use to produce that user interface. This article looks at what templates are and how to use them.

- [Django 中间件入门](https://pycoders.com/link/3880/web)
    + PAWEŁ FERTYK

“Django comes with a lot of useful features. One of them is middleware. In this post I’ll give a short explanation how middleware works and how to start writing your own.”

- [Django 和 Celery 搞掂异步任务](https://pycoders.com/link/3876/web)
    + MICHAEL HERMAN 
    + • Shared by Michael Herman

This post looks at how to configure Celery to handle long-running tasks in a Django app.


(`是也乎:`

已经是第4篇相关文章了, 看来 Celery 和 Django 是强强联合的希望

)


- [Python 3.9 中的词典合并和更新](https://pycoders.com/link/3895/web)
    + YONG CUI

- [在 CUDA 支持下构建 pyarrow](https://pycoders.com/link/3891/web)
    + RANDY ZWITCH














## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [matplotlib-3d: Matplotlib 实验性3D轴](https://pycoders.com/link/3884/web)
    + GITHUB.COM/ROUGIER


(`是也乎:`

![matplotlib](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2015.22.54.jpg)


matplotlib 虽然古老, 但是, 社区是活跃的

)


- [django-anon: 匿名你的生产数据](https://pycoders.com/link/3901/web)
    + GITHUB.COM/TESORIO • Shared by Caio Ariede

- [check-wheel-contents: Python Wheels 质量检查器](https://pycoders.com/link/3887/web)
    + GITHUB.COM/JWODDER


(`是也乎:`

车胎质量检验...

)


- [confight: 一种解析配置的简单方法](https://pycoders.com/link/3896/web)
    + GITHUB.COM/AVATURE

(`是也乎:`

叕一个配置文件内容解析器...

)

- [使用 multiprocessing 和 pytest 模拟并发写入 Sqlite3](https://pycoders.com/link/3879/web)
    + GITHUB.COM/JOEDOUGHERTY


(`是也乎:`

那什么, SQLite2/3/4/... 人家就没打算包含这种特性哪..
为什么一定触发?

)


- [NarrowEscapeSimulator: 模拟布朗运动的 Python 3 库](https://pycoders.com/link/3885/web)
    + GITHUB.COM/SIRSHARPEST

- [moderngl: 适用于 Python 的现代 OpenGL 绑定](https://pycoders.com/link/3870/web)
    + GITHUB.COM/MODERNGL

- [co2meter: 用 Python 进行 USB CO2 监控](https://pycoders.com/link/3873/web)
    + GITHUB.COM/VFILIMONOV


(`是也乎:`

利用 HomeKit 传感器?

![co2meter](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2012.08.03.jpg)

看起来外国人很担心 CO2 含量...

)


- [cliche: 从您的函数构建一个简单的命令行界面](https://pycoders.com/link/3907/web)
    + GITHUB.COM/KOOTENPV

(`是也乎:`


![cliche](http://ydlj.zoomquiet.top/ipic/2020-04-08-ScreenShot%202020-04-08%2012.04.54.jpg)


叕一个 CLI 工具框架, 装饰器配合 doc-string

)



















## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon US 2020 (Remote)](https://pycoders.com/link/3908/web)

(`是也乎:`

你说 zoom 的股票能不涨嘛?

)



- [⋅ Virtual Nationwide Django Meetup](https://pycoders.com/link/3893/web)
    + April 15, 2020

(`是也乎:`

怪不得 Django 是老大呢...

)











## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp7py 已开始报名(能开发票 ;-)

参考: 余晟以为 的推荐
[关于在本公众号进行付费阅读的通知](https://mp.weixin.qq.com/s/XznOVioOzThdFy1NzqUM-g)








# PS:
- 首发: [Issue 415 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-415.html)
- 修订: [issue-415.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-415.md)


-------------
>> NN 3977

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

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



