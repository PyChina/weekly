Title: 蠎加载 36
Slug: importpython-36
Date: 2015-06-19 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 36](http://importpython.com/newsletter/no/36/)


## 该读
~ 文章, Blog, 教程...

- [TIL there is a way to package whole Python virtualenv in a zip file, it's called PEX and it's been used by Twitter since 2011](http://importpython.com/blog/post/conversation-liza-avramenko-founder-checkio-empire-code-games-python-programmers)

pex contains the Python packaging and distribution libraries originally available through the twitter commons but since split out into a separate project. The most notable components of pex are the .pex (Python EXecutable) format and the associated pex tool which provide a general purpose Python environment virtualization solution similar in spirit to virtualenv. PEX files have been used by Twitter to deploy Python applications to production since 2011. 


- [LOST Actors' Basic Analysis - IPython Notebook](http://reinout.vanrees.org/weblog/2015/06/16/djangorecipe-gunicorn.html)

I got to thinking: how have all of the actors fared in their post-LOST careers? I scraped all of this data from IMDB, following this process. 

- [Integrating mod_wsgi-express as a Django admin command.](http://nothingbutsnark.svbtle.com/python-3-support-on-pypi)
	+ mod_wsgi
Integrating mod_wsgi-express into the Django site itself so that it can be executed as a Django management command. By integrating mod_wsgi-express in this way it can directly interrogate the Django settings module for your Django project to obtain the information it wants. 
- [virtualenvwrapper.django 0.4.1
](http://podcastinit.podbean.com/e/episode-10-brian-granger-and-fernando-perez-of-the-ipython-project-1434193715/)
	+ django
virtualenvwrapper.django is a template plugin for virtualenvwrapper to create new Django projects automatically. When used with mkproject, it installs Django into the new virtualenv then runs django-admin.py to create a new project skeleton. 
- [Djangocon: Using Python to load-test web apps - Yulia Zozulya](http://podcastinit.podbean.com/e/episode-11-naomi-ceder-lynn-root-and-tracy-osborn-on-diversity-in-the-python-community/)
    + testing
Using python for your load testing is handy. You use the same language that you use for development. You can more easily write small functions to help you. 


- [IPython Tips and Tricks](http://www.meetup.com/seattle-python-data-science/events/223183575/)
    + ipython
IPython is an advanced interactive python shell. It is a powerful tool which has many more features. However, here I would like to share some of the cool tricks of IPython. 


- [PyCharm 4.5.3 RC发布](https://github.com/jorisvandenbossche/2015-PyDataParis/)
    + pycharm
今天，我们发布了4.5.3 PyCharm RC漏洞修复更新。发行说明中列出了从以前的PyCharm4.5.2更新所有修补程序。其中最引人注目的是：对一些Django支持的修复，主要涉及新manage.py
Today we’ve published the PyCharm 4.5.3 RC bug-fix update. The Release notes lists all fixes from the previous PyCharm 4.5.2 update. The most notable among them are: a number of fixes for Django support, mostly related to the new manage.py Continue reading 

- [Django线路图](http://people.duke.edu/~ccc14/sta-663/index.html)
    + django
通过对3000Django开发者的调查和在Django开发者邮件列表讨论，Django团队公布了特性计划列表（根据需要变化）。
Following over 3,000 responses to the Django Developers Community Survey and a long discussion on the django-developers mailing list, the Django team has adopted the following release schedule (subject to change as needed). 

- [Echo, 一个集成路由的微型框架，1.0版本已发布](https://www.airpair.com/python/posts/using-python-and-qgis-for-geospatial-visualization)
    + webframwork
我们很高兴地宣布EchoV1.0.0已经发布。自从Echo诞生以来，我们已经经历了多次迭代，接受来自世界各地的人们的反馈，解决了Issue并接收pull-request超过100个。
We are pleased to announce the first production release of Echo v1.0.0. Since Echo’s inception, we have gone through several iterations, embraced feedback from people around the world and closed over 100 issues and pull-requests. 


- [扩展Django - 80亿页面浏览量| Disqus:官方博客]()
    + django
As we’re approaching 8 billion page views per month and 45k requests per second, we’ve learned a couple things about delivering comments to a lot of different people. Disqus is very well known for using Django for almost all of our web traffic, and that continues to be a thing today. 


### 工作

-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)
急招 N 名有服务端开发经验的 **gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...

- [telebot]()
- 95 Stars, 16 Fork
Telegram机器人，可使用GoogleAppEngine快速安装
Telegram Bot starter kit. Very easy to install with Google App Engine.

- [2015-06-22-s2i2-git]()
- 35 Stars, 8 Fork
This is a project for s2i2 teaching git. This was a sample repo from Daniel and Tommy to show the students the wonder of git. Really, github should be paying us.

- [shadertoy-render]()
- 27 Stars, 0 Fork
Render a ShaderToy script directly to a video file.

- [engarde]()
- 22 Stars, 1 Fork
A library for defensive data analysis.

- [pcbre]()
- 21 Stars, 3 Fork
An integrated printed circuit board reverse engineering toolkit

- [Toontown-Level-Editor]() - 16 Stars, 8 Fork
Working version of Disney's Toontown Level Editor, which is found in Panda3D 1.6.2.

- [vial-http]() - 12 Stars, 0 Fork
Simple http rest tool for vim

- [django-admin-tools]() - 9 Stars, 1 Fork
Extends the Django Admin to include a extensible dashboard and navigation menu

- [es-graphite-shim]() - 8 Stars, 3 Fork
An ElasticSearch / Graphite shim which translates graphite requests into ElasticSearch data queries for a given mapping

- [rgp]() - 8 Stars, 0 Fork
RGP provides a simple directed graph database built on top of Redis and utilizes a set of Python classes as its interface. Both vertices and edges can have data and can be queried when traversing the graph.

- [pbl]() - 7 Stars, 0 Fork
a python library for building playlists

- [ebook-isbn]() - 7 Stars, 0 Fork
An eBook tool to extract ISBN or Metadata form eBook and rename them by using ISBN database and Metadata

- [TakeStock]() - 6 Stars, 0 Fork
This project provides support for the emailing of Stock reports. It scrapes the NASDAQ site for the earnings date and gets stock prices using a web service.

- [codeofconductlink]() - 6 Stars, 5 Fork
A software community tracker to highlight projects with a Code of Conduct and underrepresented authors and contributors.

- [django-dynamic-preferences]() - 4 Stars, 0 Fork
Dynamic global and instance settings for your django project

- [RedditTwitterPoster]() - 2 Stars, 0 Fork
A python-based script that takes link posts from a subreddit and posts them as embedded media on Twitter

- [jwords]() - 1 Stars, 0 Fork
A small program written in python to help you memorize words.

- [markiavelli]() - 1 Stars, 0 Fork
A Reddit bot that posts to /r/politics using text generated with Markov chains.

# 是也乎

- 150624 老高/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150619 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
