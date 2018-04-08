Title: 蠎加载 170
Slug: importpython-170
Date: 2018-04-08 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 170](http://importpython.com/newsletter/no/170/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Slicker: 用 Python 来移动东西的工具 | Khan Academy Engineering](http://engineering.khanacademy.org/posts/slicker.htm)
    + slicker

Craig talked last post about our project to reorganize our whole Python codebase. This entails a lot of architectural challenges – deciding where to put each file, prioritizing which files and classes to split, and so on – which Carter will talk about more in the final post of this series. Today, I want to set all that aside to focus on the more mechanical process of moving: what does it take to move thousands of files, classes, and functions, each of which may be referenced by dozens or hundreds of others? We ended up writing a tool called Slicker to do it all, and the remainder of this post talks about why we needed it and how it works.


(`是也乎:`

针对移动大量文件这一基础命题, 可汗学院嗯哼出了一大套课程...

)

- [嫑写 Idiomatic Python](https://medium.com/@robmuh/dont-write-idiomatic-python-ef03d5389950)
    + idiomatic python

Write Understandable Code. There are two sides to every story :)

(`是也乎:`

传统-反传统-约定-反约定...

好象 蠎之 Zen 中就说了相关决策原则...

)


- [用 Brexit 在 Python 中分析 Tweets 情感](https://datascienceplus.com/brexit-tweets-sentiment-analysis-in-python/)
    + sentimentanalysis

Sentiment analysis is a method of analyzing a piece of text and deciding whether the writing is positive, negative or neutral. It is commonly used to understand how people feel about a topic.



- [不仅是 Python 的另一个 YOLO V3](https://medium.com/@madhawavidanapathirana/not-just-another-yolo-v3-for-python-79da6c3af082)
    + image processing

If you are interested on Computer Vision, then you have probably heard about YOLO by now. YOLO?—?“You Only Look Once” is a fast, real-time technique for object detection.

(`是也乎:`

[YOLO — “You Only Look Once”](https://pjreddie.com/darknet/yolo/)

只用看一眼 ~ 物件识别模块名称, 起名学功力很够 ;-)

全新实现的: [madhawav/YOLO3-4-Py: A Python wrapper on Darknet. Compatible with YOLO V3.](https://github.com/madhawav/YOLO3-4-Py)

基本上就是大规模人流监控的基本模块了...

)

- [Python 的多线程](https://aaronlelevier.github.io/multithreading-in-python/)
    + multithreading

This blog post is about Processes, Threads, and the GIL in Python. Because of the way that the Python GIL operates, it may be different than one initially expects, so this blog post is an attempt to discuss this in more detail.

- [通过 Python 了解区块链](https://blockchain.works-hub.com/learn/learning-about-blockchain-with-python-67736?utm_source=BCW%20(JG)&utm_medium=Reddit)
    + blockchain

About two weeks ago I realized why I had such an animosity towards bitcoin: I didn’t own any and I didn’t understand it. I decided to start learning about bitcoin through researching the technology behind it, aka block chain. I learned through creating a python script that builds a block chain, so I thought I would share it with others who would like to learn more about block chain. To clarify, while I was inspired by bitcoin, this post is focused on block chain.

(`是也乎:`

其实: [区块链随想录——一种设想中的公链架构 - 简书](https://www.jianshu.com/p/d2f1e9bd56ea)

![blockchain](https://upload-images.jianshu.io/upload_images/10072-df795c294f941a78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

)


- [成千上万错误配置的 Django 应用泄露敏感数据](https://securityaffairs.co/wordpress/70869/hacking/django-apps-misconfigured.html)
    + django, debugmode

The security researcher Fábio Castro discovered tens of thousands of Django apps that expose sensitive data because developers forget to disable the debug mode.

(`是也乎:`

PHP/MySQL/MongoDB/... 现在终于到了 Django,
凡是大规模嗯哼的, 必定基于默认配置暴露各种嗯哼...

)


- [Nathaniel's Python 从 Go 中学到的经验教训](http://nathanielobrown.com/blog/posts/python_lessons_learned_from_go.html)
    + golang

Go is cool. Python type annotations with mypy are cool. Go has influenced how I write Python.

(`是也乎:`


Gopher 和 Pythonista 一直是水乳交融的

)


- [gopro-py-api: 非官方 Python 版 GoPro API库](https://github.com/konradit/gopro-py-api)
    + gopro

Unofficial GoPro API Library for Python - connect to GoPro cameras via WiFi.

(`是也乎:`

叕一例硬件的非官方操控接口, 可想硬件的安全能力实在...

)


- [数据分析: Pandas 和 SQL 教俺平均值 | Opensource.com](https://opensource.com/article/18/4/analyzing-data-python)
    + pandas

Why data analysts should exercise caution when taking averages.



- [用高级 TensorFlow API 进行文本分类](https://medium.com/quantitative-technologies/text-classification-with-the-high-level-tensorflow-api-390809987a4f)
    + tensorflow

In this blog post we share our experience, in considerable detail, with using some of the high-level TensorFlow frameworks for a client’s text classification project. These include the Estimator framework and feature columns.


(`是也乎:`

目测, 所谓高级都是从 Google 一生产线退役的旧功能组件

)


## 好物
~ 包/模块/库/片段...

- [find-birds](https://github.com/karpathy/find-birds)
    - 219 Stars, 11 Fork

Find people you should follow on Twitter based on who the people you follow follow.

(`是也乎:`

找鸟...这名字实在忒贴切了

)

- [persistent-celery-beat-scheduler](https://github.com/richardasaurus2/persistent-celery-beat-scheduler)
    - 73 Stars, 0 Fork

persistent celery beat scheduler


(`是也乎:`

咱们的芹菜还在一线折腾哪

)

- [colab-tf-utils](https://github.com/Zahlii/colab-tf-utils)
    - 48 Stars, 8 Fork

Automatically backup keras/tensorflow models from Google's Colab service to your GoogleDrive based on a keras callback!

(`是也乎:`

Keras 生态叕一则实用工具

)


- [tvnet](https://github.com/LijieFan/tvnet)
    - 29 Stars, 13 Fork

End-to-End Learning of Motion Representation for Video Understanding

- [dedoop](https://github.com/edsu/dedoop)
    - 28 Stars, 0 Fork

recursively deduplicate a directory and write its contents to a new directory while remembering the old paths

(`是也乎:`

rsync 的一种劣化版再造?

)


- [learn-painting-the-hard-way](https://github.com/zedshaw/learn-painting-the-hard-way)
    - 22 Stars, 1 Fork

A Simple Introduction To The Application Of Pigment To A Surface To Look Like A Thing

- [aws-cost-explorer-report](https://github.com/aws-samples/aws-cost-explorer-report)
    - 10 Stars, 1 Fork

Python SAM Lambda module for generating an Excel cost report with graphs, including month on month cost changes. Uses the AWS Cost Explorer API for data.

(`是也乎:`

叕一个 AWS 价格监察工具, 可见 AWS 的收费已经到了一种境界..
)


- [wifi-graper](https://github.com/byt3bl33d3r/wifi-graper)
    - 8 Stars, 0 Fork

Automatically get internetz from access points that have MAC based filtering enabled

(`是也乎:`

![graper](https://user-images.githubusercontent.com/5151193/38379740-e894dff8-38be-11e8-89a4-3f6ee83665fc.jpg)

那什么, 万能wifi 的劣化单功能脚本?

)


- [keymaker](https://github.com/wbsdty331/keymaker)
    - 7 Stars, 0 Fork

Keymaker for VMware Products.

- [BrowsingHistoryVisualization](https://github.com/jehlokhande93/BrowsingHistoryVisualization)
    - 4 Stars, 0 Fork

Visualization of browsing history from Google data

- [django-highcharts-example](https://github.com/sibtc/django-highcharts-example)
    - 4 Stars, 0 Fork

Code samples used in the blog post "How to Integrate Highcharts.js with Django"

- [Playing-with-Asyncio](https://github.com/codingforentrepreneurs/Playing-with-Asyncio)
    - 4 Stars, 2 Fork

This series shows you the basics of how to use the Asyncio Library in Python.

(`是也乎:`

Asyncio 的安利还是要坚持哪...

)


- [django-coinpayments](https://github.com/Bearle/django-coinpayments)
    - 4 Stars, 0 Fork

Django package for handling payments via https://www.coinpayments.net

- [django-autoscroll](https://github.com/iogf/django-autoscroll)
    - 3 Stars, 0 Fork

Simplify implementing automatic scrolling in django.

- [hexsticker](https://github.com/fridex/hexsticker)
    - 3 Stars, 2 Fork

Create hexagon stickers automatically 

(`是也乎:`

![hexsticker](https://raw.githubusercontent.com/fridex/hexsticker/master/fig/output/selinon-sticker-4.png)

这种贴片图像的自动生成

)


### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180408 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180408 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


