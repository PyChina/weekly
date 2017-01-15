Title: 蠎加载 107
Slug: importpython-107
Date: 2017-01-15 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 107](http://importpython.com/newsletter/no/107/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [将数据加载入 Pandas DataFrame: 硬的和爽的方法](http://blog.enthought.com/python/with-and-without-the-canopy-data-import-tool-loading-data-theres-no-such-thing-as-a-simple-csv-file/)
    + pandas

Data exploration, manipulation, and visualization start with loading data, be it from files or from a URL. Pandas has become the go-to library for all things data analysis in Python, but if your intention is to jump straight into data exploration and manipulation, the Canopy Data Import Tool can help, instead of having to learn the details of programming with the Pandas library.

(`是也乎:`

Canopy 有专用工具来加速,只是 Canopy 环境非常嗯哼...

)

- [推介 Python 类型注释 - By Guido Van Rossum, Greg Price, and David Fisher](https://www.youtube.com/watch?v=ZP_QV4ccFHQ)
    + video, Guido

Dropbox has several million lines of production code written in Python 2.7. As a first step towards migrating to Python 3, as well as to generally make our code more navigable, we are annotating our code with type annotations using the PEP 484 standard and type-checking the annotated code with mypy. In this talk we will discuss lessons learned and show how you too can start type-checking your legacy Python 2.7 code, one file at a time. We will also describe some of the many improvements we’ve made to mypy in the process, as well as some other tools that come in handy.

(`是也乎:`

百万行代码级别的 py2->3 迁移经验分享...

有 Guido 座镇的项目都如此艰难,那么... py2 的确命不能绝也.
)

- [用 Python 处理 bug 并达到 186k requests/second](https://medium.com/@raphael.deem/fixing-bugs-and-handling-186k-requests-second-using-python-2e75d2f9f4f6)
    + sanic

Sanic is a Python3 framework built using the somewhat newly introduced coroutines, harnessing uvloop and based on Flask. However, it had an issue preventing it from utilizing multiple processes correctly.


(`是也乎:`

又一个 web 应用框架 Sanic, 当然主要面向 py3 
)

- [使用 AWS Lambda 中的 Python 来索引 Amazon Elasticsearch 服务中的 Metadata](https://aws.amazon.com/blogs/database/indexing-metadata-in-amazon-elasticsearch-service-using-aws-lambda-and-python/)
    + aws, elasticsearch, lambda, s3

Objects in S3 contain metadata that identifies those objects along with their properties. When the number of objects is large, this metadata can be the magnet that allows you to find what you’re looking for. Although you can’t search this metadata directly, you can employ Amazon Elasticsearch Service to store and search all of your S3 metadata. This blog post gives step-by-step instructions about how to store the metadata in Amazon Elasticsearch Service (Amazon ES) using Python and AWS Lambda.

(`是也乎:`

Lambda 哪, 神器,无主机微服务.

)

- [用 Pythonic 的姿态来搞 APIs](https://medium.com/@hakibenita/working-with-apis-the-pythonic-way-484784ed1ce0)
    + tutorial

Communication with external services is an integral part of any modern system. Whether it’s a payment service, authentication, analytics or an internal one?—?systems need to talk to each other. In this short article we are going to implement a module for communicating with a made-up payment gateway, step by step.

(`是也乎:`

教程揭示了一个支付网关接口的形成过程
)

- [Python 工作环境配置终极指南](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)
    + environment

When you’re beginning, it’s pretty easy to setup your Python environment on Unix. But in time things can get messy due to multiple versions, interpreters, utilities and projects.

(`是也乎:`

果断 pyenv+iPython
)


- ["生成器: Python 中最嗯哼的迭代" Luciano Ramalho](https://www.youtube.com/watch?v=o5gByn3RKFI&feature=youtu.be)

Iterables, iterators and generators are a key subject for effective Python usage, especially when processing large-scale data sets. Do you know why zip(*M) allows efficient traversal of a matrix M by columns? From the elegant for statement through list/set/dict comprehensions and generator functions, this talk shows how the Iterator pattern is so deeply embedded in the syntax of Python, and so widely supported by its libraries, that some of its most powerful applications can be overlooked by programmers coming from other languages.


- [在 Windows 机器中部署 Python 的三种方式](http://blog.yhat.com/posts/installing-python-on-windows.html)
    + windows, installation

One of the downsides is that despite the Python community’s attempts to make it an accessible tool for everyone, a lot of folks find the installation process daunting or confusing, including myself. Once I'd learned enough Python to tinker around, I didn't know where to "go" on my computer to write it or what to do next. Today I'll cover three ways to install Python on your Windows computer step by step.

(`是也乎:`

Rodeo->Anaconda->官方

图样图森破,俺推荐 `Python(x,y)`

)

- [从 PDF 输出表格到 Python DataFrame](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)
    + pandas, pdf, data frame

It is simple wrapper of tabula-java and it enables you to extract table into DataFrame or JSON with Python. You also can extract tables from PDF into CSV, TSV or JSON file.

(`是也乎:`

果断得通过中间纯数据文件转换.
)

- [半小时部署一个 Python 的 Telegram bot 到 Azure](https://hackernoon.com/host-a-python-telegram-bot-using-azure-in-30-minutes-58f246cedf23)
    + bot, telegram

Almost two years ago Telegram let developers create bots quite painlessly. You can read an introduction about it on Telegram website. In this article we will create a simple bot in python, it’ll be hosted in Azure using Bottle framework. The bot will not do anything fancy, consider it as a template for your python based bots.

(`是也乎:`

嗯哼?!是用 Bottle 开发的!?

)

- [用 Python 进行 Bayesian A/B 测试](https://medium.com/hockey-stick/tl-dr-bayesian-a-b-testing-with-python-c495d375db4d)
    + statistics, Bayesian

- [TensorBoard: 可视化学习 | TensorFlow](https://www.tensorflow.org/how_tos/summaries_and_tensorboard/)
    + tensorflow

- [介绍 TensorFlow: 解决一个简单的回归问题](https://medium.com/@saxenarohan97/intro-to-tensorflow-solving-a-simple-regression-problem-e87b42fd4845?source=rss------tensorflow-5)

Today I’ll try to explain how to hack TensorFlow to solve a simple regression problem.

- [属性访问是如何工作的?](https://medium.com/stepping-through-the-cpython-interpreter/how-does-attribute-access-work-d19371898fee)
    + cpython

Have you ever wondered how the CPython interpreter handles attribute access on a class or an instance of a class ?




## 好物
~ 包/模块/库/片段...

- [sublime-prettier](https://github.com/danreeves/sublime-prettier)
    - 10 Stars, 1 Fork

A Sublime Text 3 plugin for Prettier

(`是也乎:`

JS 世界的 gofm 也嗯哼出来了...
)

- [smsReceiver](https://github.com/mthbernardes/smsReceiver)
    - 5 Stars, 1 Fork

为网站包装提供接收手机短信的功能.

- [wagtail-sharing](https://github.com/cfpb/wagtail-sharing)
    - 5 Stars, 0 Fork

简化 Wagtail drafts 共享

- [Language-Modeling-GatedCNN](https://github.com/anantzoid/Language-Modeling-GatedCNN)
    - 5 Stars, 0 Fork

Tensorflow implementation of "Language Modeling with Gated Convolutional Networks"

- [tfchain](https://github.com/mitmul/tfchain)
    - 4 Stars, 0 Fork

Run a static part of the computational graph written in Chainer with Tensorflow

- [flask-http2-push](https://github.com/jdaroesti/flask-http2-push)
    - 3 Stars, 0 Fork

Flask 扩展,
追加 http2 服务推送功能. 


### (￣▽￣)

- [fy0/python_lite: [WIP] A simple, lightweight implementation of python3 language.](https://github.com/fy0/python_lite)
    + 36 Stars, 1 Fork

简蠎~只是因为想....

# 是也乎

- 170115 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170115 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


