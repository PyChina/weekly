Title: 蠎加载 90
Slug: importpython-90
Date: 2016-09-15 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 90](http://importpython.com/newsletter/no/90/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [在 Python 中的实时数据流管道](https://github.com/plecto/motorway)
    + streaming

Motorway is a real-time data pipeline, much like Apache Storm - but made in Python :-) We use it over at Plecto and we're really happy with it - but we're continously developing it. The reason why we started this project was that we wanted something similar to Storm, but without Zookeeper and the need to take the pipeline down to update the topology.

(`是也乎:`

![Motorway](https://camo.githubusercontent.com/3b9e2aae3a17c7c625add24c49b552747cb08a3c/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f763631346a747a30753168396872732f53637265656e73686f74253230323031362d30372d323925323031342e32382e32362e706e673f646c3d31)

类似 Apache Storm/Amazon SQS/Kinesis 的有界面数据流构建平台
)

- [与数据流一起工作: 使用 Twitter API 捕获 tweets](https://www.dataquest.io/blog/streaming-data-python/)
    + twitter

This tutorial tries to teach event driven programming by making use of streaming API offered by twitter.


- [介绍 Python 生成器](https://howchoo.com/g/otcwnwe2ndb/introduction-to-python-generators)
    + generators

In this guide we 'll cover generators in depth . We 'll talk about how and why to use them , the difference between generator functions and regular functions , the yield keyword , and provide plenty of examples.This guide assumes you have a basic knowledge of Python ( especially regular functions).Throughout this guide we are going to work towards solving a problem .

(`是也乎:`

又一篇极简说明好文.
)

- [Python 3.6.0 beta 1 发布!](http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html)
    + python3

Python 3.6.0b1 is the first of four planned beta releases of Python 3.6, the next major release of Python, and marks the end of the feature development phase for 3.6. There are quite many new features have a look.

(`是也乎:`

对于 `打死不用 Py3 党` 成员而言, 历史模块库的不兼容, 是一个怎么也绕不过去的门槛.
)

- [Channels 进入正式 Django 项目通道](https://www.djangoproject.com/weblog/2016/sep/09/channels-adopted-official-django-project/)
    + django

The Django team is pleased to announce that the Channels project is now officially part of the Django project, under our new Official Projects program. Channels is the effort to bring WebSockets, long-poll HTTP, and other non-request-response protocol and business logic handling to Django, as part of our ongoing effort to establish what makes a useful web framework in 2016.



- [在 Django 中测试日期](http://eatsomecode.com/testing-dates-django)
    + testing

Django makes unit & functional testing easy (especially with WebTest). Tests on routing, permissions, database updates and emails are all straightforward to implement but how do you test dates & time? You might for example want to test regular email notifications.

- [介绍 Django Channels](http://masnun.com/2016/09/11/a-brief-introduction-to-django-channels.html)
    + django

The idea behind Channels is quite simple. To understand the concept, let’s first walk through an example scenario, let’s see how Channels would process a request.

- [节目 74 - Python 在 Zalando](http://podcastinit.podbean.com/e/episode-74-python-at-zalando/)
    + podcast, community

Open source has proven its value in many ways over the years. In many companies that value is purely in terms of consuming available projects and platforms. In this episode Zalando describes their recent move to creating and releasing a number of their internal projects as open source and how that has benefited their business. We also discussed how they are leveraging Python and a couple of the libraries that they have published.

(`是也乎:`

Zalando 是又一个 Python 重度依赖公司,分享他们的折腾历史.
)

- [得书: 赢取 "Python 201"](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/ejwcvjsXyW4/)
    + books

To win your copy of this book, all you need to do is come up with a comment below highlighting the reason “why you would like to win this book”. Try your luck guys :)

- [机器学习一年记](https://medium.com/learning-new-stuff/machine-learning-in-a-year-cdb0b0ebd29c#.pwjo17255)
    + machine learning

Only people with masters degrees or Ph.D’s work with machine learning professionally isn't true. The truth is you don’t need much maths to get started with machine learning, and you don’t need a degree to use it professionally. Here is Per Harald Borgen journey. Yes he is using Python.

(`是也乎:`

传说机器学习得至少硕士以上学历的人才玩的了,
作者证明了,这不是真的...嗯哼.
)

- [在 JavaScript, Python, 和 Go 中对同一个算法的 12 个实现版本](https://medium.com/@kentquirk/12-versions-of-the-same-algorithm-in-javascript-python-and-go-2a1e2d4add84#.t4epl27k3)
    + languages

I recently had to write nearly the same code in Go and Python on the same day, and I realized I had written it many times before in different languages. But it does point up some interesting language differences. This article explores many different ways to write the same code

(`是也乎:`

简单的说, 算法优化到最后, Python 一行搞店, 其它语言, 嗯哼...
)

## 活动
~ Upcoming Conference / User Group Meet

- [PyCon JP 2016](https://pycon.jp/2016/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [OSCON Europe 2016](http://conferences.oreilly.com/oscon/open-source-eu-2016)
- [PyCon DE 2016](http://pycon.de/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)


## 项目
~ 包/模块/库/片段...


- [NakedTensor](https://github.com/jostmey/NakedTensor)
    - 53 Stars, 3 Fork

Bare bottom 简单实例,
基于 TensorFlow 的机器学习

- [tensorflow_image_classifier](https://github.com/llSourcell/tensorflow_image_classifier)
    - 15 Stars, 4 Fork

TensorFlow 图像分类实例 by @Sirajology on Youtube

- [packyou](https://github.com/llazzaro/packyou)
    - 10 Stars, 0 Fork

从 github 更加简单的导入 Python 模块

(`是也乎:`

向 npm/brew 致敬, 只是, packyou 只能先从 pip 中安装;
而且文档不可用, 只能先等待了,
进一步的 老爹 ,可能不同意.
)

- [lambdazen](https://github.com/brthornbury/lambdazen)
    - 7 Stars, 2 Fork

基于实时代码重写的, 更好的 Python lambda 形式语法

(`是也乎:`

用 `a = (x) > x` 替代 `a = lambda x: x` 

总之那谁曰过, Lisp 之后所有语言,都是对 Lisp 的不完全模仿,
i greeeeeee...
)

- [python-twitter-toolbox](https://github.com/hhromic/python-twitter-toolbox)
    - 6 Stars, 1 Fork

Twitter Toolbox for Python.

- [pymail](https://github.com/tstringer/pymail)
    - 3 Stars, 1 Fork

:mailbox_with_mail: Command-line email client

- [export-kobo](https://github.com/pettarin/export-kobo)
    - 3 Stars, 0 Fork

可从 Kobo SQLite 文件中导出注释和高亮行

## DAMA
~ 无责任推荐

- [GitHub Octoverse 2016](https://octoverse.github.com/)

Github 年度报吿, 值得关注的是: [rdpeng (Roger D. Peng)](https://github.com/rdpeng)
这位华人,个人仓库有两个在 top10 名单中!
你猜为毛!?

- [karpathy/arxiv-sanity-preserver: Web interface for browsing, search and filtering recent arxiv submissions](https://github.com/karpathy/arxiv-sanity-preserver)

使用 Python 开发的基于 NLP 技术, 自动化提取论文仓库核心内容搜索服务,以便大家快速定位对自己有用的论文!

~ 介绍视频: [introduction video](https://youtu.be/S2GY3gh6qC8)
作者很神奇...


# 是也乎

- 160916 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160915 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


