Title: pythonista-weekly : Pyw 445
Date: 2020-04-18 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-445

### 欢迎阅读《pythonista周刊》第445期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-445](https://mailchi.mp/pythonweekly/python-weekly-issue-445)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[通过免费的Datadog APM试用版来提高应用程序性能。](https://www.datadoghq.com/dg/apm/ts-python-tracing/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Tshirt)



### 新鲜事

[PyCon US 2020 Online](https://us.pycon.org/2020/online/)

`PyCon US 2020` 已经在线上进行了。未来 4 周，我们将在网上发布内容，供大家观看。

> Bilibili 也有同步搬运哦
> [我在这里](https://space.bilibili.com/386835083/channel/detail?cid=120394)


### 文章、教程与话题

**[使用深度学习的 OpenCV 年龄检测](https://www.pyimagesearch.com/2020/04/13/opencv-age-detection-with-deep-learning/)**
在这篇教程中，你将学习到如何使用 `OpenCV, 深度学习, 以及 Python` 来实现自动检测/预测年龄。在教程的最后，你能够以相当高的准确度在静态图片文件以及实时视频流中自动预测年龄。


**[Python 中的 Hashing 和 Equality](https://eng.lyft.com/hashing-and-equality-in-python-2ea8c738fb9d)**
不要重写 `__hash__ and __eq__` 来强制让对象可哈希。使用不可变对象来代替。


**[部署任何 Python 项目到 Kubernetes](https://martinheinz.dev/blog/20) **
随着你的项目成长，变得很难只用单个的 `VM` 或者一些简单的 `SaaS` 来解决方案来进行处理。你可以切换到更强的解决方案，例如 `Kubernetes` 来解决这个问题。然而，如果你不熟悉它的概念或者之前也没使用过，那么对你来说可能就有点复杂。因此，为了帮助你——我们将介绍你开始需要的一切以及让你的 `Python` 项目部署在集群上——包括集群设置，所有的 `Kubernetes` 清单以及一些额外的自动化配置让你更轻松！



**[用 Virtual Private Networks 实现 Python Web Scraping ](https://tech.marksblogg.com/python-scraper-wireguard-vpn-ssh-proxy.html)**
使用 `VPNs` 或者其他的隧道技术，可以很大程度上让爬虫不被发现，并尽可能地高效收集数据。这都可以在 `Cloud` 或者私人环境中部署。这篇文章展示了两种方法，第一种是用了 `WireGuard`，第二种是用了一个 `OpenSSH SOCKS5` 代理。



**[N真的, Python's Pathlib 很棒](https://rednafi.github.io/digressions/python/2020/04/13/python-pathlib.html)**
沉浸在 `Python` 的面向对象的文件系统路径中。
>  我的代码已经全面使用 `pathlib` 了。 写起来真的很顺畅！

**[深入探讨 pyenv 是如何利用 Shim 设计模式实际工作的。](https://mungingdata.com/python/how-pyenv-works-shims/)**
这篇文章展示了 `pyenv` 是如何在底层使用 `shim` 设计模式、`.python-version` 文件以及环境变量工作的。


**[用图论从新闻中构建社交网络](https://t.co/jvh5JTyJaz) **
理解报纸中的社交连接。


**[Serving Models with Seldon](https://ruivieira.dev/serving-models-with-seldon.html)**
`Seldon` 是一个旨在为机器学习模型提供一个生成工作流，允许构建暴露定义良好的 `APIs` 的模型服务容器。在本文，我将展示如何创建一个简单的模型以及如何用 `Seldon` 进行部署。

**[Pandas equivalent of 10 useful SQL queries](https://t.co/CO87iqNx5A)**
本文向您展示了与一些最有用的 `SQL` 查询等价的 `pandas`。对于那些已经了解 `SQL` 的人来说，这既可以作为对 `pandas` 的介绍，也可以作为你可能需要的常见 `pandas` 操作的备忘单。


**[解构你的 Python 代码](https://florian-dahlitz.de/blog/disassemble-your-python-code)**
使用 `dis-module` 来深入了解你的 `Python` 代码。

**[操纵 Python AST 的历险记](https://eigenfoo.xyz/manipulating-python-asts/)**

我实验了通过操纵模型代码的 `Python` 抽象语法树 `(AST)` 来简化 `PyMC4` 的模型规范 `API` 的可能性。

**[Quick Domain-Specific Languages in Python with textX](https://tomassetti.me/quick-domain-specific-languages-in-python-with-textx/ )**
这篇教程向你展示了如何编写一个小的 `domain-specific` 语言和一个用于理解我们语言的 `Visual Studio Code` 语法高亮的插件

**[ XGBoost 简介以及 iOS 应用程序中的实现](https://heartbeat.fritz.ai/introduction-to-xgboost-with-an-implementation-in-an-ios-application-cdfaa8f9930b)**
使用 `coremltools` 训练并部署 `XGBoost` 模型，以及用 `Swift and Core ML` 构建一个体验设备

[开源虚拟背景](https://elder.dev/posts/open-source-virtual-background/)

[PyCaret 发布: 一个开源，low-code 的 Python 机器学习库](https://t.co/7h50TVhEA2)

[如何使用 Postman & Python 机器人 获得 Instacart Delivery 的自动提醒](https://raju.guide/index.php/2020/04/05/how-to-get-automated-alerts-on-instacart-delivery-availability-using-postman-python-bot/)

[CuPy 加速 NumPy on the GPU? Hold my Cider, here's Clojure!](https://dragan.rocks/articles/20/Clojure-Numpy-Cupy-CPU-GPU)

[Git worktrees and pyenv: 更快地开发 Python 库](https://huonw.github.io/blog/2020/04/worktrees-and-pyenv/) 

[Analyzing the Impact of Coronavirus on the Stock Market using Python, Google Sheets and Google Finance](http://adilmoujahid.com/posts/2020/04/stocks-analysis-covid19-coronavirus-python/)

[From chunking to parallelism: faster Pandas with Dask](https://pythonspeed.com/articles/faster-pandas-dask/) 

[Django QuerySet Examples (with SQL code included)](https://davit.tech/django-queryset-examples/)

### 有趣的项目、工具和库

**[avatarify](https://github.com/alievk/avatarify)**
Avatars for Zoom and Skype.

**[imgmaker](https://github.com/minimaxir/imgmaker)**
用 `easily-hackable` 模版以可编程的方式创建高质量图片。

**[pandemic-ventilator-2.0](https://github.com/Mascobot/pandemic-ventilator-2.0)**
Open Source Pandemic Ventilator with Raspberry Pi and Arduino.

**[Zoom-Meeting-and-Recording](https://github.com/BigchillRK/Zoom-Meeting-and-Recording)**
这个 `python` 脚本让你自动加入和记录一个 `zoom` 会议。


**[cookiecutter-django-vue-graphql-aws](https://github.com/grantmcconnaughey/cookiecutter-django-vue-graphql-aws)**
一个非常有主见的 `Cookiecutter` 模板，它将 `Django、Vue.js、GraphQL和AWS` 融合到一个全栈的 `Web` 应用程序中。

**[GitPlus](https://github.com/ReviewNB/jupyterlab-gitplus)**
`JupyterLab` 扩展，用于创建 `GitHub commits & pull requests`
>  自成开发生态不远了。

**[Userge](https://github.com/UsergeTeam/Userge)**
`Userge` 是一个用 `Python` 和 `Pyrogram` 实现的 `Powerful , Pluggable Telegram UserBot`。 

**[meta-blocks](https://github.com/alshedivat/meta-blocks)**
用于加速元学习研究的模块化工具箱。

**[SReC](https://github.com/caoscott/SReC)**
`PyTorch` 实现“通过超高分辨率实现无损图像压缩”



### 最近更新

[PyPy 7.3.1](https://morepypy.blogspot.com/2020/04/pypy-731-released.html)
>  37 来了！

### 那些活动

[Virtual: PyData Chicago Meetup April 2020](https://www.meetup.com/PyDataChi/events/269946286/)
There will be a talk, Cardinality estimation using HyperLogLog with intersection support and Dask parallel computation.

[Virtual: San Diego Python Meetup April 2020](https://www.meetup.com/pythonsd/events/gmxcqrybcgbfc/)
There will be a following talk, Snakes on a Car or Building a Self-Driving RC Car with Python.

[Virtual: PyData Miami / Machine Learning Meetup April 2020](https://www.meetup.com/Miami-Machine-Learning-Meetup/events/269908832/)
There will be a talk, Evaluation of Traditional and Novel Feature Selection Approaches.



#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  



----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-445.html)
- 改进: [issue-445.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23445.md)

