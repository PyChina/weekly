Title: 蠎加载 126
Slug: importpython-126
Date: 2017-05-26 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 126](http://importpython.com/newsletter/no/126/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [PyCon 2017 视频已经在 YouTube](https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg/feed)
    + pyconus, pycon

Videos of the just concluded Pycon US 2017.

(`是也乎:`

准备和 UPYUN 合作批量搬迁到国内...
)

- [如何获得 PyPI 下载状态?](https://kirankoduru.github.io/python/pypi-stats.html)
    + bigquery, pipy

This is a short post on how to get download statistics about any package from PyPI. Though there have been efforts in that direction from sites like pypi ranking but this post finds a better solution. Google has been generous enough to donate it’s Big Query capacity to the Python Software Foundation. You can access the pypi downloads table through the Big Query console. I ran a sample query to find out how my personal package arachne has been doing on PyPI.

(`是也乎:`

Google Big Query 已经监控了...

![bigquery](https://kirankoduru.github.io/img/bigquery.jpg)

)

- [SQLAlchemy 简介 - Agiliq Blog](http://agiliq.com/blog/2017/05/introduction-sqlalchemy/)
    + SQLAlchemy

The breadth of SQLAlchemy’s SQL rendering engine, DBAPI integration, transaction integration, and schema description services are documented here. In contrast to the ORM’s domain-centric mode of usage, the SQL Expression Language provides a schema-centric usage paradigm.

(`是也乎:`

无数种草文又一则
)


- [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python#.)
    + core-python

The various meanings and naming conventions around single and double underscores (“dunder”) in Python, how name mangling works and how it affects your own Python classes.


(`是也乎:`

![underscores](https://dbader.org/blog/figures/python-underscores.png)
)

- [Python: 好物 Objects 来袭](https://medium.com/@glyif/python-the-thing-good-objects-come-in-a59d37402928)
    + PyObject

In Python, all object types inherit from one master object, declared as PyObject . This master object has all of the information Python needs to process a pointer to an object as an actual object.


- [调试一个安静的 Python 进程](https://medium.com/@priyankar/debugging-an-inactive-python-process-2b11f88730c7)
    + debugging

So we had a production case for months together, where the python process was stuck for indefinitely long time (even days) with absolutely zero activity but the process was listed as active and running by linux. A restart would fix the problem (as always) and the job would be live and kicking. Finally after sometime, I have found the root cause, so I thought I would share it. For the purpose of the blog I’m going to simulate the behavior of my application in a sample python script.


(`是也乎:`

![qAMYuML_sI5WBuBI91_EEg](https://cdn-images-1.medium.com/max/720/1*qAMYuML_sI5WBuBI91_EEg.jpeg)

其实就是一个长期运行的 py 进程的调试技巧,
尝试模拟来激发bug...

最后还是回到了 GDB

)


- [用 Python 驱动 Headless Chrome](https://duo.com/blog/driving-headless-chrome-with-python)
    + chromium, headless

Back in April, Google announced that it will be shipping Headless Chrome in Chrome 59. Since the respective flags are already available on Chrome Canary, the Duo Labs team thought it would be fun to test things out and also provide a brief introduction to driving Chrome using Selenium and Python.

(`是也乎:`

太应景了...只是用 selenium 来调, 肥了点儿?
)

- [用 Elizabeth 生成 mock 数据: Part I](https://medium.com/wemake-services/generating-mock-data-using-elizabeth-part-i-ca5a55b8027c)
    + mock

Elizabeth is a Python library, which helps generate mock data for various purposes. The library was written with the use of tools from the standard Python library, and therefore, it doesn’t have any side dependencies. Currently the library supports 30 languages and 19 class providers, supplying various data.


- [Python 3 boilerplate](https://www.python-boilerplate.com/)
    + boilerplate

Python-boilerplate.com is a collection of Python boilerplates for getting started quickly and right-footed.


- [如何用 Python 计算文档相似度?](http://www.datasciencecentral.com/profiles/blogs/how-do-i-compare-document-similarity-using-python)
    + gensim

- [用 Python + Asyncio 和 Scrape 以及 Parse 达到 600个/10分钟 的 ETF 分析速度](http://www.blackarbs.com/blog/how-to-scrape-and-parse-600-etf-options-in-10-mins-with-python-and-asyncio/5/18/2017)
    + scraping

- [教程: 用 Python 进行异步语音识别](https://medium.com/@spnichol/tutorial-asynchronous-speech-recognition-in-python-b1215d501c64)
    + speech recognition

(`是也乎:`

用的 google 接口, 其实讯飞的也足够了
)

- [PyCon JP Blog: PyCon JP 2017 开始接收 Poster-Session Proposals](http://pyconjp.blogspot.in/2017/05/call-for-poster-proposal-en.html)
    + pyconjp

PyCon JP 2017 is Now Accepting Poster-Session Proposals! PyCon JP 2017 is a perfect opportunity to connect with a wide range of people. Poster sessions allow you to make the most of that opportunity.


- [PyCon 2017 头天感想](https://www.wordfugue.com/thoughts-pycon-2017-day-1/)
    + pycon

- [Python 3 Patterns, Recipes and Idioms — Python 3 Patterns, Recipes and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html)
    + idioms


(`是也乎:`

![Idioms.py3](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/_static/cover.png)

完整的一木书了...
Bruce Eckel <-- 专门写 Think in * 的大仙,
当年 Tink in Java 看的是欲仙欲死...

~ [Bruce Eckel's MindView, Inc: Books by Bruce Eckel](http://mindview.net/Books/books.html)
对了, 唯一太监的就是 `Think in Python`
)

- [嗯哼你的 Python IDE](https://medium.com/@paysonwallach/roll-your-own-python-ide-e901ffd422e9)
    + atom

Using Atom IDE.

(`是也乎:`

VScode vs Atom vs others
)

- [Global 变量在 Python 并不是全局的](https://medium.com/python-pandemonium/global-variables-arent-global-in-python-c8936bb31f23)
    + core-python, global

Python uses global to reference to module-global variables. There are no program-global variables in Python.

(`是也乎:`

模块全局,不是程序全局, 真正的全局变量,
在移动互联网时代,只能是第三方广播服务了
)

- [大师访谈: The Unique Characters Problem](https://medium.com/@valeria.rozenbaum/mastering-technical-interviews-the-unique-characters-problem-588be78be236)
    + interview

- [获得 Python Requirements Package Hashes](https://davidwalsh.name/hashin)
    + pip, nodejs, requirement.txt

Python's (pip's) requirements.txt file is the equivalent to package.json in the JavaScript / Node.js world.  This requirements.txt file isn't as pretty as package.json but it not only defines a version but goes a step further, providing a sha hash to compare against to ensure package integrity:
 



## 好物
~ 包/模块/库/片段...


- [baselines](https://github.com/openai/baselines)
    - 241 Stars, 28 Fork

OpenAI Baselines: high-quality implementations of reinforcement learning algorithms



- [semilive](https://github.com/toji/semilive)
    - 92 Stars, 3 Fork

A Sublime Text plugin for "Live" coding

(`是也乎:`

实时编码...
)

- [IPpy](https://github.com/shivammathur/IPpy)
    - 41 Stars, 3 Fork

Parallel testing of IP addresses and domains in python

(`是也乎:`

面向网络事件的平行测试

![IPpy](https://camo.githubusercontent.com/827abcc204730d8a40434ae7fe5796883c3bae32/68747470733a2f2f73686976616d6d61746875722e636f6d2f495070792e706e67)

基于 tox 组织...
)

- [content-downloader](https://github.com/nikhilkumarsingh/content-downloader)
    - 30 Stars, 10 Fork

Python package to download files on any topic in bulk.

(`是也乎:`

![content](https://camo.githubusercontent.com/74b0884faaebae6d08d93c27e0434809eb365f20/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f336f4b49506c7437415048715775566c33712f67697068792e676966)

嚓....当然的, 国内无法使用...
)

- [v2ex-terminal](https://github.com/creatorYC/v2ex-terminal)
    - 27 Stars, 1 Fork

browse v2ex by a terminal


(`是也乎:`

CLI 的魔爪终于摸到了 V2EX,
基本上没有 CLI 界面的服务/网站,都不算真正的程序猿社区...

所以, CPyUG 一直是个纯粹的程序猿社区,因为只有一个 mailling-list 在长年服务


![v2ex](https://github.com/creatorYC/v2ex-terminal/raw/master/images/start.PNG)

)

- [logging-spinner](https://github.com/dahlia/logging-spinner)
    - 17 Stars, 0 Fork

Display spinners (in CLI) through Python standard logging.

(`是也乎:`

![spinner](https://github.com/dahlia/logging-spinner/raw/master/sample.gif)

值得体验

)

- [aws-batch-genomics](https://github.com/awslabs/aws-batch-genomics)
    - 14 Stars, 4 Fork

Software sets up and runs an genome sequencing analysis workflow using AWS Batch and AWS Step Functions.

- [twitter-bot](https://github.com/musamasiddiqui/twitter-bot)
    - 5 Stars, 0 Fork

Python Bot that Tweets quote and like Tweets.

- [jsonfeedvalidator](https://github.com/voidfiles/jsonfeedvalidator)
    - 4 Stars, 0 Fork

JSON Feed Validator

- [handcart](https://github.com/hatnote/handcart)
    - 3 Stars, 1 Fork

Command-line tools for project-oriented, human-sized Wikidata import

- [slacky](https://github.com/mathiasbc/slacky)
    - 0 Stars, 0 Fork

Slack client on the terminal with a GUI.This is a weekend project that started for me as a way to learn how to write old style command line interfaces. Slack is a tool a lot of programmers use today so I thought a lot of you would have interest in contributing to this effor. 

(`是也乎:`

![slacky](https://github.com/mathiasbc/slacky/raw/master/img/slacky.jpg)

Dos 时代是一个回不去的时代...

)

### (￣▽￣)

- [tankywoo/simiki](https://github.com/tankywoo/simiki)
    + 657 Stars, 95 Fork

Simiki is a simple wiki framework, written in Python.

(`是也乎:`

知道创宇 成员私人作品 md 的静态维基
)

# 是也乎

- 170526 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170526 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


