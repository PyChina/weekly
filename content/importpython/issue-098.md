Title: 蠎加载 98
Slug: importpython-98
Date: 2016-11-10 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 98](http://importpython.com/newsletter/no/98/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Airflow 实用介绍](https://www.youtube.com/watch?v=cHATHSB_450&feature=youtu.be)
    + video, workflow engine

Airflow is a popular pipeline orchestration tool for Python that allows users to configure complex (or simple!) multi-system workflows that are executed in parallel across any number of workers. A single pipeline might contain bash, Python, and SQL operations. With dependencies specified between tasks, Airflow knows which ones it can run in parallel and which ones must run after others. Airflow is written in Python and users can add their own operators with custom functionality, doing anything Python can do.

(`是也乎:`

今年 PyCon 上出现的仙器,多后端/Pythonic 工作流/管道管理平台
)


- [Python 中时间测试的乐趣和收益](https://hackernoon.com/timing-tests-in-python-for-fun-and-profit-1663144571#.4nromm7cy)
    + debug

I was preparing to push some changes a couple of days ago and as I usually do, I ran the tests. I sat back in my chair as the dots raced across the screen when suddenly I noticed that one of the dots linger. ”OS is probably running some updates in the background or something” I said to myself, and ran the tests again just to be sure. I watched closely as the dots filled the screen and there it was again?—?I have a slow test!

(`是也乎:`

Matrix-样 数据观察形式看来是正确的
)

- [Become a pdb power-user](https://medium.com/instamojo-matters/become-a-pdb-power-user-e3fc4e2774b2#.856wmyqbs)
    + pdb

Good Tutorial on using pdb.


(`是也乎:`

`..It is not necessary to use pdb all the time`
嗯哼,作者都说的很明白,其实大家都清楚,动用 pdb 的情景都是不得不作 `接盘侠` 时,
面对纠结在一起的代码时,不得不进行的刺探,
因为没有自信自己在看过所有代码,将思想扭曲为当初那位崩溃的程序猿相同状态后,
是否能恢复清明...
)

- [教程提案还有三周可以提交](http://pycon.blogspot.com/2016/11/tutorial-proposals-are-due-in-two-weeks.html)
    + pycon

Talk proposals will be due on 2017 January 3.Poster proposals will be due on 2017 January 3.Tutorial proposals are due on 2017 November 30. Yes, that’s right — tutorial proposals are due in three weeks.



- [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)
    + async-io, curated list

A curated list of awesome Python asyncio frameworks, libraries, software and resources.

(`是也乎:`

是 github 带领中国程序猿重新认识了 awesome 这词儿,

现在最高效的领域技术搜索技巧就是在 github 中搜索 `awesome+` 技术名
)

- [Some thoughts on asynchronous API design in a post-async/await world](https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/)
    + async-io

I've recently been exploring the exciting new world of asynchronous I/O libraries in Python 3 – specifically asyncio and curio. These two libraries make some different design choices. This is an essay that I wrote to try to explain to myself what those differences are and why I think they matter, and distill some principles for designing event loop APIs and asynchronous libraries in Python.


(`是也乎:`

Py3 中内建的 `asyncio` 和 `curio` 成为两大焦点都在进行折腾...
)

- [django-flat-responsive](https://github.com/elky/django-flat-responsive)
    + django

An extension for Django admin that makes interface mobile friendly.


- [如何在 Python 中启动 Landsat 数据处理?](https://cloud.google.com/blog/big-data/2016/11/how-to-do-distributed-processing-of-landsat-data-in-python)
    + google cloud

Cloud Dataflow provides a fully-managed, autoscaling, serverless execution environment for data pipelines written in Apache Beam. In this article Lak Lakshmanan and Matt Hancher show us how to create a monthly vegetation index from Landsat images, available as a public dataset.


(`是也乎:`

GCP 中的 Cloud Dataflow 支持 Apache Beam 可以发布无主机数据处理流程...
)


## 好物
~ 包/模块/库/片段...


- [astpath](https://github.com/hchasestevens/astpath)
    + opensource project

支持使用 XPath 语法来查询 Python ASTs 的 CLI 工具

- [nathan](https://github.com/mseclab/nathan) 
    + 108 Stars, 18 Fork

针对移动端安全测试的 Android 模拟器

(`是也乎:`

怎么看也不象能在 M$ 环境中跑的工具
)


- [byteNet-tensorflow](https://github.com/paarthneekhara/byteNet-tensorflow)
    - 92 Stars, 11 Fork

ByteNet for character-level language modelling

- [word_forms](https://github.com/gutfeeling/word_forms)
    - 47 Stars, 1 Fork

Accurately generate all possible forms of an English word e.g "election" --> "elect", "electoral", "electorate" etc.

(`是也乎:`

同根词列举工具

![word_forms](https://github.com/gutfeeling/word_forms/raw/master/logo.png)
)

- [foss-heartbeat](https://github.com/sarahsharp/foss-heartbeat)
    - 25 Stars, 4 Fork

FOSS 心跳分析,
数据来自社区志愿者
:heartbeat:

- [reprint](https://github.com/Yinzo/reprint)
    - 10 Stars, 0 Fork

适用于 Python 2/3 的简易变量绑定与多行输出刷新的库


(`是也乎:`

![horse_race_demo](https://raw.githubusercontent.com/yinzo/reprint/master/demo/images/horse_race_demo.gif)

华南理工大学在校学生,国人作品 ;-)

)

- [pyjet](https://github.com/wolfv/pyjet)
    - 8 Stars, 1 Fork

JET is a different approach to make numeric python substantially faster


(`是也乎:`

![jet_logo](https://raw.githubusercontent.com/wolfv/pyjet/master/docs/img/jet_logo.png)

嗯哼,更快的 numpy,,,随着数据科学的兴起, 作为基础中的基础作品 numpy 在遭受各种优化/加速
)

- [Batch-Image-Downloader](https://github.com/shawon922/Batch-Image-Downloader)
    - 7 Stars, 5 Fork

A simple Batch Image Downloader using Python and BeautifulSoup.

(`是也乎:`

美汤!? 弃疗... 孟加拉 的老兄弟...
)

- [ipynb](https://github.com/ipython/ipynb)
    - 6 Stars, 1 Fork

Package / Module importer for importing code from Jupyter Notebook files (.ipynb)

(`是也乎:`

ipynb 已经开始构建完备的生态了哪...
)

- [slackbridge](https://github.com/ocf/slackbridge)
    - 2 Stars, 0 Fork

Bridge between IRC and Slack 

(`是也乎:`

IRC 上古神器, Slack 今墙外仙器..
)

# 是也乎
~ 双 11 了,人造节日中可能最费銭的一个,大家都砍了什么?!

- 161110 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161110 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


