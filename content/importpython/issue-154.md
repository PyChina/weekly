Title: 蠎加载 154
Slug: importpython-154
Date: 2017-12-10 18:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 154](http://importpython.com/newsletter/no/154/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [专访:站在数据科学最重要工具背后的人](https://qz.com/1126615/the-story-of-the-most-important-tool-in-data-science/)
    + pandas

Interview with none other then Wes McKinney of Pandas.

(`是也乎:`

Pandas 之父 Wes McKinney  ....

)

- [优化ed Python](https://www.revsys.com/tidbits/optimized-python/)
    + docker

Turns out there are some optimizations you can do when compiling Python 3.5 and 3.6 that give you some significant speed improvements without any real downside. We've paired with with Google's base Debian image that rips out systemd and all it's dependencies which yields a MUCH smaller image.  

(`是也乎:`

也就是说专用版本的 Python 发行有了标准的渠道

)

- [概率论基础 - Peter Norvig](http://nbviewer.jupyter.org/url/norvig.com/ipython/Probability.ipynb)
    + probabilty

This notebook covers the basics of probability theory, with Python 3 implementations. (You should have some background in probability and Python.)


(`是也乎:`

叕一个 py3 完成的基础学科教程

)

- [比较5个数据可视化 Python 工具](https://medium.com/@ekirzhner/overview-of-python-data-visualization-tools-e32e1f716d10)
    + visualization

It could be challenging to pick the right data visualization tool in Python. There are so many options available. Summarizing most common tools, then testing and comparing different techniques would help to pick the best fit and method for the needed visualization.

(`是也乎:`

5大常见数据可视化框架的比较:

果断 Bokeh 最均衡

)


- [misocoin](https://github.com/kendricktan/misocoin)
    + bitcoin

Barebones bitcoin-like protocol implemented in Python 3.6.

(`是也乎:`

叕一个 Btc-样 协议框架

)

- [Python 3 整备](http://py3readiness.org/)
    + pypi

This site shows Python 3 support for 360 most downloaded packages on PyPI.

(`是也乎:`

动态统计 py 3 环境下载使用频率最高的 Top 360 包

)

- [推荐引擎 - Yelp](https://nick-morgan.github.io/Python-Recommendation-Engine-Yelp/)
    + machine learning

Using user review data from Yelp, our aim was to develop a recommendation system to provide a new restaurant suggestion that a user might like. The project was motivated by the fact that recommendation problems are ubiquitious, including the infamous Netflix challenge and "similar items you might like" suggestions from Amazon. Given the diverse application of this problem, we wanted to learn how to develop and implement such system using machine learning.

(`是也乎:`

实战的推荐系统架构经验

)


- [html5lib-python 1.0 released](http://bluesock.org/~willkg/blog/dev/html5lib_1_0.html)
    + open source, new release

Yesterday, Geoffrey released html5lib 1.0 [1]! The changes aren't wildly interesting.The more interesting part for me is how the release happened. I'm going to spend the rest of this post talking about that. Those looking to manage / understand the workings behind becoming a maintainer of a open source project should read this.


(`是也乎:`

叕一个尝试嗯哼 H5 的库...

)

- [为 Selenium Chrome 和 Python 设置 Digital Ocean 服务器](http://jonathansoma.com/lede/algorithms-2017/servers/setting-up/)
    + testing

(`是也乎:`

FF 发疯关闭 扩展渠道后, 基于 Chrome 扩展的工具就多了起来...

)

- [用 Wallaroo 在 Python 中嗯哼 Multi-Stream 处理](https://blog.wallaroolabs.com/2017/12/stateful-multi-stream-processing-in-python-with-wallaroo/)
    + distributed computing

Wallaroo is a high-performance, open-source framework for building distributed stateful applications.

(`是也乎:`

叕一个分布式计算框架

)


- [Kaggle 内核简介](https://towardsdatascience.com/introduction-to-kaggle-kernels-2ad754ebf77)
    + machine learning

On this episode of AI Adventures, find out what Kaggle Kernels are and how to get started using them. Though there’s no popcorn in this episode, but I can assure that Kaggle Kernels are popping!

(`是也乎:`

叕一个 ML 入门教材

)


- [用 Python 优化你的 Cryptocurrency 组合](https://medium.com/@geenty/optimizing-your-cryptocurrency-portfolio-with-python-4c3d4c824a7f)
    + cryptocurrency

Bitcoin is now mainstream. While the debate on whether it’s a speculative bubble or the greatest thing since the internet continues, one thing that is irrefutable is that it has attracted a significant amount of investor interest to cryptocurrency and digital assets.

(`是也乎:`

数字货币的入门最佳姿势, 总是从 py 开始...
)


- [在 Python 中更专业的嗯哼日期时间对象](https://medium.com/@itruong/dealing-with-datetimes-like-a-pro-in-python-fb3ac0feb94b)
    + datetime

(`是也乎:`

多谢 @Geek Cheng 的嗯哼, 
一时不查露过了机器翻译的...

)

- [使用 Apache Spark DataFrames API 进行结构化流式传输](https://medium.com/@irfanalidv/structured-streaming-using-apache-spark-dataframes-api-497a52ea0180)
    + spark

- [使用 Facebook 的 Prophet 库预测比特币价格](https://medium.com/@joshua_e_k/forecasting-bitcoin-prices-using-facebooks-prophet-library-9cfce74e414c)
    + prediction

This is just a quick post to show how you can use Facebook’s Prophet forecasting library in python to forecast bitcoin hourly bitcoin prices.



- [介绍 pymatch 包](https://medium.com/@bmiroglio/introducing-the-pymatch-package-6a8c020e2009)
    + pymatch

The pymatch Python package implements Propensity Score Matching (PSM) techniques intended for use with observational study designs. It was inspired by and adapted from Jasjeet Singh Sekhon’s Matching package in R. I wrote an adaptation in Python that is better suited for my work at Mozilla

(`是也乎:`

倾向分数匹配（PSM）技术,
Mozilla 适用版本...
)

## 好物
~ 包/模块/库/片段...

- [chubin/rate.sx](https://github.com/chubin/rate.sx)
    - 48 Stars, 4 Fork

curl cryptocurrencies exchange rates

(`是也乎:`


![rate.sx](https://camo.githubusercontent.com/8abaea5abddcfa520a517628e0d9c709ec5c67de/687474703a2f2f726174652e73782f66696c65732f73637265656e73686f742e706e67)

又一个 CLI 数字交易工具...

通过 cURL 来使用的软件,才是真正的绿色软件哪...

)


- [powerfulseal](https://github.com/bloomberg/powerfulseal)
    - 24 Stars, 1 Fork

A powerful testing tool for Kubernetes clusters.

(`是也乎:`

叕一个 K8s 支持工具.

)

- [scenescoop](https://github.com/cvalenzuela/scenescoop)
    - 13 Stars, 0 Fork

A tool to describe the content of videos and suggest similar scenes in other videos/films.

(`是也乎:`

对视频进行自动识别和自然挑选的 web 工作站: 对海量视频资源进行文本指令的基础

![scenescoop](https://github.com/cvalenzuela/scenescoop/raw/master/static/imgs/img.png)

)

- [richtext.org](https://github.com/kennethreitz/richtext.org)
    - 11 Stars, 0 Fork

a place to share things.

(`是也乎:`

基于:

    Django 2.0
    Postgres or DynamoDB
    "HTML5"
    Heroku

手制的 gist

)


- [tensorpack-recipes](https://github.com/cgtuebingen/tensorpack-recipes)
    - 9 Stars, 0 Fork

A collection of TensorPack implementations including pretrained models.



- [pyznap](https://github.com/cythoning/pyznap)
    - 6 Stars, 0 Fork

ZFS snapshot tool written in python 

(`是也乎:`

sun 公司死后留下来的最宝贵遗产之一
重新定义了 FS...

)


### (￣▽￣)

- [重大改革：Python 语言将被加入高考科目，VB 惨被淘汰！](https://mp.weixin.qq.com/s/kaEUp2q0K3a_huQa9m_LZg) 为了孩子,中国家长们得开始学习 Python 了... 
- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)


## 是也乎

- 171210 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171210 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


