Title: 蠎加载 130
Slug: importpython-130
Date: 2017-06-22 13:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 130](http://importpython.com/newsletter/no/130/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [10分钟在 Python 3.6 用起静态数据类型检查](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b)
    + static type

Automatically catch many common errors while coding

(`是也乎:`

目前只有少数 IDE 比如 [PyCharm](https://www.jetbrains.com/pycharm/) 支持 py3 这种语法,
以及并没有证据表明, 在混合使用新旧数据声明的代码项目,
可以不用其它手段就可能提高运行效能.

)

- [用 flake8 对 python 项目自动进行代码复审](https://blog.sideci.com/automatically-review-code-for-python-projects-using-flake8-6fcb056a001a)
    + flake8

I’ll now introduce flake8, a tool for checking Python syntax. SideCI supports code review automation for Python projects using flake8.

(`是也乎:`

古典的配置形式...

    [flake8]
    # it's not a bug that we aren't using all of hacking, ignore:
    # F812: list comprehension redefines ...
    # H101: Use TODO(NAME)
    # H202: assertRaises Exception too broad
    # H233: Python 3.x incompatible use of print operator
    # H301: one import per line
    # H306: imports not in alphabetical order (time, os)
    # H401: docstring should not start with a space
    # H403: multi line docstrings should end on a new line
    # H404: multi line docstring should start without a leading new line
    # H405: multi line docstring summary not separated with an empty line
    # H501: Do not use self.__dict__ for string formatting
    ignore = F812,H101,H202,H233,H301,H306,H401,H403,H404,H405,H501

)


- [Linting 对 Python 代码进行轻量级缺陷检测](https://dev.to/sethmichaellarson/linting-as-lightweight-defect-detection-for-python)
    + linting

When many people think of linting they think about how it improves the readability and maintainability of code by forcing developers to stick with an agreed upon code style. This is indeed one of the major merits of having a 'linter' as a part of your build process, but it's not the only one!


(`是也乎:`

Flake8 突然爆发这么多软文是几个意思?
)

- [Python 图表分析探索](http://pythonplot.com/)
    + graphs

Plotting is an essential component of data analysis. As a data scientist, I spend a significant amount of my time making simple plots to understand complex data sets (exploratory data analysis) and help others understand them (presentations). In particular, I make a lot of bar charts (including histograms), line plots (including time series), scatter plots, and density plots from data in Pandas data frames.

(`是也乎:`

![Plotting](http://pythonplot.com.s3-website-us-east-1.amazonaws.com/img/banner.png)


为 ggplot 章目的软文, 问题是 R 味儿忒重,
另外, 没有解决根本上的发布问题, 这事儿目前看就是bokeh 意识到了:

- 图形
- html
- ipynb

以上三种常见输出场景, 如果没有简洁的输出指令, 那么基本上不是个可用的图表库了...

)


- [Fedora 爱 Python](https://fedoralovespython.org/)
    + fedora

We're Python Special Interest Group, and we're making Fedora an even better system for Python developers, and Python an even better language for Fedora.

(`是也乎:`

![fedoralovespython](https://fedoralovespython.org/static/img/fedoralovespython.svg)

![embedded](https://fedoralovespython.org/static/img/embedded.svg)

讲真, 一个技术社区的实力,基本上可以从其设计能力正比评测出来...

)


- [Python 3 的杀手级特性: asyncio](https://medium.com/@PaxosGlobal/python-3s-killer-feature-asyncio-28b147e99fb4)
    + asyncio

- [Gunicorn — autoreload app](https://medium.com/@n1_/gunicorn-autoreload-app-5a38a343665a)
    + gunicorn

Do you run your Django app under Gunicorn and you want to reload it once you change the source code in your editor? No problem!

(`是也乎:`

俗称的一句话干货: `reload=True`

)


- [将文本映射到颜色](https://medium.com/apollo-data-solutions-blog/mapping-words-to-colors-cfa23a65d8c4)
    + code snippet



## 好物
~ 包/模块/库/片段...

- [transformer](https://github.com/Kyubyong/transformer)
    - 299 Stars, 41 Fork

A TensorFlow Implementation of the Transformer: Attention Is All You Need

- [automating-AWS-with-Python](https://github.com/tejas-kr/automating-AWS-with-Python)
    - 35 Stars, 4 Fork

automating AWS with Python using boto3 library.

- [django-admin-env-notice](https://github.com/dizballanze/django-admin-env-notice)
    - 24 Stars, 0 Fork

Visually distinguish environments in Django Admin

(`是也乎:`

![prod](https://github.com/dizballanze/django-admin-env-notice/raw/master/screenshots/prod.png)

极简 UX 侵入

)

- [InsideCoreML](https://github.com/hollance/InsideCoreML)
    - 9 Stars, 1 Fork

Python script to examine Core ML's mlmodel files

- [Fantastic-Transcoder](https://github.com/ClearSlide/Fantastic-Transcoder)
    - 8 Stars, 0 Fork

Fantastic transcoder is a video transcoder which utilizes massively parallel compute to achieve ludicrous conversion speeds.

(`是也乎:`

![FantasticTranscoder](https://github.com/ClearSlide/Fantastic-Transcoder/raw/master/FantasticTranscoder-v4.jpg)

基于 AWS 生态体系的....

)

- [ShopifyScraper](https://github.com/threebarber/ShopifyScraper)
    - 5 Stars, 0 Fork

Shopify Scraper (not monitor) 

(`是也乎:`

![ShopifyScraper](https://camo.githubusercontent.com/048d9e2862ed2f9579764302a5c161138837ee44/68747470733a2f2f7332312e706f7374696d672e6f72672f37327773767233636e2f7363726170657277696e646f772e706e67)

专用的...

)

### (￣▽￣)

- [被忽视的攻击面：Python package 钓鱼](http://paper.seebug.org/326/)
    + pypi

(`是也乎:`

嚓了个嚓...
)


# 是也乎

- 170623 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170623 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


