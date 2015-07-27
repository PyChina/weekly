Title: 蠎加载 40
Slug: importpython-40
Date: 2015-07-27 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 40](http://importpython.com/newsletter/no/40/)



## 该读
~ 文章, Blog, 教程...

- [Pycon China](http://cn.pycon.org/en/)
    + pycon
Fourth year of PyCon China. Organized by CPyUG/GDG/TopGeek, PyCon China will be held simultaneously in Shanghai/Beijing/Zhuhai/Suzhou/Hangzhou this year! For our Chinese readers worldwide please checkout the Chinese translation of ImportPython Newsletter here http://weekly.pychina.org/importpython/index.html

- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 14.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04)
    - postgres, django
In this guide, we will demonstrate how to install and configure some components on Ubuntu 14.04 to support and serve Django applications.

- [Examining Malware with Python](https://www.endgame.com/blog/examining-malware-python)
I’ve talked about before, the lack of open and labeled datasets is a huge obstacle to developing machine learning models to solve security problems. Here was an opportunity to work with an already prepared large labeled dataset of malware samples.

- [Introduction to the fast new UnQLite Python Bindings](http://charlesleifer.com/blog/introduction-to-the-fast-new-unqlite-python-bindings/)
    - cpython
UnQLite is a serverless JSON document store built on a fast key/value database. About a year ago, I blogged about some Python bindings I wrote for the embedded NoSQL document store UnQLite. One year later I'm happy to announce that I've rewritten the library using Cython and operations are, in most cases, an order of magnitude faster.

- [Quantitative Research in Python: Using Notebooks](http://feedproxy.google.com/~r/Pycharm/~3/uzryswOBBMw/)
    - pycharm
This is a first in a series of blog posts covering the use of Python for quantitative research. In this post, we take a look at IPython Notebooks: a really handy tool for structuring calculations in a document-like fashion.

- [The uWSGI Swiss Army Knife](https://lincolnloop.com/blog/uwsgi-swiss-army-knife/)
    + wsgi
uWSGI is one of those interesting projects that keeps adding features with every new release without becoming totally bloated, slow, and/or unstable. In this post, we'll look at some of its lesser used features and how you might use them to simplify your Python web service.

- [Learning Seattle's Work Habits from Bicycle Counts](https://jakevdp.github.io/blog/2015/07/23/learning-seattles-work-habits-from-bicycle-counts/)
    + machine learning
Last year I wrote a blog post examining trends in Seattle bicycling and how they relate to weather, daylight, day of the week, and other factors. Here I want to revisit the same data from a different perspective. In other words, where the previous post examined the data using a supervised machine learning approach for data modeling, this post will examine the data using an unsupervised learning approach for data exploration.

- [Guido Van Rossum Live at europython 2015](http://www.reddit.com/r/Python/comments/3e1ppr/guido_van_rossum_live_at_europython_2015/)
    + video
Must watch.

https://www.youtube.com/watch?v=yCg3EMf9EYI


- [Django and Python 3 How to Setup pyenv for Multiple Pythons](http://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/)
    + python3
We need to be doing Django development in Python 3. Unfortunately, we have a lot of projects still in Python 2.7 so switching between the 2 versions can be frustrating. Fortunately pyenv takes the guess work out of switching, and makes it super simple.

- [Building a Movie Recommendation Service with Apache Spark & Flask - Part 1 | Codementor](https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1)
    + machine learning
This Apache Spark tutorial will guide you step-by-step into how to use the MovieLens dataset to build a movie recommender using collaborative filtering with Spark’s Alternating Least Saqures implementation. It is organised in two parts. The first one is about getting and parsing movies and ratings data into Spark RDDs. The second is about building and using the recommender and persisting it for later use in our on-line recommender system.

- [Understanding Django Middlewares](http://agiliq.com/blog/2015/07/understanding-django-middlewares/)
    + django
As always Agiliq brings detailed good articles on Django. Here is one on middleware. I assume you have read official Django docs on middleware. I will elaborate on things mentioned in the documentation but I assume you are familiar with basics of middleware.

- [Mesos & Django (and Aurora and CircleCI too) — Michael Twomey](http://www.twoistoomany.com/blog/2015/7/16/mesos-django-and-aurora-and-circleci-too)
    + django
I gave a talk at Python Ireland about using Mesos, Django, Aurora and CircleCI together for deployment bliss. These are some of my notes.

- [A couple quick tips](http://b-list.org/weblog/2015/jul/22/couple-quick-tips/)
    + django
As noted the other day, I’ve spent the last little while working to freshen up various bits of open-source code I maintain, in order to make sure all of them have at least one recent release. Along the way I’ve picked up a few little tips and tricks. Today I’d like to dive into two in particular that are relevant for people who write and distribute Django applications. 


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

- [rockstar](https://github.com/avinassh/rockstar)
    - 1558 Stars, 96 Fork
Makes you a Rockstar C++ Programmer in 2 minutes. Well this has nothing to do with Python and is quite funny though. Have a read.

- [tushe](https://github.com/ericls/tushe)
    - 36 Stars, 9 Fork
A web based image hosting, viewing and sharing service build on top of Flask.

- [DQN-chainer](https://github.com/ugo-nama-kun/DQN-chainer)
    - 36 Stars, 3 Fork
This software is a python implementation of Deep Q-Networks for playing ATARI games with Chainer package.

- [pyside2](https://github.com/PySide/pyside2)
    - 23 Stars, 0 Fork
pyside repo on github

- [SpeechBot](https://github.com/Martyn96/SpeechBot)
    - 15 Stars, 1 Fork
A Text-to-Speech Python Telegram bot

- [django-sabot](https://github.com/rosarior/django-sabot)
    - 15 Stars, 0 Fork
Provoke predictable errors in your Django projects.

- [Elemental](https://github.com/ElementalCode/Elemental)
    - 8 Stars, 1 Fork
A drag and drop block-based coding environment for front-end web technologies.

- [PyPhantom](https://github.com/ryanskidmore/PyPhantom)
    - 8 Stars, 1 Fork
Basic API for PhantomJS

- [textcom](https://github.com/TachyonNZ/textcom)
    - 5 Stars, 2 Fork
A Text-Based Roguelike in Python, based on XCOM: Enemy Unknown

- [reddit_authorship](https://github.com/aehaynes/reddit_authorship)
    - 4 Stars, 4 Fork
An analysis to detect authors with multiple accounts in comments from the /r/Bitcoin subreddit. See andrehaynes.me/portfolio for the full report 

## DAMA 无责任推荐

# 是也乎

- 1507?? [Zoom.Quiet](http://zoomquiet.io) 完成快译
- 150727 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
