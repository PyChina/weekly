Title: pythonista-weekly : Pyw 436
Date: 2020-02-15 10:26
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-436

### 欢迎阅读《pythonista周刊》第436期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-436](https://mailchi.mp/pythonweekly/python-weekly-issue-436)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**

使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[马上跟踪你的python应用吧！免费试用14天哦！](


## 文章、教程与话题

**[使用Flask处理每秒65,000多个请求的峰值，同时管理英国10％的小学](https://runninginproduction.com/podcast/10-scholarpack-runs-10-percent-of-the-uks-primary-schools-and-gets-huge-traffic)**

在本期的`Running of Production`,`Gareth Thomas`介绍了一个帮助管理`3.5百万`以上学生的平台。有超过`1,500`台数据库，其峰值超过了`65k`每秒请求。一个遗留的`Zope`服务以及一系列`Flask`微服务均在`AWS Fargate`上提供服务。

> 并发成长之旅。

**[魔法:Klaviyo使用的常量时间的技巧，用于大规模操作](https://t.co/l5c5QlApa5)**

`Klaviyo`的数据存储和处理需求巨大，并且随着时间会快速增长。然而，我们的外部最终用户和内部服务消费者并不关心我们的数据大小，仍然需要对他们的查询做出快速响应。为了让我们的系统更加流畅，我们偶尔不得不使用各种非常规的优化技术。本文中提到的特定技术是获取通常是线性的甚至更复杂的操作并使它们保持恒定时间的方法。

> 实践中的各种骚操作

**[用Python编程时你做错的5件事](https://www.youtube.com/watch?v=fMRzuwlqfzs) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(12min)**

`Python`是一个很棒的语言，但是我已经看到许多新手犯了一些非常基本的错误，在这个视频中，我展示了其中的5个错误，它们会引起巨大的痛苦并让人头痛。我将介绍这些错误、它们的现象以及如何改正它们。



**[Cloudburst:Function-as-a-Service (FaaS)](https://arxiv.org/pdf/2001.04592.pdf)**

`Function-as-a-Service (FaaS)`平台和`“serverless”`云计算正变得越来越流行。当前的`FaaS`产品主要针对无状态的功能，这些功能只进行最少的`I/O`和通信。我们认为，无服务器计算的好处可以扩展到更广泛的应用程序和算法。本文介绍了`Cloudburst`的设计和实现，`Cloudburst`是一个有状态的`FaaS`平台，它提供熟悉的`Python`编程，具有低延迟的可变状态和通信，同时保持`serverless`计算的自动调优优势。

> 有时也是省钱的好帮手

**[了解Django中的Group by和SQL](https://hakibenita.com/django-group-by-sql)**

通过比较查询集和`SQL`来了解`Django ORM`中的`GROUP BY`。如果你最熟悉`SQL`，那么这就是`Django GROUP BY`教程。

**[如何在Python中编写一个Redis客户端，从零开始](https://youtu.be/C5KkQUKhc_4?t=325)** ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(1h)

你曾经有没有想过为`Redis`编写一个客户端是多难？在这次探讨中，`Loris Cro`将会向你展示如何使用`Netcat(or telnet)`检查`RESP (Redis Serialization Protocol)`  。然后，他将使用这些信息来编写实现`SET`和`GET`命令的基本`Python`客户端。

> 从入门到入R

[帮助IT管理AI/ML生态系统](https://hubs.ly/H0mGnnr0)
了解戴尔和`Domino`如何创建了一种令人耳目一新的简单方法来帮助公司获得他们需要的数据科学团队和技术，并以一种易于扩展的方式更快地运行。SPONSOR





**[使用django和postgres实现全文搜索](http://voorloopnul.com/blog/full-text-search-with-django-and-postgres/)**

如何在`Django`中实现全文搜索而不使用臃肿的`java`软件。

> 满足需求第一！



**[使用Python, Django and Twilio 构建一个IVR系统](https://www.twilio.com/blog/building-interactive-voice-response-ivr-system-python-django-twilio)**

`IVR`是交互式语音应答系统的缩写。这是你和你的用户通过电话交流的一种方式。`IVR`是通过语音和电话按键时产生的`DTMF`音调来操作的。在本教程中，您将使用`Python、Django和Twilio IVR`构建一个`IVR`系统。

> 语音传输和识别是第一



**[机器人和生成艺术还有Python，天哪!](https://www.generativehut.com/post/robots-and-generative-art-and-python-oh-my)**

如果你能将现代机器学习和人工智能工具的所有功能与现代软件开发范例的交互性和快速反馈循环联系起来，并将其直接导入到你的绘图仪中去创造艺术，那不是很酷吗?在这篇文章中，我们将学习如何用`Python`制作绘图仪艺术。

> OMG!

**[如何向Django应用程序添加Websockets而不需要额外的依赖项](https://jaydenwindle.com/writing/django-websockets-zero-dependencies/)**

现在`Django 3.0`已经提供了`ASGI`支持，在`Django`应用程序中添加`Websockets`不需要额外的依赖项。在这篇文章中，你将通过扩展默认的`ASGI`应用程序来学习如何使用`Django`处理`Websockets`。我们将讨论如何处理`Websocket`连接、发送和接收数据，并在示例`ASGI`应用程序中实现业务逻辑。

> ASGI 最高！
>
> 两用协议

[通过比较流行的项目模板来理解最佳实践的Python工具](https://t.co/OnTsVcUDAt)

[面部跟踪Nerf Turret项目](https://www.youtube.com/watch?v=cy3QToyba4s) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(5min)

[我是如何使用Python和一个不知名的公共数据库为我的LinkedIn朋友找到数千美元的](https://t.co/TIKFlBD8VP)

[Lua and Python](https://lwn.net/SubscriberLink/812122/bd245e8bd1018885/)

[电视背光补偿](http://www.lofibucket.com/articles/tv_backlight_compensation.html)

[为CPython做贡献](https://paper.dropbox.com/doc/Contributing-to-CPython--AuCcNnGQvvrN0p0G89TMUSy1Ag-JlgnduI6kw9MJIaGPpN9G)

[字典现在是有序的，要习惯它](https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/)

> 较新特性

## 有趣的项目、工具和库

**[JustPy](https://justpy.io/)** 
`JustPy`是一个面向对象的、基于组件的高级`Python Web`框架，不需要前端编程。只需几行`Python`代码，你就可以创建交互式网站，而无需任何`JavaScript`编程。

> 不走寻常路的框架
>
> 果然 starlette 强如xxx

**[vidify](https://github.com/vidify/vidify)**
在你的设备上实时观看音乐视频。

**[DeepSpeed](https://github.com/microsoft/DeepSpeed)** 

`DeepSpeed`是一个深度学习优化库，它使分布式培训变得简单、高效和有效。

**[Contextualise](https://github.com/brettkromkamp/contextualise)**
`Contexttualise`是一种简单而灵活的工具，特别适合于组织包含大量信息的项目和活动，这些项目和活动由非结构化的、广泛多样化的数据和信息资源组成。

**[Shopyo](https://github.com/Abdur-rahmaanJ/shopyo)**

面向小型商店的开放式库存管理和销售点(即将推出)。走向企业资源规划。First-timers-friendly。



**[dtale](https://github.com/man-group/dtale)**
`Flask/React`客户端可视化熊猫数据结构。

**[mnamer](https://github.com/jkwill87/mnamer)**

一个智能和可配置的命令行媒体文件组织工具。



**[Gila](https://gila.readthedocs.io/en/latest/)** 

Gila是一个基于Viper配置库的python3配置库。它的设计目的是使用python3使[12Factor apps](https://12factor.net/)的应用程序尽可能简单。



**[Diagrams](https://github.com/mingrammer/diagrams)**
`Diarams`作为原型化云系统架构的代码。

## 最近更新

[Python in Visual Studio Code – February 2020 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-february-2020-release/)
在这个版本中，我们做了一些改进，在我们的变更日志中列出了这些改进，总共关闭了66个问题，包括更快地启动`Jupyter`笔记本编辑器和减少配置通知。继续阅读，了解更多!

> VSC速度很快啊

## 活动和网络研讨会日程

[SoCal Python Meetup February 2020 - Santa Monica, CA](https://www.meetup.com/socalpython/events/268345566/)
将会有以下话题：

- Internet of Energy: 一个Pythonic的方式来支持加州电气防火努力
- 用Python开发一个高性能的通信引擎

[Introduction to using GPUs for Analytics - Philadelphia, PA](https://www.meetup.com/PyData-PHL/events/268253667/)
在这个演示中，`Randy`将重点介绍`gpu`在分析和数据科学中的应用，并使用`PyData`生态系统中的工具提供一些示例，以演示`gpu`显著减少数据处理时间的用例类型。

> 各处开花

[Bayesian Data Science by Simulation - New York, NY](https://www.meetup.com/nyc-uads/events/268293679/)
本教程通过模拟或黑客统计的视角介绍贝叶斯数据科学。我们将通过i)将它们与真实世界的故事相匹配& ii)模拟它们来熟悉许多常见的概率分布。我们将学习联合/条件概率、贝叶斯定理、先验/后验分布和概率，同时观察它们在现实数据分析中的应用。我们将看到贝叶斯推理在参数估计和比较组中的效用，最后我们将深入探讨概率编程的奇妙世界。



[Greater Hartford Python Meetup February 2020 - Hartford, CT](https://www.meetup.com/greaterhartfordpython/events/268256638/)
将会有一个演讲，数据科学的困境:Python还是R?为什么不两者都用呢?

> 这是一个问题

[PyHou Meetup February 2020 - Houston, TX](https://www.meetup.com/python-14/events/ndcfkrybcdbxb/)



Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  





----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-436.html)
- 改进: [issue-436.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23436.md)


