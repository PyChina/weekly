Title: 蠎加载 83
Slug: importpython-83
Date: 2016-07-29 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 83](http://importpython.com/newsletter/no/83/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Raymond Hettinger - 并发的思考 (Pycon RU 2016)](https://www.youtube.com/watch?v=Bv25Dwe84g0)
    + video

Walk through two examples of threading and multiprocessing to illustrate rules and best practices for taking advantage of concurrency. Documentation and code from the presentation is here - https://dl.dropboxusercontent.com/u/3967849/pyru/_build/html/index.html

(`是也乎:`

俄国PyCon!

![thistall](https://dl.dropboxusercontent.com/u/3967849/pyru/_build/html/_images/thistall.jpg)

)

- [又一个 Python 来搞掂的故事 ~ 用类定义构建 DSL](http://slott-softwarearchitect.blogspot.com/2016/07/another-python-to-rescue-story-creating.html)
    + core python

We didn’t invent a new DSL, we merely adapted Python’s existing syntax to our needs. A simple class structure and a metaclass definition gave us everything we needed to build the configuration parameter files we needed.



- [用 Python 构建 slackbot 从而帮助自己找到 SF 的公寓](https://www.dataquest.io/blog/apartment-finding-slackbot)
    + bot

Scrapes listings from Craigslist. Filter out listings that don’t match our criteria. Post the listings to Slack, a team chat tool, so we can discuss and rate them. Wrap the whole process into a persistent loop and deploy it to a server (so it would run continuously). Built by Vik Paruchuri - https://twitter.com/vikparuchuri

(`是也乎:`

其实还是对 Craigslist 进行搜索,只是控制界面变成了 Slack;

嗯哼?! 为了上班不被人发现在刷房源?!
)

- [每天 mypy. 第三部分](http://www.machinalis.com/blog/a-day-with-mypy-part-1/)
    + mypy

Earlier this year PEP-484 was accepted, the typing module was added to Python 3.5, and mypy moved into the umbrella of official python projects. Since it was a visible topic at the last Pycon.us, I decided to get some experience with it and see how it feels to use it. I decided I’d take a working, mature, open-source project that wasn’t written by me and “convert” it to mypy. Note this is a 3 part series with a follow up. Have a look at the latest post here - http://www.machinalis.com/blog/writing-type-stubs-for-numpy/

(`是也乎:`

细思恐极, PEP-484 已被接受?!
意思是 py3 为了性能,已经放弃动态语言这一特性了!?
)

- [登记开始:  Django Under the Hood 2016 !](https://www.djangounderthehood.com/)
    + conference

Based on the videos I have watched this is a must Go ( if you can that's ) Django Conference.

- [A. Jesse Jiryu Davis 对话 "撰写一个优秀的编程 Blog"](https://emptysqua.re/blog/talk-python-episode-on-writing/)
    + podcast

Michael Kennedy ( guy behind the TalkPython Podcast ) and I talked about writing about programming. What kind of writing is most valuable, how do you choose a topic, improve your writing, find an audience, and find the time to write? Listen to the podcast on the Talk Python To Me site.



- [Django 页面加速速度](https://worthwhile.com/blog/2016/07/11/django-page-load-speed/)
    + django

Django and Python tips and tricks on how to improve website page load times by optimizing images.

- [words2map: 用 word2vec, t-SNE 以及 HDBSCAN 构建的推荐框架来加强 overlap.ai](http://blog.yhat.com/posts/words2map.html)

At overlap.ai we’re building artificial intelligence to unite people through their overlapping passions, and here we introduce a framework we call words2map for considering what our users love, like these personal passions of ours. Github repo - https://github.com/overlap-ai/words2map

(`是也乎:`

又一个推荐服务的框架
)

- [用 Python 进行 Pizza 计数](http://goo.gl/m3HS3g)
    + security

I'm a full time nerd, even when I'm ordering pizza online I can't stop myself from investigating how the websites I'm ordering from work. My latest investigation was Dominoes where I found a neat way to count the number of orders that they process throughout the day. This post is supposed to highlight potential dangers when exposing integer ID's, and how they can allow someone motivated (or sad) enough to track data you might not want to share. Simple Python Code to find it out has been shared.


(`是也乎:`

对电商的又一个私人研究实践...
)

- [用 Django 和 D3 构建仪表盘 — dreisbach.us](http://www.dreisbach.us/blog/building-dashboards-with-django-and-d3/)
    + django, Django Rest Framework, d3

My workplace recently collaborated with several police departments to build a dashboard showing 911 (also known as Call for Service) data, allowing users to drill down into that data. When I started on the project, there was a prototype written in dc.js, a JavaScript framework for building dynamic dashboards with all the data on the frontend, built around records from Tampa, FL. I needed to take this and make it capable of handling much more data -- millions of records. I took on the task of building this using Django and D3. Along the way, I found a set of tools that worked for me.



- [当周 PyDev 之星 : Nicholas Tollervey](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/6r5nR2o7lIg/)
    + interview

This week we welcome Nicholas Tollervey (@ntoll) as our PyDev of the Week. He is the author of the Python in Education booklet and the co-author of Learning jQuery Deferreds: Taming Callback Hell with Deferreds and Promises. He was one of the co-founders of the London Python Code Dojo. You should check out his website to see what he’s up to. Let’s spend some time learning more about our fellow Pythonista!

(`是也乎:`

伦敦 Python Code Dojo, 代码道场!
)

- [基本 Django 的 uWSGI 配置](http://www.djangocurrent.com/2016/07/uwsgi-basic-django-setup_74.html)
    + django

Here are two basic examples of almost the same uWSGI configuration to run a Django project; one is configured via an ini configuration file and the other is configured via a command line argument. This does not represent a production-ready example, but can be used as a starting point for the configuration. 



## 活动
~ Upcoming Conference / User Group Meet

- [PyCon APAC 2016](https://www.pycon.kr/2016apac/)
- [PyCon MY 2016](http://pycon.my/)
- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon ZA 2016](https://za.pycon.org/)
- [PyCon JP 2016](https://pycon.jp/2016/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [OSCON Europe 2016](http://conferences.oreilly.com/oscon/open-source-eu-2016)




## 项目
~ 包/模块/库/片段...



- [devguide](https://github.com/python/devguide)
    - 51 Stars, 2 Fork

开发 Python 指南,
针对 CPython 的核心进入,
是以 `the devguide` 为标志的知名 核心开发人员 制作的.

- [asyncio-doc](https://github.com/asyncio-doc/asyncio-doc)
    - 9 Stars, 2 Fork

Asyncio 官方文档. 
教授 py3.5 的 async 和 await, 
来替代以往的 @asyncio.coroutine 以及 yield .

- [LastSecondSlides](https://github.com/trishume/LastSecondSlides)
    - 6 Stars, 0 Fork

使用谷歌语音到文本API
生成演示幻灯片为你代言！

(`是也乎:`

外文不好的同学的福音了,
意味着可以用中文幻灯到全球任何一个国家用当地语言自动演讲了?!
)

- [sorta](https://github.com/loics2/sorta)
    - 5 Stars, 2 Fork

帮助你对文件进行排序


## DAMA
~ 无责任推荐

# 是也乎

- 160731 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160731 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


