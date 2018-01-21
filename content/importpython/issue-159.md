Title: 蠎加载 159
Slug: importpython-159
Date: 2018-01-19 22:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 159](http://importpython.com/newsletter/no/159/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [如何加速 Python 应用程序的启动时间?](https://dev.to/methane/how-to-speed-up-python-application-startup-time-nkf)
    + processing time

Python 3.7 has new feature to show time for importing modules. This feature is enabled with -X importtime option or PYTHONPROFILEIMPORTTIME environment variable.

(`是也乎:`

Py3.7 果断划出很多精力来提升速度
)


- [使用文本分析来量化角色](https://medium.com/agatha-codes/using-textual-analysis-to-quantify-a-cast-of-characters-4f3baecdb5c)
    + NLTK

If you’ve ever worked on a text and wished you could get a list of characters or see how many times each character was mentioned, this is the tutorial for you.

(`是也乎:`

NLP 基础分析需求叕一次工具化

)


- [在 asyncio 应用程序中寻找内存泄漏](https://tech.gadventures.com/hunting-for-memory-leaks-in-asyncio-applications-3614182efaf7)
    + memory leaks, async

Sailing into the last two weeks of 2017 that I fully intended to spend experimenting with various eggnog recipes. I was alerted by our DevOps team that our asyncio app was consuming 10GB of memory. That is approximately 100 times more than it should!

(`是也乎:`

等等, Python 也有内存嗯哼问题?
一个从 10亿回到100M 的故事
)

- [DjangoCon JP 2018](https://djangocon.jp/)
    + conference

DjangoCon JP is a conference for the Django Web framework in Japan. If you're a seasoned Django pro or just starting, DjangoCon JP is for you. Our goal is for atendees to meet, talk, share tips, discover new ways to use Django, and, most importantly, have FUN.

(`是也乎:`

国外的技术大会世家都是年初, 
中国的在年尾...所以, 基于文化还是经济原因呢?
)


- [路径 flat 即功成](https://www.vinta.com.br/blog/2018/flat-success-path/)
    + code-quality

If you want to write clear and easy to understand software, make sure it has a single success path. A 'single success path' means a few things. First, it means that any given function/method/procedure should have a single clear purpose.

(`是也乎:`

很久没有见这种代码品质的经验讨论了...

)


- [规范化流程教程，第1部分：分布和决定因素](http://blog.evjang.com/2018/01/nf1.html)
    + tensorflow

This series is written for an audience with a rudimentary understanding of linear algebra, probability, neural networks, and TensorFlow. Knowledge of recent advances in Deep Learning, generative models will be helpful in understanding the motivations and context underlying these techniques, but they are not necessary.

- [预制 Docker 镜像基于 GPU 来 OpenAI Gym 开发和 TensorFlow ](https://medium.com/@pascal.brokmeier/a-gpu-ready-docker-container-for-openai-gym-development-with-tensorflow-9be3d61504cb)
    + docker, tensorflow

So, you want to write an agent, competing in the OpenAI Gym, you want to use Keras or TensorFlow or something similar and you don’t want everything installed on your workstation? You have come to the right place!

(`是也乎:`

随着 tensorflow 工具链的增长,这个 Docker 的体积当然的将越来越嗯哼

)


- [用 Python 检查 Coinbase 中收支平衡](https://medium.com/@samhagin/check-your-balance-on-coinbase-using-python-5641ff769f91)
    + coinbase

Even though Coinbase has a mobile application so you’re able to check your balance on the go, I prefer using their API instead so I can setup custom alerts not available on their platform.

(`是也乎:`

Coinbase, 哈, 一看名字就知道是相关什么

)


- [使用 bower 通过 Django 管理静态文件](https://medium.com/@siddhism/using-bower-to-manage-static-files-with-django-8521331023af)
    + django


Sharing a way to manage libraries like bootstrap, jquery with bower without using any external app.

(`是也乎:`

所以, PHP 发明之初就内置的工具, Django 一直在嗯哼
)



- [自动模型选择：H2O AutoML](https://medium.com/@mohtedibf/automatic-model-selection-h2o-automl-79b3b4696f58)
    + modeling

In this post, we will use H2O AutoML for auto model selection and tuning. This is an easy way to get a good tuned model with minimal effort on the model selection and parameter tuning side.

(`是也乎:`

叕一个 AI 框架.

)

- [Python 中的逻辑回归](https://medium.com/python-learning-notes-those-cool-stuff/logistic-regression-in-python-c9c9b76848fa)
    + sklearn




## 好物
~ 包/模块/库/片段...

- [SimpleCoin](https://github.com/cosme12/SimpleCoin)
    - 209 Stars, 20 Fork

Just a really simple, insecure and incomplete implementation of a blockchain for a cryptocurrency made in Python as educational material. In other words, a simple Bitcoin clone.


(`是也乎:`

叕一个 blockchain 的开发框架, 纯Python 实现.

![SimpleCoin](https://camo.githubusercontent.com/36c87280f39f06d85212463b9125028c67d7cae5/68747470733a2f2f6b36302e6b6e332e6e65742f332f422f332f462f452f432f3031332e706e67)

当然, 基于 Btc 的软分叉

)


- [languagecrunch](https://github.com/artpar/languagecrunch)
    - 136 Stars, 8 Fork

LanguageCrunch NLP server docker image.

(`是也乎:`

细思恐极, 好象一个开发工具没有 Docker 镜像发行版就不正规似的..

)


- [howtopython.org](https://github.com/kennethreitz/howtopython.org)
    - 86 Stars, 16 Fork

A (book, website) that decribes how to Python, from scratch.

- [unimatrix](https://github.com/will8211/unimatrix)
    - 83 Stars, 4 Fork

Python script to simulate the display from "The Matrix" in terminal. Uses half-width katakana unicode characters by default, but can use custom character sets. Accepts keyboard controls while running. Based on CMatrix.

(`是也乎:`

叕一个 Matrix 屏保工具
![screenshot1](https://github.com/will8211/unimatrix/raw/master/screenshot1.png?raw=true)

2000年左右, 俺用 Flash 实现过一次...
只是,当前这个仅支持 Py3

)


- [spacy-lookup](https://github.com/mpuig/spacy-lookup)
    - 32 Stars, 1 Fork

Named Entity Recognition based on dictionaries.

(`是也乎:`

spaCy <~ 的辅助工具,
叕一个 NLP 分析框架

)

- [simpledb](https://github.com/coleifer/simpledb)
    - 14 Stars, 0 Fork

miniature redis-like server implemented in Python.

(`是也乎:`

叕一个 redis样 再制DB 

)


- [python-bigone](https://github.com/sammchardy/python-bigone)
    - 10 Stars, 1 Fork

BigONE Exchange API python implementation for automated trading.

(`是也乎:`

叕一个 `多幣種全球交易平台` 的接口,
神奇的是私人作品, 没有通过组织仓库来组织

)

- [django-multiple-user-types-example](https://github.com/sibtc/django-multiple-user-types-example)
    - 10 Stars, 1 Fork

Django Quiz Application

- [spotify-lyrics-cli](https://github.com/kenogo/spotify-lyrics-cli)
    - 9 Stars, 0 Fork

Automatically get lyrics for the song currently playing in Spotify from command line.

(`是也乎:`

叕一个 spotify 扩展工具,
所以, 一个流行服务没有稳定的公开接口体系, 那真心没有各种场景中的专用工具出来;

那么, 进一步的, 新的用户需求也将无法浮现...

)


- [aws-security-checks](https://github.com/PortSwigger/aws-security-checks)
    - 7 Stars, 0 Fork

AWS Security Checks.

- [sgqlc](https://github.com/profusion/sgqlc)
    - 5 Stars, 0 Fork

Script for tracking file system changes.



- [sgqlc](https://github.com/profusion/sgqlc)
    - 5 Stars, 1 Fork

Simple GraphQL Client.

(`是也乎:`

什么是 GraphQL? <- RESTful 系统的 SQL, 叕一个 DSL 专门服务于 API 系统...

)


- [shellson](https://github.com/logileifs/shellson)
    - 4 Stars, 0 Fork

py-fake-rs: a fake data generator for python, backed by fake-rs in rust.

(`是也乎:`

叕一个 Mock 类工具,
但是, 用  Rust 来扩展是几个意思?

)


- [shellson](https://github.com/logileifs/shellson)
    - 3 Stars, 1 Fork

JSON command line parser.

(`是也乎:`

嗯哼, 一个管道流中的处理工具

)

- [django-qsessions](https://github.com/QueraTeam/django-qsessions)
    - 3 Stars, 0 Fork

Extends Django's cached_db session backend. 



### (￣▽￣)

*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...

- [gaojiuli/gain: Web crawling framework based on asyncio for everyone.](https://github.com/gaojiuli/gain)
- [zhoubear/open-paperless: Scan, index, and archive all of your paper documents](https://github.com/zhoubear/open-paperless)

![screenshot](https://github.com/Qix-/better-exceptions/raw/master/screenshot.png)

<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180121 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180119 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


