Title: 蠎加载 166
Slug: importpython-166
Date: 2018-03-11 20:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 166](http://importpython.com/newsletter/no/166/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Django 管理手册](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)
    + django, admin

This is a book about doing things with Django admin. It takes the form of about forty questions and common tasks with Django admin we answer.

(`是也乎:`

叕一本有关 Django 的新书了...
旁的不说, Django 制造了很多作者

)



- [又一种创建 REST API 的简易形式 – codeburst](https://www.guru99.com/restful-web-services.html)
    + flask

Learn how to create semantic REST API real quick using Python Flask

(`是也乎:`

叕一个用FLask 来折腾 RESTful 接口的案例,
但是,有专门的 API 生成器了哪

> 181130 suggest by Alex Nordeen

[RESTful Web Services Tutorial with Example](https://www.guru99.com/restful-web-services.html) is is more in-depth and well -> [This is how easy it is to create a REST API – codeburst](https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3)

thanx u Alex ;-)




)

- [非同步 - 在 async/wait 情况下](http://asherman.io/projects/unsync.html)
    + async

Python 3.5 added support for async/await, and Python 3.6 sort of wrapped up support for it (adding things like supporting await in list comprehensions). Unfortunately I’ve been having trouble adapting to Python’s version of async/await especially coming from C#’s implementation in TPL. The two big friction points I’ve had are: Difficult to “fire and forget” async calls (need to specifically run the event loop) Can’t do blocking calls to asyncio.Future.result() (it throws an exception)



- [用 Selenium 阵列 和 Docker Swarm 进行并发 Web 扫描 - TestDriven.io](https://testdriven.io/concurrent-web-scraping-with-selenium-grid-and-docker-swarm#.Wp1R571zzpc.reddit)
    + testing

In this post we’ll look at how to run a Python and Selenium-based web scraper in parallel with Selenium Grid and Docker. We’ll also look at how to quickly scale Selenium Grid on Digital Ocean using Docker Swarm to increase efficiency of the scraper. Finally, we’ll create a bash script that automates the spinning up and tearing down of resources on Digital Ocean.

(`是也乎:`

Digital Ocean 在各种领域都很积极, 不过还是 Heroku 更加好用..

)


- [介绍 timeboard, python 的商业日历包](https://medium.com/@mmamaev2/introducing-timeboard-a-python-business-calendar-package-a2335898c697)   
    + project


timeboard is a python library that creates schedules of work periods and performs calendar calculations over them. You can build standard business day calendars as well as a variety of other schedules, simple or complex.

- [Python cx_Oracle 6.2 发布到 PyPI](https://blogs.oracle.com/opal/python-cx_oracle-62-is-on-pypi)
    + oracle, database

cx_Oracle 6.2, the extremely popular Oracle Database interface for Python, is now Production on PyPI. cx_Oracle is an open source package that covers the Python Database API specification with many additions to support Oracle advanced features.


(`是也乎:`

那什么, 好吧...有关 Oracle 真心没什么可以说的...

)


- [介绍 Nerodia – Watir 项目](http://watir.com/introducing-nerodia/)
    + testing

Watir is a tool designed for browser test automation first. It is built from the perspective of developers and testers who want reliable browser automation that can scale with a browser automation project. Nerodia is designed from the same perspective, matching Watir’s approaches to browser handling, synchronizing actions, and providing flexible locators for working with DOM elements.


(`是也乎:`

![Watir_logo](https://raw.githubusercontent.com/watir/watir_logo/master/Logo/Watir_logo.png)


叕一个基于 Selenium 的测试框架....

)

- [BitStream - 管理二进制数据](http://boisgera.github.io/bitstream/)
    + binary


Bitstream is a Python library to manage binary data as bitstreams.

(`是也乎:`

使用 [MkDocs](http://www.mkdocs.org/) 
创建的文档网站....当年没有这么漂亮的 样式呢...

)


- [用 Python 构建 Elevation Profile Generator ~ Geodose](http://www.geodose.com/2018/03/create-elevation-profile-generator-python.html)  
    + geo

Elevation profile is a two dimensional cross section along a line or path. It is very helpful to visualize the elevation change along a line or path. In this post I will discuss how to create an elevation profile graph between two points using Open Elevation API.

(`是也乎:`

电梯的确是个麻烦事儿...
)

- [Pandas 列 Apply 方法 分析](https://aaronlelevier.github.io/2018-03-04-analyzing-the-pandas-series-apply-method/)
    + pandas

I saw the Pandas.apply method and started thinking about this pattern and if it’d be useful to implement on other objects. Here’s a brief blog about the pattern. The general pattern outside of framework or language specifics is, Apply an anonymous function to a value or an iterable

(`是也乎:`

Apply 简直就是 Pandas 的后门

)


- [用 Python 进行数据预处理: How I learned to love parallelized applies with Dask and Numba](https://medium.com/@ernestk.social/how-i-learned-to-love-parallelized-applies-with-python-pandas-dask-and-numba-f06b0b367138)
    + data processing

(`是也乎:`

数据工程第0步, 总是最混乱的
)



## 好物
~ 包/模块/库/片段...

- [memcachedump](https://github.com/JLospinoso/memcachedump)
    - 46 Stars, 8 Fork

Use your Shodan API Key to dump all the contents of exposed memcached servers.

(`是也乎:`

感觉很久没有 memcached 相关的工具了..

)

-[container-breakouts](https://github.com/singe/container-breakouts)
    - 36 Stars, 4 Fork

Testing/collecting some container breakouts.

- [Tensorflow-DatasetAPI](https://github.com/taki0112/Tensorflow-DatasetAPI)
    - 32 Stars, 3 Fork

Simple Tensorflow DatasetAPI Tutorial for reading image.

(`是也乎:`

叕一则 Tensorflow 教程

)

- [hue](https://github.com/UltimateHackers/hue)
    - 9 Stars, 1 Fork

Hue will help you to print awesomely in terminals.

(`是也乎:`

![hue](https://camo.githubusercontent.com/558fee80ef40c8459bd36fd28e567d728adadd50/68747470733a2f2f692e696d6775722e636f6d2f636f41437379512e706e67)

叕一则 CLI 调色工具...


)


-[TextClassification](https://github.com/lytforgood/TextClassification)
    - 8 Stars, 0 Fork

deep learning in text classification(keras).

(`是也乎:`

Keras 越来越嗯哼了

)


- [reddit_ml_challenge](https://github.com/kootenpv/reddit_ml_challenge)
    - 6 Stars, 1 Fork

Reddit Machine Learning: Tagging Challenge.

-[django-lint2](https://github.com/t-hiroyoshi/django-lint2)
    - 4 Stars, 0 Fork

LinkedIn Recon Tool.

(`是也乎:`

400行的一则 LinkedIn 扩展实例?

)


-[django-lint2](https://github.com/t-hiroyoshi/django-lint2)
    - 4 Stars, 0 Fork

Lint2 is a linter work on Django.

(`是也乎:`

Py3 only 
)


- [protostub: A tool for generating Mypy type stubs from a Protocol Buffer definition.](https://github.com/arachnys/protostub)
    - 0 Stars, 0 Fork

A tool for generating Mypy type stubs from a Protocol Buffer definition. 


(`是也乎:`

很久没见 Protocol Buffer 相关的嗯哼了

)





### (￣▽￣)

- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...
- [Neilpang/acme.sh: A pure Unix shell script implementing ACME client protocol](https://github.com/Neilpang/acme.sh)
    + https

> 国人作品, 解决 https 部署时的证书生成问题



*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180311 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180311 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


