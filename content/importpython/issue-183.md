Title: 蠎加载 183
Slug: importpython-183
Date: 2018-08-30 19:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 183](http://importpython.com/newsletter/no/183/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [和 Python 搞并行编程](https://chryswoods.com/parallel_python/index.html)
    + parallel programming

Welcome to a short course that will teach you how to write Python scripts that can take advantage of the processing power of multicore processors and large compute clusters. While this course is based on Python, the core ideas of functional programming and parallel functional programming are applicable to a wide range of languages. To follow this course you should already have a good basic understanding of Python, e.g. loops, functions, containers and classes. This course will rely on you understanding the material presented in my Beginning Python and Intermediate Python courses. This is a short course that will give you a taste of functional programming and how it can be used to write efficient parallel code. Please work through the course at your own pace. Python is best learned by using it, so please copy out and play with the examples provided, and also have a go at the exercises.


(`是也乎:`

课程, 讲述并行计算原则, 只是选择用 Python 来作为课程案例...

)


- [管道在 Python](http://sulami.github.io/posts/pipes-in-python/)
    + functional programming

I just found an article about pipes in Python on lobste.rs and was reminded that I was toying with the exact same thing recently. Using a lot of functional languages (mainly Haskell, Clojure, Elixir) and also a fair bit of bash, I am very used to streaming data through chains of functions using pipe-like constructs. Python does make this quite difficult and encourages a more imperative approach with intermediate variables

(`是也乎:`

推荐珠三角技术沙龙的赖勇浩折腾过的模块, 可以直接从形式上 pipe 起来

)


- [用 Python 构建退休储蓄模型](http://sam-koblenski.blogspot.com/2018/08/building-model-for-retirement-savings.html)
    + pandas

It's easy to find investment advice. It's a little less easy to find good investment advice, but still pretty easy. We are awash in advice on saving for retirement, with hundreds of books and hundreds of thousands of articles written on the subject. It is studied relentlessly, and the general consensus is that it's best to start early, make regular contributions, stick it all in low-fee index funds, and ignore it. I'm not going to dispute that, but I do want to better understand why it works so well. As programmers we don't have to simply take these studies at their word. The data is readily available, and we can explore retirement savings strategies ourselves by writing models in code. Let's take a look at how to build up a model in Python to see how much we can save over the course of a career.


(`是也乎:`

无论什么模型也无法抵抗国家一纸红头文件的...

)



- [mypyc - Dropbox 正在开发一个新的编译器](https://mail.python.org/pipermail/python-dev/2018-August/154951.html)
    + Cython


mypyc will compile type-annotated Python code to an optimized C. The first goal is to compile mypy with it to make it faster, so I hope that the project will be completed. Essentially, mypyc will be similar to Cython, but mypyc is a *subset of Python*, not a superset. Interfacing with C libraries can be easily achieved with cffi. Being a strict subset of Python means that mypyc code will execute just fine in PyPy. They can even apply some optimizations to it eventually, as it has a strict and static type system.


(`是也乎:`

自从老爹去了 Dropbox, 他们就经常嗯哼出全部的编译器来,
应该是好事儿? 不过, 都依赖重要的 py3 的类型声明特性

)


- [Vanilla python 聊天服务器](https://honeyspoon.me/vanilla-python-chat-server/)
    + http, toy application, webserver

In the process of trying to build a vanilla python HTTP server, I realized that I don't know much about it's inner workings. So while I was stuck learning about sockets, TCP handshakes and protocols, I decided to tackle something that was a little more within my reach thus was born this humble little project. A simple python chat server meant to be used by terminal clients through netcat.

(`是也乎:`

继 香草JS 后, Python 框架也有香草味儿的了...

)


- [如何在 Python 中从头开始构建自己的神经网络](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
    + deep learning

A beginner’s guide to understanding the inner workings of Deep Learning. .




- [用 Prophet 预测 Amazon 销售额](https://medium.com/@ilangley_77707/forecasting-amazon-sales-with-prophet-5c1701d12af)
    + forecasting

Prophet is an open-source Python package for time-series forecasting, originally developed by Facebook’s Data Science team to predict usage on different parts of Facebook. Prophet’s forte is forecasting highly seasonal data with long-term, non-stationary trends, punctuated with occasional spikes on specific dates.

(`是也乎:`

Prophet: 基于时间序列进行预测的软件

)


- [Airflow, 元数据工程和世界上最大的民主数据平台](https://medium.com/@vinayakmehta/airflow-meta-data-engineering-and-a-data-platform-for-the-worlds-largest-democracy-3b49a3efd5e8)
    + airflow

In this post, we will talk about how one of Airflow’s principles, of being ‘Dynamic’, offers configuration-as-code as a powerful construct to automate workflow generation. We’ll also talk about how that helped us use Airflow to power DISHA, a national data platform where Indian MPs and MLAs monitor the progress of 42 national level schemes. In the end, we will discuss briefly some of our reflections from the project on today’s public data technology.

- [Leveraging Docker Images to deploy your Django backend on Openshift](https://medium.com/@uddishverma22/leveraging-docker-images-to-deploy-your-django-backend-on-openshift-5e268d679173)
    + devops, openshift

Openshift with Docker Images is the ultimate tool you need for automated deployment.





## 好物
~ 包/模块/库/片段...

- [asciify](https://github.com/RameshAditya/asciify)
    - 143 Stars, 8 Fork

Convert any image into ASCII Art.

(`是也乎:`

叕一则字符艺术工具

![asciify](https://github.com/RameshAditya/asciify/raw/master/github-resources/sample.gif)

)


- [yacs](https://github.com/rbgirshick/yacs)
    - 47 Stars, 1 Fork

YACS -- Yet Another Configuration System

(`是也乎:`

叕一个 SCM 工具, 支持 py2/3 

)



- [Face-Track-Detect-Extract](https://github.com/Linzaer/Face-Track-Detect-Extract)
    - 45 Stars, 14 Fork

Detect , track and extract the optimal face in multi-target faces (exclude side face and select the optimal face).


(`是也乎:`

![Face](https://raw.githubusercontent.com/wiki/Linzaer/Face-Track-Detect-Extract/pic4.gif)


国货.. Shanghai 

)


- [voice_zaloai](https://github.com/pbcquoc/voice_zaloai)
    - 23 Stars, 5 Fork

dentifying gender and regional accent from speech

- [dropbox_ext4](https://github.com/dimaryaz/dropbox_ext4)
    - 19 Stars, 3 Fork

Hack to make Dropbox work on non-ext4 filesystems

(`是也乎:`

嗯哼? Dropbox 还挑 FS 的?

)


- [dove](https://github.com/vishalkuo/dove)
    - 18 Stars, 0 Fork

A command line utility to help manage your development server in Digital Ocean

(`是也乎:`

DO 的接口/文档嗯哼的好, 生态也就越来越好

)


- [flask-executor](https://github.com/dchevell/flask-executor)
    - 16 Stars, 2 Fork

A simple Flask wrapper for concurrent.futures

- [sales_forecast_ml](https://github.com/rshrc/sales_forecast_ml)
    - 12 Stars, 5 Fork

A web application to predict the sales of a newly launched product

(`是也乎:`

![sales_forecast_ml](https://camo.githubusercontent.com/568a2d7626b30ea9a1fa9614dd8cf2f8ba82c131/68747470733a2f2f692e696d6775722e636f6d2f4f67724664766a2e706e67)


很久没见电商类嗯哼了

)


- [SceneGraphParser](https://github.com/vacancy/SceneGraphParser)
    - 11 Stars, 0 Fork

A python toolkit for parsing sentences (in natural language) into scene graphs (as symbolic representation).

(`是也乎:`

叕一则 NLP 模块,当然, 没中文什么事儿

)


- [Python-Face-Recongition-ML-OpenCv](https://github.com/ritik-gupta/Python-Face-Recongition-ML-OpenCv)
    - 5 Stars, 1 Fork

Face recognition using open-cv and machine learning written in python

(`是也乎:`

叕一则人脸识别的嗯哼

)


- [pavlova](https://github.com/freelancer/pavlova)
    - 5 Stars, 0 Fork

A python deserialisation library built on top of dataclasses

(`是也乎:`

py3 only 的..
)


- [XMeans](https://github.com/alexkimxyz/XMeans)
    - 4 Stars, 0 Fork

Implementation of X-means clustering algorithm

- [IStuPydKernel](https://github.com/MuchenSun/IStuPydKernel)
    - 4 Stars, 0 Fork

StuPyd kernel for Jupyter

(`是也乎:`

Jupyter 生态勇烈精进ing...
)




### (￣▽￣)

- [PyCon 2018 China](http://cn.pycon.org/2018/)
    + 来了, 真的来了
- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180830 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180830 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


