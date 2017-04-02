Title: 蠎加载 118
Slug: importpython-118
Date: 2017-03-31 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 118](http://importpython.com/newsletter/no/118/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...





- [和 Python 一起来玩 猴子补丁](http://hundredminutehack.blogspot.com/2017/03/fun-with-python-and-monkey-patching.html)
    + monkey patching

Monkey patching is about replacing attributes of a Python thing with other attributes. Let's use the word "thing" very loosely and have some fun.

(`是也乎:`

.... unless you really want to. ;-)

讲真, 能作, 和应该作,完全不同, 老老实实平平淡淡干干净净的写代码是最好的了...
)


- [通过 Zipkin 在 Python 应用中引入分布式跟踪](http://echorand.me/introducing-distributed-tracing-in-your-python-application-via-zipkin.html)
    + monitoring, distributed

Distributed tracing is the idea of tracing a network request as it travels through your services, as it would be in a microservices based architecture. The primary reason you may want to do is to troubleshoot or monitor the latency of a request as it travels through the different services.

(`是也乎:`

主要面向微服务...跨进程/主机/机房...
)


- [如何在 Python 中使用 Numpy 描述符统计](http://www.pybloggers.com/2017/03/how-to-do-descriptives-statistics-in-python-using-numpy/)
    + numpy, statistics

The descriptive statistics we are going to calculate are the central tendency (in this case only the mean), standard deviation, percentiles (25 and 75), min, and max.

- [介绍 Pandas 进行数据分析 - 101](https://medium.com/@devopslearning/introduction-to-pandas-for-data-analysis-c14bb9b1c21b)
    + pandas

pandas is a software library written for the Python programming language for data manipulation and analysis.

(`是也乎:`

讲真 Pandas 真的很好用, 前提是数据清洗的要好...
)


- [Google Cloud 上的 GPU 上跑 Jupyter notebooks](https://medium.com/@durgeshm/containerized-jupyter-notebooks-on-gpu-on-google-cloud-8e86ef7f31e9)
    + docker, jupyter

In a previous post, I listed out the steps to run Jupyter notebooks on GPU instances on GCP Compute Engine. It turns out, there is a much easier and more flexible way. Using Docker containers.

(`是也乎:`

GUP 在 GCP 中已经成为一个实体对象可以创建了,
然后 CUDA 的协助下, Jupyter 就能跑了...
)

- [说,这是什么? TensorFlow](https://www.oreilly.com/learning/caption-this-with-tensorflow)
    + TensorFlow

In this article, we will walk through an intermediate-level tutorial on how to train an image caption generator on the Flickr30k data set using an adaptation of Google’s Show and Tell model. We use the TensorFlow framework to construct, train, and test our model because it’s relatively easy to use and has a growing online community.

(`是也乎:`

![caption](https://d3ansictanv2wj.cloudfront.net/image-02-946136968ac62fa1138aab6263098455.jpg)

其实, 一切都被部署在云端了, 具体怎么来的,谁也不知道,
反正 google 知道, 大家用的越多, 他们就识别的越快...

然后, 再也没有公司能赢的了 google 了.

)

- [Python 中用 感知散列 进行重复图像检测](http://tech.jetsetter.com/2017/03/21/duplicate-image-detection/)
    + image processing

Jetsetter has hundreds of thousands of high-resolution travel photos, and we’re adding lots more every day. The problem is, these come from a variety of sources and are uploaded in a semi-automated way, so there are often duplicates or almost-identical photos that sneak in. And we don’t want our photo search page filled with dupes.

(`是也乎:`

所谓 dHASH, 将
![原图](http://tech.jetsetter.com/public/img/dupes-diver-large.jpg)

--> 劣化为

![特征图](http://tech.jetsetter.com/public/img/dupes-diver-gray-square.png)

来加速对比
)

- [用 Python 管理 corn 任务](https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231)
    + cron

- [Luigi: 一个 ExternalProgramTask 示例 – 将 JSON 转换为 CSV](http://www.markhneedham.com/blog/2017/03/25/luigi-externalprogramtask-example-converting-json-csv/)
    + luigi

I’ve been playing around with the Python library Luigi which is used to build pipelines of batch jobs and I struggled to find an example of an ExternalProgramTask so this is my attempt at filling that void.


- [如何用 Selenium 嗯哼 Python - 完整教程](https://hackernoon.com/how-to-use-selenium-with-python-complete-tutorial-ed1e4832f3a5)
    + Selenium

(`是也乎:`

Windows 中的 Eclipse+PyDev 的依赖...弃疗...

)

- [Tutorial: Using MTurk together with AWS Lambda](https://blog.mturk.com/tutorial-using-mturk-together-with-aws-lambda-c91d414496d3?source=rss------python-5)
    + aws

- [用 MicroPython 和 NodeMCU 构建 IoT 启动电源](https://kushaldas.in/posts/building-iot-enabled-power-strip-with-micropython-and-nodemcu.html)
    + IOT

- [在 Python 中从 bytes 到 strings 然后再回来](http://wordaligned.org/articles/from-bytes-to-strings-in-python-and-back-again)
    + core-python

(`是也乎:`

反正这段公案是可以长长久久说下去的...
)


- [理解 Python3 中的类和实例变量](https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3)
    + core-python

(`是也乎:`

反正都不一样了...
)

- [音频应用程序音频信号处理（Python，NumPy，SciPy，Matplotlib等）](https://www.coursera.org/learn/audio-signal-processing)
    + Audio

About this course: In this course you will learn about audio signal processing methodologies that are specific for music and of use in real applications. We focus on the spectral processing techniques of relevance for the description and transformation of sounds, developing the basic theoretical and practical knowledge with which to analyze, synthesize, transform and describe audio signals in the context of music applications.

(`是也乎:`

又一大课程
)


- [PyData Tel Aviv Meetup: 闪电演讲 - Pandas tips & tricks](https://www.youtube.com/watch?v=HnwUpnnXlOw&feature=youtu.be&t=37m31s)
    + pandas, video

Pandas tips and tricks video

(`是也乎:`

特拉维夫 聚会,当然的有 Youtube 自动生成的字幕, 足够快速嗯哼...

全程单手 Jupyter 演示下来, 没有幻灯..
)



## 好物
~ 包/模块/库/片段...

- [poline](https://github.com/riolet/poline)
    - 160 Stars, 6 Fork

Python one-liners: Awk-like one-liners for python

(`是也乎:`

流水线操作, 广州齐昌的赖总5年前就发布过类似的模块...

)

- [TensorFlow-TransX](https://github.com/thunlp/TensorFlow-TransX)
    - 17 Stars, 3 Fork

An implementation of TransE and its extended models for Knowledge Representation Learning on TensorFlow



- [travis-python-template](https://github.com/jakevdp/travis-python-template)
    - 7 Stars, 0 Fork

Small template for setting up Travis CI with Python.

(`是也乎:`

就喜欢这种脚手架式的分享, 可以加速常用目标的达成
)

- [pdf2thumb](https://github.com/salmedina/pdf2thumb)
    - 4 Stars, 0 Fork

This little program generates a thumbnail of a certain pdf for quick visualization. It is based on ImageMagick as it has all the functionality required.

(`是也乎:`

![pdf2thumb](https://github.com/salmedina/pdf2thumb/raw/master/demo/report_5.png)

实用...快速将 pdf 文档嗯哼成缩略图

)

- [microURL](https://github.com/francium/microURL)
    - 3 Stars, 2 Fork

URL shortener written in Python + Flask.

(`是也乎:`

又一个缩址服务,使用 MySQL ....
)

- [Relatively-Sized-Progress-Bar](https://github.com/cjoeml/Relatively-Sized-Progress-Bar)
    - 3 Stars, 0 Fork

Creates a progress bar that is sized dynamically to the current terminal window size.

(`是也乎:`

![Relatively](https://camo.githubusercontent.com/beab4154ba9296407556979bab8f00d11a0c5b0d/68747470733a2f2f63732d70656f706c652e62752e6564752f636a6f652f6f7574707574322e676966)

问题是如何同程序行为结合....
)


- [PyData-TLV-Talk](https://github.com/alonnir/PyData-TLV-Talk)
    - 1 Stars, 0 Fork

Notebook for my PyData TLV talk on Pandas tips & tricks

(`是也乎:`

又一个 Pandas 使用技巧 .ipynb 小书...

)

### (￣▽￣)
~ 

# 是也乎

- 170402 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170331 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


