Title: 蠎加载 106
Slug: importpython-106
Date: 2017-01-05 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 106](http://importpython.com/newsletter/no/106/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [Go 跑 Python!](https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html)
    + golang, grumpy

Grumpy is an experimental Python runtime for Go. It translates Python code into Go programs, and those transpiled programs run seamlessly within the Go runtime. We needed to support a large existing Python codebase, so it was important to have a high degree of compatibility with CPython (quirks and all). The goal is for Grumpy to be a drop-in replacement runtime for any pure-Python project. Curator's note - If you are a Go Programming Language Developer do checkout http://importgolang.com/newsletter/

(`是也乎:`

玩具级,看爹了...
)


- [亲,2017 愿意升级到 Python 3.x 嘛?](https://twitter.com/importpython/status/815283645992710144)
    + importpython

Take the twitter poll, Do you see yourself using 3.x in 2017.

(`是也乎:`

当前近6成的人原意升级,不过,真实来也得看项目是否允许了
)

- [Handling Unicode Strings in Python](https://blog.emacsos.com/unicode-in-python.html)
    + unicode

I am a seasoned python developer, I have seen many UnicodeDecodeError myself, I have seen many new pythonista experience problems related to unicode strings. Actually understanding and handling text data in computer is never easy. Sometimes the programming language makes it even harder. In this post, I will try to explain everything about text and unicode handling in python.


(`是也乎:`

简单的说用 Py3 ...可是...唉;-(
)

- [5 things to watch in Python in 2017](https://www.oreilly.com/ideas/5-things-to-watch-in-python-in-2017)

An improved asyncio module, Pyjion for speed, and moving to Python 3 will make for a rich Python ecosystem.

(`是也乎:`

又一个预言术...一切都在 py3 怎么赢得 google 的心了

)

- [如何在 Linux 中安装 Scikit-Learn 来我开始机器学习的指南](https://techarena51.com/index.php/getting-started-machine-learning-linux-python-3-scikit-learn/)
    + machine learning

In this Tutorial I will describe how you can get started with Machine Learning on Linux using Scikit-Learn and Python 3.


- [用 pbr 来作 Python 包管理](https://julien.danjou.info/blog/2017/packaging-python-with-pbr)
    + packaging

A library for managing seatuptools packaging needs in a consistent manner. pbr reads and then filters the setup.cfg data through a setup hook to fill in default values and provide more sensible behaviors, and then feeds the results in as the arguments to a call to setup.py - so the heavy lifting of handling python packaging needs is still being done by setuptools.

(`是也乎:`

什么年代了还是 ini 格式...也没有解决包的本地存储管理...
)

- [BDFL 的启源](http://www.artima.com/weblogs/viewpost.jsp?thread=235725)
    + Guido

This is an old article written by Guido van van Rossum himself. Occasionally people ask me about the origins of my nickname BDFL (Benevolent Dictator For Life). At some point, Wikipedia claimed it was from a Monty Python skit, which is patently false, although it has sometimes been called a Pythonesque title. I recently trawled through an old mailbox of mine, and found a message from 1995 that pinpoints the origin exactly. I'm including the entire message here, to end any doubts that the term originated in the Python community.

(`是也乎:`

旧文有回甘...
)


- [Armin 解说 Flask globals - Video](https://www.youtube.com/watch?v=1ByQhAM5c1I)
    + flask, video

This talk explores how you can build applications and APIs with Flask step by step by being easy to test and scale to larger and more complex scenarios. The talk will also go a bit into the history of some design decisions in Flask and what works well and in which areas you might want to mix it with other technologies for better results.

- [如何审查 Django ORM SQL 查询](http://mrcoles.com/how-view-django-orm-sql-queries/)
    + ORM

Copy-paste this into your Python 3 interpreter to see a human-readable version of the raw SQL queries that your Django code is running.


- [DSF 宣布2016 Malcolm Tredinnick Memorial Prize 的获胜者 ](https://www.djangoproject.com/weblog/2016/dec/22/dsf-announces-winner-2016-malcolm-tredinnick-memor/)
    + djangogirls

Aisha (@AishaXBello) joined the Django community when she attended a Django Girls workshop during EuroPython in 2015. From that point on, Aisha's trajectory in the Django world was unstoppable. She is not only a talented developer but her desire to keep learning and sharing her knowledge with others is simply inspiring. She organized or helped organize a huge number of Django Girls workshop in her home country of Nigeria. Thanks to her, Nigeria is on its way to be the world-record holder of most Django Girls events organized.

(`是也乎:`

尼日利亚 的

![AishaXBello](https://pbs.twimg.com/profile_images/623150174311981056/ibNHNfZ6_400x400.jpg)

)


- [Django 或 Flask - Reddit 讨论](https://www.reddit.com/r/Python/comments/5lk0or/django_or_flask/)
    + flask

(`是也乎:`

也属月经贴了...简单的说, 有銭就上 Django.
)

- [用NumPy进行通道检测](https://medium.com/@tempflip/lane-detection-with-numpy-56b923245fc9)
    + numpy, scipy

Detect lanes on video frames, using NumPy and SciPy. My goal is not to achieve better performance or speed then with OpenCV. Rather, I’m going to implement some techniques learned at the Computer Vision course.

(`是也乎:`

OpenCV 也大量使用 Numpy
)

- [Python 机器学习的副作用](https://danny.fyi/side-effects-of-python-machine-learning-16b0d2f55882)
    + machine learning

- [基于 IP 地址的天气预报](https://medium.com/ipapi/weather-forecast-from-ip-address-9a1b8bd14970)
    + code snippet

- [Jupyter + Pachyderm — 第1部分，探索和了解历史分析](https://medium.com/pachyderm-data/jupyter-pachyderm-part-1-exploring-and-understanding-historical-analyses-2a37e56c6578)
    + jupyter

- [第 8 集: Armin Ronacher 谈 Flask，Python生态系统和Unicode](https://soundcloud.com/import-this/episode-8)
    + podcast

- [用 Python 从头开始实现分类器令俺明白了什么?](http://www.jeannicholashould.com/what-i-learned-implementing-a-classifier-from-scratch.html)
    + machine learning, classification

Machine learning can be intimidating for a newcomer. The concept of a machine learning things alone is quite abstract. How does that work in practice ?. In order to demystify some of the magic behind machine learning algorithms, I decided to implement a simple machine learning algorithm from scratch. I will not be using a library such as scikit-learn which already has many algorithms implemented. Instead, I’ll be writing all of the code in order to have a working binary classifier algorithm. The goal of this exercise is to understand its inner workings.

(`是也乎:`

这是理解目标对象的最精确学习方式,
再制丫的.

)



## 好物
~ 包/模块/库/片段...

- [hello-vue-django](https://github.com/rokups/hello-vue-django)
    - 11 Stars, 1 Fork

vuejs + Django 的热集成重加载

- [alexabot-asana](https://github.com/peterxdeng/alexabot-asana)
    - 6 Stars, 1 Fork

AlexaBot for Asana -- Create Asana Tasks with Amazon Echo

- [tensorflow-mnist-cnn](https://github.com/hwalsuklee/tensorflow-mnist-cnn)
    - 5 Stars, 1 Fork

使用卷积神经网络完成 MNIST 分类;
实现了诸如数据增加，丢弃，批量规范化等各种技术...

### (￣▽￣)

- [fy0/python_lite: [WIP] A simple, lightweight implementation of python3 language.](https://github.com/fy0/python_lite)
    + 36 Stars, 1 Fork

简蠎~只是因为想....

# 是也乎

- 170106 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170105 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


