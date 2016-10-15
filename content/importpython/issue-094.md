Title: 蠎加载 94
Slug: importpython-94
Date: 2016-10-14 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 94](http://importpython.com/newsletter/no/94/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [介绍 Djaneiro, 专注 Django 开发的 Sublime Text 插件.](https://goo.gl/U8RbN5)
    + django, sublime

In this review I’ll explain how Djaneiro can make your Django development workflow more productive and I’ll go over the pros and cons of the plugin as I experienced them. After that I’ll take a look at alternatives to Djaneiro in the Sublime Text plugin landscape. At the end I’ll share my final verdict and ratings.

(`是也乎:`

Djaneiro ~ 专门为 subl 用户打造的 django 环境...
由于出色的接口, subl 现在比 eclipes 当年的插件社区还要活跃...
)

- [PyData DC 2016 --5种 Python 函式](https://slott56.github.io/five-kinds-of-python-functions/assets/player/KeynoteDHTMLPlayer.html)
    + core python

Talk by Steven F. Lott.

- [Python AST 探险家](https://python-ast-explorer.com/)
    + AST

Write Python code and see how the ast looks like in the browser right now. No installation needed.

(`是也乎:`

在线实时代码编译结构观察服务
)

- [Python 作弊条](https://www.pythonsheets.com/)
    + resource

This project tries to provide a lot of piece of Python code that makes life easier.

(`是也乎:`

其实就是 mini 版本的 Python Cookbook

使用 virtualenv 发布本地文档网站

)

- [pandasql: 让 Python 讲 SQL](http://blog.yhat.com/posts/pandasql-intro.html)
    + sql

pandasql, a Python package we (Yhat) wrote that emulates the R package sqldf. It's a small but mighty library comprised of just 358 lines of code. The idea of pandasql is to make Python speak SQL. For those of you who come from a SQL-first background or still "think in SQL", pandasql is a nice way to take advantage of the strengths of both languages.

(`是也乎:`

![pandasql](http://blog.yhat.com/static/img/meat-and-birth.png)

作为 Rodeo IDE 插件诚意之作;
只有 358 行代码!

)


- [用来学习二叉树的 Python 库](https://github.com/joowani/binarytree)
    + opensource project

BinaryTree is a minimal Python library which provides you with a simple API to generate, visualize and inspect binary trees so you can skip the tedious work of mocking up test trees, and dive right into practising your algorithms! Heaps and BSTs (binary search trees) are also supported.


- [Patat – 又一个终端上的幻灯工具,基于 Pandoc](https://github.com/jaspervdj/patat)
    + opensource project

patat (Presentations And The ANSI Terminal) is a small tool that allows you to show presentations using only an ANSI terminal. It does not require ncurses.

(`是也乎:`

![patat](https://github.com/jaspervdj/patat/raw/master/extra/screenshot.png)

)

- [PyCon 2017 网站已上线](https://us.pycon.org/2017/)
    + pycon

PyCon 2017 ( US ) site is live. Note - Registration starts on Oct 17th. If you are looking to speak/attend reach out dates for talk/tutorial/paper aka Call For Proposals ( CFP ) submission.

- [异步 Python: 不同机制的并发 - By Abu Ashraf Masnun](http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/)
    + concurrency

In this post we shall explore the different ways we can achieve concurrency and the benefits/drawbacks of them. With the advent of Python 3 the way we’re hearing a lot of buzz about “async” and “concurrency”, one might simply assume that Python recently introduced these concepts/capabilities. But that would be quite far from the truth. We have had async and concurrent operations for quite some times now. Also many beginners may think that asyncio is the only/best way to do async/concurrent operations.

- [功能性 Python](http://feedproxy.google.com/~r/activestate/blog/~3/FiDE6pnNy7E/functional-python)
    + core python

Functional programming is a discipline, not a language feature. It is supported by a wide variety of languages, although those languages can make it more or less difficult to practice the discipline. Python has a number of features that support functional programming, including map/reduce functions, partial application, and decorators.

(`是也乎:`

功能性编程,而不是函式编程,又一门新的编程学科...

)

- [Python 旋风之旅](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/9GFa-FsUNv8/a-whirlwind-tour-of-python)
    + python3

Jake VanderPlas explains Python’s essential syntax and semantics, built-in data types and structures, function definitions, control flow statements, and more, using Python 3 syntax.

(`是也乎:`

针对 Py3 新用户的简介
)

- [介绍 Python 图像库 / Pillow](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/fID79q60JzQ/)
    + pillow

The Python Imaging Library or PIL allowed you to do image processing in Python. Here is a tutorial.

(`是也乎:`

瞌睡送枕头,对于图像处理,现在都用 Pillow 了
)

- [用 Python 如何构造图像间的差异](http://www.blog.pythonlibrary.org/2016/10/11/how-to-create-a-diff-of-an-image-in-python)
    + image processing, pillow

For the past couple of years, I’ve been writing automated tests for my employer. One of the many types of tests that I do is comparing how an application draws. Does it draw the same way every single time? If not, then we have a serious problem. An easy way to check that it draws the same each time is to take a screenshot and then compare it to future versions of the same drawing when the application gets updated.

- [获得 Python 模块的所有属性名称和类型](http://code.activestate.com/recipes/580705-get-names-and-types-of-all-attributes-of-a-python-/)
    + code snippet

This recipe shows how to get the names and types of all the attributes of a Python module. This can be useful when exploring new modules (either built-in or third-party), because attributes are mostly a) data elements or b) functions or methods, and for either of those, you would like to know the type of the attribute, so that, if it is a data element, you can print it, and if it is a function or method, you can print its docstring to get brief help on its arguments, processsing and outputs or return values, as a way of learning how to use it. 

(`是也乎:`

也只有 Python 这种有足够内省能力的语言,才可以随时拷问出这么丰富的信息来;
代码来自:

http://jugad2.blogspot.in/2016/10/get-names-and-types-of-python-modules.html
)

## 活动
    ~ Upcoming Conference / User Group Meet

- [Python Northwest](http://pynw.org.uk/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon HK 2016](http://pycon.hk/2016) ![pyconhk](http://pycon.hk/2016/images/pyconhk-logo.jpg)
- [PyCon Finland 2016](http://fi.pycon.org/2016/)
- [PyCon Ireland 2016](https://python.ie/pycon-2016/)
- [PyCon Canada 2016](https://2016.pycon.ca/)
- 


## 项目
~ 包/模块/库/片段...


- [RocketFuelPython](https://github.com/sahilshekhawat/RocketFuelPython)
    - 8 Stars, 0 Fork

RocketFuel 拓扑映射引擎的Python实现

- [testssl.sh-masscan](https://github.com/TKCERT/testssl.sh-masscan)
    - 7 Stars, 0 Fork

Make TLS/SSL security mass scans with testssl.sh and import results into ElasticSearch. Script collection for generating testssl.sh command lines that can be executed sequentially or in parallel with tools like GNU Parallel and importing the results into a structured document in ElasticSearch for further analysis.

(`是也乎:`

安全测试的各种结果自动导入 ElasticSearch 的 CLI 工具
)

- [RacketCallGraph](https://github.com/pollow/RacketCallGraph)
    - 7 Stars, 2 Fork

A simple Python script that generate Call Graph of simple Racket program by generating dot language scripts. It uses naive approach that basically traverse the program and maintain a state machine regardless of context. Currently it only maintain a FSM so advance features of Racket, like lambda-function is not support, will improve if needed in the future.

(`是也乎:`

又一个程序运行可视化解析工具
)

- [gender_classification_challenge](https://github.com/llSourcell/gender_classification_challenge)
    - 5 Stars, 7 Fork

Gender Classification Challenge for 'Learn Python for Data Science #1'. This is the code for the gender classification challenge for 'Learn Python for Data Science #1' by @Sirajology on YouTube. The code uses the scikit-learn machine learning library to train a decision tree on a small dataset of body metrics (height, width, and shoe size) labeled male or female. Then we can predict the gender of someone given a novel set of body metrics.

(`是也乎:`

猜性别挑战赛又一实例, 通过对人体数据进行机械学习来判定男女.
)

- [second_2016_presidential_debate_twitter](https://github.com/chrisalbon/second_2016_presidential_debate_twitter)
    - 4 Stars, 0 Fork

tweets from the the second presidential debate. This repo contains data on roughly 150,000 debate tweets. However, to make the data compliant with Twitter's terms of service, the public data only contains tweet IDs. A short python script to convert that list of tweet IDs into the full twitter data is coming soon.

(`是也乎:`

米国总统竟选第二次辩论时所有有关 tweets 数据集,
可以用来预测成功率.
)

- [TrickleDownML](https://github.com/andykamath/TrickleDownML)
    - 4 Stars, 0 Fork

Start a conversation with Ronald Reagan!. I made a chatbot that mimics Ronald Reagan.

(`是也乎:`

模仿里根总统语气的聊天儿机器人
)

- [flask_church](https://github.com/lk-geimfari/flask_church)
    - 3 Stars, 0 Fork

An extension for Flask that help you generate fake data. Flask-Church is a small wrapper for Church library.

(`是也乎:`

上周介绍过的专注假数据生成的工具 Church 的 Falsk 配合模块.
)

# 是也乎

- 161015 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161014 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


