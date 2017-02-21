Title: 蠎加载 112
Slug: importpython-112
Date: 2017-02-20 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 112](http://importpython.com/newsletter/no/112/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [以 Python 介绍计算机科学和编程.MIT 视频系列](https://www.youtube.com/playlist?list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA)
    + video

Introduction to Computer Science and Programming in Python is intended for students with little or no programming experience. It aims to provide students with an understanding of the role computation can play in solving problems and to help students, regardless of their major, feel justifiably confident of their ability to write small programs that allow them to accomplish useful goals. The class uses the Python 3.5 programming language.

(`是也乎:`

基于 py3.5
)

- [Python 代码仓库移入 GitHub](https://snarky.ca/the-history-behind-the-decision-to-move-python-to-github/)
    + core-python

Python core developer Brett talks about the history the decision to move Python to GitHub

(`是也乎:`

可怜的 Hg
)

- [memoryview](https://amitu.com/python/memoryview/)
    + core python

memoryview is a special type that can be used to work with data stored in other data-structures.

(`是也乎:`

又一个全新数据类型
)

- [又一个 Python-esque 类型系统: 鸭式静态类型](https://trm.io/2017/01/29/structural-subtyping-python.html)
    + mypy

I think the mypy static type checker is a fantastic initiative, and absolutely love it. My one complaint is that it relies a little too much on subclassing for determining compatibility. This post discusses nominal vs. structural subtyping, duck typing and how it relates to structural subtyping, subtyping in mypy, and using abstract base classes in lieu of a structural subtyping system.

(`是也乎:`

mypy 比 python 更快的 C++ 化ing...
)

- [无惧正则表达式](http://feeds.doughellmann.com/~r/doughellmann/python/~3/TFcEaEE9x4s/)
    + regex

(`是也乎:`

的确, 如果每天都用 Vim 进行基于正则表达式的各种表达, 自然就嗯哼了
)

- [在 Python 中使用 Apache Parquet 实现极高的并行 IO 性能](http://wesmckinney.com/blog/python-parquet-multithreading/)
    + parquet, IO

In this post, I show how Parquet can encode very large datasets in a small file footprint, and how we can achieve data throughput significantly exceeding disk IO bandwidth by exploiting parallelism (multithreading).


(`是也乎:`

![parquet_multithreaded_benchmarks](http://wesmckinney.com/images/parquet_multithreaded_benchmarks.png)

嗯哼,超越硬盘 IO 速度...
可是,现在不都在云端了? PK 的是内存速度了哪...

)

- [使用Scikit学习和Dask的两个简单的方法](http://matthewrocklin.com/blog/work/2017/02/07/dask-sklearn-simple)
    + sckit learn

This post describes two simple ways to use Dask to parallelize Scikit-Learn operations either on a single computer or across a cluster.


- [对数学嗯哼的人来学习 AI — P4 — Tensors Illustrated (和喵!)](https://hackernoon.com/learning-ai-if-you-suck-at-math-p4-tensors-illustrated-with-cats-27f0002c9b32)
    + tensorflow

This the 4th part in the series.


- [Kafka 入门](https://medium.com/@am9/getting-started-with-kafka-fec181f797d2#.lqbmkg1ju)
    + kafka

Basically in this guide we will configure a basic Kafka instance in an Ubuntu environment & write a very very basic python producer & consumer.

(`是也乎:`

卡夫卡 是西方现代派文学的宗师和探险者,表现主义大师,作品突出的是孤独感与恐惧感;
所以, 程序猿创建了 Kafka 工程来管理孤独的消息队列...
)

- [使用语音数据预测性别](https://medium.com/@jameschen_78678/predict-gender-with-voice-and-speech-data-347f437fc4da)
    + machine learning, classification

A beginner’s guide to implementing classification algorithms in Python

- [Ergonomica](https://ergonomica.github.io/)
    + shell

Ergonomica is a Python-based console language, integrating modules such as os, shutil, and subprocess into a fast, easy-to use environment. It allows for functional programming tools and operations as well as data types that would otherwise require obscure grep or sed commands.


(`是也乎:`

又一个使用纯Python 完成的 Shell 环境...
)

- [在 Google Compute Engine 中使用 Keras 进行深度学习](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058#.lbu7ghel7)
    + deep learning, keras

Inception, a model developed by Google is a deep CNN. Against the ImageNet dataset (a common dataset for measuring image recognition performance) it performed top-5 error 3.47%. In this tutorial, you’ll use the pre-trained Inception model to provide predictions on images uploaded to a web server.


- [Django Weekly Issue 26](http://djangoweekly.com/newsletter/no/26/)
    + django

Django round up for this week.




## 好物
~ 包/模块/库/片段...


- [cpython](https://github.com/python/cpython)
    - 5349 Stars, 303 Fork

The Python programming language default implementation is now on github.

(`是也乎:`

以 Python 的年龄,只有这么点儿星数,
只因投入 github 世界太迟了...
)

- [Bella](https://github.com/manwhoami/Bella)
    - 494 Stars, 53 Fork

A pure python, post-exploitation, data mining tool and remote administration tool for macOS.

(`是也乎:`

针对 mscOS 的专用工具包.

![Bella](https://github.com/manwhoami/Bella/raw/master/Screenshots/Bella%20Info.png)

能远程控制/使用各种 macOS 系统
...嗯哼, 这不就是后门嘛!?
)

- [PyTorch-Mini-Tutorials](https://github.com/vinhkhuc/PyTorch-Mini-Tutorials)
    - 112 Stars, 12 Fork

Minimal tutorials for PyTorch

- [mog](https://github.com/witchard/mog)
    - 38 Stars, 2 Fork

A different take on the UNIX tool cat

(`是也乎:`

![mog](https://github.com/witchard/mog/raw/master/mog.gif)

cat 的升级版, 支持语法颜色...

)


- [pyowl](https://github.com/vene/pyowl)
    - 31 Stars, 6 Fork

Ordered Weighted L1 regularization for classification and regression in Python

(`是也乎:`


![toy_example](https://github.com/vene/pyowl/raw/master/toy_example.png?raw=true)

所谓的 OWL

)

- [QuoraDQBaseline](https://github.com/erogol/QuoraDQBaseline)
    - 10 Stars, 5 Fork

Baseline solution to Quora Duplicate Question dataset.

Quora 重复问题数据集的基线解决方案


- [http_heartbeat_proxy](https://github.com/purepy/http_heartbeat_proxy)
    - 2 Stars, 0 Fork

A simple proxy make some service heartbeat-able. 

(`是也乎:`

不到40行的心跳代理
)


### (￣▽￣)
~ 

# 是也乎

- 170220 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170220 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


