Title: 蠎加载 96
Slug: importpython-96
Date: 2016-10-28 11:11
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 96](http://importpython.com/newsletter/no/96/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [搜索所有过往文章 Import Python Newsletters. By Tag, Keywords, Issue No.](http://importpython.com/search/)
    + importpython

Hello Subscribers. If you ever want to find an article we curated and don't rememeber the issue ?. Or you want to find all articles based on a tag/topic e.g. admin panel, PEP etc. Head to http://importpython.com/search/ . Please let us know your feedback / Bug if any.

(`是也乎:`

蠎周刊快速积累到 96 期了,果断官方给出了关键词搜索服务
)

- [Python 的 iterators 和 iterables 需要相同嘛?!](https://medium.com/@adrian.hintermaier/python-iterators-and-iterables-need-not-be-the-same-5ba280e6514d#.i01eu9u4a)
    + iterator

So what are iterators and iterables, and are they distinct? They are distinct. Iterables are classes that implement the __iter__ method, a method which returns an iterator. Iterators are classes that implement the __next__ method (or next in Python 2), which continuously returns the next element until the end. So this begs the question, does an iterable also have to be an iterator? Or does an iterator also have to be an iterable?

(`是也乎:`

命名是艺术也是命运,一个再好的功能,名字起错了,
除了给人留下很多的口水仗机会,对开发只能是种心碍,还是人工的...
)

- [检查 Django 的所有迁移点.](https://medium.com/@kitsunde/checking-that-django-has-all-migrations-55a1c23c3a59#.jyuaskk5z)
    + django

All of our project are setup with continuous deployment on CircleCI. An occasional source of errors has been caused by missing model migrations because the migration wasn’t committed. There’s a simple solution by adding a migration check before deploying.

(`是也乎:`

随着 Django 的高速发展以及快速流传,
不兼容的升级行为也越来越艺术化,
得配合专门技艺...作死
)


- [你有哪些不常见的心爱 projects/notebooks/modules ?](https://www.reddit.com/r/Python/comments/59izbt/what_are_your_favorite_python/)
    + opensource project

Reddit Discussion where Python developers are sharing their favourite projects/modules. Lot of noise but found python-dependency-injector to be interesting.

(`是也乎:`

挂出来的日子不长,但是 [fuckit](https://github.com/ajalt/fuckitpy) 
的确值得体验...当然只是 linux/mac 党可以体验的了
)

- [PEP 531 -- Existence checking operators](https://www.python.org/dev/peps/pep-0531/)
    + PEP

Inspired by PEP 505 and the related discussions, this PEP proposes the addition of two new logical operators to Python: 

i) Existence-checking fallback: expr1 ?else expr2 

ii) Existence-checking precondition: expr1 ?and expr2. 

As well as the following abbreviations for common existence checking expressions and statements 

i) Existence-checking attribute access: `obj?.attr (for obj ?and obj.attr )`
ii) Existence-checking subscripting: `obj?[expr] (for obj ?and obj[expr] )` 
iii) Existence-checking assignment: `target ?= expr`

(`是也乎:`

受到动态的影响,运行时自省不足一定非常难受的,
所以,py 又接受了两种存在检验器
)


- [所有 Python 包都能预安装的在线 REPL 环境 -- Repl.it](https://repl.it/site/blog/python-import)
    + REPL

At Repl.it, our goal is to make programming more accessible, and as part of this we aim to provide the full power of popular programming environments with no setup time. And no modern programming language is complete without third-party packages. That's why today we're making every Python package ever immediately available on repl.it. Just select the language (Python or Python3) and start importing packages.

(`是也乎:`

将整个儿 PyPi 事先都加载到目录中的在线 REPL,
真心脑洞太大了...

问题是俺想基于这种零部署的环境,
发布私人应用呢!?

不过,真心是个好想法...

而且提供20+种开发语言的 REPL
)

- [Mike Driscoll: 用Python和GooPyCharts创建图形](http://www.blog.pythonlibrary.org/2016/10/26/creating-graphs-with-python-and-goopycharts/)
    + charts

I came across an interesting plotting library called GooPyCharts which is a Python wrapper for the Google Charts API. In this article, we will spend a few minutes learning how to use this interesting package.

- [改进和扩展 pip 的搜索功能](https://medium.com/@balazs.saros/improving-and-extending-the-search-functionality-of-pythons-pip-50d01a4a344f#.g6dmcbzbi)
    + pip

The main reason I’m in love with Python is the elegance and beauty of the design the language holds. Why not improve a bit on pip search to match the aesthetics? That’s why I created yip.

(`是也乎:`

已成痛点...
)

- [Python API 客户端和 Tapioca](http://www.vinta.com.br/blog/2016/python-api-clients-with-tapioca/)
    + opensource project, API

Tapioca is a Python API client maker. It gathers most of the features API clients implement and puts them in an extensible core. Wrappers will then extend this core implementing only the specifics from each service (such as authentication and pagination) and get all the common API client features for free. Tapioca approach also comes in handy because regardless of the service, clients look the same in the way you interact with them.


(`是也乎:`

Tapioca 是一个致力于彻底改变 API 开发模式的服务商,
具体点,就是想接管所有互联网 API 的发布...
)


- [如何编写你自己的 Python 文档生成器?](https://medium.com/@tryexceptpass/python-introspection-with-the-inspect-module-2c85d5aa5a48#.kekht2lym)
    + core python

Originating from the standard library, inspect not only lets you look at lower level python frame and code objects, it also provides a number of methods for examining modules and classes, helping you find the items that may be of interest. It’s what pydoc uses to generate the help files mentioned previously.

(`是也乎:`

给娇贵的 pydoc 生成可用文档的前置工具
)

- [使用 Python Mock 来折腾你的代码](https://medium.com/@raiderrobert/using-python-mock-in-unusual-ways-7b56fdaab319#.yc16sj4x4)
    + mock

I want to share 2 specific use cases that I recently encountered. 

Case 1: Testing without calling a REST/SOAP API and 

Case 2: Pretend that you have imported a library. 

(`是也乎:`

很有脑洞的案例分享
)

## 活动
    ~ Upcoming Conference / User Group Meet

- ??? 进入冬歇期了?

## 项目
~ 包/模块/库/片段...



- [is-service-up](https://github.com/marcopaz/is-service-up)
    - 84 Stars, 6 Fork

IsServiceUp helps you monitor all the cloud services you rely on in a single web page. You can customize it with the services you want to monitor and host it on your own server.

(`是也乎:`

云服务用的多了也麻烦,这下有个单一页面可以同时监察所有涉及服务的状态了
)

- [CNN-Sentence-Classifier](https://github.com/shagunsodhani/CNN-Sentence-Classifier)
    - 25 Stars, 7 Fork

简化实现 “卷积神经网络的句子分类”论文


- [verify-email](https://github.com/teknotus/verify-email)
    - 6 Stars, 2 Fork

用于检查DKIM的工具 - 在电子表格中签名许多电子邮件和报告结果


- [wagtailmodelchooser](https://github.com/takeflight/wagtailmodelchooser)
    - 2 Stars, 0 Fork

Model choosers for Wagtail admin. A plugin for Wagtail that provides a ModelChooserPanel and ModelChooserBlock for arbitrary models. 


# 是也乎

- 161028 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161028 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


