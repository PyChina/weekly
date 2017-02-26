Title: 蠎加载 113
Slug: importpython-113
Date: 2017-02-26 23:32
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 113](http://importpython.com/newsletter/no/113/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Guido van Rossum 访谈](https://player.backtracks.fm/talkpython/m/100-guido-van-rossum)
    + podcast, BDFL

Talkpython interview with Guido van Rossum aka BDFL.

(`是也乎:`

有字幕的, 基本上就是回忆了 ABC 时代的嗯哼...
)


- [几个 Python 3 决择 / 进化 的关键视图](http://charlesleifer.com/blog/what-happened/)
    + core-python

The people who introduced me to Python chose it because of the elegance of the language, and it's aesthetic qualities. Would they choose it again, I wonder? Would I?.

(`是也乎:`

是什么以及为什么的 Py3

    def hello_world(name):
        print 'Hello', name

-->


    @coroutine
    async def hello_world(name: str) -> str:
        await print('Hello {}'.format(yield from name))

一定是太多 C++ 程序媛进入了 python 内核开发团队!
)


- [在 Python 中设计模块 - ebook](https://hashedin.com/training/designing-modules-in-python-ebook/)
    + book

This book is for people with some experience in an object oriented programming language. This book will help you get better at module/class level design. Hopefully, it will teach you to identify good design from bad.


- [为工程师和科学家的 Python 视频](http://apm.byu.edu/)
    + video

Python material in data science, analysis, and modeling, and optimization. Here is the youtube video channel of the site https://www.youtube.com/user/APMonitorCom

(`是也乎:`

各种实战领域在职工程师/科学家们的 Pythonic 折腾
)

- [使用 Uber 的 Pyflame 和日志解决问题](https://benbernardblog.com/using-ubers-pyflame-and-logs-to-tackle-scaling-issues/)
    + debugging

This time, it was different though. My distributed web crawler seemed to be slowing down over time. Adding more nodes only had a temporary performance boost; the overall crawling speed gradually declined afterwards. So simply put, it couldn't scale. But why?. In this post, you'll find out what techniques and tools I used to diagnose scaling issues - and to an extent, more general performance issues - in my Python-based web crawler.

(`是也乎:`


![flame_graph_full](https://benbernardblog.com/content/images/2017/02/flame_graph_full.png)

火焰图.... OpenResty 内置了专用工具, 现在咱大蠎也有了...

)

- [Python Packaging 简要指南](https://medium.com/@jiefeng/lets-talk-about-python-packaging-6d84b81f1bb5)
    + packaging

Code reuse is a very common need. It saves you time for writing the same code multiple times, enables leveraging other smart people’s work to make new things happen. Even just for one project, it helps organize code in a modular way so you can maintain each part separately. When it comes to python, it means format your project so it can be easily packaged. This is a simple instruction on how to go from nothing to a package that you can proudly put it in your portfolio to be used by other people.

(`是也乎:`

一切最终归向 pypi ,这样有问题哪...
)

- [闭包约束](https://medium.com/@dawran6/closures-bind-late-7b01e3abcb7b)
    + closures

- [Emacs 作为 Python IDE](https://robots.thoughtbot.com/emacs-as-a-python-ide)
    + emacs

Note - The video is old, but worth watching for emacs users.


- [一种用于肺癌检测的python解决方案](https://goo.gl/mGBHFC)
    + deep learning

- [使用 Python 查找损坏的图像](https://opensource.com/article/17/2/python-tricks-artists)
    + image processing

- [5种 Python 库轻松进入机​​器学习](http://www.infoworld.com/article/3171654/artificial-intelligence/5-python-libraries-to-lighten-your-machine-learning-load.html#tk.rss_all)
    + machine learning

PyWren, Tfdeploy, Luigi, Kubelib, PyTorch. Note - We used luigi at my previous workplace and it's a solid library to custom pipelines for batch processing. In our case it was used to enforce database migrations.


- [类型跟踪对Python很有用](http://renesd.blogspot.in/2017/02/is-type-tracing-for-python-useful-some.html)
    + debugging

Type Tracing - as a program runs you trace it and record the types of variables coming in and out of functions, and being assigned to variables.

(`是也乎:`

嗯哼?! 真正靠谱的还是人
)


- [使用 Python 对扫描文档进行数据挖掘](https://datascience.blog.wzb.eu/2017/02/16/data-mining-ocr-pdfs-using-pdftabextract-to-liberate-tabular-data-from-scanned-documents/)
    + data mining

I've written a Python package called pdftabextract 
https://github.com/WZBSocialScienceCenter/pdftabextract 
that contains several helpful functions for that task and I'm explaining how to use them in that blog post.






## 好物
~ 包/模块/库/片段...


- [tkui](https://github.com/asrp/tkui)
    - 166 Stars, 11 Fork

A visual introspective GUI maker with live editing of the GUI and its editor at the same time

(`是也乎:`

值得关注
)

- [tweetfeels](https://github.com/uclatommy/tweetfeels)
    - 18 Stars, 1 Fork

Real-time sentiment analysis in Python using twitter's streaming api

(`是也乎:`

实时情绪分析, weibo 已经上线相同的了.
)

- [WallpapersFromReddit](https://github.com/tsarjak/WallpapersFromReddit)
    - 13 Stars, 3 Fork

Download all the hot images from reddit.com/r/wallpaper subreddit every 24 hours to a local device and set an image from those local files as a wallpaper, which updates automatically every 30 minutes!

(`是也乎:`

从 reddit 壁纸专栏自动下载生成自己的

)


- [lda2vec-tf](https://github.com/meereeum/lda2vec-tf)
    - 12 Stars, 1 Fork

Tensorflow port of the lda2vec model for unsupervised learning of document + topic + word embeddings.

- [ieighteen](https://github.com/emadehsan/ieighteen)
    - 10 Stars, 1 Fork

Speed up your Localization/Internationalization efforts by automating translation with single script

(`是也乎:`

自动翻译哪...项目名好象 Clojure 的嗯哼...
)

- [fish-hook](https://github.com/dcalsky/fish-hook)
    - 8 Stars, 1 Fork

A console tool which manages your github webhooks efficiently.

(`是也乎:`

又一个 CLI 工具, 来管理 github webhooks 的...
)

- [ipyaml](https://github.com/prabhuramachandran/ipyaml)
    - 8 Stars, 1 Fork

IPython notebooks with YAML file format

(`是也乎:`

这个... just for fun
)

- [Scrapstagram](https://github.com/xTEddie/Scrapstagram)
    - 3 Stars, 0 Fork

An Instagram Scrapper

- [kimo](https://github.com/putdotio/kimo)
    - 3 Stars, 0 Fork

Find OS processes of MySQL queries 




### (￣▽￣)
~ 

# 是也乎

- 170226 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170226 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


