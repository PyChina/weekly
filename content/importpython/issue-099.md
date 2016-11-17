Title: 蠎加载 99
Slug: importpython-99
Date: 2016-11-17 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 99](http://importpython.com/newsletter/no/99/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [因长期运行而使用困难的数据如何激活在 Python](https://medium.com/@jeffknupp/how-python-makes-working-with-data-more-difficult-in-the-long-run-8da7c8e083fe?source=rss------golang-5)
    + core-python

Jeff Knupp author of one of my favorite Python books "Writing Idiomatic Python" talks why Python is terrible for writing long-lived programs dealing with complicated data structures. He then goes to compare it with Go Programming languages where the datatype and data modeling has to be done before hand ( we are talking about complex nested data structures ) . Curator's Note - If you are interested in golang do check out http://importgolang.com a weekly go programming newsletter.

(`是也乎:`

当然的,和 golang 进行了对比,然后...
)

- [Email API from SendGrid](https://goo.gl/5sp3XN)
    + Sponsor

Reliably deliver your emails with a quick and simple API or SMTP integration. Try for Free. Curator's Note - Python and Django integration for sendgrid https://github.com/sendgrid/sendgrid-python and https://github.com/RyanBalfanz/django-sendgrid respectively. You can send 12,000 emails per month free.


(`是也乎:`

一个实用的服务,值得关注的赞助商...
免费的话, 2K/月, 对小应用足够了
)


- [用 Python 开发可扩展应用](https://medium.com/doqmnt/developing-scalable-apps-in-python-e8eb38cc0f07)
    + scalability

David Rodriguez attended the Udacity course: Developing Scalable Apps in Python - App Engine course and took these notes on building scalable apps.

(`是也乎:`

可扩展应用本质上是个架构而不是语言问题...
当然,笔记在 docs.google 中,嗯哼.
)


- [用 Splinter 在 Python 中自动化 Web 测试](https://medium.com/the-python-corner/web-test-automation-in-python-a319a0783187?source=rss------python-5)
    + testing, automation

Splinter is just an abstraction layer on top of Selenium and makes easy to write automation tests for web applications. This is a brief introduction to Splinter.


(`是也乎:`

测试呢,最终还是得统一为 DSL, 当然,如果这个 DSL 和目标程序使用的相同,是最好的了.
)

- [命令行上的 HTTP 响应后端](http://ronaldbradford.com/blog/getting-a-clearer-picture-of-http-response-time-breakdown-via-cli-2016-11-10/)
    + code snippet

httstat https://github.com/reorx/httpstat provides a HTTP response breakdown on command line. This saves you having to open up a browser and look at a visual network response waterfall.

(`是也乎:`

目测是一个现成的无头浏览器的值守?
)


- [命令行上高速 Django 开发技巧](http://davidfozo.com/blog/command-line-tricks-for-ridiculously-fast-django-development/)
    + django

David shares his list of command line alias for Django development. Curator's note - Caution making alias for dot and double dot.


- [keyboard](https://github.com/boppreh/keyboard)
    + opensource project

Take full control of your keyboard with this small Python library. Hook global events, register hotkeys, simulate key presses and much more.

(`是也乎:`

PyHook 之后, 又一键盘控制模块,期望是跨平台兼容的...嗯哼,可怜的 M$ 
)

- [Monkey-patching 又一 Python 实例方案](https://makina-corpus.com/blog/metier/2016/how-to-make-a-python-method)
    + core-python, monkey patching

Dynamically adding or overwriting an instance method in Python is rarely needed, but it's a good excuse to explore interesting aspects of the language that aren't always well known: the descriptor protocol, types.MethodType and partial function applications.


(`是也乎:`

`猴补丁` ~ 方便了程序猿,逼死编译器的好物,令 Py 的加速大业又多一层壁垒
)

- [Django Model Managers](http://samskeller.me/blog/posts/django-model-managers/)
    + django, models

Model Managers (and custom QuerySets) are really useful. If you find yourself doing some complicated queryset logic over and over again, you can put that logic in one place and just refer to it with a simple name.

(`是也乎:`

对于死也只用 SQL 的人来说,不存在哪...
)

- [Django 在 instagram - Carl Meyer](https://www.youtube.com/watch?v=lx5WQjXLlq8)
    + django, video

Instagram operates at a scale unprecedented and is one of the largest users of Python/Django. In this video Carl talks about Django usage @instagram . What modification they made to Django and Why ?, How Django usage evolved over the years at instagram and more.


- [用 PyCharm 通过 SSH 工作在远程机器上](https://medium.com/@erikhallstrm/work-remotely-with-pycharm-tensorflow-and-ssh-c60564be862d)
    - pycharm

This article shows us the remote interpreter feature of PyCharm. Useful for those using PyCharm and want to execute scripts on a remove machine where the environment / data resides.


(`是也乎:`

![pycharm](https://cdn-images-1.medium.com/max/960/1*t4QDc1ilWiCVr_-APAb1qw.png)

嗯哼,这样的界面,哪儿有心思写代码哪...

)


## 好物
~ 包/模块/库/片段...

- [paintingReorganize](https://github.com/ardila/paintingReorganize)
    - 183 Stars, 9 Fork

Use PCA analysis to reorganize the pixels of a painting into a smooth color palette.

(`是也乎:`

![input](https://github.com/ardila/paintingReorganize/raw/master/input.jpg)

变成

![output](https://github.com/ardila/paintingReorganize/raw/master/output.png)

最近折腾图像的模块越来越多了..因为....

)

- [ankeshanand/neural-cryptography-tensorflow](https://github.com/ankeshanand/neural-cryptography-tensorflow)
    - 42 Stars, 6 Fork

Neural Networks that invent their own encryption :key.

(`是也乎:`

又一个 TF 上的神经网络, Python 在所有领域都是一样的节奏,
海量类似模块/框架/功能,然后拼谁坚持到最后,当然,最终还得看 Guido 的脸色收入内建...
)

- [ParhamP/altify](https://github.com/ParhamP/altify)
    - 11 Stars, 23 Fork

Uses deep learning to caption images in an HTML file and fills out its alternative text attributes with the related caption. Altify automizes the task of inserting alternative text attributes for image tags. Altify uses Microsoft Computer Vision API's deep learning algorithms to caption images in an HTML file and returns a new HTML file in which alt attributes are filled out with their corresponding captions.

(`是也乎:`

当然的对中文,呵呵的...

![altify](https://github.com/ParhamP/altify/raw/master/images/gif.gif)

ParhamP 复活了!?
)

- [Deepomatic/dmake](https://github.com/Deepomatic/dmake)
    - 9 Stars, 2 Fork

DMake is a tool to manage micro-service based applications. It allows to easily build, run, test and deploy an entire application or one of its micro-services.

(`是也乎:`

基于 Docker 的微服务!? 表示担心哪...
)

- [check_docker_image](https://github.com/eliasgranderubio/check_docker_image)
    - 7 Stars, 2 Fork

A tool to perform static analysis of known vulnerabilities in docker images/containers

(`是也乎:`

利用 Docker 镜像的非安全性,进行静态检查和修复
)

- [python-dockerflow](https://github.com/mozilla-services/python-dockerflow)
    - 7 Stars, 1 Fork

A Python package to implement tools and helpers for Mozilla Dockerflow

(`是也乎:`

不明觉厉, Mozilla 刷版本数之外,又开始折腾容器云了!?
)

- [slack-to-telegram-bot](https://github.com/kleiinnn/slack-to-telegram-bot)
    - 2 Stars, 0 Fork

Bot for forwarding slack messages to telegram.

(`是也乎:`

telegram 虽然安全,可惜...
)

- [pylogging](https://github.com/ansrivas/pylogging)
    - 2 Stars, 0 Fork

A small wrapper around python logging module which can easily format and write logs to file.

(`是也乎:`

内建日志模块的一个轻包装,协助我们快速格式化
)

- [albertlai/deep-style-transfer](https://github.com/albertlai/deep-style-transfer)
    - 1 Stars, 1 Fork

在 Tensorflow 上 实现快速前馈神经式传输网络

- [sidneijp/webblocker](https://github.com/sidneijp/webblocker)
    - 0 Stars, 0 Fork

A simple website list blocker for time periods based on hosts. 


# 是也乎
~ (￣▽￣) 今天开始,俺将永远是 42 岁了...

- 161117 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161117 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


