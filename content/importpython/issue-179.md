Title: 蠎加载 179
Slug: importpython-179
Date: 2018-07-10 18:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 179](http://importpython.com/newsletter/no/179/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [Python 3.8 已明确7项新嗯哼](https://hackernoon.com/7-features-proposed-so-far-in-python-3-8-acb0d97c83c8)
    + PEP, 3.8

Python 3.7 benefitted from both new functionality and optimizations. From what we know so far about 3.8, it’s going to be a similar story. This time, most of the new functionality is targeted at C extension and module development. Based on the existing, Python Enhancement Proposals, or “PEPs” that have been submitted for 3.8 we have a good grasp on what features are likely to be included. I’ve put together a PEP-Explorer UI here for 3.8.


(`是也乎:`

总之, 为了吸引大家进入 py3 世界, PEP 的嗯哼也加速了
)


- [第 #168 集: 10种 Python 安全漏洞以及如何插入它们](https://talkpython.fm/episodes/show/168/10-python-security-holes-and-how-to-plug-them)   
    + podcast

Do you write Python software that uses the network, opens files, or accepts user input? Of course you do! That's what almost all software does. But these actions can let bad actors exploit mistakes and oversights we've made to compromise our systems. Python is safer than some languages, but there are plenty of issues to be careful about. That's why Anthon Shaw and Anthony Langsworth are joining me to discuss Python security.


(`是也乎:`

用 Python 开发软件的常见嗯哼...

其实吧, 嘦不是运行在 windows 环境中的都很好解决

)

- [比较 Python,R 和 Scala 的顶级数据科学库](https://medium.com/activewizards-machine-learning-company/comparison-of-top-data-science-libraries-for-python-r-and-scala-infographic-574069949267)
    + infographics

(`是也乎:`

其实吧, 这种比例早已没什么必要了

)


- [使用 LINQ 扩展 python 列表以实现干净快速编码](https://github.com/avilum/linqit)
    + project

A list-like type with fun functionality. Extents the builtin list with .NET's Language Intagrated Queries (Linq) and more. Write clean code with powerful syntax. Forget about messy loops, conditions and list comprehensions.

(`是也乎:`

传说 LINQ 是项非常嗯哼的技术...然后...

)


- [马尔可夫链文本生成器的优雅 Python 代码 - Eli Bendersky's website](https://eli.thegreenplace.net/2018/elegant-python-code-for-a-markov-chain-text-generator/)
    + markov chain

While preparing the post on minimal char-based RNNs, I coded a simple Markov chain text generator to serve as a comparison for the quality of the RNN model. That code turned out to be consice and quite elegant (IMHO!), so it seemsed like I should write a few words about it. It's so short I'm just going to paste it here in its entirety, but this link should have it in a Python file with some extra debugging information for tinkering, along with a sample input file.




- [用 Python 在 AWS Lambda 为星际争霸II构建 Amazon Alexa Skill](https://upsidelab.io/blog/alexa-skill-starcraft-python-aws-lambda/)
    + aws, lamda

The rising adoption of Amazon's Alexa and Google Assistant brings a lot of amazing possibilities for developers. I'm going to show you the basic concepts of building voice user interfaces and how to build a simple Alexa skill. And since there's plenty of "hello world" Alexa tutorials on the internet, we're going to build something more interesting. Something that you can literally play with.


(`是也乎:`

AWS lamda 虽然是开创性的微服务形态,但还没有成为标准

)


- [Meet Daniel Imberman and Seth Edwards: Apache Airflow and the Kubernetes Executor](https://medium.com/pybay/meet-daniel-imberman-and-seth-edwards-apache-airflow-and-the-kubernetes-executor-c3564a66a9e1)
    + pybay

This post is part of a series introducing the speakers at the PyBay2018 conference in San Francisco this August. It’s a great chance to learn and connect with an engaged and diverse community of Python developers. We hope you’ll join us!



- [扩展和定制 django-allauth](https://medium.com/@gajeshbhat/extending-and-customizing-django-allauth-eed206623a1a)
    + django

In the previous tutorial, we learned about setting up and configuring some basic settings of django-allauth. If you have not yet read it, I recommend you read it here. You can proceed if you have completed the basic setup and configuration. This article deals with customizing django-allauth signup forms, intervening in registration flow to add custom process and validations. Social logins and their customizations discussed in the next article.


(`是也乎:`

Django 早已成功进入复杂到一眼看不出问题的境界了

)



- [DBSCAN 聚类教程](https://medium.com/nearist-ai/dbscan-clustering-tutorial-dd6a9b637a4b)
    + clustering algorithm

DBSCAN is a popular clustering algorithm which is fundamentally very different from k-means.

(`是也乎:`

叕一则流行分类算法教程

)


- [Python 中的基本统计: 描述性统计](https://www.dataquest.io/blog/basic-statistics-with-python-descriptive-statistics/)
    + statistics

- [对 Celery 任务进行单元测试](https://www.python-celery.com/2018/05/01/unit-testing-celery-tasks/)
    + celery, TDD

While you might get away with not writing unit tests for very simple Rest API endpoints, doing the same for celery tasks is recipe for frustration (and disaster). Celery tasks are asynchronous by design and therefore a lot harder to get a grip on using a “development driven development” approach. Test Driven Development (TDD) might not have taken us to the promised land we had hoped for, but when it comes to celery tasks, it most definitely is essential to a sane, effective and efficient development process - and having that peace of mind when releasing your code into production.

(`是也乎:`

对分布式嗯哼的测试一直是个大问题...

)



- [计算文件](https://no-title.victordomingos.com/projects/count-files/)
    + project


A little command-line interface (CLI) utility written in Python to help you count files, grouped by extension, in a directory. By default, it will count files recursively in current working directory and all of its subdirectories, and will display a table showing the frequency for each file extension (e.g.: .txt, .py, .html, .css) and the total number of files found.

(`是也乎:`

文件统计小工具...

)


## 好物
~ 包/模块/库/片段...

- [Adam-experiments](https://github.com/sgugger/Adam-experiments)
    - 87 Stars, 6 Fork

Experiments with Adam/AdamW/amsgrad

- [bitcoin-lightning-docker](https://github.com/PierreRochard/bitcoin-lightning-docker)
    - 37 Stars, 2 Fork

A docker environment for Bitcoin/LN

(`是也乎:`

反正空气币的嗯哼是越来越方便了...
)


- [pgn2gif](https://github.com/dn1z/pgn2gif)
    - 27 Stars, 2 Fork

A small tool that generates 640x640 gif of chess pgn

(`是也乎:`

![pgn2gif](https://camo.githubusercontent.com/2c02bab1ba67885f7ac7b9483a0627e9017bae4f/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f3255746b4b6d6b684243667630625848426b2f67697068792e676966)

)


- [gle](https://github.com/iogf/gle)
    - 25 Stars, 3 Fork

A tiny but functional google searcher lib.

(`是也乎:`

Glee ?

)


- [facebook-dl](https://github.com/sdushantha/facebook-dl)
    - 24 Stars, 0 Fork

Download facebook videos from your terminal

(`是也乎:`

同感觉工具作者 youtube-dl 的嗯哼?

)


- [2018-Tencent-social-advertising-algorithm-contest](https://github.com/liupengsay/2018-Tencent-social-advertising-algorithm-contest)
    - 24 Stars, 7 Fork

(`是也乎:`

我大鹅厂的嗯哼....`儿须成名酒须醉_v2`

)


- [Switchable_Normalization-Tensorflow](https://github.com/taki0112/Switchable_Normalization-Tensorflow)
    - 11 Stars, 0 Fork

Simple Tensorflow implementation of "Switchable Normalization"

(`是也乎:`

![transfer](https://github.com/taki0112/Switchable_Normalization-Tensorflow/raw/master/assests/transfer.png)

叕一种...
支持的越越嗯哼

![comparison](https://github.com/taki0112/Switchable_Normalization-Tensorflow/raw/master/assests/comparison.PNG)

)


- [Autopilot](https://github.com/akshaybahadur21/Autopilot)
    - 10 Stars, 3 Fork

A self driving car model for humans.

(`是也乎:`

嗯哼? 现在自动驾驶已经泛滥到这种程度了?

![Autopilot](https://github.com/akshaybahadur21/Autopilot/raw/master/final.gif)


好吧, 这就 监介 了...

)


- [Face-Recognizer](https://github.com/junior08/Face-Recognizer)
    - 9 Stars, 0 Fork

A Face Recognition system that works in real time!

(`是也乎:`

真实时人脸识别注册系统

![live](https://github.com/junior08/Face-Recognizer/raw/master/live.gif)

最近几期都有这些印度小哥哥的嗯哼...

)


- [sortr.py](https://github.com/IsraelAdura/sortr.py)
    - 6 Stars, 0 Fork

sort files using python

(`是也乎:`

工程名用 `.py` 后缀的实在是直男
)


- [alacrity](https://github.com/vishnuvardhan-kumar/alacrity)
    - 4 Stars, 2 Fork

Quickstart your Python project with a single handy command.

(`是也乎:`

叕一个工程脚手架工具.

)


- [Smarties](https://github.com/anisayari/Smarties)
    - 3 Stars, 0 Fork

Smarties is a Text Classifier using an innovative method based on Wikipedia to classify any documents/text. We use a Machine Learning and Doc2Vec algorithms.

(`是也乎:`

还以为是锤子的作品...

)


- [naz](https://github.com/komuw/naz)
    - 0 Stars, 0 Fork

naz is an SMPP client. It's name is derived from Kenyan hip hop artiste, Nazizi. 

(`是也乎:`

好久没见 SMPP 的嗯哼了

)


### (￣▽￣)

- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)



*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180710 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180710 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


