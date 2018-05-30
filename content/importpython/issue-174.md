Title: 蠎加载 174
Slug: importpython-174
Date: 2018-05-31 12:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 174](http://importpython.com/newsletter/no/174/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [中级 Python eBook - Free](http://book.pythontips.com/en/latest/index.html)
    + ebook

If you are a beginner, intermediate or even an advanced programmer there is something for you in this book. Please note that this book is not a tutorial and does not teach you Python. The topics are not explained in depth, instead only the minimum required information is given.

(`是也乎:`

叕一本免费入门书...
所以, 图书免费, 找作者干点儿什么再收费?

)



- [用特征标记驯服不可逆性](https://www.vinta.com.br/blog/2018/taming-irreversibility-feature-flags-python/)
    + software engineering

Feature Flags are a very simple technique to make features of your application quickly toggleable. The way it works is, everytime we change some behavior in our software, a logical branch is created and this new behavior is only accessible if some specific configuration variable is set or, in certain cases, if the application context respects some rules.


(`是也乎:`

简单的说, 防御型软件架构, 远远没有到放弃的地步...

)

- [Python 咯表驱动单元测试](http://opensourceprojects.org/python-table-driven-unit-test-in-python/)
    + unit testing

Now days, table driven tests are pretty much industry standard. In my workplace, we use table driven tests when we write unit tests (in golang though). Here I shall share a simple code example using pytest that shows how to write table driven tests in Python. In table driven test, what you need to do is, to gather all the tests cases together in a single table. We can use dictionary for each test case and a list to store all the test cases. Instead of discussing it further, let me show you an example.


(`是也乎:`

其实吧, 单元测试的难点不在技术, 而在成本的认同...

)


- [Qt for Python: under the hood](http://blog.qt.io/blog/2018/05/24/qt-for-python-under-the-hood/)
    + pyside

When the PySide project was launched back in 2009, the team decided to use external tools to generate Python bindings from Qt C++ headers. One of the main concerns, besides using a tool that properly handles all the Qt C++ constructs, was the size of the final packages. The previous choice was using templates excessively, hence another alternative was required. After analyzing a few other options the team decided to write their own generator, Shiboken.

(`是也乎:`

Qt 当年的开源是自救,现在面对移动互联网, 却一直没找到嗯哼点...

当然从  PySide --> Shiboken ,
可能也只是因为 `Why not` 毕竟客户不多...

)


- [用 Python 和 scrapy, xarray, 以及 cartopy 可视化全球土地温度](https://cbrownley.wordpress.com/2018/05/15/visualizing-global-land-temperatures-in-python-with-scrapy-xarray-and-cartopy/)
    + scrapy, xarry, cartopy

A few years ago, I worked on a project that involved collecting data on a variety of global environmental conditions over time. Some of the data sets included cloud cover, rainfall, types of land cover, sea temperature, and land temperature. I enjoyed developing a greater understanding of our Earth by visualizing how these conditions vary over time around the planet. To get a sense of how fun and informative it can be to analyze environmental data over time, let’s work on visualizing global land surface temperatures from 2001 to 2016.


(`是也乎:`

![global-land-temperatures](https://cbrownley.files.wordpress.com/2018/05/12-monthly-averages.gif?w=869)

当然, 一切的开始, 还是得要先有公开数据


)


- [A Gilectomy 更新](https://lwn.net/Articles/754577/)
    + gil

In a rather short session at the 2018 Python Language Summit, Larry Hastings updated attendees on the status of his Gilectomy project. The aim of that effort is to remove the global interpreter lock (GIL) from CPython. Since his status report at last year's summit, little has happened, which is part of why the session was so short. He hasn't given up on the overall idea, but it needs a new approach. Gilectomy has been "untouched for a year", Hastings said. He worked on it at the PyCon sprints after last year's summit, but got tired of it at that point. He is "out of bullets" at least with that approach. With his complicated buffered-reference-count approach he was able to get his "gilectomized" interpreter to reach performance parity with CPython—except that his interpreter was running on around seven cores to keep up with CPython on one.

(`是也乎:`

真的有人真正动手来清除所有 `GIL` ,
虽然 Guido 不动手, 但是, 开源世界里, 不代表不可能...

)


- [forge](https://github.com/dfee/forge)
    + project

forge is an elegant Python package for crafting function signatures. Its aim is to help you write better, more literate code with less boilerplate.

(`是也乎:`

![forge](https://raw.githubusercontent.com/dfee/forge/master/docs/_static/forge-horizontal.png)

好闹...

)


- [用 Python 实现缝线雕刻](https://karthikkaranth.me/blog/implementing-seam-carving-with-python/?utm_source=reddit&utm_medium=social)
    + image processing

Seam carving is a novel way to crop images without losing important content in the image. This is often called “content-aware” cropping or image retargeting.


(`是也乎:`

![pietro_first_seam](https://karthikkaranth.me/img/pietro_first_seam.jpg)


内容感知向的图片智能裁剪

)

- [Bpython - 可选交互式 Python 解释器 - YouTube](https://www.youtube.com/watch?v=HDwKdUfWfGk)
    + video

Bpython - alternative interactive python interpreter

(`是也乎:`

和 IPyNB 同时期诞生的交互增强,
可惜, 人家都独立为 `Jupyter` 了,

Bpython 还在嗯哼...
)



- [Python 中的抽象语法树(ast library)](https://medium.com/@SergioPaniego/abstract-syntax-trees-in-python-ast-library-9bfd705ef9f1)
    + AST

An Abstract Syntax Tree is a simplified syntactic tree representation of a programming language’s source code. Each node of the tree stands for an statement occurring in the code. This trees don’t show the entire syntactic clutter, just the important information for analyzing the code. If it showed the entire structure it would be a Concrete Syntax Tree, but it’s usually better to simplify it because the information we use when building compilers can be found on an abstract syntax tree.

(`是也乎:`

内置的只是可用, 远远达不到大家的期待..

)


## 好物
~ 包/模块/库/片段...


- [SmoothLife](https://github.com/duckythescientist/SmoothLife)
    - 383 Stars, 11 Fork

Continuous Domain Game of Life in Python with Numpy

(`是也乎:`

![smoothlife](https://github.com/duckythescientist/SmoothLife/raw/master/img/smoothlife.gif)

哈原理和 Wolframe 提出的可计算世界一样

![SmoothLife](https://camo.githubusercontent.com/53467ab1e4484a875086f78f71b10554b20c3eef/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f662f66322f47616d655f6f665f6c6966655f616e696d617465645f676c696465722e676966)

)


- [SleuthQL](https://github.com/RhinoSecurityLabs/SleuthQL)
    - 123 Stars, 17 Fork

Python3 Burp History parsing tool to discover potential SQL injection points. To be used in tandem with SQLmap.

(`是也乎:`

SQL 不死...因为数据太多在其控制之下了...

)


- [pypykatz](https://github.com/skelsec/pypykatz)
    - 106 Stars, 11 Fork

Mimikatz implementation in pure Python




- [Emojinator](https://github.com/akshaybahadur21/Emojinator)
    - 65 Stars, 25 Fork

A simple emoji classifier for humans.

(`是也乎:`

![Emojinator](https://github.com/akshaybahadur21/Emojinator/raw/master/emo.gif)


印度 gg 们对 CV 都很积极...
因为?

)


- [R2Plus1D-PyTorch](https://github.com/irhumshafkat/R2Plus1D-PyTorch)
    - 65 Stars, 4 Fork

PyTorch implementation of the R2Plus1D convolution based ResNet architecture described in the paper "A Closer Look at Spatiotemporal Convolutions for Action Recognition"

(`是也乎:`

叕一则 PyTorch 工具
)


- [twitchslam](https://github.com/geohot/twitchslam)
    - 24 Stars, 0 Fork

Live coding SLAM

(`是也乎:`

习惯性内心补上 `DUNK`


![twitchslam](https://raw.githubusercontent.com/geohot/twitchslam/master/example.png)


)


- [python-doctl](https://github.com/kennethreitz/python-doctl)
    - 20 Stars, 1 Fork

A Python wrapper for the Digital Ocean CLI utility — doctl.





- [kasane](https://github.com/google/kasane)
    - 18 Stars, 0 Fork

A simple kubernets deployment manager

(`是也乎:`

叕一个 K8s 的辅助工具

)


- [advanced-data-analytics-using-python](https://github.com/Apress/advanced-data-analytics-using-python)
    - 16 Stars, 8 Fork

Source Code for 'Advanced Data Analytics Using Python' by Sayan Mukhopadhyay

(`是也乎:`

现在出本技术图书, 没有对应的 gh 仓库, 简直就象是徦的

)


- [org-babel-tangle.py](https://github.com/thblt/org-babel-tangle.py)
    - 11 Stars, 2 Fork

The same, much faster.


(`是也乎:`

Emacs 的插件也都开始 py 化了?
)



- [same-same](https://github.com/gwk/same-same)
    - 11 Stars, 0 Fork

A git diff highlighter

(`是也乎:`

![same](https://github.com/gwk/same-same/raw/master/doc/example-same-same.png)

其实, 将 CLI 嗯哼的5颜6色 并不一定舒服


)

- [s3tree](https://github.com/sanketsaurav/s3tree)
    - 10 Stars, 0 Fork

Access S3 like a tree.

(`是也乎:`

其实, 类似 S3/7牛的对象式云空间, 
一直都需要合理的常见结构化访问界面

)



- [evt2sigma](https://github.com/Neo23x0/evt2sigma)
    - 7 Stars, 0 Fork

Log Entry to Sigma Rule Converter


(`是也乎:`

各种数据格式转换, 简直就是 py 的最随手命题了...

)


- [gitDiffTool](https://github.com/luochenxun/gitDiffTool)
    - 4 Stars, 0 Fork

GitDiffTool is a tool to compare two commits of a gitProject and generate the diff into html. You can read the diff in one html page, the list of modified files on one side and the specifics diff-content on the other. 


(`是也乎:`


![luochenxun](https://avatars3.githubusercontent.com/u/7877801?s=460&v=4)

国人作品, 因为输出 html 的汇报结果,也的确是中国特色钢需了...

中山大学 - 算是计算机科班出道

    在 百度 搞了3年 
    离职 创业 1年 
    加入 平安科技 搞了半年 
    加入 加油宝 ，开混互联网金融 

简单说也是 ICO 圈里人了...

可惜这工具并没有输出对应修订了的文件的具体嗯哼

> 右边栏是改动的具体内容

并没有...
)




### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180531 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180531 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


