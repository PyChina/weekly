Title: 蠎加载 153
Slug: importpython-153
Date: 2017-12-02 23:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 153](http://importpython.com/newsletter/no/153/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Awesome python talks](https://github.com/jhermann/awesome-python-talks)
    + videos

An opinionated list of awesome videos related to Python, with a focus on training and gaining hands-on experience.

(`是也乎:`

没有中文分享...
)


- [对象模型](https://eev.ee/blog/2017/11/28/object-models/)
    + core-python, oops

Here, then, is a (very) brief run through the inner workings of objects in four very dynamic languages. I don’t think I really appreciated objects until I’d spent some time with Python, and I hope this can help someone else whet their own appetite.



- [用于数据分析的Python - 关键性逐行回顾](https://medium.com/dunder-data/python-for-data-analysis-a-critical-line-by-line-review-5d5678a4c203)
    + pandas

A not so nice review of Python for Data Analysis Book

(`是也乎:`

最怕逐行解释的图书了...
)


- [Python软件基金会新闻: PSF 从 Mozilla 开放源代码项目中获得 $ 170,000 赠款，以提高 PyPI 的可持续性](https://pyfound.blogspot.ae/2017/11/the-psf-awarded-moss-grant-pypi.html)
    + PSF, mozilla

Today we are excited to announce that we have applied for, and been awarded, a grant to help improve the sustainability of the Python Package Index in the amount of $170,000.  This has been awarded by Mozilla, through the Foundational Technology track of their Open Source Support Program.  We would like to thank Mozilla for their support.

(`是也乎:`

细思恐极...mozilla?
)


- [免费 Apache Spark™ 指南](http://4url.in/20ONEZPb/)
    + ebook, advert, free

The Definitive Guide to Apache Spark. Download today!

(`是也乎:`

这种广告越多越好
)


- [使用 Python 的 Pathlib 模块 - 实用商用 Python](http://pbpython.com/pathlib-intro.html)
    + pathlib

The pathlib module was first included in python 3.4 and has been enhanced in each of the subsequent releases. Pathlib is an object oriented interface to the filesystem and provides a more intuitive method to interact with the filesystem in a platform agnostic and pythonic manner. I recently had a small project where I decided to use pathlib combined with pandas to sort and manage thousands of files in a nested directory structure. Once it all clicked, I really appreciated the capabilities that pathlib provided and will definitely use it in projects going forward. That project is the inspiration for this post.

(`是也乎:`

最常用, 也最无奈的一个模块, 特别是遇到中文...
)


- [使用 NLTK 可视化 我最爱 专辑的歌词](https://medium.com/@chekos/using-nltk-to-visualize-my-favorite-albums-lyrics-e1044ee39b6c)
    + NLTK

A few weeks ago I was enrolled in Python for Data Science by UCSD on EdX.org. It is an introductory course so it starts with the basics but by the end of it you have worked with Twitter’s API, predicted weather using Machine Learning and even done some Natural Language Processing using NLTK.

(`是也乎:`

前提是 lyrics 的语种都兼容吧?
果然和中文歌曲没什么关系

)


- [python cheat sheet](https://medium.com/@ka666wang/python-cheat-sheet-2455a2634b31)
    + core-python

- [pypika](https://github.com/kayak/pypika)
    + sql

PyPika is a Python API for building SQL queries. The motivation behind PyPika is to provide a simple interface for building SQL queries without limiting the flexibility of handwritten SQL. Designed with data analysis in mind, PyPika leverages the builder design pattern to construct queries to avoid messy string formatting and concatenation. It is also easily extended to take full advantage of specific features of SQL database vendors.

(`是也乎:`

可以说叕一个 SQL 的 Py DSL
)




## 好物
~ 包/模块/库/片段...


- [deep-image-prior](https://github.com/DmitryUlyanov/deep-image-prior)
    - 856 Stars, 70 Fork

Image restoration with neural networks but without learning.

(`是也乎:`

![teaser_compiled](https://github.com/DmitryUlyanov/deep-image-prior/raw/master/data/teaser_compiled.png)

非学习图像处理模块

)


- [the-endorser](https://github.com/eth0izzle/the-endorser)
    - 77 Stars, 12 Fork

An OSINT tool that allows you to draw out relationships between people on LinkedIn via endorsements/skills.

(`是也乎:`

![endorser](https://raw.githubusercontent.com/eth0izzle/the-endorser/master/example/example.png)

对 LinkedIn 的技能数据可视化
可惜...

)

- [WPSploit](https://github.com/m4ll0k/WPSploit)
    - 36 Stars, 9 Fork

WordPress Plugin Security Testing.

(`是也乎`

细思恐极, 这是 PHP 和 Py 合流的先兆?
)


- [progrmoiz/python-snippets](https://github.com/progrmoiz/python-snippets)
    - 17 Stars, 0 Fork

The most useful python snippets.

(`是也乎:`

叕叕叕一个 代码片段仓库,偏向 对象自省的加强

)


- [selectolax](https://github.com/rushter/selectolax)
    - 12 Stars, 0 Fork

Python bindings to Modest engine (fast HTML5 parser with CSS selectors).

- [speeed](https://github.com/XenGi/speeed)
    - 11 Stars, 0 Fork

Ping like tool that measures packet speed instead of response time.

(`是也乎:`

ping-样, AWS-样, cURL-样....

太多软件一诞生就几乎完美, 逼的后来人只能全力兼容

![demo](https://github.com/XenGi/speeed/raw/master/demo.gif)


只是这么发数据包, 不怕当成 DDOS?
)


- [pytudes](https://github.com/norvig/pytudes)
    - 4 Stars, 0 Fork

Python programs to practice or demonstrate skills.

(`是也乎:`

叕叕叒一个 `实用` 技巧集锦

)


- [datasette](https://github.com/simonw/datasette)
    - 0 Stars, 0 Fork

An instant JSON API for your SQLite databases.

(`是也乎:`

思路清奇, 不改变 SQLite 行为,只通过 I/O 来改变 DB 的应用领域
)


- [cidr-house-rules](https://github.com/trulia/cidr-house-rules)
    - 0 Stars, 0 Fork

A lightweight API and collection system to centralize important AWS resource information across multiple accounts in near-realtime.

(`是也乎:`

![cidr](https://user-images.githubusercontent.com/538171/33504603-eb6a71d6-d69c-11e7-9a54-5f2d8ad95f8a.png)

叕叕叕一个 AWS 实用工具

)


- [fireant](https://github.com/kayak/fireant)
    - 0 Stars, 0 Fork

fireant is a a data analysis tool used for quickly building charts, tables, reports, and dashboards. It defines a schema for configuring metrics and dimensions which removes most of the leg work of writing queries and formatting charts. fireant even works great with Jupyter notebooks and in the Python shell providing quick and easy access to your data. 


(`是也乎:`

针对 Jupyter 平台的图表工具,
火蚁...名字不错

)

### (￣▽￣)

- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

关键响应非常敏捷, 10.1 长徦期间嗯哼了一下, 立即追加了两个功能:
[pyheatmap/test.py at 31d80c89529e194e743e3125d56a189712186c55 · oldj/pyheatmap](https://github.com/oldj/pyheatmap/blob/31d80c89529e194e743e3125d56a189712186c55/examples/test.py#L49)

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)


## 是也乎

- 171202 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171202 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


