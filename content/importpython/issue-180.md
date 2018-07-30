Title: 蠎加载 180
Slug: importpython-180
Date: 2018-07-15 13:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 180](http://importpython.com/newsletter/no/180/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Transfer of power - Guido van Rossum](https://mail.python.org/pipermail/python-committers/2018-July/005664.html)
    + BDFL

Now that PEP 572 is done, I don't ever want to have to fight so hard for a PEP and find that so many people despise my decisions. I would like to remove myself entirely from the decision process. I'll still be there for a while as an ordinary core dev, and I'll still be available to mentor people -- possibly more available. But I'm basically giving myself a permanent vacation from being BDFL, and you all will be on your own.

(`是也乎:`

    [python-committers] Transfer of power
    Guido van Rossum guido at python.org
    Thu Jul 12 10:57:35 EDT 2018

        Previous message (by thread): [python-committers] A different way to focus discussions
        Next message (by thread): [python-committers] Transfer of power
        Messages sorted by: [ date ] [ thread ] [ subject ] [ author ]

    Now that PEP 572 is done, I don't ever want to have to fight so hard for a
    PEP and find that so many people despise my decisions.

    I would like to remove myself entirely from the decision process. I'll
    still be there for a while as an ordinary core dev, and I'll still be
    available to mentor people -- possibly more available. But I'm basically
    giving myself a permanent vacation from being BDFL, and you all will be on
    your own.

    After all that's eventually going to happen regardless -- there's still
    that bus lurking around the corner, and I'm not getting younger... (I'll
    spare you the list of medical issues.)

    I am not going to appoint a successor.

    So what are you all going to do? Create a democracy? Anarchy? A
    dictatorship? A federation?

    I'm not worried about the day to day decisions in the issue tracker or on
    GitHub. Very rarely I get asked for an opinion, and usually it's not
    actually important. So this can just be dealt with as it has always been.

    The decisions that most matter are probably
    - How are PEPs decided
    - How are new core devs inducted

    We may be able to write up processes for these things as PEPs (maybe those
    PEPs will form a kind of constitution). But here's the catch. I'm going to
    try and let you all (the current committers) figure it out for yourselves.

    Note that there's still the CoC -- if you don't like that document your
    only option might be to leave this group voluntarily. Perhaps there are
    issues to decide like when should someone be kicked out (this could be
    banning people from python-dev or python-ideas too, since those are also
    covered by the CoC).

    Finally. A reminder that the archives of this list are public (
    https://mail.python.org/pipermail/python-committers/) although membership
    is closed (limited to core devs).

    I'll still be here, but I'm trying to let you all figure something out for
    yourselves. I'm tired, and need a very long break.

    -- 
    --Guido van Rossum (python.org/~guido)


> 可以说,这是大家内心都明白不可避免的结果,毕竟岁月不饶人, 老爹真的累了...虽然主要不是身体上的, 
> 但是, 和老哥儿们越来越无法理解新程序猿的期许, 又实在厌烦反复强调相同的事儿...
> 不如眼不见心不烦... Python 2.7 永垂不朽...


)



- [Jupyter notebooks for teaching/learning Python 3](https://github.com/jerry-git/learn-python3#idiomatic-python)
    + learn python

Jupyter notebooks for teaching/learning Python 3

(`是也乎:`

现成的教案...

![比利时](https://avatars0.githubusercontent.com/u/30327563?s=460&v=4)

刚刚赢了3喵军团的国家...

)



- [The Naive Bayes Algorithm in Python with Scikit-Learn](http://stackabuse.com/the-naive-bayes-algorithm-in-python-with-scikit-learn/)
    + naive bayes, scikit-learn

When studying Probability & Statistics, one of the first and most important theorems students learn is the Bayes' Theorem. This theorem is the foundation of deductive reasoning, which focuses on determining the probability of an event occurring based on prior knowledge of conditions that might be related to the event. The Naive Bayes Classifier brings the power of this theorem to Machine Learning, building a very simple yet powerful classifier. In this article, we will see an overview on how this classifier works, which suitable applications it has, and how to use it in just a few lines of Python and the Scikit-Learn library.


(`是也乎:`

叕一则 朴素Bayes 的实现

)



- [Object serialization in Python](https://www.thepythoncorner.com/2018/05/object-serialization-inpython.html)
    + pickle, serialize

Today we’re going to explore a wonderful feature that the Python library offers to you out of the box: the serialization. To serialize an object means to transform it in a format that can be stored, so as to be able to deserialize it later, recreating the original object from the serialized format. To do all these operations we will use the pickle module.

(`是也乎:`

其实理解为数据对象就好,千万别将一切对象都嗯哼出来

)



- [Python Sets: What, Why and How](https://www.pythoncheatsheet.org/blog/python-sets-what-why-how)
    + sets

Python comes equipped with several built-in data types to help us organize our data. These structures include lists, dictionaries, tuples and sets.

(`是也乎:`

其实各种 Py 数据对象基于直觉来用就好...

)


- [A multi-core Python HTTP server (much) faster than Go](https://www.nexedi.com/NXD-Blog.Multicore.Python.HTTP.Server)
    + python, golang

A multi-core Python HTTP server that is about 40% to 110% faster than Go can be built by relying on the Cython language and LWAN C library. A proof of concept validates the possibility of high performance system programming in the Cython language.


(`是也乎:`

多核...基于 LWAN 模块..

![Server io](https://www.nexedi.com/NXD-Blog.Multicore.Python.HTTP.Server/NXD-Image.Multicore.Python.Server.IO?format=)

![Fibonacci](https://www.nexedi.com/NXD-Blog.Multicore.Python.HTTP.Server/NXD-Image.Multicore.Python.Server.Fibonacci?format=)

)


- [Detecting Spam as it happens: Getting Erlang and Python working together with Wallaroo](https://blog.wallaroolabs.com/2018/07/detecting-spam-as-it-happens-getting-erlang-and-python-working-together-with-wallaroo/)
    + erlang, spam

We’ll design and implement a toy spam detection pipeline to demonstrate how to leverage streaming analytics to tackle the issue. We’ll also sketch out the next steps needed to move this solution into production.

(`是也乎:`

靠谱

)


- [appkernel](https://github.com/accelero-cloud/appkernel)
    + microservices

A beautiful python framework "for humans", enabling you to deliver a REST enabled micro-services from zero to production within minutes (no kidding: literally within minutes).


(`是也乎:`

专注给人写的微服务...Flask...

)



- [Optimizing a Python application with C++ code](https://antlarr.io/2018/07/optimizing-a-python-application-with-c-code/)
    + cplusplus

I’ve been working lately in a command line application called Bard which is a music manager for your local music collection. Bard does an acoustic fingerprinting of your songs (using acoustid) and stores all song metadata in a sqlite database. With this, you can do queries and find song duplicates easily even if the songs are not correctly tagged. I’ll talk in another post more about Bard and its features, but here I wanted to talk about the algorithm to find song duplicates and how I optimized it to run around 8000 times faster.

(`是也乎:`

那什么, 不如 golang?

)


- [Classify Passenger Jets Using PyTorch](https://medium.com/@Linpingyu/identify-passenger-jets-in-seconds-using-pytorch-ddba993fa21d)
    + pytorch

But there always be questions for me and my friends: “How can we tell, at a single glance, whether the jet is Boeing or Airbus”. Although experts and enthusiasts can easily distinguish different jets, my friends and I often have hard time correctly identify them.

- [The Sheer Joy of Packaging](https://python-packaging-tutorial.readthedocs.io/en/latest/)
    + packaging

Packaging from start to finish for both PyPI and conda.

(`是也乎:`

叕一则自制 packag 的教程

)



## 好物
~ 包/模块/库/片段...


- [contrib](https://github.com/pytorch/contrib)
    - 115 Stars, 0 Fork

Implementations of ideas from recent papers

- [Research_to_Code](https://github.com/llSourcell/Research_to_Code)
    - 41 Stars, 5 Fork

This is the code for "Research to Code" By Siraj Raval on Youtube

(`是也乎:`

技术图书对应代码仓库...以及

https://youtu.be/pQyzdwHBbqo


)

- [pip-plus](https://github.com/hmhuo/pip-plus)
    - 27 Stars, 0 Fork

pip management tool base base

(`是也乎:`

其实, pip 自身已经足够好了...
问题是和工程结合后的 升级/部署/迁移 操作...至今没有合理的自动化工具.

)


- [django-impersonate-auth](https://github.com/JordanReiter/django-impersonate-auth)
    - 20 Stars, 1 Fork
Impersonation backend for Django

- [tadpole](https://github.com/Ekultek/tadpole)
    - 12 Stars, 2 Fork

Download files out of open AWS buckets

(`是也乎:`

等等...官方有接口的哪...


    (bucketdump) TBG-a0216:tadpole admin$ python tadpole.py
    ------------------------------------------------------------------
      _            _____         ____  _ ______ 
     | |     /\   |  __ \       / __ \| |  ____|
     | |_   /  \  | |  | |_ __ | |  | | | |__   
     | __| / /\ \ | |  | | '_ \| |  | | |  __|  
     | |_ / ____ \| |__| | |_) | |__| | | |____ 
      \__/_/    \_\_____/| .__/ \____/|_|______|[][][]
                         | |                    
                         |_|   Aws Download Open buckEt files v(0.1)
    ------------------------------------------------------------------

    [09:29:39][FATAL] must provide a search query with `-q/--query` flag
    usage: tadpole.py [-h] [-q SEARCH-QUERY] [--random-agent] [--verbose]
                      [-P PROXY] [-H HEADER=1,HEADER=2,etc..] [-s STRING]
                      [--check-proxy] [--swim] [--limit AMOUNT]

    optional arguments:
      -h, --help            show this help message and exit
      -q SEARCH-QUERY, --query SEARCH-QUERY
                            provide a search query to search open buckets with
      --random-agent        Use a random HTTP User-Agent
      --verbose             Run in verbose mode
      -P PROXY, --proxy PROXY
                            Use a proxy for the requests
      -H HEADER=1,HEADER=2,etc.., --headers HEADER=1,HEADER=2,etc..
                            Pass extra headers with your request
      -s STRING, --search STRING
                            Search for a file and output the location of it
      --check-proxy         Verify that your proxy is working correctly
      --swim                Swim upstream to the found bucket and try to pull
                            everything out of it
      --limit AMOUNT        Used in conjunction with `--swim` specify an amount of
                            buckets to pull (*default=300)
    (bucketdump) TBG-a0216:tadpole admin$ 




)


- [instagram-analyzer](https://github.com/nejckorasa/instagram-analyzer)
    - 10 Stars, 1 Fork

Analyzes user's Instagram location geotags to find most frequent locations, countries, cities ...


(`是也乎:`

好象所有有公开 API 的 SNS 服务都有这类自动化分析工具

)

- [stocki](https://github.com/AndrewRPorter/stocki)
    - 7 Stars, 2 Fork

The CLI for fetching stock market data.



- [Liscript-Python](https://github.com/Ivana-/Liscript-Python)
    - 5 Stars, 2 Fork

Liscript command line REPL on Python

(`是也乎:`

大俄罗斯作品..

)


- [MarkdownWriter](https://github.com/vanleo2001/MarkdownWriter)
    - 5 Stars, 2 Fork

A Sublime Text 3 (windows) plugin for markdown writing.

(`是也乎:`

嗯哼? 首次见 windows 专供插件...

![MarkdownWriter](https://github.com/vanleo2001/MarkdownWriter/raw/master/demo1.gif)

)


- [cc.py](https://github.com/si9int/cc.py)
    - 4 Stars, 0 Fork

Extracting URLs of a specific target based on the results of "commoncrawl.org"

(`是也乎:`

叕一则针对具体网站的工具

)


- [flow-dashboard](https://github.com/UoC-Radio/flow-dashboard)
    - 3 Stars, 0 Fork

A flow schedule and zone management app


(`是也乎:`

![dashboard](https://github.com/UoC-Radio/flow-dashboard/raw/master/gallery/thumbnails/imported_thumbnail.png?raw=true)

Gtk....

)

- [elastalert-lambda](https://github.com/beezz/elastalert-lambda)
    - 3 Stars, 1 Fork

Lambda handler for Yelp's ElastAlert

(`是也乎:`

江湖有曰: 一切语言都是对 LISP 的不完备仿制...

)



- [insta.js](https://github.com/gregyjames/insta.js)
    - 3 Stars, 2 Fork

A simple way to download images from instagram.

(`是也乎:`

等等...哈,用了一个 Py web 后台来完成真正的嗯哼

)



- [3DmapsDjango](https://github.com/pengoox/3DmapsDjango)
    - 2 Stars, 1 Fork

How to Add Maps + 3D buildings to Django Web App 



### (￣▽￣)

- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)



*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180715 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180715 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


