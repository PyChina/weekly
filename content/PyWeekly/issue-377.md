Title: 蠎周刊 377
Slug: issue-377
Date: 2018-12-16 21:21
Tags: Weekly,Python,ZH



原文: [Python Weekly - Issue 377](https://mailchi.mp/pythonweekly/python-weekly-issue-377?e=a4782d704d)

## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [修复Python中的严重内存泄漏](https://info.cloudquant.com/2018/12/numpyleaks)

A few of our power users reported that long-running backtests would sometimes run out of memory. These power-users are the people who often find new trading strategies and so we wanted to work with them to improve the performance of our backtesting tools. Over the past couple of weeks, our senior engineer found that the problem wasn’t in our code, but in one of the popular Python libraries that we use. We found the problem in numpy and numba. The leak was ultimately caused by how we were using these libraries.  We made the correction and as you can see from the following chart, it really improved the memory utilization for our trade simulator. The following is the write-up by our senior engineer so that others can learn from our engineering efforts.

- [pandas 库将来准备干什么?](https://www.dataschool.io/future-of-pandas/)
    + pandas

pandas is a very popular Python library for data analysis, manipulation, and visualization, but it still hasn't reached version 1.0. What&#x27;s next for pandas?

- [gpython: 用Go编写的Python解释器 "不含电池"](https://blog.gopheracademy.com/advent-2018/gpython/)
    + py3,interpreter

Gpython is a Python 3.4 interpreter written in Go. This is the story of how it came to be, how it works and where it is going. This includes a quick run through how an interpreted language like Python/Gpython works with a dip into the Virtual Machine (VM), lexing source, parsing it and compiling to byte code.

(`是也乎:`

叕一个 VM , 只是 JVM 上的 python 实现一直比不过 coljure 的 PR 哪

)


- [介绍用 Python 进行 Web 抓取](https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-a2601e8619e5)
    + scraping

Let’s scrape a fictional book store’s website with BeautifulSoup!

- [构建自动驾驶 Q-Bot](https://medium.com/@michael_87060/build-a-self-driving-q-bot-6aa67ba60769)
    + Self-Driving,AI

All it takes is a 3-d printer, some Python, and lots of trial and error

- [用 Twilio 在 Python 中构建无服务器 SMS Raffle](https://www.twilio.com/blog/twilio-serverless-sms-raffle-python-lambda)
    + SMS,Serverless

Create a serverless SMS raffle in Python using Amazon Lambda, API Gateway, and DynamoDB with Twilio Programmable SMS.

- [Five Things You Didn't Know Python Can Do](https://www.youtube.com/watch?v=WlGkBqBRsik)
    + FAQ

(`是也乎:`

All Things Open 2018 - Nina Zakharenko, Microsoft 

M$ MM 总结 28岁的 Python 还能作什么...
)

- [如何纠正你的 Python 代码风格?](https://www.caktusgroup.com/blog/2018/12/10/how-to-fix-python-code-style/)
    + PEP8

- [用 Python 和 Selenium 在酒店免费上 Wifi](https://gkbrk.com/2018/12/free-hotel-wifi-with-python-and-selenium/)
    + auto

- [通过深度强化学习嗯哼个 Pong AI ](https://blog.floydhub.com/spinning-up-with-deep-reinforcement-learning/)

- [Python 在 Microsoft: 雷达下飞行](https://medium.com/microsoft-open-source-stories/python-at-microsoft-flying-under-the-radar-eabbdebe4fb0)

- [Keras – 保存并加载您的深度学习模型](https://www.pyimagesearch.com/2018/12/10/keras-save-and-load-your-deep-learning-models/)

- [如何从 Jupyter Notebooks 中自然扩展出有整洁架构的软件?](https://github.com/guillaume-chevalier/How-to-Grow-Neat-Software-Architecture-out-of-Jupyter-Notebooks)
    + ipynb

(`是也乎:`

文档/调试/运行 3合一 的环境很舒服, 
但是, 从来不是一个可发行为用户软件的嗯哼,
其实, 也可以的...

)


- [用Python 3, AWS Lambda,Twilio Lookup 和 SMS 识别未知电话号码](https://www.twilio.com/blog/identify-unknown-phone-numbers-python-3-aws-lambda-lookup-sms)

- [从Jupyter Notebook安装Python包](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

(`是也乎:`

等等, 可是为什么哪...

)


## 好物
> Interesting Projects, Tools and Libraries

- [PracticalAI](https://github.com/GokuMohandas/practicalAI)
    + ML,DL,AI

A practical approach to learning machine learning.

- [loguru](https://github.com/Delgan/loguru)
    + logging

Python logging made (stupidly) simple.

(`是也乎:`

![demo](https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/demo.gif)

![logo](https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/logo.png) 大师一点儿也不简单...

一个好用又稳定的logging 太难以嗯哼了.


)


- [DGL](https://github.com/dmlc/dgl)
    + DL,ML,AI

Python package built to ease deep learning on graph, on top of existing DL frameworks. 

- [completion_utils](https://github.com/CarvellScott/completion_utils)
    + CLI,zsh...

A small utility to assist in writing shell completions in python instead of bash, fish, zsh, etc.

- [Athena](https://github.com/M4cs/Athena)
    + CLI,

General User Interface for the Theos Tweak Development Framework.

(`是也乎:`

![Athena](https://camo.githubusercontent.com/f1081783219ae24086c20e8dc23e01d2ae176088/68747470733a2f2f692e696d6775722e636f6d2f65474336314c5a2e706e67)

)


- [DynamicForms](https://github.com/velis74/DynamicForms)
    + DRF, django

DynamicForms performs all the visualisation & data entry of your DRF Serializers & ViewSets and adds some candy of its own: It is a django library that gives you the power of dynamically-shown form fields, auto-filled default values, dynamic record loading and similar candy with little effort.


- [crudcast](https://github.com/chris104957/crudcast)
    + API, REST,YAML

Create and deploy a RESTful API with a few lines of YAML.


(`是也乎:`

YAML 的表述能力...唉

)


- [secure](https://github.com/cakinney/secure)
    + http,cookies, Securety

Secure 🔒 headers and cookies for Python web frameworks



- [Varken](https://github.com/Boerderij/Varken)
    + CLI,DBA,Plex/InfluxDB/Grafana

Standalone command-line utility to aggregate data from the Plex ecosystem into InfluxDB.

(`是也乎:`

![Varken](https://camo.githubusercontent.com/92aff9b739e4f7310e15aa2bf1fe8cf65360af0c/68747470733a2f2f692e696d6775722e636f6d2f617638653048502e706e67)

)



- [terracotta](https://github.com/DHI-GRAS/terracotta)
    + Flask , Rasterio, AWS ,lambda

A light-weight, versatile XYZ tile server, built with Flask and Rasterio.

(`是也乎:`

![logo](https://github.com/DHI-GRAS/terracotta/raw/master/docs/_figures/logo-banner.svg?sanitize=true)


![preview](https://github.com/DHI-GRAS/terracotta/raw/master/docs/_figures/workflow-preview.png)

)



- [pyAudioClassification](https://github.com/98mprice/pyAudioClassification)
    + Audio

Dead simple audio classification 🎶

(`是也乎:`

Py3 only 的声音分析基础模块
)

- [python-chirp](https://github.com/concretecloud/python-chirp)
    + TLS,message

Message-passing for everyone.

(`是也乎:`

![chirp](https://raw.githubusercontent.com/concretecloud/chirp/master/doc/_static/chirp.png)

内网消息

)


- [wtfiswronghere](https://github.com/qxf2/wtfiswronghere)
    + 101,error

A collection of simple errors that beginners are likely to hit when they start writing Python.

(`是也乎:`

> WTF ...

用心了...


)


- [SSD](https://github.com/lufficc/SSD)
    + PyTorch, SSD 

High quality, fast, modular reference implementation of SSD in PyTorch 1.0.

(`是也乎:`

简单的说 SSD 不是硬盘,得有专门的嗯哼姿势...
)



## 新放
> New Releases

- [PyTorch 1.0](https://github.com/pytorch/pytorch/releases/tag/v1.0.0)
    + 嗯哼,终于1.0 了
- [Python 3.7.2rc1 和 3.6.8rc1](https://blog.python.org/2018/12/python-372rc1-and-368rc1-now-available.html)


## DAMA
(`大妈私人无责任播报`)

# 是也乎

- 181205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 181205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
