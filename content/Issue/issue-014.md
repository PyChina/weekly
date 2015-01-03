Title: Issue 14 ~ Simple is better than complex. 
Date: 2012-05-18 
Tags: Weekly,Pycoder,Zh 
Slug: issue-14 
## Hi Pythonistas!

So we decided to send stickers everyone who tweeted @pycoders last week about stickers. Those of you who are listed here can reply to this email with your name, address and twitter handle. We will get them out to you as soon as possible.

Sorry to those of you who didn't make it, but if you want a sticker send us a self addressed stamped envelope to:

44 Byward Market Square, Suite 210
Ottawa, Ontario Canada 
K1P 7A2

We weren't satisfied with the stickers we recieved and we have sent them to another printer and should be sent out by next week's issue. 

@girasquid
@Fitoria
@StephenYoungDev
@anentropic
@codegrappler
@dnathe4th
@chriswalkr
@tlots
@catchagain
@rafael_ab
@palmerj3
@ServerCobra
@emre_yilmaz
@dstufft
@SarmaTangirala
@themexicat
@fyelles
@RebbitMe
@gmarkall
@jiggyjensen
@martinogden
@ajmendez
@IWillCode
@xemoka
@iwanbk
@regisb
@benregn
@esoltys
@odonnell004
@thomasemge
@RealJohnConnor
@WilliamHerring
@adrop
@kstrauser
@scummlet
@thomasemge
@AshuMehta
@dalanmiller
@R_Macy
@caritos
@fkumro
@WCleve7
@nremond
@mxuribe
@gerlv
@SuperKronos
@MarcelChastain
@jrhunt
@eugeneching
@schnapptack
@speg 
@psnj



Now on to this week's issue, we hope you guys enjoy it.  

想跟上所有 蠎界 新闻?
 [@pycoders](http://twitter.com/pycoders).

请用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #14) : Simple is better than complex.](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=f6f2704baa)


## 新闻与开发动态

- [Jython 2.7 Alpha 1](http://fwierzbicki.blogspot.co.uk/2012/05/jython-27-alpha1-released.html)
Latest version of Jython has been announced, which implements much of the functionality introduced by CPython 2.6 and 2.7. Its an alpha release expect some issues.




## 讨论

- [Tracking Down a Bug](http://www.reddit.com/r/Python/comments/tpixc/ive_spent_the_past_week_tracking_down_a_bug_in/) (reddit.com)
Let's face it we all write bugs, some of even fix a few from time to time. That being said sometimes some bugs are tricky; Often times it's a thankless battle, but there is glory to be had. 


## 项目

- [redis-faina: a query analysis tool for Redis](http://instagram-engineering.tumblr.com/post/23132009381/redis-faina-a-query-analysis-tool-for-redis) (tumblr.com)
What do you do when you sell your company for a Billion dollars to Facebook? You write a query analysis tool for Redis! No really, that's not fair, the guys at Instagram are doing good work and this is a nice tool for sites that do a lot of volume on their redis server and need to better intelligence on their queries. Check it out.

- [grequests](https://github.com/kennethreitz/grequests) (github.com)
GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily. He seems to be on a gevent kick as of late.

- [plumbum](https://github.com/tomerfiliba/plumbum) (github.com)
The motto of the library is "Never write shell scripts again", and thus it attempts to mimic the shell syntax ("shell combinators") where it makes sense, while keeping it all pythonic and cross-platform. Check it out.



## 文章


- [Writing Python Daemons](http://coder.cl/2012/05/writing-python-daemons/) (coder.cl)
This article highlights the use of the daemon module in python, and goes through a tutorial for creating your first daemon process in Python.

- [Python is a Voluntary Language](http://www.johndcook.com/blog/2011/10/26/python-is-a-voluntary-language/) (johndcook.com)
This article starts off describing  how python is a voluntary language, most people choose to develop in it. The interesting part of the article crops up towards the end describing how ruby has been affected by growth driven by web development ( ruby on rails) while python stays it course.

- [Sublime Text 2 tips for Python and Web Developers](http://opensourcehacker.com/2012/05/11/sublime-text-2-tips-for-python-and-web-developers/) (opensourcehacker.com)
If you use Sublime Text 2 as your primary text editor, this article is a great resource of tips for using it effectively with Python and for web development. After you take a look at the article give the reddit discussion a look, there are a lot of tips in there too.

- [A comprehensive guide through Python packaging (a.k.a. setup scripts)](http://foobar.lu/wp/2012/05/13/a-comprehensive-step-through-python-packaging-a-k-a-setup-scripts/) (a.k.a. setup scripts) (foobar.lu)
If you are working on a project you want to distribute via pypi or have it pip installable from a git repository, or just want the ability to install your package into your path then this guide has the answers. It gives you a good step by step walkthrough of how to organize your packages and create appropriate setup scripts for them.

- [2012 PyData Workshop Videos](http://marakana.com/s/2012_pydata_workshop,1090/index.html) (marakana.com)
The PyData workshop was a two-day workshop hosted by google for data scientists interested in Python and Python developers interested in big data. This page has a list videos for many of the talks at the workshop. If big data is something that excites you, check this out.

- [Determining the Name of a Process from Python](http://www.doughellmann.com/articles/how-tos/python-process-name/index.html) (doughellmann.com)
This article is a great investigation of the best way to determine the name of a process in Python. Starting at a one liner seen at a conference Doug Hellmann goes down the rabbit hole in discussion strengths and weaknesses of the stated solution as well as the solutions he investigates.

- [Dynamic State Machines](http://harkablog.com/dynamic-state-machines.html) (harkablog.com)
This is a nice post about implementing finite state machines in a dynamic language like Python. Good explanation, complete with code example, take a look.

- [I am doing HTTP wrong](https://speakerdeck.com/u/mitsuhiko/p/i-am-doing-http-wrong) (speakerdeck.com)
A fresh look at HTTP for agile languages (more importantly: Python) by Armin Ronacher, goes through the evolution of web developer and mistakes he has made.

- [Multiple Python Sites nginx and uWSGI emperor](http://tghw.com/blog/multiple-django-and-flask-sites-with-nginx-and-uwsgi-emperor) (tghw.com)
This article highlights the uWSGI emperor mode. It is a special uWSGI instance that will monitor specific events and will spawn/stop/reload instances on demand. Pretty awesome.

- [Python HOWTOs](http://docs.python.org/release/3.1.5/howto/index.html) (python.org)
This is a collection of HOWTOs modelled after the Linux Documentation Project's HOWTO collection that is maintained in the python documentation. It has a bit of everything from "Curses programming with Python" to "Use Python in the web". Definitely worth checking out.


# 是也乎

- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 4.2 分钟 完成原文 md 格式化.
