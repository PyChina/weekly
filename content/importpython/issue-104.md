Title: 蠎加载 104
Slug: importpython-104
Date: 2016-12-23 13:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 104](http://importpython.com/newsletter/no/104/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [房价的可负担性 - 用 Apache Spark](http://blog.scottlogic.com/2016/12/19/spark-unaffordable-britain.html)
    + apache spark

Back in September last year, the Guardian published a fantastic visualisation looking at house price affordability in the United Kingdom. The raw data is easily available from data.gov.uk, and they provide monthly, annual and the complete history allowing you to work with a reasonably sized set before running on the complete data set. Recreating the Guardian’s data process within Apache Spark felt like a great way to get an introduction into the platform.

(`是也乎:`

卫报编辑的折腾...这年头什么行业都不易哪
)

- [Sanic 入门: 基于异步/uvloop 的 web 框架仅 Python 3.5+ 支持](https://twilioinc.wpengine.com/2016/12/getting-started-with-sanic-the-asynchronous-uvloop-based-web-framework-for-python-3-5.html)
    + python3, sanic, webserver

uvloop has been making waves in the Python world lately as a blazingly fast drop-in for asyncio’s default event loop. Sanic is a Flask-like, uvloop-based web framework that’s written to go fast. Sanic is made for Python 3.5 . The framework allows you to take advantage of async/await syntax for defining asynchronous functions. With this, you can write async applications in Python similar to how you would write them in Node.js.

(`是也乎:`

目测退化为 py2 兼容的,才是成功的
)

- [命名实体分类](https://blog.booking.com/named-entity-classification.html)
    + machine learning, NLP

This blog post describes three prototype solutions for the task of Named Entity Classification in the context of Booking.com. The aim is to present different approaches to the classification task, analyse their implementation and compare them in a small scale prototype use case. Sample code in Python is also provided in the following sections for each model described.

- [pdb 到 bug](https://twitter.com/getpy/status/810594994616532992)
    + humor

If you have watched / heard the famous dialog from the movie taken, you will be able to understand this funny meme.



- [如何图形化 Python 调试器](https://medium.freecodecamp.com/hacking-together-a-simple-graphical-python-debugger)
    + debugging

Zero-to-Debugging in 15 mins.



- [Complementing Python With Rust](https://medium.com/@caulagi/complementing-python-with-rust-657a8cb3d066)
    + rust-lang

(`是也乎:`

又来... rust 语言发展求突破, py 这么帮不是个办法
)


- [如何用 Python 重采样并插入时宜序列数据](http://machinelearningmastery.com/resample-interpolate-time-series-data-python/)
    + pandas

In this tutorial, you will discover how to use Pandas in Python to both increase and decrease the sampling frequency of time series data.


- [Pythonic 代码复审 (Red Hat Security Blog)](https://access.redhat.com/blogs/766093/posts/2802001)
    + code quality

Most of us programmers go through technical interviews every once in a while. At other times, many of us sit on the opposite side of the table running these interviews. Stakes are high, emotions run strong, intellectual pressure builds up. I have found that an unfortunate code review may turn into something similar to a harsh job interview.

(`是也乎:`

其实庄表伟在 gitchat 中的系列嗯哼非常实用的了.
)
- [Django Weekly Issue 18](http://djangoweekly.com/newsletter/no/18/)
    + djangoweekly
This weeks roundup insightful articles, videos on everything Django.


(`是也乎:`

以后 Django 相关的嗯哼,可以到专用周刊中挖掘了...

顺便先作一下 [The State of the Developer Nation Survey 2017 ](https://s.developereconomics.com/en/?campaign=DE1Q17ImportPython)
有中文版本的

)

- [介绍 Maya: 人性的数据时间 - By Kenneth Reitz](https://www.kennethreitz.org/essays/introducing-maya-datetimes-for-humans)
    + open source project

Datetimes are a headache to deal with in Python, especially when dealing with timezones, especially when dealing with different machines with different locales. Maya exists to do all the hard work for you, so you can focus on what you're trying to do — import or export simple datetime data in known human and machine-readable formats.

(`是也乎:`

处理海量数据时,时间对准越来越头痛了...

[☀ Say Thank You](https://saythanks.io/to/ZoomQuiet)
)

- [和 Python 函式编程相关的精选列表](https://github.com/sfermigier/awesome-functional-python)
    + open source project

(`是也乎:`

![hy](http://docs.hylang.org/en/latest/_images/hy-logo-small.png)

竟然有这种萌物!

)


- [用 TensorFlow 进行交通标志识别](https://medium.com/@waleedka/traffic-sign-recognition-with-tensorflow-629dffc391a6)
    + machine learning, tensorflow

In this part, I’ll talk about image classification and I’ll keep the model as simple as possible. In later parts, I’ll cover convolutional networks, data augmentation, and object detection.


- [Python 3 in one image](https://twitter.com/getpy/status/810452259284713472)
    + infpgraph

(`是也乎:`

![py3in1pic.jpg（JPEG 图像，892x2048 像素） - 缩放 (43%)](http://openmindclub.qiniucdn.com/res/map/py3in1pic.jpg?imageView2/2/w/360)
)

- [谁可解释 David Beazley 的 tweet ?](https://www.reddit.com/r/Python/comments/5jk0ro/can_someone_explain_david_beazleys_tweet/)
    + discussion

I am glad someone on reddit asked this. I can't get some of David's tweets. It's from his book I learned Python. If you are on twitter follow him.

(`是也乎:`

迷之代码的嗯哼...

    def spam():
        X: auto @ property.template<T> X(*T, ...) = object
        class Y(X):
            pass
        return Y()


如果 Py3 越来越象C++ 那基本上是嗯哼的
)



## 好物
~ 包/模块/库/片段...



- [wordvectors](https://github.com/Kyubyong/wordvectors)
    - 98 Stars, 11 Fork

Pre-trained word vectors of 30+ languages. This project has two purposes. First of all, I'd like to share some of my experience in nlp tasks such as segmentation or word vectors. The other, which is more important, is that probably some people are searching for pre-trained word vector models for non-English languages.

(`是也乎:`

世界上好人就是多!当然这也给各种野生 betacat 发育提供了激素...对人类的未来是否嗯哼不好说.
)

- [tgboost](https://github.com/wepe/tgboost)
    - 76 Stars, 18 Fork

Tiny Gradient Boosting Tree. It is a Tiny implement of Gradient Boosting tree, based on the xgboost algorithm, and support most features in xgboost. This project aims to help people get deeper insights into GBM, especially XGBoost. The current implement has little optimization, so the code is easy to follow. But this leads to high memory consumption and slow speed.

(`是也乎:`

梯度促进树??
)

- [squeaky-wheel](https://github.com/mrpappas/squeaky-wheel)
    - 65 Stars, 8 Fork

Automatically run speed tests and tweet @ your ISP if they are garbage.

(`(￣▽￣):`

又一个基于 tweet 来测试互联网速度的
)

- [hml-equation-parser](https://github.com/OpenBapul/hml-equation-parser)
    - 9 Stars, 0 Fork

If you have equation string from hml document, you can convert it to latex string by using eq2latex function.

(`是也乎:`

韩国作品? 将 LaTex 公式自动变成 html 代码
)

- [razer](https://github.com/rossgoodwin/razer)
    - 6 Stars, 3 Fork

Patterns & Scrolling Text for Razer RGB LED Keyboards.

- [sofia](https://github.com/masterzh01/sofia)
    - 5 Stars, 0 Fork

An simple monitor of memory usage in real time 

(`是也乎:`

![memory](https://github.com/masterzh01/sofia/raw/master/memory.png)
)

# 是也乎

- 161223 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161223 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


