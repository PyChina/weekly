Title: 蠎加载 129
Slug: importpython-129
Date: 2017-06-15 19:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 129](http://importpython.com/newsletter/no/129/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [fsudoku: 快速数独解算器](https://github.com/jcoffland/fsudoku)
    + codesnippet

I decided to crush Sudoku, once and for all, by solving all Sudoku puzzles in one fell swoop and in less than 300 lines of Python.



- [PyDev 周刊: Amir Rachum](http://www.blog.pythonlibrary.org/2017/06/12/pydev-of-the-week-amir-rachum/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheMouseVsThePython+%28The+Mouse+Vs.+The+Python%29)
    + interview

This week we welcome Amir Rachum as our PyDev of the Week. Amir is the author / maintainer of pydocstyle and yieldfrom. Amir also write a fun little blog about Python. Let’s take a few moments to get to know Amir better!

(`是也乎:`

pydocstyle / yieldfrom 的作者, 一看名字就是...

<-- [About](http://amir.rachum.com/about/)
)

- [colorama](https://medium.com/getpy/colorama-e7aaa0cdae4c)
    + codesnippet

colorama allows you to print text in color on the terminal.

(`是也乎:`

![windows](https://github.com/tartley/colorama/raw/master/screenshots/windows-demo.png)

早已推荐过...


    from colorama import Fore, Back, Style
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')

)

- [ShutIt](https://learnxinyminutes.com/docs/shutit/)
    + codesnippet

ShutIt is an shell automation framework designed to be easy to use.

(`是也乎:`

非-win 平台支持..

![ShutIt](https://github.com/ianmiell/shutit/raw/gh-pages/images/ShutIt.png)
)

- [Timsort in Python](https://medium.com/@sivabalanb92/timsort-in-python-wickedly-fast-sorting-bc57bb46a030)
    + algorithms

Sorted(list) vs list.sort()


- [Instagram 平滑升级到 Python 3 - 在 Instagram 身后的工程师](https://thenewstack.io/instagram-makes-smooth-move-python-3/)
    + interview

Four. Hundred. Million. Users. Per. Day. Not only has Instagram scaled to become the biggest Python user in the world, but the company recently moved over to Python 3 with zero user experience interruption. Instagram engineers Hui Ding and Lisa Guo talked with The New Stack to share the Python love and describe the Python 3 migration experience.


(`是也乎:`

![python3performance](https://cdn.thenewstack.io/media/2017/06/562968f5-python3performance.jpg)

简单的说...没那么简单.

)

- [Twitter 上的 NLP 广告数据](https://medium.com/towards-data-science/twitter-advertising-1d497d066fef)
    + NLP

I chose to perform Natural Language Processing (NLP) on Twitter data in order to assist in advertising campaigns. This project is geared more towards advertisers, marketing, and any company who wants to extend their customer relations platform to communicate with their followers.

(`是也乎:`

简单的说, 只有商业成功的技术方案才有权力继续嗯哼...
)


- [用 uWSGI 在 Docker 部署迷你 Python](https://medium.com/@greut/minimal-python-deployment-on-docker-with-uwsgi-bc5aa89b3d35)
    + docker

So, you’ve built a great Python web application using Flask, Django, aiohttp, or Falcon. The next issue you could be facing is probably the setup regarding the deployment. We will explore how to use docker-compose to deploy a WSGI application using uWSGI and NGINX.

(`是也乎:`

简单的说, 还是离开不能 NGNIX
)

- [A good way to lose an afternoon reading about Python's internals](https://twitter.com/kevin_london/status/875059550944206849)
    + tweet

- [TDD 课程 - By The RealPython Folks](http://testdriven.io/)
    + tutorial

In this tutorial, you'll learn how to quickly spin up a reproducible development environment with Docker to create a RESTful API powered by Python, Postgres, and the Flask web framework....


- [极端 Lazy 来并行 Python 函式](http://tdhopper.com/blog/2017/Jun/07/parallelizing-a-python-function-for-the-extremely-lazy/)
    + codesnippet

- [用 Python 检验伪影片](http://sunnybala.com/2017/05/28/python-video-loop-detection.html)
    + codesnippet

Program to detect if there are any loops in the video.


- [用 Python 来折腾音频信号](https://thehackerdiary.wordpress.com/2017/06/09/it-is-ridiculously-easy-to-generate-any-audio-signal-using-python/)
    + codesnippet

Now it comes as a surprise to many people when I tell them that generating an audio waveform is extremely simple.

(`是也乎:`

有一系列案例代码 -> [3.5-Sensor2Phone/generate_any_audio.py at master · makermovement/3.5-Sensor2Phone](https://github.com/makermovement/3.5-Sensor2Phone/blob/master/generate_any_audio.py)

项目名叫 `3.5mm` ~ 问题是, 已经出现倾向: 这一标准接口将消失
)

- [如何用 Jupyter Notebook 从 Google Analytics 获取数据](https://read.dataly.co/google-analytics-api-how-to-get-data-from-google-analytics-with-python-in-jupyter-notebook-with-85483dd73e22)
    + codesnippet

Today I found an online tool that can get the stats of the published articles from Google Analytics. That’s how I got interested in Google Analytics API. As I am studying Data Science at the moment, knowing how to do web analytics would open up a lot of new possibilities.

(`是也乎:`

![GAnalytics](https://cdn-images-1.medium.com/max/800/0*HwS77OZGVUi1Pjuw.png)

简单说就是配置过程太复杂了...

)


- [Python 填字游戏拼图生成器](http://bryanhelmig.com/python-crossword-puzzle-generator/)
    + codesnippet

- [Python Requests 构建](https://medium.com/journey-of-one-thousand-apps/building-with-python-requests-d9260b26e7ab)
    + codesnippet

- [Epithet](https://www.wordfugue.com/introducing-epithet/)
    + github

Introducing Epithet, a Python-based command line tool for managing labels across an organization. You give it a Github key, organization, and label name, and it will make sure that label exists across all the repos in your org. Give it a color, and it’ll make the color of that label consistent across all repos as well. Have you decided you’re done with a particular label? Epithet can delete it from all your repos for you. Are you using Github Enterprise? Epithet supports that too.

(`是也乎:`

又一个 CLI 工具, 通过标签来管理组织的仓库...
哈.
)


- [搞笑 - Python 私有方法](https://dzone.com/storage/temp/5554985-python-private-methods.png)
    + humor

(`是也乎:`

![5554985-python-private-methods.png（PNG 图像，900x1000 像素） - 缩放 (79%)](https://dzone.com/storage/temp/5554985-python-private-methods.png)

)

- [RC Car + MacBook Pro = The Carputer!](https://blog.hackster.io/rc-car-macbook-pro-the-carputer-b3b7f10e38e1)
    + arduino

If you’d like to build a miniature self-driving car, perhaps you would first turn to an Arduino for control or even a Raspberry Pi for more advanced processing. Otavio Good is no exception, but after attaching a few Arduinos to an RC car, he moved on to driving it with a speedometer and camera via a TensorFlow neural network running on a Macbook Pro?—?yes, it has an actual notebook computer embedded in the 1/10th-scale model car.


(`是也乎:`


![原型](https://cdn-images-1.medium.com/max/800/1*2zTxBkYBjLdX7eabuIxY_g.jpeg)

)

- [Python 数据科学书 Jupyter 版](https://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb)
    + data science

This is the Jupyter notebook version of the Python Data Science Handbook by Jake VanderPlas; the content is available on GitHub.* The text is released under the CC-BY-NC-ND license, and code is released under the MIT license. If you find this content useful, please consider supporting the work by buying the book!

(`是也乎:`

![PDSH](https://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/figures/PDSH-cover.png)

伟大的 CC 保护下, 好书整体嗯哼成 .ipynb 了!

)

- [Toolchest for Python shell scripters](https://medium.com/hultner/how-to-write-bash-scripts-in-python-10c34a5c2df1)
    + command line

Curated list of tools/packages.

(`是也乎:`

一系列 CLI 中好用的模块推荐:
~[sh](https://amoffat.github.io/sh/)
嗯哼是最实用的一个
)

- [对 LHL Facebook 页面回复的情感分析](https://medium.com/@jiayu./sentiment-analysis-of-comments-on-lhls-facebook-page-9db8b3a60eb3)
    + machine learning



- [Python 中的 Go-Flavored 错误处理](https://expl.info/display/MISC/Go-Flavored+Error+Handling+in+Python)
    + golang

The point of this article is to present an Error class in the spirit of Go error handling and consider its use/application in Python from a personal perspective.


- [在 Python 中嵌入 Go 和 groupcache](https://www.nathanvangheem.com/posts/2017/06/03/embedding-golang-in-python-with-groupcache.html)
    + go

Go(golang) is a very fast and efficient compiled programming language. Much like how you can build Python C-extensions to speed up your python applications, Python developers also have the option to build Go components that are embedded into their python.


- [Python 中变量的玩耍](http://baruchel.github.io/python/2017/07/10/playing-with-variables-in-python/)
    + core-python

The first one is a decorator “freezing” some global variables to their current value at the time a function is defined.


- [为毛 context-manager 是种更好的嗯哼?](https://medium.com/@sinister/https-medium-com-sinister-why-using-a-context-manager-is-a-better-choice-55ccfcecddb8)
    + core-python






## 好物
~ 包/模块/库/片段...


- [stephanie-va](https://github.com/SlapBot/stephanie-va)
    - 525 Stars, 58 Fork

Stephanie is an open-source platform built specifically for voice-controlled applications as well as to automate daily tasks imitating much of an virtual assistant's work.

(`是也乎:`

专门为定制语音助手构建的支持库,
当然的,没中文什么事儿...
)

- [end-to-end-negotiator](https://github.com/facebookresearch/end-to-end-negotiator)
    - 204 Stars, 22 Fork

Deal or No Deal? End-to-End Learning for Negotiation Dialogues

(`是也乎:`

有关 AI 的检验游戏?
)

- [yotaq](https://github.com/JoseTomasTocino/yotaq)
    - 153 Stars, 6 Fork

yotaq - Your Own Task Queue for Python

(`是也乎:`

又一个任务队列,通过 Docker,redis...
)

- [validus](https://github.com/shopnilsazal/validus)
    - 141 Stars, 5 Fork

A dead simple Python data validation library.

(`是也乎:`

又一个校验库, 死简单? 有这种 en?
)

- [Headless-rendering-with-python](https://github.com/cprogrammer1994/Headless-rendering-with-python)
    - 6 Stars, 0 Fork

Headless 3D rendering with python 

(`是也乎:`

![sitting](https://raw.githubusercontent.com/cprogrammer1994/Headless-rendering-with-python/master/data/sitting.png)

是的,无头是流行了性行为...
)


### (￣▽￣)

- [无我编程的十条戒律 | 湾区日报](https://wanqu.co/a/5177/2017-06-06-the-ten-commandments-of-egoless-programming.html?s=social)
    + zen,coder

这是 StackOverflow 联合创始人 Jeff Atwood 注释的十戒。程序员普遍有很强的 ego，都应该看看本文，打印下来时刻提醒自己：）

(`是也乎:`

![Ten Commandments of Egoless Programming](https://blog.codinghorror.com/content/images/uploads/2006/05/6a0120a85dcdae970b0120a86d5ea4970b-pi.jpg)

源自 71 年神书: [The Psychology of Computer Programming](https://www.amazon.com/exec/obidos/ASIN/0932633420?tag=wanquribao-20)

![银年纪念版](https://img3.doubanio.com/lpic/s28104646.jpg)

- 承认并接受你也会犯错
- 你不是你的代码
- 无论你有多少奇招, 别人都有更多
- 获得共识前不要重写代码(<-- 不是重构)
- 在尊重和耐心的前提下, 和菜鸟沟通
- 世上唯一不变的是变化 (即, PM 是自然现象)
- 真正的权威源自知识而不是立场 (呵呵...)
- 为你坚信的战斗, 但得优雅的接受失败
- 嫑作 "房间摆设" (悲惨工作三征兆:无闻/无关/不可测)
- 批评代码而不是人


> 软件的人性化原则 是永恒的

`(￣▽￣)` 可惜, 程序猿的边缘化也是永恒的...

)


# 是也乎

- 170615 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170615 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


