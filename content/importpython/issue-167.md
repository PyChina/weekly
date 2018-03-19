Title: 蠎加载 167
Slug: importpython-167
Date: 2018-03-19 20:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 167](http://importpython.com/newsletter/no/167/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [通过 Python 检测共振频率来破坏酒杯](https://www.makeartwithpython.com/blog/break-glass-with-resonant-frequency/)
    + project, sound engineering

In today’s post, I walk through the journey of writing a Python program to break wine glasses on demand, by detecting their resonant frequency. Along the way we’ll 3D print a cone, learn about resonant frequencies, and see why I needed an amplifier and compression driver. So, let’s get started.


(`是也乎:`

![Breaking](https://www.makeartwithpython.com/blog/assets/images/break-glass/header.jpg)

论优雅的震碎酒杯的姿势...

)


- [用 Python 实现区块链的实用介绍](http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/)
    + blockchain

Blockchain is arguably one of the most significant and disruptive technologies that came into existence since the inception of the Internet. It's the core technology behind Bitcoin and other crypto-currencies that drew a lot of attention in the last few years. As its core, a blockchain is a distributed database that allows direct transactions between two parties without the need of a central authority. This simple yet powerful concept has great implications for various institutions such as banks, governments and marketplaces, just to name a few. Any business or organization that relies on a centralized database as a core competitive advantage can potentially be disrupted by blockchain technology.

- [Python 2.7 终结在 2020年1月1日?](https://mail.python.org/pipermail/python-dev/2018-March/152348.html)
    + 2.7

Curator's note - Lot of banks and financial companies are not going to upgrade and be happy to pay vendors for security updates.

- [如何使用 Scikit-Learn 从文本语料库中列出最常用的单词?](https://medium.com/@cristhianboujon/how-to-list-the-most-common-words-from-text-corpus-using-scikit-learn-dad4d0cab41d)
    + machine learning, scikit

Frequently we want to know which words are the most common from a text corpus sinse we are looking for some patterns.



- [如何在 Python 中用 Deep Learning 实现 iPhone X 的 FaceID](https://towardsdatascience.com/how-i-implemented-iphone-xs-faceid-using-deep-learning-in-python-d5dbaa128e1d)
    + FaceID

Reverse engineering iPhone X’s new unlocking mechanism.

- [Python 中并行 IO 操作的内存效率](https://code.kiwi.com/memory-efficiency-of-parallel-io-operations-in-python-6e7d6c51905d)
    + parallel processing

Python allows for several different approaches to parallel processing. The main issue with parallelism is knowing its limitations. We either want to parallelise IO operations or CPU-bound tasks like image processing. The first use case is something we focused on in the recent Python Weekend* and this article provides a summary of what we came up with.

- [Python 3.7 的内置断点 — 快速介绍](https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c)
    + core-python

Debugging in Python has always felt a bit “awkward” compared with other languages I’ve worked in. Introducing breakpont()


(`是也乎:`

是的, 单步调试是所有 C+++++++ 程序猿思维的依赖...

)

- [Python 编程练习书](http://joaoventura.net/static/files/python_exercises_book.pdf)
    + book

It's free.

(`是也乎:`

21页的小小书...

)


- [PyPI 支持 Markdown 了- Dustin Ingram](https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi)
    + pypi

I’m really excited to say that as of today, PyPI supports rendering project descriptions from Markdown! This has been a oft-requested feature and after lots of work (including the creation of PEP 566) it is now possible, without translating Markdown to rST or any other hacks!




- [python-itertools](https://medium.com/@speakholly95/python-itertools-949a321a0cab)
    + core-python

itertools.accumulate(iterable[, func])

- [Python, SQLAlchemy 和 Factory Boy 进行敏捷数据库集成测试](https://medium.com/@vittorio.camisa/agile-database-integration-tests-with-python-sqlalchemy-and-factory-boy-6824e8fe33a1)
    + testing

So you are interested in testing, aren’t you? Not doing it yet? That’s the right time to start then! In this little example, I’m going to show a possible procedure to easily test your piece of code that interacts with a database.

- [部署 TensorFlow 模型 - 迈向数据科学](https://towardsdatascience.com/deploy-tensorflow-models-9813b5a705d5)
    + tensorflow

Super fast and concise tutorial

- [Stack Overflow 2018 开发者调查- 瞅瞅 Python 怎样.](https://insights.stackoverflow.com/survey/2018/#technology-programming-scripting-and-markup-languages)
    + survey

This year, over 100,000 developers told us how they learn, build their careers, which tools they’re using, and what they want in a job.


(`是也乎:`

一个字: `非常猛`

)


## 好物
~ 包/模块/库/片段...


- [black](https://github.com/ambv/black)
    - 958 Stars, 15 Fork

The uncompromising Python code formatter.




- [makesite](https://github.com/sunainapai/makesite)
    - 216 Stars, 16 Fork

Simple, lightweight, and magic-free static site/blog generator for Python coders

(`是也乎:`

叕一种静态网站生成工具,
但是, 嘦 gh 没内置的, 基本上都是个怂

)


- [thug-memes](https://github.com/jerry-git/thug-memes)
    - 115 Stars, 4 Fork

Command line Thug Meme generator written in Python.

(`是也乎:`

![1_face_debug_dlib](https://raw.githubusercontent.com/jerry-git/thug-memes/master/doc/examples/1_face_debug_dlib.jpg)

为了制造 meme CV 工具是必须有的...


)


- [requests-core](https://github.com/kennethreitz/requests-core)
    - 79 Stars, 3 Fork

Experimental lower-level async HTTP client for Requests 3.0

(`是也乎:`

[@kennethreitz](https://github.com/kennethreitz)
大神出品 必属人品

叕一款注定要流行的嗯哼...

当然:

> This is a work in progress. Don't install it.

)


-[white](https://github.com/kennethreitz/white)
    - 78 Stars, 1 Fork

The Black code formatter, but brighter (PEP8–inspired).


(`是也乎:`

![white](https://camo.githubusercontent.com/f2cd273070089ac5ff0addf35d1ebdbc44f150ce/687474703a2f2f73686172652e6b656e6e657468726569747a2e6f72672f324c326d31553141336d304c2f53637265656e25323053686f74253230323031382d30332d31352532306174253230362e32312e3034253230414d2e706e67)

可以说是 gofmt 的 py 版本了


)


- [socialsentiment](https://github.com/Sentdex/socialsentiment)
    - 40 Stars, 2 Fork

Sentiment Analysis application created with Python and Dash, hosted at socialsentiment.net.

(`是也乎:`

![socialsentiment](https://camo.githubusercontent.com/e22f34fcb852614302c6550b0ad12ceabd0c3e99/68747470733a2f2f707974686f6e70726f6772616d6d696e672e6e65742f7374617469632f696d616765732f646173682f646173686170706c69636174696f6e2e6a7067)

人民群众对合成仪表盘的需求是无尽的...
所以有了 Dash


)


- [rose](https://github.com/kaustubhhiware/rose)
    - 12 Stars, 0 Fork

Analyse all kinds of data for a TV series.

(`是也乎:`

等等...

![imdb_barchart](https://github.com/kaustubhhiware/rose/raw/master/images/imdb_barchart.png)

这种专业分析工具....看起来象 电影学院的毕业设计哪

)


- [onegram](https://github.com/pauloromeira/onegram)
    - 5 Stars, 0 Fork

A simplistic api-like instagram bot powered by requests.


(`是也乎:`

requests 实在是人间圣品, 真正完成了 `for humanbin` 承诺的模块

)


- [convert-outlook-msg-file](https://github.com/JoshData/convert-outlook-msg-file)
    - 5 Stars, 0 Fork

Python library to convert Microsoft Outlook .msg files to .eml/MIME message files.


(`是也乎:`

那什么...好吧, 多年以后, 真心只有 outlook 死撑下来, 变成商务邮件客户端唯一选择了...

)


- [Siamese-LSTM](https://github.com/likejazz/Siamese-LSTM)
    - 4 Stars, 1 Fork

Siamese LSTM for evaluating semantic similarity between sentences of the Quora Question Pairs Dataset.




- [MusicTag](https://github.com/EnricoBilla/MusicTag)
    - 3 Stars, 0 Fork

MusicTag allows you to download from YouTube all the music you want and automatically set the ID3 tags. 

(`是也乎:`

时隔N 年, 又看到 mp3 相关工具, 而来源都变成了 油管...
实在是自云苍狗...

)


### (￣▽￣)

- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...
- [Neilpang/acme.sh: A pure Unix shell script implementing ACME client protocol](https://github.com/Neilpang/acme.sh)
    + https

> 国人作品, 解决 https 部署时的证书生成问题



*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180319 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180319 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


