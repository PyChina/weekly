Title: 蠎加载 76
Slug: importpython-76
Date: 2016-06-10 16:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 76](http://importpython.com/newsletter/no/76/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Q&A: Guido van Rossum 有关 Python 未来策划](http://www.infoworld.com/article/3078633/application-development/qa-guido-van-rossum-on-pythons-next-steps.html)
    + interview

Python 创始者/仁义的暴君 Guido 老爹的采访

(`是也乎:`

老爹每年的公开分享, 都是 Python 的宏观规划,必须理解,在理解中理解...

简单的说:加紧 mobile 和 browser 的浸入,只是当前没有明确的好招;
PyPy 很可用了, 但是 Py3 的目标也包含性能的;Py 的整体生态的是好的,没问题的.
)

- [Python: 正则表达式介绍](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/8tGh175aO6E/)  
    - core python

Regular expressions are basically a tiny language all their own that you can use inside of Python and many other programming languages. You will often hear regular expressions referred to as “regex”, “regexp” or just “RE”. Some languages, such as Perl and Ruby, actually support regular expression syntax directly in the language itself. Python only supports them via a library that you need to import. The primary use for regular expressions is matching strings. You create the string matching rules using a regular expression and then you apply it to a string to see if there are any matches.

(`是也乎:`

正则表达式几乎是一种独立语言了, 在 Py 中当然也能简洁的用起来.
)

- [Python lambda 表达式的爆发](https://blogs.msdn.microsoft.com/pythonengineering/2016/06/07/lambda-exp-unleashed/)
    + functional programming

Lambda expressions provide a way to pass functionality into a function. Sadly, Python puts two annoying restrictions on lambda expressions. First, lambdas can only contain an expression, not statements. Second, lambdas can’t be serialized to disk. This blog shows how we can work around these restrictions and unleash the full power of lambdas.

(`是也乎:`

如何在 Py 中真正引爆 Lambada 的能量?
用 dill 来替代 pickle!
ANACONDA 内置实用序列化模块...
)

- [在 Python 折腾点集群](http://moderndata.plot.ly/point-clustering-in-python/)
    + machine learning

By definition, clustering is a task of grouping a set of objects in a way that objects in a particular group are more similar to each other rather than the objects in the other groups. It has multiple applications in almost every field. You can even segment your customers into different groups based on their purchase patterns. This is a Python script demonstrating the basic clustering algorithm, “k-means”. Also, it will plot the clusters using Plotly API. It uses sample data points for now, but you can easily feed in your dataset.

(`是也乎:`

正热门的数据科学又一实例,"k-means" 完成聚类, 用 Plotly 接口进行可视化
)

- [Flask 规模化](https://www.youtube.com/watch?v=tdIIJuPh3SI)
    + flask

If you are a flask user. You would greatly benefit by this pretty exhaustive (information wise) talk. Do you think that because Flask is a micro-framework, it must only be good for small, toy-like web applications? Well, not at all! In this tutorial I am going to show you a few patterns and best practices that can take your Flask application to the next level.

(`是也乎:`

作为微型框架 flask 也可以提供大规模服务!

PS: 同理 Bottle 也是可以的...
)


- [见 Python, 遇 Python Go, Go Python Go](http://feedproxy.google.com/~r/heroku/~3/2kbyblVkDlA/see_python_see_python_go_go_python_go)

Today we're going to make a Python library that is actually the Go webserver, for which we can write handlers in Python. It makes Python servers really fast, and—more importantly—it’s a bit fun and experimental. Andrey Petrov is the author of urllib3. If you have coded in Go you would realize this is pretty cool idea.

(`是也乎:`

人生苦短, Python 当歌
!-)


- [从头创建 Python 框架 - Code walkthrough](http://mattscodecave.com/posts/simple-python-framework-from-scratch.html)
    + web framework
You're curious how web frameworks work because you want to become a better web developer. This post aims to describe what I learned by writing a small server and framework by explaining the design and implementation process step by step, function by function.

(`是也乎:`

源发自 ![the-clean-architecture](https://blog.8thlight.com/assets/posts/2012-08-13-the-clean-architecture/CleanArchitecture-81565aba46f035911a5018e77a0f2d4e.jpg)

的框架实例...

)

- [5个值得爱上的 Django 包 — Medium](https://medium.com/@raiderrobert/5-django-packages-that-get-too-little-love-d55232c28640#.dcmzfkann)
    + django

Lots of packages get a lot of love like django-rest-framework and wagtail, and rightfully so, they’re awesome! But I wanted to give some less well know ones some love.



- [Pycon India CFP 来也](https://in.pycon.org/cfp/2016/proposals/)
    + pycon

PyCon India, the premier conference in India on using and developing the Python programming language is conducted annually by the Python developer community. It attracts the best Python programmers across the country and abroad. Submit your proposal here.



- [用装饰器维护 Python 硬盘缓存](http://tohyongcheng.github.io/python/2016/06/07/persisting-a-cache-in-python-to-disk.html)
    + code snippet

Caches are important in helping to solve time complexity issues, and ensure that we don’t run a time-consuming program twice. You never know when your scripts can just stop abruptly, and then you lose all the information in your cache, and you have you run everything all over again.In order to counter this, saving your cache to a disk is something that can be very helpful in that it allows state to be saved to disk, and be retrieved from it anytime as long as its there.

(`是也乎:`

保卫我们的运行时数据,用 修饰符, 随时导出到硬盘!
)

- [用 Python 从头实现神经网络](http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/)
    + machine learning

In this post we will implement a simple 3-layer neural network from scratch. We won’t derive all the math that’s required, but I will try to give an intuitive explanation of what we are doing. I will also point to resources for you read up on the details. Here I’m assuming that you are familiar with basic Calculus and Machine Learning concepts, e.g. you know what classification and regularization is. But even if you’re not familiar with any of the above this post could still turn out to be interesting ;)


- [用纸和 Python 实现的 Enigma 机](http://williamedwardscoder.tumblr.com/post/145304200648)
    + crytography

It turns out my kids have been sending each other secret messages, enciphered with a substitution cipher of their own invention! They only let me see the secret key when I agreed to help them mix up a very complicated recipe for invisible ink.

(`是也乎:`

二战中最强大的德军密码机,现在用纸+脚本就可以完美复刻.
)

- [Python 类属性](http://python-resources.pythonblogs.com/304_python_resources/archive/1548_python_class_attributes.html)
    + core python

I had a programming interview recently, a phone-screen in which we used a collaborative text editor. I was asked to implement a certain API, and chose to do so in Python. Abstracting away the problem statement, let’s say I needed a class whose instances stored some data and some other_data. As it turns out, we were both wrong. The real answer lay in understanding the distinction between class and instance attributes. 


(`是也乎:`

是的,虽然是 Python 的基础功能,但是,很少人用对味儿.
)

## 活动
~ Upcoming Conference / User Group Meet

- [GeoPython 2016](http://www.geopython.net/)
- [PyCon Singapore 2016](https://pycon.sg/)
- [EuroPython 2016](http://ep2016.europython.eu/)
- [PyOhio 2016](http://pyohio.org/)
- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [EuroScipy 2016](https://www.euroscipy.org/2016)
- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon ZA 2016](https://za.pycon.org/)

## 项目
~ 包/模块/库/片段...


- [dl-docker](https://github.com/saiprashanths/dl-docker)
    - 403 Stars, 33 Fork

一键安装 `深度学习` 相关的所有东西,
用 Docker.
(含 TensorFlow, Theano, Torch, Caffe, etc.)

- [LeadQualifier](https://github.com/xeneta/LeadQualifier)
    - 114 Stars, 21 Fork

对 Xeneta 销售数据进行机械学习分析的相关脚本


- [affirm](https://github.com/gooli/affirm)
    - 24 Stars, 0 Fork

对断言的增强, 
每当运行出错时, 当然希望能输出更多参考信息.

(`是也乎:`

希望能进入内建模块的又一个人性化实用模块
)

- [flask-konch](https://github.com/sloria/flask-konch)
    - 22 Stars, 0 Fork

对 Flask CLI 的增强

- [TextSuggest](https://github.com/bharadwaj-raju/TextSuggest)
    - 17 Stars, 0 Fork

在 GUI 上自动完成单词的简单工具, Linux 的.

- [MarkdownPicPicker](https://github.com/kingname/MarkdownPicPicker)
    - 16 Stars, 2 Fork

支持 md 写作时的图片发布工具 ,
自动从剪贴板中提取图像上传云端,
并组织成 md 图片字串复制回 剪贴板.

- [yascrapy](https://github.com/jianxunio/yascrapy)
    - 15 Stars, 0 Fork

用 golang 和 Python 联合完成的高性能分布式 爬虫.

(`是也乎:`

名字叫 `又一个XXX` 的很容易成功, 
嘦解决初代模块的痛点问题.

Fuubo 团队作品!
是的, 为一个 HR 服务提供后台数据用.

)

- [libfib](https://github.com/karan/libfib)
    - 13 Stars, 0 Fork

尝试直接从 Py 运行 go 代码.

(`是也乎:`

再次检验了 CPython 的 C 语言接口能力而已
)

- [scroller](https://github.com/kbrgl/scroller)
    - 12 Stars, 0 Fork

能在终端绘制动画文字效果的工具.

(`是也乎:`

![scroller](https://github.com/kbrgl/scroller/raw/master/scroller.gif)
)

- [Python-Design-Patterns](https://github.com/buckyroberts/Python-Design-Patterns)
    - 9 Stars, 0 Fork

Python Design Patterns. Here is an overview of several different design patterns and concepts in Python.



## DAMA 无责任推荐

- 贡献一个刚刚好的python仓库吧：https://github.com/shell909090/webserver

> 从头开始写一个 web服务器，python代码刚刚好1046行
> 由著名的 7牛 CSO 分享
> 引发自 [爱上Python](https://book.douban.com/subject/26807339/)`~送书换头像` 活动


# 是也乎

- 160613 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160610 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


