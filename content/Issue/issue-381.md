Title: Issue 381
Slug: issue-381
Date: 2019-08-14 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #381](https://pycoders.com/issues/381)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------


- [用 Python 进行`传统`人脸检测](https://pycoders.com/link/2265/web)
    + REAL PYTHON 
    + video

In this course on face detection with Python, you'll learn about a historically important algorithm for object detection that can be successfully applied to finding the location of a human face within an image.


(`是也乎:`


![Face Detection](https://ipic.zoomquiet.top/2019-08-14-ScreenShot%202019-08-14%2010.44.51.jpg)


当然, 现在 BAT 都有自己云 AI 了,
直接调用, 就不用本地生撸了...

)


- [Python 中的三种反转控制技术](https://pycoders.com/link/2250/web)
    + DAVID SEDDON

Inversion of Control, in which code delegates control using plugins, is a powerful way of modularising software. It may sound complicated, but it can be achieved in Python with very little work. This article examines three different techniques for handling IOC in Python.

(`是也乎:`

IoC ~ 委托控制插入...

模块化软件的有效手段, 
其实就是插件技术, 只是在代码层面上的...

大约是:

依赖注入,注册,猴补丁, 这几个思路.

)



- [NumPy 1.17.0 不再支持 Python 2](https://pycoders.com/link/2266/web)
    + MAIL-ARCHIVE.COM

"The 1.17.0 release contains a number of new features that should substantially improve its performance and usefulness. The Python versions supported are 3.5-3.7, note that Python 2.7 has been dropped."

(`是也乎:`

爱过...

)


- [print() 函式深挖 (17,000 字指南)](https://pycoders.com/link/2257/web)
    + REAL PYTHON

Learn all there is to know about the print() function in Python and discover some of its lesser-known features. Avoid common mistakes, take your "hello world" to the next level, and know when to use a better alternative.

(`是也乎:`

深挖灵魂40层,
当问打印合理无.

![print](https://ipic.zoomquiet.top/2019-08-14-ScreenShot%202019-08-14%2010.43.17.jpg)


)



- [Python 工具环境概述](https://pycoders.com/link/2249/web)
    + ADITHYA BALAJI

An opinionated guide to tooling in Python covering pyenv, poetry, black, flake8, isort, pre-commit, pytest, coverage, tox, Azure Pipelines, sphinx, and readthedocs.


(`是也乎:`

每年这种文章都得更新一下,
非常值得对比检验自己武器库是否合理的:

    Python 工具全景图

)


- [通过从头开始编写异步 Web 框架来剖析其工作原理](https://pycoders.com/link/2272/web)
    + OLEH KUCHUK

(`是也乎:`

叕一则从0 开始, 手撸框架, 只为了嗯哼明白到底什么是重要的

)

## 讨论
> Discussions


- [云端远程/结对编程工具??](https://pycoders.com/link/2248/web)
    + MAIL.PYTHON.ORG

(`是也乎:`

云队友工具?



I have surveyed various cloud-based services:

    + PythonAnywhere: Py3.6, used them in London (UK) perhaps one decade 
    ago, team/"education" facility appears to work. Am checking with them...

    + ShiftEdit: have been awaiting promised credentials-email all day...

    + CodeAnywhere: 7-day trial free

    and tomorrow will be experimenting with:

    + AWS Cloud9: (apparently will run on a small, free, cloud-server)

    Then there is the possibility of installing a multi-user editor on my 
    VPS or in an OpenStack PublicCloud instance:

    + Codiad: its need for PHP puts me off (haven't used/configured that 
    language for >10yrs)

    and tomorrow will be reviewing:

    + Koding: (no longer offer their own server/services so looks-like I'll 
    have to dredge-up my inner-SysAdmin - small children should look away now!)


简单说, 没有...
不如用 zoom.us 持续开着屏幕共享,
相互用另外一个屏幕, 看对方在干什么...

有个真人陪伴的感觉就好...


)


- [谁说Python程序员没有幽默感?](https://pycoders.com/link/2253/web)
    + RAYMOND HETTINGER

(`是也乎:`

当然是隔壁 PHP 程序猿了

)


- [作为一名专家,您建议初学Python程序员避免哪些不良习惯?](https://pycoders.com/link/2259/web)
    + REDDIT


(`是也乎:`

糟点太多, 大家总结不过来了...

当然, 整体上主要就是非要将 Python 写成 C/C++/JAVA/PHP/... 引发各种不舒

)

- [Python 正在吞噬世界 (Discussion)](https://pycoders.com/link/2264/web)
    + HACKER NEWS

(`是也乎:`

外国一样喜欢标题党,
这两天这个话题很激荡...

在 Hacker New 中也引发了上百页的回复讨论...

也算证明了 Pythoneer 数量真心不少了...

)



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks




- [继承和组合: Python OOP指南](https://pycoders.com/link/2267/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn about inheritance and composition in Python. You'll improve your object oriented programming skills by understanding how to use inheritance and composition and how to leverage them in their design.


(`是也乎:`

真蟒教材

![OOP](https://ipic.zoomquiet.top/2019-08-14-ScreenShot%202019-08-14%2010.26.08.jpg)


能不用就嫑用...

)


- [Flake8 简介](https://pycoders.com/link/2263/web)
    + MIKE DRISCOLL

Flake8 is a style guide enforcement tool for Python that you can use in place of PyLint to help you find errors in your code and more closely follow PEP8. This article shows you how to get up and running with Flake8.

(`是也乎:`

至今 Python 代码静态分析市场还没完成统一...

)



- [组织 PythonPune Meetups](https://pycoders.com/link/2258/web)
    + BHAVIN GANDHI

PythonPune is a meetup group in Pune India. This blog post is about how the author got involved in organizing the meetup and what the process looks like.

(`是也乎:`

简单说  MeetUP 已经考虑到线下组织活动的所有方面,
按照应用提供的功能和指示来就好...

关键是 meetUP 在印度几乎就是 QQ 在中国的状态,
网速又能保证...
简直太 easy 了...

)



- [给小白的 Keras: 实现卷积神经网络](https://pycoders.com/link/2251/web)
    + VICTOR ZHOU

A beginner-friendly guide on using Keras to implement a simple Convolutional Neural Network (CNN) in Python.

(`是也乎:`

本家毕业前, 目测将持续将自己自学过程嗯哼为科普文章...

)


- [每个开发人员应该尽早学到什么](https://pycoders.com/link/2270/web)
    + RYLAND GOLDSTEIN

"These are a few of the things I wish they were teaching at university instead of pure theory."

(`是也乎:`

防脱发技能...

)

- [Python + OpenCV 创建交互式投影界面](https://pycoders.com/link/2243/web)
    + TSUKURU.CLUB

"Computer vision + music = life-sized rhythm games"

(`是也乎:`

早年 `好看薄` 创始人, Alex 在周游世界定居 NZ 初期创业项目就是类似的白噪音服务,
基于 github 整体 commit/fork/merge/... 真随机事件,
作为数据源来生成无限心流音乐...

可惜09年就停止运营了.

)

- [用于可解释机器学习的 Python 库](https://pycoders.com/link/2261/web)
    + REBECCA VICKERY

- [Using Django Signals to Simplify and Decouple Code](https://pycoders.com/link/2252/web)
    + ROBLEY GORI

- [测试科学代码](https://pycoders.com/link/2244/web)
    + PHILIPP JUNG

(`是也乎:`

民科代码?

)

## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [austin: 帧堆采样器 for CPython](https://pycoders.com/link/2256/web)
    + GITHUB.COM/P403N1X87

"The most interesting use of Austin is probably in conjunction with FlameGraph to profile Python applications while they are running, without the need of instrumentation. This means that Austin can be used on production code with little or even no impact on performance."


(`是也乎:`


![austin](https://github.com/P403n1x87/austin/raw/master/art/austin-tui_threads_nav.gif)


结合各种分析工具的可视化运行时分析,
也支持火焰图

)

- [jupyter-black: Jupyter Notebook 的块代码格式器](https://pycoders.com/link/2245/web)
    + GITHUB.COM/DRILLAN

(`是也乎:`

![Black](https://github.com/drillan/jupyter-black/raw/master/demo.gif)

自动 pprint 式代码排版...
不过, 对于大数据样本, 一样会卡...

)


- [moviepy: 用 Python 进行视频编辑](https://pycoders.com/link/2262/web)
    + GITHUB.COM/ZULKO

(`是也乎:`

每年都会推荐的 FFmpeg 包装补品

)


- [LibCST: 具体语法树分析器和序列化器库](https://pycoders.com/link/2247/web)
    + GITHUB.COM/INSTAGRAM

Parses Python 3.7 source code as a CST tree that keeps all formatting details (comments, whitespaces, parentheses, etc). It's useful for building automated refactoring (codemod) applications and linters.

(`是也乎:`

ins. 开源作品


)


- [chart: 无外部依赖的 Python 图表库](https://pycoders.com/link/2246/web)
    + GITHUB.COM/MAXHUMBER 
    + • Shared by Max Humber

(`是也乎:`

叕一则 CLI 图表库

    from chart import bar

    x = [500, 200, 900, 400]
    y = ['marc', 'mummify', 'chart', 'sausagelink']

    bar(x, y)

           marc: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇             
        mummify: ▇▇▇▇▇▇▇                       
          chart: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    sausagelink: ▇▇▇▇▇▇▇▇▇▇▇▇▇                              


好用.
)



- [mintotp: 20行Python 实现的最小 TOTP 生成器](https://pycoders.com/link/2255/web)
    + GITHUB.COM/SUSAM

(`是也乎:`

TOTP => Time-Based One-Time Password

囧...通过 QR 码进行检验.

)


- [mesapy: 基于 PyPy 的内存安全 Python](https://pycoders.com/link/2271/web)
    + GITHUB.COM/MESALOCK-LINUX

(`是也乎:`

PyPy 也在 Rust 化?

)

- [pip-tools: Set of Tools to Keep Your Pinned Python Dependencies Fresh](https://pycoders.com/link/2254/web)
    + GITHUB.COM/JAZZBAND

(`是也乎:`

叕一个包更新管理工具

)


- [Poetry: Python 依赖管理和包装变得轻松](https://pycoders.com/link/2268/web)
    + EUSTACE.IO

(`是也乎:`

叕一个包及运行时管理工具,
基于 toml 管理依赖/版本关系.

和 conda 类似都要代理运行,


)


- [scalpl: 在嵌套字典上无缝操作](https://pycoders.com/link/2242/web)
    + GITHUB.COM/DUCDETRONQUITO

(`是也乎:`

![scalpl](https://raw.githubusercontent.com/ducdetronquito/scalpl/master/assets/scalpl.png)

专注多层嵌入字典的使用

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ PyBay](https://pycoders.com/link/2236/web)
    + August 15 to August 19, 2019
    + 三潘

- [⋅ PyCon Korea 2019](https://pycoders.com/link/2239/web)
    + August 15 to August 19, 2019
    + 宇宙国

- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/2235/web)
    + August 16, 2019
    + 德国

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/2237/web)
    + August 17, 2019
    + 印度

- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/2240/web)
    + August 20, 2019
    + 多米尼加
    + 网站已失效

- [⋅ Kiwi PyCon X](https://pycoders.com/link/2238/web)
    + August 23 to August 26, 2019
    + NZ, 惠灵顿 

- [⋅ IndyPy Web Conf 2019](https://pycoders.com/link/2241/web)
    + August 23 to August 24, 2019
    + WHERE: Online 



## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 第2期
    + 101camp2py

进入 ch3, 下期 190901 左右启动...

本周准备上线 `写作入门班`

- [Chromium\+APISIX GDG珠海 MeetUp \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/263962960/)
    + GDG 珠海
    + 极简汇率

- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
    + FAQ

(`是也乎:`

![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)

总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...

其实, 本质上并不是对应技术是否有什么能力,
而是相反...

)




### Jobs:
> 必须 Pythonic 相关

...

# 是也乎

- 190814 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190814 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.


> NN 3739




