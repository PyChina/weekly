Title: pythonista-weekly : Pyw 438
Date: 2020-02-29 14:47
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-438

### 欢迎阅读《pythonista周刊》第438期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-438](https://mailchi.mp/pythonweekly/python-weekly-issue-438)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**

使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[马上跟踪你的python应用吧！免费试用14天哦！](https://www.datadoghq.com/dg/apm/python-troubleshooting/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Troubleshooting)

### 文章、教程与话题

**[如何用 Python and Django 创建一个 YouTube 的克隆](https://www.education-ecosystem.com/andreybu/RaWGm-how-to-create-a-youtube-clone-in-python-and-django/9b4Kz-youtube_webapp/) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(about 5 h)**

这篇教程介绍了如何用`Python`创建一个`YouTube.com web app`克隆，将会引导你完成构建一个最小化`www.youtube.com`的所有过程。我们将聚焦于构建一个最小化的`app`,但是可以根据你的需要进行扩展。

> Django - part 1

**[Django 提速手册: 创建一个更快的 Django app ](https://openfolder.sh/django-faster-speed-tutorial)**

在创建几个`Django app`的过程中，我学到了一些关于速度优化的东西。在这个过程中的某些地方，无论是前端或者后端，都没有很好的文档。所以我决定尽量收集一些我知道的在这篇文章中。



> Django - part 2

**[个性化你的python提示](https://arpitbhayani.me/blogs/python-prompts)**

个性化是我们所有人都喜欢的。在这篇文章中，我们发现了我们可以个性化定制`Python`解释器的提示。

> IPython独家秘籍

**[从硬盘中读取NumPy 数组: mmap() vs. Zarr/HDF5](https://pythonspeed.com/articles/mmap-vs-zarr-hdf5/)**

如果你的`NumPy array`太大了而不能一次性都丢到内存里，你可以分块处理：隐式或者显式的每次从硬盘中只加载一块。不管怎样，你需要将数组存到硬盘中。针对这种特殊的情形，有两种常见的方式可以采用。每种方式都有不同的优缺点，所以在这篇文章中，我将解释每种存储系统是如何工作的，以及你什么时候可能需要使用它们。特别的是，我将重点关注为运行你的计算而优化的数据格式，而不一定是为了与他人共享。

> 数据存储要素。

**[如何在 pandas 中合并 DataFrames?](https://www.youtube.com/watch?v=iYWKfUOtGaw) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(22 min)**

如果你想把多个数据集连合到一个`pandas DataFrame`中，你就需要使用`"merge"`功能。在这个视频中，你将确切了解合并操作期间发生了什么，以及如何使用四种不同类型的联接。在视频的最后，你将对于合并你自己的`DataFrames`得心应手。

> 选择困难症的解法吗！

[2020 Gartner Magic Quadrant for Data Science and Machine Learning Platforms](https://hubs.ly/H0n2-j60)
The 2020 Gartner Magic Quadrant for Data Science and Machine Learning Platforms is now available, and Domino is named a Visionary. Read the full analysis of Domino and other vendors in the report. SPONSOR

**[在Visual Studio代码中开始使用Jupyter Notebook 工作](https://t.co/Iz4sjQ71r2)** 

`VS Code`现在通过`Python`插件提供了对`Jupyter Notebook`的本地支持。这里有一个简单的例子来概述它的主要功能。

> 来势汹汹的 VSC

**[Python 数据清洗: 终极指南 (2020)](https://t.co/jX0OKuB3qu)**

清洁什么和如何清洁的技巧。



**[Conditional coverage](https://sobolevn.me/2020/02/conditional-coverage)**

有时，你的代码必须根据外部环境采取不同的路径。确保你的`coverage`流畅运行。



[如何禁止Django 的自动命名迁移](https://adamj.eu/tech/2020/02/24/how-to-disallow-auto-named-django-migrations/)

[卷积网络的音高检测](https://0xfe.blogspot.com/2020/02/pitch-detection-with-convolutional.html)

[使用Rich实现更好的Python回溯](https://www.willmcgugan.com/blog/tech/post/better-python-tracebacks-with-rich/)

> 话不多说，来张图：
>
> ![image.png](https://i.loli.net/2020/02/29/dwM5xo8cZ2fbgIW.png)
>
> 提取关键字版本。

[让我们构建一个简单的解释器。第18部分:执行过程调用](https://ruslanspivak.com/lsbasi-part18/)

> 原理层，还是很有趣。

[深度学习和PyTorch的手语识别](https://theaisummer.com/Sign-Language-Recognition-with-PyTorch/)

[Python in Production](https://hynek.me/articles/python-in-production/)

> 快来看看！

[Pro-Tip – A Tip About DRF Permissions](https://www.revsys.com/tidbits/tip-about-drf-permissions/)

[如何使用pytest和Black欺骗单元测试](https://simonwillison.net/2020/Feb/11/cheating-at-unit-tests-pytest-black)





### 有趣的项目、工具和库

**[PostHog](https://github.com/PostHog/posthog)** 

`PostHog`是开源产品分析，专为开发人员打造。自动收集您网站或应用程序上的每个事件，无需向第三方发送数据。只需点击一下鼠标，就可以在你自己的基础架构上进行部署，并且可以完全访问底层数据。

> 摆脱第三方指日可待！？

**[Dispatch](https://github.com/Netflix/dispatch)**

所有你今天要管理的临时事件，以及需要做的其他时间，甚至更多。

> trending 今日常见
>
> 调度新助手。

**[Newscatcher](https://github.com/kotartemiy/newscatcher)**
以编程方式从（几乎）任何网站收集标准化新闻。

> 一个没有感情的新闻抓取机

**[vectorbt](https://github.com/polakowo/vectorbt)**

`Python`库，用于大规模回测和分析交易策略。



**[AdelaiDet](https://github.com/aim-uofa/adet)**

`AdelaiDet`是一个开源工具箱，用于执行多个实例级检测和识别任务。

**[Updog](https://github.com/sc0tfree/updog)** 

`Updog`替代了`Python`的`SimpleHTTPServer`。 它允许通过`HTTP / S`进行上传和下载，可以设置临时`SSL`证书并使用`http`基本身份验证。

> More pythonic

**[glitch-this](https://github.com/TotallyNotChase/glitch-this)**
将静态图像毛刺化为毛刺图像和GIF！

> 风格突变！
>
> ![glitched2.gif](https://i.loli.net/2020/02/29/lVFjaR6KbponrJO.gif)
>
> 

**[Broadcaster](https://github.com/encode/broadcaster)**

`Broadcaster`通过在许多不同的后端服务上提供简单的广播`API`来帮助您开发实时流功能。

> 0.2的测试版本中，不过很有意思。
>
> 当然，基于 startlette，看来 startlette 备受瞩目。
>
> 另外，作者在找会CI的小伙伴创建 Action 有兴趣就 突突突！

**[text-script](https://github.com/GeorgeCiesinski/text-script)**
在后台运行的应用程序，它将文本快捷方式替换为预先保存的文本块。

**[batch-copy](https://github.com/dibsonthis/batch-copy)**
允许用户一次复制/粘贴多个内容的工具。

**[face2data](https://github.com/rodrigobressan/face2data)**
在不到一秒钟的时间内从人脸提取有意义的信息。 由`Keras`和`Flask`提供支持。



Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  





----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-438.html)
- 改进: [issue-438.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23438.md)


