Title: Issue 10 ~ 反重力 
Date: 2012-04-20 
Tags: Weekly,Pycoder,Zh 
Slug: issue-10 
## Hi Pythonistas!

一点系统变更.
有小伙伴反应不喜欢重定向的链接形式.
所以,另外在标题之后提供了直接链接.
以上.
本周的消息依旧给力!

几乎忘记了,
俺们已经提交了众筹的 STICKERS!!
详细情况以后说.


想跟上所有 蠎界 新闻?
 [@pycoders](http://twitter.com/pycoders).

请用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #10) : Antigravity](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=404d979179)


## 新闻与开发动态

- [PyCharm 2.5 Released!](http://blog.jetbrains.com/pycharm/2012/04/pycharm-2-5-released-a-really-environment-friendly-ide/) (blog.jetbrains.com)

Version 2.5 of the PyCharm IDE has been released, now with full support for remote python interpreters and improved virtualenv support. If you like PyCharm or are looking for a full fledged Python IDE this is worth checking out.

- [NumPy on PyPy progress report](http://morepypy.blogspot.ca/2012/04/numpy-on-pypy-progress-report.html) (morepypy.blogspot.ca)
We are really excited about the work that is going on with PyPy, one of the alternative implementations of Python. These guys are making leaps and bounds with getting up to date with python releases(working on python 3k) and increasing speed and support for packages like NumPy. This is the latest report on progress for NumPy support in PyPy, check it out.

- [Circus 0.3 Released](http://blog.ziade.org/2012/04/17/circus-03-released/) (blog.ziade.org)
Circus the Supervisord like program has reached its third release. Circus has a few new features in this point release and all in all this project looks more interesting all the time.

- [Epio Closing Down](https://www.ep.io/blog/epio-closing-down/) (ep.io)
Ep.io is a python web application deployment solution. We have been using ep.io since they started in beta. We are extremely sad to see it close its doors.  Andrew Godwin and Ben Firshman have done an excellent job, and we wish them luck in the future.

- [DjangoCon Europe 2012 Talk Schedule Announced](http://2012.djangocon.eu/blog/schedule-announced/) (2012.djangocon.eu)
This year DJangoCon Europe is in Zurich and the final talk schedule has been announced. Lots of really great topics and speakers on the list. We won't be there but we are definitely looking forward to all the post-conference blog posts and videos that are sure to come.


## 讨论

- [antigravity.py](http://www.reddit.com/r/Python/comments/scw24/til_antigravitypy_exists/) (reddit.com)
Fun little discussion, about how antigravity.py actually exists in the Python stand library source. For those of you unfamiliar with the antigravity.py joke, check out this cartoon from 
[xkcd.com](http://xkcd.com/353/)
![python.png(PNG 图像,518x588 像素)](http://imgs.xkcd.com/comics/python.png)





## 项目
- [datastore](https://github.com/jbenet/datastore) (github.com)
Datastore is a simple API with the aim to enable application development in a datastore-agnostic way, allowing data stores to be swapped seamlessly without changing application code. This project is in its infancy and has some serious potential, we urge anyone with experience in wrapping data stores to help 
[Juan](https://github.com/jbenet)
.

- [PyMuninCli - a Python Library for Accessing Munin Daemons](http://css.dzone.com/articles/first-release-pymunincli) (dzone.com)
PyMuninCli is a command line client library to query your munin servers. This is the perfect library for the Ops guy/gal in all of you.

- [Selfspy](https://github.com/gurgeh/selfspy) (github.com)
Selfspy is a daemon for Unix/X11 that continuously monitors and stores what you are doing on your computer. It is inspired by the 
[Quantified Self](http://en.wikipedia.org/wiki/Quantified_Self)
 movement. It can tell you what you were working on a couple of days go, what your password for a website, it stores everything you type and does it securely for self inspection later. SO awesome.

- [pyspread](http://manns.github.com/pyspread/) (github.com)
So this is really neat, the goal of pyspread is to be the most pythonic spreadsheet. It is written in Python and expects Python expressions in its grid cells. Each cell returns a Python object that can be accessed by other cells which opens up a bunch of possibilities and you also have Python module access, so you can perform operations with NumPy or your favorite library. Watch out Excel!

- [python-cloudsearch](https://github.com/sunlightlabs/python-cloudsearch) (github.com)
Last week Amazon announced and released 
[CloudSearch(beta)](http://aws.amazon.com/cloudsearch/)
 on AWS. If you are looking to get started with Cloud Search before Boto supports it and you don't want to roll your own library support, this is your ticket. Python-cloudsearch provides "A simple, pythonic interface to instances of Amazon's CloudSearch service."

- [The Hitchhiker's Guide to Python!](http://docs.python-guide.org/en/latest/index.html) (docs.python-guide.org)
This opinionated guide exists to provide both novice and expert Python developers a best-practice handbook to the installation, configuration, and usage of Python on a daily basis.


## 文章

- [Using Redis Pub/Sub and IRC for Error Logging with Python](http://charlesleifer.com/blog/using-redis-pub-sub-and-irc-for-error-logging-with-python/) (charlesleifer.com)
This article is about a neat little hack for pushing JSON encoded logging data to a Redis pub/sub channel and then displaying that logging data in IRC using an IRC bot subscribed to this pub/sub channel. If you are working on a application and you are looking to get error notifications and tracebacks by means other than the standard email or reading log files, you may want to check this out.

- [Check Python site-packages for Updates](http://stefan.sofa-rockers.org/2012/04/14/check-python-site-packages-updates/) (stefan.sofa-rockers.org)
Freezing package versions with 
[PIP](http://pypi.python.org/pypi)
 is easy, but keeping everything up to date can be a pain. The script in this blogpost solves this problem. It searches your site-packages for all upgradeable packages and upgrades them with pip. Very awesome.

- [Down the rabbit hole, profiling your Python code](http://reinout.vanrees.org/weblog/2012/04/18/profiling-python.html) (reinout.vanrees.org)
This is a brief summary of some of your options for profiling your Python code as well as some django specific tips of the things you can look for. The author also gave a talk on this subject at the April 2012 Dutch Django Meeting. You can see the slides here

- [Python object creation sequence](http://eli.thegreenplace.net/2012/04/16/python-object-creation-sequence/) (thegreenplace.net)
This is another great article by Eli about the inner workings of Python. In this article he takes you for a deep dive into the Python object creation sequence. This is definitely worth the read.

- [How to Add Push Notifcations to your Website](http://jbalogh.me/2012/04/05/how-to-add-push-notifications-to-your-site/) (jbalogh.me)
This is a very cool and very brief tutorial about how to add push notifications support to your website for sending notifications to Firefox. Very cool.

- [Python FAQ: Equality](http://me.veekun.com/blog/2012/03/24/python-faq-equality/) (me.veekun.com)
This is a section of an ongoing Python FAQ(
[here](http://me.veekun.com/blog/2011/07/22/python-faq/)
). For those who are interested, this is a really good explanation of the difference between 'is' and '==' and when you should use either. Check it out.

- [Using a custom SQLAlchemy Users model with Django](http://tomforb.es/using-a-custom-sqlalchemy-users-model-with-django) (tomforb.es)
This article details, with code examples, how to go about swapping out Django's User model for a custom one created with SQLAlchemy. If you have every had issues with Django's ORM not fitting the bill for you, this is a good place to get started if you are looking for a change.


# 是也乎

- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 4.2 分钟 完成原文 md 格式化.
