Title: 蠎加载 133
Slug: importpython-133
Date: 2017-07-14 12:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 133](http://importpython.com/newsletter/no/133/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [与 Python 中长时间运行的子进程交互](http://eli.thegreenplace.net/2017/interacting-with-a-long-running-child-process-in-python/)
    + debugging

The Python subprocess module is a powerful swiss-army knife for launching and interacting with child processes. It comes with several high-level APIs like call, check_output and (starting with Python 3.5) run that are focused at child processes our program runs and waits to complete. In this post I want to discuss a variation of this task that is less directly addressed - long-running child processes.

(`是也乎:`

作者脑补出了几种方案, 但是,都不嗯哼...
其实吧长时间运行, 要不服务化, 要不事务化,
就别想着中间还能嗯哼什么, 毕竟这是冯机体系不是代码和运行时一致的 LISP 世界.
)

- [传说: 一个深度学习分类器，可以压缩 Unicode 和奇怪的 Youtube 评论](https://medium.com/@hhl60492/seeing-words-a-deep-learning-spam-classifier-that-can-crunch-unicode-and-weird-youtube-comments-3c00f0ae7d10)
    + machine learning

One of the things I’ve been thinking about recently is how to do natural language processing (NLP) effectively with deep neural networks using real world language examples. An example would be to classify the youtube comment


- [探索并清洗科学家联盟的卫星数据库](http://probcomp.csail.mit.edu/bayesdb/satellites-notebook.html)
    + data science

The Union of Concerned Scientists maintains a database of ~1000 Earth satellites. For the majority of satellites, it includes kinematic, material, electrical, political, functional, and economic characteristics, such as dry mass, launch date, orbit type, country of operator, and purpose. The data appears to have been mirrored on other satellite search websites, e.g. http://satellites.findthedata.com/ . This iPython notebook describes a sequence of interactions with a snapshot of this database using the bayeslite implementation of BayesDB, using the Python bayeslite client library. The snapshot includes a population of satellites defined using the UCS data as well as a constellation of generative probabilistic models for this population.


- [实体提取和网络分析](http://brandonrose.org/ner2sna)
    + machine learning

How you can extract meaningful information from raw text and use it to analyze the networks of individuals hidden within your data set.


- [使用 scikit-learn 制作电子商务业务决策](https://medium.com/tensorist/making-e-commerce-business-decisions-using-scikit-learn-2dd1d76ab675)
    + machine learning, scikit-learn

Today, let’s learn how to build a simple linear regression model using Python’s Pandas and Scikit-learn libraries. Our goal is to build a model that analyses customer data and solves a problem for a (simulated) e-commerce business.

(`是也乎:`

反复强调了简单的, 即无实用价值的...
)

- [Python 怪癖: 注释](https://medium.com/@PhilipTrauner/python-quirks-comments-324bbf88612c)
    + core-python

- [使用 Locust.io 和 Docker Swarm 进行负载测试](https://wheniwork.engineering/load-testing-with-locust-io-docker-swarm-d78a2602997a)
    + testing, docker, locust

- [FAT Python : Python优化的下一章](https://hackernoon.com/fat-python-the-next-chapter-in-python-optimization-69dc974bcca2)
    + optimization

The FAT Python project was started by Victor Stinner in October 2015 to try to solve issues of previous attempts of “static optimizers” for Python. Victor has created a set of changes to CPython (Python Enhancement Proposals or “PEPs”), some example optimizations and benchmarks. We’ll explore those 3 levels in this article.


- [K 平均聚类在 Python 中](https://decisionstats.com/2017/07/07/k-means-clustering-in-python/)
    + machine learning

- [f-strings For the Win](http://albertoconnor.ca/f-strings-for-the-win.html)
    + f-strings

It has been a long time coming, but I am now actively migrating existing projects to Python 3. Python 3.6 specifically, because when I am done I will be able to take advantage of my new favourite feature everywhere! That feature is f-strings.

(`是也乎:`

[PEP-0498](https://www.python.org/dev/peps/pep-0498/) 的心声


    Python 3.6.1 (...) 
    Type "help", "copyright", "credits" or "license" for more...
    >>> name = 'Albert'
    >>> f'Hello, {name}!'
    'Hello, Albert!'

嚓, f 算子...
)

- [一个奇怪的技巧将简化 ETL 工作流程针脚修复技术 - 多线程](http://multithreaded.stitchfix.com/blog/2017/07/06/one-weird-trick/)

- [Seashells](https://seashells.io/)
    + project

Seashells lets you pipe output from command-line programs to the web in real-time, even without installing any new software on your machine. You can use it to monitor long-running processes like experiments that print progress to the console. You can also use Seashells to share output with friends!

(`是也乎:`

真心不怕嗯哼了?!

)


- [为 Python 开发人员安排 Act Assert 模式 // James Cooke // Brighton-based Python developer](http://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html)
    + testing
This is the first post in a series exploring the Arrange Act Assert pattern and how to apply it to Python tests.


- [回文日期](https://github.com/flutefreak7/palindrome_dates/blob/master/Palindrome%20Days.ipynb)
    + numpy, pandas, code snippets


- [使用 AWS Lambda 将 API 结果保存到 PostgreSQL 中](https://caseym.me/save-api-results-to-postgresql-for-free-with-aws-lambda/)
    + aws lambda

In this tutorial I will show you how to use Amazon Web Services (AWS) Lambda service to save the results of an API response to a PostgreSQL database on a recurring schedule.


- [从 Matplotlib 开始 - Python的数据可视化](http://kanoki.org/2017/07/09/get-started-with-matplotlib-data-visualization-for-python/)    
    + matpoltlib

(`是也乎:`

讲真, 除非你只要个图片结果,
否则,还是多看看可以直接输出为 html 的
[![Bokeh](http://bokeh.pydata.org/en/latest/_static/images/logo.png)](http://bokeh.pydata.org/en/latest/)

)




## 好物
~ 包/模块/库/片段...

- [crackcoin](https://github.com/DutchGraa/crackcoin)
    - 392 Stars, 28 Fork

Very basic blockchain-free cryptocurrency PoC in Python.

(`是也乎:`

UDP 环境中的简单加密...
)

- [crocs](https://github.com/iogf/crocs)
    - 334 Stars, 18 Fork

Write regex using pure python class/function syntax and test it better. (Regex for humans).

(`是也乎:`

正则表达式的 pythonic 使用...

)

- [django-eraserhead](https://github.com/dizballanze/django-eraserhead)
    - 67 Stars, 0 Fork

Provide hints to optimize database usage by deferring unused fields (and more).

- [winton-kafka-streams](https://github.com/wintoncode/winton-kafka-streams)
    - 16 Stars, 3 Fork

A Python implementation of Apache Kafka Streams

- [py-clui](https://github.com/hmleal/py-clui)
    - 13 Stars, 0 Fork

This is a Python toolkit for quickly building nice looking command line interfaces.

(`是也乎:`

![spinner](https://raw.githubusercontent.com/hmleal/py-clui/master/docs/spinner.gif)

叕一个 CLI 界面构建框架..
)


- [s3-environ](https://github.com/jonatasbaldin/s3-environ)
    - 8 Stars, 0 Fork

Load environment variables from a AWS S3 file. 

(`是也乎:`

嗯哼?将要命的环境变量部属到 S3 中?!
)


### (￣▽￣)

- [被忽视的攻击面：Python package 钓鱼](http://paper.seebug.org/326/)
    + pypi

(`是也乎:`

嚓了个嚓...
)


# 是也乎

- 170714 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170714 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


