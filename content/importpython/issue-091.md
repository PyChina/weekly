Title: 蠎加载 91
Slug: importpython-91
Date: 2016-09-22 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 91](http://importpython.com/newsletter/no/91/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [俺出席在 新德里的 Pycon India 2016](http://importpython.com/newsletter/)
    + importpython

Hey guys, this is Ankur. Curator behind ImportPython. Will be attending PyconIndia. Happy to meet you all and discuss all things Python. Get your opinion on the newsletter, How to make it better ?. Ping me on ankur at outlook dot com or just reply to this email. I will respond back. See you there.

(`是也乎:`

Ankur 就是 ImportPython 的作者,原来是 印度人...
)

- [在 Quora 用 Python 和 asynq 进行异步编程](https://engineering.quora.com/Asynchronous-Programming-in-Python)
    + async-io

asynq is a library for asynchronous programming in Python with a focus on batching requests to external services. It also provides seamless interoperability with synchronous code, support for asynchronous context managers, and tools to make writing and testing asynchronous code easier. asynq was developed at Quora and is a core component of Quora's architecture. See the original blog post here.


(`是也乎:`

嗯哼, 又一个没有进入 build-in 的优秀模块

![asynq](https://camo.githubusercontent.com/d8d52ecb8b1db0ed494020ffc9c15925db01c68c/687474703a2f2f692e696d6775722e636f6d2f6a43504e794f612e706e67)

其实,公司想成名, 将公司名嵌入到著名的开源模块中,一直是非常好的渠道.
)

- [Python 包管理生态 - Nick Coghlan](http://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html)
    + packaging

There have been a few recent articles reflecting on the current status of the Python packaging ecosystem from an end user perspective, so it seems worthwhile for me to write-up my perspective as one of the lead architects for that ecosystem on how I characterise the overall problem space of software publication and distribution, where I think we are at the moment, and where I'd like to see us go in the future.

(`是也乎:`

少见的长篇大论, 追根溯源 Python 包管理的的历史和发展;
这已经不是头一家从根儿上重构 py 包发行机制的尝试了.
当然, 事实也证明, 从一开始不完美的事物,往往能在其后发展出创始人也无法想象的花活儿来.
参考 JavaScript ... 嗯哼, 那个连姓名都故意乱起的语言.
)

- [用 pkgsrc 部署现代 Python 应用到古老的基础设施上](http://pythonsweetness.tumblr.com/post/150466265417)
    + infrastructure

This team is responsible for supplying a variety of web apps built on a modern stack (mostly Celery, Django, nginx and Redis), but have almost no control over the infrastructure on which it runs, and boy, is some of that infrastructure old and stinky. We have no root access to these servers, most software configuration requires a ticket with a lead time of 48 hours plus, and the watchful eyes of a crusty old administrator and obtuse change management process. The machines are so old that many are still running on real hardware, and those that are VMs still run some ancient variety of Red Hat Linux, with, if we’re lucky, Python 2.4 installed.

(`是也乎:`

就是上篇文章的另外一个分支, 分享 PayPal 的折腾成果.
)

- [创作公众可读的 Python notebooks](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook)
    + ipython

The notebook functionality of Python provides a really amazing way of analyzing data and writing reports in one place. However in the standard configuration, the pdf export of the Python notebook is somewhat ugly and unpractical. In the following I will present my choices to create almost publication ready reports from within IPython/Jupyter notebook.


(`是也乎:`

讲真, 每次见到这么细心的一点点解决 LeTaX 和现实世界结合的分享,
就看见了20年前的 王珢 孤独的宣传 Emacs+TeX 的身影
)


- [SF Pybay 大会视频](https://www.youtube.com/channel/UC51aOZF5nnderbuar5D5ifw)

Paul Bailey, "A Guide to Bad Programming", at PyBay2016 was my fav talk amongst all. Check out the youtube channel.

(`是也乎:`

哈! 其实烂代码指南比好代码手册,要更加有用的.
)

- [压缩和增强手写笔记](https://mzucker.github.io/2016/09/20/noteshrink.html)
    + image processing

I wrote a program to clean up scans of handwritten notes while simultaneously reducing file size. Some of my classes don’t have an assigned textbook. For these, I like to appoint weekly “student scribes” to share their lecture notes with the rest of the class, so that there’s some kind written resource for students to double-check their understanding of the material. The notes get posted to a course website as PDFs.

(`是也乎:`

![notesA1_comparison](https://mzucker.github.io/images/noteshrink/notesA1_comparison.png)

~ Left: input scan @ 300 DPI, 7.2MB PNG / 790KB JPG. Right: output @ same resolution, 121KB PNG

简单的说,经过复杂的处理,终于可以免去重新用电脑整理课堂笔记的事儿了!
大体积的扫描件经过处理,就能变成又小又清晰的 pdf 来卖了!

)

- [Python 中的图像处理 - 教程](https://www.codementor.io/python/tutorial/image-manipulation-in-python)
    + image processing

This tutorial will show you how to transform an image with different filters and techniques to deliver different outputs. These methods are still in use and part of a process known as Computer-To-Plate (CTP), used to create a direct output from an image file to a photographic film or plate (depending on the process). Note - It's a pretty good article that makes uses of Python 3, Pillow and is well written.

(`是也乎:`

WoW 强烈历史感的科普文, 将出版的图像处理和 python 的结合聊明白了.

![semi-opacity property](https://cdn.filestackcontent.com/mXHi44pSTl6xAZsNHnRi)

)

- [每周聊 Python: 学习 Django 的技巧](http://ccst.io/e/learning-django)
    + video

This is a Weekly Python Chat live video chat events. These events are hosted by Trey Hunner. This week Melanie Crutchfield and he are going to chat about things you'll wish you knew earlier when making your first website with Django. Much watch for newbies building websites in Django.

- [2 步认证在 Django](https://markusholtermann.eu/2016/09/2-factor-authentication-in-django/)
    + security

If you are looking to implement 2 Factor Authentication as part of your product and don't know where to start read this. 


## 活动
    ~ Upcoming Conference / User Group Meet

- [PyCon DE 2016](http://pycon.de/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon Ireland 2016](https://python.ie/pycon-2016/)
- [PyHPC 2016](http://www.dlr.de/sc/pyhpc2016)
- [PyData Cologne 2016](http://pydata.org/cologne2016/)
- 


## 项目
~ 包/模块/库/片段...

- [streamlink](https://github.com/streamlink/streamlink) 
    + 59 Stars, 10 Fork

CLI for extracting streams from various websites to video player of your choosing

(`是也乎:`

永远的命令行工具,从系列服务网站中选择视频批量播放...

嗯哼,系列小电影观看利器
)

- [encore.ai](https://github.com/dyelax/encore.ai)
    - 40 Stars, 6 Fork

Generate new lyrics in the style of any artist using LSTMs and TensorFlow

(`是也乎:`

使用 LSTMs 和 TensorFlow 自动生成指定目标歌手的新歌词...

词作家将失业了...
)

## DAMA
~ 无责任推荐

- [GitHub Octoverse 2016](https://octoverse.github.com/)

Github 年度报吿, 值得关注的是: [rdpeng (Roger D. Peng)](https://github.com/rdpeng)
这位华人,个人仓库有两个在 top10 名单中!
你猜为毛!?

- [karpathy/arxiv-sanity-preserver: Web interface for browsing, search and filtering recent arxiv submissions](https://github.com/karpathy/arxiv-sanity-preserver)

使用 Python 开发的基于 NLP 技术, 自动化提取论文仓库核心内容搜索服务,以便大家快速定位对自己有用的论文!

~ 介绍视频: [introduction video](https://youtu.be/S2GY3gh6qC8)
作者很神奇...


# 是也乎

- 160922 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160922 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


