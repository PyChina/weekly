Title: 蠎加载 78
Slug: importpython-78
Date: 2016-06-24 22:22
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 78](http://importpython.com/newsletter/no/78/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Instagram 的 Python 服务效能提高](https://engineering.instagram.com/web-service-efficiency-at-instagram-with-python-4976d078e366#.fezx5eyeu)
    + performance

Instagram currently features the world’s largest deployment of the Django web framework, which is written entirely in Python. We initially chose to use Python because of its reputation for simplicity and practicality, which aligns well with our philosophy of “do the simple thing first.” But simplicity can come with a tradeoff: efficiency. Instagram has doubled in size over the last two years and recently crossed 500 million users

(`是也乎:`

Instagram 已经是世界上最大的 Django 功能集群,
用户应该也是最多 5亿了..
)

- [Python wats](https://github.com/cosmologicon/pywat)
    + code snippet

A "wat" is what I call a snippet of code that demonstrates a counterintuitive edge case of a programming language. (The name comes from this excellent talk by Gary Bernhardt.) If you're not familiar with the language, you might conclude that it's poorly designed when you see a wat. Often, more context about the language design will make the wat seem reasonable, or at least justified.


(`是也乎:`

通过一段反直觉的代码, 来展示 Py 的伟大
)

- [Coconut - 简单,优雅的 Pythonic 函式编程](http://coconut-lang.org/)

Coconut is a simple, elegant, Pythonic functional programming language that compiles to Python. Since all valid Python is valid Coconut, joining the over 30,000 people already using Coconut will only extend and enhance what you're already capable of in Python.

(`是也乎:`

自从世界从了 冯氏 体系后,
函式派从来就没有停止过也怀念.
又一个在 Py 身体上进行的 Lisp 还魂术...
)

- [在 Statsd 和 Consul 支持下从  Docker 中运行 Py3 的 REST 应用](http://www.giantflyingsaucer.com/blog/?p=5892)
    + REST

Today, I’m going to go over setting up a very simple way to spin up a Python Falcon REST service that reports to Statsd as well as registering as a service with Consul along with setting up health checks. I’ve borrowed some ideas/code from several places and changed as needed.

(`是也乎:`

基于 Falcon 的 Docker 运行时镜像的建立实战
)


- [Pigar](https://github.com/Damnever/pigar)

梦幻般的工具,
可以用来生成你的 Python 项目, 以及其它.

(`是也乎:`

终于出现 pip 的二级工具了,
配合 pyenv 应该真正笑醒...
等等! 还是国人作品, 点赞!
)


- [Django 1.10 beta 1 发布](https://www.djangoproject.com/weblog/2016/jun/21/django-110-beta-1-released/)
    + django, release

As part of the Django 1.10 release process, today we've released Django 1.10 beta 1, a preview/testing package that represents the second stage in the 1.10 release cycle and an opportunity for you to try out the changes coming in Django 1.10.

- [错过了 pycon, 最应该看什么来补 ? - Reddit Discussion](http://www.reddit.com/r/Python/comments/4oh4vr/i_missed_pycon_what_is_your_favorite_talk_that/)
    + video

Discussion on Reddit on Pycon talk recommendations.

- [最合算的高可用 Django 部署 - Roland van Laar](http://reinout.vanrees.org/weblog/2016/06/22/high-availability-django-cheap.html)
    + django

Roland build an educational website that needed to be high available on a tight budget. Nice write up on how to achieve it.

- [BeginnersGuide/NonProgrammers - Python Wiki](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
    + resource

If you've never programmed before, the tutorials on this page are recommended for you; they don't assume that you have previous experience. If you have programming experience, also check out the BeginnersGuide/Programmers page. This section is hosted on the Python website and is well curated and maintained.

- [80 Python 课程的 策划名单](http://bafflednerd.com/learn-python-online)
    + resource

Learn Python online – A curated list of courses on Python

- [如何在 Ubuntu 16.04 的 Apache 用 mod_wsgi 发布 Django 服务? - DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)
    + installation

In this guide, we will demonstrate how to install and configure Django in a Python virtual environment. We'll then set up Apache in front of our application so that it can handle client requests directly before passing requests that require application logic to the Django app. We will do this using the mod_wsgi Apache module that can communicate with Django over the WSGI interface specification.

(`是也乎:`

虽然 OC 的文档一向非常的有爱,
但是, mod_wsgi 上古神器,还有必要用嘛!?
)

- [行者访问 Katharine Jarmul](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/qoNKxbAWJXQ/an-interview-with-pythonista-katharine-jarmul)
    + interview

This interview with Pythonista Katharine Jarmul focuses on data work. A couple of events provide context. Katharine is presenting a talk titled "How Machine Learning Changed Sentiment Analysis, or I Hate You, Computer ????" at this year's Sentiment Analysis Symposium, July 12, 2016 in New York, following which she's offering a class, Learn Big Data Wrangling with Python, July 13-14, also in New York.


(`是也乎:`

是时候通过 Py 的大数据分析来自行评估家庭爱情残余量了...
)

- [Python 中的简单类型检验](https://gist.github.com/luke14free/144239699da237588291497dd547654e)
    + code snippet

Code snippet to check types. 


## 活动
~ Upcoming Conference / User Group Meet

- [PyDelhi Meetup](http://www.meetup.com/pydelhi/)
- [Inland Empire Pyladies](http://www.meetup.com/iepyladies/)
- [Monthly Python user group in Sheffield, United](http://groups.google.com/group/python-sheffield)
- [PyStaDa](http://pystada.github.io/)
- [Fox Valley Python User Group](http://foxpython.tumblr.com/)
- [Python Meeting Düsseldorf](http://pyddf.de/)
- [Sydney Python User Group](http://sypy.org/)



## 项目
~ 包/模块/库/片段...


- [coursera-dl-all](https://github.com/Chillee/coursera-dl-all)
    + 111 Stars, 15 Fork

Extend the Coursera Downloader by downloading quizzes and assignments (and hopefully forum posts soon!). Uses coursera-dl in the process.

- [socli](https://github.com/gautamkrishnar/socli)
    - 86 Stars, 9 Fork

是的我们爱 桟溢, 也爱 CLI,所以结合了两者是必须的


- [reductio](https://github.com/xoreaxeaxeax/reductio)
    - 80 Stars, 2 Fork

r.a.a. reduces all C programs to identical instruction streams; that is, the instructions executed by the processor become the same for every program. The demonstration uses C and x86, but is not unique to either of these - the concept is easily adapted to most languages and architectures.

(`是也乎:`

又一个用 Py 来对 C 代码进行动手的工具
)

- [TensorflowKR-2016-talk-debugging](https://github.com/wookayin/TensorflowKR-2016-talk-debugging)
    - 55 Stars, 10 Fork

Slides and supplementary codes for my talk 'Debugging Tips on Tensorflow' (2016) https://wookayin.github.io/TensorflowKR-2016-talk-debugging

(`是也乎:`

每次分享后,发布幻灯以及配套的代码最性感了...
)

- [ank](https://github.com/sunary/ank)
    - 18 Stars, 0 Fork

Python 的微服务, 
针对 队列/流媒体/REST-API, 以及计划任务

- [Effective-Python-Penetration-Testing](https://github.com/PacktPublishing/Effective-Python-Penetration-Testing)
    - 12 Stars, 3 Fork

This is the code repository for [Effective Python Penetration Testing], published by Packt Publishing. It contains all the required files to run the code. This book is ideal for those who are comfortable with Python or a similar language and need no help with basic programming concepts but want to understand the basics of penetration testing and the problems pentesters face.

(`是也乎:`

渗透测试图书的配套代码库.
)


- [emojibot](https://github.com/owocki/emojibot)
    - 10 Stars, 0 Fork

This is a bot that adds custom emojis your slack team; *inline in Slack*. No more putzing around in your web browser.


- [gh-streak](https://github.com/csu/gh-streak)
    - 5 Stars, 1 Fork

A Python library, CLI, and API for fetching GitHub contribution streaks.



- [PAN-Card-OCR](https://github.com/dilippuri/PAN-Card-OCR)
    - 4 Stars, 0 Fork

专门从  PAN Card 图片获得信息的模块,
对印度开发者应该非常有用

## DAMA 无责任推荐

- [一个 Python requirements 工具 -- pigar - V2EX](http://www.v2ex.com/t/225127)

就是这期的 pigar 国产的 ;-)

- [Pycon US 2016 视频和演讲幻灯](https://speakerdeck.com/pycon2016)

必须首先复习: [Guido van Rossum - Python Language - PyCon 2016](https://www.youtube.com/watch?v=YgtL4S7Hrwo) 明确 Py2 何时正式放弃...



# 是也乎

- 160701 [Zoom.Quiet](http://zoomquiet.io) 重新部署 pyenv 本地环境发布
- 160629 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160624 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


