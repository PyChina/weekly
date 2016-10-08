Title: 蠎加载 93
Slug: importpython-93
Date: 2016-10-08 21:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 93](http://importpython.com/newsletter/no/93/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [为 Python 开发者配置 Sublime Text](https://dbader.org/products/sublime-python-guide)
    + sublime

We have been sharing Daniel's articles and videos from this youtube channel dedicated to Python and Sublime for a while now https://www.youtube.com/channel/UCI0vQvr9aFn27yR6Ej6n5UA . Today Daniel published his book on Sublime Text for Python Developers. Have a look if you use sublime text. Here is a 30% discount for all ImportPython Subscribers.


(`是也乎:`

价值 $29 的课程
![book-package](https://dbader.org/img/book-package.png)
)

- [用 Flask 和 SQLAlchemy 实现 "Soft Delete" 模式](http://blog.miguelgrinberg.com/post/implementing-the-soft-delete-pattern-with-flask-and-sqlalchemy)
    + flask, SQLAlchemy

You can find lots of reasons to never delete records from your database. The Soft Delete pattern is one of the available options to implement deletions without actually deleting the data. It does it by adding an extra column to your database table(s) that keeps track of the deleted state of each of its rows. This sounds straightforward to implement, and strictly speaking it is, but the complications that derive from the use of soft deletes are far from trivial. In this article I will discuss some of these issues and how I avoid them in Flask and SQLAlchemy based applications.

(`是也乎:`

简单的说, 手写 SQL 可以轻易作的事儿,在 ORM 世界中,嗯哼...
)

- [通过 Python 的 Data Visualization Landscape 进行动态游历(包含 ggplot 以及 Altair)](https://dansaber.wordpress.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/)
    +  data visualization

Comprehensive listing of all data visualization packages with small codesnippets.

- [在 Django 折腾并发数据的正确姿势](http://www.vinta.com.br/blog/2016/database-concurrency-in-django-the-right-way/)
    + django

Guilherme Caminha explores the utility of using on_commit hook available from 1.9 onwards in sequencing part of a time consuming task in django view and rest offloaded to an async process.


- [思考一下协程](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/ogAkpm2QzzM/thinking-in-coroutines)
    + async-io

Lukasz Langa uses asyncio source code to explain the event loop, blocking calls, coroutines, tasks, futures, thread pool executors, and process pool executors.

(`是也乎:`

这是 go 的核心竞争力,其实 py 也早已有了对应的机制,只是....
)

- [自动为 click 应用生成 man 说明](https://github.com/timofurrer/click-man)
    + opensource project

Click is my go to Python package for creating command line applications. click-man will generate one man page per command of your click CLI application specified in console_scripts in your setup.py.

(`是也乎:`

http://click.pocoo.org/
对的只出精品的  pocoo 团队的 CLI 工具包
)


- [当周PyDev: Bryan Van de Ven](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/F8vkE9fKESU/)
    + interview

Bryan is a core developer of the Bokeh project, which is a visualization package for Python. He has also helped with the development of Anaconda.

(`是也乎:`

名字有 van 的, 都是贵族后代,
同时在 Anaconda 和 数据可视化领域都有深入的强人...
)


- [Flashlight 是分析及解决四旋翼控制问题的轻量级 Python 库.](https://mikeroberts3000.github.io/flashlight/)

Flashlight enables you to easily solve for minimum snap trajectories that go through a sequence of waypoints, compute the required control forces along trajectories, execute the trajectories in a physics simulator, and visualize the simulation results.

(`是也乎:`

当然,不是 DJI 开源的
)

- [Church](https://github.com/lk-geimfari/church)
    + opensource project

Church is a library to generate fake data. It's very useful when you need to bootstrap your database.

(`是也乎:`

专注自动生成徦数据的库,再也不用折腾 SQL 了...
)

- [5 music things and Python](http://raspberry-python.blogspot.com/2016/09/5-music-things.html)

Raspberry and Python projects/scripts.

(`是也乎:`

![church](https://raw.githubusercontent.com/lk-geimfari/church/master/examples/church.png)
)

- [validr](https://github.com/guyskk/validr)

A simple,fast,extensible python library for data validation.

(`是也乎:`

简单，快速，可拓展的数据校验库;
国人作品, 仅支持 Py 3.3+;
使用 tox 管理 pytest 测试案例...

私人官网果然也关注了 "新人到底需要什么" 长线讨论: [Python入门指北](https://www.kkblog.me/notes/Python%E5%85%A5%E9%97%A8%E6%8C%87%E5%8C%97)
)



## 活动
    ~ Upcoming Conference / User Group Meet

- [Santa Cruz Python Meetup](http://www.meetup.com/Santa-Cruz-Python-Meetup/)
- [Python Brasil [12]](http://2016.pythonbrasil.org.br/)
- [PyCon Ireland 2016](https://python.ie/pycon-2016/)
- [PyCon Canada 2016](https://2016.pycon.ca/)
- [PyData Cologne 2016](http://pydata.org/cologne2016/)
- [GeoPython 2017](http://2017.geopython.net/)


## 项目
~ 包/模块/库/片段...

- [tf-agent](https://github.com/karpathy/tf-agent)
    - 27 Stars, 1 Fork

专注 OpenAI gym 环境中代理 tensorflow 强化学习请求

- [become](https://github.com/llllllllll/become)
    - 5 Stars, 0 Fork

Make one object become another.

(`是也乎:`

github ID 好屌, 这个模块的功能也非常屌...
)

- [python-line-api](https://github.com/shlee322/python-line-api)
    - 4 Stars, 0 Fork

SDK of the LINE Messaging API for Python.

(`是也乎:`

又一个 IM 在 CLI 可用了...
)

- [football-stats](https://github.com/dev-labs-bg/football-stats)
    - 2 Stars, 0 Fork

Football stats is a system which has the purpose of helping football match analyses. The final goal of the project is to have the capability of ball and players' position analysis, creating heatmaps and statistics of different actions or situations.

(`是也乎:`

数据可视化从蓝球进入了 Football,俄国银作品
)

- [pytocli](https://github.com/renzon/pytocli)
    - 2 Stars, 0 Fork

A Python lib to generate CLI commands

-  [xfce4-system-monitor](https://github.com/d0u9/xfce4-system-monitor)
    - 1 Stars, 0 Fork

An xfce panel plugin to display the necessary information of the system.

(`是也乎:`

![screenshoot_1.png（PNG 图像，95x36 像素）](https://raw.githubusercontent.com/d0u9/xfce4-system-monitor/master/screenshoot_1.png)
)

# 是也乎

- 161008 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161008 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


