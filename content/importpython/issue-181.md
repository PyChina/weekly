Title: 蠎加载 181
Slug: importpython-181
Date: 2018-07-30 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 181](http://importpython.com/newsletter/no/181/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [在现代基础设施上持续交付 - Kubernetes 中跑 GoCD](https://www.gocd.org/kubernetes/?utm_campaign=Kubernetes&utm_medium=newsletter_ad&utm_source=importpython&utm_content=kubernete_lp&utm_term=)
    + kubernetes, GoCD

Model Docker-based build workflows more effectively with our GoCD Kubernetes integration. Run GoCD natively on Kubernetes, define your build workflow and let GoCD provision and scale build infrastructure on the fly.




- [grumpy-runtime 发布](https://labs.getninjas.com.br/released-grumpy-runtime-v0-3-0-a05f1cf8e111)
    + go, cpython

The Golang-made Python "interpreter" is now installable via pip on Linux, macOS and Android. Featuring a more near-drop-in replacement of CPython than before.

(`是也乎:`

为了解决 Py 的运行速度问题, go 是必须浪一下的

)


- [Python 的全局变量](https://punchagan.muse-amuse.in/blog/python-globals/)
    + core-python

(`是也乎:`

全局是魔鬼, 用好了也舒服

)


- [Python 正在成为世界上最流行的编程语言](https://www.economist.com/graphic-detail/2018/07/26/python-is-becoming-the-worlds-most-popular-coding-language)
    + core-python

The language’s two main advantages are its simplicity and flexibility. Its straightforward syntax and use of indented spaces make it easy to learn, read and share. Its avid practitioners, known as Pythonistas, have uploaded 145,000 custom-built software packages to an online repository. These cover everything from game development to astronomy, and can be installed and inserted into a Python program in a matter of seconds.

(`是也乎:`

怪不得老爹受气了...核心团队的心思多了...

)



- [Glances - 关注您的系统](https://nicolargo.github.io/glances/)
    + devops, system monitoring

Glances is a cross-platform system monitoring tool written in Python.

(`是也乎:`

早就用起来了, 非常爽直的工具桟, 
而且可以全部用 py 调用到...

)


- [Termgraph](https://github.com/mkaz/termgraph)
    + charts, command line

A python command-line tool which draws basic graphs in the terminal.

(`是也乎:`

    $ termgraph.py data/ex1.dat

    # Reading data from data/ex1.dat

    2007: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 183.32
    2008: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 231.23
    2009: ▇ 16.43
    2010: ▇▇▇▇ 50.21
    2011: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 508.97
    2012: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 212.05
    2014: ▏ 1.00


非常实用的 CLI 工具,py3 only

)



- [在2018 终结 Python 的依赖性地狱 – tech-at-instacart](https://tech.instacart.com/freezing-pythons-dependency-hell-in-2018-f1076d625241)
    + dependency management

A simpler solution for a complicated problem by folks at Instacart.

- [教程: Python 中的量子计算入门 (第一部分)](http://dataespresso.com/en/2018/07/22/Tutorial-Generating-random-numbers-with-a-quantum-computer-Python/)
    + Quantum computin

Quantum computers might sound a bit exotic and far into the future, but in reality, they are now accessible in the cloud or through emulators for everyone to write quantum code. In this tutorial, we’ll go through how you can program a simple quantum computer to generate random numbers. This example can be done on any emulator or quantum computer. For this blog post, the free and open source Python library ProjectQ is used. ProjectQ can emulate a quantum computer on any CPU, or connect to IBMs quantum computer as a backend.

(`是也乎:`

因为 量子计算机没有 GIL 问题?

)


- [初学者 Python 测试指南](https://miguelgfierro.com/blog/2018/a-beginners-guide-to-python-testing/)
    + paper

Test development is key for most software projects. In this post, we are going to discuss 4 different tests: unit tests, smoke tests, integration tests and utility tests. In simple words, unit tests make sure that each class or function behaves as it should, smoke tests make sure that the system works, integration tests make sure that the program results are acceptable and utility tests give an example on how to use a class or function. We will show how to work with these tests in Python.




- [Django-Rok : 发布本地 Web 服务的公共 URL](https://medium.com/@ankurj630/django-rok-public-url-for-your-local-web-server-fec89e635282)
    + django

The django-rok is an reverse-ssh tunneling tool provides a public URL for your local web server. This is helpful in web-hook testing, quick UAT and many more.

- [用符号表达式生成随机回归和分类问题](https://towardsdatascience.com/random-regression-and-classification-problem-generation-with-symbolic-expression-a4e190e37b8d)
    + machine learning, scikit

Now, Scikit-Learn, the leading machine learning library in Python, does provide random data set generation capability for regression and classification problems. However, the user have no easy control over the underlying mechanics of the data generation and the regression output are not a definitive function of inputs?—?they are truly random. While this may be sufficient for many problems, one may often require a controllable way to generate these problems based on a well-defined function (involving linear, nonlinear, rational, or even transcendental terms).




- [为毛 Python 这么慢?](https://hackernoon.com/why-is-python-so-slow-e5074b6fe55b)
    + gil

GIL anyone?

(`是也乎:`

老调...

)



- [分析犹他州的空气质量 - 清洁和改造AQS数据 - 33 Sticks](https://33sticks.com/analyzing-utahs-air-quality-cleaning/)
    + pandas

As a lifelong Utahan, I began to wonder how bad is the pollution? The news reporters seem to think it’s pretty bad. The politicians say it’s never been better. So how bad is it? What impact does it have on things like real estate value? How many people are impacted? As we continue our series analyzing Utah’s air quality with Randy Zwitch, Senior Developer Advocate at MapD, we now turn our focus on to cleaning the data that we received from the EPA’s Air Quality API. In addition we will cover how we use the data to calculate an Air Quality Index (AQI) score and exporting the data out for import into MapD which we will use to further analyze the data.

(`是也乎:`

犹他州...

)




- [用 Python 实现遗传算法](https://www.aitribune.com/article/2018071087)
    + genetic

This tutorial will implement the genetic algorithm optimization technique in Python based on a simple example in which we are trying to maximize the output of an equation. The tutorial uses the decimal representation for genes, one point crossover, and uniform mutation.

- [Python 3.4.9rc1 发布](https://www.python.org/downloads/release/python-349rc1/)
    + new release

Python 3.4.9rc1 was released on July 19th, 2018. Python 3.4 has now entered "security fixes only" mode, and as such the only changes since Python 3.4.7 are security fixes. Also, Python 3.4.9rc1 has only been released in source code form; no more official binary installers will be produced.

(`是也乎:`

老爹主持的最后一个版本释放...

)


## 好物
~ 包/模块/库/片段...

- [pytorch_bn_fusion](https://github.com/MIPT-Oulu/pytorch_bn_fusion)
    - 34 Stars, 1 Fork

Batch normalization fusion for PyTorch

(`是也乎:`

Torch 迁移到 Py 世界后, 工具在爆发...

)


- [fridump3](https://github.com/rootbsd/fridump3)
    - 22 Stars, 4 Fork

A universal memory dumper using Frida for Python 3

(`是也乎:`

通用内存 dump 工具, 
用来尸检? 但是, 现在有活检好工具了哈...

)


- [LastMinuteFlashcards](https://github.com/FakeCola/LastMinuteFlashcards)
    - 22 Stars, 1 Fork

A command-line tool to learn GRE words with flashcards.

(`是也乎:`

徦可乐同学为了考试还是满拼的...
)


- [rockstar-py](https://github.com/yanorestes/rockstar-py)
    - 19 Stars, 5 Fork

Python transpiler for the esoteric language Rockstar


(`是也乎:`

实验作品, 嗯哼对象是 [dylanbeattie/rockstar: The Rockstar programming language specification](https://github.com/dylanbeattie/rockstar)

)

- [delete-tweets](https://github.com/QuincyLarson/delete-tweets)
    - 19 Stars, 3 Fork

Bulk-delete your past tweets before a specific date.

(`是也乎:`

准备潜逃...

)


- [opentfd](https://github.com/SlavikMIPT/opentfd)
    - 12 Stars, 0 Fork

Opensource telegram flood daemon

(`是也乎:`

电报网的工具也开始兴盛了...
)


- [Django-Styleguide](https://github.com/HackSoftware/Django-Styleguide)
    - 12 Stars, 0 Fork

Django styleguide used in HackSoft projects

- [python-ls](https://github.com/gabrielcnr/python-ls)
    - 10 Stars, 1 Fork

Think about Python's dir builtin with recursive search capabilities

(`是也乎:`

用 `ls` 命令来对自身进行挖掘...

)


- [del_gmail](https://github.com/wb14123/del_gmail)
    - 9 Stars, 0 Fork

Python script to delete mails from Gmail that match a keyword

(`是也乎:`

等等, 为什么要删除? gmail 的口号不就是:

    嫑删
    归档永备

)


- [semantic-image-inpainting](https://github.com/ChengBinJin/semantic-image-inpainting)
    - 9 Stars, 0 Fork

Tensorflow implementation of Semantic Image Inpainting with Deep Generative Models


(`是也乎:`


![a47680de2efe](https://user-images.githubusercontent.com/37034031/43245170-4eefe500-90e8-11e8-8f49-a47680de2efe.png)

嚓, 这都能自动嗯哼了?

)

- [generate-thai-lyrics](https://github.com/tupleblog/generate-thai-lyrics)
    - 9 Stars, 0 Fork

Generate Thai Songs' lyrics using Deep Learning

(`是也乎:`

等等, 为什么是泰国?

)


- [ImprovedGAN-Tensorflow](https://github.com/bruno-31/ImprovedGAN-Tensorflow)
    - 9 Stars, 0 Fork

A working Tensorflow implementation of Semi-supervised Learning GAN.

- [dark-mode](https://github.com/sdushantha/dark-mode)
    - 7 Stars, 1 Fork

Control the macOS dark mode from the terminal

(`是也乎:`

![dark](https://raw.githubusercontent.com/sdushantha/dark-mode/master/preview.gif)

只能说 macOS 的接口很友好了...

)


- [deductive-reasoning](https://github.com/lyk2018-python/deductive-reasoning)
    - 6 Stars, 5 Fork

A tool for deductive reasoning.

(`是也乎:`

演绎推理...可惜没有文档
)


- [slackcontestwatcherbot](https://github.com/p-society/slackcontestwatcherbot)
    - 3 Stars, 1 Fork

Slack bot to quickly find info on the contests across websites like CodeChef, Codeforces, Topcoder and many more. 

(`是也乎:`

Slack 是程序猿输出折腾之力的主要场景了...
毕竟现在开源项目越来越多的在其中嗯哼了

)


### (￣▽￣)

- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180730 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180730 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


