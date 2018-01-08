Title: 蠎加载 157
Slug: importpython-157
Date: 2018-01-07 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 157](http://importpython.com/newsletter/no/157/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [给小白的 Pandas: 如何处理真实的数据](https://medium.com/@camille.malis2/pandas-for-beginners-how-to-handle-real-life-data-a27c68bd21a2)
    + pandas

Handling real life datasets can be painful when you are used to cleaned and ‘ready-to-use’ datasets that are used in books, tutorials and beginner challenges in Data Science. This tutorial aims to provide some useful tips and codes to get started with the Pandas library and data provided by your company or client.

- [用TensorFlow识别手写数字](https://medium.com/@sanjitjain2/recognizing-handwritten-digits-with-tensorflow-28d4cb95cd60)
    + deep learning, tensorflow

DeepLearning is a subfield of machine learning that is a set of algorithms and functions inspired by the structure and fucntioning of the brain. TensorFlow is a machine learning framework that Google created and is used to design, build and train deep learning models. This tutorial is an attempt on the MNIST dataset from this Kaggle competition while also explaining the basics of writing TensorFlow code.

(`是也乎:`

这已经是标准的入门嗯哼了,
关键是启动训练集容易建立, 并早已有...

)


- [Python 的SQLite教程](http://stackabuse.com/a-sqlite-tutorial-with-python/)
    + sqlite3

This tutorial will cover using SQLite in combination with Python's sqlite3 interface.

(`是也乎:`

叕一个 SQLite 教程, 简单的说, 得先会 SQL

)


- [在 Go 中扩展 Python 3](https://hackernoon.com/extending-python-3-in-go-78f3a69552ac)
    + golang

Extending Python has been a core feature of the platform for decades, the Python runtime provides a “C API”, which is a set of headers and core types for writing extensions in C and compiling them into Python modules. But, do you really have to write extensions to Python in C? Why can’t we use something a tad more modern, like Go.


(`是也乎:`

golang 的优良设计之一就是方便的支持 C,
所以, 扩展到 Python 也是相似的工具链

)


- [$1200 的深度学习钻机](https://medium.com/@schnee/a-1200-deep-learning-rig-b84db5ec3b40)
    + deep learning, offtopic

Inspired by several other system builds ($1000, $1700, and forum posts), I decided to have a go and build one. I was a Sr Director of Data Science for a large travel company at the time and was a bit envious of the work being done by the individual scientists. I was also contemplating a change in employment (with some downtime)?—?I wanted to ensure I had access to resources to continue my deep learning leveling-up. Finally, I wanted to make sure I could demonstrate to my kids the Internet’s most important task: distinguishing between “cat” and “not cat”.

- [Python 作为教学语言可以退休了](http://prog21.dadgum.com/203.html?1)
    + teaching

For the last ten years, my standard advice to someone looking for a programming language to teach beginners has been start with Python. And now I'm changing that recommendation.

(`是也乎:`


这位老师尝试过 Erlang 作为开蒙的语言?
现在果断推荐上 Javascript...

)


- [和我谈谈Python: ＃145 2017 Python年度回顾](https://talkpython.fm/episodes/show/145/2017-python-year-in-review)
    + podcast

- [用 Python 构建一个 Redis-样 的服务器](http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)
    + Redis-like

The other day the idea occurred to me that it would be neat to write a simple Redis-like database server. While I've had plenty of experience with WSGI applications, a database server presented a novel challenge and proved to be a nice practical way of learning how to work with sockets in Python. In this post I'll share what I learned along the way.

- [When and how to use Django TemplateView](http://agiliq.com/blog/2017/12/when-and-how-use-django-templateview/)
    + django, template

Django provides several class based generic views to accomplish common tasks. Simplest among them is TemplateView. TemplateView should be used when you want to present some information in a html page. TemplateView shouldn't be used when your page has forms and does creation or update of objects.




## 好物
~ 包/模块/库/片段...


- [Parris](https://github.com/jgreenemi/Parris)
    - 237 Stars, 13 Fork

Parris, the automated infrastructure setup tool for machine learning algorithms.

(`是也乎:`

又一个自动配置 AI 生成器配置的工具
)


- [xkeysnail](https://github.com/mooz/xkeysnail)
    - 55 Stars, 3 Fork

Script to remove homoglyphs and zero-width characters to allow for safe distribution of documents from anonymous sources.

> 删除同义字和零宽字符的脚本，以便从匿名来源安全分发文档


- [xkeysnail](https://github.com/mooz/xkeysnail)
    - 29 Stars, 1 Fork

Yet another keyboard remapping tool for X environment.


(`是也乎;`

这种工具如果不是跨平台的, 使用成本就太太太高了...

![xkeysnail](https://camo.githubusercontent.com/51e5017f66b7350dbd22ba51e1e1270d5d8c2788/687474703a2f2f6d6f6f7a2e6769746875622e696f2f696d6167652f786b6579736e61696c5f73637265656e73686f742e706e67)

一位日本工程师, 基于国人作品改进的: [DreaminginCodeZH/pykeymacs: Emacs style keyboard macros implemented in Python](https://github.com/DreaminginCodeZH/pykeymacs)

)

- [vidDistill](https://github.com/rkindi/vidDistill)
    - 23 Stars, 3 Fork

Automated (YouTube) Video Summarization Using Captions.



- [flask-docker](https://github.com/chhantyal/flask-docker)
    - 16 Stars, 2 Fork

Fastest way to ship Python web apps, anywhere. Be shipping (using Docker, Flask, Gunicorn, Whitenoise).

(`是也乎:`

叕一个预装好 Flask 生产链接的 docker,
但是, 永远不是最合理的...

)


- [CryptoTracker](https://github.com/Max00355/CryptoTracker)
    - 15 Stars, 2 Fork

Create and track your crypto currency portfolio from the terminal.

> 从终端创建并跟踪您的加密货币组合

- [tensorflow-grad-cam](https://github.com/hiveml/tensorflow-grad-cam)
    - 12 Stars, 0 Fork

Tensorflow Slim Grad-Cam to Explain Neural Network Predictions with Heatmap or Shading

- [Flask-Person-Detector](https://github.com/rememberlenny/Flask-Person-Detector)
    - 10 Stars, 2 Fork

Flask based web application that provides a REST endpoint using OpenCV's Deep Neural Network method for Object Detection.

- [LineDistiller](https://github.com/hatsuame/LineDistiller)
    - 9 Stars, 3 Fork

A data-driven line extractor for 2D anime, manga and illustration using Keras.

(`是也乎:`


![overview](https://github.com/hatsuame/LineDistiller/raw/master/overview.jpg)


可是这种工具到底什么场景中要用?
复刻上右动画片时?

)


- [24-game](https://github.com/cls1991/24-game)
    - 5 Stars, 2 Fork

24 point game implemented in Python, 

> just for fun!.

- [flask-validates](https://github.com/tjpnz/flask-validates)
    - 5 Stars, 1 Fork

Painless form validation using view decorators.

(`是也乎:`

叕一个在 view 层实现的表单检验器

)


- [mastering-pycharm-course](https://github.com/talkpython/mastering-pycharm-course)
    - 4 Stars, 0 Fork

Course demos and handouts for Talk Python's Mastering PyCharm course.


(`是也乎:`

叕一个 pycharm 教程,
俺总感觉如果开发工具的界面复杂到得专门学习时,
就已经不值得嗯哼了?

)


- [GitHub-contributions](https://github.com/faheel/GitHub-contributions)
    - 4 Stars, 0 Fork

Get details about all the projects to which you have contributed to on GitHub.

(`是也乎:`

叕一个 gh 生态私人状态采集服务,
不过...没几个人敢于直接将其数据用在简历中的吧?

py3 only 的, 而且, 如果你有很多私人仓库, 这工具也就嗯哼了...

)


- [tweetsender](https://github.com/nurtdinovadf/tweetsender)
    - 3 Stars, 0 Fork

Get tweets of particular users into your gmail inbox without using twitter app.

(`是也乎:`

twitter -> gmail 的叕一工具,
再次怀念 buzz
)


- [ExpenseManager](https://github.com/aganjali10/ExpenseManager)
    - 3 Stars, 0 Fork

An application to manage all your personal expenditures. Add all your expenses along with the amount spent, the date and time of your spending and other additional description.


(`是也乎:`

叕一个私人支出管理工具...
其实吧, 发票扫描才是必要的
人工输入都忒累...

)


- [fleep](https://github.com/floyernick/fleep)
    + project, user submission

Determining file format using Python

(`是也乎:`

叕一个文件格式判定器工具

)


### (￣▽￣)

- [重大改革：Python 语言将被加入高考科目，VB 惨被淘汰！](https://mp.weixin.qq.com/s/kaEUp2q0K3a_huQa9m_LZg) 为了孩子,中国家长们得开始学习 Python 了... 
    + 传说 高考 编程


## 是也乎

- 180108 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180107 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


