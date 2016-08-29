Title: 蠎加载 84
Slug: importpython-84
Date: 2016-08-04 22:22
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 84](http://importpython.com/newsletter/no/84/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Django 图书全集](http://djangoweekly.com/books/)
    + books

Djangoweekly has a listing of all published Django books on one page. Note check publication date and which version of Django the book is using.

- [为毛应该用 Python 3?](https://eev.ee/blog/2016/07/31/python-faq-why-should-i-use-python-3)
    + python3

The short answer is: because it’s the actively-developed version of the language, and you should use it for the same reason you’d use 2.7 instead of 2.6. If you’re here, I’m guessing that’s not enough. You need something to sweeten the deal. Well, friend, I have got a whole mess of sugar cubes just for you.

(`是也乎:`

何时没有这种文章发布了, 才说明 Py3 真正获得用户肯定了
)

- [和 Josh Gordon 学习机械学习](https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal)
    + machine learning, video

Series of Python Videos by Josh Gordon of Google teaching Machine learning basics.

- [流利的 Python: 特殊方法的威能](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/gxcXOFutozs/fluent-python-new)
    + pythonic

Pythonistas praise a good API by calling it “Pythonic.” That quality has much to do with proper use of the special methods used in the Python Data model, which define the essential behaviors that we expect in objects. Perhaps you’ve used Python for years. Do you really know it? This tutorial is intended for a Python programmer who has working/practical knowledge of the language plus an understanding of object-oriented programming, who now needs to learn how to write idiomatic APIs

(`是也乎:`

正确用好内置数据结构是一组稳固 API 的基础.
)


- [如何构建 Django 信号](http://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html)
    + django

The Django Signals is a strategy to allow decoupled applications to get notified when certain events occur. Let’s say you want to invalidate a cached page everytime a given model instance is updated, but there are several places in your code base that this model can be updated. You can do that using signals, hooking some pieces of code to be executed everytime this specific model’s save method is trigged. In this tutorial I will present you the built-in signals and give you some general advices about the best practices.

(`是也乎:`

嗯哼,将 GUI 的信号/槽 机制用在 web 中.
)

- [Semaphore 社区: 用 Behave 进行 Python 应用行为测试](https://semaphoreci.com/community/tutorials/getting-started-with-behavior-testing-in-python-with-behave)
    + testing

Learn how to write behavioral tests for your next Python application using the Behave library.

- [Django 1.10 发布](https://www.djangoproject.com/weblog/2016/aug/01/django-110-released/)
    + django, release

Full text search for PostgreSQL. New-style middleware to solve the lack of strict request/response layering of the old-style of middleware. Official support for Unicode usernames. Check release notes for more info.

- [自动化 OSINT: 暗网 OSINT 使用 Python 和 OnionScan: 第一节](http://www.automatingosint.com/blog/2016/07/dark-web-osint-with-python-and-onionscan-part-one/)
    + security

You may have heard of this awesome tool called OnionScan that is used to scan hidden services in the dark web looking for potential data leaks. Recently the project released some cool visualizations and a high level description of what their scanning results looked like. What they didn’t provide is how to actually go about scanning as much of the dark web as possible, and then how to produce those very cool visualizations that they show.

(`是也乎:`

类似 Zoomeye 服务,从 dark web 中为用户进行数据泄漏检验,
也是数据科学的一种, 所以, 必然的 Python 可以
)


- ["避免知识的诅咒": 社区服务奖获得者 Ned Batchelder 曰](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/8OEAOmeX_NQ/avoiding-curse-of-knowledge-ned-batchelder.html)
    + community

The Python Software Foundation recognized Batchelder with a Community Service Award for his tireless work helping run the Boston Python user group, being a regular speaker at conferences, maintaining coverage.py, and being a friendly face for the community on IRC and elsewhere

(`是也乎:`

coverage.py 的创造者
)

- [Python 201: multiprocessing 教程](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/pF_P0Zp45-M/)
    + multiprocessing

The multiprocessing module was added to Python in version 2.6. It was originally defined in PEP 371 by Jesse Noller and Richard Oudkerk. The multiprocessing module allows you to spawn processes in much that same manner than you can spawn threads with the threading module. The idea here is that because you are now spawning processes, you can avoid the Global Interpreter Lock (GIL) and take full advantages of multiple processors on a machine.

(`是也乎:`

Py2.6 就加入内置模块了, 但是,用起来的不多
)

- [Django Channels 和 Celery 样例 - Vincent Zhang](http://vincenttide.com/blog/1/django-channels-and-celery-example/)
    + django, celery

In this tutorial, I will go over how to setup a Django Channels project to work with Celery and have instant notification when task starts and completes. Django Channels uses WebSockets to enable two-way communication between the server and browser client. It is assumed that the reader is comfortable with how to setup a normal Django project and we will only cover the parts relating to Channels and Celery.

(`是也乎:`

华人,当然外国的...
)


- [用 Keras 和 Python 开始深度学习](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/v4JMuiflIAk/getting-started-with-deep-learning-using-keras-and-python-new)
    + deep learning

Despite all the recent buzz about deep learning, the design and testing of a neural network pipeline may become a task for developers who aren't machine learning specialists. This tutorial is intended for a software developer who has intermediate experience in Python, plus some hands-on experience developing data pipelines and working with machine learning use cases, who now needs to learn how to build high-performance classifiers based on deep learning.

- [udatetime 已经支持 PyPy](https://aboutsimon.com/blog/2016/08/02/udatetime-pypy-support-ultra-fast.html)
    + pypy

I just finished the performance optimized pure Python implementation of my RFC3339 date-time library udatetime for PyPy and Python 3.5. The benchmark say PyPy is now officially the fastest with udatetime. Again it’s astonishing how good PyPy performs.

- [连续分析新闻: Dask 和 scikit-learn: 教程三部曲](https://www.continuum.io/blog/developer-blog/dask-and-scikit-learn-3-part-tutorial)
    + scikit

Dask core contributor Jim Crist has put together a series of posts discussing some recent experiments combining Dask and scikit-learn on his blog, Marginally Stable. The tutorial spans three posts, which covers model parallelism, data parallelism and combining the two with a real-life dataset.

(`是也乎:`

主要分享 涵盖模型的并行，数据并行和两个与现实生活相结合的数据集
)

- [Python 内脏: Hello, ceval.c!](https://tech.blog.aknin.name/category/my-projects/pythons-innards/)
    + core python

The “Python’s Innards” series owes its existence, at least in part, to hearing one of the Python-Fu masters in my previous workplace say something about a switch statement so large that it was needed to break it up just so some compilers won’t choke on it. I remember thinking then: “Choke the compiler with a switch? Hrmf, let me see that code.” Turns out that this switch can be found in ./Python/ceval.c. 

(`是也乎:`

追查 switch 到源代码
)

## 活动
~ Upcoming Conference / User Group Meet

- [PyCon MY 2016](http://pycon.my/)
- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon JP 2016](https://pycon.jp/2016/)
- [PyCon ZA 2016](https://za.pycon.org/)




## 项目
~ 包/模块/库/片段...

- [deep-learning-models](https://github.com/fchollet/deep-learning-models)
    - 110 Stars, 15 Fork

Keras 代码和权重文件 的深度学习模块


- [PokeVisionFinder](https://github.com/encode32/PokeVisionFinder)
    - 22 Stars, 12 Fork

PokeVision 搜索器

- [visualize_ML](https://github.com/ayush1997/visualize_ML)
    - 19 Stars, 1 Fork

可视化机械学习相关过程的 Py 包

- [python-vulkan-triangle](https://github.com/gabdube/python-vulkan-triangle)
    - 14 Stars, 0 Fork

Standalone python program that draws a triangle using vulkan on Windows and Linux

(`是也乎:`

![vulkan-triangle](https://github.com/gabdube/python-vulkan-triangle/raw/master/images/ubuntu.png)

这货的生成
)

- [getPokeStats](https://github.com/traversc/getPokeStats)
    - 11 Stars, 5 Fork

Get exact IVs for Pokemon Go

- [Trump-Tweets](https://github.com/sashaperigo/Trump-Tweets)
    - 4 Stars, 1 Fork

Donald Trump's entire Twitter feed and the script used to scrape it.

- [minigraphdb](https://github.com/yantisj/minigraphdb)
    - 3 Stars, 0 Fork

用 Python 3 实现的内存极简向量图数据库

(`是也乎:`

![sample-graph](https://github.com/yantisj/minigraphdb/raw/master/sample-graph.png)

手绘原理图最赛高!!

)
## DAMA
~ 无责任推荐

# 是也乎

- 160805 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160804 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


