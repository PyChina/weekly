Title: 蠎加载 25
Slug: importpython-25
Date: 2015-03-20 21:12
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 26](http://importpython.com/newsletter/no/26/)

## 该读
~ 文章, Blog, 教程...


- [Protecting a Python codebase](http://bits.citrusbyte.com/protecting-a-python-codebase/)
    + core python
The very nature of Python makes the task of protecting the source code complicated. As an interpreted language, the source code must be available in some form in order to execute it. During this article, I’ll write down the steps I’ve followed while trying to find a fit solution to the problem of protecting a Python based codebase

- [Feature Spotlight: Python remote development with PyCharm](http://feedproxy.google.com/~r/Pycharm/~3/ObAFl6CPM8w/)
    + pycharm
Happy Friday everyone, In today’s blog post I’m going to cover some basic principles and features in PyCharm that make Python remote development easy as pie. To demonstrate them I’ll use a very simple flask web application.

- [High Performance Django Infrastructure Preview](http://feedproxy.google.com/~r/LincolnLoop/~3/iorgEgsweiQ/)
    + django
We've been users of Salt for configuration management for almost three years. Over the last few weeks I've been extracting our internal Salt states into a reusable and extensible system I like to call infrastructure-in-a-box. It encompasses all the lessons we've learned over the years with our different clients and allows anyone to setup a complete Python website (load balancer, web accelerator, cache, database, task queue, etc.) in about 15 minutes.

- [Introducing mod_wsgi-express.](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html)
    + apache
The first major difference with mod_wsgi-express over the traditional path of installing mod_wsgi is that you can install it like any other Python package. In other words you can 'pip install' it directly from PyPi. You can even list it in a 'requirements.txt' file for 'pip.

- [Meet Scout, a Search Server Powered by SQLite](http://charlesleifer.com/blog/meet-scout-a-search-server-powered-by-sqlite/)
    + sqlite
,
text search
In my continuing adventures with SQLite, I had the idea of writing a RESTful search server utilizing SQLite's full-text search extension. You might think of it as a poor man's ElasticSearch – a very, very poor man.

- [PyCharm 4.0.6 RC is available](http://feedproxy.google.com/~r/Pycharm/~3/zqHWETobnx8/)
    + pycharm
Today we’ve published the PyCharm 4.0.6 RC bug-fix update. This build has a few fixes that can be found in the release notes: a fix for the Django ORM inspection problem, a fix for the ManyToManyField resolve bug and more

- [The PSF Fellow recognition program](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/wC01hCZ8GtY/for-shes-jolly-good-psf-fellow.html)
    + PSF
The PSF Fellow recognition program aims to explicitly acknowledge notable efforts of Python community members in contributing to, managing and growing the global Python community. To nominate a candidate for recognition as a PSF Fellow, the following steps should be completed by the nominating Fellow.

- [Getting started with Django tastypie](http://agiliq.com/blog/2015/03/getting-started-with-django-tastypie/)
    + rest
Django tastypie is a library to write RESTful apis in Django. Here is a tutorial to get you started.

- [Django 1.8 released](https://www.djangoproject.com/weblog/2015/apr/01/release-18-final/)
    + django
After more than a year of development, the Django team is happy to announce the release of Django 1.8 according to schedule. This version has been designated as a long-term support (LTS) release, which means that security and data loss fixes will be applied for at least the next three years.

- [How Celery Chord Synchronization Works](http://blog.untrod.com/2015/03/how-celery-chord-synchronization-works.html)
    + celery
Celery is a powerful tool for managing asynchronous tasks in Python. The basic model is your synchronous Python code pushes a task (in the form of a serialized message) into a message queue (the Celery "broker", which can be a variety of technologies - Redis, RabbitMQ, Memcached, or even a database), and worker processes pull tasks off the queue and execute them.

- [Webcast: Building Scalable Web Apps with Python and Google Cloud Platform](http://www.oreilly.com/pub/e/3388)
    + webcast
In this presentation, Google engineer and O'Reilly author Dan Sanderson shows how to set up a Python cloud development environment, build a scalable web app using various Google services and tools, and deploy and manage a live application.

- [Webcast: Practical Network Automation Using Python and Ansible](http://www.oreilly.com/pub/e/3386)
    + webcast
In this webcast, you will learn about using Python and Ansible to automate various networking tasks including configuration templating, gathering network device information, and executing bulk configuration changes.

- [Getting started with redis-py](http://agiliq.com/blog/2015/03/getting-started-with-redis-py/)
    + python,redis
This post explains how to interface with Redis from Python and how to use different Redis commands from Python using redis-py.

- [Jython 2.7 release candidate 1 available!](http://fwierzbicki.blogspot.com/2015/03/jython-27-release-candidate-1-available.html)
    + jython
On behalf of the Jython development team, I'm pleased to announce that the first release candidate of Jython 2.7 is available! We're getting very close to a real release finally. 




## 项目
~ 包/模块/库/片段...

- [reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
    - 947 Stars, 36 Fork
A fast, offline reverse geocoder in Python

- [InsideReCaptcha](https://github.com/ReCaptchaReverser/InsideReCaptcha)
    - 187 Stars, 10 Fork
Reverse-engineering the new “captchaless” ReCaptcha system...

- [spectra](https://github.com/jsvine/spectra)
    - 142 Stars, 2 Fork
Easy color scales and color conversion for Python.

-[CleanCut](https://github.com/CleanCut/green)
    - 141 Stars, 10 Fork
Green is a clean, colorful test runner for Python unit tests. Compare it to nose or trial.

- [palladium](https://github.com/ottogroup/palladium)
    - 86 Stars, 2 Fork
Framework for setting up predictive analytics services

- [bulby](https://github.com/sontek/bulby)
    - 75 Stars, 6 Fork
Python library for managing the phillips hue lightbulb

- [cron-metrics](https://github.com/manugarri/cron-metrics)
    - 57 Stars, 2 Fork
Implementation of a monitoring system of interval cron tasks in Python

- [gist](https://github.com/jdowner/gist)
    - 29 Stars, 1 Fork
Gist command line interface

- [fontawesome-to-android](https://github.com/deepankarb/fontawesome-to-android)
    - 11 Stars, 0 Fork
A python script to convert font awesome icons to png and place them in android density buckets

- [ReactiPy](https://github.com/logandhead/ReactiPy)
    - 11 Stars, 0 Fork
Compile React Components Server Side using Python

- [Email-Autoresponder](https://github.com/SlightlyCyborg/Email-Autoresponder)
    - 8 Stars, 1 Fork
I made an AI auto responder to respond to repetitive questions that appear in my mailbox. Since I don't use email very often, I had to ask some of my friends what they would have an AI do if it could read their emails.

- [rietveld](https://github.com/rietveld-codereview/rietveld) 
    - 6 Stars, 2 Fork
Code Review, hosted on Google App Engine

(`是也乎:`
Guido 老爹遗作!
)

- [jsonschema-test](https://github.com/kylef/jsonschema-test)
    - 5 Stars, 0 Fork
A tool for writing and running tests against a given JSON Schema 



## 工作

- [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
四月急招 N 名有服务端开发经验的 **gopher**!


- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

## DAMA
(`大妈私人无责任播报`)

~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 15040? [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150403 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
