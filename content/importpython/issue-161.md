Title: 蠎加载 161
Slug: importpython-161
Date: 2018-01-31 10:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 161](http://importpython.com/newsletter/no/161/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- ["装饰器模式" 以及 Python "wrapt" 模块.](http://blog.dscpl.com.au/2018/01/the-pattern-versus-python-package.html)
    + wrapt

Brandon Rhodes published a post today about the Decorator Pattern and how that translates into Python. He explains the manual way that the pattern can be implemented in Python as a wrapper, as well as how you can try to minimise the amount of work you need to do by overriding special methods of a Python object. The wrapt package I authored was purpose built for this task of creating wrappers which Brandon describes, and much more. To avoid some of the name confusion around Decorator Pattern versus Python decorators, which Brandon highlights as an issue, I tend to refer to the wrappers as transparent object proxies.


(`是也乎:`

叕一个对原生特性增强的模块,来自 Hear no evil, see no evil, patch no evil: Or, how to monkey-patch safely. - YouTube https://www.youtube.com/watch?v=GCZmGgtWi3M

NZPyUG 的年度大会 KiwiPyCon 2017...

14年就发布的老梗, 作者还在一直讲...


)



- [预测第一投手的薪水](https://medium.com/discovering-data-science-a-chronicle/predicting-starting-pitcher-salaries-4b7a4a26cb65?source=rss------datascience-5)
    + data science, jupyter

Today’s post focuses on applying linear regression techniques to a less-than-ideal dataset. In order to do so, I need a scenario from which to work. As of this writing, the MLB free agent signing period (or ‘Hot Stove’ as it is affectionately named) is in full effect. Therefore, I chose the following problem statement as my challenge: my client, a professional baseball team, is interested in offering a contract to a free agent starting pitcher and wants a recommendation for the annual salary it should propose. Now that I have my problem, I can begin working on the answer!


(`是也乎:`

线性回归技术的一个真实案例
)



- [用 AWS Lambda 来爬取数千产品](https://engineering.21buttons.com/crawling-thousands-of-products-using-aws-lambda-80332e259de1)
    + Selenium, lamda, chromedriver

Or how to run Headless Chrome on AWS Lambda together with Python, Selenium and Chromedriver

(`是也乎:`

无头 Chrome 的又一个嗯哼案例

)


- [Zulko/moviepy: 用Python编辑视频](https://github.com/Zulko/moviepy)
    + video

MoviePy (full documentation) is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects. See the gallery for some examples of use.

(`是也乎:`

MoviePy 的确是一个完备的视频折腾工具,
可以说是 FFmpeg 的 Pythonic 包装

)

- [Django — Asset compression and Storages](https://blog.botreetechnologies.com/django-asset-compression-and-storages-55e3d4d590ee)
    + django

The problem was, once we change something in the CSS/JS, that change was not getting reflected on the client side and browser was taking the old files from the cache. To avoid this, we needed a mechanism to refresh the cache once anything has changed in the CSS/JS. The obvious approach was to change the name or attach a version number to a CSS file each time we make a change. But we wanted this process to be automated so we came across Django-compressor.

- [在 Windows,Mac 和 Linux 上处理文件路径的简单方法](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)
    + core-python

Python 3.4 introduced a new standard library for dealing with files and paths called pathlib?—?and it’s great!

(`是也乎:`

Py3 的软文叕一则

)


- [Jupyter Notebook 技巧来提高 Data Science 效率](https://medium.com/@nokkk/jupyter-notebook-tricks-for-data-science-that-enhance-your-efficiency-95f98d3adee4)
    + jupyter


(`是也乎:`

叕一则 Jupyter 的数据科学嗯哼技巧

)



- [用 Bounter pt. 2 有效地计数: CountMinSketch](https://rare-technologies.com/counting-efficiently-with-bounter-pt-2-countminsketch/)
    + counter

In my previous post on the new open source Python Bounter library we discussed how we can use its HashTable to quickly count approximate item frequencies in very large item sequences. Now we turn our attention to the second algorithm in Bounter, CountMinSketch (CMS), which is also optimized in C for top performance.



- [Reportlab: 用 Python 进行 PDF 处理 ~ Mike Driscoll — Kickstarter](https://www.kickstarter.com/projects/34257246/reportlab-pdf-processing-with-python)
    + kickstarter

Learn how to create PDFs using the popular Python programming language and the ReportLab toolkit. Kickstarter campaign.




- [gist-evernote](https://github.com/leemengtaiwan/gist-evernote)
    + project, gist, evernote
 
A Python application that sync Github Gists and save them to Evernote notebook as screenshots.

- [Python 中监督机器学习算法](https://www.toptal.com/machine-learning/supervised-machine-learning-algorithms)
    + machine learning

The main goal of this reading is to understand enough statistical methodology to be able to leverage the machine learning algorithms in Python’s scikit-learn library and then apply this knowledge to solve a classic machine learning problem. The first stop of our journey will take us through a brief history of machine learning. Then we will dive into different algorithms. On our final stop, we will use what we learned to solve the Titanic Survival Rate Prediction Problem.




- [用 Python 解压缩 zip 文件的最快方法](https://www.peterbe.com/plog/fastest-way-to-unzip-a-zip-file-in-python)
    + code snippet, zip

So the context is this; a zip file is uploaded into a web service and Python then needs extract that and analyze and deal with each file within. In this particular application what it does is that it looks at the file's individual name and size, compares that to what has already been uploaded in AWS S3 and if the file is believed to be different or new, it gets uploaded to AWS S3.

(`是也乎:`

不是不用解压缩就能使用所有内容的嘛?

)


## 好物
~ 包/模块/库/片段...

- [minigo](https://github.com/tensorflow/minigo)
    - 1201 Stars, 83 Fork

An open-source implementation of the AlphaGoZero algorithm.


- [captivox](https://github.com/expectocode/captivox)
    - 47 Stars, 3 Fork

cool animations with pyqt5 and parametrics

(`是也乎:`

少见的 Qt5 工具

![captivox](https://github.com/expectocode/captivox/raw/master/captivox.gif)

专注生成动画

)


- [cryptoCMD](https://github.com/guptarohit/cryptoCMD)
    - 37 Stars, 3 Fork

Cryptocurrency historical market price data scraper in Python


(`是也乎:`

叕一个加密币价格查询器, CLI 的

)


- [tinfoleak](https://github.com/vaguileradiaz/tinfoleak)
    - 28 Stars, 2 Fork

The most complete open-source tool for Twitter intelligence analysis.

(`是也乎:`

叕一个更加嗯哼的 Twitter 数据分析框架

)


-[Rust_Api_Generator](https://github.com/LivingInSyn/Rust_Api_Generator)
    - 21 Stars, 0 Fork

a toolset for autogenerating rust APIs and translating structs.

(`是也乎:`

不是 rust 语言, 而是支持多种语言的结构化 API 代码生成

)


- [invoiceless](https://github.com/forrestbrazeal/invoiceless)
    - 18 Stars, 1 Fork

Serverless backend for sending simple recurring invoices.


(`是也乎:`

叕一则 AWS 生态的次级嗯哼

)

- [python-patterns](https://github.com/brandon-rhodes/python-patterns)
    - 14 Stars, 0 Fork

Source code behind the python-patterns.guide site by Brandon Rhodes.

(`是也乎:`

叕一部新书的配套代码...
所以, 现在技术图书没有配套的 github 仓库, 基本上可以不用看了...

当然, github 发布前的老书不在此列.

)


- [django_social_pill](https://github.com/devmanorg/django_social_pill)
    - 7 Stars, 3 Fork

Django Social Pill offers convenience tools for routine tasks concerning social authentication.

- [django_binance_trader](https://github.com/conroy-cheers/django_binance_trader)
    - 6 Stars, 0 Fork

Automated trading bot for Binance.

- [vc-crypt](https://github.com/drdrsh/vc-crypt)
    - 4 Stars, 0 Fork

A simple python script with zero dependencies that can be used to encrypt/decrypt secret credentials (API secret keys, HTTP passwords, etc.) using a password to be able to safely put them under version control.


(`是也乎:`

和 Pyenv 类似, 用约定的特殊文件来切换不同的嗯哼

)

- [python3_with_pleasure](https://github.com/arogozhnikov/python3_with_pleasure)
    - 0 Stars, 0 Fork

A short guide on features of Python 3 for data scientists. 

(`是也乎:`

所以, 以往 Py2 嗯哼的领域, 都得用 Py3 重新宣传一次?

![python3_with_pleasure](https://camo.githubusercontent.com/9936046c7d691a3f6d74c2873e483332b7a0b20e/68747470733a2f2f75706c6f6164732e746f7074616c2e696f2f626c6f672f696d6167652f39323231362f746f7074616c2d626c6f672d696d6167652d313435373631383635393437322d62653266333830666533616164343133333334323765636435613165633563352e6a7067)
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

- 180205 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180204 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


