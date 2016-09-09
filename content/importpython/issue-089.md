Title: 蠎加载 89
Slug: importpython-89
Date: 2016-09-08 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 89](http://importpython.com/newsletter/no/89/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [通过 Python 使用 Markov Chains 来构建 Slack bot 模拟同事.](http://hirelofty.com/blog/how-build-slack-bot-mimics-your-colleague/)
    + bot

Imagine in your company slack team there's this person (we'll call him Jeff). Everything that Jeff says is patently Jeff. Maybe you've even coined a term amongst your group: a Jeffism. What if you could program a Slack bot that randomly generates messages that were undeniably Jeff?

(`是也乎:`

西乔精确的预测了相同的 bot 在微信中诞生后导致人类灭亡的故事
)

- [Python 中是否有三元计算符?](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/-w79X0YhCYo/ternary-statements-in-python)
    + core python

Learn how to use Python’s ternary operator to create powerful “one-liners” and enhance logical constructions of your arguments.

(`是也乎:`

必须有, 不过,何必?
)

- [500行以内 | 用 Python 完成一个 Python 的解释器](http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

Byterun is a Python interpreter implemented in Python. Through my work on Byterun, I was surprised and delighted to discover that the fundamental structure of the Python interpreter fits easily into the 500-line size restriction. This chapter will walk through the structure of the interpreter and give you enough context to explore it further. The goal is not to explain everything there is to know about interpreters—like so many interesting areas of programming and computer science, you could devote years to developing a deep understanding of the topic.

(`是也乎:`

这几乎就是 PyPy 的诞生机制...

PS: `500行内` 已经成为 github 中包含最多脑洞的可用项目了...
)


- [第 73 集 - Alex Martelli](http://podcastinit.podbean.com/e/episode-73-alex-martelli/)

Note from curator - I met Alex at Pycon Singapore / Py APAC as it was called then, I found him inspirational. We sat down and talked about Java developer's obsession with design patterns. It was a blast. I wonder if he would remember. Here is a podcast where he is interviewed. Alex Martelli has dedicated a large part of his career to teaching others how to work with software. He has the highest number of Python questions answered on Stack Overflow, he has written and co-written a number of books on Python, and presented innumerable times at conferences in multiple countries. We spoke to him about how he got started in software, his work with Google, and the trends in development and design patterns that are shaping modern software engineering.


(`是也乎:`

Alex 是 Stack Overflow 中有关 Python 问题回答最多的人.
采访中分享了很多在 google 以及软件工程上的体验
)

- [Machinalis: OCR 和 Django 以及 Tesseract](http://www.machinalis.com/blog/ocr-with-django/)
    + django, OCR

A Django site that integrates with Tesseract to provide an OCR service.

- [使用消息框架](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)
    + django

Tutorial on how to use messages framework.

- [分版本统计 pip 的下载总量](https://gist.github.com/juanpabloaj/dffc6900f80abcfe8ce121a39cffa743)
    + benchmark

Wow 3.x isn't far behind. Couple of years may be. I see more and more companies using 3.x series for newer projects.

(`是也乎:`

基本上差了一个量级... Py3 和 Py2

![juanpabloaj](https://camo.githubusercontent.com/18f68ea99ec363874853ba87ed1fe29b36d66c88/687474703a2f2f692e696d6775722e636f6d2f6c456c5754755a2e706e67)

)

- [连续分析新闻: 介绍 GeoViews](https://www.continuum.io/blog/developer-blog/introducing-geoviews)

GeoViews is a new Python library that makes it easy to explore and visualize geographical, meteorological, oceanographic, weather, climate, and other real-world data. GeoViews was developed by Continuum Analytics, in collaboration with the Met Office. GeoViews is completely open source, available under a BSD license freely for both commercial and non-commercial use, and can be obtained as described at the Github site.

(`是也乎:`

BSD 许可的 GeoViews 是一个完备的地理数据分析/展示相关的库.
可以轻巧的生成可互动的地理相关可视化图谱!

![cell8](https://www.continuum.io/sites/all/themes/continuum/posts/geoviews/imgs/cell8.png)

以上这图就是一行代码:

    url = 'https://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'
gv.WMTS(url, layer='VIIRS_CityLights_2012', crs=crs.PlateCarree(), extents=(0, -60, 360, 80))

)


- [Mike Driscoll: 当周PyDev: Reinout van Rees](http://www.blog.pythonlibrary.org/2016/09/05/pydev-of-the-week-reinout-van-rees/)
    + interview

This week we welcome Reinout van Rees (@reinoutvanrees) as our PyDev of the Week! Reinout is the creator / maintainer of zest.releaser. He has a nice website that includes a Python blog that you might want to check out. I would also recommend checking his Github page to see what projects he’s a part of. Note - We have been including Reinout van Rees blogposts for long time now in importpython. Here you can know more about the person behind the blog.

(`是也乎:`

又一位 van ;-)
zest.releaser 的作者, 带大家如何分析一位程序猿的网络数据
)


- [Chris Moffitt: 从列表和字典构建 Pandas DataFrames](http://pbpython.com/pandas-list-dict.html)
    + pandas

Whenever I am doing analysis with pandas my first goal is to get data into a panda’s DataFrame using one of the many available options. For the vast majority of instances, I use `read_excel` , `read_csv` , or `read_sql` . There are multiple methods you can use to take a standard python datastructure and create a panda’s DataFrame. For the purposes of these examples, I’m going to create a DataFrame with 3 months of sales information for 3 fictitious companies.

(`是也乎:`

享受 Pandas 的便利,第一步就是将数据倒入为 DataFrames ...
)

- [18 个最常见的 Python 列表问题](https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python)

Go find how many you can answer

(`是也乎:`

发布的网站倒是值得关注: `datacamp.com`
在线自学 R/Py 进行数据科学研究...
)

- [Python 201 正式发布!](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/1CWjaB3pGlk/)
    + book review

Mike Driscoll's second book Python 201: Intermediate Python is out.

(`是也乎:`

![Python201_cover20160330_sm](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/04/Python201_cover20160330_sm-237x300.jpg)

![mousecovertitlejpg_sm2](http://www.blog.pythonlibrary.org/wp-content/uploads/2014/02/mousecovertitlejpg_sm2-237x300.jpg)

嗯哼,封面很有爱...
)

- [PayPal 中使用 Anaconda 进行 Python Packaging](https://www.paypal-engineering.com/2016/09/07/python-packaging-at-paypal)
    + packaging

At PayPal, we write and deploy our fair share of Python, and we wanted to devote a couple minutes to our story and give credit where credit is due. For conclusion seekers, without doubt or further ado: Continuum Analytics’ Anaconda Python distribution has made our lives so much easier. For small- and medium-sized teams, no matter the deployment scale, Anaconda has big implications. But let’s talk about how we got here.

(`是也乎:`

历史原因...
![snake_esc_sm](http://sedimental.org/uploads/snake_esc_sm.png)

)

- [csssdbpy](https://github.com/deslum/cssdbpy)

cssdbpy is a simple SSDB client written on Cython. Faster standart SSDB client.

- [Semaphore Community: Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)
    + docker

Get an understanding of how to dockerize your Django application, using the Gunicorn web server, capable of serving thousands of requests in a minute.

(`是也乎:`

dockerize ~ 又一个新词儿
)

- [Python (Windows)中快又脏 的驱动器](http://jugad2.blogspot.com/2016/09/quick-and-dirty-drive-detector-in.html)
    + code snippet

While using Python's os.path module in a project, I got the idea of using it to do a quick-and-dirty check for what drives exist on a Windows system. Actually, not really the physical drives, but the drive letters, that may in reality be mapped any of the following: physical hard disk drives or logical partitions of them, CD or DVD drives, USB drives, or network-mapped drives.



- [有用的 python 视频德语教程系列.](https://www.youtube.com/watch?v=dyJdLalc7TA&amp;list=PLNmsVeXQZj7q0ao69AIogD94oBgp3E9Zsc)
    + video

Note I haven't personally gone through the video series, the no of upvotes and views looks pretty decent. Please make your own judgement. 

## 活动
~ Upcoming Conference / User Group Meet

- [PyCon JP 2016](https://pycon.jp/2016/)
- [PyCon ZA 2016](https://za.pycon.org/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [OSCON Europe 2016](http://conferences.oreilly.com/oscon/open-source-eu-2016)
- [PyCon DE 2016](http://pycon.de/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)


## 项目
~ 包/模块/库/片段...



- [keras_snli](https://github.com/Smerity/keras_snli)
    - 77 Stars, 9 Fork

基于 Stanford Natural Language Inference (SNLI) 
使用神经网络进行计算 和/或


- [commandlinefu_slackbot](https://github.com/jh69/commandlinefu_slackbot)
    - 9 Stars, 0 Fork

又一个 slack 机器人, 自动从 commandlinefu.com 获得结果


- [word2vec-slim](https://github.com/eyaler/word2vec-slim)
    - 8 Stars, 0 Fork

word2vec Google News model slimmed down to 260k English words

- [pyh2o](https://github.com/iceboy-sjtu/pyh2o)
    - 5 Stars, 0 Fork

The pyh2o module provides Python binding for the H2O HTTP server. Currently this is a toy project, PRs are welcome to make it useful. Think of high performance, interaction with asyncio, etc.


## DAMA
~ 无责任推荐


# 是也乎

- 160909 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160908 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


