Title: 蠎加载 110
Slug: importpython-110
Date: 2017-02-10 12:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 110](http://importpython.com/newsletter/no/110/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 支撑每秒百万请求](https://medium.com/@squeaky_pl/million-requests-per-second-with-python-95c137af319)
    + 

Japronto implements a pretty solid feature set:HTTP 1.x implementation with support for chunked uploadsFull support for HTTP pipelining, Keep-alive connections with configurable reaper, Support for synchronous and asynchronous views, Master-multiworker model based on forking, Support for code reloading on changes, Simple routing.

(`是也乎:`

Japronto 出来的...
)


- [Reuven Lerner: 设置 Jupyter 服务器的五分钟指南](http://blog.lerner.co.il/five-minute-guide-setting-jupyter-notebook-server/)
    + jupyter

Nearly every day, I teach a course in Python. And nearly every day, I thus use the Jupyter notebook: I do my live-coding demos in it, answer students’ questions using it, and also send it to my students at the end of the day, so that they can review my code without having to type furiously or take pictures of my screen.

(`是也乎:`

Jupyter 内置了...
)

- [使用 Django，Celery 和 rabbitMQ 构建异步任务](http://bookofstranger.com/asynchronous-tasks-using-django-celery-and-rabbitmq/)
    + celery, rabbitmq

In this post, I’ll be talking about setting up a distributed task processing system for doing asynchronous processing. As your website grows and handles lot of traffic, there naturally comes a need to ensure best performance for your users. While there are multiple things which need to be done to achieve that, one of the most important things is processing things in background.

(`是也乎:`

这个组合,有点儿...
)


- [使用 Arduino 和 Python 构建简单的摆锤来测量运动](https://www.instructables.com/id/Building-a-Simple-Pendulum-and-Measuring-Motion-Wi/)
    + arduino

We'll build a classic and important physical system, the simple pendulum. We'll use an Arduino and a potentiometer to measure the amplitude of the pendulum's motion and Python to read and visualize our data.


- [什么是Flake8和为什么我们应该使用它？?](https://medium.com/@itechgirly/what-is-flake8-and-why-we-should-use-it-b89bd78073f2?source=rss------python-5)
    + linting

There are a couple good python code linter tools you can use. The one I’ve recently discovered is a Flake8. Which is “the wrapper which verifies pep8, pyflakes and circular complexity “. It has low rate of false positives.

(`是也乎:`

徦阳性少的 linter..
)


- [用 Python 运动跟踪](http://derek.simkowiak.net/motion-tracking-with-python/)
    + motion tracking

My daughter, Alex, was in the 6th grade this year. For her science fair project, Alex wanted to do something involving animals. I had read about an experiment where lab rats were recorded on video, and their motion was analyzed by a computer (to determine the effects of a neurotoxin). We owned 2 gerbils, Havoc and Zoom, so I suggested to Alex we do a similar experiment with the gerbils. For some reason, she didn’t want to test a neurotoxin on her pets, so instead she decided to test the effects of full spectrum lighting on their movement.

(`是也乎:`

儿童行为心理学方面的嗯哼
)

- [用 Pytest 测试 Python 应用](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)
    + testing

Pytest stands out among Python testing tools due to its ease of use. This tutorial will get you started with using pytest to test your next Python project.

(`是也乎:`

Pytest 已经成为标准了...
)

- [为什么要学习Python？这里有8个数据驱动的原因](https://dbader.org/blog/why-learn-python)
    + core-python

Is Python worth learning? We’ve interviewed experts and surveyed the job market to identify the key reasons why you should learn Python today.




- [Python Excel 教程: 初级导引](https://medium.com/@kacawi/python-excel-tutorial-the-definitive-guide-934ee6dd15b0)
    + excel

- [Python 的黑客指南 - 作者访谈](http://importpython.com/blog/post/hackers-guide-python-book-review-and-interview-author)
    + book review

- [机器学习与 Jupyter 使用 Scala，Spark 和 Python：安装](https://medium.com/@faizanahemad/machine-learning-with-jupyter-using-scala-spark-and-python-the-setup-62d05b0c7f56?source=rss------scala-5)
    + jupyter, spark

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
    + style guide

This guide has been there for a while, sharing it again.

(`是也乎:`

这份文档,值得一读再读
)

- [绘制IMDb平均评分](https://medium.com/@rubfi/plotting-imdb-average-rating-6d9e69d8049f?source=rss------python-5)
    + matplotlib

In the previous post (Playing with IMDB, Python and Pandas), I tried to obtain the average IMDb rating of an actress. This time I’ll play with matplotlib in order to plot the evolution of an actress over the years.


- [在 Python 中处理ssh](https://kushaldas.in/posts/working-over-ssh-in-python.html)
    + ssh

Working with the remote servers is a common scenario for most of us. Sometimes, we do our actual work over those remote computers, sometimes our code does something for us in the remote systems. Even Vagrant instances on your laptop are also remote systems, you still have to ssh into those systems to get things done.

(`是也乎:`

早已可以了...    
)

- [使用 Docker，Python，Amazon SNS 和 SQS 构建实时事件驱动的访问日志系统](https://hackernoon.com/building-a-real-time-event-driven-system-using-docker-python-amazon-sns-sqs-985759e660eb#.fyhqc0y61)
    + docker, aws, sns, sqs

- [简易构造符号链接](https://dmerej.info/blog/post/symlinks-made-easier/)
    + code snippet

I never could remember how to use it, mixing the order of the parameters, and the man page did not help. So I thought, why not write a small wrapper around it?




## 好物
~ 包/模块/库/片段...

- [tweets_analyzer](https://github.com/x0rz/tweets_analyzer)
    - 500 Stars, 51 Fork

Tweets 元数据抓取器和活动分析器

- [pyzdb](https://github.com/asrp/pyzdb)
    - 230 Stars, 7 Fork

用 ZeroMQ 的轻量级数据库，具有 Python 语法查询接口

- [deep-makeover](https://github.com/david-gpu/deep-makeover)
    - 105 Stars, 6 Fork

Deep learning project to transform male portraits into female and vice versa

(`是也乎:`

![example_male_to_female](https://github.com/david-gpu/deep-makeover/raw/master/images/example_male_to_female.jpg)

)

- [bucketstore](https://github.com/kennethreitz/bucketstore)
    - 94 Stars, 9 Fork

用于与Amazon S3交互的简单库。

- [pycycle](https://github.com/bndr/pycycle)
    - 60 Stars, 3 Fork

用于精确定位Python中的循环导入的工具。 在项目中查找循环导入

(`是也乎:`

值得嗯哼

![camo pycycle](https://camo.githubusercontent.com/4d5000d5e9b834e9b60b1189b53a595f0b1c5c1b/68747470733a2f2f692e696d6775722e636f6d2f384a654c5178752e676966)
)

- [sceptre](https://github.com/cloudreach/sceptre)
    - 59 Stars, 6 Fork

构建更好的 AWS 基础架构

- [lifelights](https://github.com/jjensn/lifelights)
    - 42 Stars, 8 Fork

视频游戏和家庭自动化。 基于游戏中状态控制物联网设备。


- [fastq-and-furious](https://github.com/lgautier/fastq-and-furious)
    - 14 Stars, 0 Fork

以 Python 有效处理 FASTQ 文件


### (￣▽￣)
~ 

# 是也乎

- 170210 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170210 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


