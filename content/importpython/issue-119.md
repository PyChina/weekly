Title: 蠎加载 119
Slug: importpython-119
Date: 2017-04-09 11:11
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 119](http://importpython.com/newsletter/no/119/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [一分钟就能将 PEP8 通过 flake8 嗯哼成 git pre-commit hooks](https://medium.com/@importpython/comply-with-pep8-using-flake8-and-git-pre-commit-hooks-it-will-take-just-a-minute-39a343ded293)
    + flake8, pep8, git

Helpful for small Python teams to enforce PEP8 compliance by not allowing commits that aren't PEP8 compliant. Takes only a minute to read and implement.


- [5 大功率令我们不得不从 Py -> Go](https://medium.com/@tigranbs/5-reasons-why-we-switched-from-python-to-go-4414d5f42690)
    + golang

It Compiles Into Single Binary, Static Type System, Performance, You Don’t Need Web Framework For Go, Great IDE support and debugging. Curator's Note - I disagree with not needing a web framework. Having shipped a moderatly size golang web app I missed not being able to make it in Django all the way. Also if you looking to learn go do check out the newsletter http://importgolang.com

(`是也乎:`

能编成单一执行文件;
静态类型系统;
性能;
不用 web 框架;
优良的 IDE 调试支持;

~ 好吧,看来又是一位被 Django 虐过的 gg
)

- [用 Google BigQuery 更好了解 Python 生态系统](https://dev.to/walker/using-googles-bigquery-to-better-understand-the-python-ecosystem)
    + github, bigquery

(`是也乎:`

![BigQuery](https://res.cloudinary.com/practicaldev/image/fetch/s--bqXezros--/c_limit,f_auto,fl_progressive,q_66,w_725/https://d1ax1i5f2y3x71.cloudfront.net/items/3G3U023q252n1B3A0D3L/Screen%2520Recording%25202017-03-28%2520at%252004.57%2520PM.gif%3FX-CloudApp-Visitor-Id%3D2119651)

是的必须的, 前提是海量数据先有了,而且清洗好了.

)

- [理解 Pandas 的变换功能](http://pbpython.com/pandas_transform.html)
    + pandas

- [用以构建 REST API 的 Flask 终极扩展](https://github.com/miLibris/flask-rest-jsonapi)
    + flask

Flask-REST-JSONAPI is a flask extension for building REST APIs. It combines the power of Flask-Restless and the flexibility of Flask-RESTful around a strong specification JSONAPI 1.0. This framework is designed to quickly build REST APIs and fit the complexity of real life projects with legacy data and multiple data storages.


- [Python 编码面试挑战](https://github.com/donnemartin/interactive-coding-challenges)
    + python, interview

Huge update! Interactive Python coding interview challenges (algorithms and data structures).

- [对, Python 很慢, 但俺不在乎](https://hackernoon.com/yes-python-is-slow-and-i-dont-care-13763980b5a1)
    + productivity

- [profile 和 pstats - 性能分析](http://feeds.doughellmann.com/~r/doughellmann/python/~3/BuQxE8nxfjk/)
    + profile

The profile module provides APIs for collecting and analyzing statistics about how Python source consumes processor resources.


- [基于 Python 的类实现 Unix tee-样 功能](http://code.activestate.com/recipes/580767-unix-tee-like-functionality-via-a-python-class/)
    + code snippet

The Unix tee commmand, when used in a command pipeline, allows you to capture the output of the preceding command to a file or files, while still sending it on to standard output (stdout) for further processing via other commands in a pipeline, or to print it, etc.

(`是也乎:`

这位同学, 没有享受过 tee 命令带来的快感吧? 你的人生不完满哪.
)

- [每周聊 Python: 和别人一起学编程](http://ccst.io/e/learn-together)
    + video

- [Django Weblog: Django 1.11 发布](https://www.djangoproject.com/weblog/2017/apr/04/django-111-released/)
    + django

This version has been designated as a long-term support (LTS) release, which means that security and data loss fixes will be applied for at least the next three years. It will also receive fixes for crashing bugs, major functionality bugs in newly-introduced features, and regressions from older versions of Django for the next eight months until December 2017.

(`是也乎:`

又一个 `LTS` 版本...可以放心使用 3年, 足够搞崩又一个新公司了
)





## 好物
~ 包/模块/库/片段...

- [img2html](https://github.com/xlzd/img2html)
    - 198 Stars, 26 Fork

Convert image to HTML


(`是也乎:`

![img2html](https://raw.githubusercontent.com/xlzd/img2html/master/demo/after.png)

国人作品 --> https://xlzd.me/hide/img2html/

用不同颜色的 `爱` 字,重新在网页上展现照片...
目测, 一定表白失败的.

)

- [drawlikebobross](https://github.com/kendricktan/drawlikebobross)
    - 56 Stars, 9 Fork

Draw like Bob Ross using the power of Neural Networks (With PyTorch)!

(`是也乎:`

![drawlikebobross](https://camo.githubusercontent.com/7ef99b70814f63698811a41071c26bf182a82d3d/68747470733a2f2f692e696d6775722e636f6d2f3972645866644d2e706e67)


)

- [BEGAN-tensorflow](https://github.com/carpedm20/BEGAN-tensorflow)
    - 55 Stars, 5 Fork

Tensorflow implementation of "BEGAN: Boundary Equilibrium Generative Adversarial Networks".

(`是也乎:`

![115827_G](https://github.com/carpedm20/BEGAN-tensorflow/raw/master/assets/115827_G.png)

-->

![115827_AE_G](https://github.com/carpedm20/BEGAN-tensorflow/raw/master/assets/115827_AE_G.png)

)

- [consolemd](https://github.com/kneufeld/consolemd)
    - 33 Stars, 0 Fork

Render markdown to the console (not just highlight it).

(`是也乎:`

![consolemd](https://camo.githubusercontent.com/f541e95e510654171f0fdd8d35aa1cd191deb2f7/687474703a2f2f692e696d6775722e636f6d2f625233416c6c592e706e67)

嗯哼, 没有那些 md->CLI 幻灯 工具实用...

)

- [gydl](https://github.com/JannikHv/gydl)
    - 27 Stars, 2 Fork

gydl (Graphical Youtube-dl) is a GUI wrapper around the already existing youtube-dl program.

(`是也乎:`

Youtube-dl 的图形封装 <-- 
哈....都是要跳到海外主机命令行中执行的, 图形界面给毛用...
)

- [google-youtube-history-analytics](https://github.com/srcecde/google-youtube-history-analytics)
    - 19 Stars, 0 Fork

A Python Python Google-YouTube History Analytics, which reads your history data you get from Google and provide analytics about your searches on Google, YouTube and YouTube watch history. It provides number of counts for the term you searched for.

- [pt-styletransfer](https://github.com/tymokvo/pt-styletransfer)
    - 16 Stars, 0 Fork

Neural style transfer as a class in PyTorch

- [wayback-machine-scraper](https://github.com/sangaline/wayback-machine-scraper)
    - 12 Stars, 0 Fork

A command-line utility and Scrapy middleware for scraping time series data from Archive.org's Wayback Machine.

(`是也乎:`

专用中间件 Scrapy 的...
)

- [YouTube-Caption](https://github.com/JacobChrist/YouTube-Caption)
    - 11 Stars, 1 Fork

YoutTube Caption API Python example converted to Python 3.

(`是也乎:`

YouTube 借助 google 的力量, 越来越好用了,
接口也 py3 了
)

- [mitm_postman](https://github.com/viraja1/mitm_postman)
    - 9 Stars, 0 Fork

A tool that creates a Postman collection from App / Web API calls.

- [sphinx-click](https://github.com/stephenfin/sphinx-click)
    - 3 Stars, 0 Fork

A Sphinx plugin to automatically document click-based applications. 

(`是也乎:`

![sphinx](http://www.sphinx-doc.org/en/stable/_static/sphinxheader.png)

真的是这个文档生成工具的插件...
被 md 为基础的嗯哼了很久了,,,
嘦不被 github 内置支持, 基本上没有什么出头的机会了

)

### (￣▽￣)
~ 

# 是也乎

- 170409 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170409 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


