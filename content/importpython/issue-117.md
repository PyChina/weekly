Title: 蠎加载 117
Slug: importpython-117
Date: 2017-03-17 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 117](http://importpython.com/newsletter/no/117/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [Python 的 Memoization 以及 Decorators](https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84#.mee758aex)
    + core-python

With memoization, we can “memoize” (remember, store) the result of problems that we’ve dealt with before, and return a stored result instead of repeating calculations.

(`是也乎:`

对计算的缓存..
)


- [用 Apache Airflow 开始折腾工作流](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/)
    + airflow

Apache Airflow is an open-source tool for orchestrating complex computational workflows and data processing pipelines. If you find yourself running cron task which execute ever longer scripts, or keeping a calendar of big data processing batch jobs then Airflow can probably help you. This article provides an introductory tutorial for people who want to get started writing pipelines with Airflow.


- [数据科学基本统计: Python 案例集, 第一部分](http://www.learndatasci.com/data-science-statistics-using-python/)
    + statistics

In this post, we'll take a step back to cover essential statistics that every data scientist should know.


- [PyMedium](https://github.com/enginebai/PyMedium)

PyMedium is an unofficial Medium API written in python flask. It provides developers to access to user, post list and detail information from Medium website. This is a read-only API to access public information from Medium, you can customize this API to fit your requirements and deploy on your own server.

(`是也乎:`

又一个非法接口嗯哼出来了
)

- [TensorFlow 可视化: Summary 和 TensorBoard](https://medium.com/@liyin_27935/visualization-in-tensorflow-summary-and-tensorboard-86d5a12660e8)
    + tensorflow

This article is going to discuss some basic methods and functions in tensorflow used to visualize and monitor the training process. I believe visualization is top priority for the research. Because the deep learning itself is a “black box”. So, if the visualization could help us analyze why the final result is successful or failed.


- [用 Python, pandas 和线性回归模型 预测住房价格](http://www.learndatasci.com/predicting-housing-prices-linear-regression-using-python-pandas-statsmodels/)
    + pandas

- [Pandas & Seaborn - 优雅地处理和可视化数据指南](https://tryolabs.com/blog/2017/03/16/pandas-seaborn-a-guide-to-handle-visualize-data-elegantly/)
    + pandas

- [折腾 Machine Learning Algorithms](https://medium.com/@ubajakacj/playing-with-machine-learning-algorithms-806ded11240)
    + machine learning

- [破解虚拟内存](https://blog.holbertonschool.com/hack-the-virtual-memory-python-bytes/)
    + virtual memory

- [用 Apache Kafka 和 Python 构建分布式流系统](https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python)
    + kafka

(`是也乎:`

![Kafka](https://cdn.scotch.io/15775/PRPg1998TfO6VKXTeaTz_illustration.jpg)
)

- [使用 HTML5 和 Flask 拖放文件](http://hundredminutehack.blogspot.in/2017/03/drag-and-drop-files-with-html5-and-flask.html)
    + flask

- [如何使用 IBM Watson 的 语音-文本 功能来转录我们的课程](https://blog.rmotr.com/how-we-use-ibm-watson-speech-to-text-to-transcribe-our-classes-9f59cafdb4b0?source=rss------python-5)
    + watson

In this step by step guide we’ll show you how to transcribe an audio file using IBM Watson speech-to-text API and a little bit of Python.


- [如何生成 文本总结 - 介绍深度学习](https://www.youtube.com/watch?v=ogrJaOIuBx4&lc=z12jidbzikicwvs2d23zyxsp3wmfyvovo)
    + machine learning, video

I'll show you how you can turn an article into a one-sentence summary in Python with the Keras machine learning library. We'll go over word embeddings, encoder-decoder architecture, and the role of attention in learning theory.

- [Python 用 Circle CI 进行持续集成](https://scotch.io/tutorials/continuous-integration-with-python-and-circle-ci)
    + CI

- [如何在 ModelForm 中动态过滤 ModelChoice 的查询集?](https://simpleisbetterthancomplex.com/questions/2017/03/22/how-to-dynamically-filter-modelchoices-queryset-in-a-modelform.html)
    + django

- [Python 3.6.1 已发布](http://blog.python.org/2017/03/python-361-is-now-available.html)
    + core-python

- [几分钟内在 GCP 构建无服务器 Python 应用](https://medium.com/@PicardParis/building-a-serverless-python-app-in-minutes-with-gcp-5184d21a012f)
    + google cloud, cloud functions

Google's answer to aws lambda.

- [Django Admin: 昂贵的 COUNT(*) 查询](http://masnun.rocks/2017/03/20/django-admin-expensive-count-all-queries/)
    + admin

If you have maintained a website with a huge amount of data, you probably already know that Django Admin can become very slow when the database table gets so large. If you log the SQL queries (either using Django logging or using Django Debug Toolbar), you would notice a very expensive SQL query, something like this.






## 好物
~ 包/模块/库/片段...


- [Aeneas – a Python audio/text aligner](https://github.com/readbeyond/aeneas)
    - 793 Stars, 38 Fork

aeneas is a Python/C library and a set of tools to automagically synchronize audio and text (aka forced alignment) http://www.readbeyond.it/aeneas/

(`是也乎:`

![Waveform with aligned labels, detail](https://github.com/readbeyond/aeneas/blob/master/wiki/align.png)

非常实用哪...当然, 对中文嗯哼的..
当然 youtube 还能自动从视频音频中识别文字并自动变成字幕的...
)

- [Snaky](https://github.com/memoiry/Snaky)
    - 28 Stars, 2 Fork

A snake game, three versions of AI included, implemented in python, pygame.

(`是也乎:`

包含了3种 ai 来玩...想起多年前的 `饿狼战役`
)

- [facebook-messenger-bot-tutorial](https://github.com/twtrubiks/facebook-messenger-bot-tutorial)
    - 10 Stars, 0 Fork

facebook-messenger-bot-tutorial use Python Django

- [Ticky](https://github.com/memoiry/Ticky)
    - 9 Stars, 3 Fork

Tic Tac Toe game, implemented in python, pygame. It includes a unbeatable computer AI. Have a try : ) 

(`是也乎:`

又一个 AI 游戏

![Ticky](https://github.com/memoiry/Ticky/raw/master/images/ticky.gif)

5子棋...200行,没有引用任何 AI 框架,就是 pygame 自己...
)

### (￣▽￣)
~ 

# 是也乎

- 170326 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170326 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


