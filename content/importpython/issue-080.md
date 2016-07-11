Title: 蠎加载 80
Slug: importpython-80
Date: 2016-07-08 23:23
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 80](http://importpython.com/newsletter/no/80/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Spectrum 使用 - Python 构建的独立日志服务. Review on Import Python Blog.](http://goo.gl/EsgvEK)
    + importpython

Spectrum is to logging what sqlite3 is to databases. It’s a standalone logging server plus log viewer with filtering capabilities. It scales to multiple logging streams with endpoint being a file residing on filesystem, REST API endpoint, Syslog, UDPStream, WebSocketStream. This blogpost shows how to use spectrum and wraps up with pros and cons. Have a read.

(`是也乎:`

能接入当前所有主要日志后端的独立服务,
内置过滤器.
)


- [Django 开发者快讯 - Djangoweekly.com Launched.](http://djangoweekly.com/newsletter/)
    + django

Djangoweekly.com is a weekly newsletter dedicated to Django. The first issue is already out. Have a look.

- [Python 为毛慢 ?](http://blog.kevmod.com/2016/07/why-is-python-slow/)
    + benchmark

In case you missed it, Marius recently wrote a post on the Pyston blog about our baseline JIT tier. Our baseline JIT sits between our interpreter tier and our LLVM JIT tier, providing better speed than the interpreter tier but lower startup overhead than the LLVM tier. There's been some discussion over on Hacker News, and the discussion turned to a commonly mentioned question: if LuaJIT can have a fast interpreter, why can't we use their ideas and make Python fast? This is related to a number of other questions, such as "why can't Python be as fast as JavaScript or Lua", or "why don't you just run Python on a preexisting VM such as the JVM or the CLR". Since these questions are pretty common I thought I'd try to write a blog post about it.

(`是也乎:`

又一篇从 JIT 环境角度来分析的文章.
问题是, 明白了, 并不能改变 Py 平台的现状,,,
)

- [在 Py 中构建自己的 Shell](https://hackercollider.com/articles/2016/07/05/create-your-own-shell-in-python-part-1/)
    + core python

I’m curious to know how a shell (like bash, csh, etc.) works internally. So, I implemented one called yosh (Your Own SHell) in Python to answer my own curiosity. The concept I explain in this article can be applied to other languages as well. Note from curator - After graduating from college I interviewed with Yahoo and they had asked me to create one during interview. It's a good exercise for any computer science student/professional.

(`是也乎:`

yosh 作者的心灵自述, 推荐所有计算机专业的学生都来造一把好轮子.
)

- [MongoFrames - 轻快而不招摇的 MongoDB ODM](http://mongoframes.com/getting-started)
    + mongodb

A five minute walk-through of MongoFrames' key features and how to start using them.



- [科学 Python 介绍– Pandas](http://www.datadependence.com/2016/05/scientific-python-pandas/)
    + pandas

Pandas allows us to deal with data in a way that us humans can understand it; with labelled columns and indexes. It allows us to effortlessly import data from files such as csvs, allows us to quickly apply complex transformations and filters to our data and much more. It’s absolutely brilliant. This is the third post in this series on scientific Python and take a look at Pandas. Don’t forget to check out the other posts if you haven’t yet!

(`是也乎:`

数据科学领域 Python 是一重镇, Pandas 则是其中无法忽视的不将
)

- [教程: 用 Docker Swarm 复用部署 Py3 应用](http://www.giantflyingsaucer.com/blog/?p=5923)
    + docker

Today, I want to show you how to use Docker Swarm and then deploy a simple Python Falcon REST app. Although I won’t be using dockerrun or the serverless capabilities I think you might be surprised how easy it is to deploy (replicated) Python applications (actually any sort of application: Java, Go, etc.) with Docker Swarm.

(`是也乎:`

一个具体的 Falcon REST 应用, 通过 Docker 如何快速部署运行,
其实相同的操作可以用以部署 JAVA/Go/... 等等任何语言应用系统
)

- [Allen Downey - 让 贝叶斯 统计更加简单 - PyCon 2016](https://www.youtube.com/watch?v=TpgiFIGXcT4)
    + statistics

An introduction to Bayesian statistics using Python. Bayesian statistics are usually presented mathematically, but many of the ideas are easier to understand computationally. People who know Python can get started quickly and use Bayesian analysis to solve real problems. This tutorial is based on material and case studies from Think Bayes (O’Reilly Media).

- [Say What ?](https://github.com/joshnewlan/say_what)
    + api

This script listens to meetings I'm supposed to be paying attention to and pings me on hipchat when my name is mentioned. It sends me a transcript of what was said in the minute before my name was mentioned and some time after. It also plays an audio file out loud 15 seconds after my name was mentioned which is a recording of me saying, "Sorry, I didn't realize my mic was on mute there." Uses IBM's Speech to Text Watson API for the audio-to-text.

(`是也乎:`

基于 IBM Watson 的接口,完成的 hipchat 插件,
可以监听所有关于自己的语音事件. 
)

- [Pendulum - Python datetimes made easy](http://pendulum.eustace.io/)

Handle datetimes, timedeltas and timezones in a more natural fashion. Pendulum provides a cleaner and more easy to use API while still relying on the standard library. So it's still datetime but better.

(`是也乎:`

又一个人性化的时间/日期处理模块
)

- [EuroPython 2016: 最后一天可以获得定款门票了](http://blog.europython.eu/post/147035184592)
    + pycon

We will be switching to the on-desk rates for tickets tomorrow, so today is your last chance to get tickets at the regular rate, which is about 30% less than the on-desk rate.

- [The Python/Django 社区超赞! ?](http://blog.djangogirls.org/post/146887124043)
    + community

Experience with the Djangogirls community. 


## 活动
~ Upcoming Conference / User Group Meet

- [Edmonton Python User Group](http://edmontonpy.com/)
- [PyGotham 2016](https://2016.pygotham.org/)
- [EuroPython 2016](http://ep2016.europython.eu/)
- [PyOhio 2016](http://pyohio.org/)
- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [PyCon APAC 2016](https://www.pycon.kr/2016apac/)
- [EuroScipy 2016](https://www.euroscipy.org/2016)
- [Kiwi PyCon](http://kiwi.pycon.org/)



## 项目
~ 包/模块/库/片段...

- [tv](https://github.com/daleroberts/tv)
    - 26 Stars, 0 Fork

Quickly view (satellite) imagery directly in your terminal

(`是也乎:`

又一个 why not 的作品

![tv](https://github.com/daleroberts/tv/raw/master/docs/anim.gif)
)

- [Face-Extractor](https://github.com/JeeveshN/Face-Extractor)
    - 10 Stars, 0 Fork

从任意图片中提取面孔的工具

(`是也乎:`

![Extractor](https://github.com/JeeveshN/Face-Extractor/raw/master/extras/1.png?raw=True)

)

- [yosh](https://github.com/supasate/yosh)
    - 10 Stars, 1 Fork

yosh - Your Own Shell in Python. Repository of the article shared in Worthy Read section.

- [TensorFlow101](https://github.com/nihit/TensorFlow101)
    - 8 Stars, 1 Fork

介绍 TensorFlow. 
作者在 Stanford 学习 cs224d 过程中的总结.

- [CalvinBall](https://github.com/thekindlyone/calvinball_pythonanywhere)
    - 5 Stars, 0 Fork

calvin and hobbes 专用搜索引擎,
给文字, 找到对应的漫画.

- [django-docker-cloud-template](https://github.com/bfirsh/django-docker-cloud-template)
    - 2 Stars, 0 Fork

This is a template for Django applications that can be run with Docker Compose locally and Docker Cloud in production.

(`是也乎:`

又一个 Docker 部署模板, 针对 Django 的.
)

# 是也乎

- 160711 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160708 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


