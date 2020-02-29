Title: Issue 409
Slug: issue-409
Date: 2020-02-26 11:42
Tags: Weekly,Python,pycoders,ZH

> PyCon2020US 按时开始注册,没受疫情影响



原文: [PyCoder's Weekly - Issue #409](https://pycoders.com/issues/409)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------


- [分析NBA助攻: 如何使用Python可视化数据中的隐藏关系](https://pycoders.com/link/3631/web)
    + JP HWANG

Using basketball as the background setting, the author discusses several different strategies for uncovering relationships and producing beautiful visualizations with Python.

(`是也乎:`

其实, 前提是有老司机能先识别出关系,
才能找到数据模型来提取.

)


- [PyCon美国2020年 Packaging 峰会：注册和主题提案](https://pycoders.com/link/3637/web)
    + PYTHON.ORG

Registration is open for the PyCon US 2020 Packaging Summit. Topic proposals are also being accepted. Both registration and topic proposals close on March 7, 2020.

(`是也乎:`

来了, 来了, 没受疫情影响

)


- [Django 安全漏洞: CVE-2020-7471](https://pycoders.com/link/3655/web)
    + MITRE.ORG

Django 1.11 before 1.11.28, 2.2 before 2.2.10, and 3.0 before 3.0.3 allows SQL Injection if untrusted data is used as a StringAgg delimiter (e.g., in Django applications that offer downloads of data as a series of rows with a user-specified column delimiter).

- [用 Python 处理 PDF](https://pycoders.com/link/3624/web)
    + REAL PYTHON 
    + video

In this step-by-step course, you’ll learn how to work with a PDF in Python. You’ll see how to extract metadata from preexisting PDF files. You’ll also learn how to merge, split, watermark, and rotate pages in PDFs using Python and the PyPDF2 library.


(`是也乎:`

![PDFs](http://ydlj.zoomquiet.top/ipic/2020-02-26-ScreenShot%202020-02-26%2010.11.05.jpg)

在中国虽然 PDF 不怎么受待见, 但是, 人家的确是世界第一通用文档格式哪

)


- [生产中的 Python](https://pycoders.com/link/3636/web) 
    + HYNEK SCHLAWACK


Hynek Schlawack feels that discussions of Python web applications in production are missing from Python conferences. He is offering to mentor people who are interested in proposing conference talks on the subject

- [Python 中的 Null : 了解 NoneType 对象](https://pycoders.com/link/3622/web)
    + REAL PYTHON

Learn about the NoneType object None, which acts as the “null” in Python. This object represents emptiness, and you can use it to mark default parameters and even show when you have no result.


(`是也乎:`

![Null](http://ydlj.zoomquiet.top/ipic/2020-02-26-ScreenShot%202020-02-26%2010.04.16.jpg)

Python 中, 万物皆对象, 没有对象本身也是一种对象

)


- [PEP 584 PR 已合并 (Dictionary Union)](https://pycoders.com/link/3621/web)
    + GITHUB.COM/PYTHON

This will add the following dictionary operations: dict1 | dict2 (copy + update) and dict1 |= dict2 (update). See PEP 584 for example use cases.




## 讨论
> Discussions

- [Werner Herzog 的 “Programming in Python” 中的场景;-)](https://pycoders.com/link/3617/web)
    + TWITTER.COM/MVATTUONE

“I see the lie in front of me – import time, and I am appalled – how can a machine offer such a promise, such a lie, the ability to import time as if it were a simple commodity. Once again, the vile snake has bitten me.”



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [Pycel: 将 Excel 电子表格编译为 Python 并制作精美图片 \[2011\]](https://pycoders.com/link/3633/web)
    + DIRK GORISSEN

Author describes how he compiled Excel spreadsheets with formulas into Python code in order to optimize the calculations and visualize results. Very interesting read!

(`是也乎:`

9年前的...

![screenshot_124942.png (PNG Image, 600 × 450 pixels)](https://elazungu.files.wordpress.com/2011/10/screenshot_124942.png?w=300&h=225&zoom=2)

)

- [用 Rich 获得更好的回溯 ](https://pycoders.com/link/3648/web)
    + WILL MCGUGAN

“I’ve never found Python tracebacks to be a great debugging aid beyond telling me what the exception was, and where it occurred. In a recent update to Rich, I’ve tried to refresh the humble traceback to give enough context to diagnose errors before switching back to the editor.”


(`是也乎:`

叕一则, 对 taceback 美化的尝试


![e7f01f10-5679-11ea-8329-f23c91845b44png.lg.3.jpeg (JPEG Image, 1140 × 1127 pixels)](https://media.moyaproject.com/willmcgugan/uploads/thumbnails/techblog/e7f01f10-5679-11ea-8329-f23c91845b44.png/e7f01f10-5679-11ea-8329-f23c91845b44png.lg.3.jpeg)

)


- [Python SQL 库简介](https://pycoders.com/link/3646/web)
    + REAL PYTHON

Learn how to connect to different database management systems by using various Python SQL libraries. You’ll interact with SQLite, MySQL, and PostgreSQL databases and perform common database queries using a Python application.


(`是也乎:`


![CRUD](http://ydlj.zoomquiet.top/ipic/2020-02-26-ScreenShot%202020-02-26%2010.00.17.jpg)

其实,没什么 DB 值得支持了,星际统一在少数产品周围了...


)


- [Blake 的诗歌中象征主义的简要网络分析](https://pycoders.com/link/3628/web)
    + MARTA PALANDRI

The author explains how she used the spaCy and NetworkX libraries to analyze William Blake’s 18th century poetry collection The Songs of Innocence and of Excellence.

- [Python Packaging 元数据](https://pycoders.com/link/3619/web)
    + HYNEK SCHLAWACK

“Since this topic keeps coming up, I’d like to briefly share my thoughts on Python package metadata because it’s – as always – more complex than it seems.”

- [Python 如何成为流行的选择](https://pycoders.com/link/3641/web)
    + JUN WU

“With the popularity of Python with programmers still growing, we tried to understand how it became one of the most impactful languages in the world.”

(`是也乎:`

好问题, 这的确是个神奇的事儿...

一般来说, 所谓流行技术, 都是要大企业大国家以及大学共同支持和推动时,
才能成为社会流行事物的, 而 Python 什么也没有...

![cstory](http://ydlj.zoomquiet.top/ipic/2020-02-26-collection_coder_stories-zip.jpg)

)



- [如何将 robots.txt 添加到您的Django网站](https://pycoders.com/link/3647/web)
    + ADAM JOHNSON

robots.txt is a standard file to communicate to “robot” crawlers, such as Google’s Googlebot, which pages they should not crawl.


(`是也乎:`

实用, 只是, 这年头, 有遵守交通规则的 crawl 嘛?

)


- [用100行 Python 自动执行 Dating 生活](https://pycoders.com/link/3625/web)
    + ELI MERNIT

Author used a Python-based man-in-the-middle proxy to deconstruct network calls made by the Hinge app and then built a service to automatically “swipe right” on dating profiles.





- [用 Python 和 GitHub 管理 Kindle Highlight](https://pycoders.com/link/3627/web)
    + DUARTE O.CARMO

Author writes a Python script to build a GitHub repo for storing Kindle book highlights in an organized way.


(`是也乎:`

嗯哼, 超级实用哪, 这下就可以自动化 Kindle 处理笔记了

)


- [如何在 Pytest 和 Black 的单元测试中作弊](https://pycoders.com/link/3644/web)
    + SIMON WILLISON

Some tips for quickly writing rough initial implementations for test cases and then iterating on them.

(`是也乎:`

叕一则老司机好文

)


- [用 OpenCV 在 Python 中进行图像处理的简介](https://pycoders.com/link/3623/web)
    + MUHAMMAD JUNAID KHALID



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [PayloadsAllTheThings: 实用 渗透测试/CTF有效负载列表](https://pycoders.com/link/3634/web)
    + GITHUB.COM/SWISSKYREPO




- [Carnets: iOS 独立 Jupyter Notebook 实现](https://pycoders.com/link/3635/web)
    + HOLZSCHU.GITHUB.IO

(`是也乎:`

等等, 为什么是 iOS ?
难道 Android 对此无兴趣?

)


- [Pycel: 将 Excel 电子表格编译为 Python 代码并可视化它们](https://pycoders.com/link/3643/web)
    + GITHUB.COM/DGORISSEN

(`是也乎:`

果然, Excel 每一个功能,  都能拆解出一个独立软件或是公司的

)


- [darknet.py: TOR Proxy Written in Python](https://pycoders.com/link/3639/web)
    + GITHUB.COM/MULTIVERSECODER

(`是也乎:`

嗯哼? 这个实用哪, 将 bot 置于 TOR 之后,
不就等于获得无限可用 IP 了?

)


- [dg: A Python With a Haskell Syntax](https://pycoders.com/link/3638/web)
    + PYOS.GITHUB.IO

(`是也乎:`

少见的逆操作哪,
多数都是支持用 Py 语法来自动生成其它语言代码的...

![doge.png (PNG Image, 200 × 200 pixels)](https://pyos.github.io/dg/images/doge.png)

真的 `狗言` 来了


)


- [HiPlot: High-Dimensional Interactive Plots Made Easy](https://pycoders.com/link/3640/web)
    + FACEBOOK.COM

- [Django Security: PyCharm Python Security Plugin](https://pycoders.com/link/3642/web)
    + PYCHARM-SECURITY.READTHEDOCS.IO

(`是也乎:`

看来 Django 选择了 PyCharm 生态, 优先嗯哼?

)

- [DeepSpeed: Deep Learning Optimization Library](https://pycoders.com/link/3653/web)
    + GITHUB.COM/MICROSOFT


(`是也乎:`

叕一个 DL 加速模块,
注意发布者...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ JupyterCon 2020](https://pycoders.com/link/3654/web)
    + August 10–14 in 
    + Berlin, 
    + Germany.

- [⋅ Python Vienna Meetup](https://pycoders.com/link/3618/web)
    + February 29, 2020
    + 维也纳

- [⋅ Python Mauritius User Group Meetup](https://pycoders.com/link/3650/web)
    + February 29, 2020
    + 毛里求斯

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/3629/web)
    + February 29, 2020
    + 印度

- [⋅ Melbourne Python Users Group, Australia](https://pycoders.com/link/3630/web)
    + March 2, 2020
    + 澳洲


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [中国「远程办公」大考](https://edu.csdn.net/huiyiCourse/detail/1159)
    + 抗击疫情，
    + 科技公司在行动
    + 系列

(`是也乎:`

2020.2.29 CSDN 继续线上技术峰会,
大妈, 继续主持吐糟.

)



# PS:
- 首发: [Issue 409 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-409.html)
- 修订: [issue-409.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-409  .md)


-------------
>> NN 3934

好文笔,感叹号年度配额: **1/3**

-------------

ZoomQuiet/**大妈**

就是四处 `是也乎,(￣▽￣)` 的那个大妈:


- 私自嗯哼: ZoomQuiet (订阅号 **ZoomQuiet42**)
- 公开课程: **蟒营** (订阅号: Mainium)
- 全国大会: PyChina (订阅号: PyChinaOrg)
- 本地社区: 
    + GDG珠海 (订阅号: GDG-ZhuHai)
    + TFUG珠海 (订阅号: ZH_TFUG)
- 历史吐糟: Chaos42 (订阅号 PythoniCamp)

-------------





