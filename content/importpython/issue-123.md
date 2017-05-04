Title: 蠎加载 123
Slug: importpython-123
Date: 2017-05-04 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 123](http://importpython.com/newsletter/no/123/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [嗯哼掉 GIL: 快速写和线程安全的Python](https://emptysqua.re/blog/grok-the-gil-fast-thread-safe-python/)
    + gil

static PyThread_type_lock interpreter_lock = 0; /* This is the GIL */ This line of code is in ceval.c, in the CPython 2.7 interpreter’s source code. Guido van Rossum’s comment, “This is the GIL,” was added in 2003, but the lock itself dates from his first multithreaded Python interpreter in 1994. On Unix systems, PyThread_type_lock is an alias for the standard C lock, mutex_t. It is initialized when the Python interpreter begins:

(`是也乎:`

挖出对应代码, 13年前的坑...

![hair-fashion](https://emptysqua.re/blog/grok-the-gil-fast-thread-safe-python/hair-fashion.png)

为这用心的配图手工点赞...少数没有被功夫认证了的技术 blog 了...

)

- [Asyncio Coroutine 模式: 超越等待](https://medium.com/@yeraydiazdiaz/asyncio-coroutine-patterns-beyond-await-a6121486656f)
    + asyncio

concurrent programming is hard and while coroutines allow us to avoid callback hell it can only get you so far, you still need to think about creating tasks, retrieving results and graceful handling of errors. Sad face. Good news is all of that is possible in asyncio. Bad news is it’s not always immediately obvious what wrong and how to fix it. Here are a few patterns I’ve noticed while working with asyncio.

(`是也乎:`

py3 only 的坑模式...其实咧这类事儿,直接用 go 吧.
)



- [3分钟内在 Jupyter Notebook 用起 PySpark](https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f)
    + jupyter, spark

Python is the perfect language for prototyping in Big Data/Machine Learning fields. Plus, there is no Jupyter Notebook in Scala: PySpark is our only option.

- [构建优良 Celery 异步任务的自查清单](http://celerytaskschecklist.com/)

Best Practices, Monitoring & Tests, Resources for celery.

- [该怎么用 Python Debugger](https://medium.com/@sourleangchhean/how-to-use-the-python-debugger-43a05a826f82)
    + debugging

The Python debugger provides a debugging environment for Python programs. It supports setting conditional breakpoints, stepping through the source code one line at a time, stack inspection, and more.


- [有关 Django 中预取应该知道的全部 - By Haki Benita](https://hackernoon.com/all-you-need-to-know-about-prefetching-in-django-f9068ebe1e60)
    + ORM

- [使用 单一责任 原则重构 Python 代码库](https://medium.com/unbabel-dev/refactoring-a-python-codebase-using-the-single-responsibility-principle-ed1367baefd6)
    + refactoring

The Single Responsibility Principle (SRP) is an effective strategy against this sort of problem by reducing the amount of code in the several layers of your codebase, focusing each one on specific objectives and separating them by logical domain.


- [poet](https://github.com/sdispater/poet)
    + pip

Poet helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere. The package is highly experimental at the moment so expect things to change and break. However, if you feel adventurous I'd gladly appreciate feedback and pull requests.

(`是也乎:`

又一个 pip 的增强工具,
问题是所有 PyPi 的外围工具都没有很好的解决工程中最要命的一个需求:

    如何将开发环境
    一键迁移/备份/恢复/部署/升级/.. 到目标主机中?
    而不依赖外部资源 <--

至今也就见过 dh-virtualenv 依赖 Debain 的软件包机制完成了
py 环境的真正封装...

)


- [语言中的性别偏见 - 新闻文本语料库中的双语分析](http://maxberggren.se/2017/05/02/gender-bias/)
    + bigrams, ngrams, maching learning

- [如何用 Chromium 和 PyInstaller 将 Web 应用程序转换为桌面应用程序](https://medium.freecodecamp.com/the-python-desktop-application-3a66b4a128d3)
    + sofi, desktopUI

I’ve been working on a Python module called Sofi that generates user interfaces. It can deliver a desktop feel while using standard single-page web technologies. For flexibility, I designed it to work through two methods of distribution: in-browser and executable.

(`是也乎:`

这简直是在抢 React 的饭碗哪!

)


- [用 Async Python 3.6 和 Redis 编写快速应用程序](https://eng.paxos.com/write-fast-apps-using-async-python-3.6-and-redis)
    + redis, async

- [城市中的自驾车神经网络](https://www.youtube.com/watch?v=KSX2psajYrg)
    + tensorflow

In this self-driving car with Python video, I introduce a newer, much more challenging network and task that is driving through a city.


- [玩树莓Pi:交通灯](https://medium.com/@simon_prickett/playing-with-raspberry-pi-traffic-lights-89e0d1cb51fd)
    + IOT

I’ve recently been doing some simple Python programming with the Raspberry Pi and a set of traffic light LEDs that connect to it. In this post I’ll look at setting up a Pi to drive the lights.


- [用 scikit-learn 搞出学习排名 ](https://medium.com/@motta.lrd/learning-to-rank-with-python-scikit-learn-327a5cfd81f)
    + scikit-learn

- [在IPython或Jupyter中使用Python unittest](https://medium.com/@vladbezden/using-python-unittest-in-ipython-or-jupyter-732448724e31)
    + jupyter, test

Configuration for running unittest in IPython or Jupyter is different than running unittest from command line.





## 好物
~ 包/模块/库/片段...

- [py-backwards](https://github.com/nvbn/py-backwards)
    - 202 Stars, 4 Fork

Python to python compiler that allows you to use some Python 3.6 features in older versions, you can try it in the online demo.

(`是也乎:`

py3to2 的兄弟
)

- [gruvi](https://github.com/geertj/gruvi)
    - 77 Stars, 10 Fork

gruvi

(`是也乎:`

基于 libuv 的 pyuv 进一步封装
)

- [webcam-pix2pix-tensorflow](https://github.com/memo/webcam-pix2pix-tensorflow)
    - 56 Stars, 10 Fork

Source code and pretrained model for webcam pix2pix

(`是也乎:`

将 pix2pix 应用到 webcam 的嗯哼
)

- [how_to_convert_text_to_images](https://github.com/llSourcell/how_to_convert_text_to_images)
    - 40 Stars, 13 Fork

This is the code for "How to Convert Text to Images - Intro to Deep Learning #16' by Siraj Raval on YouTube

(`是也乎:`

![bird1](https://github.com/llSourcell/how_to_convert_text_to_images/raw/master/examples/bird1.jpg)

是的, 当然不支持中文...

)

- [fitting-random-labels](https://github.com/pluskid/fitting-random-labels)
    - 29 Stars, 6 Fork

Example code for the paper "Understanding deep learning requires rethinking generalization".

- [shcheck](https://github.com/m3liot/shcheck)
    - 19 Stars, 2 Fork

Just a small tool to check security headers

(`是也乎:`

![shcheck](https://github.com/m3liot/shcheck/raw/master/screenshot.png)

只用了 urllib2 等内建模块

)

- [dqn](https://github.com/lufficc/dqn)
    - 13 Stars, 2 Fork

Implementation of q-learning using TensorFlow

- [mputil](https://github.com/rasbt/mputil)
    - 8 Stars, 0 Fork

Utility functions for Python's multiprocessing standard library module.

(`是也乎:`

对 multiprocessing 内建模块的增强:


)

- [PSPy](https://github.com/vector-sec/PSPy)
    - 6 Stars, 0 Fork

AWS PowerShell Python Lambda, or PSPy for short, is a simple Python 2.7 AWS Lambda function designed to execute the PowerShell binary and marshal input/output to PowerShell.

(`是也乎:`

AWS PowerShell <-- M$ 不会告你嘛?

)

- [logging2](https://github.com/vforgione/logging2)
    - 4 Stars, 0 Fork

A More Pythonic Logging System 



### (￣▽￣)

- [tankywoo/simiki](https://github.com/tankywoo/simiki)
    + 657 Stars, 95 Fork

Simiki is a simple wiki framework, written in Python.

(`是也乎:`

知道创宇 成员私人作品 md 的静态维基
)

# 是也乎

- 170504 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170504 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


