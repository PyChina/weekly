Title: 蠎加载 81
Slug: importpython-81
Date: 2016-07-15 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 81](http://importpython.com/newsletter/no/81/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [AWS 无服务微框架 Python 版本预览](https://aws.amazon.com/blogs/developer/preview-the-python-serverless-microframework-for-aws/)
    + aws

Serverless computing is one of the most talked-about subjects among AWS customers. The AWS serverless offerings, AWS Lambda and Amazon API Gateway, make it possible for developers to create and run API applications with built-in, virtually unlimited scalability without managing any servers. Today the AWS Developer Tools team is excited to announce the preview of the Python Serverless Microframework for AWS. You can read Martin Fowler talking about the benefits of Serverless architecture http://martinfowler.com/articles/serverless.html#benefits

(`是也乎:`

Google 推出了 firebase, AWS 当然要加强 Lambda 的概念.
果断给出了更加易用的 `无服务微框架`
)


- [Python 的逆向调试](http://feedproxy.google.com/~r/PyPyStatusBlog/~3/hEARFKZvdTQ/reverse-debugging-for-python.html)
    + pypy

The PyPy team is pleased to give you "RevPDB", a reverse-debugger similar to rr but for Python.

(`是也乎:`

PyPy 团队赛高
)

- [Facebook 笑话机械人的 django 教程](https://codeexperiments.quora.com/Facebook-chat-bot-aka-joke-bot-with-django-tutorial)
    + chatbots

I have decided to try to develop a chat bot which does only one thing. Send a random joke like the below one without an image irrespective of what the user types


- [书评: “探挖两勺 Django: Django 1.8 的最佳实践”](http://blog.endpoint.com/2016/07/book-review-two-scoops-of-django-best.html)
    + book review

The book can be used as a reference of best practices and a cover-to-cover guide to best practices. I’ve done both and found it to be enjoyable, accessible, and educational when read cover-to-cover and a valuable reference when setting up a new Django project or doing general Django development. It covers a huge range of material.

- [再推 Spectrum - 独立日志服务器. Review](http://importpython.com/blog/post/spectrum-standalone-logging-server-python-product-review)

Spectrum is a standalone logging server plus log viewer with filtering capabilities. It scales to multiple logging streams with endpoint being a file residing on filesystem, REST API endpoint, Syslog, UDPStream, WebSocketStream.


- [构建第一个 Django 应用](https://scotch.io/tutorials/build-your-first-python-and-django-application)
    + tutorial

Decent tutorial to get people started with Python and Django.

- [用 Docker 构建异步 Py3 无服务应用](http://www.giantflyingsaucer.com/blog/?p=5968)
    + serverless

I will show you a simple way to build a “serverless” application and test it via Docker. When I refer to “serverless” I’m referring to the idea that the application is a short lived app, does its job, stops – just like AWS Lambda. I will create two applications each in their own project folders: serverless-app and serverless-web The serverless-app piece is the actual “serverless” piece of this, the web app will run as long as we want. I just gave them similar names to make it easier to keep the projects named closely but different enough to know what does what.

(`是也乎:`

AWS 配套软文, 好在入华了, 可用,只是北京节点不一定有.
)

- [djangobot: 通过 Channels 桥接 Slack 和 Django](https://github.com/djangobot/djangobot)
    + bot

Djangobot is a bridge between Slack and a Channels-enabled Django app. Specifically, it is a protocol server that produces and consumes messages for channels-based apps. It is built atop autobahn and twisted.

- [可视化 Python 包间关系](https://kozikow.com/2016/07/10/visualizing-relationships-between-python-packages-2/)
    + pypi

I extracted co-occurence of top 3500 python packages in github repos using the the github data on BigQuery. I implemented the visualization force layout in d3 via the velocity verlet integration. I also clustered the graph using algorithms from python-igraph and updated it to http://graphistry.com/.


(`是也乎:`

Why not 类型小工程,将 github 中能抓到的 3500 个 Py 包的关系绘制了出来!


![graphistry1](https://kozikow.files.wordpress.com/2016/07/graphistry1.png?w=1140)
)

- [用 Py 在 PNG 文件中当众隐藏有效数据](http://blog.brian.jp/python/png/2016/07/07/file-fun-with-pyhon.html)
    + security

How could I store files online, in plain sight, for free. Because who doesn’t like a good ‘ol game of hide and seek. But with files. On the internet. Hide files in plain sight. Allow them to be distributed via free public channels. E.g Twitter, Reddit, imgur. 

(`是也乎:`

公开的图床一样可以走秘密数据;

代码在: [Don't be a punk, punk](https://gist.github.com/briandeheus/9df32136c756227df4bfbff580a1aadd)

居然能不影响 MD5 !
)


## 活动
~ Upcoming Conference / User Group Meet

- [PyGotham 2016](https://2016.pygotham.org/)
- [EuroPython 2016](http://ep2016.europython.eu/)
- [PyOhio 2016](http://pyohio.org/)
- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [PyCon APAC 2016](https://www.pycon.kr/2016apac/)
- [EuroScipy 2016](https://www.euroscipy.org/2016)
- [PyCon MY 2016](http://pycon.my/)



## 项目
~ 包/模块/库/片段...


- [aq](https://github.com/lebinh/aq)
    - 34 Stars, 0 Fork

Query AWS resources with SQL. aq allows you to query your AWS resources (EC2 instances, S3 buckets, etc.) with plain SQL.

(`是也乎:`

用 SQL 来查询 AWS 的自有资源
)

- [csv-sql](https://github.com/alex/csv-sql)
    - 8 Stars, 0 Fork

Query your CSV files with SQL

(`是也乎:`

用 SQL 来查询 CSV 的数据...

嗯嗯嗯,世界上真的有 SQL 依赖人群,的确, 当年只有SQL 是普通人也在用的开发语言了.
)


- [sokChoGo](https://github.com/cjeon/sokChoGo)
    - 26 Stars, 5 Fork

Travel the pokemon world in your comfy bed, with your keyboards, not on your legs.

(`是也乎:`

足不出户用 CLI 来探索口袋世界,而不是脚,

宅御族必须品.
)

- [macOSLAPS](https://github.com/joshua-d-miller/macOSLAPS)
    - 19 Stars, 2 Fork

A python script that will change a local adminsitrator password to a random generated password. Similar behavior to LAPS for Windows


(`是也乎:`

用 LDAP 管理和生成随机口令, 从 win 迁移来,
对 1Password 的本地仿制?
)

- [Pokemon_Go_API](https://github.com/Mila432/Pokemon_Go_API)
    - 13 Stars, 0 Fork

Pokémon GO API in Python

(`是也乎:`

用蠎来抓老鼠 `天经地义`
)

- [stdgif](https://github.com/thcipriani/stdgif)
    - 10 Stars, 0 Fork

Standard output for gifs. Dumps gifs to stdout or creates shell scripts that can be sourced from a .bashrc or other shell initialization file.

(`是也乎:`

又一个 CLI 上的 gif 放映工具
)

- [pstack](https://github.com/wooparadog/pstack)
    - 9 Stars, 1 Fork

Tool to dump python thread and greenlet stacks. pstack is to python as jstack is to java! It's a debug tool to print python threads or greenlet stacks.

(`是也乎:`

将 py 的线程导出给 JAVA 来分析.
借用用其它语言生态链又一实例
)

- [PostMail](https://github.com/Yinzo/PostMail)
    - 6 Stars, 1 Fork

A simple mail server which can let you send a email only sending a POST request

(`是也乎:`

将邮发形式统一为 HTTP 的 POST
)

## DAMA
~ 无责任推荐

# 是也乎

- 160715 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160715 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


