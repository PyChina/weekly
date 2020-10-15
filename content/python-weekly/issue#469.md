Title: pythonista-weekly : Pyw 469
Date: 2020-10-08 16:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-469

### 欢迎阅读《pythonista周刊》第469期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-469](https://mailchi.mp/pythonweekly/python-weekly-issue-469)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[今天免费试用](https://www.datadoghq.com/dg/apm/python-performance-monitoring/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Newsletter)[.](https://www.datadoghq.com/dg/apm/python-performance-monitoring/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Newsletter)

### 新闻

[阿斯利康利用PyTorch驱动的算法发现新药](https://www.zdnet.com/article/astrazeneca-is-using-pytorch-powered-algorithms-to-discover-new-drugs/)
这家制药公司透露了它是如何使用复杂的机器学习工具来加速药物发现的。

[Python Web Conf 2021 Call for Proposals](https://www.papercall.io/pwc-2021)
The 3rd Annual Python Web Conference will be fully virtual and the audience will range from beginner to expert level attendees. The call for proposals is now open and they are looking for a wide variety of talk levels and subjects.

### 文章、教程与话题

[用Streamlit和Python构建一个实时语音传输应用](https://www.youtube.com/watch?v=4qzAjOJ0Td4) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（30min）
最近的研究引入了一个深度学习框架，允许从几秒钟的音频中创建一个语音的数字表示，并使用它来调节一个经过训练的文本到语音模型，以泛化到新的声音。本讲座介绍了如何使用预先训练好的模型，将一个复杂的深度学习过程用于克隆训练过程中未见过的声音，并将其轻松转换为 `Streamlit` 应用。

[What’s New In Python 3.9](https://docs.python.org/release/3.9.0/whatsnew/3.9.html)
本文介绍了与 `3.8` 相比，`Python 3.9` 的新功能。

[用新的Nvidia Jetson Nano 2GB和Python构建一个60美元的人脸识别系统](https://t.co/Bxjpf12LF3)
使用 `Python 3.6、OpenCV、Dlib` 和 `face_recognition` 模块。

[Embedding Python in Go](https://poweruser.blog/embedding-python-in-go-338c0399f3d5)
学习如何使用 `Python C API` 从 `Golang` 代码中调用 `Python` 代码。

[Python deque implementation](http://www.laurentluce.com/posts/python-deque-implementation/)
`Python deque` 是一个双端队列。你可以向两端追加和从两端弹出。这些操作的复杂度会摊到恒定的时间。这篇文章解释了 `Python 3` 内部对 `deque` 的实现。它使用了一个 `64` 个指向对象的链接列表块。这减少了内存开销，因为上一个和下一个链接较少。

[使用Python创建漂亮的架构图](https://t.co/pLuwSpAvyV)
不要再花时间手动调整错位的箭头了。

[Minimum-Effort Transpiler](https://t.co/YqeJ3xLNsX)
用半天时间写出一门合格的程序设计语言。

[不要直接编写命令行接口](https://arogozhnikov.github.io/2020/10/01/dont-write-cli.html)
如果要写的话，又该怎么写呢？

[Python上下文管理器的魔力](https://t.co/5yK4eUbGEY)
使用和创建超棒的 `Python` 上下文管理器的秘诀，这将使你的代码更易读、更可靠、更不容易出错。

[带有Flask和Python的总统候选人投票仪表板教程](https://blog.thecodex.me/polling-dashboard-python/)
用 `BeautifulSoup` 构建一个美国总统民调仪表盘，它可以从 `FiveThirtyEight` 中收集最新的民调，并在 `Flask` 仪表盘中呈现数据

[Hijack To Help Customers](https://www.mattlayman.com/blog/2020/hijack-to-help-customers/)
当客户报告最棘手的问题而你的所有诊断工具都使你失败时，你将如何帮助你？ 在本文中，我们探索了适用于 `Django` 应用程序的技术和工具，可帮助你快速投入并节省时间。

[Lyft 如何使用 PyTorch 为其自动驾驶汽车提供机器学习的动力](https://medium.com/pytorch/how-lyft-uses-pytorch-to-power-machine-learning-for-their-self-driving-cars-80642bc2d0ae)

[Django Day Copenhagen 2020 Videos](https://www.youtube.com/playlist?list=PLEpW1LzVyQWhqb_OoWtURF5cfKSGof0It)

[Creating Games in Streamlit](https://joelgrus.com/2020/10/02/creating-games-in-streamlit/)

[展开丰富的比较运算符](https://snarky.ca/unravelling-rich-comparison-operators/)

[用Python解决平衡指数问题](https://johnlekberg.com/blog/2020-10-03-equilibrium-index.html)

### 有趣的项目、工具和库

[Human-First AI](https://github.com/h1st-ai/h1st)
`Human-First AI` 解决了工业人工智能的 "冷启动 "问题：将人类的专业知识进行编码，以补充数据的不足，同时基于松下打造人工智能解决方案的经验，对接强大的ML：robotics predictive maintenance, cold-chain energy optimization, Gigafactory battery mfg, avionics, automotive cybersecurity, and more.

[GHunt](https://github.com/mxrch/ghunt) 
`GHunt` 是一个 `OSINT` 工具，可以通过电子邮件从任何谷歌账户中提取信息。

[GDBFrontend](https://github.com/rohanrhu/gdb-frontend) 
一个简单、灵活、可扩展的 `GUI` 调试器。

[Archai](https://github.com/microsoft/archai) 
`Archai` 是一个神经网络搜索（NAS）的平台，你可以你为你的应用生成高效的深度网络。

[igel](https://github.com/nidhaloff/igel)
一个机器学习工具，可以在不编写代码的情况下训练、测试和使用模型。

[GenForce](https://github.com/genforce/genforce)
用于深度生成式建模的高效 `PyTorch` 库（StyleGANv1v2、PGGAN等）。

[rotate](https://github.com/rvizzz/rotate)
创建递归的图片旋转动画。

[3270font](https://github.com/rbanffy/3270font)
A 3270 font in a modern format.

[Spotify-Playlist-Generator1](https://github.com/AcrobaticPanicc/Spotify-Playlist-Generator1)
`Flask` 网络应用，用于根据选定的曲目和个人偏好创建 `Spotify` 播放列表。

[AcurusTrack](https://github.com/AIHunters/AcurusTrack)
`AcurusTrack` 是一个高度可预测的多对象跟踪器。它是基于一个自定义的数据关联方法。

[NERVE](https://github.com/PaytmLabs/nerve) 
Network Exploitation, Reconnaissance & Vulnerability Engine.

[pyinspect](https://github.com/FedeClaudi/pyinspect)
Find functions when you can't remember their name.

### 最近更新

[Python 3.9.0](https://www.python.org/downloads/release/python-390/)
`Python 3.9.0` 是 `Python` 最新的主要版本，它包含了许多新的功能和优化。

[Django bugfix release: 3.1.2](https://www.djangoproject.com/weblog/2020/oct/01/django-bugfix-release-312/)

### 新活动

[Virtual: San Francisco Python Meetup October 2020](https://www.meetup.com/sfpython/events/xkwxvqybcnbsb/)
将会有以下话题:

- 用 `pytest` 解读 `Flask` 的应用和请求上下文。 
- 使用 `AWS` 的开放数据集和 `Chalice` 构建第一个 `REST API`。
- 测试使用 `Amazon S3` 的 `Python` 代码的策略


[Virtual: Austin Python Meetup October 2020](https://www.meetup.com/austinpython/events/lgrbmqybcnbsb/)
将会有以下的话题

- 用于 `Ethereum` 区块链的 `Python`
- Hummingbot for crypto trading


[Virtual: Instrumenting your Python applications with Prometheus](https://www.meetup.com/PyLadies-Berlin/events/273248890/)
学习如何从你的代码中导出监控指标，并在 `Prometheus` 中捕获它。我们将以一个简单的网络应用为基础，使用 `Python` 客户端 `API` 来跟踪代码中的事件，同时介绍应用监控的基本原理和 `Prometheus` 数据获取模型。你将学习如何在自己的应用程序中添加监控，以及如何查询和解释所产生的数据。作为奖励，我们还将向你介绍如何利用你的数据构建`grafana` 仪表盘。

[Virtual: pandas and friends](https://www.meetup.com/PyDataNYC/events/273620753/)
在本次演讲中，`Marc Garcia` 将快速概述生态系统，分析这些系统的不同组件，并讨论未来的数据框架生态系统可能是什么样子。

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-469.html)
- 改进: [issue-469.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23469.md)

