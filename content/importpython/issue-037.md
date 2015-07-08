Title: 蠎加载 37
Slug: importpython-37
Date: 2015-06-26 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 37](http://importpython.com/newsletter/no/37/)


## 该读
~ 文章, Blog, 教程...

- [Twitter 从 2011 起就用 PEX 方式将整个儿 Python virtualenv 打到一个 zip 中](https://pex.readthedocs.org/en/latest/index.html)

pex 包括 Python 的包管理和分发,
原先是 Twitter 内部公用服务,已经开源为独立项目.

核心组件是和 .pex(Python EXecutable) 相关的 PEX 工具.
提供了类似 virtualenv 的通用虚拟环境.

Twitter 已规模使用了4年!

(`是也乎:`

电影: [WTF is PEX? - YouTube](https://www.youtube.com/watch?v=NmpnGhRwsu0)

嗯哼,就是利用了 Python 内置的 zip 无缝解压能力,
将一切随时用 PEX 折腾到可命名/可执行/可升级/可部署的 .zip 文档中.

)

- [LOST 演员基本分析 - IPython Notebook](http://nbviewer.ipython.org/github/pmbaumgartner/LOST/blob/master/WE%20HAVE%20TO%20GO%20BACK.ipynb)
    - ipynb

不禁在想 LOST 演员们的事业发展,现在如何?!
于是基于 IMDB 数据分析了一下下


- [mod_wsgi-express 集成为 Django 管理命令](http://blog.dscpl.com.au/2015/04/integrating-modwsgi-express-as-django.html)
	+ mod_wsgi

通过这种集成命令,
可以直接查询 Django 的模块配置.

- [virtualenvwrapper.django 0.4.1](http://feeds.doughellmann.com/~r/DougHellmann/~3/NTInBNBM7so/virtualenvwrapper-django-0-4-1.html)
	+ django

virtualenvwrapper.django 
作为模板插件,配合 virtualenvwrapper
可以高速完成 virtualenv 的环境部署


- [Djangocon: 对 web 应用进行负载测试 - Yulia Zozulya](http://reinout.vanrees.org/weblog/2015/06/02/07-load-test.html)
    + testing

其实用 Python 来构建负载测试也很容易的.


- [IPython 技巧](http://blog.endpoint.com/2015/06/ipython-tips-and-tricks.html)
    + ipython

IPython 是种魔性交互界面.
强大到无法想象...



- [PyCharm 4.5.3 RC 发布](http://feedproxy.google.com/~r/Pycharm/~3/SaURFg9dISo/)
    + pycharm

今天 PyCharm 4.5.3RC发布了漏洞修复更新. 
发行说明中列出了从以前的PyCharm4.5.2更新所有修补程序. 

其中最引人注目的是:对一些Django支持的修复,主要涉及
manage.py 的持续读写.


- [Django线路图](https://www.djangoproject.com/weblog/2015/jun/25/roadmap/)
    + django

通过对3000Django开发者的调查和在Django开发者邮件列表讨论,Django团队公布了特性计划列表(根据需要变化). 


- [Echo, 一个集成路由的微型框架,1.0版本已发布](http://labstack.com/blog/echo-production-ready/)
    + webframwork

Echo 高兴地宣布 V1.0.0 发布. 自从Echo诞生以来,我们已经经历了多次迭代,接受来自世界各地的人们的反馈,解决了Issue并接收pull-request超过100个. 

(`是也乎:`

又一个框架轮子
)

- [扩展Django - 80亿页面浏览量| Disqus:官方博客](http://blog.disqus.com/post/62187806135/scaling-django-to-8-billion-page-views)
    + django

每月请求已近 80亿, 45K/秒.
我们坚持使用 Django.
当然也学到了更多技巧.


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

- [telebot](https://github.com/yukuku/telebot)
    - 95 Stars, 16 Fork

Telegram机器人,可使用GoogleAppEngine快速安装


- [2015-06-22-s2i2-git](https://github.com/chendaniely/2015-06-22-s2i2-git)
    - 35 Stars, 8 Fork

s2i2 的 git 教学项目.
Daniel and Tommy 向学生展示 git 的各种奇迹.

如此酷炫,以至 github 应该付费给我们.


- [shadertoy-render](https://github.com/alexjc/shadertoy-render)
    - 27 Stars, 0 Fork

用 ShaderToy 直接渲染成视频

- [engarde](https://github.com/TomAugspurger/engarde)
    - 22 Stars, 1 Fork

防守数据分析库.


- [pcbre](https://github.com/davidcarne/pcbre)
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

- 1507?? 老高/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150704 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
