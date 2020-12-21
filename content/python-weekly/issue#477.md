Title: pythonista-weekly : Pyw 477
Date: 2020-12-03 16:25
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-477

### 欢迎阅读《pythonista周刊》第477期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-477](https://mailchi.mp/pythonweekly/python-weekly-issue-477)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
Seamlessly correlate logs and traces at the level of individual requests, allowing you to quickly troubleshoot your Python application. Datadog's Continuous Profiler allows you to find the most resource-consuming parts in your production code all the time, at any scale. [Try it today with a free trial.](https://www.datadoghq.com/dg/apm/ts/profiler/continuous-profiling-ts/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-ProfilingTshirt)

### 文章、教程与话题

[我是如何做一个自我引用的Tweet](https://oisinmoran.com/quinetweet)
或者说，`Twitter` 不希望你有编辑按钮的真正原因。

[Reed-Solomon error recovery in RAID-6](http://anadoxin.org/blog/error-recovery-in-raid6.html/)
这篇文章给你一个简单的例子，你可以根据 `RAID-6` 中使用的东西来创建自己的错误恢复解决方案。更具体的说，如果你需要在你的介质上提供冗余，这样就可以容忍1或2个介质的故障，不要再看了!)

[一个全面的Python程序剖析指南](https://t.co/57XvamGycf)
了解你的代码中哪些部分存在问题。

[3个有效的Django Async视图实例，无需睡眠](https://arunrocks.com/django-async-views-examples/)
学习如何通过绝妙的例子来使用 `Django Async Views`。

[如何使用Moto和Pytest测试你的AWS代码](https://www.learnaws.org/2020/12/01/test-aws-code/)
`AWS` 的 `Boto` 库通常用于将 `Python` 应用与各种 `AWS` 服务（如 `EC2、S3` 和 `SQS` 等）集成。然而，为这样的代码编写单元测试可能是复杂和混乱的。本文将向你展示如何使用 `Moto`，这是一个 `Python` 库，可以轻松模拟 `AWS` 服务，来测试我们的 `AWS` 代码。

[如何使用Python制作交互式Todo List CLI，并提供简单的登录机制](https://blog.cotter.app/how-to-make-an-interactive-todo-list-cli-using-python-with-an-easy-login-mechanism/)
使用 `Python` 构建你自己的 `Todo List CLI`，使用 `Click、PyInquirer` 和 `Cotter` 等包，在几分钟内就能完成。 

[Introducing datasette-ripgrep](https://simonwillison.net/2020/Nov/28/datasette-ripgrep/)
为你的源代码部署一个正则表达式搜索引擎。

[Introducing FARM Stack - FastAPI, React, and MongoDB](https://developer.mongodb.com/how-to/FARM-Stack-FastAPI-React-MongoDB)
`FARM` 协议栈在很多方面与 `MERN` 非常相似。我们保留了 `MongoDB` 和 `React`，但我们用 `Python` 和 `FastAPI` 替换了 `Node.js` 和 `Express` 后端。

[Build a Flask microservice with OpenFaaS](https://www.openfaas.com/blog/openfaas-flask/)
`Flask` 和 ` server-less Python` 函数哪个好？为什么不能同时拥有呢？

[用PyTorch实现char-rnn的一个尝试](https://jvns.ca/blog/2020/11/30/implement-char-rnn-in-pytorch/)

[Unravelling `not` in Python](https://snarky.ca/unravelling-not-in-python/)

[在Python中构建一个Pandoc过滤器，将CSV数据转化为格式化的表格](https://johnlekberg.com/blog/2020-11-27-cli-pandoc.html)

[编写iTerm2 Python脚本](https://cgamesplay.com/post/2020/11/25/iterm-plugins/)



### 有趣的项目、工具和库


[A Day in Code: Python](https://www.kickstarter.com/projects/914595512/a-day-in-code-python)
一个用 `Python` 编程语言编写的绘本故事。这非常适合孩子以及成人以有趣的方式学习 `Python`。

[Cyberbrain](https://github.com/laike9m/Cyberbrain)
重新定义`Python` 调试。

[ipycanvas](https://github.com/martinRenou/ipycanvas)
`Jupyter` 的交互式画布。

[marketools](https://github.com/AlbertRtk/marketools)
`marketools` 是一个 `Python` 包，用于网络抓取和分析股市数据。

[caer](https://github.com/jasmcaus/caer)
一个轻量级的计算机视觉库，用于高性能的人工智能研究。

[HTML2Image](https://github.com/vgalin/html2image)
作为现有网络浏览器的无头模式的封装器，从URL和HTML+CSS 字符串或文件中生成图像。

[SEC Filings App](https://gitlab.com/briancaffey/sec-filings-app)
一个由 `API` 和 `Web UI` 组成的 `Web` 应用，用于查看和分析 `SEC 13F` 申报数据。使用 `Django、Postgres、Redis、Django REST` 框架、`Celery、Quasar` 框架和其他技术。

[PolyFuzz](https://github.com/MaartenGr/PolyFuzz)
模糊字符串匹配、分组和评价。

[lux](https://github.com/lux-org/lux)
用于智能可视化数据发现的 `Python API`。

[illuminatio](https://github.com/inovex/illuminatio)
`kubernetes` 网络策略验证器。

[FioSynth](https://github.com/facebookincubator/FioSynth)
能够创建合成存储工作负载，自动执行和收集合成存储基准结果的工具。

[gallery-dl](https://github.com/mikf/gallery-dl)
命令行程序可以从多个图片托管网站下载图片库和图片集。

[inventory-hunter](https://github.com/EricJMarti/inventory-hunter)
Get notified as soon as your next CPU, GPU, or game console is in stock.

[TinyCheck](https://github.com/KasperskyLab/TinyCheck)
TinyCheck可以让你轻松地从智能手机或任何可以与Wi-Fi接入点相关联的设备上捕捉网络通信，并快速分析它们。这可以用来检查是否有任何可疑或恶意的通信从智能手机发出，通过使用启发式或特定的入侵指标（IoCs）。

[spylls](https://github.com/zverok/spylls)
纯 `Python` 拼写检查器，（几乎）完全移植了Hunspell。

### 最近更新

[pip 20.3](https://discuss.python.org/t/announcement-pip-20-3-release/5948)
这个版本的特点是默认启用了一个新的依赖解析器。当它接收到不兼容的指令时，会更加严格和一致，并且减少了对某些类型约束文件的支持，因此一些变通方法和工作流可能会被破坏。你可以在 [changelog](https://pip.pypa.io/en/stable/news/) 中找到更多细节（包括废弃和删除）。

[PyCharm 2020.3](https://blog.jetbrains.com/pycharm/2020/12/pycharm-2020-3-overview/)
`PyCharm` 2020.3正式发布了! 2020的最后一个重要版本，主要是让广大用户体验和培训流程变得更好。

[Python 3.9.1rc1](https://www.python.org/downloads/release/python-391rc1/)
`Python 3.9.1rc1` 是 `Python` 的最新主要版本，它包含了许多新的特性和优化。

### 新活动

[Virtual: Pyjamas Conf 2020](https://pyjamas.live/)
 `24` 小时流媒体播放关于 `Python` 的讲座，并连接世界各地的 `Python` 社区，你可以在家里访问。

[Virtual: Austin Python Meetup December 2020](https://www.meetup.com/austinpython/events/lgrbmqybcqbmb/)
将会有以下话题:

- Patent Analytics, There And Back Again
- Who "owns" what parts of your code, how much trouble can it get you into, and how can it make you money?


[Virtual: London Python Meetup December 2020](https://www.meetup.com/LondonPython/events/274784720/)
将会有以下话题:

- 通用 `Python` 效率最佳实践
- For, what is it good for? 


[Virtual: SF Python Meetup December 2020](https://www.meetup.com/sfpython/events/qlcnxrybcqbmb/)

[Virtual: Build an advanced answering machine using Flask and 46elks](https://www.meetup.com/PyLadiesStockholm/events/274883334/)

[Virtual: PyMNtos Python Presentation Night #90](https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/events/274769404/)
 



Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-477.html)
- 改进: [issue-477.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23477.md)

