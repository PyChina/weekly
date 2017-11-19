Title: 蠎加载 151
Slug: importpython-151
Date: 2017-11-19 21:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 151](http://importpython.com/newsletter/no/151/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [用 Python 和 OpenCV 搞增强现实（第1部分| Bites of code](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)
    + opencv

You may (or may not) have heard of or seen the augmented reality Invizimals video game or the Topps 3D baseball cards. The main idea is to render in the screen of a tablet, PC or smartphone a 3D model of a specific figure on top of a card according to the position and orientation of the card. 

(`是也乎:`

嗯哼, 这个方向上 Py 也有很多积累
)

- [高级 Python 程序猿最想把什么技巧传授给嫩枪们?](https://www.reddit.com/r/Python/comments/7cs8dq/senior_python_programmers_what_tricks_do_you_want/)
    + core-python

Must read thread.



- [Instagram 在分析 CPython](https://engineering.instagram.com/profiling-cpython-at-instagram-89d4cbeeb898)
    + cpython, production

Instagram employs Python in one of the world’s largest settings, using it to implement the “business logic” needed to serve 800 million monthly active users. We use the reference implementation of Python, known as CPython, as the runtime used to execute our code. As we’ve grown, the number of machines required toserve our users has become a significant contributor to our growing infrastructure needs. These machines are CPU bound, and as a result, we keep a close eye on the efficiency of the code we write and deploy, and have focused on building tools to detect and diagnose performance regressions. This continues to serve us well, but the projected growth of our web tier led us to investigate sources of inefficiency in the runtime itself.

(`是也乎:`

Instagram 用 Python 来服务8亿用户,
但是,依然只是 Python 单体应用最大之一

)


- [如何学习 Pandas - 走向数据科学 ](https://towardsdatascience.com/how-to-learn-pandas-108905ab4955)
    + pandas

In this post, I will outline a strategy to ‘learn pandas’. For those who are unaware, pandas is the most popular library in the scientific Python ecosystem for doing data analysis. Pandas

- [开源采购 ptracer, 面向 Python 的系统跟踪库](https://medium.com/@Pinterest_Engineering/open-sourcing-ptracer-a-syscall-tracing-library-for-python-b0fe0d91105d)
    + Pinterest

Making Pinterest faster and more reliable is a constant focus for our engineering team and using hardware resources more efficiently is a major part of this effort. Improving efficiency and reliability requires good diagnostic tools, and today we’re announcing our newest tracing tool: ptracer, which provides granular syscall tracing in Python programs. In this post we’ll cover background on Pinterest’s codebase, why we needed a better tracer and how ptracer can help solve certain engineering problems.


- [Python wat](https://github.com/cosmologicon/pywat/blob/master/explanation.md)
    + core-python

A "wat" is what I call a snippet of code that demonstrates a counterintuitive edge case of a programming language. (The name comes from this excellent talk by Gary Bernhardt.) If you're not familiar with the language, you might conclude that it's poorly designed when you see a wat. Often, more context about the language design will make the wat seem reasonable, or at least justified.


(`是也乎:`

wat ~ 笏 <-- 反直觉的自然设计

)

- [Blender Python 教程 - 用10行代码实现多米诺骨牌效应](http://slicker.me/blender/domino.htm)
    + code snippets

- [The Mypy Blog: Dropbox 发布 PyAnnotate -- 为 mypy 自动生成类型注释](http://mypy-lang.blogspot.ae/2017/11/dropbox-releases-pyannotate-auto.html)
    + mypy

For statically checking Python code, mypy is great, but it only works after you have added type annotations to your codebase. When you have a large codebase, this can be painful. At Dropbox we’ve annotated over 1.2 million lines of code (about 20% of our total Python codebase), so we know how much work this can be. It’s worth it though: the payoff is fantastic.


- [Django 2.0 rc1 发布](https://www.djangoproject.com/weblog/2017/nov/15/django-20-release-candidate-1-released/)
    + django

Django 2.0 release candidate 1 is the final opportunity for you to try out the assortment of new features before Django 2.0 is released.

- [Tangent - By Google](https://research.googleblog.com/2017/11/tangent-source-to-source-debuggable.html)
    + neural networks

Tangent is a new, free, and open-source Python library for automatic differentiation. In contrast to existing machine learning libraries, Tangent is a source-to-source system, consuming a Python function f and emitting a new Python function that computes the gradient of f. This allows much better user visibility into gradient computations, as well as easy user-level editing and debugging of gradients. Tangent comes with many more features for debugging and designing machine learning models.

(`是也乎:`

和其它机械学习没出息不同,
Tangent 工作成果不是计算结果, 是针对具体问题的新代码, 
然后再运行....

> 哪什么...嗯哼, 你高兴就好.

)

- [用 Python 和 Pandas 分析浏览器历史记录](https://applecrazy.github.io/blog/posts/analyzing-browser-hist-using-python/)
    + pandas, codesnippets

Today, we’re going to do some splunking within the deep, dark place which is your browser history.

- [用 Python 自动生成 Memes 与人脸检测 - 用 Python 艺术处理](https://www.makeartwithpython.com/blog/deal-with-it-generator-face-recognition/)
    + meme

DEAL WITH IT is a meme where glasses fly in from off the screen, and on to a user’s face. The best instances of this meme do so in a unique way. Today we’ll write an automatic meme generator, using any static image with faces as our input. This code makes a great starting point for a meme API, or building your own animated version using video input.

(`是也乎:`

![deal](https://www.makeartwithpython.com/assets/images/deal-with-it/deal.gif)

`弥姆` 嚓,这种交互式行为占了个好名儿

--> [automatic-memes](https://github.com/burningion/automatic-memes)

)


- [Getting Streaming data from Kafka with Spark Streaming using Python.](https://medium.com/@mukeshkumar_46704/getting-streaming-data-from-kafka-with-spark-streaming-using-python-9cd0922fa904)
    + spark, code snippets

In this article, we going to look at Spark Streaming and this is one of several other libraries exposed by Spark Platform.

- [学习 Python 用代码进行创作特别是艺术](https://medium.com/@kevinhowbrook/learning-python-and-being-creative-making-art-with-code-da02880e3738)
    + image processing, art

What do words look like as colours? What would Shakespear’s sonnets look like as colours? This mini project renders text as colours using Python and saves them in a grid as an image.

- [PoetBot: 又一 Telegram 机器人只是能推荐诗歌](https://towardsdatascience.com/poetbot-2-a-telegram-chat-bot-for-poem-recommendation-70d1b809761c)
    + telegram

Building your first poetical chat-bot from scratch

- [Monitoring Cryptocurrency Markets — CryptoCompare Python API Client](https://blog.botreetechnologies.com/monitoring-cryptocurrency-markets-cryptocompare-python-api-client-fc035656c3ef)
    + cryptocurrency





## 好物
~ 包/模块/库/片段...



- [pyannotate](https://github.com/dropbox/pyannotate)
    - 383 Stars, 8 Fork

Auto-generate PEP-484 annotations

(`是也乎:`

好吧, 要是每个 PEP 都有对应的工具出现, 那可就屌了...
)

- [tosheets](https://github.com/kren1/tosheets)
    - 156 Stars, 1 Fork

Send your stdin to google sheets.

(`是也乎:`

简单的说墙外就是幸福, 有无数资源可以串联...
)

- [YOLO_Object_Detection](https://github.com/llSourcell/YOLO_Object_Detection)
    - 117 Stars, 38 Fork

This is the code for "YOLO Object Detection" by Siraj Raval on Youtube

(`是也乎:`

![preview](https://github.com/llSourcell/YOLO_Object_Detection/raw/master/preview.png)

汪...对黑影都能嗯哼出来

)

- [django-subadmin](https://github.com/inueni/django-subadmin)
    - 59 Stars, 2 Fork

A special kind of ModelAdmin that allows it to be nested within another ModelAdmin.

- [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite)
    - 36 Stars, 0 Fork

Convert CSV files into a SQLite database.


- [automatic-memes](https://github.com/burningion/automatic-memes)
    - 13 Stars, 3 Fork

Automatic Memes in Python with Face Detection.

(`是也乎:`

![meme_generator_architecture](https://github.com/burningion/automatic-memes/blob/master/images/meme_generator_architecture.png?raw=true)

)

- [smop](https://github.com/victorlei/smop)
    - 0 Stars, 0 Fork

Small Matlab to Python compiler (Please open an issue if you are using this program)

(`是也乎:`

太初级以至无人关注?
)

- [collab-ide](https://github.com/lambsteak/collab-ide)
    - 0 Stars, 0 Fork

An online real-time collaborative IDE for teams to work together efficiently in a fast-paced project. 

(`是也乎:`

在线, 哈哈哈哈哈哈哈...
)


### (￣▽￣)

- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

关键响应非常敏捷, 10.1 长徦期间嗯哼了一下, 立即追加了两个功能:
[pyheatmap/test.py at 31d80c89529e194e743e3125d56a189712186c55 · oldj/pyheatmap](https://github.com/oldj/pyheatmap/blob/31d80c89529e194e743e3125d56a189712186c55/examples/test.py#L49)

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)

- [Calysto/calysto_scheme: A Scheme kernel for Jupyter that can use Python libraries](https://github.com/Calysto/calysto_scheme)
    + scheme.ipynb

屌炸天的 Jupyter 能力扩展思路...


## 是也乎

- 171119 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171119 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


