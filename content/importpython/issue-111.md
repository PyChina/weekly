Title: 蠎加载 111
Slug: importpython-111
Date: 2017-02-11 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 111](http://importpython.com/newsletter/no/111/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Sublime Text 3 和 Python - Kenneth Reitz](https://www.kennethreitz.org/essays/sublime-text-3-heaven)
    + sublime

I decided to revisit my editor configuration the other night, and experimented with every possible editor I could think of / imagine. I heavily configured vim (neovim), PyCharm, Eclipse, Emacs (Spacemacs), VSCode, Atom, Textual, and more. I knew I was going to stay put with my choice of Sublime Text 3 (which I have been using for 5+ years), but it's nice to have validation.

(`是也乎:`

又一个心碎的故事,其实, 编辑器不好用, 只是因为我们成长的太快,
没有什么东西可以一直容纳我们所有的编程个性的...
所以,要不自己开发一个, UliEditor 就是这样来的,
要不个性化配置一个出来, 这就是 Vim/Emacs 成神成圣的原因
)


- [Think Python 第二版 - 免费下载](http://greenteapress.com/wp/think-python-2e/)
    + book

This is the second edition of Think Python, which uses Python 3 is out.


- [如何使用 Python 和 Google Maps API 绘制自己的自行车/慢跑路线](https://blog.alookanalytics.com/2017/02/05/how-to-plot-your-own-bikejogging-route-using-python-and-google-maps-api/)

Apart from being a data scientist, I also spend a lot of time on my bike. It is therefore no surprise that I am a huge fan of all kinds of wearable devices. Lots of the times though, I get quite frustrated with the data processing and data visualization software that major providers of wearable devices offer. That’s why I have been trying to take things to my own hands. Recently I have started to play around with plotting my bike route from Python using Google Maps API. My novice’s guide to all this follows in the post.



- [将 Vim 用成 Python IDE](http://www.liuchengxu.org/posts/use-vim-as-a-python-ide/)
    + vim, editor

I love vim and often use it to write Python code. Here are some useful plugins and tools for building a delightful vim python environment, escpecially for Vim8.


(`是也乎:`


![vim-python-ide-tmux](http://www.liuchengxu.org/assets/images/posts/vim-python-ide-tmux.png)

TMUX 一直是 Vim 党的好朋友

)

- [Python 3.6 和性能](https://speakerdeck.com/playpauseandstop/python-3-dot-6-and-performance-a-love-story)
    + python3.6

Slides from Why Python 3.6 is faster than Python 3.5 talk. Also included a preview of new features of Python 3.6

(`是也乎:`

性能党的注意力果断从 py2 迁移到了 py3 
)


- [我们团队中的 3 种方式提高多系统构建速度.](http://4url.in/XlPEGkLB)
    + Sponsor

How xMatters Uses Toolchains to Move Process Forward


- [Python function 脑移植?](http://blog.lerner.co.il/python-function-brain-transplants/)
    + core-python

Did you know about `__code__` ?

(`是也乎:`

    def foo():
          return "I'm foo!"

    def bar():
          return "I'm bar!"

    foo.__code__ = bar.__code__
    foo()

猜?! 最后输出什么!?

)

- [K-Means和其他聚类算法：基于 Python 的快速入门](http://www.learndatasci.com/k-means-clustering-algorithms-python-intro/)
    + k-means, clustering

- [在 Python 中将 Postgres 数据作为 JSON 返回](http://kracekumar.com/post/156769849745)
    + postgres

row_to_json and json_build_object usage along with code snippet for SQLAlchemy users.

(`是也乎:`

可是,这本身不是 Pg 的一个特性嘛?!
)

- [在 Apache Spark 中用 UDF](http://blog.cloudera.com/blog/2017/02/working-with-udfs-in-apache-spark/)
    + spark, user defined functions

User-defined functions (UDFs) are a key feature of most SQL environments to extend the system’s built-in functionality. UDFs allow developers to enable new functions in higher level languages such as SQL by abstracting their lower level language implementations. Apache Spark is no exception, and offers a wide range of options for integrating UDFs with Spark SQL workflows.

- [在 Python 中进行 Encoding Categorical Values in Python](http://pbpython.com/categorical-encoding.html)
    + datascience

Many machine learning algorithms can support categorical values without further manipulation but there are many more algorithms that do not. Therefore, the analyst is faced with the challenge of figuring out how to turn these text attributes into numerical values for further processing.


- [Python 的简单热门产品推荐引擎](http://blog.untrod.com/2017/02/recommendation-engine-for-trending-products-in-python.md.html)
    + machine learning, recommendation engine


- [Pyweek Game Jam is 19th-26th February](http://mauveweb.co.uk/posts/2017/01/pyweek-23.html)
    + community, game development

The Pyweek rules, in short, are Develop a game, In Python (mostly, at least!), As an individual or with a team, In exactly one week (or less!), From "scratch" - no personal codebases, only public, documented librarie, On a theme that is selected by vote, announced at the moment the contest starts.

(`是也乎:`

用一周时间从0开始构建一个游戏的比赛
)

- [Seaborn 的 Python](http://www.pypython.site/2017/01/seaborn-for-python.html)
    + matplotlib, statistics

Seaborn is a wrapper around Matplotlib that makes creating common statistical plots easy. The list of supported plots includes univariate and bivariate distribution plots, regression plots, and a number of methods for plotting categorical variables. The full list of plots Seaborn provides is in their API reference.

- [用 Amazon ML 对 Tweets 分类](https://dev.to/rohanjamin/classifying-tweets-with-amazon-ml)
    + aws, machine learning

- [Python 新手经](https://twitter.com/getpy/status/829241707610923010)
    + humor

- [十小时 Python 解释器源代码通读](https://www.youtube.com/playlist?list=PLzV58Zm8FuBL6OAv1Yu6AwXZrnsFbbR0S)

Python Video Series on CPython Internals.

- [使用 Python 在 Google 地球中打点](https://medium.com/@nhuphan0404/kmlcreate-points-in-google-earth-with-python-ee4f3d27df55#.ee2jmjrwi)
    + simplekml, kml

First we need to import the library to create point in the Google Earth using simplekml module.

- [用 scikit-learn 的线性回归分析棋盘游戏数据](https://medium.com/@galen.ballew/board-games-meet-machine-learning-34026870f8d5#.h0zruyhzg)
    + scikit-learn

- [Doc2vec 简介](https://medium.com/@mishra.thedeepak/doc2vec-in-a-simple-way-fa80bfe81104#.3ksrfk71i)
    + NLP, doc2vec

Today I am going to demonstrate a simple implementation of nlp and doc2vec. The idea is to train doc2vec model from text document. I had about 20 text files to start with. Although the 20 document corpus seems small but the perk is it takes around 2 minutes to train the model.

(`是也乎:`

比 perk 更加简洁以及高速的 NPL 模块
)




## 好物
~ 包/模块/库/片段...

- [pyheat](https://github.com/csurfer/pyheat)
    - 141 Stars, 8 Fork

pprofile + matplotlib = Python program profiled as an awesome heatmap!

(`是也乎:`

直接将性能损耗对应到代码行上的热力图

![heatmap](https://camo.githubusercontent.com/d8c814336a1f9df72c96b55106cfda96d87f2812/687474703a2f2f692e696d6775722e636f6d2f714f65585550522e706e67)

)

- [block](https://github.com/bamos/block)
    - 109 Stars, 5 Fork

An intelligent block matrix library for numpy, PyTorch, and beyond.

(`是也乎:`

![block](https://github.com/bamos/block/raw/master/images/example.png)

可是,这样要逼死编辑器吧...

)

- [rm-protection](https://github.com/alanzchen/rm-protection)   
    - 101 Stars, 6 Fork

A safe alternative for "rm".

(`是也乎:`

![rm](https://camo.githubusercontent.com/cf1f241a7b8ea8bc90886f0210804afe5678f72f/68747470733a2f2f6f6f6f2e306f302e6f6f6f2f323031372f30322f30332f353839343337363062373665642e676966)

图样图森破, 世界需要 `rm -f . /` 的乐趣

)

- [DeepSpell](https://github.com/surmenok/DeepSpell)
    - 8 Stars, 4 Fork

Spelling Correction with Deep Learning

(`是也乎:`

纠正拼写当然可以用深度学习了...
)

- [green-recorder](https://github.com/green-project/green-recorder)
    - 6 Stars, 4 Fork

A simple yet functional desktop recorder for Linux systems. 

(`是也乎:`

刻度机?

![recorder](https://camo.githubusercontent.com/1b2a0354688469a5b88f7c300b830cc6395cc6f3/687474703a2f2f692e696d6775722e636f6d2f76684a7078496c2e706e67)

嚓! 都快买不到了吧...
)


### (￣▽￣)
~ 

# 是也乎

- 170215 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170215 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


