Title: 蠎加载 135
Slug: importpython-135
Date: 2017-07-28 16:16
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 135](http://importpython.com/newsletter/no/135/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 中测试重构实际一例](http://blog.thedigitalcatonline.com/blog/2017/07/21/refactoring-with-test-in-python-a-practical-example/#.WXoHlnWGM8o)
    + refactoring

This post contains a step-by-step example of a refactoring session guided by tests. When dealing with untested or legacy code refactoring is dangerous and tests can help us do it the right way, minimizing the amount of bugs we introduce, and possibly completely avoiding them. Refactoring is not easy. It requires a double effort to understand code that others wrote, or that we wrote in the past, and moving around parts of it, simplifying it, in one word improving it, is by no means something for the faint-hearted. Like programming, refactoring has its rules and best practices, but it can be described as a mixture of technique, intuition, experience, risk.


- [波士顿地铁用 Python 的性能分析 (Pandas, Numpy, MatplotLib 以及 Seaborn)](https://medium.com/@aankul.a/performance-analysis-of-mbta-using-python-pandas-numpy-matplotlib-and-seaborn-81cbc14007a3)
    + data science

Boston’s Massachusetts Bay Transit Authority (MBTA) operates the 4th busiest subway system in the U.S. The MBTA recently began publishing substantial amount of subway data through its public APIs. I performed five analysis.


- [高效管理 Python 与 Docker 的项目依赖关系](https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/)
    + docker, dependency management

There are many ways to handle Python app dependencies with Docker. Here is an overview of the most common ones – with a twist.



- [通过 Sklearn 实现监督学习算法 - 线性回归](https://medium.com/@mayank.trp48/implementing-supervised-learning-algorithm-by-sklearn-linear-regression-96ffbdb29961)
    + supervised learning

In this blog, we will see how we can implement Supervised Learning Algorithm. Linear Regression using SkLearn Library in Python. SkLearn or scikit-learn is one of the most widely used tools for Machine Learning and Data Analysis. It does all the computation allowing you to focus on increasing the efficiency and not on the calculation part of the Algorithm.


- [TeachCraft](https://teachcraft.net/)
    + minecraft

Learn to program Python within a multiplayer world we all know and love, Minecraft!

(`是也乎:`

![mine_pyth](https://teachcraft.net/static/images/mine_pyth.png)

)

- [Quart](https://gitlab.com/pgjones/quart)
    + flask, project

Quart is a Python asyncio web microframework with the same API as Flask. Quart should provide a very minimal step to use Asyncio in a Flask app.

(`是也乎:`

叕一个针对 Py3 特性的微型 web 框架


    from quart import Quart

    app = Quart(__name__)

    @app.route('/')
    async def hello():
        return 'hello'

    app.run()

忒象 Bottle 了...

)

- [Github 贡献简历生成器](https://medium.com/@baazzilhassan/github-contributions-resume-builder-d6d437668a91)
    + offtopic

This project give you the ability to generate your Resume from your Github contributions.


- [关于 Python 的 Matplotlib 简介](https://medium.com/@wilfredgithuka/introduction-to-matplotlib-on-python-8ed952953a4b)
    + matpoltlib

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts and the jupyter notebook, web application servers, and four graphical user interface toolkits.


- [使用 Sklearn 的 Count / Hash / TDiF 矢量化器分类文档](https://medium.com/@rnbrown/classifying-documents-with-sklearns-count-hash-tdif-vectorizers-9f8200e5a91e)
    + machine learning, classification

The Sklearn library provides several powerful tools that can be used to extract features from text. In this article, I will show you how easy it can be to classify documents based on their content using Sklearn.

- [Cython 0.26 有咩新咯?](http://blog.behnel.de/posts/whats-new-in-cython-026.html)
    + cpython

- [PyData 西雅图 2017 视频已经上传](https://www.youtube.com/playlist?list=PLGVZCDnMOq0rxoq9Nx0B4tqtr891vaCn7)
    + pydata conference

- [采访 HTTP 提示的 Chang-Hung Liang](https://theinitialcommit.com/2017/07/25/chang-hung-liang/)
    + open source

An exploration of the people behind the projects. Each post is an exclusive interview with a member of the open source community.


- [如何使用转移学习创建图像分类引擎](https://m.oursky.com/using-tensorflow-and-support-vector-machine-to-create-an-image-classifications-engine-7ee51b5617d5)
    + image processing, tensorflow

In this post, we are documenting how we used Google’s TensorFlow to build this image recognition engine.

- [在组织中分发私有 Python 包的简单方法](https://blog.chezo.uno/simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9)
    + dependency management, packages, distribution

(`是也乎:`

--> `wheelhouse`

)

- [机器学习 NLP:使用scikit-learning，python和NLTK的文本分类](https://medium.com/towards-data-science/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a)
    + text classification

- [风格化 Bokeh Visualizations](https://bokeh.github.io/blog/2017/7/24/styling-bokeh/)
    + graph

Bokeh is a Python interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js, and to extend this capability with high-performance interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications.. Bokeh's styling is very nice by default. However, extending Bokeh with your own custom styles can add an impressive level of polish to your visualizations.



## 好物
~ 包/模块/库/片段...

- [SmoothCriminal](https://github.com/G4lB1t/SmoothCriminal)
    - 24 Stars, 5 Fork

Detect sandbox by cursor movement speed

(`是也乎:`

光标移动速度...
)

- [ens.py](https://github.com/carver/ens.py)
    - 11 Stars, 2 Fork

Ethereum Name Service, made easy in Python.

(`是也乎:`

Ethereum 名称服务 ~ 以太坊域名
基于区块链的全新互联网形态...
)


- [Hindi-Words-Importance-Dataset](https://github.com/VastoLorde95/Hindi-Words-Importance-Dataset)
    - 9 Stars, 0 Fork

A repository of 14000 Hindi words and their Inverse Document Frequency.

(`是也乎:`

印地语词汇库, 类似我们的细胞词库...
)

- [pytorch-kaggle-amazon-space](https://github.com/EdwardTyantov/pytorch-kaggle-amazon-space)
    - 8 Stars, 2 Fork

Pytorch solution for Planet: Understanding the Amazon from Space https://www.kaggle.com/c/planet-understanding-the-amazon-from-space

(`是也乎:`

又一个空间相关的公益嗯哼....

)

- [python-code](https://github.com/zeeshanhanif/python-code)
    - 3 Stars, 2 Fork

Python Code for AI class

- [pionic](https://github.com/tlocke/pionic)
    - 0 Stars, 0 Fork

The Ion format is a superset of JSON, adding (among other things) the much-needed timestamp, decimal and binary data types.

(`是也乎:`

JSON 的超集 Ion 的支持库

)

- [text_classification](https://github.com/brightmart/text_classification)
    - 0 Stars, 0 Fork

All kinds of text classificaiton models and more with deep learning. 


### (￣▽￣)


# 是也乎

- 170728 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170728 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


