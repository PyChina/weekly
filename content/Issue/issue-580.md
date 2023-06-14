Title: 蠎周刊(PyCoder)580
Slug: issue-580
Date: 2023-06-07 11:42
Tags: Weekly,Python,pycoders,ZH


> 标准库有毛用?


原文: [PyCoder's Weekly - Issue #580](https://pycoders.com/issues/580)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230607 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230607 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [用 Python 构建你自己的人脸识别工具](https://pycoders.com/link/10924/web)
    + REAL PYTHON

In this tutorial, you’ll build your own face recognition command-line tool with Python. You’ll learn how to use face detection to identify faces in an image and label them using face recognition. With this knowledge, you can create your own face recognition tool from start to finish!


(`是也乎:`


![pycoders](https://ipic.zoomquiet.top/2023-06-07-zshot%202023-06-07%2010.50.52.jpg)

)

- [通过双因素身份验证保护 PyPI 帐户](https://pycoders.com/link/10908/web)
    + PYPI.ORG

PyPI has already added two-factor authentication for high volume projects, but now they’ve announced that all package maintainers must upgrade to 2FA by the end of 2023. This post talks about why the decision was made and what your 2FA options are.





- [用 Kivy 进行 GUI 开发](https://pycoders.com/link/10915/web)
    + FRANCIS ALI

Kivy is an open source Python library for developing desktop and mobile GUI development. It is supported on Windows, Linux, macOS, Android, and iOS. This article introduces you to Kivy and teaches you how to build your first GUI with it.


(`是也乎:`

不时冒头的古老框架,
不过, 现在大家好象注意力都在 WASM.py 了

)


- [Python 软件基金会董事会提名](https://pycoders.com/link/10917/web)
    + PYTHON SOFTWARE FOUNDATION


-----------------------------------------
## 探讨/吐糟
> Discussions

- [您如何处理大型 Python 代码库？](https://pycoders.com/link/10910/web)
    + HACKER NEWS

(`是也乎:`

用 Rust 重写? 如果有投资的话...

回答中有推荐 bazel 的...这看来是真的无法想象大型项目的具体结构了...

> ...别的语言是把小项目搞成大项目，Python 则擅长把大项目变成简单的 “小项目”。所以 python 看起来 “没有大项目”

现在回顾沈游侠的断言, 感觉还是故意的了...巨型 Py 项目的话...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [用 NumPy 获取正态分布的随机数](https://pycoders.com/link/10904/web)
    + REAL PYTHON

In this tutorial, you’ll learn how you can use NumPy to generate normally distributed random numbers. The normal distribution is one of the most important probability distributions. With NumPy and Matplotlib, you can both draw from the distribution and visualize your samples.


(`是也乎:`


![NumPy](https://ipic.zoomquiet.top/2023-06-07-zshot%202023-06-07%2010.44.26.jpg)


)


- [Python 3.13 删除了 20 个 Stdlib 模块](https://pycoders.com/link/10903/web)
    + VICTOR STINNER

Core developers are busy working on PEP 594, removing dead batteries from Python 3.13. This long post in the discussion forum highlights what work has been completed so far.

- [像不存在故障一样编写代码](https://pycoders.com/link/10934/web)
    + TEMPORAL
    + SPONSOR

Temporal is an open source programming model that can simplify your code, make your applications more reliable, and allow you to deliver more features faster. Check out the Temporal Python SDK Developer’s Guide to 
[learn more and get started →](https://pycoders.com/link/10934/web)

(`是也乎:`

不得不说, 这个厂商的 slogan 点中了内心戏...

)



- [Celery的许多问题](https://pycoders.com/link/10913/web)
    + STEVE DIGNAM

“Celery is the de facto solution for background workers and cron jobs in the Python ecosystem, but it’s full of footguns.” This article describes the problems and offers some solutions.

- [使 GIL/全局解释器锁 可选](https://pycoders.com/link/10914/web)
    + PYTHON SOFTWARE FOUNDATION

Sam Gross has outlined in the past on how to make the GIL optional in CPython. He presented at the Python Language Summit, updating on his progress and future plans in the project.

- [Python 项目的 Makefile 技巧](https://pycoders.com/link/10906/web)
    + RICARDO ANDER-EGG AGUILAR

Richard likes using Makefiles. They work great both as simple task runners as well as build systems for medium-size projects. This is his starter template for Python projects.

(`是也乎:`


Makefile 上古神器, 打通 C 世界最方便法门,
问题是....值得嘛?

)


- [在你的 Django 项目中使用 pyproject.toml](https://pycoders.com/link/10909/web)
    + PETER BAUMGARTNER

A quick tutorial on how to use a pyproject.toml file inside of your Django projects to specify dependencies.

- [用 Python 与 Kubernetes 交互](https://pycoders.com/link/10930/web)
    + FAIZANBASHIR.ME 
    + • Shared by Faizan Bashir

Discover the power of Kubernetes combined with Python! This guide delves into using the Python SDK for interacting with Kubernetes deployments and services.




- [标准库有毛用?](https://pycoders.com/link/10916/web)
    + PYTHON SOFTWARE FOUNDATION

This posting summarizes a conversation at the Python Language Summit proposing that guidelines be defined for when something should be added to the standard library.

(`是也乎:`


呵...尖锐了;

> ...大型“内置电池”标准库的最初动机不再经得起推敲

只有在企业内部才倾向使用内建模块...

)


- [Django REST 框架身份验证](https://pycoders.com/link/10912/web)
    + NIK TOMAZIC 
    + • Shared by Michael Herman

Details how to add authentication endpoints to Django REST Framework with django-allauth and dj-rest-auth.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [lmql: 语言模型的查询语言](https://pycoders.com/link/10919/web)
    + GITHUB.COM/ETH-SRI

- [DbgE: 具有子表达式断点的基于 IPdb 的调试器](https://pycoders.com/link/10927/web)
    + GITHUB.COM/ARANEGA 
    + • Shared by vincent

- [Bevy: 依赖注入框架](https://pycoders.com/link/10918/web)
    + GITHUB.COM/ZECHCODES


(`是也乎:`

奇怪 bevy 在 Rust 是一个流行游戏引擎, 在 Python 是个注入框架, 在其它语言中也应该有不同项目, 这词儿有什么亮点?

就像 Sphinx 也有很多重名项目...
)

- [django-docker-quickstart: Django-Docker 入门套件](https://pycoders.com/link/10931/web)
    + GITHUB.COM/GODD0T

(`是也乎:`

可能每家创业团队都得有自己的一个核心 Django 镜像了...

)


- [PentestGPT: GPT赋能的渗透测试工具](https://pycoders.com/link/10911/web)
    + GITHUB.COM/GREYDGL

(`是也乎:`

empowered -> 赋能,

GPT-empowered -> 这又是一个热词了...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [LambdaConf, Estes Park, CO](https://pycoders.com/link/10933/web)
    + September 16-19, 2023


(`是也乎:`

![LambdaConf](https://ipic.zoomquiet.top/2023-06-07-zshot%202023-06-07%2010.06.12.jpg)

这个会议是将所有包含 Lambda 算子的语言都纳入了范畴...

)

- [STL Python](https://pycoders.com/link/10921/web)
    +　June 7, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10902/web)
    + June 7, 2023

- [Python Meeting Düsseldorf](https://pycoders.com/link/10928/web)
    + June 7, 2023

- [Python Atlanta](https://pycoders.com/link/10922/web)
    + June 8, 2023

- [PyDay La Paz 2023](https://pycoders.com/link/10923/web)
    + June 10 to June 11, 2023





-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 528](https://weekly.pychina.org/issue/issue-528.html)
- 2021: [蠎周刊 475](https://weekly.pychina.org/issue/issue-475.html)
    + [pythonista-weekly : Pyw 502](https://weekly.pychina.org/python-weekly/pyw-502.html)
- 2020: [蠎周刊 422](https://weekly.pychina.org/issue/issue-422.html)
    + [pythonista-weekly : Pyw 452](https://weekly.pychina.org/python-weekly/pyw-452.html)
- 2019: [蠎周刊 371](https://weekly.pychina.org/issue/issue-371.html)
- 2018: [蠎周刊 320: Force](https://weekly.pychina.org/issue/issue-320.html)
- 2017: [蠎加载 127](https://weekly.pychina.org/importpython/importpython-127.html)
- 2016: [蠎加载 76](https://weekly.pychina.org/importpython/importpython-76.html)
- 2015: [蠎周刊 169](https://weekly.pychina.org/issue/issue-169.html)
    + [蠎加载 35](https://weekly.pychina.org/importpython/importpython-35.html)
- 2014: [Issue 118](https://weekly.pychina.org/issue/issue-118.html)
- 2013: 空缺
- 2012: [Issue 16 ~ 规则胜于特例](https://weekly.pychina.org/issue/issue-16.html)


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
        _~---~_
    \) /  ◕ ◵  \ (/
      '_   V   _'
      > '--~--' )

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```

-----------------------------------------
# PS:

- 首发: [Issue 580 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-580.html)
- 修订: [issue-580.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-580.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF580D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF580D4Q90XdDA7g):



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



