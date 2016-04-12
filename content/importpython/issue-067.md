Title: 蠎加载 67
Slug: importpython-67
Date: 2016-04-07 17:17
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 67](http://importpython.com/newsletter/no/67/)

## 该读
~ 文章, Blog, 教程...

- [和 Slack 一起更好的工作](http://www.launchbit.com/taz/11284-6334-111)
    + Sponsor

Slack 能将团队的所有消息聚集在一起的工具.
更少邮件/会议,嗯哼,作的更好.

(`是也乎:`

其实,好象并不怎么得力...
)


- [应该如何准备 Python 面试 ? - Reddit Discussion.](http://www.reddit.com/r/Python/comments/4df3oq/how_should_i_prepare_for_python_interview/)
    + interview

自学编程,两年前开始用 Django, Bootstrap, Python, Javascript.
刚刚通知有个 Python 工程师的职位,
那么应该如何准备?


- [面向 Python 程序猿的 函式编程 介绍](https://codesachin.wordpress.com/2016/04/03/a-practical-introduction-to-functional-programming-for-python-coders/)
    + core python

文章为已有 Python 编程经验的,给出了 函式编程 的介绍.

- [Python 在 JavaScript | 特性! PyCharm 远程调试.](http://i.imgur.com/1BKr16n.gif)
    + pycharm

新功能展示 gif 动画, PyCharm 全桟用户应该看看


- [Python 3 中的类型比较](http://eli.thegreenplace.net/2016/comparing-types-in-python-3/)
    + core python

如果在折腾 元编程, 一定发现需要一个类型排序.
不是对象,而是类型.
之前 Python2 的同类文章非常受欢迎,
Eli Bendersky 又写出了面向 Python 3 的.


- [Apache Kafka 生产者基线 - Java vs Jython vs Python](http://mrafayaleem.com/2016/03/31/apache-kafka-producer-benchmarks/)
    + benchmark

文章中,针对 Java, Jython 和 Python 进行了基线评测.


- [51 集 - Pyjion 和 Dino Viehland 以及 Brett Cannon](http://podcastinit.podbean.com/e/episode-51-pyjion-with-dino-viehland-and-brett-cannon/)
    + podcast

为了提高 CPython 的性能,
Dino Viehland 在暂定在 JIT 上进行改进.
他的公司 M$ , 决定赞助这一想法.
于是就有了 Pyjion 项目.
这集中,采访了核心成员,讨论了最新进展,以及一路上的困难.
当然,也跑题讨论了, 为什么 GIL 创造出来前,并没有想到这么可怕?


- [构建实时 apps](http://www.launchbit.com/taz/11284-6191-111)
    + Sponsor

Syncano. Database. Backend. Middleware. Real-time. Support. Start for free!


- [用 Feather 进行数据标准化](http://blog.yhat.com/posts/data-normalization-in-python.html)
    + pandas

The 162 game marathon MLB season is officially underway. In honor of the opening of another season of America's Pasttime I was working on a post that uses data from the MLB. What I realized was that as I was writing the post, I found that I kept struggling with inconsistent data across different seasons. It was really annoying and finally it hit me: This is what I should be writing about! Why not just dedicate an entire post to normalizing data!

- [如何扩展 Django: 超越基础 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-scale-django-beyond-the-basics)
    + django

文章包含以下内容: 缓存技术,
包括用 Varnish 高速缓存整个儿网站,
或视图基础上进行缓存控制.
静态文件传送给 CDN 而不是 Django.
如何用 uWSGI 从网络服务器上运行 Django 来提高恬静.
最后,可以了解到如何尽可能多的分配内存给 应用程序.


- [Python-lambda: 10分钟以内完成第一个 Python 的 Lambda 微应用](https://github.com/nficano/python-lambda)
    + aws

AWS Lambda 是种支持 Python/Jana/Node.js 的无主机应用发布平台.
只有在有请求时才真正运行的应用.
编写 Lambda 应用比较简单,
但是,绑定和部署没那么简单.
Python-lambda 就是专门简化这方面麻烦的工具!

- [8 皇后问题](http://feeds.wordaligned.org/~r/wordaligned/~3/OZXREqk3P9I/8-queens-puzzle)


Raymond Hettinger 将之前的方案,升级为 Python 3.

- [Channels 的 Docker 实例](https://zerokspot.com/weblog/2016/04/04/channels-in-docker/)
    + django

在 Budapest 举行的 DjangoCon Europe 2016 中 sprints 项目之一,
Andrew Godwin 的 Channels 框架很可能进入 Django 1.10 版本特性.
现在需要一个稳定的 WebSocket 方案,
其中基于 docker-compose 的很不错.上周宣布


- [Big Data Wrangling 和 Python Course](http://www.oreilly.com/pub/e/3704)

作者 Katharine Jarmul (Data Wrangling with Python) 

将发布为期两天的课程, 包含数据采集和管理,
使用 Pandas 进行数据分析,
以及使用类似 Hadoop 和 PySpark 进行集成,
地点在 NY.

- [如何在 Python 和 Django 中用 Elasticsearch, 第4部分 -创建前端](https://qbox.io/blog/elasticsearch-python-django-frontend-queries)

这是最后一集, 讨论如何在前端增加功能项,包含查询/索引/更新...

In the previous posts in this series ( shared in the previous issue of the newsletter ) we created a basic Django app and populated a database with automatically generated data. We also added data to the elasticsearch index in bulk, wrote a basic command, and added a mapping to the elasticsearch index. In this final article we will add functional frontend items, write queries, allow the index to update, and discuss a bonus tip.

- [Airbnb 开源 Caravel, 基于 Python/Javascript 的数据探索/可视化平台!](https://github.com/airbnb/caravel)

Caravel is a data exploration platform designed to be visual, intuitive and interactive.

(`是也乎:`

![sankey](http://airbnb.io/caravel/_images/sankey.png)

![force_directed](http://airbnb.io/caravel/_images/force_directed.png)

类似 AJAX, Airbnb 组合现有的优秀框架,变成了一个任性的大数据通用分享平台!

后端:Flask+Pandas+SqlAlchemy; 前端: react+d3.js+nvd3.org

唯一原创的是 [Druid](http://druid.io/druid.html) ~
近线通用数据存储.
异常活跃,已经有近千 Issue 了...

)

- [rochacbruno/dynaconf: 为 Python 动态加载配置](https://github.com/rochacbruno/dynaconf)

dynaconf  是 OSM(对象设置映射器),
可以读取从不同的数据源,
比如 配置文件/环境变量/redis/memcached/ini文件/json文件/yaml文件,
甚至于可以自定义格式.
(别说要从 xml 读取!)

(`是也乎:`

非常需要,但是,看起来还不成就.
其实,最关键的是如何动态加载/更新
)


- [smarturls](http://amitu.com/smarturls/)
    + django

smarturls 内置正则表达式模式库,
来轻松为 Django 构建路径表.
作者 Amit 是早期 Django 用户之一.
另外还有作品: [importd](https://github.com/amitu/importd)

(`是也乎:`

![Amit](https://avatars2.githubusercontent.com/u/58662?v=3&s=460)

胡子不够哪...

)

## 新书
~ New Books

NULL

## 项目
~ 包/模块/库/片段...


- [rsync-time-machine](https://github.com/infinet/rsync-time-machine)
    - 42 Stars, 1 Fork

Time Machine 样的备份.

- [cppn-gan-vae-tensorflow](https://github.com/hardmaru/cppn-gan-vae-tensorflow)
    - 36 Stars, 7 Fork

Train CPPNs 为 Generative Model, 
使用 Generative Adversarial Networks 以及 Variational Autoencoder 
技术生成高分辨率照片!

(`是也乎:`

![是也乎](https://camo.githubusercontent.com/71d9f802bb9af06ac24b9c87242196993406533b/68747470733a2f2f63646e2e7261776769742e636f6d2f686172646d6172752f6370706e2d67616e2d7661652d74656e736f72666c6f772f6d61737465722f6578616d706c65732f6f75747075745f6c696e6561722e676966)

不明觉厉

)

- [django-serial-forms](https://github.com/mjtamlyn/django-serial-forms)
    - 35 Stars, 4 Fork

Constructible, introspectable serializers and forms

- [channels-in-docker](https://github.com/zerok/channels-in-docker)
    - 8 Stars, 0 Fork

An example project for getting to know django channels.

(`是也乎:`

现在推广一个模块的标准三件套是:
github/pip/docker !!!

)

- [reCaptcha](https://github.com/ajaxtpm/reCaptcha)
    - 8 Stars, 4 Fork

为了自动通过 Google reCaptcha v2 而创建的系统.
包含 hashes/颜色直方 的宏大训练图像集.
所有研究细节在: https://habrahabr.ru/post/280230/

- [stats](https://github.com/fsr/stats)
    - 6 Stars, 0 Fork

:chart_with_upwards_trend: 

俺们办公室的状态数据.
公开了光传感器从办公室收集的数据.
并整理为卡片,为了给亲们任性的参观.
因为并没有严格的作习规定...

Statistics from our office. This projects evaluates the data gathered by the light sensor in our office and punches them into a card. The intention behind this is to give folks, who want to visit us in our office, a recommendation on how likely it is that somebody will be there, since we don't have strict office hours. These statistics pose as an addition to the Buerostatus project, which gathers the data and gives live feedback on our website.

(`是也乎:`

![stats](https://github.com/fsr/stats/raw/master/assets/example.png)

传说中的 `NoZuoNoDie` 嘛!?
)

- [couchbase-dump](https://github.com/rounds/couchbase-dump)
    - 6 Stars, 0 Fork

对 couchbase buckets 的导出/入, 以及查阅的支持脚本


- [aionotify](https://github.com/rbarrois/aionotify)
    - 6 Stars, 0 Fork

Simple, asyncio-based inotify library for Python

- [tnpy](https://github.com/ferventdesert/tnpy)
    - 5 Stars, 1 Fork

文本分析引擎
(匹配/改写/提取) (python edition)

(`是也乎:`

![tnpy](https://camo.githubusercontent.com/dfa0a0067f507296d4884f6f2400f40f71f0cd4a/687474703a2f2f7374617469632e7a7962756c756f2e636f6d2f627570747a796d2f6b736c3567677266636e3170736d646632663831693877672f666f6f2e706e67)

国人作品!
使用 qq 邮箱的 gitter ...
)

- [pyshaders](https://github.com/gabdube/pyshaders)
    - 5 Stars, 1 Fork

Pythonic OpenGL shader wrapper for python

- [pyrag-sports](https://github.com/PyRag/pyrag-sports)
    - 3 Stars, 2 Fork

CLI 工具,专门用来关注 football 和 cricket 信息.

(`是也乎:`

板球?! 好吧,印度人...
)

- [flask-pw](https://github.com/klen/flask-pw)
    - 3 Stars, 0 Fork

Peewee ORM integration for Flask framework

- [Earthquake-Notifier](https://github.com/requestsigdel/Earthquake-Notifier)
    - 2 Stars, 2 Fork

地震通知!
如果 感知到相关数据,
立即发送短信到 美国地质勘探局 的电话!

(`是也乎:`

细思恐极, 绝对需要哪! 
等等! 原来是用 Raspberry Pi 制造的地震仪?!
嚓! 官方信了才见鬼了...
)

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

- 160408 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160407 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


