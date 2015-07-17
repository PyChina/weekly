Title: 蠎加载 39
Slug: importpython-39
Date: 2015-07-17 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 39](http://importpython.com/newsletter/no/39/)


**翻译ing...**

## 该读
~ 文章, Blog, 教程...


- [Get started with functional programming in Python - Free Book from Orielly](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/dPL7jUJwgss/get-started-with-functional-programming-in-python.html)
    + book review
Functional Programming in Python provides readers with an excellent introduction to how to write Python in a more functional style, and when doing so make projects easier to create and maintain. Did we mention it's FREE.

- [Python 3.5 Promises New Syntax Features](http://www.infoq.com/news/2015/07/Python-35)
    - core python
In the article What’s New In Python 3.5 core developer Benjamin Petersen details new syntax features, and new library modules, as well as new built-in features and significantly improved library features.

- [Debugging Python Code on Raspberry Pi with Wing IDE](http://wingware.blogspot.com/2015/07/debugging-python-code-on-raspberry-pi.html)
The Raspberry Pi is not really capable of running Wing IDE itself, but you can set up Wing IDE on a computer connected to the Raspberry Pi to work on and debug Python code remotely.

- [EuroPython 2015: Guidebook (mobile schedule) available](http://blog.europython.eu/post/124165903022)
    - conference
Nice Features, Maps of the venue, Full schedule, Create your personal schedule (My Schedule) ,Watch Twitter updates and tweet right in the guidebook, Contact other attendees who have sign in to the guidebook, Useful information (Contacts, CoC, FAQ, City Infos, etc.), Offline use (for the native apps).

- [Searching for Approximate Nearest Neighbours](http://developers.lyst.com/2015/07/10/ann/)
    - machine learning    
The essence of approximate nearest neighbour search consists in roughly dividing the search space into a number of buckets that contain points that are close to each other, and then only looking within a given bucket when performing a search. This gives us speed (we only have to scan the contents of a given bucket) at the expense of accuracy (it's possible for a point's nearest neighbours to lie in a different bucket).

- [Getting started with Celery and Redis](http://agiliq.com/blog/2015/07/getting-started-with-celery-and-redis/)
    - redis, celery
This Article focuses on When to use Celery? Why to use Celery ?. A simple celery program. Having a slow script and making it faster using celery. Celery configuration and code in different files. Using celery with tasks spanned across multiple modules. Using celery with a package. Redis and celery on separate machine. Web-application/script and celery on separate machines.

- [Decorator for defining functions with keyword-only arguments (Python)](http://code.activestate.com/recipes/579079-decorator-for-defining-functions-with-keyword-only/)
    - core python
Python2.x implementation of python3's keyword-only arguments (aka arguments that must be specified as keywords, and are not automatically filled in by positional arguments - see PEP 3102).

- [Episode #16 Python at Netflix - [Talk Python To Me Podcast]](http://www.talkpythontome.com/episodes/show/16/python-at-netflix)
Podcast by the folks a talkpythontome

- [Elliott's Dev Blog: Azure AD in Django with Python Social Auth](http://www.elliottmiller.me/2015/06/azure-ad-in-django-with-python-social.html)
    - django
Azure Active Directory (AAD) support was recently added to the Python-Social-Auth library. I was really impressed by how easy it was to get Azure Authentication up and running in a Django application. I'd like to call out this blog post for its very good introduction to using Python-Social-Auth in a Django App, and it made my exploration of this library a lot easier.

- [Episode 15 - Damien George Talks To Us About MicroPython](http://podcastinit.podbean.com/e/episode-15-damien-george-talks-to-us-about-micropython/)
    - podcast
Podcast with Damien on MicroPython. Python Interpreter running on micro-controller. Look Ma, No OS.

- [Scientific computing in Python](http://feedproxy.google.com/~r/TheEndeavour/~3/ioZwJmNKjaM/)
Scientific computing in Python is expanding and maturing rapidly. Last week at the SciPy 2015 conference there were about twice as many people as when I’d last gone to the conference in 2013. You can get some idea of the rapid develop of the scientific Python stack and its future direction by watching the final keynote of the conference by Jake VanderPlas.

- [Sane Password Strength Validation for Django with zxcvbn | scot hacker's foobar blog](http://birdhouse.org/blog/2015/06/16/sane-password-strength-validation-for-django-with-zxcvbn/)
    - django
A while back, Dropbox released a very smart password validation library called zxcvbn (check the bottom left row of your keyboard) which measures strength as “entropy,” rather than as a function of adherence to a particular set of rules. Running zxcvbn on the backend eliminates the dictionary size problem, but introduces a new one: You want to be able to preserve back-end field validation but still provide real-time feedback in the client. I’ve put together a kit for Django that satisfies both goals (yes there are other Django implementations for zxcvbn but none of them worked quite how I wanted).

- [Django Tutorial | Internationalization & Localization](http://www.marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones)
    + django
In this part of the TaskBuster Django Tutorial, we’ll talk about Internationalization, Localization and Time Zones. We will define two different languages for our website, create urls specific for each of them, and make our website to support these two languages. Moreover, we’ll talk about the time zone and how we can show the local time on a template. 


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

- [Animator5D](https://github.com/bencbartlett/Animator5D)
    - 55 Stars, 4 Fork
Very simple-to-use framework for rendering 5-dimensional animations (x, y, z, time, some color value) as an animated gif. This requires ImageMagick to combine the frames, but you can still render them without having it installed and just combine them with some online gif maker.

- [rpforest](https://github.com/lyst/rpforest)
    - 27 Stars, 6 Fork
It is a forest of random projection trees

- [Salary-API](https://github.com/narenaryan/Salary-API)
    - 11 Stars, 4 Fork
Chicago city employees Salary API built in one hour with Python and Flask under 35 lines of code

- [technetium](https://github.com/DrkSephy/technetium)
    - 11 Stars, 2 Fork
Bitbucket Centralized Issue Tracker and Report Generation

(`是也乎:`

K.K 发明的 `科技元素` 终于被抢先用上了
)

- [sempervirens](https://github.com/njsmith/sempervirens)
    - 10 Stars, 4 Fork
An experimental prototype for gathering anonymous, opt-in usage data for open scientific software

- [screenshot.py](https://github.com/jabbalaci/screenshot.py)
    - 10 Stars, 0 Fork
Taking a screenshot of a webpage.

- [pyprice](https://github.com/Parkayun/pyprice)
    - 8 Stars, 0 Fork
stock price index wrapper.

- [data-analytics-course](https://github.com/captainsafia/data-analytics-course)
    - 6 Stars, 1 Fork
A repository for data analytics with the Python stack

- [csv2tex](https://github.com/mithodin/csv2tex)
    - 6 Stars, 1 Fork
Convert your data files to LaTeX tabular

- [sympy-pycon](https://github.com/aktech/sympy-pycon)
    - 5 Stars, 3 Fork
PyCon India - SymPy Presentation

- [pireal](https://github.com/centaurialpha/pireal)
    - 5 Stars, 0 Fork
Educational tool for working with relational algebra 



## DAMA 无责任推荐

# 是也乎

- 1507?? 老高/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150717 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
