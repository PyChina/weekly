Title: 蠎加载 131
Slug: importpython-131
Date: 2017-07-01 13:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 131](http://importpython.com/newsletter/no/131/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [将 Python 语法编译为 x86-64 指令集只为好玩并无增益](http://benhoyt.com/writings/pyast64/)
    + AST

I used Python’s built-in AST module to parse a subset of Python syntax and turn it into an x86-64 assembly program. It’s basically a toy, but it shows how easy it is to use the ast module to co-opt Python’s lovely syntax for your own ends.

(`是也乎:`

简单的说, 就是内置 AST 能力的嗯哼...
)


- [如何在 Python 中设立基准性能](https://www.peterbe.com/plog/how-to-do-performance-micro-benchmarks-in-python)
    + performance

Suppose that you have a function and you wonder, "Can I make this faster?" Well, you might already have thought that and you might already have a theory. Or two. Or three. Your theory might be sound and likely to be right, but before you go anywhere with it you need to benchmark it first. Here are some tips and scaffolding for doing Python function benchmark comparisons.



- [几个俺开始用的新工具](https://medium.com/@kevinhowbrook/a-few-new-tools-i-started-using-6713a78165d7)
    + curated list
Note - Two, to be precise. Wasn't aware of python-gist myself.


- [月度 PyPI: IPython, pytest, cryptography 和 NumPy](https://medium.com/@gemnasiumapp/pypi-monthly-ipython-pytest-cryptography-and-numpy-599c1d068215)
    + pypi

Monthly PyPI digest.


- [用 Python 和 Flask 进行图像上传和审核](https://medium.com/@antoinegrandiere/image-upload-and-moderation-with-python-and-flask-e7585f43828a)
    + flask

Almost all applications contain images. Image moderation has become a necessity. We will see in this article how to moderate your images automatically.

(`是也乎:`

基于 [Realtime image moderation and nudity detection API \- Sightengine](https://sightengine.com/)
进行鉴黄...

)

- [Kruskal 的算法可视化](https://medium.com/musoc17-visualization-of-popular-algorithms/kruskals-algorithm-43e6ae27034a)
    + algorithms

Kruskal’s algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected garph. Visualisation and code snippet included.


- [在 Python 基于贝叶斯进行 AB 测试](https://medium.com/@thibalbo/coding-bayesian-ab-tests-in-python-e89356b3f4bd)
    + A/B-Testing

Back when I was getting started into Bayesian Statistics I found it hard to find some simple ready-to-use code examples to get started with probabilistic programming. Today, there are great resources available and I want to contribute with that sharing a very simple code to get started with AB Tests in Python.


- [使用 nose 以及 coverage 进行 Django 测试](https://medium.com/@Zaccc123/django-tests-with-nose-and-coverage-dff5d3633b4b)
    + django, testing

Django testing using django-nose and coverage.

- [用 scikit-learn, AWS Lambda, S3 和 Amazon API Gateway 构建接口](https://datascience.com.co/creating-an-api-using-scikit-learn-aws-lambda-s3-and-amazon-api-gateway-d9d10317e38d)
    + scikit, s3, lamda

This tutorial will help you build a classifier as a service. The classifier will be trained using iris flower data set witch consists on 3 different types of irises’ (Setosa, Versicolour, and Virginica). The rows being the samples and the columns being features: sepal length, sepal width, petal length and petal width. Scikit-learn library will be used for machine-learning algorithms.

(`是也乎:`

看起来很复杂, 但是, AWS 就是这样将元能力嗯哼好,
大家就可以自在的组合成各种嗯哼...
)

- [logzero - 简化 Python 2 和 3 的 logging](https://www.metachris.com/2017/06/logzero---simplified-logging-for-python-2-and-3/)
    + logging

I’ve just published logzero, a small Python package which simplifies logging with Python 2 and 3. It is easy to use and robust, and heavily inspired by the Tornado web framework.

(`是也乎:`


![demo_output](https://www.metachris.com/images/posts/logzero/demo_output.png)

冲这么嗯哼的 logo 就可以尝试了..

![logzero](https://www.metachris.com/images/posts/logzero/logo-text-wide-cropped.png)

)

- [使用 PyFolio，R 的 PerformanceAnalytics 和 backtrader 进行股票交易分析优化](https://ntguardian.wordpress.com/2017/06/28/stock-trading-analytics-and-optimization-in-python-with-pyfolio-rs-performanceanalytics-and-backtrader/)
    + stock trading

Curator - If you ever dreamed of writing code that makes you money while you sleep or are relaxing on a beach. On a serious note this is a solid blog post on stock reading Stock Performance analytics.


- [CPython 和 MicroPython 中的内存应用](https://lwn.net/Articles/725508/)
    + micropython

At PyCon 2017, Kavya Joshi looked at some of the differences between the Python reference implementation (known as "CPython") and that of MicroPython. In particular, she described the differences in memory use and handling between the two. Those differences are part of what allows MicroPython to run on the severely memory-constrained microcontrollers it targets—an environment that could never support CPython.


(`是也乎:`

![pycon-joshi-sm](https://static.lwn.net/images/2017/pycon-joshi-sm.jpg)

嗯哼?哲学一切都和设计哲学取舍有关...

)

## 好物
~ 包/模块/库/片段...


- [lambda-toolkit](https://github.com/lucioveloso/lambda-toolkit)
    - 71 Stars, 2 Fork

Lambda-toolkit is a lambda command line (CLI). It helps you in creating, building, DEBUG in your own machine real events, testing and deploying your lambda functions.

- [DeepLearning](https://github.com/prakritidev/DeepLearning)
    - 24 Stars, 10 Fork

This repository will contain the example detailed codes of Tensorflow and Keras, This repository will be useful for Deep Learning staters who find difficult to understand the example codes .

(`是也乎:`

又一个 示例详细代码 仓库...
)

- [gitlab-kube-deploy](https://github.com/torchbox/gitlab-kube-deploy)
    - 13 Stars, 1 Fork

Kubernetes deploy utility for Gitlab

- [hippolyte](https://github.com/ocadotechnology/hippolyte)
    - 8 Stars, 0 Fork

Tool to automate DynamoDB backups.

(`是也乎:`

<-- 鹰嘴豆
哈...
)

- [htmlBuilder](https://github.com/jaimevp54/htmlBuilder)
    - 3 Stars, 0 Fork

A beautiful html builder built with python.

(`是也乎:`

```

    from htmlBuilder.tags import *
    from htmlBuilder.attributes import Class, InlineStyle

    def my_div() -> list:

        result = Div(
            Div(
                Div(),
                P().times(4),
            ),
        ).times(2)

        return result


    a = Html(
        Body(
            my_div(),
        ),
    )

```

简单的说, 就是将html 的标签变成了函式...

)

- [Solid](https://github.com/100/Solid)
    - 0 Stars, 0 Fork

A comprehensive gradient-free optimization framework written in Python. It contains basic versions of many of the most common optimization algorithms that do not require the calculation of gradients, and allows for very rapid development using them. It's a very versatile library that's great for learning, modifying, and of course, using out-of-the-box. 

(`是也乎:`

gradient-free 优化框架...

)

### (￣▽￣)

- [被忽视的攻击面：Python package 钓鱼](http://paper.seebug.org/326/)
    + pypi

(`是也乎:`

嚓了个嚓...
)


# 是也乎

- 170701 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170701 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


