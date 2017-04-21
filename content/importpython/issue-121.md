Title: 蠎加载 121
Slug: importpython-121
Date: 2017-04-21 11:11
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 121](http://importpython.com/newsletter/no/121/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Django ORM vs SQLAlchemy – Vizbi](http://www.vizbi.com/technical/django-orm-vs-sqlalchemy/)
    + django, SQLAlchemy, ORM

Recently I started using SQLAlchemy and am very impressed with it. I have used Django ORM a lot in the past. This post compares achieving same result using Django and with SQLAlchemy. Let’s see which looks more intuitive.

(`是也乎:`

港真, 别在 Django 之外用 Django ORM
)

- [Python类型注释与图形算法 - 课程 第二部分](https://pkch.io/2017/04/12/python-graphs-part2/)
    + type annotation, graph

In this part, we will implement graph data structure using classes and interfaces, and discuss when it’s worth overruling type hints.

- [加速 Websockets 60X](https://www.willmcgugan.com/blog/tech/post/speeding-up-websockets-60x/)
    + websockets

I recently I had the opportunity to speed up some Websocket code that was a major bottleneck. The final solution was 60X (!) faster than the first pass, and an interesting exercise in optimizing inner loops.


- [图形数据库: 探讨你和 Python 的关系](https://medium.com/labcodes/graph-databases-talking-about-your-data-relationships-with-python-b438c689dc89)
    + graph databases

This trouble to visualise the relationship between entities in a Relational Database is a great reason to introduce the concept of graph. Graph is a data structure formed by a set of vertices V and a set of edges E. It can be represented graphically (where the vertices are shown as circles and edges are shown as lines) or mathematically in the form G = (V, E).


- [6 分钟魔改 Python 语言](https://hackernoon.com/modifying-the-python-language-in-7-minutes-b94b0a99ce14)
    + core-python, cpython

This week I raised my first pull-request to the CPython core project, which was declined :-( but as to not completely waste my time I’m writing my findings on how CPython works and show you how easy it is to modify the Python syntax.

- [使用 Nginx Nchan 和 Python 实现网络应用程序](https://medium.com/@skabbass1/realtime-web-apps-with-nginx-nchan-and-python-284c8ec61b65) 
    + nginx, nchan

Nchan makes writing realtime web based pub/sub applications a breeze. In this article, we will build a simple systems monitoring dashboard which displays process information in realtime similar to what you would see when you run the unix top or htop commands.

(`是也乎:`

港真, OpenResty 可以尝试

)

- [Python 中"非空集合"的交集](http://hackwrite.com/posts/intersection-of-non-empty-sets-in-python/)
    + list, set, code_snippets

Suppose you generate several sets on the fly, and you want to find the elements that are in all the sets. That's easy, it's the intersection of sets.

- [用 Watchdog 监控文件目录变更](https://medium.com/@vladbezden/monitoring-directories-for-file-changes-using-watchdog-8d4766e50340)
    + python, watchdog

I was working recently on writing Python code using TDD. So every time I change code I wanted to run command that will test my code if it pass unit tests. In order to do that I needed some service/app that will monitor for file changes, and if it changes execute my batch file that runs unit tests.



- [Jupyter Notebook 在项目的 virtual env](https://medium.com/@rohitsinha/jupyter-notebook-in-projects-virtual-env-df7cd686bd94)
    + jupyter

- [AWS Lambda 刚刚支持 3.6](https://aws.amazon.com/releasenotes/5198208415517126)
    + aws, lamda

- [SQL Server 2017: 用 Python 进行高级分析](https://www.youtube.com/watch?v=FcoY795jTcc)
    + sqlserver

In this session you will learn how SQL Server 2017 takes in-database analytics to the next level with support for both Python and R; delivering unparalleled scalability and speed with new deep learning algorithms built in.

(`是也乎:`

M$ 将 Linux 虚拟层追加到自己OS 中了,然后呢?

)

- [Control-C handling in Python and Trio](https://vorpus.org/blog/control-c-handling-in-python-and-trio/)
    + core-python

- [Kubernetes 调度在 Python](https://medium.com/@sebgoa/kubernetes-scheduling-in-python-3588f4928b13)
    + kubernetes

- [学习 Python 脚本来自动发布播客](https://opensource.com/article/17/4/automate-podcast-publishing-python)
    + podcast

(`是也乎:`

解决真实问题,永远是学习的正义动力...
)

## 好物
~ 包/模块/库/片段...


- [algorithms:](https://github.com/keon/algorithms)
    - 2112 Stars, 174 Fork

Minimal examples of data structures and algorithms in Python

(`是也乎:`

数据结构和算法的最小例子
)

- [jokekappa](https://github.com/CodeTengu/jokekappa)
    - 74 Stars, 7 Fork

A library for delivering one-line programming jokes

(`是也乎:`

国人作品...
)

- [cashier](https://github.com/atmb4u/cashier)
    - 53 Stars, 2 Fork

Persistent caching for python functions

(`是也乎:`

收银员? 这个项目名字起的好.

后端可以是 SQLite 的函式缓存模块,
可以对反复使用的函式进行 16倍速的加载加速...
是的,也支持了 Py3 
)

- [crickbuzz_cricket_score](https://github.com/LinuxTerminali/crickbuzz_cricket_score)
    - 13 Stars, 2 Fork

A Terminal based program to follow live cricket score by scraping crickbuzz.com

- [MigrateGitlabToGogs](https://github.com/MarcelSimon/MigrateGitlabToGogs)
    - 3 Stars, 0 Fork

Migrate repositories from Gitlab to Gogs or Gitea

(`是也乎:`

将仓库迁出 Gitlab 的工具...这是预兆哪, 俺也得迁移了...

以及 Gogs->Gitea 都是国人作品...
)

- [venvdetect](https://github.com/tstringer/venvdetect)
    - 3 Stars, 1 Fork

Detect available Python virtual environments in your current directory 

(`是也乎:`

py3 又得将 pyenv 解决过的问题,重新再嗯哼一下...
)

### (￣▽￣)

- [tankywoo/simiki](https://github.com/tankywoo/simiki)
    + 657 Stars, 95 Fork

Simiki is a simple wiki framework, written in Python.

(`是也乎:`

知道创宇 成员私人作品 md 的静态维基
)

# 是也乎

- 170421 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170421 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


