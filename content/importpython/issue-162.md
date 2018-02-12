Title: 蠎加载 162
Slug: importpython-162
Date: 2018-02-12 13:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 162](http://importpython.com/newsletter/no/162/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [免费 Python 书: 开始 Python, 高级 Python, 以及 Python 练习](http://www.davekuhlman.org/python_book_01.html)
    + book

This document is a self-learning document for a course in Python programming. This course contains (1) a part for beginners, (2) a discussion of several advanced topics that are of interest to Python programmers, and (3) a Python workbook with lots of exercises.

(`是也乎:`

叕一本 Python 入门书.

)


- [类似Snapchat AR 过滤器](https://www.codemade.io/snapchat-like-augmented-reality-filters/?=yc)
    + augmentedreality

My project lets you try on virtual pairs of sunglasses or masks. To achieve this I utilized python, Dlib, OpenCV, Scipy, and Numpy. The pipeline involves opening a live webcam feed, detecting keypoints on faces in the feed, warping a png image of sunglasses to match the face, rotating the png with face movements, and blending the two images together so they look like one real image.

(`是也乎:`

叕一个 Python 实现的简易 AV 面具嗯哼工具

)


- [Python - Clean Design 的分类](https://ac1235.github.io/fractal-of-clean-design)
    + core-python

Some Python programmers like to think of their language as flawless. I personally know some Python programmers claiming that Python is superior to other languages in its clean design and unmatched elegance. This however isn’t true. Python has at least as many deep and fundamental flaws as most other languages, despite parts of its community claiming something different.



- [将Python项目打包到Debian .deb 第1部分](https://medium.com/@pycoder_boy/packaging-python-project-to-debian-deb-part-1-f01f510d7d10)
    + packaging

Hi, Have you ever try to package your code/project to became .deb or in official Debian or Ubuntu Repository to share to the rest of the world?

(`是也乎:`

发布 Python 工程为 .deb ...
是的, 很少有人发布为 .exe/.msi

)



- [Python 弱性能问题](https://metarabbit.wordpress.com/2018/02/05/pythons-weak-performance-matters/)
    + performance

What changed in my reasoning? First of all, I’m working on other problems. Whereas I used to do a lot of work that was very easy to map to numpy operations (which are fast as they use compiled code), now I write a lot of code which is not straight numerics. And, then, if I have to write it in standard Python, it is slow as molasses. I don’t mean slower in the sense of “wait a couple of seconds”, I mean “wait several hours instead of 2 minutes.”

(`是也乎:`

Python 中的囧问题, 几小时都算不出来的场景..

)


- [信用建模与 Dask](http://matthewrocklin.com/blog/work/2018/02/09/credit-models-with-dask)
    + dask

This post explores a real-world use case calculating complex credit models in Python using Dask. It is an example of a complex parallel system that is well outside of the traditional “big data” workloads.

- [NumPy 教程第1部分 - Python 数组入门](https://www.machinelearningplus.com/numpy-tutorial-part1-array-python-examples/)
    + numpy

Numpy is the most basic and a powerful package for scientific computing in python. This is part 1 of a mega-tutorial covering all the core aspects of performing data manipulation and analysis with numpy’s ndarrays.

- [63.8% – Python 3 移植数据库](http://fedora.portingdb.xyz/)
    + python3, community, fedora

This is a dashboard to track progress of porting Fedora packages to Python 3.


- [From Mordor, with love: 从头开始设计异步任务调度库 - Part-2](http://templated-thoughts.blogspot.ae/2018/02/designing-async-task-dispatch-library.html)
    + future

In layman terms, a future is an object which can hold the value or result of some computation done asynchronously. What does that mean ?



- [Python to Google Sheets](https://erikrood.com/Posts/py_gsheets.html)
    + google sheets

(`是也乎:`

docs.google 的表格终于有 Python 接口了,
当然, 大陆用不了.

)


- [“Group By” 在 SQL 以及 Python: 比较](https://blog.modeanalytics.com/group-by-sql-python/)
    + pandas, sql

Exploring the overlapping functionality of SQL and Python can help those of us familiar with one language become more adept with the other. And with a deep understanding of both, we can all make smarter decisions about how to combine and leverage each, making it easy to always choose the right tool for every task.

(`是也乎:`

Group By 的叕一个嗯哼...

)


## 好物
~ 包/模块/库/片段...

- [algnuth](https://github.com/louisabraham/algnuth)
    - 240 Stars, 6 Fork

Algebraic Number Theory package.

-[grafana-scripts](https://github.com/DirtyCajunRice/grafana-scripts)
    - 54 Stars, 5 Fork

API scripts written (both pushing and pulling) to aggregate data into influxdb for grafana.


- [cryptory](https://github.com/dashee87/cryptory)
    - 35 Stars, 3 Fork

Retrieve historical crpytocurrency data.

(`是也乎:`

叕一个 加密币值历史查询工具...只是,
至今没有人作个工具来预测币值变化的?

)


- [automation](https://github.com/liubobo/automation)
    - 33 Stars, 8 Fork

code generator


(`是也乎:`

![automation](https://github.com/liubobo/automation/raw/master/iOS%E8%87%AA%E5%8A%A8%E5%8C%96/start.gif)

深度使用 macOS 内置自动化工具的案例集...

国人作品~ iOS代码自动化工具;虽然所有功能, 在一个靠谱的 IDE 中都提供了;
只是留的沟通工具是 QQ 号, README 也是中文的...
好吧, 可以肯定, 周刊官方编辑有华人在掺合了...

)

- [electrum-personal-server](https://github.com/chris-belcher/electrum-personal-server)
    - 31 Stars, 3 Fork

Maximally lightweight electrum server for a single user.

- [r2kit](https://github.com/cmatthewbrooks/r2kit)
    - 28 Stars, 5 Fork

A set of scripts for a radare-based malware code analysis workflow.

- [git-ctm](https://github.com/pavdmyt/git-ctm)
    - 24 Stars, 0 Fork

git Commit Time Machine.

(`是也乎:`

git 提交定时器...嗯哼? 伪装自己在深夜工作?

)

- [augmented-reality](https://github.com/glennglennglenn/augmented-reality)
    - 18 Stars, 4 Fork

Snapchat-like augmented reality filter.

- [brutepanel](https://github.com/code-sploit/brutepanel)
    - 10 Stars, 0 Fork

Brute Panel is a modern admin login path finder written in Python.

- [feed](https://github.com/laixintao/feed)
    - 7 Stars, 1 Fork

Some feeds output from feedly.

(`是也乎:`

叕一个手制造 RSS 聚集器,
国人作品, 挖掘的多数也是中国人的 blog/网站, 
也被 周刊发现了...
使用 cvs2md 生成, 哈...

)


- [Simple-OpenCV-Calculator](https://github.com/EvilPort2/Simple-OpenCV-Calculator)
    - 5 Stars, 4 Fork

A gesture controlled calculator. 

(`是也乎:`

叕一个计算器案例, 套了5层 if 的...
不过看视频还是很屌的: https://youtu.be/6bE9veUsQf4

是通过实时识别手势来完成计算式输入的...
当前只支持个位数字的普通计算

小黑哥, 用力了.

)


### (￣▽￣)

- [爱湃森 2017年度Python榜单](https://annual2017.pycourses.com/)
    + 是也乎
- [Moving efficiently in the CLI](https://clementc.github.io/blog/2018/01/25/moving_cli/)
    + CLI
- [Neilpang/acme.sh: A pure Unix shell script implementing ACME client protocol](https://github.com/Neilpang/acme.sh)
    + https

> 国人作品, 解决 https 部署时的证书生成问题


- [kaleguy/leovue: File viewer for the Leo open source outline editor / IDE, integrated with Vue.js](https://github.com/kaleguy/leovue#leo-vue)
    + Leo,Vue

> 猛然发现, Leo 生态已经走到这种程度了...

![leovue](https://camo.githubusercontent.com/710523b7e44c98cbffe6546278535f6665ef5cec/68747470733a2f2f6b616c656775792e6769746875622e696f2f6c656f7675652f73637265656e63617374732f6c656f7675652d636f6d706f6e656e74732e676966)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...

- [gaojiuli/gain: Web crawling framework based on asyncio for everyone.](https://github.com/gaojiuli/gain)
- [zhoubear/open-paperless: Scan, index, and archive all of your paper documents](https://github.com/zhoubear/open-paperless)

![screenshot](https://github.com/Qix-/better-exceptions/raw/master/screenshot.png)

<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180212 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180212 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


