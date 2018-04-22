Title: 蠎加载 171
Slug: importpython-171
Date: 2018-04-22 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 171](http://importpython.com/newsletter/no/171/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [最好的 Python：从2017年到2018年收藏的一系列文章（到目前为止）](https://medium.freecodecamp.org/python-collection-of-my-favorite-articles-8469b8455939)
    + 2017, python articles

In this article, I’d like to share with you the articles I found most interesting and insightful (inspiring) last year and this year (so far). My other goal was to create a comprehensive list of the most valuable pieces for my Python students.

(`是也乎:`

老司机的私人体验, 应该就是 Py 自身真正的好物了...

)



- [Python 3.7: 介绍数据类](https://blog.jetbrains.com/pycharm/2018/04/python-37-introducing-data-class/)
    + pycharm, data classes

Python 3.7 is set to be released this summer, let’s have a sneak peek at some of the new features! If you’d like to play along at home with PyCharm, make sure you get PyCharm 2018.1 (or later if you’re reading this from the future). There are many new things in Python 3.7: various character set improvements, postponed evaluation of annotations, and more. One of the most exciting new features is support for the dataclass decorator.

(`是也乎:`

怀疑哪,  Py3 这么多激荡的变化, 是否有 IDE 厂商的嗯哼?

)



- [Qt 让 Python 令计算贴近你 - Qt Blog](http://blog.qt.io/blog/2018/04/13/qt-for-python-is-coming-to-a-computer-near-you/)
    + pyside

PySide2 – the bindings from Python to Qt – changes skin this spring. We have re-branded it as Qt for Python on a solution level, as we wanted the name to reflect the use of Qt in Python applications. Under the hood it is still PySide2 – just better.


(`是也乎:`

Qt 开源后走的一直不错, 只是太慢,
就连 IDE 都一直非常不嗯哼...这种广告都没有 subl 来的多...可想...

)



- [转换 Python ASTs 来优化](https://cypher.codes/writing/transforming-python-asts-to-optimize-comprehensions-at-runtime)
    + AST

tl;dr Python comprehensions can have duplicate function calls (e.g. [foo(x) for x in ... if foo(x)]). If these function calls are expensive, we need to rewrite our comprehensions to avoid the cost of calling them multiple times. In this post, we solve this by writing a decorator that converts a function in to AST, optimizes away duplicate function calls and compiles it at runtime in ~200 lines of code.

(`是也乎:`

不过,这种机械优化, 永远没有人工介入后, 经验加成的效果好...

)



- [Cgo 和 Python](https://www.datadoghq.com/blog/engineering/cgo-and-python/)
    + go, cpython

If you look at the new Datadog Agent, you might notice most of the codebase is written in Go, although the checks we use to gather metrics are still written in Python. This is possible because the Datadog Agent, a regular Go binary, embeds a CPython interpreter that can be called whenever it needs to execute Python code. This process can be made transparent using an abstraction layer so that you can still write idiomatic Go code even when there’s Python running under the hood.

(`是也乎:`

通过 C , go 和 python 一直灵魂相通的...

)



- [用 Python 进行机器学习的一些基本技巧和窍门](https://heartbeat.fritz.ai/some-essential-hacks-and-tricks-for-machine-learning-with-python-5478bc6593f2)
    + machine learning

We describe some essential hacks and tricks for practicing machine learning with Python.

- [在 Kubernetes 中部署深度学习 GPU 运算模型](https://blogs.technet.microsoft.com/machinelearning/2018/04/19/deploying-deep-learning-models-on-kubernetes-with-gpus/)
    + deep learning, GPU

In this tutorial, we provide step-by-step instructions to go from loading a pre-trained Convolutional Neural Network model to creating a containerized web application that is hosted on Kubernetes cluster with GPUs on Azure Container Service (AKS). AKS makes it quick and easy to deploy and manage containerized applications without much expertise in managing Kubernetes environment. It eliminates complexity and operational overhead of maintaining the cluster by provisioning, upgrading, and scaling resources on demand, without taking the applications offline. AKS reduces the cost and complexity of using a Kubernetes cluster by managing the master nodes for which the user does no incur a cost.


(`是也乎:`

这类工具一定会越来越方便的,
问题在 GPU 本身是硬件, 有固定成本, 这就是门槛了...

)


- [Python 3 cheatsheet](https://www.dataquest.io/blog/large_files/python-regular-expressions-cheat-sheet.pdf)
    + cheatsheet

(`是也乎:`

叕一则作弊条...但是, 
最靠谱的还是多用...
)


- [Python 3 到 ES6 Javascript 转译器](https://gitlab.com/metapensiero/metapensiero.pj)
    + js


(`是也乎:`

没毛病, 问题只是, 这种转换的使用场景在哪儿?
)

- [用 PySpark 进行单元测试 – CambridgeSpark](https://blog.cambridgespark.com/unit-testing-with-pyspark-fb31671b1ad8)
    + testing

I don’t particularly enjoy writing tests, but having a proper testing suite is one of the fundamental building blocks that differentiate hacking from software engineering. Sort of like sending your application to the gym, if you do it right, it might not be a pleasant experience, but you’ll reap the benefits continuously. At work we are especially big fans of the testing pyramid, and having dozens of unit tests give us the support that we need to deliver high quality software with rapid delivery to production.


(`是也乎:`

叕一个单元测试框架,



)


## 好物
~ 包/模块/库/片段...

- [import-pypi: 单一依赖模块控制.](https://github.com/miedzinski/import-pypi)
    - 146 Stars, 3 Fork

Copy pypi.py into your site-packages directory or straight into your project. Don't bother using pip, requirements.txt and all that crap.

- [BoomMine](https://github.com/ArtrixTech/BoomMine)
    - 63 Stars, 22 Fork

BoomMine - An CV-Based Minesweeper Cheat

- [tweet-generator](https://github.com/minimaxir/tweet-generator)
    - 29 Stars, 3 Fork

Train a neural network optimized for generating tweets based off of any number of Twitter users.

(`是也乎:`
等等, 这不就是 黑镜 中基于生前 SNS 内容,
自动生成交互模型的那个...

![textgenrnn_console](https://github.com/minimaxir/tweet-generator/raw/master/textgenrnn_console.gif)

)


- [PyKoSpacing](https://github.com/haven-jeon/PyKoSpacing)
    - 27 Stars, 4 Fork

Automatic Korean word spacing with Python

(`是也乎:`

![arch](https://github.com/haven-jeon/PyKoSpacing/raw/master/arch.png)

神奇哪...Korea 和古代中文类似, 没有标点时, 句逗不同, 意义不同,
所以, 终于...

)


- [rnn-text-classification-tf](https://github.com/roomylee/rnn-text-classification-tf)
    - 21 Stars, 4 Fork

Tensorflow Implementation of Recurrent Neural Network (LSTM, GRU) for Text Classification


(`是也乎:`
叕一个 TF 的实用嗯哼
)

- [certificates](https://github.com/cassiobotaro/certificates)
    - 14 Stars, 1 Fork

script to generate event certificates easily

- [QtPyConvert](https://github.com/digitaldomain/QtPyConvert)
    - 11 Stars, 2 Fork

An automatic Python Qt binding transpiler to the Qt.py abstraction layer.

(`是也乎:`

远没有达到官方内置工具的可用度...
但是, 给出了一个真正好用的方向...是的,前后兼容的 Qt 界面设计->可用代码的转换, 
一直就是个坑...
)

- [louisPy](https://github.com/louisLouL/louisPy)
    - 10 Stars, 1 Fork

A collection of handy python utilities

- [pygrape](https://github.com/Leviathan1995/pygrape)
    - 8 Stars, 2 Fork

pygrape is a python library for updating terminal output in realtime

(`是也乎:`

![pygrape](https://github.com/Leviathan1995/pygrape/raw/master/doc/HD.gif)

比专门的进度条模块更加底层

)

- [MyPythonCNN](https://github.com/BinWang-shu/MyPythonCNN)
    - 4 Stars, 0 Fork

Writing some cnn layers ans the computation graph in python

- [progress_bar](https://github.com/shijungg/progress_bar)
    - 3 Stars, 0 Fork

A simple python progress bar tool to help show your job's progress

(`是也乎:`

![color](https://github.com/shijungg/progress_bar/raw/master/color.gif)


可以说终端的能力一直在被低估...
问题是, 这类嗯哼, 得事先知道任务总量...

)


- [TopSim: 在 Py3 中针对查询有效地搜索最相似的字符串.](https://github.com/chuanconggao/TopSim)
    - 0 Stars, 0 Fork

Search the most similar strings against the query in Python 3. State-of-the-art algorithm and data structure are adopted for best efficiency. For both flexibility and efficiency, only set-based similarities are supported right now, including Jaccard and Tversky. 

(`是也乎:`

叕一个 Py 实现的搜索模块...当然, 对中文是否支持就不一定了

)

### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180422 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180422 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


