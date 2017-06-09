Title: 蠎加载 128
Slug: importpython-128
Date: 2017-06-08 19:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 128](http://importpython.com/newsletter/no/128/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [保持 Python 竞争力](https://lwn.net/Articles/723949/)
    + core-python

Victor Stinner sees a need to improve Python performance in order to keep it competitive with other languages. He brought up some ideas for doing that in a 2017 Python Language Summit session. No solid conclusions were reached, but there is a seemingly growing segment of the core developers who are interested in pushing Python's performance much further, possibly breaking the existing C API in the process.

(`是也乎:`

运行时性能爱好者们的嗯哼...
)

- [用 Luigi 构建并监视批量处理的管道](https://labs.getninjas.com.br/using-luigi-to-create-and-monitor-pipelines-of-batch-jobs-eb8b3cd2a574)
    + luigi, pipeline

Luigi is a Python module that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualisation etc. It also comes with Hadoop support built in.

- [机器学习和数学的 Python 作弊条](https://unsupervisedmethods.com/cheat-sheet-of-machine-learning-and-python-and-math-cheat-sheets-a4afe4e791b6)
    + machine learning

Curated list of cheatsheets.

(`是也乎:`

![cheat-sheet](https://cdn-images-1.medium.com/max/800/1*gccuMDV8fXjcvz1RSk4kgQ.png)

讲真, 图形的不如 ipynb 那种可运行的...

)


- [PyGotham 2017 - 主题征集ing](https://www.papercall.io/pygotham-2017)
    + pygotham

PyGotham is a New York City based, eclectic, Py-centric conference covering many topics. There’s a diverse speaker list, and some things which will be quite different. PyGotham attracts developers of various backgrounds and skill levels from the New York metropolitan area and beyond. Activities include two full days of talks, lightning talk sessions, and a social event.


- [pyenv 和 cron](https://medium.com/@sarit.r/pyenv-with-cron-17a9f2aacd42)
    + pyenv

Do not use /root/.pyenv/shims/python . Use direct python in pyenv.


(`是也乎:`

其实, 更加 Pythonic 的方案是脱离 cron 使用 python 原生的定期任务模块
)

- [用 10 行 Python 构建个文章基础拼写检查器](https://hackernoon.com/build-a-naive-article-spell-checker-in-10-lines-of-python-code-b325a67f2c3)
    + codesnippet

Build a naive Article Spell-checker in 10 Lines of Python Code.


- [Paranoid 的包检查器](https://medium.com/python-pandemonium/python-package-management-for-the-paranoid-52c23f6aba6a)
    + security

- [用 Elizabeth 生成模拟数据: Part II](https://medium.com/wemake-services/generating-mock-data-with-elizabeth-part-ii-bb16a3f3106f)
    + mocking

Elizabeth is a Python library, which helps generate mock data. Part II of the tutorial we shared previously.


- [Infoblox Bulk DNS 追加](https://medium.com/@Weck/infoblox-bulk-dns-add-with-python-3a1551969963)
    + codesnippet

- [Python 中的记录,结构,数据传输对象](https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python#.)
    + core-python

How to implement records, structs, and “plain old data objects” in Python using only built-in data types and classes from the standard library.

(`是也乎:`

![records-structs](https://dbader.org/blog/figures/records-structs-in-python.png)

)

- [只有升级到 Py3 才能享受的 10 大极赞特性](http://www.asmeurer.com/python3-presentation/slides.html#1)
    + core-python

(`是也乎:`

可下载的 pdf 版本幻灯:
[10 awesome features](http://asmeurer.github.io/python3-presentation/python3-presentation.pdf)

- 高级解包 ~ 追加了变参数,以及更直觉的操作
- 关键词参数 ~ 能模式匹配了
- Chained 异常 ~ 能返回更多信息了
- 更好的追踪子类 OSError 
- 一切都能迭代了
- 更加严格的比较了 ~ 原先一切都能相互嗯哼不行了
- yield from ~ 形式上更加明显进行嗯哼了
- asyncio ~ 重点广告特性
- 标准库追加了几个
- Fun ~ 中文|emoji 变量/类/函式名,
- 区分了 Unicode and bytes
- 矩阵运算支持
- Pathlib ~ 只希望 win 系统也相同支持的更加自然...

)

- [Apache Kafka 简介](https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/)
    + kafka

In this blog post, we’re going to get back to basics and walk through how to get started using Apache Kafka with your Python applications.


- [Picard](https://picard.musicbrainz.org/)
    + music

Picard is a cross-platform music tagger written in Python. This is a fairly old package.



## 好物
~ 包/模块/库/片段...



- [netbox](https://github.com/digitalocean/netbox)
    - 2492 Stars, 356 Fork

NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers.

(`是也乎:`

![netbox_logo](https://github.com/digitalocean/netbox/raw/develop/docs/netbox_logo.png)

![screenshot2](https://github.com/digitalocean/netbox/raw/develop/docs/media/screenshot2.png)

因为 IPv6 了?
)

- [machine-learning-surveys](https://github.com/metrofun/machine-learning-surveys)
    - 652 Stars, 71 Fork

A curated list of Machine Learning related surveys, overviews and books.

- [gain](https://github.com/gaojiuli/gain/)
    - 594 Stars, 29 Fork

Web crawling framework for everyone. Written with asyncio, uvloop and aiohttp. Everyone could write their own web crawler easily with gain framework. Gain framework provide a pretty simple api.

(`是也乎:`

> Python3.5+

)

- [proximityhash: Geohashes in proximity](https://github.com/ashwin711/proximityhash)
    - 56 Stars, 1 Fork

Geohash is a geocoding system invented by Gustavo Niemeyer and placed into the public domain. It is a hierarchical spatial data structure which subdivides space into buckets of grid shape, which is one of the many applications of what is known as a Z-order curve, and generally space-filling curves.

(`是也乎:`

![proximityhash](https://camo.githubusercontent.com/1bf7bb09633c0dffc704a0b86a68b901cfc0435a/68747470733a2f2f7261772e6769746875622e636f6d2f61736877696e3731312f70726f78696d697479686173682f6d61737465722f696d616765732f70726f78696d697479686173685f67656f726170746f722e706e67)

震中分析

)

- [six-char-max](https://github.com/petersn/six-char-max)
    - 45 Stars, 4 Fork

80 characters per line is waaaay too many. All Python programs should have at most six characters per line.

(`是也乎:`

将一切程序转换为每行只有6个字符的可用脚本,
一种通过扩展空间来进行混淆的技术...
)

- [Nodz](https://github.com/LeGoffLoic/Nodz)
    - 37 Stars, 17 Fork

Nodz : Visualize your data - Free nodes based graph generator.

(`是也乎:`

![Nodz](https://github.com/LeGoffLoic/Nodz/raw/master/nodz.png)

嗯哼?! Qt..
)

- [spark-deep-learning](https://github.com/databricks/spark-deep-learning)
    - 13 Stars, 4 Fork

Deep Learning Pipelines provides high-level APIs for scalable deep learning in Python. The library comes from Databricks and leverages Spark for its two strongest facets: In the spirit of Spark and Spark MLlib, it provides easy-to-use APIs that enable deep learning in very few lines of code. It uses Spark's powerful distributed engine to scale out deep learning on massive datasets.

(`是也乎:`

嗯哼, 热词合体...
)

- [coreml-scikit-example](https://github.com/mfpierre/coreml-scikit-example)
    - 11 Stars, 1 Fork

Apple CoreML example with scikit-learn

- [anyserv](https://github.com/rrajaravi/anyserv)
    - 4 Stars, 1 Fork

Get a full fake REST API with zero coding

(`是也乎:`

通过一个 JSON 声明来完成 RESTfull 接口的伪服务
)

- [proxy2](https://github.com/inaz2/proxy2)
    - 4 Stars, 1 Fork

HTTP/HTTPS proxy in a single python script

(`是也乎:`

单文件的代理器
)


- [Red-Black-Tree](https://github.com/Enether/Red-Black-Tree)
    - 1 Stars, 0 Fork

An extremely well tested and commented red black tree implementation. Worth a look if you are studying the material.

- [pydantic](https://pydantic-docs.helpmanual.io/)
    - 0 Stars, 0 Fork

Data validation and settings management using python 3.6 type hinting. Define how data should be in pure, canonical python; validate it with pydantic. 

(`是也乎:`

基于 Py3.6+ 的特性,实现的数据验证和设置管理
)


### (￣▽￣)

- [无我编程的十条戒律 | 湾区日报](https://wanqu.co/a/5177/2017-06-06-the-ten-commandments-of-egoless-programming.html?s=social)
    + zen,coder

这是 StackOverflow 联合创始人 Jeff Atwood 注释的十戒。程序员普遍有很强的 ego，都应该看看本文，打印下来时刻提醒自己：）

(`是也乎:`

![Ten Commandments of Egoless Programming](https://blog.codinghorror.com/content/images/uploads/2006/05/6a0120a85dcdae970b0120a86d5ea4970b-pi.jpg)

源自 71 年神书: [The Psychology of Computer Programming](https://www.amazon.com/exec/obidos/ASIN/0932633420?tag=wanquribao-20)

![银年纪念版](https://img3.doubanio.com/lpic/s28104646.jpg)

- 承认并接受你也会犯错
- 你不是你的代码
- 无论你有多少奇招, 别人都有更多
- 获得共识前不要重写代码(<-- 不是重构)
- 在尊重和耐心的前提下, 和菜鸟沟通
- 世上唯一不变的是变化 (即, PM 是自然现象)
- 真正的权威源自知识而不是立场 (呵呵...)
- 为你坚信的战斗, 但得优雅的接受失败
- 嫑作 "房间摆设" (悲惨工作三征兆:无闻/无关/不可测)
- 批评代码而不是人


> 软件的人性化原则 是永恒的

`(￣▽￣)` 可惜, 程序猿的边缘化也是永恒的...

)


# 是也乎

- 170608 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170608 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


