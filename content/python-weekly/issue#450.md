Title: pythonista-weekly : Pyw 450
Date: 2020-05-23 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-450

### 欢迎阅读《pythonista周刊》第450期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-450](https://mailchi.mp/pythonweekly/python-weekly-issue-450)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[来免费试用 14 天吧！](https://www.datadoghq.com/dg/apm/python-troubleshooting/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Troubleshooting)

###

### 文章、教程与话题

[OpenAI模型生成Python代码](https://www.youtube.com/watch?v=fZSFNUT6iY8) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（4min）

这非常棒，让你一瞥未来。

> 面向 NLP 编程（不是人，是机器！

[构建 FunctionTrace，一个图形化的 Python 分析器](https://hacks.mozilla.org/2020/05/building-functiontrace-a-graphical-python-profiler/)

这篇文章探讨了为什么我们构建 `FunctionTrace`,并分享了一些实现的技术细节。我们将展示像这样的工具如何针对 `Firefox Profiler` 这样的强大的开源可视化工具。想试试，你也可以做一个小 `demo`。



[防止 SQL 注入: Django ](https://blog.r2c.dev/2020/preventing-sql-injection-a-django-authors-perspective/)
在这篇文章中，`Jacob Kaplan-Moss` 分享了他关于防止 `SQL` 注入的想法。


[Tinder for Netflix Using Flask](https://www.youtube.com/watch?v=HZHOhf8EXXc) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（5min）
学习如何为 `Netflix` 制作一个 `'Tinder'`，你可以随意浏览推荐的电影，阅读细节，点击按钮就可以看 `Netflix`！

[配置你的 Flask 应用](https://t.co/2KMC8VbADn)
灵活安全配置 `Flask` 的最佳实践。轻松处理特定特定环境变量配置，并在将敏感信息分离出源码。


[Shopify Customer Service Chatbot using Python Automation](https://www.youtube.com/watch?v=xof1OgxcRhY) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（22min）
厌倦了糟糕的客户服务？你并不是一个人！这个视频介绍了如何使用 `Watson Assistant and Python Webhooks` 来提升你的 `Shopify` 客户服务游戏。 

[深度学习和 TebsorFlow 2 的快速介绍](https://builtin.com/machine-learning/introduction-deep-learning-tensorflow-20) 
`TensorFlow 2.0` 的手把手教程。


[RSVP for the ONLY Python Web Conference (Virtual) | June 17-19, 2020](https://pythonwebconference.com/) 
Experts discuss hard web production problems. 40+ talks on Django, Plone, CI/CD, Containers, Serverless, REST APIs, microservices, etc. Join JetBrains and Six Feet Up to discuss what the future holds. SPONSOR

[构建 serverless 托管平台](https://blog.vtemian.com/post/serverless-hosting-platform/)
这个项目的目的是建立一个系统，让我们在一个分支上进行推送，并将我们的修改部署在一个单独的环境中，给我们一个唯一的URL，来检查它们。类似于 `now.sh` 和 `heroku.com` 的做法。我们需要一个机制来打包我们的代码和依赖关系，并将其部署，但它还需要考虑到多个版本、升级、负载均衡、缩放和我们的有状态的部分（数据库）。


[构建和部署一个 Python Web 应用程序来自动化 Twitter](https://www.youtube.com/watch?v=yCYPzoG25ak) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（1h42min）
学习如何使用 `Flask，Heroku，Twitter API & Google Sheets API`构建一个 `tweet` 调度 `app`。

[通过构建互动游戏来教孩子 Python](https://opensource.com/article/20/5/python-games)
一个可以帮助任何人用一种简单有趣的方式——做游戏来开始学习 `Python` 的开源工具。


[使用 PYthon 制作一个 Markdown To HTML 转化中间件](https://florian-dahlitz.de/blog/build-a-markdown-to-html-conversion-pipeline-using-python)
使用 `Python` 将你的文章用 `markdown` 转成 `HTML`。


[用于 Python 和 Docker 的安全扫描器：从代码到依赖项的安全扫描器](https://pythonspeed.com/articles/docker-python-security-scan/)
你不希望在生产中部署不安全的代码--但是错误和漏洞很容易被漏掉。因此，您需要一些方法来自动捕捉到安全问题，而不需要考虑它。这就是安全扫描器的作用所在。它们不能解决你的所有问题---你仍然应该使用能够主动指出不安全的依赖关系的服务，比如说。但在你的构建或CI系统中设置一些自动检查来帮助捕捉问题是很好的。

[如何用 Python 自动化你的邮件](https://www.theseattledataguy.com/how-to-automate-your-emails-with-python/)
用 `Gmail API` 来发送抓取的数据到你的 `email`。

[JupyterDash 简介](https://t.co/RQ7rKKvO8B)
`JupyterDash`, 我们新的从 `Jupyter` 环境制作一个 `Dash apps` 的 `library`。这篇文章向你介绍 `JupyterDash` 的功能。

[60 个测试你的 Python List 知识的问题](https://t.co/ODe1wRyEdd)
通过掌握列表基础知识来解决算法问题。

[用 Python 实现 gRPC 服务](https://martinheinz.dev/blog/23)
现在，当人们想要实现后端 `API` 时，他们会直接使用使用 `JSON` 通信的 `RESTful API` 创建应用程序，甚至不考虑其他选项。近年来，`gRPC` 和它的 `protobufs` 开始得到一些牵引和普及，这要归功于它们的许多优势。那么，让我们来看看所有关于使用 `Python` 实现 `gRPC` 服务器的 `buzz/hype` 是什么!

[解密 Python 装饰器](https://rednafi.github.io/digressions/python/2020/05/13/python-decorators.html)
剖析 `Python` 中的装饰器。

[如何使用 Python 开始构建一个命令行 app](https://www.youtube.com/watch?v=JwwlRkLKj7o) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（20min）
学习使用 `scafolding` 制作一个命令行 `app`。然后为它创建一个存储库，创建一个 `PyPi` 页面，使用版本化，创建文档，最后像一个随机的没用过它的人一样运行它。

[如何设置成功的 Python 项目文档](https://t.co/YtAf382hTs)
使用 `Sphinx` 和“阅读文档”自动化你的文档创建工作流程。

[优化 Django ORM 查询](http://schegel.net/posts/optimizing-django-orm-queries/)

[Python的性能：不仅是解释器](http://blog.kevmod.com/2020/05/python-performance-its-not-just-the-interpreter/) 

[以每月5美元的价格构建类似于 Heroku 的基础架构](https://jakubsvehla.me/posts/infrastructure/)

[设置 Vim 以使用 Python 应用程序](https://blog.miguelgrinberg.com/post/video-setting-up-vim-to-work-with-python-applications) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)

[Django 的缓存和扩展](https://eralpbayraktar.com/blog/django/2020/caching-with-django)

[关于工具适合工作流程的想法](https://snarky.ca/thoughts-on-a-tooling-workflow/)

[在编写Django迁移时停止丢失数据!](https://blog.theodo.com/2020/05/django-migrations-without-losing-data/)

[Python 缓存整数](https://arpitbhayani.me/blogs/python-caches-integers)

[使用哈希表提高速度](https://blog.asrpo.com/hashtables)

### 有趣的项目、工具和库


[jupyter-book](https://github.com/executablebooks/jupyter-book)
`Jupyter Book` 是一个开放源代码工具，用于从计算材料中构建具有出版质量的书籍和文档。

[cocktail-pi](https://github.com/saubury/cocktail-pi)
`Raspberry Pi` 通过伺服安装的摄像头，根据推断你的心情来调鸡尾酒。

[Realtime_PyAudio_FFT](https://github.com/tr1pzz/Realtime_PyAudio_FFT)
在 `Python` 中进行实时音频分析，使用 `PyAudio` 和 `Numpy` 从流媒体音频中提取FFT特征并可视化。

[python-keyboard](https://github.com/makerdiary/python-keyboard)
一个由 `Python` 驱动的手写键盘。

[Promnesia](https://github.com/karlicoss/promnesia) 
`Promnesia` 是一款适用于 `Chrome/Firefox`（包括移动端）的浏览器扩展，它可以作为网络冲浪的副驾驶，增强您的浏览记录和网络探索体验。

[convtools](https://github.com/itechart-almakov/convtools/)
`convtools` 是一个 `Python` 库，用于声明性地定义从 `Python` 对象到 `Python` 对象的快速转换，包括处理集合和做复杂的聚合和合并。

[aitextgen](https://github.com/minimaxir/aitextgen)
一个强大的 `Python` 工具，使用 `GPT-2` 进行基于文本的AI训练和生成。

[popmon](https://github.com/ing-bank/popmon) 
`popmon` 是一个可以检查数据集稳定性的软件包。

[Quack](https://github.com/entynetproject/quack) 
`Quack Toolkit` 是一套提供拒绝服务攻击的工具。`Quack Toolkit` 包括短信攻击工具、HTTP攻击工具等多种攻击工具。

[Stormspotter](https://github.com/Azure/Stormspotter)
用于绘制 `Azure` 和 `Azure` 活动目录对象的 `Azure Red Team` 工具

[flowtron](https://github.com/NVIDIA/flowtron)
基于自动递归流的生成网络的文本到语音合成。

[chain-reaction-ai](https://github.com/shridharrhegde/chain-reaction-ai)
策略性棋牌游戏《链反应》的AI对手。

[tda_terminal_trader](https://github.com/casey7398/tda_terminal_trader)
命令行 `TD Ameritrade` 交易终端。

[Little Ball of Fur](https://github.com/benedekrozemberczki/LittleBallOfFur) 
`Little Ball of Fur` 是 `NetworkX` 的图形采样扩展库。

[gtg](https://github.com/getting-things-gnome/gtg)
`Getting Things GNOME! ((GTG)` 是 `GNOME` 桌面环境中的个人任务和 `TODO` 列表项目整理器，其灵感来源于 `Getting Things Done (GTD)` 方法论。`GTG` 在设计时考虑到了灵活性、适应性和易用性，因此它不仅仅是一个 `GTD` 软件。



### 最近更新

[Django 3.1 alpha 1 released](https://www.djangoproject.com/weblog/2020/may/14/django-31-alpha-1-released/)

[Python 3.9.0b1](https://www.python.org/downloads/release/python-390b1/)

### 那些活动

[Virtual: Scipy Japan 2020](https://www.scipyjapan.scipy.org/)
`SciPy Japan 2020` 将是一个虚拟会议，将把日本不断发展的 `SciPy` 社区聚集在一起，展示最新的项目，并向熟练的用户和开发者学习。

[Virtual: San Diego Python Meetup May 2020](https://www.meetup.com/pythonsd/events/gmxcqrybchblc/)
将会有以下话题

- 列表中的深拷贝和浅拷贝
- 在浏览器中可视化 `Sandiego` 的 `Covid19` 数据，而无需学习 `Javascript`
- 好莱坞中的 Python


[Virtual: NLP basics from text to vectors](https://www.meetup.com/PyData-Boston-Cambridge/events/270610949/)
在这个工作坊中，我们将涵盖以下内容 令牌化设计（使用 `SpaCy`），令牌/单词计数（使用 `scikit-learn`）和 `opic` 模型（ `scikit-learn` ）。我们将利用 `Google Collaboratory` 来运行代码，所以不需要安装任何东西！我们将使用 `Google Collaboratory` 来运行代码。

[Virtual: Deep Neural Networks Workshop](https://www.meetup.com/PyData-Manchester/events/270384347/)
`Marc` 将提供一些关于机器学习的工作原理、谷歌如何使用机器学习的背景，以及如何利用机器学习来解决现实世界的问题。然后，他将带领大家做一个实验室练习，重点讲解如何训练和执行深度神经网络。

[Virtual: PyData x PyYYC Meetup May 2020](https://www.meetup.com/PyData-Calgary/events/270635191/)
将会有几个演讲，概率先决条件和高性能IO。

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-450.html)
- 改进: [issue-450.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23450.md)

