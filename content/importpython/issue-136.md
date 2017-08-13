Title: 蠎加载 136
Slug: importpython-136
Date: 2017-08-04 12:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 136](http://importpython.com/newsletter/no/136/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [对 Python object 反向工程](https://medium.com/@MTYS_FDR/reverse-engineer-a-python-object-3fd365b6c0d0)
    + python object

I faced an interesting challenge at work the other day. I felt like sharing because it might save a few hours for others, or reveal some insights about the Python internals.



- [Python 正则表达式](https://www.youtube.com/watch?v=VU60rEXaOXk)
    + regular expression

In this video series, we will be tackling Python Regular Expressions. The first few videos we will go over the basics, and then tackle some intermediate problems using Python Regular Expressions.

(`是也乎:`

叕一个正则表达式的嗯哼...可见好东西永远掌握在少数人心中...

)


- [使用进程池加速您的Python数据处理脚本](https://www.linkedin.com/pulse/speed-up-your-python-data-processing-scripts-process-pools-geitgey)
    + process pool

(`是也乎:`

问题在,数据处理首先得是可以切片并发的哪...
)

- [基于 机器学习 用 Python 开发牌照识别系统](https://medium.com/@femidotexe/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)
    + machine learning

In this tutorial, I’ll be taking you through the basics of developing a vehicle license plate recognition system using the concepts of machine learning with Python.

(`是也乎:`

用的是 [scikit\-image](http://scikit-image.org/)
)

- [Python __init__.py & modular Imports](https://medium.com/@ramrajchandradevan/python-init-py-modular-imports-81b746e58aae)
    + core-python, code snippets

(`是也乎:`

又常用又破烦的事儿...
)

- [Logging in Python](https://blog.bordum.dk/logging-tutorial-python.html)
    + logging

logging beyond 101

(`是也乎:`

![standards](https://imgs.xkcd.com/comics/standards.png)

`(￣▽￣)` 这是没个头儿的...

)


- [用 Sightengine 发觉名人](https://medium.com/@antoinegrandiere/recognizing-celebrities-in-an-image-with-sightengine-b1bb84f17f87)
    + machine learning

We will see in this article how to detect if an image contains celebrities with Sightengine.

- [Sam 清洁 Citadel (GoT) 以10小时,用 Python](http://kazuar.github.io/got-remix/)
    + video processing

Curator's Note - I am a big Game of Thrones fan so had to share this. As a fan of Game of Thrones, I couldn’t wait for it to return for a 7th season. Watching the season premier, I greatly enjoyed that iconic scene of Sam doing his chores at the Citadel. I enjoyed it so much that I wanted to see more of it… much more of it. In this post we’ll take the short video compilation of Sam cleaning the Citadel, we will split it to multiple sub clips and create a video of Sam cleaning the Citadel using a random mix of those sub clips.


- [sinuous-violin - Numpy and SciPy](https://mapio.github.io/sinuous-violin/)
    + numpy, scipy

The aim of this short notebook is to show how to use NumPy and SciPy to play with spectral audio signal analysis (and synthesis).

(`是也乎:`

ipynb 可以播放音乐了

)

- [Pandas 分组和 Agg 函数解释](http://pbpython.com/pandas-grouper-agg.html)
    + pandas

Every once in a while it is useful to take a step back and look at pandas’ functions and see if there is a new or better way to do things. I was recently working on a problem and noticed that pandas had a Grouper function that I had never used before. I looked into how it can be used and it turns out it is useful for the type of summary analysis I tend to do on a frequent basis.

- [Yosai 和 Darin Gordon – Episode 120 – Podcast](https://www.podcastinit.com/yosai-with-darin-gordon-episode-120/)
    + podcast

For any program that is used by more than one person you need a way to control identity and permissions. There are myriad solutions to that problem, but most of them are tied to a specific framework. Yosai is a flexible, general purpose framework for managing role-based access to your applications that has been decoupled from the underlying platform. This week the author of Yosai, Darin Gordon, joins us to talk about why he started it, his experience porting it from Java, and where he hopes to take it in the future.

(`是也乎:`

介绍通用 ACL 框架 Yosai
)


- [使用 Cython 来保护 Python 代码库](https://bucharjan.cz/blog/using-cython-to-protect-a-python-codebase.html)
    + cpython

Recently, I worked on a Python project that required the whole codebase to be protected using Cython. Although protecting Python sources from reverse engineering seems like a futile task at first, cythonizing all the code leads to a reasonable amount of security (the binary is very difficult to disassemble, but it's still possible to e.g. monkey patch parts of the program). This security comes with a price though - the primary use case for Cython is writing compiled extensions that can easily interface with Python code. Therefore, the support for non-trivial module/package structures is rather limited and we have to do some extra work to achieve the desired results.

(`是也乎:`

同时还能立即获得速度的提升,
问题在迁移的成本...
)

- [控制 Python 异步蠕变](https://hackernoon.com/controlling-python-async-creep-ec0a0f4b79ba)
    + asyncio

The complication arises when invoking awaitable functions. Doing so requires an async defined code block or coroutine. A non-issue except that if your caller has to be async, then you can’t call it either unless its caller is async. Which then forces its caller into an async block as well, and so on. This is “async creep”.

(`是也乎:`

雪崩在异步场景中的兄弟...
)

- [神密的 Dynamic Programming](https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296)
    + algorithms

Maybe you’ve heard about it in preparing for coding interviews. Maybe you’ve struggled through it in an algorithms course. Maybe you’re trying to learn how to code on your own, and were told somewhere along the way that it’s important to understand dynamic programming. Using dynamic programming (DP) to write algorithms is as essential as it is feared.


- [优化 Pandas 代码速度的初学指南](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)
    + pandas

- [写个 a map-reduce 任务来嗯哼数百万个小文件](https://medium.com/@dfdeshom/writing-a-map-reduce-job-to-concatenate-a-millions-of-small-documents-9c204b2164d)
    + mrjob, mapreduce

- [使用 TensorFlow 检测伪钞](https://medium.com/tensorist/detecting-fake-banknotes-using-tensorflow-be21ffd2c478)
    + tensorflow

Today, let’s use TensorFlow to build an artificial neural network that detects fake banknotes.


- [Hacking 相似搜索,用 python](https://medium.com/@blablablabla/hacking-similarity-search-with-python-c5f740cabd9)
    + project

What would you do if you wanted to know which files are the most similar to a particular text-based file? For example to find a particular configuration file which has changed its filename and its contents.



## 好物
~ 包/模块/库/片段...


- [pytorch-nice](https://github.com/alexsax/pytorch-nice)
    - 53 Stars, 1 Fork

Support powerful visual logging in PyTorch.

(`是也乎:`

![202a6c6d3239](https://user-images.githubusercontent.com/5157485/28799619-2bebef8c-75fe-11e7-898d-202a6c6d3239.png)

果断通过 http 网页来嗯哼是王道...

)


- [CryptoTracker](https://github.com/EthVentures/CryptoTracker)
    - 52 Stars, 2 Fork

A complete open source system for tracking and visualizing cryptocurrency price movements on leading exchanges.

(`是也乎:`

专门交易类型的追踪
)

- [Imports-in-Python](https://github.com/00111000/Imports-in-Python)
    - 41 Stars, 4 Fork

A guide on how importing works in Python.

(`是也乎:`

![00111000](https://avatars1.githubusercontent.com/u/13596285?v=4&s=460)

作者的 ID 实在 geek

)

- [solving-minesweeper-by-tensorflow](https://github.com/staytime/solving-minesweeper-by-tensorflow)
    - 22 Stars, 8 Fork

Tensorflow solve minesweeper.

- [Baidu-Dogs](https://github.com/holyhao/Baidu-Dogs)
    - 19 Stars, 0 Fork

Baidu competition for classifying dogs.

(`是也乎:`

PKUsz 的兄弟...
)

- [EffectiveTensorflow](https://github.com/vahidk/EffectiveTensorflow)
    - 4 Stars, 1 Fork

Guides and best practices for effective use of Tensorflow.

(`是也乎:`

嗯哼? TF 已经用到这份儿上了?!
)

- [minimal_flight_search](https://github.com/martinweigert/minimal_flight_search)
    - 3 Stars, 0 Fork

A minimalist flight search engine written in Python.

(`是也乎:`

基于 google 服务的, 所以...
)

- [django_rest_example](https://github.com/devslaw/django_rest_example)
    - 3 Stars, 0 Fork

Django/DRF rest application example.

- [ytsearch](https://gitlab.com/sj1k/ytsearch)
    - 0 Stars, 0 Fork

A program to search and view YouTube videos. 

(`是也乎:`

![search_results_playing](https://gitlab.com/sj1k/ytsearch/raw/master/screenshots/search_results_playing.png)

嗯哼, 简单的说, 程序猿不将工具作到 CLI 中是无法舒服起来的...
可是, 为毛?!

)


### (￣▽￣)

- PyConChina2017 议题征集开始
    + 申报表单: https://jinshuju.net/f/2ag6QB

中国的PyCon大会已经组织了6年，在第7年PyCon大会之际，Python3已经成熟，比如Instagram迁移到了Python3。而人工智能方兴未艾，区块链、物联网、AR、VR、机器人等领域创新不断涌现。

本大会以“大数据和人工智能技术的创新应用”为主题，将由丰富的内容和议题组成，着重探讨如何使用Python技术进行大数据和人工智能的技术开发和最佳实践，并结合具体的产品和行业发展趋势，分享不同类型的应用、场景下的开发和运营经验。

建议主题范围除了大数据和人工智能外，还可以包括近年来热门的区块链、金融科技及其他创新领域（直播，AR/VR，机器人，视频动画处理等）的话题。

特征集议题，欢迎申请专题演讲（40分钟）和快速演讲（10分钟）。

今年PyConChina2017将在两个城市举办，上海是9月23日举办

- 上海（约400人参加），预计7个主题演讲（每个40分钟），7个快速演讲（每个10分钟）。
- 杭州（约200人参加），预计7个主题演讲（每个40分钟）


## 是也乎

- 170804 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170804 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


