Title: pythonista-weekly : Pyw 437
Date: 2020-02-22 14:36
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-437

### 欢迎阅读《pythonista周刊》第437期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-437](https://mailchi.mp/pythonweekly/python-weekly-issue-437)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**  
[python开发者都需要的Vettery](https://www.vettery.com/tech?utm_source=newsletter&utm_medium=pythonweekly&utm_term=tech&utm_content=grouped&utm_campaign=ad-77579)  
Vettery是一个招聘网站，它改变了人们应聘或者雇佣的方式。准备好换工作地方了吗？免费制作简历，你的薪资你说了算，现在就和顶级雇主的HR联系吧！

### 新闻



**[PEP 614 -- 放松对装饰器的语法限制](https://www.python.org/dev/peps/pep-0614/)**

`Python`目前要求所有的装饰器都由一个点状的名称组成，后面可以有一个单独的调用。该`PEP`建议消除这些限制，并允许装饰者成为任何有效的表达式。

> 更自由的装饰器，不过还是看使用频次吧。

### 文章、教程与话题

**[Deep Learning (for Audio) with Python](https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)（一共14个章节)**

在本系列中，探索`Python`编程语言中深度学习的理论和实现。本课程侧重于音频和音乐深度学习的应用，但讨论了适用于任何问题的一般算法和原理。

> 还不错的教程，播放量可以的，分的很细

**[Python Itertools之旅](https://martinheinz.dev/blog/16)**

让我们来看看两个极好的`Python`库-`itertools and more_itertools`，以及如何用它们进行数据处理。



**[在Django模板中安全地放入JavaScript数据](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)**

`Django模版`经常被用来传输`JavaScript`代码。不凑巧的是，如果实现不正确，这还有了`Html`注入的风险，从而导致`XSS`(跨站点脚本)攻击。让我们看看这个问题，并看看我们可以如何用`json_script`进行修复。

> 前后端分离也是一种解决方式呀

**[遗传算法说明 : Python实现](https://hackernoon.com/genetic-algorithms-explained-a-python-implementation-sd4w374i)**

遗传算法，也被简称为`"GA"`,算法的灵感来自`Charles Darwin`的自然选择理论，该理论旨在为我们不太了解的问题找到最佳解决方案。让我们来看看如何使用`Python`编写一个简单的遗传算法实现！



**[Python中的函数重载](https://arpitbhayani.me/blogs/function-overloading)**

原生的`Python`不支持函数重载-有多个函数有着相同的名字。在这篇文章中，你将学习到我们可以在`Python`中通过装饰器，字典之类的常用语言结构如何实现并增加此功能。



**[如何使用Python,Flask,Postgres and JWT 构建一个认证服务](https://www.grizzlypeaksoftware.com/articles?id=5SCpQMgookgKNtupzNHg9K)**

在这篇文章，我们将学习如何构建一个认证服务器，它可以被当作调用一个`API`的认证检测或者作为微服务体系结构。在这个项目中，我们将使用`Python, Flask, Postgres and JWT`。

> 拆分后都是一个服务。

[2020 Gartner Magic Quadrant for Data Science and Machine Learning Platforms](https://hubs.ly/H0n2-j60)

The 2020 Gartner Magic Quadrant for Data Science and Machine Learning Platforms is now available, and Domino is named a Visionary. Read the full analysis of Domino and other vendors in the report. SPONSOR

**[用 Neighbourhood Components Analysis(邻里成分分析)实现 kNN 分类](https://kevinzakka.github.io/2020/02/10/nca/)**

一份`Neighbourhood Components Analysis`详尽的解释，并用`PyTorch 和一个 GPU-accelerated`实现。



**[Python CLI Utilities with Poetry and Typer](https://www.pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer/)**

`Python`作为一门脚本语言是非常灵活的-让我们学习如何将简单的脚本扩展到功能齐全的命令行工具。

> 容易忽略的教程

**[如何用一行代码将Python多进程扩展到集群](https://t.co/qCDLxnpKjb)**

这篇文章展示了`multiprocessing.Pool`可以从单台机器无缝扩展到集群。



**[Python Tools for Record Linking and Fuzzy Matching](https://pbpython.com/record-linking.html)**

这篇文章讨论了一个很有用的工具，可以用来对文本字段进行记录链接及模糊匹配。也可以用于消除重复数据。



**[来自 Python charmer的笔记: 如何让它随着你的演讲起舞](https://t.co/VYGoQEd23P)**

比较9个最著名的自动语音识别引擎。了解哪一个最适合你的需求，以及如何在`Python`程序中使用它。

> 嘿，Py 来一个 新宝岛

**[DevOps for Data Science with GCP](https://t.co/JEEMYcNHXb)**
为模型服务部署生产级容器。

> 最终都得上线。

**[Python Firebase 初学者教程](https://www.youtube.com/watch?v=VnUXbo8JvvA) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(35min)**

在这个`Python Firebase`的初学者教程中，我们将用`Python`语言来让`Firebase`工作。特别是我们将使用`Firebase`实时数据库，`Firebase认证系统`以及`Firebase存储`，当然我们也会使用`pyrebase`库，一个简单的封装了`Firebase API`的库。



**[爱我不爱我: 用TensorFlow and Twilio做文本分类](https://www.twilio.com/blog/classify-texts-with-tensorflow-and-twilio-to-answer-loves-me-loves-me-not)**

这篇文章将讨论如何在`Python`中使用`Twilio`和`TensorFlow`用神经网络进行二进制文本分类。



**[5行代码定制一个对象检测模型 ](https://t.co/73BIfMhRgN)**

用`Detecto`让计算机视觉更简单，基于`Pytorch`构建的一个`Python`库。

> 从独轮车到汽车



[剖析网络堆栈](https://www.thedigitalcatonline.com/blog/2020/02/16/dissecting-a-web-stack/)

[如何创建自己的简单的heroku-clone和设置Django和Postgres](https://blog.alfred.software/2020/02/12/how-to-create-your-own-heroku-clone-and-setup-django-and-postgres/)

> 简单博客go

[如何在Python中反转二叉树](https://ao.gl/how-to-reverse-a-binary-tree-in-python/)

[带Keras, TensorFlow, and Deep Learning的自编码器](https://www.pyimagesearch.com/2020/02/17/autoencoders-with-keras-tensorflow-and-deep-learning/)

[用WebSockets 管理测试执行资源](https://tryexceptpass.org/article/manage-test-resources-with-websockets/)

### 有趣的项目、工具和库

**[HiPlot](https://github.com/facebookresearch/hiplot)** 
`HiPlot`是一个轻量级的交互式可视化工具，可以帮助人工智能研究人员使用平行图和其他图形方式来表示信息，从而发现高维数据中的相关性和模式。

> 来张图片了解一下
>
> ![image.png](https://i.loli.net/2020/02/23/NlAjsRuX3SpnUTY.png)

**[Cozette](https://github.com/slavfox/Cozette)**
为舒适而优化的位图编程字体。

> 可能我一直不舒适！
>
> 位图编程，你也需要这个字体：
>
> ![image.png](https://i.loli.net/2020/02/23/NezWI2SJdGTEmAU.png)

**[matchering](https://github.com/sergree/matchering)**

开源音频匹配和母带处理。

**[ursina](https://github.com/pokepetter/ursina)**

一个由`python and panda3d`构成的游戏引擎。



**[PyMatting](https://github.com/pymatting/pymatting)**

A Python Library for Alpha Matting.

**[Docket](https://github.com/keva161/Docket)**
一个为测试自动化实践而构建的成熟的todo应用程序。

> 这名字，可以！rt！

**[dogelang](https://pyos.github.io/dg/)**

编译自`Python`字节码的一个编程语言，就像`Scala`编译到`JVM`。这本质上意味着`dg`是`Python 3`的另一种语法。它还允许你使用所有现有的库。

> 爱狗人士(/狗头)

**[pycharm-security](https://github.com/tonybaloney/pycharm-security)**

一个`Pycharm`插件，在你的`Python`项目中寻找安全漏洞。



**[ldapper](https://github.com/UMIACS/ldapper)**

一个简单的、符合人体工程学的`Python ORM`，用于与`LDAP`交互。

> LDAP 收藏

**[Diagrams](https://github.com/mingrammer/diagrams)**
`Diarams`作为原型化云系统架构的代码。

### 活动和网络研讨会日程

**[Getting Started Testing with pytest - Boston, MA](https://www.meetup.com/bostonpython/events/266720542/)**

你想学习如何在`Python`中用`pytest`去编写自动化测试吗？我们将从头开始！看一下`pytest`是如何工作的，以及如何编写测试。在又了基础知识之后，我们将进入`fixtures,parameterization,and coverage measurement`。之后我们将做一些进阶的技巧：包括`test doubles(mocek and fakes)`.



**[San Diego Python Meetup February 2020 - San Diego, CA](https://www.meetup.com/pythonsd/events/xrtzkrybcdbkc/)**
将会有以下的的话题

- Python2 End of Life
- Exploring Transformers with ALBERT and BERT
- 可学习的助理 that "Knows Your Business"

**[DC Python Meetup February 2020 - Arlington, VA](https://www.meetup.com/dcpython/events/267989837/)**

将会有一个演讲，用Python进行机器学习的可视化诊断。

**[Hobby Robotics with Nvidia Jetson Nano - Ottawa, ON](https://www.meetup.com/ottawapython/events/xwbgcqybcdbkc/)**
`Gerhard Roth`将讲述作为一种爱好，小型机器人能做些什么，并将重点介绍`Python`是如何用于机器人的。新的`Nvidia Jetson Nan`单板计算机和捷步机器人将使用`Jupyter`笔记本电脑进行演示。一个小型的`Jetbot`将会被展示出来。

**[Clinical Text Processing (NLP) with Python - Pittsburgh, PA](https://www.meetup.com/Python-Pittsburgh/events/268223150/)**

在这次的会话中，我们将讨论一些`clinical NLP`中的机会，规划基本的`NLP`任务，以及浏览可用的资源-用于这些的`Python`库及框架。许多这样的库使得利用最先进的自然语言处理研究在`clinical NLP`上建立模型变得非常容易。



**[DragonPyMeetup February 2020 - Ljubljana, Slovenia](https://www.meetup.com/Ljubljana-Python-Group/events/268065592/)**
将会有以下的话题

- `Azure`机器学习的`Python`软件开发工具包旋风之旅
- Going commando in Python 



Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  





----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-437.html)
- 改进: [issue-437.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23437.md)


