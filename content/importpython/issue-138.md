Title: 蠎加载 138
Slug: importpython-138
Date: 2017-08-19 19:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 138](http://importpython.com/newsletter/no/138/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [单元测试和模块 unittest](https://www.youtube.com/watch?v=6tNS--WetLI)
    + video

In this Python Programming Tutorial, we will be learning how to unit-test our code using the unittest module. Unit testing will allow you to be more comfortable with refactoring and knowing whether or not your updates broke any of your existing code. Unit testing is a must on any large projects and is used by all major companies. Not only that, but it will greatly improve your personal code as well. Let's get started.

(`是也乎:`

叕一个 TDD 方面的嗯哼了...

)


- [Python 线程 - Multithreading Playlist](https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm)
    + videos, multithreading

- [数据科学 Rosetta Stone: 分类 在 Python, R, MATLAB, SAS, 以及 Julia | Heaton Research](http://www.heatonresearch.com/2017/08/17/ds_rosetta_stone.html)
    + data science

- [自动将 Python 2 代码翻译成 3 的](http://pythonconverter.com/)
    + Python 3

This web is a online converter that reads Python 2.x source code and applies a series of fixers to transform it into valid Python 3.x code Enter your Python2 code on the left, hit the button, and boom, Python3 code on the right

(`是也乎:`

可以嘛?敢用嘛?
)


- [Python 队列死锁的悲伤故事](https://codewithoutrules.com/2017/08/16/concurrency-python/)
    + concurrency

This is a story about how very difficult it is to build concurrent programs. It’s also a story about a bug in Python’s Queue class, a class which happens to be the easiest way to make concurrency simple in Python. This is not a happy story: this is a tragedy, a story of deadlocks and despair.


- [如何在 Python 领域成为专家?](https://nbviewer.jupyter.org/github/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb)
    + core-python

Notebook based off James Powell's talk at PyData 2017.

(`是也乎:`

配合 youtube 的一则 ipynb 分享,
metaclasses 开始...

)

- [仔细看看 Python f-strings 如何工作](https://medium.com/@skabbass1/a-closer-look-at-how-python-f-strings-work-f197736b3bdb)
    + f-strings

F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

(`是也乎:`

针对 [PEP 498](https://www.python.org/dev/peps/pep-0498/) 的嗯哼
)

- [谁负责维护 PyPI 以及负责?](https://www.reddit.com/r/Python/comments/6ug04h/who_maintains_pypi_and_where_and_by_whom_is_it/)
    + pypi

Reddit Discussion


- [Hy 的小小一步 - 我的 lispy Python 经验](http://www.modernemacs.com/post/mile-hy/)
    + lisp

Roughly, Hy is to Python as Clojure is to Java. Hy completely inter-ops with Python. I've hit commit 1,500 in my Hy project at work. I wanted to share my experience working with Hy, where I feel it shines and where it falls short.

(`是也乎:`

等等-> Clojure LISP?!

![XKCD](https://camo.githubusercontent.com/2ea3c517525377dbb66d22c6e27dd2334af4731e/68747470733a2f2f7261772e6769746875622e636f6d2f68796c616e672f73687974652f313866363932356530383638346230653166353262326363326338303339383963643632636439312f696d67732f786b63642e706e67)

叕一个为了 LISP 的方言, py 造...

    #! /usr/bin/env hy
    (print "I was going to code in Python syntax, but then I got Hy.")

意思是可以用 Python 来学习 Scheme 了?!


![hy-logo](http://docs.hylang.org/en/stable/_images/hy-logo-small.png)


)


- [Python 和 Haskell 中的左右折叠->原始递归模式](http://eli.thegreenplace.net/2017/right-and-left-folds-primitive-recursion-patterns-in-python-and-haskell/)
    + haskell

A "fold" is a fundamental primitive in defining operations on data structures; it's particularly important in functional languages where recursion is the default tool to express repetition. In this article I'll present how left and right folds work and how they map to some fundamental recursive patterns. The article starts with Python, which should be (or at least look) familiar to most programmers. It then switches to Haskell for a discussion of more advanced topics like the connection between folding and laziness, as well as monoids.

(`是也乎:`

等等? Haskell ?!

![productrecursionpattern](http://eli.thegreenplace.net/images/2017/productrecursionpattern.png)

)


- [用 Python 分析和测试 C](https://jamesroutley.co.uk/tech/2017/08/16/analyse-test-c-with-python.html)
    + c-code

C is relatively difficult to write, making it harder to analyse and test. It would be helpful to be able to do this with a higher level language, such as Python. Analysis and testing don’t affect performance of the actual data structure, so using a slower but easier and more productive language for this seems reasonable. In this article, we walk though a simple example of doing this with a built-in Python library for interfacing with C called ctypes.


- [在 Python 中使用 GDAL / OGR 对地址进行地理编码和执行点多边形测试](https://datascience.blog.wzb.eu/2017/08/11/geocoding-an-address-and-performing-point-polygon-tests-with-gdalogr-in-python/)
    + geo

This short post shows how to use Python packages googlemaps and GDAL.


- [Debugging 在 Python](https://www.codementor.io/gbozee/debugging-in-python-9ia7lof32)
    + debugging

One of the reasons why I love the Python programming language is because of how easy debugging is. You don't need a full blown IDE to be able to debug your Python application. We will go through the process of debugging a simple Python script using the pdb module from the Python standard library, which comes with most installation of Python.

(`是也乎:`

叕一个 debug 的经验分享,
只是 `print()` 可以解决 99% 情况时,有什么新动力要用...

)

- [引入新的图像注释类型 - Python 代码片段](https://blog.scaleapi.com/introducing-new-image-annotation-types-47b0b482b7c2)
    + image processing

We’re excited to be launching a bunch of new annotation types for images. Since the launch of our bounding box API, we’ve annotated millions of images with boxes to identify a host of different objects, from cars and hats to roof damage and parking lots. Scale is becoming an industry-standard tool for solving computer vision problems.


- [用 lehar 在终端展示数据](https://medium.com/@darxtrix/visualizing-data-in-terminal-using-lehar-7cfded09c1ad)
    + visualization

The post is about a terminal visualization tool lehar that is open sourced at https://github.com/darxtrix/lehar


(`是也乎:`


Find commits by authors in a git repo

    $ git shortlog -s | cut -f1 | lehar
    ▇▁▁▁▁▁▁▂▃▁▁█▁▁▂▃▅▁▁▁▂▆▁▁▁▂▁▁▁▁▂▇▁▅▆▁▁▁▄▁▁█▁▁▂▁▂▁

还有这种操作?!
)


- [Select & Prefetch Related](https://medium.com/@lucasmagnum/djangotip-select-prefetch-related-e76b683aa457)
    + django

Today the `#DjangoTip` will be about using select_related and prefetch_related to improve our queries performance. Note - Django developer do check out django newsletter - http://djangoweekly.com






## 好物
~ 包/模块/库/片段...



- [jsonschema2db](https://github.com/better/jsonschema2db)
    - 28 Stars, 3 Fork

Service objects for Django

(`是也乎:`

还有这种操作需求?!

    jsonschema2db-test=# select * from schm.root;
    -[ RECORD 1 ]------------------------+-----------
    id                                   | 1
    loan_file_id                         | 1000000000
    prefix                               |
    loan__amount                         | 500000
    subject_property__acreage            | 42
    subject_property__address__latitude  | 43
    subject_property__address__longitude |
    subject_property__address_id         | 1

)

- [jsonschema2db](https://github.com/better/jsonschema2db)
    - 22 Stars, 0 Fork

Generate tables dynamically from a JSON Schema and insert data.



- [np-to-tf-embeddings-visualiser](https://github.com/nlml/np-to-tf-embeddings-visualiser)
    - 19 Stars, 3 Fork

Quick function to go from a dictionary of sets of (images, labels, feature vectors) to checkpoints that can be opened in Tensorboard.

(`是也乎:`

名字非常走心的工具.

TF 工具的工具...
)


- [smspushtx](https://github.com/prusnak/smspushtx)
    - 16 Stars, 1 Fork

Simple PushTX server to push Bitcoin transactions via SMS.

(`是也乎:`

在 5G 时代用 2G 进行交易...只能说 区块链的生命是嗯哼的
)


- [yamdl](https://github.com/andrewgodwin/yamdl)
    - 15 Stars, 1 Fork

ORM-queryable YAML fixtures for Django.



- [BookBot](https://github.com/RoberTnf/BookBot)
    - 13 Stars, 0 Fork

Reddit book bot.

(`是也乎:`

叕叕一个 bot

)

- [contract](https://github.com/osantana/contract)
    - 4 Stars, 0 Fork

Create API contracts using Python.

(`是也乎:`

叕一个 RESTful 包装工具
)


- [slick](https://github.com/pybee/slick)
    - 3 Stars, 0 Fork

A native web-based client for Slack.

(`是也乎:`

叕一个 Slack 周边工具..

)


- [PyPocketExplore](https://github.com/Florents-Tselai/PyPocketExplore)
    - 1 Stars, 0 Fork

PyPocketExplore is a CLI-based and web-based API to access Pocket Explore data. It can be used to collect data about the most popular Pocket items for different topics. 


(`是也乎:`

叕一个 Pocket 公开数据工具...
)




### (￣▽￣)

- PyConChina2017 议题征集开始
    + 申报表单: https://jinshuju.net/f/2ag6QB

中国的PyCon大会已经组织了6年，在第7年PyCon大会之际，Python3已经成熟，比如Instagram迁移到了Python3。而人工智能方兴未艾，区块链、物联网、AR、VR、机器人等领域创新不断涌现。

本大会以“大数据和人工智能技术的创新应用”为主题，将由丰富的内容和议题组成，着重探讨如何使用Python技术进行大数据和人工智能的技术开发和最佳实践，并结合具体的产品和行业发展趋势，分享不同类型的应用、场景下的开发和运营经验。

...

今年PyConChina2017将在两个城市举办，上海是9月23日举办

- 上海（约400人参加），预计7个主题演讲（每个40分钟），7个快速演讲（每个10分钟）。
- 杭州（约200人参加），预计7个主题演讲（每个40分钟）

(`是也乎:`

结果立即在 CPyUG 列表中引发了各种嗯哼,
并有行者组织了议题问卷, 得到稍有不同的期待,
所以, 大会的举行真心得看坚持了.
)

## 是也乎

- 170819 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170819 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


