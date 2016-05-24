Title: 蠎加载 72
Slug: importpython-72
Date: 2016-05-13 22:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 72](http://importpython.com/newsletter/no/72/)
- 欢迎, 来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)

## 该读
~ 文章, Blog, 教程...


- [生成器解析](http://nedbatchelder.com//blog/201605/generator_comprehensions.html)
    + core python

Python has a compact syntax for constructing a list with a loop and a condition, called a list comprehension: 
`my_list = [ f(x) for x in sequence if cond(x) ]` 
. You can also build dictionaries with dictionary comprehensions, and sets with set comprehensions///


- [Asyncio 和 uvloop](http://kracekumar.com/post/144058400775)
    + benchmark

上周看到了 uvloop 的简介, 号称比 Asyncio 快两倍以上,
不服来测! `嗯哼` 基本属实 ;-)

Today, I read an article about uvloop. I am aware of libuv and its behind nodejs. What caught me was “In fact, it is at least 2x faster than any other Python asynchronous framework.”. So I decided to give it a try with aiohttp. The test program was simple websocket code which receives a text message, doubles the content and echoes back. Here is the complete snippet with uvloop. I ran naive benchmark using thor and results favoured uvloop. uvloop was able to handle more connection on 8GB , non SSD Mac OSX . Asyncio was able to hold 154 connections and uvloop 243 connections with any socket errors .

- [Python 成本分析脚本 - AWS EC2 vs AWS Lambda - reddit discussion (self.Python)](https://www.reddit.com/r/Python/comments/4hebys/cost_analysis_for_python_scripts_aws_ec2_vs_aws/)
    + aws

官方号称 Lambda 比 EC2 性价比高...

So I decided AWS Lambda had been on the field enough time to make an analysis by my own. Lambda comes with a few problems like only Python 2.7 (they will fix it in the future I guess), libraries, etc. Also I had read some blogs like Flynn's one. But skipping those problems I wanted to know... What about money ?

- [用 python, pandas, matplotlib 下载/分析/可视化 10年份 last.fm 音乐收听历史   (代码在 github)](http://geoffboeing.com/2016/05/analyzing-lastfm-history/)
    + machine learning

Using Python, pandas, matplotlib, and leaflet, I downloaded my listening history from Last.fm’s API, analyzed and visualized the data, downloaded full artist details from the Musicbrainz API, then geocoded and mapped all the artists I’ve played. All of my code used to do this is available in this GitHub repo, and is easy to re-purpose for exploring your own Last.fm history. All you need is an API key.

(`是也乎:`

以及类似的分析 twitter/facebook/instagram ... SNS 海量数据的根源都是:
人家开放了接口!

)

- [应该学写 Python 装饰器的五大理由](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/3sHnEEZ4psw/5-reasons-you-need-to-learn-to-write-python-decorators)
    + core python

Python decorators are so easy to use. Anyone who knows how to write a Python function can learn to use a decorator. But writing decorators is a whole different skill set. And it’s not trivial; you have to understand. closures, how to work with functions as first-class arguments, variable arguments, argument unpacking, even, some details of how Python loads its source code

(`是也乎:`

bigger and bigger and bigger and bigger and bigger ...
)

- [TPOT: 自动化数据科学平台](http://www.randalolson.com/2016/05/08/tpot-a-python-tool-for-automating-data-science/)
    + 赞助商

In this article, we’re going to go over three aspects of machine learning pipeline design that tend to be tedious but nonetheless important. After that, we’re going to step through a demo for a tool that intelligently automates the process of machine learning pipeline design, so we can spend our time working on the more interesting aspects of data science.

- [如何获得 Python 工作岗位? - Reddit Discussion](https://www.reddit.com/r/Python/comments/4ix01q/how_to_get_a_python_job/)
    + core python

Recently, I've been playing around with Python and found that I really enjoy the language. Now I am wondering how I should go about switching over to a Python job. I am tired of doing front-end web development, and am thinking that I would enjoy concentrating more on the back-end. However, the back-end Python jobs seem to require me being a data scientist. Also, it seems like most Python jobs are in QA automation or DevOps.

(`是也乎:`

汇同 `哪种语言/编辑最好` 为三大月经贴...
其实,很简单...自个儿创造这个岗位!
)


- [Why Python? What's it good for? How is it special?](http://slott-softwarearchitect.blogspot.com/2016/05/why-python-whats-it-good-for-how-is-it.html)
    + core python

Quick read justifying Python.


- [安装 Jupyter Notebook Extensions](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/xy7PfhjGfQI/installing-jupyter-notebook-extensions)
    + video

Jonathan Whitmore demonstrates how to install pivot tables and showcases the features of this extension by examining a dataset of restaurant scores.Pivot tables are one of the many ways to extend the capabilities of the Jupyter Notebook. In this training segment, learn how to quickly and effectively analyze, scope, and visualize data using pivot tables in Jupyter Notebook.

(`是也乎:`

高级特性, 数据透视表的深化折腾...
)


- [davidmiller/pony-mode: Django mode for emacs](https://github.com/davidmiller/pony-mode)
    + emacs

pony-mode - Django mode for emacs

- [用 ctypes 来从 Python 调用 C 代码](http://code.activestate.com/recipes/580660-using-ctypes-to-call-c-code-from-python/)
    + code snippet

This recipe shows basic usage of the ctypes module to call C code from Python code.

- [给 Django 追加用户验证](http://blog.narenarya.in/right-way-django-authentication.html)
    + django

If you are building a new Django website from scratch, the first thing you implement is the User authentication. Here is a simple article showing you how to do it.

- [Django, ELB 健康检查和持续交付 | Octopus Energy Tech blog](http://tech.octopus.energy/2016/05/05/django-elb-health-checks.html)
    + aws

A robust means of deploying web applications with Amazon Web Services is to use an Elastic Load Balancer (ELB) to balance requests between an “Auto Scaling Group” (ASG) of EC2 instances. As well as horizontally scaling, this set-up allows automated canary (aka blue-green) deployments, where new application versions are deployed as a new ASG which replaces the existing EC2 instances with new; a so-called “immutable infrastructure” approach.

- [DjangoPaths - 为毛俺选择 Wagtail?](http://www.djangopaths.com/why-did-i-choose-wagtail/)
    + cms

在折腾了 Django-CMS 和 Mezzanin 之后,
还是理智的入了 Wagtail 教.

My decision to delve into Wagtail only came after I attempted to use Django-CMS and Mezzanine. Their strengths seemed to lie in having a comprehensive ecosystem in place with pluggable e-commerce systems and more.



- [部署 Django + Python 3 + PostgreSQL 到 AWS Elastic Beanstalk - Real Python](https://realpython.com/blog/python/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)
    + aws

The following is a soup to nuts walkthrough of how to set up and deploy a Django application, powered by Python 3, and PostgreSQL to Amazon Web Services (AWS) all while remaining sane.Elastic Beanstalk is a Platform As A Service (PaaS) that streamlines the setup, deployment, and maintenance of your app on Amazon AWS. It’s a managed service, coupling the server (EC2), database (RDS), and your static files (S3). You can quickly deploy and manage your application, which automatically scales as your site grows.


- [Onion IoT 和 Lazar 以及 Zheng](http://podcastinit.podbean.com/e/episode-56-onion-iot-with-lazar-and-zheng)
    + podcast

IoT 物联网时代来了, OpenWRT 是其中最具成功相的平台.

One of the biggest new trends in technology is the Internet of Things and one of the driving forces is the wealth of new sensors and platforms that are being continually introduced. In this episode we spoke with the founder and head engineer of one such platform named Onion. The Omega board is a new hardware platform that runs OpenWRT and lets you configure it using a number of languages, not least of which is Python. 

## 新书
~ New Books

- [Python GUI Programming Cookbook](http://importpython.com/books/517/python-gui-programming-cookbook/)

Over 80 object-oriented recipes to help you create mind-blowing GUIs in Python.


## 活动
~ Upcoming Conference / User Group Meet


- [PyCon US 2016](https://us.pycon.org/2016/)
- [PyData Berlin 2016](http://pydata.org/berlin2016/)
- [SciPy Latin America](http://conf.scipyla.org/scipyla2016/)
- [OSCON Europe 2016](http://conferences.oreilly.com/oscon/open-source-eu-2016)
- [PyGrunn 2016](http://www.pygrunn.org/)


## 项目
~ 包/模块/库/片段...

- [pip-update-requirements](https://github.com/alanhamlett/pip-update-requirements)
    - 150 Stars, 1 Fork

Update the packages in a requirements.txt file.

- [my_first_calculator.py](https://github.com/AceLewis/my_first_calculator.py)
    - 59 Stars, 7 Fork

(`是也乎:`

一个真实的故事引发的...
)


- [AI_Composer](https://github.com/llSourcell/AI_Composer)
    - 26 Stars, 4 Fork

基于机器学习的 AI 作曲

- [hackhttp](https://github.com/BugScanTeam/hackhttp)
    - 23 Stars, 16 Fork

Hackhttp 又一 HTTP library

- [autobazaar](https://github.com/dsmurrell/autobazaar)
    - 9 Stars, 1 Fork

将 OpenBazaar 安装到云空间的工具.
帮时你 5$/月 就能在 Digital Ocean 上开始折腾在线商店,
安装过程 8~11 分钟.


- [md5-encryption](https://github.com/gabe-k/md5-encryption)
    - 7 Stars, 2 Fork

Cryptographically bulletproof encryption algorithm based on the cutting edge MD5 hashing algorithm

(`是也乎`:

![md5-encryption](https://camo.githubusercontent.com/4d426bacf7c5ce573323002c277547bd9116205b/687474703a2f2f692e696d6775722e636f6d2f6447474438645a2e706e67)
)

- [stylistic-word-clouds](https://github.com/minimaxir/stylistic-word-clouds)
    - 6 Stars, 1 Fork

文字云创建脚本

- [gym-doom](https://github.com/openai/gym-doom)
    - 6 Stars, 1 Fork

Doom environment for Gym

- [jupyter-widget-example](https://github.com/jupyter/jupyter-widget-example)
    - 5 Stars, 1 Fork

Example custom Jupyter widget

(`是也乎`:

细思恐极, Jypyter 向着 web GUI 大步突进中,
我们可以期待未来跨平台 app 除了 react 后,又有新选择了?!
)


- [markdown-newsletter](https://github.com/fguillot/markdown-newsletter)
    - 4 Stars, 0 Fork

用 Markdown 发布新闻组


- [SQLAlchemy_RestfulAPI](https://github.com/RaminFP/SQLAlchemy_RestfulAPI)
    - 4 Stars, 0 Fork

Integration SQLAlchemy ORM with Restframework API

## DAMA 无责任推荐

- [Top 10 Python libraries of 2015 — Medium](https://medium.com/@tryolabs/top-10-python-libraries-of-2015-4dc95f0a0ead#.szjzsyff1)

Jupyter ~ 神器之上的神器

retrying ~ 重试小仙器

aiohttp ~ 兼容 Py3 的更加简洁的 HTTP S/C

plumbum ~ 跨平台的 AppleScript

phonenumbers ~ 将 google libphonenumbers 人性化包装的电话检验库

networkx ~ graphviz 之后,更加好用的可视化库

influxdb ~ 时间序数据存储好物

elasticsearch-dsl ~ 嗯哼, Pythonic 操作小语言

keras ~ Theano 上的深度学习界面

gensim ~ NLP 必用品


以及: [20 Python libraries you can’t live without | Python Tips](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)

- [Python 技巧总结 | Taotao's Zone](http://litaotao.github.io/python-materials)
    + 首次自我推荐 Py 原创好文章 ;-)
- [pyenv-mirror](https://github.com/huntzhan/pyenv-mirror)
    + 7 Stars, 0 Fork

快速制作 pyenv 环境镜像的工具

(`是也乎:`

国人作品, 在 CPyUG 列表反馈下, 24小时以内,兼容了 Python 2 ;-)

嗯哼,当然的,没有 M$ 的支持.
)


### 工作

....


# 是也乎

- 160518 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160513 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


