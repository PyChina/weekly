Title: 蠎加载 75
Slug: importpython-75
Date: 2016-06-04 21:12
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 75](http://importpython.com/newsletter/no/75/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [Pycon US 2016 视频和演讲幻灯](https://www.youtube.com/channel/UCwTD5zJbsQGJN75MwbykYNw/videos)
    + pycon, video

PyCon is the largest annual gathering for the community using and developing the open-source Python programming language. PyCon is organised by the Python community for the community. Currently underway in Portland and will conclude on 5th June. The talks from the conference are getting uploaded as we speak. You should glance the videos by title and see which one you like. Speaker's slides will be published here soon https://speakerdeck.com/pycon2016

(`是也乎:`

PyCon15US 的相关兴趣议题的视频30+G 在硬盘中还没有看过一遍,
又来一大波...虽然发布在不存在的网站中...感觉世界总是在持续的碾压着自己...

必须首先复习: [Guido van Rossum - Python Language - PyCon 2016](https://www.youtube.com/watch?v=YgtL4S7Hrwo) 明确 Py2 何时正式放弃...

应该去大学, 碾压一下当下心态良好的小白们了...
)

- [PyCon 2016: Machete-mode 调试 来自 Ned Batchelder - coverage.py 创造者](http://nedbatchelder.com/text/machete.html)
    + pycon, debugging

Python is simpler and more fluid than other languages. Sometimes you want this fluidity, but usually you don't. Dynamic typing means that names may have values you don't expect. Where other languages offer access control over the internals of objects, Python lets you examine and change anything. All of your program's data is on the heap, and can be used throughout your program. All of this flexibility can be a powerful tool, but sometimes, things go wrong. The flexibility comes back to bite us, and causes problems that we have to debug.

(`是也乎:`

Python 是如此简洁又灵活,以致有时爱到不行,有时又恨到不行,
特别是在调试时...
)

- [关注 Pycon 议题在 twitter #pycon2016](https://twitter.com/search?q=%23pycon2016)
    + pyconus, twitter

Takes you to the top tweets on pycon.

- [Python & Django 安全在 Shoestring: 资源](http://nerd.kelseyinnis.com/blog/2016/05/30/python-django-security-on-a-shoestring-resources/)
    + django, security

Callisto is an online reporting system. It's written in Django and provides a more empowering, transparent, and confidential reporting experience for survivors. It's absolutely essential that we keep our users' data secure Thankfully, although the infosec community can sometimes be intimidating, any one of us can learn how to build secure sites using Python. This talk covers the essential concepts behind securing your users' data and offer examples of how we applied them to Callisto.

(`是也乎:`

大圣们曰过:"计算机系统无非两种结局,简单的看不出明显的错误,复杂的没有明显的错误;-("
)

- [Oneliner-izer:约束编码练习 by Chelsea Voss](https://www.youtube.com/watch?v=DsUxuz_Rt8g)
    + pyconus

Curator's note - In every office you have that one guy who tries to accomplish a whole lot of things on one line. This is a talk that you want to show them. Ideas and implementation behind Oneliner-izer, a ""compiler"" which can convert most Python 2 programs into one line of code. As we discuss how to construct each language feature within this unorthodox constraint, we'll explore the boundaries of what Python permits and encounter some gems of functional programming – lambda calculus, continuations, and the Y combinator.

(`是也乎`:

又一基础轮子的再造练习,涉及一些函式语言的精华:
演算/连续/Y组合...
)



- [pep8 再次重命名为 "pycodestyle"](https://github.com/PyCQA/pycodestyle)
    + code quality

Simple Python style checker in one Python file. Good bye PEP8 :)

(`是也乎:`

名字起的好,项目活的了,
创始胡子长,项目久的了....

对于 `EPE8` 这么经典的名称的放弃,也是老拥趸弃疗的开始...
)


- [Python 201: importlib 简介](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/AvJLWvHLnvM/)
    + core python

Python 将 importlib 作为内建模块包含在发行版本中,
目的就是提供导入语句 (函式 `__import__()`).
从而赋予程序猿在导入过程中使用自定对象的能力,
(类似  importer)

(`是也乎:`

米国大学课程编号,`101`一般都是入门课,`201`就是中级课了...
)

- [JSON 格式日志 (Python)](http://code.activestate.com/recipes/580667-json-formatted-logging/)
    + code snippet

I have created a package that outputs JSON formatted lines to a log file. It can make use of the standard logging parameters and/or take custom input. The use of JSON in the log file allows for easy filtering and processing.



- [Episode 59 - Pillow 和 Alex Clark](http://podcastinit.podbean.com/e/episode-59-pillow-with-alex-clark/)
    + podcast

If you need to work with images the Pillow is the library to use. The Python Image Libary (PIL) has long been the gold standard for resizing, analyzing, and processing pictures in Python. Pillow is the modern fork that is bringing the PIL into the future so that we can all continue to use it moving forward. This week I spoke with Alex Clark about what first led him to fork the project and his experience maintaining it, including the migration to Python 3.

(`是也乎:`

对 PIL 的历史接替人: `Pillow` 的创造者的访谈..
)

- ["通过实例学习 Python 2 标准库" #PyCon2016 期间超5折优惠!](http://feedproxy.google.com/~r/DougHellmann/~3/BhbFMmVgHNk/)

The Python Standard Library by Example (for Python 2) is the eBook deal of the day during PyCon 2016. Visit theinformit.com/deals to order your DRM-free copy (PDF, ePub, andMobi) for $19.99 today! *Offer ends 11:59 PST June 1, 2016

- [Django Community Jobs Section | Django](https://www.djangoproject.com/community/jobs/)
    + job market

In case you weren't aware, django website has a job section.

- [Django REST 框架已经接受追加基金](https://fund.django-rest-framework.org/topics/funding/)
    + community

If you use REST framework commercially we strongly encourage you to invest in its continued development by signing up for a paid plan. Tom Christie the creator of DRF is looking to raise funds and work on it full time. Support him.

- [Jessica mckellar 为 PyCon 带来更多的程序媛.](https://twitter.com/jessicamckellar/status/737299461563502595)
    + pyconus

As many of you know we have been featuring interview of django girls from a long time now. It's very important to encourage and aid women participation. Python and Django community is at the forefront. 

(`是也乎:`

所谓`一妞扺十汉` 海外技术社区也异常认同,
特别是 DjangoGirls 如此成功,以至 老爹也主动开始站台推荐了...
)

## 活动
~ Upcoming Conference / User Group Meet

- [GeoPython 2016](http://www.geopython.net/)
- [PyCon Singapore 2016](https://pycon.sg/)
- [EuroPython 2016](http://ep2016.europython.eu/)
- [PyOhio 2016](http://pyohio.org/)
- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [EuroScipy 2016](https://www.euroscipy.org/2016)

## 项目
~ 包/模块/库/片段...


- [dockerize-me](https://github.com/fiunchinho/dockerize-me)
    - 104 Stars, 10 Fork

嗯哼, 对 Dockerize 的 Dockerfile 自动已经优化的工具,
即, Dockerfile 也同 SQL/C++ 类似,
已经高速积累起来了很多固化的优化模式...


- [ipyida](https://github.com/eset/ipyida)
    - 85 Stars, 8 Fork

IPython console integration for IDA Pro

- [Parsley](https://github.com/buckyroberts/Parsley)
    - 55 Stars, 4 Fork

处理 HTML 为 JSON.

(`是也乎:`

嗯哼?! 目测浏览器应该可以内置 JSON->HTML 的渲染器了吧...
这样 `SEOP` ~ 面向搜索引擎的页面,应该可以有了...
)

- [cursed](https://github.com/johannestaas/cursed)
    - 49 Stars, 2 Fork

Simplified curses interface with concurrency, for quick and sane curses apps. Allows easy creation of windows and menus. Code for each window runs concurrently.

(`是也乎:`

CLI 应用难以消亡...
)


- [ntm-one-shot](https://github.com/tristandeleu/ntm-one-shot)
    - 37 Stars, 9 Fork

One-shot Learning with Memory-Augmented Neural Networks

- [notebooks](https://github.com/fluentpython/notebooks)
    - 15 Stars, 2 Fork

Jupyter Notebooks with Fluent Python examples.

- [monopoly_simulator](https://github.com/ohjuny/monopoly_simulator)
    - 13 Stars, 1 Fork

A few days ago, I was playing Monopoly with my friends and found myself often asking the question, "What are the odds of me going there?". So I decided to find out.

(`是也乎:`

用数据科学的思路来玩 `大富豪`
)

- [ansible-python-lambda](https://github.com/YPlan/ansible-python-lambda)
    - 7 Stars, 0 Fork

Example deployment of AWS Lambda functions with Ansible

(`是也乎:`

希望不是 AWS 的软文,去年使用 lambda 时,那叫个酸爽...
)

## DAMA 无责任推荐

- [Pyston 0.5 released | The Pyston Blog](https://blog.pyston.org/2016/05/25/pyston-0-5-released/)

欢迎订阅 [python-cn(华蟒用户组,CPyUG 邮件列表) - Google 网上论坛](https://groups.google.com/forum/#!forum/python-cn) 和 Pyston 开发者直接沟通,嗯哼 ;-)

- [混乱的 Python Tyrant's Technology](http://t.cn/RUieq1O)
- [Python 模块在全局作用域里应避免任何产生副作用的语句 Tyrant's Technology](http://t.cn/RGxdl9n)


~ 嗯哼, 继续来自自荐的 [御宅暴君](http://acgtyrant.com/) 同学 ;-)


# 是也乎

- 160604 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160604 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


