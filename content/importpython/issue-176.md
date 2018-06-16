Title: 蠎加载 176
Slug: importpython-176
Date: 2018-06-16 15:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 176](http://importpython.com/newsletter/no/176/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 中自然语言处理速度提高100倍](https://medium.com/huggingface/100-times-faster-natural-language-processing-in-python-ee32033bdced)
    + NLP, spaCy

How to take advantage of spaCy & a bit of Cython for blazing fast NLP


- [对 Python 的 GIL 以纯 Python 实现](https://rushter.com/blog/python-gil-thread-scheduling/)
    + gil

There is an excellent presentation of how the modern GIL performs thread scheduling, but unfortunately, it lacks some interesting details (at least for me). I was trying to understand all the details of the GIL, and it took me some time to fully understand it from the CPython's source code. So here is a simplified algorithm of the thread scheduling that is taken from CPython 3.7 and rewritten from C to pure Python for those, who are trying to understand all the details.

(`是也乎:`

PyPy 已经作过了?

)


- [吃一些代码 - 在Django中处理重复测试](http://eatsomecode.com/handling-repetitive-tests-django?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+eatsomecode+%28Eat+Some+Code%29)
    + testing

When writing tests (unit and/or functional), one of the goal is to cover all edge-cases. DDT is a great way to write such tests; here is how to do so in Python and Django.

- [Python 3 – 分配表达式](http://www.blog.pythonlibrary.org/2018/06/12/python-101-assignment-expressions/)
    + core-python

I recently came across PEP 572, which is a proposal for adding assignment expressions to Python 3.8 from Chris Angelico, Tim Peters and Guido van Rossum himself! I decided to check it out and see what an assignment expression was. The idea is actually quite simple. The Python core developers want a way to assign variables within an expression using the following notation.

(`是也乎:`

实现很简单,但是, 想确保追加到语法后不引发其它问题,太难...

)


- [Mypy 0.610 发布ed](http://mypy-lang.blogspot.com/2018/06/mypy-0610-released.html)
    + new release

We’ve just uploaded mypy 0.610 to the Python Package Index (PyPI). Mypy is an optional static type checker for Python. This release includes new features, bug fixes and library stub (typeshed) updates.

- [5种 Python 发行版用于掌握机器学习](https://www.infoworld.com/article/3279544/python/5-python-distributions-for-machine-learning.html#tk.rss_all)
    + machine learning

From bare-bones to full-blown, learn which edition of Python is best for your machine learning projects.

- [创建和共享私有 Python 包](https://medium.com/@christopherdavies553/creating-and-sharing-private-python-packages-689c73ce01ff)
    + build

How django-carrot uses PyPRI to store and distribute development build?

(`是也乎:`

简单说,上 [PyPRI](https://www.python-private-package-index.com/)
也是墙外的服务...

)


- [估计最希望谁赢得 FIFA 世界杯: 用 Python 嗯哼推文](https://medium.com/@theprasadpatil/estimate-the-favorite-scraping-tweets-using-python-863303384e29)
    + twitter api

Religious festival of all football followers?—?FIFA World Cup 2018,has just began in Russia.This month long prestigious sports bonanza will be celebrated across the globe till it’s mega finale scheduled on 15th July.

- [TextBlob 和情感分析](https://medium.com/@rahulvaish/textblob-and-sentiment-analysis-python-a687e9fabe96)
    + machine learning

Let’s see a very simple example to determine sentiment Analysis in Python using TextBlob.

- [保存和托管您的第一个机器学习模型指南](https://heartbeat.fritz.ai/guide-to-saving-hosting-your-first-machine-learning-model-cdf69729e85d)
    + machine learning

In this article, we’re going to build a simple sentiment analysis platform using Flask, a lightweight web application framework. Our platform will be able to classify a movie review as either positive or negative. We’ll use the IMDB dataset to build a simple sentiment analysis model, save it, and host it on Heroku. We’ll use Gunicorn to serve our model.

- [Python 3.7.0rc1 和 3.6.6rc1 可用](https://mail.python.org/pipermail/python-dev/2018-June/153882.html)
    + new release





## 好物
~ 包/模块/库/片段...

- [gif-for-cli](https://github.com/google/gif-for-cli)
    - 958 Stars, 33 Fork

Takes in a GIF, short video, or a query to the Tenor GIF API and converts it to animated ASCII art. Animation and color support are performed using ANSI escape sequences.

(`是也乎:`

基于: ![Tenor](https://github.com/google/gif-for-cli/raw/master/docs/gif-for-cli-logo.png)

支持多种颜色模式,比如说:

![256 Colors Supported](https://camo.githubusercontent.com/7092156c82f05effba0b57b06eb37b1f08522ef7/68747470733a2f2f6d65646961312e74656e6f722e636f6d2f696d616765732f64333534656530383430643933373665326261616364626565353962366330362f74656e6f722e6769663f6974656d69643d3131393937343239)

py3 only...

)


- [StarGAN-Tensorflow](https://github.com/taki0112/StarGAN-Tensorflow)
    - 332 Stars, 52 Fork

Simple Tensorflow implementation of StarGAN (CVPR 2018 Oral)

- [senticomment](https://github.com/johnafish/senticomment)
    - 175 Stars, 20 Fork

Gets the sentiment of YouTube comments

(`是也乎:`

所以, 次级内容也开始被分析重视了;
目测因为变成了广告阵地?

)

- [glad](https://github.com/salesforce/glad)
    - 33 Stars, 0 Fork

Global-Locally Self-Attentive Dialogue State Tracker


(`是也乎:`

挺快乐的工具

)

- [PyTorchCV](https://github.com/CVBox/PyTorchCV)
    - 23 Stars, 3 Fork

Repo for most of CV problems, such as image classification, object detection, pose estimation, segmentation, and so on.

(`是也乎:`

PyTorch 对机器视觉的一系列嗯哼

)


- [awesome-fintech](https://github.com/FinancialDataGirl/awesome-fintech)
    - 22 Stars, 3 Fork

A collections of awesome fintech stuff.

(`(￣▽￣)`:


来自 [财报妹](https://weibo.com/marsfactory/)

)

- [click-boilerplate](https://github.com/manparvesh/click-boilerplate)
    - 19 Stars, 3 Fork

Boilerplate project for creating sophisticated command line applications using the Click library in Python

(`是也乎:`

基于 pocoo.org 出品的 click 快速完成实用工具

)


- [nonoCAPTCHA](https://github.com/mikeyy/nonoCAPTCHA)
    - 15 Stars, 2 Fork

nonoCAPTCHA - defeating Google's reCAPTCHA one step at a time

(`是也乎:`

![8osnqnvmm6211.gif（GIF 图像，1597x982 像素） - 缩放 (77%)](https://i.redd.it/8osnqnvmm6211.gif)

略帬...
)


- [Dee.py](https://github.com/AliFlux/Dee.py)
    - 13 Stars, 3 Fork

Deep neural network for python in 200 LOCs

(`是也乎:`


![promo](https://github.com/AliFlux/Dee.py/raw/master/promo.png)

)


- [archive_tweet](https://github.com/motherboardgithub/archive_tweet)
    - 11 Stars, 1 Fork

A Twitter bot that archives tweets on demand.


(`是也乎:`

叕一则不存在的公共大数据工具..

)


- [tensorflow-DSMM](https://github.com/ChenglongChen/tensorflow-DSMM)
    - 6 Stars, 0 Fork

Deep Semantic Matching Models

- [FAP](https://github.com/salan668/FAP)
    - 6 Stars, 0 Fork

Feature Analysis Pipeline




- [jumbo](https://github.com/adaltas/jumbo)
    - 5 Stars, 0 Fork

A local Hadoop cluster bootstrapper using Vagrant, Ansible, and Ambari.

(`是也乎:`

很久没见 Hadoop 生态链新工具了..

)


- [week-planner](https://github.com/zoleck/week-planner)
    - 4 Stars, 0 Fork

A way to organise what you eat each week based on a database of food products 


(`是也乎:`

细思恐极->首次见减肥专用工具...

)

### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180616 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180616 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


