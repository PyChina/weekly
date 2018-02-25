Title: 蠎加载 164
Slug: importpython-164
Date: 2018-02-25 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 164](http://importpython.com/newsletter/no/164/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 3 cheatsheet](https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-new-py3.rst)
    + python3

What's new in Python 3 via code snippets.

(`是也乎:`

文字版本的作弊条儿...

Py 3.7 有了内置的 breakpiont 支持, 
可以不依赖 IDE 进行单点嗯哼了...

可是...好吧...

)


- [俺的 Python 开发环境, 2018 版 - Jacob Kaplan-Moss](https://jacobian.org/writing/python-environment-2018/)
    + pyenv, pipsi

For years I’ve noodled around with various setups for a Python development environment, and never really found something I loved – until now.

(`是也乎:`

Python 的开发环境至今没有很好的解决几个关键问题:

模块依赖, 多版本环境切换, 应用打包发布/备份/部署/升级/...

当前最靠谱的可能就是这个组合了:
用 Pyenv 管理版本环境,
在其中用 Pipenv 管理模块依赖,
Pipsi 作控制界面...

可是, 依然没有触及发布后场景...当然,现在有 Docker 了...
问题是 Docker 在 windows 世界中实在是那什么....

)


- [用 Python 收集您自己的 Fitbit 数据](https://medium.com/@begahtan/collect-your-own-fitbit-data-with-python-1ecb1b655b1e)
    + fitbit

I’m going to teach you how to collect your own Fitbit data using nothing but a little Python code.

(`是也乎:`

现在智能硬件, 如果没有一个易用的云接口,简直了...

)


- [standford 电影评论数据库的情感分类](https://github.com/kodiaklabs/MovieSentimentClassification/blob/master/MovieReviewClassification.ipynb)
    + machine learning

In this tutorial we will be using the hand labelled Standford movie review database (0) to build a sentiment classifier. Our work will highlight how to use Jupyter Notebooks with Python, Scikit-learn, and Pandas (including Numpy) to build and crossvalidate a sentiment classifier. We will also throw in a bit of EDA with the help of Matplotlib and Seaborn.

(`是也乎:`

公开数据集越来越多了...
但是, 分析套路越来越一致化

EDA 是唯一能结合直觉的阵地了...

不过用 seaborn 进行图表风格化就是个人口味选择了...
)


- [象 Python 一般调试 C](http://blog.asrpo.com/debugging_c_like_python)
    + debugging

I use the Python interpreter interactively and pdb (as well as ipdb) a lot and they let me understand my programs' state and test new things out quickly.

(`是也乎:`

pdb 体验的 gdb 模拟...

)

- [Elasticsearch 和 Django 第 1 部分](https://blog.botreetechnologies.com/elasticsearch-with-django-part-1-faefcdb7d32)
    + elasticsearch

Searching from a complex set of data has become a routine in almost all kind of applications. So I am creating a series on Elasticsearch integration with Django. I this part of series, I will be giving you a brief information about Elasticsearch and its installation on a Linux based system.



- [PEP 563 提及 Python 4.0, 究尽什么事儿? - Reddit discussion](https://www.reddit.com/r/Python/comments/7zvyhx/pep_563_mentions_python_40_whats_going_on/)
    + 4.0

PEP 563 as well as this page declare that postponed evaluation of type annotations will become the default in Python 4.0. The authors don't give any further explanation nor do they seem to think there is any further explanation required. I've never seen Python 4.0 mentioned seriously before and I find this a bit unsettling. Can somebody provide more details?

(`是也乎:`

没有回头路了...

Py3 到 Py4 就象 Py1 到 Py2 没有伤害...哈?

)

- [Truthiness and Short-Circuit Evaluation in Python](http://blog.jrheard.com/truthiness-and-short-circuit-evaluation-in-python)
    + core-python

- [通过 Python 中的 HTTP 代理建立套接字连接](https://gist.github.com/frxstrem/4487802)
    + codesnippets

- [Using Django signals for database logging](https://medium.com/algotech-solutions/using-django-signals-for-database-logging-abd1c0fc5598)
    + django

(`是也乎:`

看来 signals 技术用的人不多...

)

## 好物
~ 包/模块/库/片段...

- [twitter-scraper](https://github.com/kennethreitz/twitter-scraper)
    - 256 Stars, 11 Fork

Scrape the Twitter Frontend API without authentication.

(`是也乎:`

不用登录的 Twitter 爬虫接口?!
)

- [s3monkey](https://github.com/kennethreitz/s3monkey)
    - 209 Stars, 2 Fork

A Python library that allows you to interact with Amazon S3 Buckets as if they are your local filesystem.

(`是也乎:`

这名字起的...还以为是 chaos monkey 工具呢...

)


- [pytorch-cnn-finetune](https://github.com/creafz/pytorch-cnn-finetune)
    - 135 Stars, 12 Fork

Fine-tune pretrained Convolutional Neural Networks with PyTorch

(`是也乎:`

叕一个 PyTorch 的 CNN 实案

)


- [ssm-cache-python](https://github.com/alexcasalboni/ssm-cache-python)
    - 35 Stars, 5 Fork

AWS System Manager Parameter Store caching client for Python



- [heroku-jupyterlab](https://github.com/heroku/heroku-jupyterlab)
    - 20 Stars, 0 Fork

An example of running JupyterLab on Heroku, with Amazon S3.


(`是也乎:`

[jupyterlab/jupyterlab: JupyterLab computational environment.](https://github.com/jupyterlab/jupyterlab)

的 Heroku 部署样例...

![jupyterlab](http://jupyterlab.readthedocs.io/en/latest/_images/jupyterlab.png)

Jupyter 开始认真的将网页变成 IDE 了...

)



- [cursor-tracking-css](https://github.com/zaytoun/cursor-tracking-css)
    - 18 Stars, 3 Fork

Tracking a cursor across a webpage using only CSS.

(`是也乎:`

![cursor-tracking-css](https://github.com/zaytoun/cursor-tracking-css/raw/master/static/img/demo.gif)

细思恐极, CSS 也是完备的应用语言嘛?
嚓...只是作了一个简单的反射追踪.


)


- [simple-visual-geocoder](https://github.com/jsoma/simple-visual-geocoder)
    - 3 Stars, 0 Fork

A tool to allow US addresses to be geocoded/georeferenced easily, without using Python or the command line or paid services or anything.

(`是也乎:`

![geocoded](https://github.com/jsoma/simple-visual-geocoder/blob/master/screenshots/main.png)

叕一个简单的地理信息数据包...当然转换的是国外的系统和数据

)


- [heroku-platform](https://github.com/kennethreitz/heroku-platform)
    - 2 Stars, 0 Fork

Heroku Platform API client for Python.

(`是也乎:`

叕一个 Heroku 平台接口包装

)


- [appconf](https://github.com/adonisnafeh/appconf)
    - 2 Stars, 0 Fork

Simple method used to load configuration variables from different sources.

(`是也乎:`

多源配置加载工具...

配置管理不在源头的复杂, 而是配置信息到系统行为的表述对应关系吧

)


- [Thor](https://github.com/AsgardIO/Thor)
    - 2 Stars, 0 Fork

Takes power from simplicity. Simple, Powerful, Async web framework developed with Asgard Technologies. 


(`是也乎:`

叕一个 web 框架原型
文档都没有嗯哼好, 先养着...

)

### (￣▽￣)

- [Neilpang/acme.sh: A pure Unix shell script implementing ACME client protocol](https://github.com/Neilpang/acme.sh)
    + https

> 国人作品, 解决 https 部署时的证书生成问题


- [kaleguy/leovue: File viewer for the Leo open source outline editor / IDE, integrated with Vue.js](https://github.com/kaleguy/leovue#leo-vue)
    + Leo,Vue

> 猛然发现, Leo 生态已经走到这种程度了...

![leovue](https://camo.githubusercontent.com/710523b7e44c98cbffe6546278535f6665ef5cec/68747470733a2f2f6b616c656775792e6769746875622e696f2f6c656f7675652f73637265656e63617374732f6c656f7675652d636f6d706f6e656e74732e676966)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180225 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180225 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


