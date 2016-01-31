Title: 蠎加载 59
Slug: importpython-59
Date: 2016-01-30 01:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 59](http://importpython.com/newsletter/no/59/)

## 该读
~ 文章, Blog, 教程...



- [在 minecraft 中学习编程](http://importpython.com/blog/post/learn-to-program-with-minecraft)
    + book review

Minecraft(我的世界) 
是最著名的沙箱游戏.
用户通过接口在3D 世界中探索/创造立方体为基础的世界.
当然的有 Python 接口,
可以可以编程来创建/控制/使用这一无限世界.
链接是图书信息...


- [Python 测试/图书/播客](http://nedbatchelder.com//blog/201601/python_testing_book_and_podcast.html)
    + book review

Harry Percival 的好书,有关测试驱动开发在Python 编程实践中.
如果之前注意过此书信息,
那么这是另外一个渠道来感受其魅力.


- [用  Marathon API 部署 Py3 应用到 Apache Mesos 集群](http://www.giantflyingsaucer.com/blog/?p=5813)

工作中,笔者一直在使用 Apache Mesos 部署各种应用,
包含 go/python/lua 等等.
同时也在使用  Chronos 和 Marathon.
文章中展示如何对 Marathon(通过 Docker)管理的本地 Mesos 集群
进行简单的应用部署.


- [caktus/margarita: 很赞的 Django 部署相关 Salt states 脚本集合.](https://github.com/caktus/margarita/)

仓库中收集了各种基于 SaltStack 的部署/监控模块.
专门为 Caktus Django 项目创建.

- [Your Django Story: Meet Katie Bell](http://blog.djangogirls.org/post/138026903728)
    + interview
Katie Bell is a developer at Grok Learning, where she’s been doing a combination of things since joining the team in March 2015. She builds new components of the learning platform and also writes course content. Grok Learning provides programming and web development courses to be used in schools. Before Katie moved back to Sydney to join Grok, she was a Site Reliability Engineer at Google in Switzerland, working on storage systems.

- [meza: 处理表格( tabular )数据的 Python 工具集](https://github.com/reubano/meza)

meza 是个 Python 库,
专门读取和处理表格数据 ;
函式型接口,擅长读写大文件,
并支持十数种文件格式.

- [PyDelhi Conference](http://pydelhi.org/conference/)
    + pycon

Py德里大会 又一个技术大会,
由 PyDelhi 社区创办,每年一次,关注 Python 技术的应用和开发.
今年是第一届,期待全球 Pythoneer 来参加.

- [Walrus 实例, 又一种轻型 Redis 工具集](http://charlesleifer.com/blog/examples-of-using-walrus-a-lightweight-redis-toolkit)
    + redis

walrus 是作者结合 Python 和 Redis 工作经验的作品.
包含大量 Redist 原语水平的 Python 接口以及功能,
文章中展示各种功能,并演示在项目中使用的情景.


- [基于 Python 的缩址](https://github.com/ugcoder/Py-URL-Shortener)
    + flask

Py URL Shortener 
是供 Flask 应用中对 URL 缩址以及重定向支持.


- [PEP 513 - 便携式 Linux 构建发布的标签平台](https://www.python.org/dev/peps/pep-0513/)

PEP 提案描述了又一种 Python 包构建发布的标签平台,
类似 wheels, 调用 `manylinux1_{x86_64,i386}` 外部依赖限制,
来利用 Linux 内核限制在核心用户空间ABI.
建议 PyPI 支持在标签平台中上传以及发布 wheel 包,
以便在所有支持平台上通过 pip 完成下载和安装.

- [django-scribbler](https://github.com/caktus/django-scribbler)
    + django

django-scribbler 
是片段管理应用,可以包含在 Django 发布的web 网站中

http://readthedocs.org/docs/django-scribbler/ 


## 新书
~ New Books

...


## 项目
~ 包/模块/库/片段...

- [whatportis](https://github.com/ncrocfer/whatportis)
    - 104 Stars, 12 Fork

搜索端口名和数值的命令

(`是也乎:`


    $ whatportis redis
    +-------+------+----------+---------------------------------------+
    | Name  | Port | Protocol | Description                           |
    +-------+------+----------+---------------------------------------+
    | redis | 6379 |   tcp    | An advanced key-value cache and store |
    +-------+------+----------+---------------------------------------+

    $ whatportis 5432
    +------------+------+----------+---------------------+
    | Name       | Port | Protocol | Description         |
    +------------+------+----------+---------------------+
    | postgresql | 5432 |   tcp    | PostgreSQL Database |
    | postgresql | 5432 |   udp    | PostgreSQL Database |
    +------------+------+----------+---------------------+


实用到爆的工具!
)

- [django-stackoverflow-trace](https://github.com/emre/django-stackoverflow-trace)
    - 104 Stars, 3 Fork

定制的Django的堆栈跟踪

- [flyover](https://github.com/jeremybmerrill/flyover)
    - 62 Stars, 5 Fork

`当前`有哪些航班飞过我们头顶?!


- [open-syllabus-project](https://github.com/davidmcclure/open-syllabus-project)
    - 30 Stars, 0 Fork

我们能从 100万 以上的课程中学到什么?!

(`是也乎:`

细思恐极...所以,课程并不是都值得学习!?
还是人类的知识体系已经发展到没有这么多课程就无法承载了?!
又或是...

)

- [jenkins-phoenix](https://github.com/ianmiell/jenkins-phoenix)
    - 21 Stars, 5 Fork

用 Docker 进行无状态的 Jenkins 部署

- [django-post-request-task](https://github.com/mozilla/django-post-request-task)
    - 16 Stars, 2 Fork

celery 任务类的扩展,
可以在请求结束后,
通知为 Django 的 `request_started` 和 `request_finished` 信号.


- [preprocessor](https://github.com/s/preprocessor)
    - 12 Stars, 1 Fork

优雅的 tweet 预处理...

- [pipstrap](https://github.com/erikrose/pipstrap)
    - 9 Stars, 1 Fork

简单脚本,能伪装可信根,以便 pip 安装.

- [pipgh](https://github.com/ffunenga/pipgh)
    - 8 Stars, 1 Fork

A tool to install python packages from Github.

(`是也乎:`

上次介绍过,作者曰了,先别用...
)

- [Gitffiti](https://github.com/Moises404/Gitffiti)
    - 7 Stars, 0 Fork

Gitffiti Repo




## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 160131 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160130 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


