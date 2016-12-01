Title: 蠎加载 100
Slug: importpython-100
Date: 2016-11-23 13:31
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 100](http://importpython.com/newsletter/no/100/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [蠎加载百期知识竞赛](http://importpython.com/newsletter/quiz/)
    + importpython

It's been 2 years of curating ImportPython and today is the 100th Issue. Wow. What a moment ?. Here is a python quiz competition. Five random() participants who answer all questions correctly win complete bundle of Writing Idiomatic python book by Jeff Knupp. If you take the quiz at the end of it is a link with discount too. This quiz is an our attempt at having fun and saying thanks to all you readers of ImportPython. Do take to twitter with the hashtag #importpython100 happy to hear what you have to say.

(`是也乎:`
追查了一下, `2014-09-25` 开始快译 [蠎加载](http://weekly.pychina.org/importpython/index.html) 的, 
嗯哼,`2012-02-17` 开始翻译 [蠎周刊](http://weekly.pychina.org/issue/index.html) 的,
当然 蠎周刊 之前有朋友翻译过前20期,俺是从 77 期开始坚持翻译到 200期,引人了新的快译小伙伴,老高,
然后,重心转移到 蠎加载;
风格也从之前正文的翻译,慢慢变成了主要进行 `是也乎` 的点评;
不变的是很少有人提交 PR,想来也是因为这种周刊,实在只是个定时 技术新闻点收集,
时效性太强,大家参与进来,并不能获得类似伟大的 `字幕组` 那种可以长期流传,洗脑天下的乐趣.
之于俺和小伙伴,最大的收获的确也就是:

- 定期翻译,形成周自学节奏
- 了解 Python 领域的主流变化
- 积累 Python 技术演化趋势概念
- 架构选型时帮助扩大思考范围
- ...

简单的说,定期快译一个技术新闻周刊,是种非常好的强迫自学的形式;
并不特别强烈的建议大家都来加入这种自学,毕竟太散了...
但是,的确是一个有效无意识提高领域技术语感的好形式.


)

- [MLAlgorithms](https://github.com/rushter/MLAlgorithms)
    + machine learning, algorithms

Minimal and clean examples of machine learning algorithms


- [用 pip 从 github 安装 Python 模块](https://medium.com/@lynzt/install-python-packages-from-github-5866d234c4e4)
    + pip, github

`pip install --upgrade git+git://github.com/user/user_repository.git` and you are done.

(`是也乎:`

现代语言生态的标志行为:加载 github 
)

- [迭代器和生成器](https://medium.com/the-python-corner/iterators-and-generators-in-python-2c3929a144b?source=rss------python-5)
    + core-python

Simple code snippets showing how iterators and generators work in Python.


- [Patrick Kennedy: Flask 应用的单元测试](http://www.patricksoftwareblog.com/unit-testing-a-flask-application/)
    + testing, flask

This blog post provides an introduction to unit testing a Flask application. I’ve been on a big unit testing kick at work recently which is spilling over into updating the unit tests for my personal projects. Therefore, I thought it would be a good time to document the basics of unit testing a Flask application.

(`是也乎:`

是的 Flask 的单元测试生态并没有兴起...
)

- [DigitalOcean 中 Tensorflow 的 Python 支持](https://www.garysieling.com/blog/tensorflow-python-setup-digitalocean)
    + tensorflow, digitalocean

The following steps will install TensorFlow1 on a fresh Digital Ocean virtual machine running Ubuntu.


(`是也乎:`

数字海洋是唯一一个 AWS/GCP 之外最有成功相的 `*aaS` 厂商了
)

- [用 Pandas 构建财务模型 - By Chris Moffitt](http://pbpython.com/amortization-model.html)
    + pandas

This specific post will discuss how to do financial modeling in pandas instead of Excel. For this example, I will build a simple amortization table in pandas and show how to model various outcomes.

(`是也乎:`

谁说社科生不玩程序的?! 这在经济领域现在是必须的强项了...
)

- [定义过滤器和有序字典](http://www.snowboardingcoder.com/django/?p=54)
    + django, python3

This week I ran into a minor problem that took a surprising amount of time to resolve. Getting a Django template to produce a dict in sorted order. While there were answers out there, none seemed to match the environment that I am using (python 3, Django 1.10). After some experimentation, I finally came up with what I think is a good solution.

(`是也乎:`

Django 中的模板看起来什么都能作,其实...
)

- [使用 BeautifulSoup 的 Web Scraping 教程](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
    + beautifulsoup

In this tutorial, we’ll show you how to perform web scraping using Python 3 and the BeautifulSoup library. We’ll be scraping weather forecasts from the National Weather Service, and then analyzing them using the Pandas library.

(`是也乎:`

国家天气局的数据抓取整理后给 美汤 分析.
)


- [在 Python 中构建动画 GIFs](http://tabletopwhale.com/2016/11/14/automated-color-palettes.html)
    + gif

I first wrote a Python script to make a GIF illustration for any 5-unit color scheme.

(`是也乎:`

![GIFs](http://tabletopwhale.com/img/colorpalette/29.gif)
)

- [如何通过 Pynini 在 Python 中获得卓越的文本分析能力 ?](https://www.oreilly.com/ideas/how-to-get-superior-text-processing-in-python-with-pynini)
    + regex

Regular expressions are the standard for string processing, but did you know you can often get better text untangling with Pynini's finite-state transducers ?

(`是也乎:`

利用 Pynini 的有限状态机来替代正则表达式来处理文本.
)


- [CPython 内存管理](https://medium.com/python-pandemonium/cpython-memory-management-479e6cd86c9#.fdfvkwki9)
    + cpython

This post is high level description of how CPython (just Python below) manages object life cycle.


(`是也乎:`

在冯机框架之内, 执行效率总是得面对内存这一物理结构的额外问题
)

- [针对 Python 3 的案例](https://learnpythonthehardway.org/book/nopython3.html)
    + python3

"There is high probability that Python 3 is such a failure it will kill Python" - Zed Shaw. As Curator of a Python Newsletter for 2+ years I can tell you at-least 20-30% of all articles I read of late have code written only for Python 3. Just recently I was at Pycon India and met lot of student who never wrote a single line in 2.x. Startup founders starting with new development choosing Python 3. Lot of people are sleeping on Python 3. A year more and hopefully everyone will be awake.

(`是也乎:`

全球只有印度沉浸在 Py 3 的世界中..嗯哼,为什么?!

何况 Py 3 不是图灵完备的...
)


- [用 Python 进行研究 - 哈佛大学课程 - edx](https://www.edx.org/course/using-python-research-harvardx-ph526x)
    + course, mooc

Take your introductory knowledge of Python programming to the next level and learn how to use Python 3 for your research. You will learn Python 3 programming basics, Python tools (e.g., NumPy and SciPy modules) for research applications, How to apply Python research tools in practical settings.


(`是也乎:`

介绍学界在 py 3 生态中如何进行研究
)

- [在 Django 网站上水印图像](http://www.machinalis.com/blog/watermarking-images-django/)
    + pillow, watermarking

Have you ever noticed how stock photography sites add watermarks to the images shown on their catalogs ? They do that to make sure people don’t just take the free samples and use them without proper licensing. Turns out this is pretty easy to do it with Pillow.

- [元编程和 Django - 使用 Decorators](http://www.vinta.com.br/blog/2016/metaprogramming-and-django-using-decorators/)
    + django, decorators

The article starts of with an introduction snippet to decorators and then goes on to explore some real world examples in context of Django. Personally one good find in the article was boltons library.

- [JIRA 软件](https://goo.gl/NGmw3L)
    + Sponsor

Start a free JIRA Software trial and get this shirt.

(`是也乎:`

收购 bitbucekt.org 的靠谱软件管理开发商.
)



## 好物
~ 包/模块/库/片段...


- [pipfile](https://github.com/pypa/pipfile) 
    + 1187 Stars, 24 Fork

A Pipfile, and its related Pipfile.lock, are a new (and much better!) replacement for pip's requirements.txt files.

(`是也乎:`


又一个 `requirements.txt` 的替代品
)

- [greendots](https://github.com/joewalnes/greendots)
    - 56 Stars, 4 Fork

Write with those green dots on your GitHub profile. This takes a message, encodes it to a simple bitmap font, and generates a bunch of git commits in the past.

(`是也乎:`

![greendots](![Example profile](https://github.com/joewalnes/greendots/blob/master/example.png))
)

- [Algorithms-and-Data-Structures](https://github.com/juliascript/Algorithms-and-Data-Structures)
    - 14 Stars, 0 Fork

A Trie, (also known as a prefix tree) is a special type of tree used to store associative data structures. A trie (pronounced try) gets its name from retrieval?—?its structure makes it a stellar matching algorithm. Repository for the article https://medium.com/algorithms/trie-prefix-tree-algorithm-ee7ab3fe3413#.e5281rxmo

(`是也乎:`

前缀树之类的数据结构和算法的折腾
)

- [financial-life](https://github.com/MartinPyka/financial_life)
    - 1 Stars, 0 Fork

financial_life is an opinionated framework written in Python that allows to simulate monetary flows between different types of accounts. These simulations allow a deeper understanding of financial plans and a better comparison of financial products (in particular loan conditions) for personal circumstances. With financial_life you can

(`是也乎:`

`financial_life` 是 Python 构建的模拟不同类型帐户货币流动的框架,
用以进行金融产品的设计实验...

)


- [flask-djcelery](https://github.com/waqasjaved160/flask-djcelery)
    - 1 Stars, 0 Fork

An example project for configuring Djcelery with Flask application and dynamically changing tasks via REST API and through django admin. 

(`是也乎:`

自动打通 Falsk 和 Django 应用的框架.
)




# 是也乎
~ (￣▽￣) 这么快就100期了?!

- [The End Of Coder Influence \| Zed A\. Shaw](https://zedshaw.com/2016/11/24/the-end-of-coder-influence/)

(`嗯哼:`

这真是一个悲哀的故事...
)

- 161123 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161123 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


