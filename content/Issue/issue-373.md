Title: Issue 373
Slug: issue-373
Date: 2019-06-19 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #373](https://pycoders.com/issues/373)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [如果将自己的包合理发布到 PyPI](https://pycoders.com/link/1822/web)
    + REAL PYTHON 
    + video

Learn how to create a Python package for your project and how to publish it to PyPI, the Python Package Repository with this step-by-step tutorial. Quickly get up to speed on everything from naming your package to configuring it using setup.py.


(`是也乎:`

![PyPI](https://ipic.zoomquiet.top/2019-06-19-ScreenShot%202019-06-19%2023.09.51.jpg)

虽然教程很多, 但是, 有专用题图的不多.


)


- [比较Rust,Haskell,C,Python,Scala和OCaml中的相同项目](https://pycoders.com/link/1837/web)
    + TRISTAN HUME

"A rare opportunity to compare implementations of large programs that all did the same thing, written by friends I knew were highly competent, and have a fairly pure opportunity to see what difference design and language choices could make."



- [走向 "Kernel Python"](https://pycoders.com/link/1821/web)
    + GLYPH LEFKOWITZ 
    + opinion

"We need a newer, leaner, unburdened 'kernel' Python. We need to dump the whole standard library out on the floor, adding back only the smallest bits that we need, so that we can tell what is truly necessary and what's just nice to have."

- [在 Python 中用 __main__.py](https://pycoders.com/link/1844/web)
    + SHANE O'NEILL

"The magic file __main__.py is called when you run your project with the -m module flag. If you code is intended to be used a module first, and command line interface second, this makes perfect sense to use. Think of it as a place we can put whatever would be in our body of our if __name__ === "__main__" statement."




- [PyPI现在支持通过 WebAuthn 进行双因登录](https://pycoders.com/link/1853/web)
    + PYFOUND.BLOGSPOT.COM

"To further increase the security of Python package downloads, we're adding a new beta feature to the Python Package Index: WebAuthn support for U2F compatible hardware security keys as a two-factor authentication (2FA) login security method."

- [PSF公布2019年董事会选举结果](https://pycoders.com/link/1826/web)
    + TWITTER.COM/THEPSF

"The 4 available seats go to: Lorena Mesa @loooorenanicole , Kushal Das @kushaldas, Marlene Mhangami @marlene_zw, and Jannis Leidel @jezdez. Congratulations to Lorena, Kushal, Marlene, and Jannis!"

- [Python 动态编程示例](https://pycoders.com/link/1824/web)
    + NATHAN GOLDBAUM

A short introduction to the (confusingly named) concept of dynamic programming with Python.




## 讨论
> Discussions


- [A Fibonacci Assignment Expression Dict Comprehension (??)](https://pycoders.com/link/1838/web)
    + TWITTER.COM/CODEWITHANTHONY


- [Anyone Up for a Funeral for Python 2 on January First 2020?](https://pycoders.com/link/1833/web)
    + REDDIT





## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [想为 CPython 做贡献, 姿势都在这里](https://pycoders.com/link/1831/web)
    + JOANNAH NANJEKYE

"I will try to explain how you can start contributing to CPython borrowing from some few ways I have used and found to work for me."

(`是也乎:`

详解, 如何为 CPython 贡献

)


- [循环更好:深入研究Python中的迭代](https://pycoders.com/link/1834/web)
    + TREY HUNNER

"Python's for loops don't work the way for loops do in other languages. In this article we're going to dive into Python's for loops to take a look at how they work under the hood and why they work the way they do."

- [用 ActiveState 几分钟内构建 Python](https://pycoders.com/link/1859/web)
    + ACTIVESTATE
    + sponsor

Tired of Conda-installing? Automatically build your Python runtime environment with the packages you need: Automatically resolve dependencies, install in a virtual environment with a single command, build Python 2.7 and 3.6 on Linux and Windows. Learn more →

(`是也乎:`

ACTIVESTATE 居然还活着?

)


- [如何用 Argparse 在 Python 中构建 CLI](https://pycoders.com/link/1861/web)
    + REAL PYTHON

In this step-by-step Python tutorial, you'll learn how to take your command line Python scripts to the next level by adding a convenient command line interface that you can write with argparse.


(`是也乎:`

![Argparse](https://ipic.zoomquiet.top/2019-06-19-ScreenShot%202019-06-19%2023.03.19.jpg)


Argparse 不错...只是... Click 们更加现代.

)


- [Python vs R — 为数据科学选择最佳编程语言](https://pycoders.com/link/1842/web)
    + JUN WU opinion

"Functional Programming vs. Imperative Programming, the Nature of R Programming versus Python Programming, Data Science Tasks all determine what programming language to use in Data Science Project."

(`是也乎:`

反正, 数据清洗什么的 Py 最顺手...
)


- [在 Go 和 Python 或 R 之间进行通信](https://pycoders.com/link/1840/web)
    + MATTHEW MAHOWALD

"Sometimes, we need code from one language to call code written in another language directly. In this post, we'll take a short look at how to do that using C foreign function interfaces (FFI) as a way to call functions written in Go using Python."

(`是也乎:`

C 永远丢不了

)


- [用 Docker 更快构建 Pipenv,Poetry 或 Pip-Tools ](https://pycoders.com/link/1843/web)
    + ITAMAR TURNER-TRAURING

"Installing dependencies separately from your code allows you to take advantage of Docker's layer caching. Here's how to do it with pipenv, poetry, or pip-tools."

(`是也乎:`

测试过, 上 Docker 比 Pipenv 祼跑至少多4倍空间, 每次
)




- [从 NodeJS 调用 Python 函数](https://pycoders.com/link/1827/web)
    + NICK FRANKEN

On NodeJS and Python interoperability.

(`是也乎:`

嗯哼, 这个可以有
)


- [用 Python 爬 Stack Overflow](https://pycoders.com/link/1832/web)
    + NAVEEN VERMA

(`是也乎:`

嗯哼? 这是刚需哪...
只是依赖 C++ 写的包装器.我

)

- [用 Python 生成词云图片](https://pycoders.com/link/1846/web)
    + STANISLAS MORBIEU


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [flake8-black: Flake8 Plugin to Run Black for Checking Python Coding Style](https://pycoders.com/link/1850/web)
    + GITHUB.COM/PETERJC 
    + • Shared by Python Bytes Podcast

(`是也乎:`

类似 flake8 的 EPE8 工具, 原本就应该集成到仓库中,
但是....所以, ....

)


- [semantic: Parsing, Analyzing, and Comparing Source Code Across Many Languages](https://pycoders.com/link/1839/web)
    + GITHUB.COM/GITHUB

(`是也乎:`

叕一个静态代码分析工具

)


- [Voilà: Turn Jupyter Notebooks Into Standalone Web Applications](https://pycoders.com/link/1835/web)
    + JUPYTER.ORG

(`是也乎:`

将 Jupyter 笔记直接发布为 we 应用?
好思路哪...

)


- [lutris: Open Source Gaming Platform for GNU/Linux](https://pycoders.com/link/1825/web)
    + GITHUB.COM/LUTRIS

(`是也乎:`

Linux 一直没放弃游戏平台

)


- [Python Preview: VS Code Plugin That Creates Object-Visualizations for Python](https://pycoders.com/link/1845/web)
    + VISUALSTUDIO.COM 
    + • Shared by Python Bytes Podcast

(`是也乎:`

叕一个 VSCode 的 py 可视化插件

)


- [fern: Curses-Based Mastodon Client](https://pycoders.com/link/1828/web)
    + GITHUB.COM/ENKIV2

(`是也乎:`


                            
                                
       :##  Ｆｅｄｅｒａｔｅｄ  
       #. Ｅｄｉｔｏｒ  ａｎｄ  
       # Ｒｅａｄｅｒ  ｏｆ  Ｎｅｗｓ                                                               
     #####   ###    #:##: #:##: 
       #       :#   ##  # #  :#   /.\
       #    #   #   #     #   #  // \\
       #    #####   #     #   #  \\///
       #    #       #     #   #   \//
       #        #   #     #   # -=//=-
       #     ###:   #     #   #-=//==-
                                


)



## 📆🐍 活动/大会
> Events


- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/1847/web)
    + June 22, 2019
    + 印度

- [⋅ GeoPython 2019](https://pycoders.com/link/1851/web)
    + June 24 to June 27, 2019
    + 

- [⋅ Inland Empire Pyladies (CA, USA)](https://pycoders.com/link/1823/web)
    + (CA, USA) 
    + June 24, 2019

- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/1848/web)
    + June 25, 2019
    + 多米尼加

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/1820/web)
    + June 26, 2019
    + 汉堡

- [⋅ Dash Conference](https://pycoders.com/link/1857/web)
    + July 16–17 in NYC
    + 大苹果


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- 七牛云年中大促
    + sponsor

[七牛云服务]没赶上618?七牛云年中大促,狂欢到月底!存储秒杀低至0.001元/G,云主机0元抢,另有多款产品5折起,每日限量购,手慢无!https://dwz.cn/HfTSeUHE

(`是也乎:`

7牛 应该是亚洲最大单体 golang 服务了, 
从创始之初就一直给 CPyUG 系列社区以渠道联盟的待遇,
提供空间和流量, 长期用下来, 对比其它 CDN 是真的好用...

CLI 工具最舒服的一家了.

)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 本周毕业

> 下期应该 7月1


[![PyScaffold](https://pyscaffold.org/en/latest/_images/logo.png)](https://pyscaffold.org/en/latest/)

~ helps you setup a new Python project


- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
    + FAQ

(`是也乎:`

![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)

总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...

其实, 本质上并不是对应技术是否有什么能力,
而是相反...

)


### Jobs:
> ...

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
    + 北京
    + anti-996


# 是也乎

- 190619 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190619 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
