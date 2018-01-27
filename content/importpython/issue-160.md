Title: 蠎加载 160
Slug: importpython-160
Date: 2018-01-27 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 160](http://importpython.com/newsletter/no/160/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [Python 折腾: 如果 None 在等式左边?](http://www.pythondoeswhat.com/2018/01/none-on-left.html)
    + core-python

A natural default, None is probably the most commonly assigned value in Python. But what happens if you move it to the left side of that equation?


(`是也乎:`


经典不折腾要死星人的游戏...

)

- [理解 Python 类内部](https://rushter.com/blog/python-class-internals/)
    + core-python

The goal of this series is to describe internals and general concepts behind the class object in Python 3.6. In this part, I will explain how Python stores and lookups attributes. I assume that you already have a basic understanding of object-oriented concepts in Python.

(`是也乎:`

叕一次尝试嗯哼 class 的行为

)


- [如何将 PyLint 集成到自己的 PyCharm 工作流 ?](https://medium.com/@wbrucek/how-i-integrated-pylint-into-my-pycharm-workflow-47047ce5e7fd)
    + pycharm

PyCharm has it’s own built-in linting, which is already useful and nicely integrated. However, it misses much that PyLint catches. In this post I explain how I integrate PyLint into PyCharm as an external tool, with links from the PyLint results back to the python file.

(`是也乎:`

叕一个 PyLint 技巧

)


- [使用 Python 进行哈佛大学研究课程 - MOOC](https://www.edx.org/course/using-python-research-harvardx-ph526x-0)
    + course

Take your introductory knowledge of Python programming to the next level and learn how to use Python 3 for your research.

(`是也乎:`

叕一个春虅大学的 MOOC

)

- [用 Tensorflow 对象检测在 Android 上检测皮卡丘](https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd)
    + tensorflow


Deep inside the many functionalities and tools of TensorFlow, lies a component named TensorFlow Object Detection API. The purpose of this library, as the name says, is to train a neural network capable of recognizing objects in a frame, for example, an image.


(`是也乎:`

Pikachu 已经正式成为现实世界物种了?

)


- [集群上的分布式 Pandas 中折腾 Dask DataFrames](http://matthewrocklin.com/blog/work/2017/01/12/dask-dataframes)
    + pandas

Dask Dataframe extends the popular Pandas library to operate on big data-sets on a distributed cluster. We show its capabilities by running through common dataframe operations on a common dataset.

(`是也乎:`

叕叕叕又一个 Dataframe 的嗯哼,
这次分布式了...

)


- [Pangeo: 云上的 JupyterHub, Dask, 以及 XArray](https://matthewrocklin.com/blog//work/2018/01/22/pangeo-2)
    + geo

A few weeks ago a few of us stood up pangeo.pydata.org, an experimental deployment of JupyterHub, Dask, and XArray on Google Container Engine (GKE) to support atmospheric and oceanographic data analysis on large datasets. This follows on recent work to deploy Dask and XArray for the same workloads on super computers. This system is a proof of concept that has taught us a great deal about how to move forward. This blogpost briefly describes the problem, the system, then describes the collaboration, and finally discusses a number of challenges that we’ll be working on in coming months.

(`是也乎:`

Jupyter 的生态越来越丰富了...

)


- [pyclbr](https://pymotw.com/3/pyclbr/)
    + core-python, packages

pyclbr can scan Python source to find classes and stand-alone functions. The information about class, method, and function names and line numbers is gathered using tokenize without importing the code.


(`是也乎:`

这个可以有 ;-)

Py3 内建模块的工程支持工具.
再结合 Graphviz 就是工程代码图谱了...

)

- [Python 3.7 数据类简介](https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517)
    + core-python, 3.7

A Brand-new feature in Python 3.7 is “Data Classes”. Data classes are a way of automating the generation of boiler-plate code for classes which store multiple properties.

(`是也乎:`

多重属性类的生成

)


- [Learn Leap Fly: 用 Python 和 Kjell Wooding 提升全球读写能力 – Episode 145 – Podcast.__init__](https://www.podcastinit.com/learn-leap-fly-with-kjell-wooding-episode-145/#utm_source=rss&utm_medium=rss)
    + podcast

Learning how to read is one of the most important steps in empowering someone to build a successful future. In developing nations, access to teachers and classrooms is not universally available so the Global Learning XPRIZE serves to incentivize the creation of technology that provides children with the tools necessary to teach themselves literacy. Kjell Wooding helped create Learn Leap Fly in order to participate in the competition and used Python and Kivy to build a platform for children to develop their reading skills in a fun and engaging environment. In this episode he discusses his experience participating in the XPRIZE competition, how he and his team built what is now Kasuku Stories, and how Python and its ecosystem helped make it possible.

(`是也乎:`

Kivy 构建的教育支持平台...

)



- [用 Python 进行 Linux 系统挖掘](http://echorand.me/linux-system-mining-with-python.html)
    + platform module

In this article, we will explore the Python programming language as a tool to retrieve various information about a system running Linux. Let's get started.


(`是也乎:`

Glance 你值得拥有...

)

- [Google Colab Free GPU 教程](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d)
    + pytorch

Now you can develop deep learning applications with Google Colaboratory -on the free Tesla K80 GPU- using Keras, Tensorflow and PyTorch.


(`是也乎:`

Google 全家桶也支持 PyTorch 了...

)



- [在 TensorFlow 中使用 tf.Print()](https://towardsdatascience.com/using-tf-print-in-tensorflow-aa26e1cff11e)
    + tensorflow

Today I’ll show how TensorFlow’s print statements work, and how to make the most of them, hopefully saving you some confusion along the way.

- [在Python中处理时间戳和时区转换](https://medium.com/@jmarhee/handling-timestamps-and-timezone-conversion-in-python-3d7cc5759088)
    + datetime



## 好物
~ 包/模块/库/片段...


- [safeyaml](https://github.com/imbal/safeyaml)
    - 54 Stars, 3 Fork

SafeYAML: A linter for YAML-favoured JSON (& autoformatting too!)

(`是也乎:`

叕一个 Ymal/JSON 相互转换的工具..

)


- [simple_tensorflow_serving](https://github.com/tobegit3hub/simple_tensorflow_serving)
    - 34 Stars, 3 Fork

Generic and easy-to-use serving service for machine learning models.

- [NapkinML](https://github.com/eriklindernoren/NapkinML)
    - 27 Stars, 5 Fork

A tiny lib with pocket-sized implementations of machine learning models in NumPy.




-[loaf](https://github.com/NickBeeuwsaert/loaf)
    - 19 Stars, 0 Fork

A Slack Client written in Python wtih Urwid.

(`是也乎:`

叕一个 Slack 客户端..

![loaf](https://github.com/NickBeeuwsaert/loaf/raw/master/screenshot.png)

当然, CLI 的..

)


- [list-lambdas](https://github.com/epsagon/list-lambdas)
    - 17 Stars, 1 Fork

Enumerate Lambda functions across all regions with useful metadata.

(`是也乎:`

![examples](https://github.com/epsagon/list-lambdas/raw/master/examples/cli.png)

对 AWS 不同 region 的不同运行版本无奈之下的工具...

)


- [mini-docker](https://github.com/fireflyc/mini-docker)
    - 10 Stars, 2 Fork

A tiny container.

(`是也乎:`

那么 Docker 已经标准化了, 再山寨...

![mini](https://github.com/fireflyc/mini-docker/raw/master/screenshot/v01.gif)

果断还是国人嗯哼的...

)

- [mango](https://github.com/legshort/mango)
    - 7 Stars, 1 Fork

Python BDD Pattern.

- [aws_products](https://github.com/palsarma/aws_products)
    - 7 Stars, 2 Fork

Script to retrieve the list of AWS Services and their one-line descriptions.

(`是也乎:`

叕一个 AWS 运营工具.

)


- [function-storage-example](https://github.com/alexellis/function-storage-example)
    - 4 Stars, 1 Fork

Serverless Functions storage tutorial with Minio and OpenFaaS.

(`是也乎:`

![Minio+OpenFaaS](https://camo.githubusercontent.com/ac9e19eb39751b57997ced32b1940589774a900e/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a4339383435536c79616154315f787241474f425552672e706e67)

`FaaS` 又开始嗯哼了...

)




- [TrafficSignDetection](https://github.com/caoyuan0816/TrafficSignDetection)
    - 4 Stars, 0 Fork

A Traffic Sign Detection System Written by Python (SVM Classifier). 

(`是也乎:`

交通标志识别系统.py

只是对于中国的应该不嗯哼了...

)

### (￣▽￣)

*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...

- [gaojiuli/gain: Web crawling framework based on asyncio for everyone.](https://github.com/gaojiuli/gain)
- [zhoubear/open-paperless: Scan, index, and archive all of your paper documents](https://github.com/zhoubear/open-paperless)

![screenshot](https://github.com/Qix-/better-exceptions/raw/master/screenshot.png)

<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180127 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180127 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


