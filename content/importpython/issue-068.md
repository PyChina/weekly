Title: 蠎加载 68
Slug: importpython-68
Date: 2016-04-14 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 68](http://importpython.com/newsletter/no/68/)

## 该读
~ 文章, Blog, 教程...



- [有个 app 的念头?](https://azure.microsoft.com/en-us/trial/free-trial-open-source/?WT.mc_ID=OLA_11087206637883_11087205814819)
    + Sponsor

Create a new app, free with Azure App Service, now.

(`是也乎:`

可见 M$ 是有诚意的,只是一切必须透过 VS ...
而且中国区指定世纪互联代理...呵呵...
)


- [基于 Falsk 创建可扩展/可容错的 REST 端服务](http://www.ibm.com/developerworks/cloud/library/cl-scalable-fault-tolerant-rest-endpoint-flask-python-bluemix-trs/index.html)
    + flask

展示如何用命令行工具,部署 Falsk 和 AngularJS 结合的应用到 IBM Bluemix® .
教程中, 
选择了不同 Django, Pyramid, 或是 web2py 的框架,
Flask, 因为更加小巧.
如果嘦一个 REST 接口服务,更加合用.
并展示了 REST 端服务如何在不同功能中进行多路复用.

- [15 则 Python 面试基本问题](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
    + interview

想获得 Python 职位?
首先得证明能用 Python 完成工作.
这里给出了一系列涵盖了 Python 语言相关的基础技能/问题.
只专注语言本身,没有涉及包/框架.
每个问题都有对应的教程, 希望得的上.

- [Ruby vs. Python](https://www.toptal.com/technology-battles/ruby-vs-python)
    + podcast

Toptal 特别约专家 Damir Zekic 和 Amar Sahinovic,
来讨论这两个知名脚本语言的特性.
收听节目,还能投票反馈你的见解.

(`是也乎:`

PHP是最好的语言!
)


- [用 Django 创建公司前最希望知道的 11 件事儿: ](https://medium.com/cs-math/11-things-i-wish-i-knew-about-django-development-before-i-started-my-company-f29f6080c131#.gc8qecmdy)
    + Computer Science, Math, and Statistics.

两年前创办了 `Math & Pencil`.
之前对 web 开发的经验基本为 0.
为了公司, 从头学习了HTTP, Javascript, AJAX, 以及 Django MVC.
虽然急促,但是技术桟是成熟的.
基于 D3.js, Backbone.js, Celery, Mongo, Redis, 等等一堆其它东西,
完成了数据科学相关的应用!
回顾写下来的代码,
认为这几件事儿,必须事先明确了.


- [Christine Doig 写的 Data Science 漫游指南 ](https://speakerdeck.com/chdoig/the-hitchhickers-guide-to-data-science)
    + data science

又一则 `Hitchhickers Guide`

Slidedeck that shows tools needed to be productive as a data scientist.

- [将 Ember 和 Django 搞在一起: 待办应用演练](https://www.smallsurething.com/making-ember-and-django-play-nicely-together-a-todo-mvc-walkthrough/)
    + tutorial

教程包含
Django 的 JSON 接口服务,完成 CRUD 支持;
用 token 完成安全认证.



- [用 Watson TextToSpeech 创建语言警报和通知](https://developer.ibm.com/recipes/tutorials/creating-alerts-notifications-using-python-and-watson-texttospeech/)

IBM Watson 是自然语言处理和机器学习平台.
能从海量非结构数据挖掘出规律.
通过 Python 接口,可以快速完成 报警和通知系统.

(`是也乎:`

目测不通中文..
)

- [在 Azure 中构建 Django 应用](https://azure.microsoft.com/en-in/documentation/articles/web-sites-python-create-deploy-django-app/)
    + django, azure


You will create an application using the Django web framework. You will create an application using the Django web framework (see alternate versions of this tutorial for Flask and Bottle). You will create the web app from the Azure Marketplace, set up Git deployment, and clone the repository locally. Then you will run the application locally, make changes, commit and push them to Azure. The tutorial shows how to do this from Windows or Mac/Linux. Curator Note - Our sponsor Azure is offering free $200 to use on Azure for Linux projects. Check it out.- http://goo.gl/fd17H9


- [简化 Segment 分析](http://goo.gl/RCr8iZ)
    + Sponsor

Segment 是可定制的数据平台,
开发者和分析师通过优雅的 API 同广泛的合作伙伴形成了兴盛的生态.



- [兼容 Python3 的关键字唯一参数传真修饰.](http://code.activestate.com/recipes/580639-python2-keyword-only-argument-emulation-as-a-decor/)
    + code snippet

Provides a very simple decorator (~40 lines of code) that can turn some or all of your default arguments into keyword-only arguments. You select one of your default arguments by name and the decorator turn this argument along with all default arguments on its right side into keyword only arguments.

- [和 NGINX 最大化 Python 性能, 第一部分 : Web 服务和缓存](https://www.nginx.com/blog/maximizing-python-performance-with-nginx-parti-web-serving-and-caching/)
    + nginx

所有人都希望自家网站和应用运行的更快.
可惜越来越多的流量以及冲击,总能引发宕机问题.
时常进入忙-崩-忙 的循环.
而且杯具的是,几乎所有崩溃问题都发生在业务增长的关键时刻.
这时就是 NGINX 大显身手的时刻了....

- [依赖性注入在 Bottle/Flask](http://qihqi.github.io/python/dependency-injection-python/)

在一个 OOP 方式构成的系统中,
通常有两种类型的对象:
数据对象(存储数据)
和服务对象(操作数据).
例如,
有数据库在后端时,必然有服务对象和数据库进行交互...



- [深入 PyCharm 中的测试](http://blog.jetbrains.com/pycharm/2016/04/in-depth-screencast-on-testing/)
    + pycharm

仅仅4分钟的视频中,
展示了 PyCharm 运行原生 pytest ,
通过最近追加的 tox 支持,管理文档测试安全带,
并能理解本地配置...
甚至是用母语来表述的测试....


- [Python 3.6 的新特性](https://docs.python.org/3.6/whatsnew/3.6.html)
    + core python

This article explains the new features in Python 3.6, compared to 3.5.

- [第52集 - Hypothesis 和 David MacIver](http://podcastinit.podbean.com/e/episode-52-hypothesis-with-david-maciver/)
    + podcast

Writing tests is important for the stability of our projects and our confidence when making changes. One issue that we must all contend with when crafting these tests is whether or not we are properly exercising all of the edge cases. Property based testing is a method that attempts to find all of those edge cases by generating randomized inputs to your functions until a failing combination is found. This approach has been popularized by libraries such as Quickcheck in Haskell, but now Python has an offering in this space in the form of Hypothesis.

- [数据分析基础 II - 朴素贝叶斯网络](http://blog.endpoint.com/2016/04/learning-from-data-basics-ii-simple.html)

去年的文章中介绍了能简化复杂的概率计算的模型: 朴素贝叶斯.
在电子商务领域,
给用户的推广框功能,能预测用户最想买的商品.
实际应用中的效果不错.
这其实就是基于改进的  朴素贝叶斯网络 模型.


- [如何构建 Heroku 插件](https://buttercms.com/blog/how-to-build-a-heroku-add-on)

Butter CMS 
能协助我们快速构建/测试/发布 Heroku 插件.

- [针对年轻程序的教程开放注册了!](http://pycon.blogspot.in/2016/04/registration-is-open-for-our-young.html)
    + pycon, community

`The Young Coders`
工作坊, 通过游戏探索 Python 编程.
从基础的数据类型开始,快速体验基本语句,
然后就可以基于 pygame 的图书馆游戏结合构建自己的游戏了!
这次 PyCon 专门为儿童设立的全天教程活动!
推荐注册体验!



## 新书
~ New Books

- [Python 描述符: 完全指南](http://www.lulu.com/spotlight/jacobz_20)
    + book

![book face](http://static.lulu.com/browse/product_thumbnail.php?productId=22634851&resolution=320)

本书希望探讨 描述符 这一基础思想在各种实用场景中的应用,
令大家都能更好的构建自己的描述符应用.

## 项目
~ 包/模块/库/片段...


- [DynamicMemoryNetworks](https://github.com/swstarlab/DynamicMemoryNetworks)
    - 26 Stars, 9 Fork

Python 实现的 DMN

- [PyCraft](https://github.com/traverseda/PyCraft)
    - 12 Stars, 4 Fork

`"Minecraft in 500 lines of python"` 
的分支, 准备完成一个真正的引擎,
而不仅仅是演示

- [api-star](https://github.com/tomchristie/api-star)
    - 12 Stars, 0 Fork

基于 Flask & Falcon 的 API 框架

- [django-gunicorn](https://github.com/uranusjr/django-gunicorn)
    - 12 Stars, 0 Fork

用 Gunicorn 驱动的 Django 框架

- [waybackpack](https://github.com/jsvine/waybackpack)
    - 10 Stars, 0 Fork

根据链接从 Wayback Machine 档案仓库中下载.

- [dodotable](https://github.com/spoqa/dodotable)
    - 8 Stars, 1 Fork

支持 SQLAlchemy 的 HTML 表格生成器

- [unsafe](https://github.com/jribbens/unsafe)
    - 7 Stars, 3 Fork

检验不可信代码,
在沙箱中防止逃逸.


- [quotekey](https://github.com/santoshankr/quotekey)
    - 7 Stars, 1 Fork

SSH 密钥对精品生成器!
个性化你的 SSH keys.

(`是也乎:`

![quotekey](https://github.com/santoshankr/quotekey/raw/master/quotekey.png?raw=true)

能夹入私人语句...

)


- [spammy](https://github.com/prodicus/spammy)
    - 5 Stars, 0 Fork

私人垃圾邮件过滤器

- [python_console.log](https://github.com/ScottBarkman/python_console.log)
    - 3 Stars, 1 Fork


JS 程序猿转行入 Python 时必须品.

Its about time that python got a console.log. For years, JavaScript developers have had a one up on Python. They've been able to print whatever they like to the console using the infamous console.log command. It's about time python had this killer functionality. I've managed to replicate this behavior using state of the art python class(es).



## DAMA 无责任推荐

- [pyenv-mirror](https://github.com/huntzhan/pyenv-mirror)
    + 7 Stars, 0 Fork

快速制作 pyenv 环境镜像的工具

(`是也乎:`

国人作品, 在 CPyUG 列表反馈下, 24小时以内,兼容了 Python 2 ;-)

嗯哼,当然的,没有 M$ 的支持.
)


### 工作

....


# 是也乎

- 160415 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160414 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


