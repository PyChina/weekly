Title: 蠎加载 103
Slug: importpython-103
Date: 2016-12-15 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 103](http://importpython.com/newsletter/no/103/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [PyCon Canada 视频](https://www.youtube.com/channel/UCclkPrurwUP_ajqi3vDTNDg)
    + video, conference, pycon-canada

PyCon Canada's Youtube channel now has most of the event's videos.

(`是也乎:`

当然的 油管儿的...)

- [通过 Python 函式进行追踪](https://www.mihneadb.net/tracing-through-python-functions/)
    + debugging

python-execution-trace allows you to choose what function you are interested in and it records its execution(s), together with the local state. You can then step through any execution, both forwards and backwards. All you need to do is pip install the library, decorate the target function and run your code as you normally do.

(`是也乎:`

![python-execution-trace](https://www.mihneadb.net/content/images/2016/12/demo.gif)

Py3 的库, python-execution-trace 妄想恢复当年 C++ 的单步追踪的体验..

)

- [课程:用 Python 获取 web 数据 - By University of Michigan](https://www.coursera.org/learn/python-network-data)
    + scraping

This course will show how one can treat the Internet as a source of data. We will scrape, parse, and read web data as well as access data using web APIs.


- [在 Python 中如何规范化/标准化时间序列数据](http://machinelearningmastery.com/normalize-standardize-time-series-data-python/)
    + time-series

Some machine learning algorithms will achieve better performance if your time series data has a consistent scale or distribution. Two techniques that you can use to consistently rescale your time series data are normalization and standardization. In this tutorial, you will discover how you can apply normalization and standardization rescaling to your time series data in Python.

(`是也乎:`

嗯哼?! 居然要动用机械学习!?
)

- [一次奇异的 Python 内存泄漏追踪 - By Benoit Bernard](https://benbernardblog.com/tracking-down-a-freaky-python-memory-leak/)
    + debugging

"I thought that memory leaks were impossible in Python?", I said to myself, staring incredulously at my screen. It was 8:00 PM. The memory use of my crawler was slowly, but steadily increasing. As I hadn't changed any significant portion of my code, this made no sense at all. Had I introduced a new bug? If so, where was it? Here follows the full story of how I tracked down a memory leak in my Python application. Note - Benoit Bernard is writing these long form articles on his debugging experiences it's worth reading.

(`是也乎:`

![graph](https://benbernardblog.com/content/images/2016/12/graph.jpg)

为了挖出来问题根源....
应该使用火熖图了吧?

)

- [Mypy 如何简化编译 Python 的](http://www.infoworld.com/article/3148718/open-source-tools/how-mypy-could-simplify-compiling-python.html)
    + mypy

The Mypy static type-checking project for Python is exploring ways it could aid with effortlessly compiling Python into C or machine language

(`是也乎:`

一切为了编译为 C, 可是为毛?!
)


- [Python Snippetizer](http://pythonsnippetizer.com/)
    + snippets, website

Python snippets for beginners to explore.

- [Python 3.6 中的语法糖](https://medium.com/the-python-corner/syntax-sugar-in-python-3-6-776178ce51f4)
    + python3.6

Simple code snippets showing us what's new in Python 3.6.

(`是也乎:`

这世界上语法糖最多的可能是 Ruby 语言了,然后呢?!
)

- [Why I'm Making Python 2.8](https://www.naftaliharris.com/blog/why-making-python-2.8/)
    + placeholder

For the past two months I've been spending half my time on Python 2.8. Python 2.8 is a backwards-compatible Python interpreter that runs Python 2 code and C-extensions exactly as-is, while also allowing Python 2 programmers to use the most exciting new language features from Python 3. These new backported language features include async/await syntax, function annotations and typing support, keyword-only arguments, and new metaclass syntax, among many others. I use Python 2.8 as my system python now, and haven't had any problems running my old 2.7 code or using packages like IPython, pip, numpy, pandas, requests, and flask.

(`是也乎:`

细思恐极,官方声称放弃 Py2 后,江湖中果断有英雄出面!
2.8 准备继承 Py 2 的遗产,
并成为可以同时运行 Py2和Py3 代码的更加兼容的环境!

已经编译出来的 Py2.8 运行当前所有重要的常见模块/框架都没有问题...
)


- [在 Python 中提高异常敏度- By Moshe Zadka](https://moshez.wordpress.com/2016/12/10/on-raising-exceptions-in-python/)
    + exception handling

There is a lot of Python code in the wild which does something like raise SomeException("Could not fraz the buzz: {} is less than {}".format(foo, quux)). This is, in general, a bad idea. Exceptions are not program panics.




- [谁测试了什么 - By Ned Batchelder](http://nedbatchelder.com//blog/201612/who_tests_what.html)
    + coverage

The next big feature for coverage.py is what I informally call "Who Tests What." People want a way to know more than just what lines were covered by the tests, but also, which tests covered which lines.

(`是也乎:`

越来越关心具体的测试序列对应的覆盖行区块了...
)

## 好物
~ 包/模块/库/片段...


- [learning-to-learn](https://github.com/deepmind/learning-to-learn)
    - 1221 Stars, 119 Fork

Learning to Learn in TensorFlow https://arxiv.org/abs/1606.04474

- [ppgn](https://github.com/Evolving-AI-Lab/ppgn)
    - 164 Stars, 25 Fork

Code for paper "Plug and Play Generative Networks". This repository contains source code necessary to reproduce some of the main results in the paper.


(`是也乎:`

论文:"即插即用网络" 的实践

![1e-1](https://github.com/Evolving-AI-Lab/ppgn/raw/master/examples/chain_epsilon1_1e-1.gif)

可以自动将任意序列的图片进行自然嗯哼.

)

- [tensorflow_qrnn](https://github.com/icoxfog417/tensorflow_qrnn)
    - 60 Stars, 4 Fork

QRNN implementation for TensorFlow

- [tensorflow_speech_recognition_demo](https://github.com/llSourcell/tensorflow_speech_recognition_demo)
    - 38 Stars, 6 Fork

This is the code for 'How to Make a Simple Tensorflow Speech Recognizer' by @Sirajology on Youtube

(`是也乎:`

另一篇文章的对应代码,基于 TF 进行语音识别
)

- [sublimetext-edit_in_new_tab-plugin](https://github.com/borjacampina/sublimetext-edit_in_new_tab-plugin)
    - 20 Stars, 0 Fork

Sublime Text - edit in new tab plugin

(`是也乎:`

![edit_in_new_tab](https://camo.githubusercontent.com/87f2f7ace9bd3b9ff03c1fc4d1b44698c081a78a/68747470733a2f2f7261772e6769746875622e636f6d2f626f726a6163616d70696e612f7375626c696d65746578742d656469745f696e5f6e65775f7461622d706c7567696e2f6d61737465722f6578616d706c652e676966)
)

- [check-domains-py](https://github.com/mavieth/check-domains-py)
    - 16 Stars, 1 Fork

Check WHOIS information for a list of domains 

(`是也乎:`

基于 WHOIS 信息提取域名数据;
要求使用 virtualenv 来隔离运行环境...
win 环境简直了.
)

# 是也乎

- 161219 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161215 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


