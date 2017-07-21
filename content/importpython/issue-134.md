Title: 蠎加载 134
Slug: importpython-134
Date: 2017-07-21 12:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 133](http://importpython.com/newsletter/no/134/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [首则 Python Notebook - 学习 Pandas](http://www.firstpythonnotebook.org/)
    + pandas

A step-by-step guide to analyzing data with Python and the Jupyter Notebook. This textbook will guide you through an investigation of money in politics using data from the California Civic Data Coalition. The course will teach you how to use pandas to read, filter, join, group, aggregate and rank structured data.

(`是也乎:`

值得体验, 一开始不是环境配置的都是骗纸...
)


- [在Python中重新进行单元测试和模拟](https://blog.fugue.co/2017-07-18-revisiting-unit-testing-and-mocking-in-python.html)
    + testing, mocking

This post covers some higher-level software engineering principles demonstrated in my experience with Python testing over the past year and half. In particular, I want to revisit the idea of patching mock objects in unit tests.


- [数据科学: Python vs Pandas vs Numpy 的性能 - 机器学习实验](http://machinelearningexp.com/data-science-performance-of-python-vs-pandas-vs-numpy/)
    + benchmark

Speed and time is a key factor for any Data Scientist. In business, you do not usually work with toy datasets having thousands of samples. It is more likely that your datasets will contain millions or hundreds of millions samples. Customer orders, web logs, billing events, stock prices – datasets now are huge.

(`是也乎:`

虽然 Numpy 以及 Pandas 都是 python 写的,
但是,作两样的事儿, 效率就是不同的哪...
)


- [通用 Jinja: 疯狂的想法 Python-ready 前端](https://whatisjasongoldstein.com/writing/universal-jinja/)
    + jinja, frontend development

- [Python 3 vs Python 2: 这次真咯不一样了](https://www.activestate.com/blog/2017/01/python-3-vs-python-2-its-different-time)
    + Python 3

A difficult decision for any Python team is whether to move from Python 2 and into Python 3. Although this is not a new decision for Python development teams, 2017 brings with it several important differences that make this decision crucial for proper forward planning. It feels like this is the year that we're really seeing the move to Python 3. It has been a long road, but Python 3 may finally have the upper hand.



- [Python 中的解析: 可用的所有工具和库](https://tomassetti.me/parsing-in-python/)
    + parsing

- [conda-merge](https://github.com/amitbeka/conda-merge)
    + project, reader submission

Tool for merging Conda (Anaconda) environment files into one file. This is used to merge your application environment file with any other environment file you might need (e.g. unit-tests, debugging, jupyter notebooks) and create a consistent environment without breaking dependencies from the previous environment files.

(`是也乎:`

刚需哪!

)

- [faker-schema](https://github.com/ueg1990/faker-schema)
    + project, reader submission

Generate fake data using joke2k's faker and your own schema.

(`是也乎:`

虚拟数据的模式化生成
)

- [Dockerizing Django, uWSGI 以及 Postgres 的生产路径](http://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/)
    + django, docker

Let’s dockerize a serious Django application. Curator's note - Love the humour in the article.


- [创建自己的 Cryptocurrency - 用 Python](https://cranklin.wordpress.com/2017/07/11/lets-create-our-own-cryptocurrency/)
    + cryptocurrency

I’ve been itching to build my own cryptocurrency… and I shall give it an unoriginal name - Cranky Coin. After giving it a lot of thought, I decided to use Python. GIL thread concurrency is sufficient. Mining might suffer, but can be replaced with a C mining module. Most importantly, code will be easier to read for open source contributors and will be heavily unit tested. Using frozen pip dependencies, virtualenv, and vagrant or docker, we can fire this up fairly easily under any operating system.

(`是也乎:`

又一种 Coin 的加密算法
)

- [创建 Jupyter 笔记本小部件](http://kazuar.github.io/jupyter-widget-tutorial/)
    + jupyter

This post will provide a step-by-step tutorial for creating and running a Jupyter widget.

- [让我们建立最小的块链](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)
    + blockchain

In Less Than 50 Lines of Python.


- [Python3 asyncio - 从同步代码调用异步代码](https://rokups.github.io/blog/#!pages/python3-asyncio-sync-async.md)
    + asyncio

(`是也乎:`

golang 的最大思想贡献: 用同步代码形式,运行异步效果
)


## 好物
~ 包/模块/库/片段...


- [yams](https://github.com/leesoh/yams)
    - 57 Stars, 6 Fork

A collection of Ansible roles for automating infosec builds.

(`是也乎:`

关键词->Ansible

)


- [dependency](https://github.com/encode/dependency)
    - 16 Stars, 0 Fork

A dependency injection framework for Python.

(`是也乎:`

Python 不是 JS , 随便注入没事儿嘛?
)

- [ptime](https://github.com/jcrist/ptime)
    - 15 Stars, 1 Fork

IPython magic for parallel profiling.

(`是也乎:`

ipynb 中的魔法算子也是可以自制的

)

- [sammy](https://github.com/capless/sammy)
    - 12 Stars, 1 Fork

Python library for generating AWS SAM (Serverless Application Model) templates with validation.

- [cpython_core_tutorial](https://github.com/haypo/cpython_core_tutorial)
    - 9 Stars, 0 Fork

Tutorial to contribute to the CPython project

(`是也乎:`

非常嗯哼的 CPython 入门教程
)

- [bod](https://github.com/diouziou/bod)
    - 3 Stars, 0 Fork

objdump beautifier

(`是也乎:`


![bod](https://github.com/diouziou/bod/raw/master/screenshot.png)

只是追加了颜色..

)


- [yacron:](https://github.com/gjcarneiro/yacron)
    - 0 Stars, 0 Fork

A modern Cron replacement that is Docker-friendly. 

(`是也乎:`

面向 Docker 的编程,越来越多了...
)


### (￣▽￣)

- [被忽视的攻击面：Python package 钓鱼](http://paper.seebug.org/326/)
    + pypi

(`是也乎:`

嚓了个嚓...
)


# 是也乎

- 170721 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170721 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


