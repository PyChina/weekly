Title: 蠎加载 142
Slug: importpython-142
Date: 2017-09-16 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 142](http://importpython.com/newsletter/no/142/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 3.7 有什么新的?](https://docs.python.org/3.7/whatsnew/3.7.html)
    + new release

This article explains the new features in Python 3.7, compared to 3.6.

(`是也乎:`

因为老爹没有公司任务了, 所以,开始发力社区版本?
)

- [如何用 Python 生成 FiveThirtyEight 图表?](https://www.dataquest.io/blog/making-538-plots/)
    + graph, FiveThirtyEight

If you read data science articles, you may have already stumbled upon FiveThirtyEight’s content. Naturally, you were impressed by their awesome visualizations. You wanted to make your own awesome visualizations and so asked Quora and Reddit how to do it. You received some answers, but they were rather vague. You still can’t get the graphs done yourself. In this post, we’ll help you. Using Python’s matplotlib and pandas, we’ll see that it’s rather easy to replicate the core parts of any FiveThirtyEight (FTE) visualization.

(`是也乎:`

![FTE](https://avatars3.githubusercontent.com/u/6267336?v=4&s=200)

[FiveThirtyEight](https://fivethirtyeight.com/tag/data-visualization/)

原来是家公司,因为精美的可视化作品, 而变成了专门的 FTE 风格...


)


- [在 Unix 环境中配置 Python (用 pyenv 以及 direnv)](https://mike.place/2017/python-pyenv/)
    + environment, pyenv

This post is about how to set up multiple Python versions and environments on a development machine (and why I don’t use conda).

- [在 Docker 中用 Jupyter Notebook 跑 PySpark – Suci Lin – Medium](https://medium.com/@suci/running-pyspark-on-jupyter-notebook-with-docker-602b18ac4494)
    + docker, spark, jypyter

It is much much easier to run PySpark with docker now, especially using an image from the repository of Jupyter. When you just want to try or learn Python. it is very convenient to use Jupyter Notebook for an interactive developing environment. The same reason makes me want to run Spark through PySpark in Jupyter Notenook.

(`是也乎:`

嚓, 这热点组合的...

)

- [Surgical 时间追踪在 Python](https://blog.sicara.com/profile-surgical-time-tracking-python-db1e0a5c06b6)
    + performance

How to profile your python code to improve performance?

- [用卷积去噪在基于内容的图像检索中使自动编码器](https://blog.sicara.com/keras-tutorial-content-based-image-retrieval-convolutional-denoising-autoencoder-dc91450cc511)
    + machine learning, image processing

Content based image retrieval (CBIR) systems enable to find similar images to a query image among an image dataset. The most famous CBIR system is the search per image feature of Google search. This article is a keras tutorial that demonstrates how to create a CBIR system on MNIST dataset. Our CBIR system will be based on a convolutional denoising autoencoder. It is a class of unsupervised deep learning algorithms.

(`是也乎:`

基于内容的图像搜索...

)

- [itertools.count](https://medium.com/@adamshort/python-gem-itertools-count-afd7765ddb56)
    + code snippets

You need to iterate over an infinite series of numbers, breaking when a condition is met.



- [如何用 Python 监听 S&P 500 股票](https://medium.com/python-data/how-to-scrape-information-of-s-p-500-listed-companies-with-python-8205f895ee7a)
    + scraping, codesnippets

I thought it would be nice to show how one can leverage Python’s Pandas library to get stock ticker symbols from Wikipedia.

- [Equality 和 Identity](https://twitter.com/python_tip/status/908356538435125248)
    + tweet

(`是也乎:`

> Equality vs Identity:

    >>> a = ["x", "y"]
    >>> b = a
    >>> c = ["x", "y"]

    >>> a == b == c
    True
    >>> a is b
    True
    >>> a is c
    False

所以, 这个 推 关注时间长了就怀疑人生了...

不过,  logo 很萌...

)


- [用 Python 对 Trump's tweets 进行情感分析](https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-)
    + machine learning, sentiment analysis

In this article we will. Extract twitter data using tweepy and learn how to handle it using pandas. Do some basic statistics and visualizations with numpy, matplotlib and seaborn. Do sentiment analysis of extracted (Trump's) tweets using textblob.

(`是也乎:`

所以, 蹭热点也是技术界的习惯...
)


- [Django Girls 年度报告 2016-2017](https://djangogirls.org/2016-2017/)
    + django-girls

Django Girls Foundation is an initiative that aims to introduce women and girls who never coded before to the world of technology and increase the diversity of the tech industry. We achieve this by organising one-day workshops and inviting women to come and learn how to build the internet using HTML, CSS, Python and Django. Django Girls is a volunteer run organisation with volunteers all over the world. Django Girls has two part-time paid staff members and the support team (six awesome ladies who are also volunteers) to help provide support to all other volunteers.

(`是也乎:`

![DjGirls](https://a.tiles.mapbox.com/v4/marker/pin-m-heart+FF9400@2x.png?access_token=pk.eyJ1Ijoib2xhc2l0YXJza2EiLCJhIjoiZGUzZjUyNjUxYWNkOGU1ODBkYjcxNzc4MTllNGRlMjcifQ.t0yuSZmW5FvragLmVgJXNQ)

神奇的非洲...
万恶的资本主义, 程序猿已经不够了, 开始夯力发掘程序媛的劳动力了,
不禁想到 WAR II 时发动家庭妇女们走入工厂的宣传片儿...

)

- [使用 Python 的 Logistic回归 (Sklearn, NumPy, MNIST, Handwriting Recognition, Matplotlib)](https://medium.com/@GalarnykMichael/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a)
    + machine learning

Logistic regression can be used to solve problems like classifying images.

(`是也乎:`

叕一个手写文字识别案例...
只是,已经有能在各种表面上即时打印印刷文字的手势打印机了...

)

- [理解 Asyncio](https://medium.com/@philip.graham.jones/understanding-asyncio-a6592a517def)
    + asyncio, code snippets

A recent article by Jason Goldstein expressed the author’s difficulty understanding and using Asyncio, especially in a Flask context. Asyncio in a Flask context is the exact experience I have with Quart, so I hope I can add something to the conversation this author started.

(`是也乎:`

怎么说呢? 需要理解才能正确应用的技术,都是...
)


## 好物
~ 包/模块/库/片段...


- [future-fstrings](https://github.com/asottile/future-fstrings)
    - 80 Stars, 2 Fork

A backport of fstrings to python<3.6

(`是也乎:`

等等 `< 3.6` ???

为了将 fstrings 用在之前的版本中...
这叫什么补丁来的?

    # -*- coding: future_fstrings -*-
    thing = 'world'
    print(f'hello {thing}')


)

- [python-switch](https://github.com/mikeckennedy/python-switch)
    - 57 Stars, 4 Fork

Adds switch blocks to Python.

- [socksmon](https://github.com/mrschyte/socksmon)
    - 31 Stars, 3 Fork

Monitor arbitrary TCP traffic using your HTTP interception proxy of choice.

(`是也乎:`

浏览器是操作系统, 实在是越来越实在的现实了...
)

- [s3tk](https://github.com/ankane/s3tk)
    - 30 Stars, 0 Fork

A security toolkit for Amazon S3.

- [Octomender](https://github.com/frankyjuang/Octomender)
    - 22 Stars, 0 Fork

Get repo recommendation based on your GitHub star history.

(`是也乎:`

gh 的次级生态环境越来越好玩儿了...
)

- [web-traffic-forecasting](https://github.com/sjvasquez/web-traffic-forecasting)
    - 13 Stars, 3 Fork

Kaggle | Web Traffic Forecasting.

- [list_dict_DB](https://github.com/Jwink3101/list_dict_DB)
    - 13 Stars, 0 Fork

In-Memory noSQL-like data structure.

(`是也乎:`

简单的说 bsddb 之后, redis 重爆了内存 DB 的世界...
但是, 依然没有出现 bsddb 的替代品

![benchmark](https://github.com/Jwink3101/list_dict_DB/raw/master/benchmark.png)

不过,总算有关注性能的 内存原生 DB 出现了...

当然 [list_dict_DB -- Turn a list of dictionaries into a fast, O(1), noSQL-like data structure：Python](https://www.reddit.com/r/Python/comments/6zfilv/list_dict_db_turn_a_list_of_dictionaries_into_a/#bottom-comments) 引发了足够深入的讨论,并指向了:

[Using a mutable default value as an argument — Python Anti-Patterns documentation](https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html)

![snake_warning](https://docs.quantifiedcode.com/python-anti-patterns/_images/snake_warning.png)

[反模式.py](https://docs.quantifiedcode.com/python-anti-patterns/index.html)
这部小书 ;-)

)


- [pyprof-timer](https://github.com/RussellLuo/pyprof-timer)
    + 0 Stars, 0 Fork

A timer for profiling a Python function or snippet. 

(`是也乎:`

输出的嗯哼:

    main (2507.00 ms)
    ├── sleep1 (1002.23 ms)
    └── sleep2 (1504.77 ms)

简单的说, 为了 CLI 中图形化的展示, 也是值得嗯哼的...


)


### (￣▽￣)

- PyConChina2017 议题征集开始
    + 申报表单: https://jinshuju.net/f/2ag6QB

中国的PyCon大会已经组织了6年，在第7年PyCon大会之际，Python3已经成熟，比如Instagram迁移到了Python3。而人工智能方兴未艾，区块链、物联网、AR、VR、机器人等领域创新不断涌现。

本大会以“大数据和人工智能技术的创新应用”为主题，将由丰富的内容和议题组成，着重探讨如何使用Python技术进行大数据和人工智能的技术开发和最佳实践，并结合具体的产品和行业发展趋势，分享不同类型的应用、场景下的开发和运营经验。

...

今年PyConChina2017将在两个城市举办，上海定档:

    2017年10月22日 8:30 ～ 17:00 

- [【上海场】PyConChina2017](http://www.huodongxing.com/event/3403439712600?td=8211933664158)
  + **[--> 主题申报](https://jinshuju.net/f/2ag6QB)** 
  + [---> 门票购买](http://www.huodongxing.com/event/3403439712600?td=8211933664158)

(`是也乎:`

结果立即在 CPyUG 列表中引发了各种嗯哼,
并有行者组织了议题问卷, 得到稍有不同的期待,
所以, 大会的举行真心得看坚持了.
)

## 是也乎

- 170908 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170908 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


