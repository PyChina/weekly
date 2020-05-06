Title: pythonista-weekly : Pyw 447
Date: 2020-05-02 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-447

### 欢迎阅读《pythonista周刊》第447期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-447](https://mailchi.mp/pythonweekly/python-weekly-issue-447)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**

[python开发者都需要的Vettery](https://www.vettery.com/tech?utm_source=newsletter&utm_medium=pythonweekly&utm_term=tech&utm_content=grouped&utm_campaign=ad-77579)  
Vettery是一个招聘网站，它改变了人们应聘或者雇佣的方式。准备好换工作地方了吗？免费制作简历，你的薪资你说了算，现在就和顶级雇主的HR联系吧！

### 新鲜事

[为 Steering Council Q&A 收集问题](https://discuss.python.org/t/collecting-questions-for-a-steering-council-q-a/4010)
作为 `PyCon US 2020` 的一部分，他们计划与 `Steering Council` 进行 `Q&A` 记录。如果你有任何问题，请务必提交它们。

### 文章、教程与话题


[TCP Reset Attack 是如何做的？](https://robertheaton.com/2020/04/27/how-does-a-tcp-reset-attack-work/)
`TCP` 重置攻击是使用不超过几字节大小的单个数据包进行的。一个由攻击者精心制作并发送的欺骗 `TCP` 段，欺骗两个受害者放弃 `TCP` 连接，中断了它们之间可能重要的通信。在这篇文章中：将学习到 `TCP` 协议的基础知识，学习攻击原理，并使用一个简单的 `Python` 脚本来攻击我们自己。

[More Python for Beginners](https://www.youtube.com/playlist?list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
来自 `Microsoft` 的另一种 `Python` 教程。

[在 `Rust` 代码中编写 Python 代码 — Part 2](https://blog.m-ou.se/writing-python-inside-rust-2/)
在这章中，我们将扩展我们的 `python!{}-macro` ，让其能够在 `Python` 代码中无缝使用 `Rust` 变量。我们构思了几种方式，并实现了两种。

[Hacking Together an E-ink Dashboard](https://healeycodes.com/hacking-together-an-e-ink-dashboard/)
一个树莓派仪表盘原型，省得我和智能助手说话。

[Talko: 一个端到端的聊天应用](https://t.co/WLdF2Cmcnr)
如何不用任何库或者框架构建一个完整的聊天应用。

[Python 3.9 中你应该知道的新特性](https://martinheinz.dev/blog/21) 
`Python 3.9 Beat` 就将发布了，所以是时候来看看将要推出的功能了，比如新的字典操作，新的 `functools` 以及其他～

[在 Python 应用中配置使用的最佳实践](https://tech.preferred.jp/en/blog/working-with-configuration-in-python/)
许多计算机应用可以被配置成某种的行为方式，不论是通过命令行标志，环境变量或者是配置文件。对你来说，作为一个软件开发者，处理并配置会遇到一些挑战，比如解析不可信的输入，验证输入以及在程序的各层中访问它。用 `Python` 作为一个例子，这篇文章分享了一些最佳实践，来帮助你安全并高效的处理配置。

[简易 Django 部署 : 指南](https://mattsegal.dev/simple-django-deployment.html)
如何用很多小步骤部署 `Django`。

[如何用 Django and GraphQL 创建一个 URL 缩短器](https://www.digitalocean.com/community/tutorials/how-to-create-a-url-shortener-with-django-and-graphql)
在这篇指南中，你将创建一个 `URL 缩短器` 的后台 —— 可以将接受任何 `URL` 并生成一个更短的 `URL` 的服务，更加可读的版本 —— 同时介绍了一些 `GraphQL` 的概念，例如 `queries and mutations`，以及工具，例如 `GraphiQL` 接口。

[Python 中从零开始的深度神经网络](https://www.youtube.com/watch?v=b_w4eEiogaE) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
确保一个灵活的神经网络架构 `API` 并不太难。但是，我们需要注意的是，为了方便用户的工作，我们要把抽象的层层设为简单的拟合和预测。这里我们利用以下三个概念。网络、层和神经元。这三个部分将共同组成一个完全连接的前馈神经网络神经网络。

[使用 Google Sheets, S3, and Python 来快速构建一个网站](https://t.co/kvkzPGbkeV)
非 `web` 开发者的生存指南。

[Generators, Iterables, Iterators in Python: 何时何处](https://www.pythonforthelab.com/blog/generators-iterables-iterators-python-when-and-where/)
学习如何扩展你的代码，使你的代码能够很容易地在类的元素中循环，或者快速生成数据。


[GraphQL Tutorial with Django (Python) and Excel](https://www.youtube.com/watch?v=nPQE5B51DQ8) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（37min）
在这个 `Django，Excel and GraphQL` 指南中学习如何用 `Django` 构建一个 `GraphQL 客户端和服务器` 并支持 `excel` 数据。我们将会从零开始搭建所有东西。

[41 问题，测试  Python Strings 知识](https://t.co/HkQ4FbffhD)
如何通过掌握字符串基础知识来粉碎算法题。

[Django 中创建交互视图](https://hackersandslackers.com/creating-django-views/) 
通过编写 `Django` 视图来处理动态内容、提交表单以及与数据交互，创建交互式用户体验。

[用 Flask-Monitoring-Dashboard 自动监控你的Flask Web Application ](https://t.co/mUQTNhMNaG)
一篇如何使用并设置一个简单的 `Flask` 应用，并使用 `Flask-Monitoring-Dashboard` 来监控这个系统。 它将展示自动监控您的网络服务是多么简单，并解释 `Flask-Monitoring-Dashboard` 提供的一些功能。

[在 Python 中处理警告 (或者说: 什么时候异常不是异常？)](https://lerner.co.il/2020/04/27/working-with-warnings-in-python/)
`Python` 的警告和异常有什么不同？学习如何发出以及过滤警告，另外为什么要这样做。

[从零开始半小时构建一个仪表盘!](https://www.youtube.com/watch?v=SnzwO4vEkJE) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
如何完全从零开始在半小时内构件内部交易仪表盘。

[PyTorch Distributed Training](https://leimao.github.io/blog/PyTorch-Distributed-Training/)

本帖介绍了一个简单的 `PyTorch` 分布式训练在 `CIFAR-10` 分类上使用 `DistributedDataParallel` 包裹的 `ResNet` 模型的简单实现。此外，还将介绍 `Docker` 容器在分布式训练中的使用方法，以及如何使用 `torch.distributed.remotion` 启动分布式训练。

[用 Python 制作你自己的 Diff-Tool ](https://florian-dahlitz.de/blog/create-your-own-diff-tool-using-python)
在这篇文章中，你会学习到如何只用 `Python` 创建你自己的 `diff-tool`。

[用 Alpaca 编一个 Python Stock Trading bot](https://www.youtube.com/watch?v=9R7pCh4yCm8) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（20min）

[Oops! 在 Docker 中删除 Django 项目中的隐私](https://startcodingnow.com/removing-secrets-from-django-project-in-docker)

[Introducing django-gsheets, an easy way to sync to and from Google Sheets](https://labs.meanpug.com/sync-data-to-and-from-google-sheets-with-django-gsheets)

[Jupyter Notebook 最佳实践](https://levelup.gitconnected.com/jupyter-notebook-best-practices-fc326eb5cd22)



### 书籍

[Springer releases 50 Programming books for free](https://link.springer.com/search/page/1?facet-discipline="Computer+Science"&package=mat-covid19_textbooks&facet-language="En"&facet-content-type="Book")
它包括 `Python`、机器学习、深度学习、AI 等方面的书籍。

### 有趣的项目、工具和库

[Shynet](https://github.com/milesmcc/shynet)
现代，隐私友好及详细的网络分析，不需要 `cookies or JS` 就能工作。

[Jina](https://github.com/jina-ai/jina) 
`Jina` 是由最先进的 AI 和深度学习驱动的云原生神经搜索框架。

[pivotnacci](https://github.com/blackarrowsec/pivotnacci)

通过 `HTTP` 代理进行 `socks` 连接的工具。



[ESPnet](https://github.com/espnet/espnet)
End-to-End Speech Processing Toolkit.

[Printy](https://github.com/edraobdu/printy)

`Printy` 是一个轻量级的跨平台库，它扩展了内置函数 `print()` 和 `input()` 的功能。`Printy` 以其简单、易用的特点而闻名，它可以让您通过一个直观友好的基于 `flags`的 `API` 为您的文本着色和应用一些标准格式。

[RepoPeek](https://github.com/sameera-madushan/RepoPeek)

在克隆一个存储库之前，通过 `Python` 脚本来获取关于存储库的详细信息。

[shhh](https://github.com/smallwat3r/shhh)

不要在电子邮件或聊天记录中泄露秘密，使用带有密码和到期日期的安全链接来分享。

[drf-starter-template](https://github.com/nishantwrp/drf-starter-template)

一个简单易用的项目模板，用于使用 `Django Rest Framework` 的小型项目。

[StockInsider](https://github.com/charlesdong1991/StockInsider)

一个用来收集、分析以及可视化股票交易指标的 `Python` 工具。

[gitland](https://github.com/programical/gitland)

用 `GitHub` 控制的多人游戏。

[django-sockpuppet](https://github.com/jonathan-s/django-sockpuppet)

使用你已经熟悉和喜爱的django工具，构建反应式应用程序。

[BentoML](https://github.com/bentoml/BentoML) 

`BentoML` 是一个用于高性能 `ML` 模型服务的开源平台。

[Taichi](https://github.com/taichi-dev/taichi) 

面向可移植、高性能、稀疏和可区分计算的高效编程语言。

[PyDP](https://github.com/OpenMined/PyDP) 

`PyDP` 是 `Google's Differential Privacy` 项目的 `Python` 封装器。该库提供了一套 `e-differential private` 算法，可用于生成包含私有或敏感信息的数字数据集的聚合统计数据。

[postgres_restorer](https://github.com/pyux/postgres_restorer)
用于在集成测试期间恢复数据库的简单工具。

### 最近更新

[Python 3.9.0a6](https://mail.python.org/archives/list/python-committers@python.org/message/JJWIXYICQHCEFCJCCXVSWTP5O67UVCQC/)

### 那些活动

[Webinar: Learn Scraping with Python and Poshmark](https://my.demio.com/ref/jjUDGs9tqIYdFYiS)
在本次讲座中，我们将学习如何使用网页抓取来提取关于 `Poshmark` 列表的信息。然后，我们将使用 `Python` 库来分析和可视化数据。

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-447.html)
- 改进: [issue-447.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23447.md)

