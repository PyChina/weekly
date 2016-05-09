Title: 蠎加载 71
Slug: importpython-71
Date: 2016-05-06 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 71](http://importpython.com/newsletter/no/71/)
- 欢迎, 来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)

## 该读
~ 文章, Blog, 教程...



- [Python 元类解释](http://masnun.com/2016/05/03/python-metaclass-explained.html)
    + core python

Python 的核心特性就是:`一切为对象`,
其实都是类的实例.

- [教程:如何基于 Django,Ngrok 构建 facebook 消息机械人 - Blog - Abhay Kashyap](https://abhaykashyap.com/blog/post/tutorial-how-build-facebook-messenger-bot-using-django-ngrok)
    + django

2016 是 Facebook 机械人元年,
基于地球上最大的短信平台, Facebook 推出了 Messenger 平台,
支持企业构建自己的自动应答系统;
此平台虽然还在 beta 阶段,
但是接入了 十亿 活跃用户,值得折腾....



- [uvloop: 异常快的 Python 网络](http://magic.io/blog/uvloop-make-python-networking-great-again/)
    + web framework

asyncio 是当前 Python 的标准异步 I/O 网络框架.
uvloop 则是能完全替代 asyncio 完备的更快的异步事务循环.
基于 libuv 以 Cython 构建;
事实上 uvloop 比 nodejs, gevent 或是其它异步框架快两倍以上.
性能接近 Go 语言实现的.

- [Django 爱好者的 ES6](https://www.caktusgroup.com/blog/2016/05/02/es6-django-lovers)
    + django

The Django community is not one to fall to bitrot. Django supports every new release of Python at an impressive pace. Active Django websites are commonly updated to new releases quickly and we take pride in providing stable, predictable upgrade paths. We should be as adamant about keeping up that pace with our frontends as we are with all the support Django and Python put into the backend. I think I can make the case that ES6 is both a part of that natural forward pace for us, and help you get started upgrading the frontend half of your projects today.

- [Growler](https://github.com/pyGrowler/Growler)
    + web framework


利用通过 PEP 3156 包含在 Python 3.4 内建模块中的 asyncio 库,
Growler 作为 web 应用框架,
类似 nodejs 的 express 库,
基于一系列中间件完成 HTTP 请求响应.
也通过中间件的串接完成复杂业务.


(`是也乎:`

何时开始微型 web 框架都和瓶子干上了!? 
)

- [Redis 缓存修饰符](https://github.com/alexk307/redis_cache)
    + code snippet

用 redis 完成的髙水平的函式缓存.

- [应该聘请那种给力的 Python 开发者? ](http://www.reddit.com/r/Python/comments/4gvoie/what_should_i_ask_to_hire_a_good_python_developer/)
    + Reddit Discussion

I need some advice. I founded a SAAS startup that is doing pretty well. When I was looking to build out my software I found a developer I had worked with in the past and brought him on as a partner in the business. He held an equity stake and built out the backend of our software (restful API and database) all using Python. Front end is also Python based.

- [Django bugfix 版本发布: 1.9.6 + 1.8.13](https://www.djangoproject.com/weblog/2016/may/02/bugfix-releases/)
    + release

Today we've issued bugfix releases for the 1.9 and 1.8 release series. Details can be found in the release notes for 1.9.6 and 1.8.13.

- [Python 3 的功能卫士](http://code.activestate.com/recipes/580658-function-guards-for-python-3/)
    + code snippet

模块实现了功能卫士 - 根据不同的参数将运行时调用重定向到不同的函式上.
表现形式是 `@guard` 修饰符.
并提供缺省值表达式: `_when`


- [用 Python 来预测你更喜欢面条中加 Qdoba 还是 Chipotle.](https://bigishdata.com/2016/05/03/the-special-relationship-between-noodles-and-qdoba)
    + machine learning

I’ve had a theory that for every Noodles, there’s a Qdoba that’s right next door. It might be some sort of selection bias however, since I can think of a couple locations where they’re directly next to each other. To me, Noodles and Qdoba have a special relationship, at least compared to other restaurants. I figured now was about the time I should test this, and I can use Chipotle to test. The question is: Which restaurant is more special to Noodles, Qdoba or Chipotle?



- [随机找到 bit.ly 地址](https://github.com/Nhadroj/bitly_finder/blob/master/bitly_finder.py)
    + code snippet

如果有人有足够的计算能力会发生什么?


- [PYCON上提出了澳大利亚教育研讨会的演讲！!](http://www.curiousefficiency.org/posts/2016/05/pycon-australia-education-cfp-2016.html)
    + community

Involved in Australian education, whether formally or informally? Making use of Python in your classes, workshops or other activities? Interested in sharing your efforts with other Australian educators, and with the developers that create the tools you use? Able to get to the Melbourne Convention & Exhibition Centre on Friday August 12th, 2016? Then please consider submitting a proposal to speak at the Python in Australian Education seminar at PyCon Australia 2016!

- [Get on Track w/ JIRA.](http://goo.gl/9PI2pq)
    + Sponsor

JIRA Software is the #1 software dev tool used by agile teams. Get started for free!


## 新书
~ New Books

- [Python GUI Programming Cookbook](http://importpython.com/books/517/python-gui-programming-cookbook/)

Over 80 object-oriented recipes to help you create mind-blowing GUIs in Python.



## 活动
~ Upcoming Conference / User Group Meet


- [SciPy Latin America](http://conf.scipyla.org/scipyla2016/)
- [OSCON Europe 2016](http://conferences.oreilly.com/oscon/open-source-eu-2016)
- [PyGrunn 2016](http://www.pygrunn.org/)
- [PyCon Iran](http://pycon.ir/)
- [PyData London 2016](http://pydata.org/london2016/)
- [Pycon Sweden](http://www.pycon.se/)




## 项目
~ 包/模块/库/片段...

Projects

- [cherrypy](https://github.com/cherrypy/cherrypy)
    - 50 Stars, 4 Fork

CherryPy is a pythonic, object-oriented HTTP framework.

(`是也乎:`

嗯哼?!10多年的老梗也开花了?!
)

- [tracker](https://github.com/BlockedServers/tracker)
    - 28 Stars, 9 Fork

自动追踪最近的变化, 不用人工刷了.

- [TensorNet-TF](https://github.com/timgaripov/TensorNet-TF)
    - 22 Stars, 4 Fork

TensorNet (TensorFlow implementation)

- [vmbench](https://github.com/MagicStack/vmbench)
    - 21 Stars, 7 Fork

Network Server Performance Benchmarking Toolbench

- [redis_cache](https://github.com/alexk307/redis_cache)
    - 15 Stars, 4 Fork

Redis Cache decorator

- [sqlitebiter](https://github.com/thombashi/sqlitebiter)
    - 15 Stars, 1 Fork

能从 CSV/JSON/Excel/Google-Sheets 创建 SQLite 数据库的 CLI 工具


- [PyDiscover](https://github.com/cr0hn/PyDiscover)
    - 11 Stars, 1 Fork

简单安全的轻量级服务发现!

PyDiscover: Simple Secure and Lightweight Python Service Discovery

- [word-rnn-tensorflow](https://github.com/hunkim/word-rnn-tensorflow)
    - 7 Stars, 1 Fork

Multi-layer Recurrent Neural Networks (LSTM, RNN) for word-level language models in Python using TensorFlow.

- [flask-optimize](https://github.com/sunary/flask-optimize)
    - 6 Stars, 0 Fork

Flask 优化: cache, minify html 以及 gzip response

- [drow](https://github.com/Sendhub/drow)
    - 6 Stars, 1 Fork

A Django-esque ORM for Riak with an emphasis on flexibility

- [lightsout](https://github.com/freakboy3742/lightsout)
    - 5 Stars, 0 Fork

将各种电台播放列表转化为 Spotify 播放列表.

- [twitter-sentiment-analysis](https://github.com/vivekanand1101/twitter-sentiment-analysis)
    - 5 Stars, 0 Fork

命令工具, 对 Twitter 消息进行情绪分析.
基于 sem 项目进行数据挖掘.


- [watchman](https://github.com/skcript/watchman)
    - 4 Stars, 4 Fork

将文件的变更转化为 API

- [django-webpush](https://github.com/safwanrahman/django-webpush)
    - 3 Stars, 2 Fork

Web Push Notification Package for Django


## DAMA 无责任推荐

- [pyenv-mirror](https://github.com/huntzhan/pyenv-mirror)
    + 7 Stars, 0 Fork

快速制作 pyenv 环境镜像的工具

(`是也乎:`

国人作品, 在 CPyUG 列表反馈下, 24小时以内,兼容了 Python 2 ;-)

嗯哼,当然的,没有 M$ 的支持.
)


### 工作

....


# 是也乎

- 160509 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160506 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


