Title: pythonista-weekly : Pyw 525
Date: 2021-11-13 16:11
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-525


### 欢迎阅读《pythonista周刊》第525期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-525](https://mailchi.mp/pythonweekly/python-weekly-issue-525)  
>翻译：Dustyposa

来自赞助商（PS：原文的赞助商）:

[Get Your Weekly Dose of Programming](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)
A weekly newsletter featuring the best hand curated news, articles, tutorials, talks, tools and libraries etc for programmers. [Join For Free](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)

### 新闻

[PSF 2021 End of the year fundraiser!](https://pyfound.blogspot.com/2021/11/2021-end-of-year-fundraiser.html)
`PSF` 启动了年终募捐活动。有两种捐赠方式。1.直接向PSF捐款，或者2.购买一个打折的PyCharm许可证，所有收益都归PSF。对PSF的财政捐助有助于维持支持更大的Python社区的项目。

### 文章、教程与话题


[为什么Python在 profiling 过程中需要暂停 - 但Ruby并不总是如此](https://www.benfrederickson.com/why-python-needs-paused-during-profiling/)
这篇文章讨论的是用 `py-spy` 进行剖析时，数据竞赛的影响是什么样的，为什么由于 `CPython` 和 `CRuby` 解释器实现的不同，这种情况在 `py-spy` 中比在 `rspy` 中更经常发生，以及为什么尽管有可能产生不准确的 `profiling`，你仍然可能要考虑在某些情况下使用非阻塞的方法。

[Python的后置默认参数](https://lwn.net/SubscriberLink/875441/c29a2006cf489b7f/)
`Python` 支持函数参数的默认值，但这些默认值是在函数定义时评估的。在 `python-ideas ` 邮件列表中，已经对增加默认值的建议进行了长时间的讨论，这些默认值在函数被调用时被评估。这个想法的产生，部分是由于对 `Python` 中无意识操作符的建议的又一次复活。迟到的默认值将有助于这些操作符的一个使用情况，但还有其他更有力的理由来考虑将其添加到语言中。

[An oral history of Bank Python](https://calpaterson.com/bank-python.html)
大型投资银行使用的 `Python` 的奇怪世界。

[Pass-by-value, reference, and assignment](https://mathspp.com/blog/pydonts/pass-by-value-reference-and-assignment)
这篇文章解释了为什么 `Python` 不使用逐值传递系统，也不使用逐参考传递。

[如何构建、测试和发布一个开源的Python库](https://simonwillison.net/2021/Nov/4/publish-open-source-python-library/)
学习如何使用 `cookiecutter`、`pytest` 和 `GitHub Actions` 来开发一个新的 `Python` 库、添加测试、运行持续集成并自动向 `PyPI` 发布新的软件包。

[Start Analyzing Your Python Projects](https://www.sonarqube.org/features/multi-languages/python/?utm_source=pythonweekly&utm_medium=paid&utm_campaign=python&utm_content=secondary-211111)
SonarQube has over 170 unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your Python code. Get started for free! SPONSOR

[Python中ThreadPoolExecutor的6种使用模式](https://superfastpython.com/threadpoolexecutor-usage-patterns/)
你可以采用其中一种常见的使用模式，以获得 `Python` 中 `ThreadPoolExecutor` 的最大好处。在本教程中，你将发现 `Python` 线程池的常见使用模式。

[SpaCy vs NLTK. 文本归一化比较](https://newscatcherapi.com/blog/spacy-vs-nltk-text-normalization-comparison-with-code-examples)
我们将深入探讨文本规范化的内容、原因和方法。用 `SpaCy` 和 `NLTK Python` 库编写的代码实例。

[Cython、Rust等：为Python扩展选择一种语言](https://pythonspeed.com/articles/rust-cython-python-extensions/)
有时纯 `Python` 代码是不够的，你需要用 `C、C++` 或 `Rust` 这样的编译语言实现一个扩展。根据你的特殊情况和需要，你可能想选择一个不同的工具。但是哪一个呢？让我们看看你有哪些选择，然后通过各种场景，看看哪种选择最合适。

[我只想运行这一个Python脚本](https://www.die-welt.net/2021/11/i-just-want-to-run-this-one-python-script/)
是否有过这样一个脚本，它与 `Python 2` 和 `3` 都兼容，但你不想麻烦用户知道调用哪个解释器？也许是因为这个脚本经常被用在只有一种 `Python` 的环境中，而用户只是希望事情能够顺利进行？而且只有那一个脚本文件，没有包，没有额外的包装脚本，什么都没有。

[Python中的蒙特卡洛方法简介](https://www.youtube.com/watch?v=U00Kseb6SB4) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
本视频包括 `python` 中蒙特卡洛模拟技术的基本教程，以及一些例子。

[Understand Django: Command Your App](https://www.mattlayman.com/understand-django/command-apps/)
通过这篇文章，你将了解到命令。命令是执行与你的 `Django` 应用程序互动的脚本的方式。我们将看到内置的命令以及如何建立你自己的命令。

[如何使用Ergast API和Seaborn在Python中可视化一级方程式锦标赛](https://medium.com/towards-formula-1-analysis/how-to-visualize-the-formula-1-championship-in-python-using-the-ergast-api-and-seaborn-ac2f88ae7248)
本教程将向你展示如何使用来自 `Ergast API` 的数据来可视化 `2021` 年冠军积分榜在各轮比赛中的变化。此外，本教程还将向你展示如何用 `Seaborn` 创建图表，`Seaborn` 是一个基于 `Matplotlib` 的 `Python` 库。

[如何保证你的Python软件供应链的安全](https://medium.com/artefact-engineering-and-data-science/how-to-secure-your-python-software-supply-chain-81490f6e4ff9)
了解你所面临的风险的指南，以及防范这些风险的一些提示。

### 有趣的项目、工具和库


[T5X](https://github.com/google-research/t5x)
`T5X` 是一个模块化的、可组合的、有利于研究的框架，用于高性能的、可配置的、自助式的训练、评估和推断多种规模的序列模型（从语言开始）。

[ndarray_comparison](https://github.com/synapticarbors/ndarray_comparison)
Benchmark of toy calculation on an n-dimensional array using python, numba, cython, pythran and rust.

[EfficientWord-Net](https://github.com/Ant-Brain/EfficientWord-Net)
`EfficientWord-Net` 是一个基于一次性学习的热词检测引擎，其灵感来自 `FaceNet` 的连体网络结构。

[Samila](https://github.com/sepandhaghighi/samila)
`Samila` 是一个用 `Python` 编写的生成性艺术生成器，`Samila` 让你在数千个点的基础上创造艺术。每一个点的位置都是由一个公式计算出来的，这个公式有随机参数。由于随机数的存在，每张图片看起来都不一样。

[redun](https://github.com/insitro/redun)
然而，另一个冗余的工作流引擎。`redun` 旨在成为一个更具表现力和高效的工作流框架。

[FiftyOne](https://github.com/voxel51/fiftyone) 
用于建立高质量数据集和计算机视觉模型的开源工具。

[QuadrupedRobot](https://github.com/mangdangroboticsclub/QuadrupedRobot)
Mini Pupper - ROS, OpenCV, Open-source, Pi Robot Dog.

[google-workspace](https://github.com/dermasmid/google-workspace)
一个非官方的高水平 `Python API` 包装器，用于一些基于生产力的谷歌应用程序，它专注于简单性。

[ZenGL](https://github.com/szabolcsdombi/zengl)
`ZenGL` 是一个简约的 `Python` 模块，完全提供了一种用 `OpenGL` 渲染场景的方法。

[ticktock](https://github.com/victorbenichoux/ticktock)
Simple Python code metering library.

[multi-py](https://github.com/multi-py)
支持多架构的 `Python` 容器。

[pydbantic](https://github.com/codemation/pydbantic)
在数据库中塑造、创建、访问、存储数据的单一模型。

[drf-turbo](https://github.com/Mng-dev-ai/drf-turbo)
一个用 `cython` 编写的用于 `REST` 框架的替代性序列化器的实现，是为了提高速度。

### 最近更新

[TensorFlow 2.7](https://blog.tensorflow.org/2021/11/whats-new-in-tensorflow-27.html)
这个版本通过更清晰的错误信息、简化的堆栈跟踪来提高可用性，并为迁移到 `TF2` 的用户增加了新的工具和文档。

[Python 3.9.8 and 3.11.0a2 are now available](https://pythoninsider.blogspot.com/2021/11/python-398-and-3110a2-are-now-available.html)

### 活动

[Virtual: PyLadies Dublin November 2021](https://www.meetup.com/PyLadiesDublin/events/281523439/)
将会有以下话题:

- 使用 `Python` 将实体游戏引入互联网
- Scaling Data Science with Dask


[Virtual: PyLadies SWFL November 2021](https://www.meetup.com/PyLadies-SWFL/events/281853064/)
There will be a talk, Augmenting human creativity with automated text generation.

[Virtual: PyData Chicago November 2021](https://www.meetup.com/PyDataChi/events/281821505/)
There will be a talk, Machine Learning on Graph: Graph Signal Processing & Graph Substructure Learning.

Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！


- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-525.html)
- 改进: [issue-525.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23525.md)

