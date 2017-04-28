Title: 蠎加载 120
Slug: importpython-120
Date: 2017-04-14 11:11
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 120](http://importpython.com/newsletter/no/120/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [介绍 NoDB - S3 的 Pythonic 对象存储](https://blog.zappa.io/posts/introducing-nodb-pythonic-data-store-s3)
    + aws, s3, datastore

Pythonic object store based on Amazon's S3 static file storage. NoDB isn't a database.. but it sort of looks like one! It sort of does for databases what Zappa did for web servers. That's a bit of a stretch, but it's a step in that direction. It's mostly useful for prototyping, casual hacking, and (maybe) even low-traffic server-less databases for Zappa apps!

(`是也乎:`

Zappa 的动力根本.
)

- [为 Dummies 创建语言](https://ralsina.me/weblog/posts/creating-languages-for-dummies.html)
    + parsing, PyParsing

In this article I will explain how to go from nothing to a functioning, extensible language, using Python and PyParsing.

(`是也乎:`

如何从头构建一门语言? 使用 PyParsing, 傻瓜都能...
)

- [Zen of Python](https://medium.com/getpy/zen-of-python-aa432db216f5)
    + core-python

Know more about the Zen of Python

(`是也乎:`

必须推荐中文版本译集了: **[蠎之禅](http://wiki.woodpecker.org.cn/moin/PythonZen)**

)


- [数据争吵101: 用 Python 来获取/操纵/可视化 NBA 数据](http://blog.yhat.com/posts/visualize-nba-pipelines.html)
    + data science

This is a basic tutorial using pandas and a few other packages to build a simple datapipe for getting NBA data. Even though this tutorial is done using NBA data, you don't need to be an NBA fan to follow along. The same concepts and techniques can be applied to any project of your choosing. This is meant to be used as a general tutorial for beginners with some experience in Python or R.


- [谦卑的 Python Book Bundle](http://4url.in/XvOn23O8/)
    + books, nostarch

Humble Bundle By No-Starch. Python Books presented by No Starch Press (pay what you want and help charity)

(`是也乎:`

好书一堆才 1$
)

- [如何用 Twilio, Python 和 Google 自动化我的婚礼](https://www.twilio.com/blog/2017/04/wedding-at-scale-how-i-used-twilio-python-and-google-to-automate-my-wedding.html)
    + automation

(`是也乎:`

是的 google 手机+SMS 服务
)

- [Kim: 又一个 JSON 序列化和编组框架](http://kim.readthedocs.io/en/latest/)
    + serialization

Kim is a feature packed framework for handling even the most complex marshaling and serialization requirements. Web framework agnostic - Flask, Django, Framework-XXX supported!, Highly customisable field processing system, Security focused, Control included fields with powerful roles system, Handle mixed data types with polymorphic mappers, Marshal and Serialize nested objects.


- [你可以通过分析一百万 Yelp 评论来了解食物?](http://nbviewer.jupyter.org/github/skipgram/modern-nlp-in-python/blob/master/executable/Modern_NLP_in_Python.ipynb)
    + spaCy, topic modeling


- [A Quick Link Previewer for Mattermost](https://bfontaine.net/blog/2017/04/09/a-quick-link-previewer-for-mattermost/)


- [使用Python中的长时间内存网络进行时间序列预测](http://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/)
    + machine learning

The Long Short-Term Memory recurrent neural network has the promise of learning long sequences of observations. In this tutorial, you will discover how to develop an LSTM forecast model for a one-step univariate time series forecasting problem.

(`是也乎:`

内存便宜到应该视作硬盘了
)

- [PyBites – 如何写一个带有可选参数的装饰器?](http://pybit.es/decorator-optional-argument.html)

- [大图机器学习: Classifying Text with Neural Networks and TensorFlow](https://medium.freecodecamp.com/big-picture-machine-learning-classifying-text-with-neural-networks-and-tensorflow-d94036ac2274)
    + machine learning

- [Python 中的异步编程](http://djangostars.com/blog/asynchronous-programming-in-python-asyncio/)
    + async

(`是也乎:`

![new_v1_async](http://djangostars.com/blog/content/images/2017/04/new_v1_async.jpg)

美女作者

)


- [Python 中的高级 web 抓取](https://medium.com/dualcores-studio/advanced-web-scraping-in-python-d19dfccba235)
    + scraping

- [Python TensorFlow 教程 - 构建神经网络 - 探险机器学习](http://adventuresinmachinelearning.com/python-tensorflow-tutorial/)
    + tensorflow



## 好物
~ 包/模块/库/片段...

- [apistar](https://github.com/tomchristie/apistar)
    - 680 Stars, 96 Fork

agate is a Python data analysis library that is optimized for humans instead of machines. It is an alternative to numpy and pandas that solves real-world problems with readable code.

(`是也乎:`

针对人优化的数据分析库...
)

- [apistar](https://github.com/tomchristie/apistar)
    - 438 Stars, 16 Fork

A fast and expressive API framework. For Python.

(`是也乎:`

又一个快速 API 框架
)


- [treelstm.pytorch](https://github.com/dasguptar/treelstm.pytorch)
    - 31 Stars, 5 Fork

Tree LSTM implementation in PyTorch.

- [unpossibly-instagram-challenge](https://github.com/alexeygrigorev/unpossibly-instagram-challenge)
    - 30 Stars, 5 Fork

Predicting the number of likes an instagram post will receive in 24 hours - winning solution.

- [NoDB](https://github.com/Miserlou/NoDB) 
    - 24 Stars, 2 Fork

NoDB isn't a database.. but it sort of looks like one. 

(`是也乎:`


![NoDB](https://camo.githubusercontent.com/254c27c27321b63cca5a52cc6961237aeee62e33/687474703a2f2f692e696d6775722e636f6d2f5a796d465a64382e6a7067)

冲这 logo 就值得一试

![Zappa](https://camo.githubusercontent.com/be05103c626a5afe18dc4b1208a4b465dbd9e731/687474703a2f2f692e696d6775722e636f6d2f6631504a7843512e676966)

的动力来源 ;-)

--> ![嗯哼](https://camo.githubusercontent.com/e75910ea17c3d412cd064ff4b456adc39a8a6efa/68747470733a2f2f73332d75732d776573742d322e616d617a6f6e6177732e636f6d2f6173736574732e736974652e7365727665726c6573732e636f6d2f696d616765732f7365727665726c6573735f6672616d65776f726b5f76315f642e676966)

哈...

)



### (￣▽￣)

- [tankywoo/simiki](https://github.com/tankywoo/simiki)
    + 657 Stars, 95 Fork

Simiki is a simple wiki framework, written in Python.

(`是也乎:`

知道创宇 成员私人作品 md 的静态维基
)

# 是也乎

- 170413 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170413 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


