Title: 蠎加载 108
Slug: importpython-108
Date: 2017-01-24 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 108](http://importpython.com/newsletter/no/108/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [用 Apache Spark 对8千万 Amazon 产品进行嗯哼](http://minimaxir.com/2017/01/amazon-spark/)
    + apache spark

I wrote a simple Python script to combine the per-category ratings-only data from the Amazon product reviews dataset curated by Julian McAuley, Rahul Pandey, and Jure Leskovec for their 2015 paper Inferring Networks of Substitutable and Complementary Products. The result is a 4.53 GB CSV that would definitely not open in Microsoft Excel. The truncated and combined dataset includes the user_id of the user leaving the review, the item_id indicating the Amazon product receiving the review, the rating the user gave the product from 1 to 5, and the timestamp indicating the time when the review was written (truncated to the Day). We can also infer the category of the reviewed product from the name of the data subset.

(`是也乎:`

![item_histogram](http://minimaxir.com/img/amazon-spark/item_histogram.png)

是的,现在公开的数据早已超过了 Excel 的能力!

)

- [语法~变量注释](http://www.blog.pythonlibrary.org/2017/01/12/new-in-python-syntax-for-variable-annotations/)
    + variable annotation

Python 3.6 added another interesting new feature that is known as Syntax for variable annotations.

(`是也乎:`

为了性能, Py3 向 C++ 飞奔而去
)

- [每个 Python 项目应该有什么?](https://vladcalin.github.io/what-every-python-project-should-have.html)
    + code quality

Over the past few years, the Python programming language gained a huge popularity boost and its community grew faster than ever. With this growth, a lot of tools appeared that help the community keep things organized and accessible. In this article I am going to provide a short list of iteOver the past few years, the Python programming language gained a huge popularity boost and its community grew faster than ever. With this growth, a lot of tools appeared that help the community keep things organized and accessible. In this article I am going to provide a short list of items every Python project should have in order to be accessible and maintainable.ms every Python project should have in order to be accessible and maintainable.

(`是也乎:`

这是又一份看起来简单,但是,坚持作到不容易的 check-list

requirements.txt/setup.py/Tests/Documentation/Conclusion

以及一个不言则明的目录结构!



)


- [跟踪一个奇怪的Python内存泄漏 - 来自 Benoit Bernard](https://benbernardblog.com/tracking-down-a-freaky-python-memory-leak-part-2/)
    + debugging

Benoit's first article we shared couple of issues back talked about the memory leak in his crawler and how he found the culprit. In this second and final post of the series, you'll find out how Benoit used a combination of techniques and tools to analyze and resolve memory leaks in his Python application.

(`是也乎:`

这是个系列内存传说记述,
)


- [购物蓝分析 – 用 Python 分析可能组合](https://dzenanhamzic.com/2017/01/19/market-basket-analysis-mining-frequent-pairs-in-python/)
    + machine learning

Have you ever asked yourself how the store managers decide on product shelf placement in retail stores? There must be some strategy behind it, right? It can’t be just a random choice. Almost on daily basis, you receive product purchase recommendations from variety of sources where you have left your “digital fingerprint”. In many cases these recommendations make sense, what leaves you puzzled, how did they figured it out?

(`是也乎:`

![market-basket-analysis](https://hamzic.files.wordpress.com/2016/12/market-basket-analysis.jpg)

揭示零售卖场货架布置的背后动机...
)


- [使用 Apache Spark 和 Catalyst 与 Kevin Beyer 构建现代数据发现和 BI 平台](https://www.youtube.com/watch?v=Zp2IJ74xi_s)
    + spark

Apache Spark Meetup talk on: Building a modern data discovery and BI platform using Apache Spark and Catalyst with Kevin Beyer


- [32x 倍提速: numpy, pandas, spark, tensorflow 以共同运行时(Weld)](https://blog.acolyer.org/2017/01/16/weld-a-common-runtime-for-high-performance-data-analytics/)



- [在Python中应用高斯朴素贝叶斯分类器: 第一部分](https://medium.com/@gp_pulipaka/applying-gaussian-na%C3%AFve-bayes-classifier-in-python-part-one-9f82aa8d9ec4)
    + machine learning, naive bayes

- [Python requests 深挖](https://medium.com/@anthonypjshaw/python-requests-deep-dive-a0a5c5c1e093)
    + requests

Lessons learned by replacing httplib in Apache Libcloud with requests.

- [AWS Lambda 初学者指南 - 免费电子书](http://www.oreilly.com/webops-perf/free/serverless-ops.csp)
    + serverless, FAAS

Author Michael Hausenblas explores several use cases where serverless is a great fit—primarily short-running, stateless jobs in event-driven architectures found in mobile or IoT applications. He also provides a guide for migrating from a monolithic application structure to serverless computing. The code snippet in the last chapter is in Python. Though it's a toy application.


- [了解Python的下划线](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc)
    + core-python

While the underscore _ is used for just snake-case variables and functions in most languages (Of course, not for all), but it has special meanings in Python. If you are python programmer, for _ in range(10) , __init__(self) like syntax may be familiar.


- [使用算法的文本分类](https://medium.com/@gk_/text-classification-using-algorithms-e4d50dcba45)
    + naive bayes

Understanding how chatbots work is useful. A fundamental piece of machinery inside a chat-bot is the text classifier. Let’s look at the inner workings of an algorithm approach: Multinomial Naive Bayes. This is a classic algorithm for text classification and natural language processing (NLP). Fancy terms but how it works is relatively simple, common and surprisingly effective.

(`是也乎:`

针对 chatbots 技术
)


- [Python代码库中最常用的单词](https://anvaka.github.io/common-words/#?lang=py)
    + visualization

(`是也乎:`

![pythoneer-most-use-words.png（PNG 图像，799x757 像素） - 缩放 (87%)](http://openmindclub.qiniucdn.com/res/snap/pythoneer-most-use-words.png)

嗯哼...
)

- [对象内省的两个快速函数 - 作者 Vasudev Ram](http://code.activestate.com/recipes/580747-two-quick-functions-for-object-introspection/)
    + core-python

As a curator I can state that Vasudev Ram is definitely one of the most consistent Python blogger in terms of no of articles / code snippets he writes.





## 好物
~ 包/模块/库/片段...


- [pytorch](https://github.com/pytorch/pytorch)
    - 1316 Stars, 81 Fork

PyTorch is a python package that provides two high-level features - Tensor computation (like numpy) with strong GPU acceleration and Deep Neural Networks built on a tape-based autograd system. You can reuse your favorite python packages such as numpy, scipy and Cython to extend PyTorch when needed.

(`是也乎:`

挖掘 GPU 能力的通用模块出来了
)

- [Friday](https://github.com/Zenohm/Friday/)
    - 15 Stars, 3 Fork

开源虚拟助理

(`是也乎:`

一看这名字就知道不聪明...
)

- [rake-nltk](https://github.com/csurfer/rake-nltk)
    - 13 Stars, 1 Fork

Python实现的,
基于 NLTK 快速自动关键字提取算法


- [Frest](https://github.com/h4wldev/Frest)
    - 11 Stars, 2 Fork

又一个 Flask 实现的 RESTful 接口框架

- [Runtype](https://github.com/madisonmay/Runtype)
    - 5 Stars, 0 Fork

Python 的运行时类型检查器

- [django-eventsourcing](https://github.com/ApplauseOSS/django-eventsourcing)
    - 4 Stars, 1 Fork

django-eventsourcing offers common components that are required for building Event Sourcing Django applications. 


### (￣▽￣)

嗯哼,已经放假,带牛妞已刷过魔都 `Disney Land` 对比米国原版的,
最大的差异是服务人员的态度 `눈_눈`

# 是也乎

- 170124 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170124 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


