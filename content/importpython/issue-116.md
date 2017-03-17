Title: 蠎加载 116
Slug: importpython-116
Date: 2017-03-17 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 116](http://importpython.com/newsletter/no/116/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [如何从内存中恢复丢失的 python 源代码?](https://gist.github.com/simonw/8aa492e59265c1a021f5c5618f9e6b12)
    + core-python

I used "git checkout --" on the wrong file and managed to delete the code I had just written... but it was still running in a process in a docker container. Here's how I got it back, using 

https://pypi.python.org/pypi/pyrasite/ 

and 

https://pypi.python.org/pypi/uncompyle6

(`是也乎:`

可怜的人...
)



- [PEP 308 以及为毛俺依然恨 Python](http://dvt.name/2017/03/10/pep-308-and-why-i-still-hate-python/)
    + core-python

I’m not a Python guy, but it seems that every job I’ve had has slowly pushed me into doing more and more Python until I end up doing nothing but Python all day. And I hate doing Python all day.

(`是也乎:`

简单的说怼数学计算时,被 Py 的任性怒了...
)

- [python 的怪代码](http://python-catalin.blogspot.com/2017/03/strange-code-in-python.html)
    + code snippets

Code snippets that makes you wonder what's happening?

(`是也乎:`

所谓活久见...
)

- [MetPy：驯服天气与Python - 剧集100](https://www.podcastinit.com/episode-100-metpy-with-ryan-may-sean-arms-and-john-leeman/)
    + podcast

What’s the weather tomorrow? That’s the question that meteorologists are always trying to get better at answering. This week the developers of MetPy discuss how their project is used in that quest and the challenges that are inherent in atmospheric and weather research. It is a fascinating look at dealing with uncertainty and using messy, multidimensional data to model a massively complex system.


- [Django 周刊 30](http://djangoweekly.com/newsletter/no/30/)
    + newsletter

If you use Django framework and want to keep updated with what's happening in the Django world, check out django weekly


- [有效的 Python 学习姿势](https://www.crowdcast.io/e/learning/register)
    + video

When learning a programming language, how do you know whether the effort you're putting in is working or whether you're wasting your time?. We'll be chatting with Michael Herman and Evan Moore about techniques you can use to be more effective during your Python learning adventures.

(`是也乎:`

关键就是得有一套靠谱的不依赖其他人的明确自己作的是否对的指标
)



- [从 __past__ 引入 bytes_literals](http://gregoryszorc.com/blog/2017/03/13/from-__past__-import-bytes_literals/)

- [Intel 的 Python 发行版提供数学能力的大提升](http://www.infoworld.com/article/3044512/application-development/intels-python-distribution-provides-a-major-math-boost.html)
    + intel

The still-in-beta Python distribution uses Math Kernel Library to speed up processing on Intel hardware.

(`是也乎:`

Intel 这么博爱...
)


- [客户数据驱动灯光秀](https://medium.com/zingle/customer-data-driven-light-shows-7800883182bc#.utvsgwxol)
    + IOT

- [Fast_Multi_Style_Transfer-tf](https://github.com/Heumi/Fast_Multi_Style_Transfer-tf)

Implementation of Google Brain's A Learned Representation For Artistic Style in Tensorflow. You can mix various type of style images using just One Model and it's still Fast.


(`是也乎:`

TF 中艺术风格的嗯哼
)

- [诊断并修复 Python 中的内存嗯哼](https://blog.fugue.co/2017-03-06-diagnosing-and-fixing-memory-leaks-in-python.html)
    + debugging, memory leaks

One thing we've learned from building complex software for the cloud is that a language is only as good as its debugging and profiling tools. Logic errors, CPU spikes, and memory leaks are inevitable, but a good debugger, CPU profiler, and memory profiler can make finding these errors significantly easier and faster.

(`是也乎:`

CPU 中的问题追踪,马上也将过渡到 TPU 的了...
)

- [Python 中拟合高斯过程模型](https://blog.dominodatalab.com/fitting-gaussian-process-models-python/)
    + numpy, stats

- [k 最近邻](https://pythonspot.com/k-nearest-neighbors/)
    + machine learning

- [使用Python和Django Rest Framework创建生产就绪的API - 第3部分](https://www.andreagrandi.it/2017/03/12/creating-a-production-ready-api-with-python-and-django-rest-framework-part-3/)
    + django

(`是也乎:`

上期说的 google 的 fire 也是相似的嗯哼
)

- [干掉你的Python代码与装饰](https://code.tutsplus.com/articles/dry-your-python-code-with-decorators--cms-28208)
    + decorators

- [如何使用Python编写Collectd插件？](https://blog.dbrgn.ch/2017/3/10/write-a-collectd-python-plugin/)
    + collectd, monitoring deployments

Collectd is a system statistics collection daemon. It gathers a lot of information about the system it's running on, and passes it on to a software that can process and visualize that information, e.g. Grafana. Collectd already brings along a lot of built-in plugins to gather information about the system load, the network traffic, available entropy, various sensors, etc. But sometimes there's a value that you want to log which is not covered by an existing plugin.

(`是也乎:`

SCM 一直是 Python 的擅长领域...
)

## 好物
~ 包/模块/库/片段...


- [pytorch-tutorial](https://github.com/yunjey/pytorch-tutorial)
    - 1160 Stars, 158 Fork

Tutorial for researchers to learn deep learning with pytorch.

(`是也乎:`

深度学习的 pytorch 嗯哼教程
)

- [clickbaits_revisited](https://github.com/abhishekkrthakur/clickbaits_revisited)
    - 97 Stars, 13 Fork

Deep learning models to identify clickbaits taking content into consideration.

- [pymetaterp](https://github.com/asrp/pymetaterp)
    - 19 Stars, 0 Fork

A python parser that builds python ASTs in 502 lines of python without using modules.

(`是也乎:`

原生 ASTs 解析器
)

- [sqlalchemy-mixins](https://github.com/absent1706/sqlalchemy-mixins)
    - 19 Stars, 0 Fork

Active Record, Django-like queries, nested eager load and beauty __repr__ for SQLAlchemy

(`是也乎:`

这么多年了 Active Record 一直是 OS 之外最大的代码片段仓库
)

- [newrelic-cli](https://github.com/NativeInstruments/newrelic-cli)
    - 13 Stars, 0 Fork

Newrelic client written in Python providing both CLI and Python interfaces. 

(`是也乎:`

Newrelic ~ 又一个性能监察器...
)

### (￣▽￣)
~ 

# 是也乎

- 170316 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170316 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


