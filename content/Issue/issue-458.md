Title: Issue 458
Slug: issue-458
Date: 2021-02-03 11:42
Tags: Weekly,Python,pycoders,ZH


> 老爹和爱豆在 Twitter 上的闲聊...


原文: [PyCoder's Weekly - Issue #458](https://pycoders.com/issues/458)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210203 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210203 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [在 Pandas 查找和修复意外的内存占用](https://pycoders.com/link/5657/web)
    + MARTIN JONES 
    + • Shared by Martin Jones

Storing string columns as categories can result in massive memory savings when working with large dataframes in pandas. However, those savings can surprisingly disappear when you start concatenating dataframes. In this article, you’ll learn why, and find out how to fix it.

(`是也乎:`

这应该也是门生意了...

)


- [Constant Folding 在 Python](https://pycoders.com/link/5669/web)
    + ARPIT BHAYANI

Every programming language aims to be performant and Python is no exception. Take a dive deep into Python internals and find out how Python makes its interpreter performant using a technique called constant folding.

(`是也乎:`

叕一种性能技巧的 Pythonic 化

)


- [用 Datadog APM 可视化/优化 Python 应用程序性能](https://pycoders.com/link/5652/web)
    + DATADOG
    + sponsor

Datadog APM generates detailed flame graphs from real requests so you can see which services or calls are generating errors or contributing to overall latency. Dive deeper into your production code with an always-on code profiler to troubleshoot. Start monitoring your applications with a free trial →

(`是也乎:`

![DATADOG](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.52.36.jpg)

用了都说好.

)


- [Pyston 2.1 超越 Python 3.8/3.9 性能](https://pycoders.com/link/5684/web)
    + MICHAEL LARABEL

Pyston is an alternative Python interpreter. According to these benchmarks, it’s significantly outperforming Python 3.8 and 3.9.

(`是也乎:`

亲侄儿, 也放弃 Py2 了?

)


- [Python 和 NumPy 实现随机梯度下降算法](https://pycoders.com/link/5674/web)
    + REAL PYTHON

Learn what the stochastic gradient descent algorithm is, how it works, and how to implement it with Python and NumPy.

- [DjangoCon Europe 2021 发布](https://pycoders.com/link/5681/web)
    + DJANGO SOFTWARE FOUNDATION

- [spaCy v3.0 发布](https://pycoders.com/link/5663/web)
    + EXPLOSION.AI

- [NumPy 1.20.0 发布](https://pycoders.com/link/5664/web)
    + NUMPY.ORG

(`是也乎:`

说这是史上最大一次合并,
改变了非常多的特性, 并放弃了对 Py3.6 以下的支持.

)


## 探讨/吐糟
> Discussions


- [Guido 和 Eric Idle 在 Twitter 上交谈](https://pycoders.com/link/5668/web)
    + TWITTER.COM/ERICIDLE

Python creator Guido van Rossum and Monty Python actor (and IDLE namesake) chat about the Python programming language on Twitter.

(`是也乎:`

程序猿和宅演员的交流...

![Monty](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.49.35.jpg)

演员关注如何生存,
程序猿关注如何改变世界...


)

## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Django 和 Pydantic](https://pycoders.com/link/5683/web)
    + NIK TOMAZIC 
    + • Shared by Michael Herman

Learn how to integrate Pydantic with a Django application using the Pydantic-Django and Django Ninja packages.

- [Python Web 应用: 将脚本部署为 Flask 应用](https://pycoders.com/link/5670/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to go from a local Python script to a fully deployed Flask web application that you can share with the world.

(`是也乎:`

![Deploy](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.46.41.jpg)

)



- [OO 在 Python 通常毫无意义](https://pycoders.com/link/5654/web)
    + LEON TROLSKI 
    + opinion

Is object-oriented programming a pointless paradigm? Maybe, maybe not. But it’s worth considering alternatives when deciding how to write your code. Read the article for an argument against OOP and then follow the Hacker News discussion for the debate.

(`是也乎:`

Python 一直其实是多范式语言,
OO 也只是可用而已.

)


- [数据库约束在 Django](https://pycoders.com/link/5675/web)
    + STEVEN PATE 
    + • Shared by Steven Pate

Learn about the various database constraints Django supports to ensure data integrity.

- [在 Python 用 Pillow 处理图像](https://pycoders.com/link/5660/web)
    + REAL PYTHON 
    + podcast

Are you interested in processing images in Python? Do you need to load and modify images for your Flask or Django website or CMS? Then you most likely will be working with Pillow, the friendly fork of PIL, the Python imaging library. This week on the show, we have Mike Driscoll, who is writing a new book about image processing in Python.

(`是也乎:`

从 PIL 变成枕头,
名字是越来越亲切的,
但是, 事儿从来没 for human 过...


![Pillow](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.45.50.jpg)
)


- [迷失在 Python Shell](https://pycoders.com/link/5658/web)
    + BAIRAKTARIS KONSTANTINOS

This is a fun little experiment aiming to mix bash and Python. While not meant to be taken too seriously, it’s an interesting look at using the subprocess module.

(`是也乎:`

无论 mix 还是 pure,
在 CLI 领域,
还是和系统结合深入的 shell 来的靠谱,
以往类似尝试都没了然后...

)



- [Plot 在 Pandas: Python 数据可视化基础知识](https://pycoders.com/link/5678/web)
    + REAL PYTHON

In this course, you’ll get to know the basic plotting possibilities that Python provides in the popular data analysis library pandas. You’ll learn about the different kinds of plots that pandas offers, how to use them for data exploration, and which types of plots are best for certain use cases.

(`是也乎:`

类似教程不少了,
但是, 基础永远是基础, 能解决入门问题就不错了,
实际使用中, 根本没可能 Basic 就满足.

)


## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [sailboat: 分发 Python 项目的快捷方法!](https://pycoders.com/link/5677/web)
    + GITHUB.COM/COLE-WILSON


(`是也乎:`


常规多渠道发行的半自动化,
能编译出 brew/pip/PyInstaller 安装包,

但是, 并没解决真正的带运行时发行问题,

用户还是必须先有可靠的本地 Python 运行时.

)

- [bleak: 适用于 Python 的蓝牙低功耗平台 Agnostic Klient](https://pycoders.com/link/5676/web)
    + GITHUB.COM/HBLDH



- [Gistfinder: 从终端模糊搜索您的 gist](https://pycoders.com/link/5662/web)
    + GITHUB.COM/ROBDMC 
    + • Shared by Rob deCarvalho


(`是也乎:`

Gists 被和谐也有年头了,
这种

)

- [schedule v1.0.0: 友好的任务日程](https://pycoders.com/link/5666/web)
    + PYPI.ORG

(`是也乎:`

for Humans 的一般都很 Pythonic,
所以, 以往 not for Humans 的都是老一辈思维已经数字化的大仙儿.

只是, 定期事务这事儿,
难的不是人性化解析,
而是如何维持自身可以真正系统级稳定活着...

)

- [Math Inspector: 用 NumPy 和 SciPy 进行科学计算的可视化编程环境](https://pycoders.com/link/5686/web)
    + MATHINSPECTOR.COM

(`是也乎:`


![Visual](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.29.26.jpg)


任何可视化计算过程的尝试,
本质上都是单向灌输?

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5679/web)
    + February 3, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ BelPy](https://pycoders.com/link/5604/web)
    + January 30 – 31, 2021

- [⋅ PyCascades 2021 (Virtual)](https://pycoders.com/link/5609/web)
    + February 19 – 21, 2021

(`是也乎:`

![Diamond](http://ydlj.zoomquiet.top/ipic/2021-01-20-ScreenShot%202021-01-20%2009.40.38.jpg)


)


- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021

(`是也乎:`

![DjangoCon](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.27.25.jpg)

浪漫的欧洲? 这是要线下了?

)


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)


# PS:
- 首发: [Issue 458 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-458.html)
- 修订: [issue-458.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-458.md)


-------------

好文笔,感叹号年度配额: **0/3**

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
>> NN 4278


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/458)






