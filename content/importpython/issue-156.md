Title: 蠎加载 156
Slug: importpython-156
Date: 2017-12-24 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 156](http://importpython.com/newsletter/no/156/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [贵宾犬/哈巴狗还是维也纳狗? 用 Python 和 Flask 部署一个 Dog Identification TensorFlow 模型](https://thenewstack.io/poodle-pug-weiner-dog-deploying-dog-identification-tensorflow-model-using-python-flask/)
    + machine learning

In this post, we’ll create a demo to see how simple it is to develop a machine learning-based service using Python’s Flask library.

- [在Python> = 3.6中唯一化列表的最快方法](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6)
    + core-python

This is an update to a old blog post from 2006 called Fastest way to uniquify a list in Python. But this, time for Python 3.6. Why, because Python 3.6 preserves the order when inserting keys to a dictionary. How, because the way dicts are implemented in 3.6, the way it does that is different and as an implementation detail the order gets preserved. Then, in Python 3.7, which isn't released at the time of writing, that order preserving is guaranteed.

- [与 Paige Bailey 来机器学习101- Podcast](https://www.hanselminutes.com/611/machine-learning-101-with-paige-bailey)
    + podcast

This week on the show Scott talks to Data Scientist and AI expert Paige Bailey. What's the difference between machine learning and deep learning? Do I need to learn R and Python to use machine learning models? Do models need to deploy regularly or can I use them forever? All these questions and more, this week!

- [用Python构建穷人的深度学习相机 - Make Art with Python](https://www.makeartwithpython.com/blog/poor-mans-deep-learning-camera/)
    + deep learning

Imagine being able to use a camera that’s able to tell when you’re playing a guitar, or creating a new dance, or just learning new skateboard tricks. It could use the raw image data to tell if you landed a trick or not. Or if you’re doing a new dance routine, what the series of poses are, and how they fit to the music.


- [Python Community is at its Peak at North Bay Python](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/qxjNSJdd5P8/community-is-at-its-peak-at-north-bay.html)
    + community

- [Generators <<- Functions (  R 程序猿视角)](http://koaning.io/generators-functions.html)
    + R

I got in a small argument at a meetup about R. Something about python being a BetterLanguage[tm] than R. One of the arguments was that python is better because the language has support for generators. This was an interesting moment because I definately agree that the way that generators work in python is great. I would even argue that there are parts in python that work better for many tasks than R might (and vise versa). But I wouldn't argue that R does not a very similar feature to generators in python, but they do require you to think differently.


- [您 Python Web 应用程序的性能如何？](http://agiliq.com/blog/2017/11/how-performant-your-python-web-application/)
    + performance

This post tries to explain web application performance. Performance means the number of requests per second that can be served by a deployed application.

- [Msgpack vs JSON（使用gzip）](https://www.peterbe.com/plog/msgpack-vs-json-with-gzip)
    + msgpack

I was curious, how much more efficient is Msgpack at packing a bunch of data into a file I can emit from a web service.




- [信用卡欺诈检测中的类不平衡 - 第1部分:理解对模型准确性的影响](http://blog.madhukaraphatak.com/class-imbalance-part-1/)
    + machine learning

Whenever we do classification in ML, we often assume that target label is evenly distributed in our dataset. This helps the training algorithm to learn the features as we have enough examples for all the different cases. For example, in learning a spam filter, we should have good amount of data which corresponds to emails which are spam and non spam.

- [Julia vs. Python: Julia语言在数据科学 | InfoWorld](https://www.infoworld.com/article/3241107/python/julia-vs-python-julia-language-rises-for-data-science.html#tk.rss_all)
    + datascience, julia

Python has turned into a data science and machine learning mainstay, while Julia was built from the ground up to do the job.

(`是也乎:`

所以, 在 Jupyter 的大光中其它数据分析语言, 也有了一丝活路?

)


- [Python Release Python 3.6.4](https://www.python.org/downloads/release/python-364/)
    + new release

Python 3.6.4 is the fourth maintenance release of Python 3.6.

- [2017年十大Python库 - Tryolabs Blog](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/?ref=hn)
    + packages


(`是也乎:`

分别是:

> [Pipenv](https://github.com/pypa/pipenv)

![Pipenv](https://camo.githubusercontent.com/2287c881cb3a045f4f70f20f0326ec4ef1474ccd/687474703a2f2f6d656469612e6b656e6e657468726569747a2e636f6d2e73332e616d617a6f6e6177732e636f6d2f706970656e762e676966)

> ; [PyTorch](http://pytorch.org/)
> ; [Caffe2](https://caffe2.ai/) ~ 叕一个 Fb 发现的 DSL 
> ; [Pendulum](https://github.com/sdispater/pendulum)
> ; [Dash](https://plot.ly/products/dash/)
> ; [PyFlux](https://github.com/RJT1990/pyflux)
> ; [Fire](https://github.com/google/python-fire) ~ 叕一个 CLI 工具构造框架
> ; [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
> ; [FlashText](https://github.com/vi3k6i5/flashtext) ~ 叕一个正则表达式增强工具
> ; [Luminoth](https://luminoth.ai/)

作者又额外推荐了:

> [PyVips](https://github.com/jcupitt/pyvips) ~ 全新的图片处理模块
> ; [Requestium](https://github.com/tryolabs/requestium) 
> ; [skorch](https://github.com/dnouri/skorch)
~ ![skorch](https://github.com/dnouri/skorch/raw/master/assets/skorch.svg?sanitize=true) PyTorch+scikit-learn

)



- [Python 中的简单线性回归](https://medium.com/@mjfstanford/simple-linear-regression-in-python-905b759ef0e6)
    + numpy, linear regression

Simple linear regression is a statistical method that allows us to summarise and study relationships between two continuous (quantitative) variables. I hope today to prove to myself that I understand and can demonstrate linear regression by coding it from scratch in Python without using Scikit Learn.

- [Episode #143 调整Python Web应用性能 - Podcast](https://talkpython.fm/episodes/show/143/tuning-python-web-app-performance)
    + podcast

Do you run a web application or web service? You probably do a couple of things to optimize the performance of your site. Make sure the database response quickly and more. But did you know a well of performance improvements live in your web servers themselves?

- [Copy-on-write 友好的Python垃圾回收 – Instagram Engineering](https://engineering.instagram.com/copy-on-write-friendly-python-garbage-collection-ad6ed5233ddf)
    + garbage collection

At Instagram, we have the world’s largest deployment of the Django web framework, which is written entirely in Python. We began using Python early on because of its simplicity, but we’ve had to do many hacks over the years to keep it simple as we’ve scaled. Last year we tried dismissing the Python garbage collection (GC) mechanism (which reclaims memory by collecting and freeing unused data), and gained 10% more capacity. However, as our engineering team and number of features have continued to grow, so has memory usage. Eventually, we started losing the gains we had achieved by disabling GC. 




## 好物
~ 包/模块/库/片段...

- [open-paperless](https://github.com/zhoubear/open-paperless)
    - 1204 Stars, 50 Fork

Scan, index, and archive all of your paper documents.

(`是也乎:`

叕一则国人作品

![logo](https://github.com/zhoubear/open-paperless/raw/master/contrib/logo.png)

)


- [nmtpytorch](https://github.com/lium-lst/nmtpytorch)
    - 245 Stars, 23 Fork

Neural Machine Translation Framework in PyTorch.

(`是也乎:`

其实一直在想 PyTorch 的主要用户的心理动机...

)


- [poor-mans-deep-learning-camera](https://github.com/burningion/poor-mans-deep-learning-camera)
    - 117 Stars, 21 Fork

Build a thin client deep learning camera with the Raspberry Pi, Flask, and YOLO.

(`是也乎:`

这工程名起的实在 low...
)


- [tache](https://github.com/zhihu/tache)
    - 32 Stars, 1 Fork

A tag based invalidation caching library

(`是也乎:`

![zhihu](https://avatars0.githubusercontent.com/u/409513?s=200&v=4)

开源的基于 tag 的缓存系统

)


- [evolving-simple-organisms](https://github.com/nathanrooy/evolving-simple-organisms)
    - 22 Stars, 5 Fork

Evolving simple organisms using a genetic algorithm and deep learning from scratch with python.

(`是也乎:`

![organism_v1](https://github.com/nathanrooy/evolving-simple-organisms/raw/master/organism_v1.gif)

神经算法+深度学习框架, 已经是各种嗯哼的标准配置了

)


- [firefox-privacy-restorer](https://github.com/shawnanastasio/firefox-privacy-restorer)
    - 15 Stars, 1 Fork

A script to modify your Firefox preferences to disable telemetry, built-in advertisements, and data collection anti-features.

(`是也乎:`

那什么, 这种后台接口这么嗯哼, 好嘛?

)


- [persistent-dict](https://github.com/richardasaurus/persistent-dict)
    - 10 Stars, 0 Fork

A Python dict which stores data in Redis.

(`是也乎:`

叕一个基于 Redis 的嗯哼...

)

- [albert](https://github.com/Olamyy/albert)
    - 2 Stars, 0 Fork

An Open Source Public API for making Machine Learning powered recommendation system.


(`是也乎:`

哈?现在一推荐系统这么简单就可以有了?

Celery+Heroku+Docker ...
)

- [colour-detection](https://github.com/Godley/colour-detection)
    - 2 Stars, 0 Fork

python module for doing colour detection. 






### (￣▽￣)

- [重大改革：Python 语言将被加入高考科目，VB 惨被淘汰！](https://mp.weixin.qq.com/s/kaEUp2q0K3a_huQa9m_LZg) 为了孩子,中国家长们得开始学习 Python 了... 
    + 传说 高考 编程
- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)


## 是也乎

- 171224 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171224 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


