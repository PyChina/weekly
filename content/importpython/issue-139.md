Title: 蠎加载 139
Slug: importpython-139
Date: 2017-08-25 21:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 139](http://importpython.com/newsletter/no/139/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [用 flit 轻松发布你的包](http://brunorocha.org/python/publish-your-python-packages-easily-using-flit.html)
    + pypi

Flit is a simple way to Package and deploy Python projects on PyPI, Flit makes it easier by using a simple flit.ini file and assumes common defaults to save your time and typing. I knew about Flit when I was taking a look at Mariatta Wijaya game called Tic Tac Taco Pizza and noticed that she used flit to deploy the game, so we also asked her the reason for using this on the podcast we recorded so I decided to try porting my projects to Flit.


- [用 Python 进行研究 - edX 课程 ( Harvard University )](https://www.edx.org/course/using-python-research-harvardx-ph526x#!)
    + course, mooc

This course bridges the gap between introductory and advanced courses in Python. While there are many excellent introductory Python courses available, most typically do not go deep enough for you to apply your Python skills to research projects. In this course, after first reviewing the basics of Python 3, we learn about tools commonly used in research settings.

- [Python 的 sys.getrefcount() 趣味](http://groverlab.org/hnbfpr/2017-06-22-fun-with-sys-getrefcount.html)
    + core-python

Python has a function called sys.getrefcount() that tells you the reference count of an object.



- [用机器学习来预测获胜团队](https://www.youtube.com/watch?v=6tQhoUuQrOw&feature=youtu.be)
    + machine learning

Can we predict the outcome of a football game given a dataset of past games? That's the question that we'll answer in this episode by using the scikit-learn machine learning library as our predictive tool.


- [用 Docker 组合 Travis CI 进行持续集成的姿势](https://medium.com/@jamiehewland/patterns-for-continuous-integration-with-docker-on-travis-ci-71857fff14c5)
    + docker, CI

Part 2 of 3: The “Docker repo” pattern. Note - Very informative and detailed article for those looking to bring CI + docker into their workflow.

(`是也乎:`

城会玩 ->

![CI-with-Docker-on-TravisCI.png（PNG 图像，705x365 像素）](http://openmindclub.qiniucdn.com/snap/CI-with-Docker-on-TravisCI.png)

)


- [使用 Python 分析 Cryptocurrency Markets](https://blog.patricktriest.com/analyzing-cryptocurrencies-python/?utm_source=hackernews)
    + cryptocurrency

How do Bitcoin markets behave? What are the causes of the sudden spikes and dips in cryptocurrency values? Are the markets for different altcoins inseparably linked or largely independent? How can we predict what will happen next?

(`是也乎:`

数字货币交易市场越来越兴旺, 而且数据是公开的, 值得分析
)

- [用 Python Flask, Pandas 以及 MongoDB 折腾出分析仪表盘](http://kanoki.org/2017/08/25/analytical-dashboard-with-python-flask-pandas-and-mongodb/)
    + mongodb, pandas, flask

Analyzing your sensor data has always been a daunting task and putting your data in the Dashboard has never been an easy task. In this article, we will see how using Python Flask, Pandas and MongoDB you can develop an Analytical Dashboard over a weekend.


(`是也乎:`

![Dashboard](http://kanoki.org/wp-content/uploads/2017/08/dash2-1024x614.png)

有用, 但还是丑...

)

- [拟态](https://github.com/lk-geimfari/mimesis)
    + testing, mocking

Mimesis is a fast and easy to use library for Python, which helps generate mock data for a variety of purposes (see "Data providers") in a variety of languages (see "Locales"). This data can be particularly useful during software development and testing. The library was written with the use of tools from the standard Python library, and therefore, it does not have any side dependencies.

(`是也乎:`

不是 erlang 那个内置 DB 哪...
能模拟各种语言数据集的工具...

![mimesis](https://raw.githubusercontent.com/lk-geimfari/mimesis/master/media/logo.png)

好象支持中文?

)

- [纤程, 线程和进程](http://stupidpythonideas.blogspot.in/2015/01/greenlets-threads-and-processes.html)
    + parallel processing

- [Python 列表的实现](https://py.checkio.org/blog/how-big-is-the-python-family/)
    + core-python

- [USER-USER 协同过滤推荐系统](https://medium.com/@tomar.ankur287/user-user-collaborative-filtering-recommender-system-51f568489727)
    + recommendation engine

we will start building a system that uses the profile of the given user and provide recommendation completely based on that user’s preference and liking.


- [Gaussian Naive Bayes - numpy](https://medium.com/@LSchultebraucks/gaussian-naive-bayes-19156306079b)
    + machine learning

Bayes Theorem describes the probability of an event, based on prior knowledge of conditions be related of conditions to the event. So it basically fits perfectly for machine learning, because that is exactly what machine learning does: making predictions for the future based on prior experience.

(`是也乎:`

叕一则科普文...

)


- [Python Matplotlib Style - 2.0](https://medium.com/@sanatinia/python-matplotlib-style-a961a4d402f7)
    + matpoltlib

Matplotlib is a great and very capable plotting library for Python.

(`是也乎:`

可惜一直没有解决互联网时代的直接输出需求...
)

- [如何使用 Python 删除或修改 CSV 数据集中的空值](https://medium.com/@leah.e.cole/how-to-use-python-to-remove-or-modify-empty-values-in-a-csv-dataset-34426c816347)
    + code snippets, csv

Data sets are not perfect. Sometimes they end up with invalid, corrupt, or missing values. For the project I was working on, I could not have any values that are null or empty. This How-To will walk you through writing a simple Python script to see if your data set has null or empty values, and if so, it will propose two options for how to modify your data.

- [如何使用 Cloudinary 和 Python 加速工艺术网站的加载](https://medium.com/@alon7/how-to-make-an-art-website-load-at-lightning-speed-using-cloudinary-and-python-9129acc8cef4)
    + cloudinary

- [pip 黑魔法 ~ 一键升级所有 Python 模块](https://hackernoon.com/a-pip-hack-to-upgrade-all-your-python-packages-492658c49681)
    + pip

- [使用 PySpark Dataframe – Zhiqiang Zhong – Medium](https://medium.com/@zhiqiangzhong/using-pyspark-dataframe-as-python-dataframe-2959c2a085e)
    + pyspark, dataframes

I will share you about how using Dataframe of PySpark as Dataframe of Python.

- [如何跨越 CPython 解释器](https://medium.com/@skabbass1/how-to-step-through-the-cpython-interpreter-2337da8a47ba)
    + cpython

I will outline the process I typically follow to dig deeper into aspects of the python programming language I am curious about.


- [Python: Guidelines & Code Style](https://medium.com/storepilots-team/python-guidelines-code-style-5b5a0d402032)
    + coding standards

This document is intended to Storepilots employees, but worth the read.


- [http(s) session recording 技巧](https://medium.com/@george.shuklin/tips-and-tricks-on-http-s-session-recording-4194f99adbf)
    + http

- [pep 551](https://github.com/python/peps/blob/cd795ec53c939e5b40808bb9d7a80c428c85dd52/pep-0551.rst)
    + PEP

This PEP describes additions to the Python API and specific behaviors for the CPython implementation that make actions taken by the Python runtime visible to security and auditing tools. The goals in order of increasing importance are to prevent malicious use of Python, to detect and report on malicious use, and most importantly to detect attempts to bypass detection. Most of the responsibility for implementation is required from users, who must customize and build Python for their own environment.

(`是也乎:`

有关运行安全的嗯哼

)


- [What is self healing software?](https://twitter.com/importpython/status/900316548379713538)
    + humor

- [用 CFFI 将 Python 链接到 C](https://tmarkovich.github.io//articles/2017-08/linking-python-to-c-with-cffi)
    + c

- [让我们在 Python 中同步线程](https://www.codementor.io/saurabhchaturvedi63/let-s-synchronize-threads-in-python-b8pwcz2d1#.WZ22zfgigcg.hackernews)

(`是也乎:`

让我们荡起双桨

)


- [Nuitka - Python Complier](http://nuitka.net/pages/overview.html)
    + compiler

Nuitka is a Python compiler. It's fully compatible with Python 2.6, 2.7, 3.2, 3.3, 3.4, 3.5, and 3.6. You feed it your Python app, it does a lot of clever things, and spits out an executable or extension module.

(`是也乎:`

又一个 编译器, 可以递归的将 python 脚本以及依赖库编译成单一 .exe

但是,类似 Qt/OpenCV/numpy/pandas/... 巨型模块,
就别想了...

)


- [Python 加密作弊书](https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-crypto.rst)
    + cryptocurrency

- [pyheatmagic](https://github.com/csurfer/pyheatmagic)
    + ipython

IPython magic command to profile and view your python code as a heat map using py-heat.


(`是也乎:`

![pyheatmagic](https://camo.githubusercontent.com/91d83aa2f68ff8f2848235cb190c99a00b74b81f/687474703a2f2f692e696d6775722e636f6d2f495574617350482e676966)

自动分析代码执行热度的插件...

)


## 好物
~ 包/模块/库/片段...



- [raven](https://github.com/0x09AL/raven)
    + 133 Stars, 20 Fork

raven is a Linkedin information gathering tool that can be used by pentesters to gather information about an organization employees using Linkedin.

(`是也乎:`

嚓,专门协助公司监察职员是否有嗯哼心理的...

)

- [unformat](https://github.com/johnmcfarlane/unformat)
    - 113 Stars, 6 Fork

generates .clang-format file from example codebase

- [Pytorch_fine_tuning_Tutorial](https://github.com/Spandan-Madan/Pytorch_fine_tuning_Tutorial)
    - 47 Stars, 6 Fork

A short tutorial on performing fine tuning or transfer learning in PyTorch.

(`是也乎:`

第一波  PyTorch 教程
)


- [coinbin.org](https://github.com/kennethreitz/coinbin.org)
    - 44 Stars, 3 Fork

A Human–Friendly API Service for Crypto Currency Information.

(`是也乎:`

数字货币的二级工具
)


- [Tiny-URL-Fuzzer](https://github.com/orangetw/Tiny-URL-Fuzzer)
    - 35 Stars, 1 Fork

A tiny and cute URL fuzzer.

(`是也乎:`

对于各种新生的域名不知道是否 hold 了

)

- [argo](https://github.com/argoproj/argo)
    - 16 Stars, 13 Fork

Get stuff done with container-native workflows for Kubernetes.

(`是也乎:`

K8s 的辅助工具

)

- [awesome-apistar](https://github.com/penny-api/awesome-apistar)
    - 10 Stars, 0 Fork

A curated list of awesome packages, articles, and other cool resources from the API Star community.

(`是也乎:`

这个组件的生态嗯哼的也忒快了...
)


- [htmldate](https://github.com/adbar/htmldate)
    - 2 Stars, 0 Fork

extract the date of HTML documents.

(`是也乎:`

提取页面中的日期信息...不支持中文的,当然
)

- [pg-materialize](https://github.com/aanari/pg-materialize)    
    - 2 Stars, 0 Fork

Postgres Materialized View Dependency Manager.

(`是也乎:`

Pg 的辅助工具...很久没见有新
)


- [phone-scraper](https://github.com/rpasta42/phone-scraper)
    - 0 Stars, 0 Fork

Python library for finding phone numbers in random user input text. 

(`是也乎:`

实用, 但是,不包含中国的...
)

### (￣▽￣)
~ 抢在珠海第二波台风来袭, 前嗯哼出来

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


