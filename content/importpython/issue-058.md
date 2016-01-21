Title: 蠎加载 58
Slug: importpython-58
Date: 2016-01-22 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 58](http://importpython.com/newsletter/no/58/)

## 该读
~ 文章, Blog, 教程...



- [ImportPython Job Board Update For Our Readers](http://www.importpython.com/jobboard/)
    + job market
It's been approx six months since the launch of the free Import Python Job Board. We have received three emails from job posters thanking us for helping them find developers. We couldn't be more happy. There are 25 job posting and on average 3 applicants per posting. If you are hiring in any part of the world. Do post your opening on the 100% free job board. We will even feature it in the newsletter for free.

- [Discussion - What do you believe WSGI 2.0 should and should not do? Should we do it at all ?](https://mail.python.org/pipermail/web-sig/2016-January/005357.html)
    + web framework
It’s a new year, and that means it’s time for another attempt to get WSGI 2.0 off the ground. Many of you may remember that we attempted to do this last year with Rob Collins leading the charge, but unfortunately personal commitments made it impossible for Rob to keep pushing that attempt forward. Since then, the need for a revision of WSGI has become even more apparent. Casual discussion on the web has indicated that application developers are uncomfortable with the limitations of WSGI. These limitations are providing an incentive for both application developers and server developers to take an end-run around WSGI in an attempt to get a framework that is more suitable for the modern web. A great example of the result of WSGI’s deficiencies is Andrew Godwin’s channels work for Django, which represents a paradigm shift in application development that takes it far away from what WSGI is today.

- [Testing Web Apps with Python, Selenium, Django. Interview with Harry Percival.](http://pythontesting.net/podcast/harry-percival-pt009/)
    + podcast
If you develop and/or test web applications, especially django, you will probably enjoy this episode. Harry Percival is none other then the author of "The GOAT book" :)

- [[Tutorial]: Deploying Python 3, Django, PostgreSQL to AWS Elastic Beanstalk | Jameson Ricks](https://jamesonricks.com/?p=159)
    + django
, aws
We all know Amazon Web Services frequently changes how things are done. Most of the tutorials I found online for deploying Django to Elastic Beanstalk with PostgreSQL were outdated, using Python 2.7 and Django 1.7. There’s a few things that are different when deploying to Python 3 that I had to figure out.

- [Understanding CPython by Patching – part 1](https://orenmn.wordpress.com/2016/01/16/understanding-cpython-by-patching-part-4/)
    + core python
During the last year or so, I have made some attempts to become familiar with CPython (henceforth, I would refer to the CPython implementation of the awesome python 3 simply as CPython). This is a four series article worth reading.

- [Introducing Getting Started with PyCharm video tutorials](http://feedproxy.google.com/~r/Pycharm/~3/jF-S83DB134/)
    + pycharm
Many of our users have been asking us to create a set of video tutorials covering PyCharm functionality and features. Today we’re happy to announce the very first Getting Started with PyCharm series of nine short video tutorials.

- [Pragmatic Python GIL in 3 Minutes](https://blog.ssundarraj.me/the-python-gil-in-2-minutes-80d74d56a1a0)
    + gil
Multithreading is a source of confusion for many developers both novice and experienced. The Python GIL adds another layer of confusion. It’s not explained in a succinct and understandable manner in many places. The fact is that there is very little to be confused about. I’ll attempt to explain it, or at least the parts that impact day to day applications, within two minutes.

- [SQL query inspector for Django](https://github.com/dobarkod/django-queryinspect#readme)
    + django
Query Inspector is a Django application providing middleware for inspecting and reporting SQL queries executed for each web request.

- [Resources for learning functional programming in Python?](http://www.reddit.com/r/Python/comments/4144js/resources_for_learning_functional_programming_in/)
    + core python
Discussion on reddit on resources for learning FP in Python.

- [Deploying a Django App with No Downtime](https://medium.com/@healthchecks/deploying-a-django-app-with-no-downtime-f4e02738ab06#.1fcfu4907)
    + django
When healthchecks.io started to receive more than 1 request per second, it became clear I could not just go on carelessly restarting web servers after code deploys. For a monitoring service, it would be bad form to miss even a few HTTP requests. And, going forward, if the server gets busier, the problem only becomes bigger.

- [Now accepting Financial Aid applications](http://pycon.blogspot.com/2016/01/now-accepting-financial-aid-applications.html)
    + pycon
If you are looking to visit / have a ticket and deserve to get aid, do apply. 


## 新书
~ New Books

- [Real-World Machine Learning](http://importpython.com/books/525/real-world-machine-learning/)
In a world where big data is the norm and near-real-time decisions are crucial, machine learning (ML) is a critical component of the data workflow. Machine learning systems can quickly crunch massive amounts of information to offer insights and make decisions in a way that matches or even surpasses human cognitive abilities. These systems use sophisticated computational and statistical tools to build models that can recognize and visualize patterns, predict outcomes, forecast values, and make recommendations.

## 项目
~ 包/模块/库/片段...



- [TrumpScript](https://github.com/samshadwell/TrumpScript)
    - 1033 Stars, 48 Fork
Make Python great again. Editor note to non american readers: Please read on Donald trump to get a sense of what this repo is about.

(`是也乎`:

基于唐纳德·特朗普的修辞手法的编程语言 [Coders Assimilate Donald Trump to a Programming Language | Inverse](https://www.inverse.com/article/10448-coders-assimilate-donald-trump-to-a-programming-language)

真爱!

![examplescripttooutput](http://i1.wp.com/media.boingboing.net/wp-content/uploads/2016/01/examplescripttooutput-shows-a-more-complex-bit-of-trumpscript-at-the-top-after-the-first-cat-comm1.png?w=970)

)


- [spaceShooter](https://github.com/prodicus/spaceShooter)
    - 71 Stars, 11 Fork
The classic retro game recreated using Pygame and python

- [pick](https://github.com/wong2/pick)
    - 59 Stars, 3 Fork
a small library to help you create curses based interactive selection list in the terminal

- [tornaREST](https://github.com/nekocode/tornaREST)
    - 44 Stars, 4 Fork
:cyclone: A simple RESTful Web Service build with Tornado.

- [kaggle-right-whale](https://github.com/felixlaumon/kaggle-right-whale)
    - 25 Stars, 5 Fork
2nd place solution to the Kaggle Right Whale challenge

- [reality-of-Dream-of-Red-Mansions](https://github.com/Huangtuzhi/reality-of-Dream-of-Red-Mansions)
    - 20 Stars, 12 Fork
Comparision analysis of words use between 1~80 chapters and 80~120 chapters of ?A Dream of Red Mansions?.

- [PrettyPandas](https://github.com/HHammond/PrettyPandas)
    - 17 Stars, 0 Fork
A Pandas Styler class for making beautiful tables

- [github_reviewer](https://github.com/gabrielhora/github_reviewer)
    - 16 Stars, 1 Fork
Use GitHub Webhooks and Commit Status API to control pull requests reviews

- [fython](https://github.com/nicolasessisbreton/fython)
    - 9 Stars, 0 Fork
Fython is Fortran with a Python syntax

(`是也乎:`

老树新花儿!
)

- [git-money](https://github.com/21hackathon/git-money)
    - 7 Stars, 0 Fork
Git Money lets people make money off their pull requests on GitHub.

- [loadcf](https://github.com/singpenguin/loadcf)
    - 6 Stars, 1 Fork
It is a python config file loader

- [notebook-api](https://github.com/jefersondaniel/notebook-api)
    - 5 Stars, 0 Fork
Rest API for notes, uses Python Flask, Mongo, Behave and Docker-Compose

- [logen-trace](https://github.com/perhapsspy/logen-trace)
    - 5 Stars, 0 Fork
Delivery confirmation for Logen(https://www.ilogen.com)



## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 16012? [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160122 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


