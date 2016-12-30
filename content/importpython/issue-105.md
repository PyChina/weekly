Title: 蠎加载 105
Slug: importpython-105
Date: 2016-12-30 19:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 105](http://importpython.com/newsletter/no/105/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [现代字典 ~ Raymond Hettinger : Python](https://www.youtube.com/watch?v=p33CVV29OG8)
    + core-python, dict

Python's dictionaries are stunningly good. Over the years, many great ideas have combined together to produce the modern implementation in Python 3.6. This fun talk is given by Raymond Hettinger, the Python core developer responsible for the set implementation and who designed the compact-and-ordered dict implemented in CPython for Python 3.6 and in PyPy for Python 2.7.

(`是也乎:`

事实证明一个贴心的数据类型可以增加很多语言的依赖,
但是,另外一个现实也证明了只有一种数据类型的开发语言一样可以很好的使用,
所以? 存乎一心了.
)

- [通过 SSH 远程运行 Python 3](http://www.revsys.com/tidbits/python-3-run-command-over-ssh/)
    + ssh, click

I ran into this situation today where I wanted to issue a few commands over ssh to a remote host as part of a Click command I'm building to do some ops automation here at REVSYS. It's probably not perfect in terms of error handling, but it sure is simple!.

(`是也乎:`

嗯哼,就是 Fabric3 的软广呗.
)


- [用 Python 介绍数据科学 - Univeristy of Michigan](https://www.coursera.org/learn/python-data-analysis/)
    + data science, mooc

The course will also introduce data manipulation and cleaning techniques using the popular python pandas data science library and introduce the abstraction of the DataFrame as the central data structure for data analysis. The course will end with a statistics primer, showing how various statistical measures can be applied to pandas DataFrames. By the end of the course, students will be able to take tabular data, clean it, manipulate it, and run basic inferential statistical analyses.

(`是也乎:`

就是 panda 呗...
)

- [用 Python 进行数据整理](http://www.jeannicholashould.com/tidy-data-in-python.html)

In this post, I will summarize some tidying examples Wickham uses in his paper and I will demonstrate how to do so using the Python pandas library.

(`是也乎:`

依然是 Panda 呢...
)


- [用 Python 查询和展示天气数据](https://medium.com/planet-os/querying-and-rendering-weather-data-with-python-72ac1938fc21)
    + data science

Considering rich Python Ecosystem of tools, libraries, and frameworks for data crunching, I’d like to share a few examples how to plug Datahub API as a data source to your Python-based workflow. I’ll start with a simple example: how to turn Datahub API JSON output into Numpy arrays using Pandas framework.

(`是也乎:`

针对 Datahub API 输出的 JSON
)


- [2017 放弃 Python 2](https://medium.com/broken-window/python-3-support-for-third-party-libraries-dcd7a156e5bd)
    + python3

Python 3.6.0 came out day before yesterday, and it was like a Christmas present for many of us. But in the midst of all the celebration, many of you were still asking if it is safe to drop Python 2 and move over to Python 3. There still seems to be a fear of missing out on useful third party libraries that lack Python 3 support. So in this post, I will try to settle this issue once and for all by presenting the relevant data. After you have seen all the data, you will be able to come to your own conclusion (I have already expressed my conclusion in the title).

(`是也乎:`

目测嗯哼的...
)


- [从 Python 到 Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)
    + numpy

There are already a fair number of books about Numpy (see Bibliography) and a legitimate question is to wonder if another book is really necessary. As you may have guessed by reading these lines, my personal answer is yes, mostly because I think there is room for a different approach concentrating on the migration from Python to Numpy through vectorization.

(`是也乎:`

![cubes](http://www.labri.fr/perso/nrougier/from-python-to-numpy/data/cubes.png)

是一部完备的小书...CC 协议,还没有翻译为中文....
[rougier/from-python-to-numpy: An open-access book on numpy vectorization techniques, Nicolas P. Rougier, 2017](https://github.com/rougier/from-python-to-numpy)

rST 格式

)


- [加速 Python 运行: 案例研究](http://www.faingezicht.com/articles/2016/12/25/means/)
    + performance

- [支持 PyKids 服务](https://www.gofundme.com/pykids)
    + community

pykids is a voluntary effort to bring Python to elementary school (5th & 6th grades). At present I run AWS servers to support my venture. These servers are available for anyone to use. I run a monthly bill of about 20 USD to run this server. The money that you donate will go into support keeping these servers online.


- [为小白的 Python IDE](http://thonny.org/)
    + IDE

(`是也乎:`

乱说! 初学更加不应该用 IDE 了...
)

- [检查 Python 包依赖](http://orkohunter.net/depends/)
    + dependency

(`是也乎:`

可怕的 [Dependencies of django](http://orkohunter.net/depends/django/)
)

- [为毛 Python 不是俺的最爱](https://zenhack.net/2016/12/25/why-python-is-not-my-favorite-language.html)
    + opinion

(`是也乎:`

Python 的目标从来不是最爱哪...

)


## 好物
~ 包/模块/库/片段...

- [soundhax](https://github.com/nedwill/soundhax)
    - 124 Stars, 20 Fork

A heap overflow in tag processing leads to code execution when a specially- crafted m4a file is loaded by Nintendo 3DS Sound. This bug is particularly good, because as far as I can tell it is the first ever homebrew exploit that is free, offline, and works on every version of the firmware for which the sound app is available.

(`是也乎:`

是的,不支持中文...
)


- [pep8speaks](https://github.com/OrkoHunter/pep8speaks)
    - 69 Stars, 3 Fork

A GitHub integration to automatically review Python code style over Pull Requests

(`是也乎:`

在 PR 时,自动运行的风格检查器
)

- [mx-lsoftmax](https://github.com/luoyetx/mx-lsoftmax)
    - 24 Stars, 7 Fork

卷积神经网络的大边际Softmax损失的mxnet版本


- [objectify](https://github.com/gideonn/objectify)
    - 9 Stars, 1 Fork

Upload any image, and the app will tell you the object in the image and translate it to any language you want (read out aloud).

(`是也乎:`

基于 EC2 和 Google Vision API 的图片内容识别服务,
给俺一张图片,俺告诉你图片里有什么...
)

- [djangohero](https://github.com/gutfeeling/djangohero)
    - 8 Stars, 2 Fork

DjangoHero automates the process of starting a new Django project on Heroku.

(`是也乎:`

自动化在 Heroku 上部署一个新 Django 实例的过程
)

- [pipupdate](https://github.com/o355/pipupdate)
    - 2 Stars, 1 Fork

An easy-to-use PIP package manager. Update, force reinstall, do an easy requirements.txt install, and uninstall all packages in 1 command. 

(`是也乎:`

又一个基于 `requirements.txt` 的包含管理工具,
可是大家需要的只是:

根据代码净化包环境+快速迁移所有包含恢复到另外一个虚拟环境或是主机上,
其它的都是伪需求..
)

# 是也乎

- 161230 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161230 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


