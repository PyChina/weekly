Title: pythonista-weekly : Pyw 526
Date: 2021-11-19 16:11
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-526


### 欢迎阅读《pythonista周刊》第526期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-526](https://mailchi.mp/pythonweekly/python-weekly-issue-526)  
>翻译：Dustyposa

### 文章、教程与话题

[Infrastructure as Code](https://www.youtube.com/watch?v=EtEb40LE5zQ) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
什么是基础设施即代码？在本课程中学习，并通过实施三个 `IaC` 项目获得实践机会。

[Trojan Source and Python](https://lwn.net/SubscriberLink/875964/cf2e97bf44fd5fd4/)
自从 `11月1日` 木马源码漏洞被披露以来，它们一直在各个开发社区激荡。在编程语言中处理 `Unicode`，尤其是双向 `Unicode` 时，可能会出现一些奇怪的情况，例如，Rust会检查字符串和注释中的问题代码点，如果存在这些代码点，默认情况下会拒绝编译。 `Python` 选择了一条不同的道路，但正在进行的工作是帮助程序员了解 `Trojan Source` 所强调的各种隐患。

[Spotify Codes - Part 2](https://boonepeter.github.io/posts/spotify-codes-part-2/)
第一部分深入探讨了 `Spotify` 代码，并解释了它们如何工作的一般技术概念。这篇文章将比第一部分更有技术含量，因为作者试图解释 `Spotify` 是如何编码他们的条形码的。

[如何在Python中对一个字典进行排序](https://treyhunner.com/2021/11/how-to-sort-a-dictionary-in-python/)
词典最好用于键值查询：我们提供一个键，词典非常迅速地返回相应的值。但是如果你既需要键值查找又需要迭代呢？我们可以在 `dictionary` 上进行循环，当循环时，我们可能关心 `dictionary` 中项目的顺序。考虑到 `dictionary` 项目的顺序，你可能会想知道我们如何对 `dictionary` 进行排序？

[Django, FastAPI, Full Stack Roles & Python Programming](https://www.youtube.com/watch?v=PJkO1NPgEk4) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
与 `Daniel Roy Greenfeld的对话` ，他是《Two Scoops of Django》系列书籍的共同作者，也是大量 `Python` 和 `Django` 开源项目的创建者。

[Game Hacking with Python and cheat engine](https://noob3xploiter.medium.com/game-hacking-with-python-and-cheat-engine-5000369e27b9)
这篇文章告诉你如何用作弊引擎编辑内存来黑掉游戏，我们还将用 `python` 写一个程序，自动编辑内存，便于我们做黑客。

[Customize Python dependency resolution with machine learning](https://developers.redhat.com/articles/2021/11/17/customize-python-dependency-resolution-machine-learning)
本文介绍了 `Project Thoth` 创建的一个新的基于云的 `Python` 依赖性解析器。在云端运行，`Thoth` 使用强化学习技术和你想要的标准来解决 `Python` 库的依赖性。此外，一个可插拔的接口让你可以修复 `underpinning` 和 `overpinning` 问题（即指定版本的软件包过于严格或过于宽松），并对解析过程进行额外的调整。这个过程考虑到了运行环境、硬件和其他对基于云的解析器的输入。

[Speed up your Conda installs with Mamba](https://pythonspeed.com/articles/faster-conda-install/)
`Conda` 的安装速度非常慢，但你可以用一个更快的小`Conda` 重新实现，即 `Mamba` 来加速安装。

[Ruby vs Python comes down to the for loop](https://softwaredoug.com/blog/2021/11/12/ruby-vs-python-for-loop.html)
对比每种语言处理迭代的方式，有助于理解如何有效地使用其中一种语言。

[16 Reasons to Use VS Code for Developing Jupyter Notebooks](https://pbpython.com/vscode-notebooks.html)
VS Code has many features that make it a useful platform for Jupyter Notebook development.

[Getting Started With Pants and Django (Part 1)](https://g-cassie.github.io/2021/10/30/django-pants-tutorial-pt1.html)

[Python: Please stop screwing over Linux distros](https://drewdevault.com/2021/11/16/Python-stop-screwing-distros-over.html)

[How Python list really works](https://antonz.org/list-internals/)

### 书籍📚

[Scientific Visualization: Python + Matplotlib](https://github.com/rougier/scientific-visualization-book)
一本关于使用 `python` 和 `matplotlib` 的科学可视化的开放性书籍。

### 有趣的项目、工具和库

[OpenFold](https://github.com/aqlaboratory/openfold)
可训练的 `AlphaFold 2` 的 `PyTorch` 复制品。 

[prometeo](https://github.com/zanellia/prometeo)
用于嵌入式高性能计算的实验性 `Python-to-C` 转译器和特定领域语言。 

[arxiv-sanity-lite](https://github.com/karpathy/arxiv-sanity-lite)
`arxiv-sanity`，但非常精简，只是提供核心价值主张，即能够标记感兴趣的 `arxiv` 论文，并让程序推荐类似的论文。

[tiptop](https://github.com/nschloe/tiptop)
`tiptop` 是一个符合 `top` 精神的命令行系统监控工具。它可以显示各种有趣的系统统计信息，并绘制成图表，而且可以在所有操作系统上使用。

[video-stream](https://github.com/levina-lab/video-stream)
`Video Stream `是一个先进的 `Telegram` 机器人，允许你在 `Telegram` 群组视频聊天中播放视频和音乐。 

[TorchGeo](https://github.com/microsoft/torchgeo)
`TorchGeo` 是一个 `PyTorch` 领域库，类似于 `torchvision` ，它提供了专门针对地理空间数据的数据集、变换、采样器和预训练模型。

[DeepMosaics](https://github.com/HypoX64/DeepMosaics)
自动删除图像和视频中的马赛克，或为其添加马赛克。

[fileless-elf-exec](https://github.com/nnsee/fileless-elf-exec)
执行 `ELF` 文件而不把它们丢在磁盘上。

[kuroko](https://github.com/kuroko-lang/kuroko)
`Python` 的方言，具有明确的变量声明和块范围，有一个轻量级的、易于嵌入的字节码编译器和解释器。

[rocket-recycling](https://github.com/jiupinjia/rocket-recycling)
Rocket-recycling with Reinforcement Learning.

### 最近更新

[Python 3.9.9 hotfix release is now available](https://pythoninsider.blogspot.com/2021/11/python-399-hotfix-release-is-now.html)
`3.9.9` 作为 `Python 3.9.8` 中的 `argparse` 回退的热修复版提前发布，它导致复杂的命令行工具无法正确识别子命令。详情见  `BPO-45235`。与 `3.9.8` 相比，这个版本中只有三个其他的错误修正。

### 活动

[Virtual: XtremePython 2021](https://xtremepython.dev/2021/)
The XtremePython online conference is organised by developers for developers! It includes 6 small sessions (25min each).

[Virtual: DragonPy Meetup November 2021](https://www.meetup.com/Ljubljana-Python-Group/events/281911382/)
将会有以下话题:

- Everyday Jupyter
- Graphviz (create charts and diagrams with Python)
- FFMPEG (create videos with Python)


[PyBerlin 33 - Berlin](https://www.meetup.com/PyBerlin/events/281660854/)
将会有以下话题:

- Scalable crawling with Kafka, Scrapy and Spark
- 软件工程过程质量的衡量标准
- 用领域驱动设计让你的软件架构大放异彩
- From Python to Product


[Virtual: PyData Hamburg Meetup November 2021](https://www.meetup.com/PyData-Hamburg/events/281549679/)
将会有以下话题:

- ATHENA Art Assistant - Women & AI Creations
- Hyper parameter tuning with Deep learning

Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！


- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-526.html)
- 改进: [issue-526.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23526.md)

