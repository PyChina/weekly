Title: 蠎加载 39
Slug: importpython-39
Date: 2015-07-17 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 39](http://importpython.com/newsletter/no/39/)


**翻译ing...**

## 该读
~ 文章, Blog, 教程...


- [Orielly 免费书 - 开始用 Python 进行函式编程](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/dPL7jUJwgss/get-started-with-functional-programming-in-python.html)
    + book review

本书为读者展示了如何用函式编程来令项目更加易于创建和维护.
嗯哼,免费的!

(`是也乎:`

原版可爱的 Python 作者!

国内下载: [eBOOK-2015-07-19.zip](http://zoomq.qiniudn.com/ZQCollection/pdf/eBOOK-2015-07-19.zip)
)

- [Python 3.5 承诺新语法特性](http://www.infoq.com/news/2015/07/Python-35)
    - core python

3.5 核心开发者 Benjamin Peterse 曰了,
新语法特性以及新内建模块,等等,将显著提高库的效能.

(`是也乎:`

这是向 go 看齐的节奏哪....

)

- [在树莓派上用 Wing IDE 来调试 Python 代码](http://wingware.blogspot.com/2015/07/debugging-python-code-on-raspberry-pi.html)


Raspberry Pi 
并不是真的能跑  Wing IDE,
但是,通过远程工程的配置,可以连接到远程代码进行调试.

(`是也乎:`

坊间传说,世界上最远的调试是从地球调试月球轨道上的 LISP 应用...

)


- [EuroPython 2015: 指南 (移动版) 发布](http://blog.europython.eu/post/124165903022)
    - conference

大会新功能,
包含会场地图/完整的时间表/可创建个人日程/订阅 Twitter 标签,
可登录联络其它参会人员,
常用信息(联系人,CoC,FAQ,城市信息....)
而且能脱机使用(原生 app.)


(`是也乎:`

自从 Google I/O 2012 提供了大会专用 App. 后,
这已经成为了技术大会的标准配置了.

)


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

非常易用的 5维 gif 动画生成器
(X,Y,Z,时间,颜色).

依赖 ImageMagick 和框架的结合.


- [rpforest](https://github.com/lyst/rpforest)
    - 27 Stars, 6 Fork

生成随机森林投影

![rpforest](https://github.com/lyst/rpforest/raw/master/rpforest.jpg)

- [Salary-API](https://github.com/narenaryan/Salary-API)
    - 11 Stars, 4 Fork

芝加哥市职工工资API,
用 Python 基于 Flask 仅一小时内完成.

- [technetium](https://github.com/DrkSephy/technetium)
    - 11 Stars, 2 Fork

Bitbucket Centralized 的提案追踪和报告生成器

(`是也乎:`

K.K 发明的 `科技元素` 终于被抢先用上了
)

- [sempervirens](https://github.com/njsmith/sempervirens)
    - 10 Stars, 4 Fork

为开放数据科学, 收集实验性质数据的工具

- [screenshot.py](https://github.com/jabbalaci/screenshot.py)
    - 10 Stars, 0 Fork

抓网页为截屏


- [pyprice](https://github.com/Parkayun/pyprice)
    - 8 Stars, 0 Fork

股票价格指数的包装


- [data-analytics-course](https://github.com/captainsafia/data-analytics-course)
    - 6 Stars, 1 Fork

用 Python 桟来进行数据分析的仓库

- [csv2tex](https://github.com/mithodin/csv2tex)
    - 6 Stars, 1 Fork

将 csv 数据变成 LaTeX 表格, WoW!


- [sympy-pycon](https://github.com/aktech/sympy-pycon)
    - 5 Stars, 3 Fork

PyCon 印度 - SymPy 幻灯

- [pireal](https://github.com/centaurialpha/pireal)
    - 5 Stars, 0 Fork

关系代数的教育工具

(`是也乎:`

![pireal logo](https://github.com/centaurialpha/pireal/raw/master/src/images/pireal_banner.png)
)


## DAMA 无责任推荐

# 是也乎

- 150720 [Zoom.Quiet](http://zoomquiet.io) 完成快译
- 150717 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
