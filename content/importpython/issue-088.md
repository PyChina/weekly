Title: 蠎加载 88
Slug: importpython-88
Date: 2016-09-04 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 88](http://importpython.com/newsletter/no/88/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [doctest — 通过文档测试 — PyMOTW 3](http://feeds.doughellmann.com/~r/DougHellmann/~3/MqzfG-MEpHc/)
    + testing

doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find doctest easier to use than unittest because, in its simplest form, there is no API to learn before using it.

(`是也乎:`

这是进入测试最简单的形式, 但是,对于单元测试而言,并没有什么用,
只有设计精良的可测试代码, 对接口类的测试才 hold 的住...
)

- [用 twitter 订阅 getpy ](https://twitter.com/getpy)
    + twitter

If you like this newsletter and you are on twitter you want to follow getpy. Daily get selected ( 4 - 5 ) tweets super relevant to Python.

(`是也乎:`

类似的通过 SNS 进行友好的技术新闻订阅的服务/工具/插件 有很多,
残念的是都在墙外...

)

- [Django 用 Gunicorn 部署以及监察](https://samoylov.tech/2016/08/31/deploying-django-with-gunicorn-and-supervisor/)
    + django

We deploy all Django applications with Gunicorn and Supervisor. I personally prefer Gunicorn to uWSGI because it has better configuration options and more predictable performance. In this article we will be deploying a typical Django application. We won't be using async workers because we're just serving HTML and there are no heavy-lifting task in background.

- [Python 3 模式/技巧/约定](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/)
    + python3

What you see here is an early version of the book.

- [激进的规则: Facebook 中对 Python 文化的改进](https://www.youtube.com/watch?v=nRtp9NgtXiA)
    + video

Today, services built on Python 3.5 using asyncio are widely used at Facebook. But as recently as May of 2014 it was actually impossible to use Python 3 at Facebook. Come learn how we cut the Gordian Knot of dependencies and social aversion to the point where new services are now being written in Python 3 and existing codebases have plans to move to Python 3.5.

(`是也乎:`

PyCon 上的分享,有关 fb 工程师为了 py3 作出的种种折腾...

值得嘛?!....
)

- [Brian Okken: 21: 术语: 测试夹具/皮下测试/端到端测试/系统测试](http://pythontesting.net/podcast/21-terminology-part-1/)

Covered in this episode: Test Fixtures, Subcutaneous Testing, End to End Testing (System Testing) . Curator's note - Of all the podcast out there pythontesting is my fav podcast.

(`是也乎:`

细思恐极, 又一个硬核技术的播客....
)


- [Reuven Lerner: 用列表解析实现 “zip”](http://blog.lerner.co.il/implementing-zip-list-comprehensions/)
    + core python

Simple tutorial with code snippets on zip.


- [自动化 OSINT: 暗网 OSINT 和 Python 第三部分: 可视化](http://www.automatingosint.com/blog/2016/08/dark-web-osint-with-python-part-three-visualization/)
    + security

Welcome back! In this series of blog posts we are wrapping the awesome OnionScan tool and then analyzing the data that falls out of it. If you haven’t read parts one and two in this series then you should go do that first. In this post we are going to analyze our data in a new light by visualizing how hidden services are linked together as well as how hidden services are linked to clearnet sites. One of the awesome things that OnionScan does is look for links between hidden services and clearnet sites and makes these links available to us in the JSON output. Additionally it looks for IP address leaks or references to IP addresses that could be used for deanonymization.

(`是也乎:`

网络安全实战系统分享,以分析 Onion 网络为实例讲解...
)

- [在容器引擎中运行 Django | Python | Google Cloud Platform](https://cloud.google.com/python/django/container-engine)
    + django

How to deploy Django app on Google Cloud

- [Conda: 传说和误解](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

In the four years since its initial release, many words have been spilt introducing conda and espousing its merits, but one thing I have consistently noticed is the number of misconceptions that seem to remain in the (often fervent) discussions surrounding this tool. I hope in this post to do a small part in putting these myths and misconceptions to rest.

(`是也乎:`

Conda 是个传奇的 Python 发行版, 但是,在宣传中形成了很多误解,所以,作者...
)

- [Brett Cannon: 介绍哪部电影](http://www.snarky.ca/introducing-which-film)

It's a website to help you choose what movie you and your family/friends should watch together. Here is the code for the software https://github.com/which-film/which-film.info

(`是也乎:`

开源了一个为家人自动推荐电影的网站代码..
)

- [Montreal Python 用户组: Montréal-Python 59: 召唤讲师](http://montrealpython.org/2016/08/mp59-cfp/)
    + community, conference

September is back and it's for the Montreal Python community to gather again and share exciting new technologies and projects. This month, our friends from Ubisoft are welcoming us into their offices and are going to present to us how they are using Python and how they scaling it at large to powered some of their games.



- [PEP-526 复审准备: 语法变量以及属性注释](https://www.python.org/dev/peps/pep-0526/)
    +  core python

Although type comments work well enough, the fact that they're expressed through comments has some downsides. The majority of these issues can be alleviated by making the syntax a core part of the language. Read the PEP to know more. I think it is a very exciting PEP.

(`是也乎:`

为了语言的运行性能修订语言形式本身, 嗯哼....
)


- [Python 周聊: 胶合在一起的字符串](http://ccst.io/e/strings)

Learn when and why you'd glue strings together using concatenation, interpolation, or other methods. 



## 活动
~ Upcoming Conference / User Group Meet

- [PyCon JP 2016](https://pycon.jp/2016/)
- [PyCon ZA 2016](https://za.pycon.org/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon Ireland 2016](https://python.ie/pycon-2016/)
- [PyHPC 2016](http://www.dlr.de/sc/pyhpc2016)
- [PyData Cologne 2016](http://pydata.org/cologne2016/)




## 项目
~ 包/模块/库/片段...

- [Young](https://github.com/shiyanhui/Young)
    - 187 Stars, 20 Fork

充满了爱心的全功能 Python 制造论坛

(`是也乎:`

![Young](https://camo.githubusercontent.com/c7025c1eee7b46b0cdc7cb163be0122c405ca28a/687474703a2f2f692e696d6775722e636f6d2f6a495273735a382e706e67)

简单的说国产 weibo 的 py 再制品;
基于 mongodb/NodeJS/Elasticsearch/Ejabberd ...嗯哼...

)

- [srez](https://github.com/david-gpu/srez)
    - 133 Stars, 4 Fork

Image super-resolution through deep learning. This project uses deep learning to upscale 16x16 images by a 4x factor. The resulting 64x64 images display sharp features that are plausible based on the dataset that was used to train the neural net.

(`是也乎:`

![srez_sample_output](https://github.com/david-gpu/srez/raw/master/srez_sample_output.png)

基于神经网络的深度学习,完成从 16x16pix 的微型图片中还原出大图片...
)


- [httpstat](https://github.com/reorx/httpstat)
    - 48 Stars, 1 Fork

curl 状态可视化工具

(`是也乎:`

![httpstat](https://github.com/reorx/httpstat/raw/master/screenshot.png)

嗯哼, 在宽屏电脑上, CLI 的能力永远在底估...

)

- [NSC](https://github.com/thunlp/NSC)
    - 36 Stars, 5 Fork

Neural Sentiment Classification

(`是也乎:`

神经网络来分析情感倾向...当然也可以训练为分析理论的左右倾向
)

- [yapi](https://github.com/ahmetkotan/yapi)
    - 10 Stars, 1 Fork

Python Youtube Data API v3

- [imapclient](https://github.com/mjs/imapclient)
    - 10 Stars, 0 Fork

易用的, Pythonic 的完全的 IMAP 客户端库

- [google](https://github.com/robolyst/google)
    - 7 Stars, 0 Fork

登录后可方便的访问 google 后台的各种数据

(`是也乎:`

别的不说, 这种项目名简直了...
)

- [json-algorithm](https://github.com/cheery/json-algorithm)
    - 4 Stars, 0 Fork

Now even your pet rock can parse JSON.

(`是也乎:`

又一个可以玩 JSON 的模块
)

- [django-explain](https://github.com/oeegor/django-explain)
    - 2 Stars, 0 Fork

A helper to get EXPLAIN or EXPLAIN ANALYZE OUTPUT for django queryset.

- [interview-with-python](https://github.com/thundergolfer/interview-with-python)
    - 2 Stars, 0 Fork

The ultimate in python interview preparation and coding practice.

(`是也乎:`

用以面试准备的终极代码集, 嗯哼
)

## DAMA
~ 无责任推荐


# 是也乎

- 160905 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160904 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


