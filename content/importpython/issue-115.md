Title: 蠎加载 115
Slug: importpython-115
Date: 2017-03-14 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 115](http://importpython.com/newsletter/no/115/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



Worthy Read

- [Fire 介绍 - 能自动生成 CLI 的嗯哼 - By Google](https://opensource.googleblog.com/2017/03/python-fire-command-line.html)
    + CLI

Today we are pleased to announce the open-sourcing of Python Fire. Python Fire generates command line interfaces (CLIs) from any Python code. Simply call the Fire function in any Python program to automatically turn that program into a CLI. The library is available from pypi via `pip install fire`, and the source is available on GitHub.

(`是也乎:`

文档在 [google/python-fire: Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.](https://github.com/google/python-fire#python-fire)

已经快 5000 星了...
)


- [用 Python 3.6 类型提示编写更好软件](http://www.daveoncode.com/2017/03/06/writing-better-software-with-python-3-6-type-hints/)
    + type annotations

Type annotations are a precious tool (especially if used in combination with an advanced IDE like PyCharm) that allow us to: write clear and implicitly documented code, prevent us from invoking methods with wrong data types (ok, actually we can do whatever at runtime since Python is a dynamic language and type hints as the name suggests is just that: an hint) and get useful code suggestions and autocompletion.


(`是也乎:`

简单的说, 追加各种 C++ 式的特性, 就是为了将 IDE 卖的更好...
)



- [简单机器学习模型5行 Python 代码](https://medium.com/@ramansah/simple-machine-learning-model-in-python-in-5-lines-of-code-fe03d72e78c6)
    + machine learning

We will test a simple Linear Regression Model by passing it training data and expecting correct output for a new input.


- [用 Facebook 的 Prophet Library 预测网站流量 ](http://pbpython.com/prophet-overview.html)
    + machine learning, forecasting

I was very interested to see that Facebook recently open sourced a python and R library called prophet which seeks to automate the forecasting process in a more sophisticated but easily tune-able model. In this article, I’ll introduce prophet and show how to use it to predict the volume of traffic in the next year for Practical Business Python. To make this a little more interesting, I will post the prediction through the end of March so we can take a look at how accurate the forecast is.

(`是也乎:`

Py+R 的一个实用库,或是说 PaaS

)

- [Generator 清理](http://amir.rachum.com/blog/2017/03/03/generator-cleanup/)
    + generators

What happens if you close the generator instead of throwing an exception?

(`是也乎:`

生成器关闭后...
)


- [俺的经验: 基于长运行时 芹菜 发布的微服务](https://theblog.workey.co/my-experiences-with-a-long-running-celery-based-microprocess-b2cc30da94f5)
    + celery

While Celery is well-maintained, it’s not easy to find examples of advanced patterns of real-world usage. Also it’s often been difficult to find solutions to issues that we’ve come across. So I want to share some of our experiences.

(`是也乎:`

又一个重病芹菜依赖症团队的嗯哼...
)


- [知识 Bootstrapping](https://medium.com/@NikitaVoloboev/knowledge-bootstrapping-36c97e0dee19#.c0e9kmpqp)
    + mindmap

A little offtopic but enjoyed reading it. Do check 

https://github.com/nikitavoloboev/research/




- [Python 中使用 ctypes 导入:解决溢出问题](https://www.cossacklabs.com/blog/fighting-ctypes-overflows.html)
    + ctypes

- [在Jupyter可重复的数据分析](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)
    + jupyter

- [使用Python构建微服务 第一部分](https://medium.com/@ssola/building-microservices-with-python-part-i-5240a8dcc2fb)
    + microservices
Nowadays it is a common practice to work in smaller applications, sharing the responsibility among many different services. I believe it is critical to have some standard tools between the teams working solving those problems. Note here is the link to Part II https://medium.com/@ssola/building-microservices-with-python-part-2-9f951199094a


- [用 Python 寻找免费食物](http://jamesbvaughan.com/python-twilio-scraping/)
    + scraping

Postmates regularly does promotions where they offer free food and waive the delivery fee for certain restaurants. I recently realized that I could make this simpler by creating something that would track the Postmates website and notify me of deals.


- [用 Python 解析维基百科全数据 XML 转储](http://www.heatonresearch.com/2017/03/03/python-basic-wikipedia-parsing.html)
    + xml, parsing

Note - My college project 11 years back did the same thing using C++. Today if I were to attempt the same problem I might look at using mapreduce / spark.

(`是也乎:`

作者用 C++ 作过, 现在用 py 来...
)


- [Python Datetime 获取月范围](https://www.codingforentrepreneurs.com/blog/datetime-monthly-ranges/)
    + datetime

- [HackerRank 二元搜索: 冰淇淋店](http://thisthread.blogspot.com/2017/03/hackerrank-binary-search-ice-cream.html)
    + algorithms




## 好物
~ 包/模块/库/片段...

- [qiskit-api-py](https://github.com/IBM/qiskit-api-py)
    - 117 Stars, 15 Fork

A Python library for the Quantum Experience API

- [xweb](https://github.com/gaojiuli/xweb)
    - 86 Stars, 10 Fork

Web framework written in very little code.

(`是也乎:`

![logo](https://github.com/gaojiuli/xweb/raw/master/logo.png)

文件比 bottle 多10倍,
文档比 bottle 少10倍...


)

- [simon](https://github.com/hcyrnd/simon)
    - 69 Stars, 2 Fork

Simple macOS menubar system monitor, written in Python3.6 + pyobjc.

(`是也乎:`

用 py 3.6 进行 macOS 的菜单监察
)

- [travis-pls](https://github.com/naftulikay/travis-pls)
    - 47 Stars, 3 Fork

A utility for disturbing standard output to keep Travis jobs alive.

(`是也乎:`

github 的三级工具也出来了
)

- [DeepAA](https://github.com/OsciiArt/DeepAA)
    - 27 Stars, 3 Fork

make Ascii Art by Deep Learing

(`是也乎:`

ai 的 ASCII 艺术创作...

![DeepAA](https://camo.githubusercontent.com/fe8c220256088ad932864ace9e1c3940723b0fb2/687474703a2f2f692e696d6775722e636f6d2f726173615951692e706e67)

)

- [pytorch-dqn](https://github.com/transedward/pytorch-dqn)
    - 22 Stars, 1 Fork

Deep Q-Learning Network in pytorch.

- [scrabble](https://github.com/benjamincrom/scrabble)
    - 16 Stars, 0 Fork

Implements Scrabble. Also allows user to recover all game moves from given board and score list as well as brute-force find best move.

(`是也乎:`

拼字游戏, 基于 AI
)


- [parade](https://github.com/bailaohe/parade)
    - 3 Stars, 0 Fork

A data processing engine and service. 
一个数据处理引擎和服务


### (￣▽￣)
~ 

# 是也乎

- 170314 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170314 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


