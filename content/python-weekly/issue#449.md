Title: pythonista-weekly : Pyw 449
Date: 2020-05-16 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-449

### 欢迎阅读《pythonista周刊》第449期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-449](https://mail chi.mp/pythonweekly/python-weekly-issue-449)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[来免费试用 14 天吧！](https://www.datadoghq.com/dg/apm/python-troubleshooting/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Troubleshooting)

### 新鲜事

[征集志愿者! Python GitHub 迁移工作小组](https://pyfound.blogspot.com/2020/05/call-for-volunteers-python-github.html)

我们正在寻找志愿者来加入一个工作小组，参与 `Python` 从 `bugs.python.org` 迁移到 `GitHub`。我们希望确保这次迁移能代表社区的需求。

[官宣一个用 Pyro 设计最佳实验的新框架](https://eng.uber.com/oed-pyro-release/)

`Uber AI` 发布了一个在 `Pyro` 的基础上的新框架，可以让实验者无缝自动优化实验设计（OED），用于模型的快速迭代。

### 文章、教程与话题

[通过在公共仓库中反编译 Python 字节码来查找机密信息](https://blog.jse.li/posts/pyc/)

缓存控制这我周围的一切，`.pyc` 文件可能会包含一些机密信息，不应该将它签入源代码控制，使用标准的 `Python .giignore`。

[Python 风格要素](https://github.com/amontalenti/elements-of-python-style)

这篇文档超越了 `PEP8`，涵盖了我认为优秀的 `Python` 风格的核心内容。它超越了仅仅是语法和模块布局的问题，而是涉及到了范式、组织和架构等领域。

[使用 Patreon API 和 Pillow 来自动创建图片](https://www.youtube.com/watch?v=RO6JxDOVwLQ) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（52min）

在这篇教程中，我们将学习如何使用 `Patreon API` 和 `Pillow lib` 来自动创建图片。我特别用这个在我的视频末尾添加了致谢词来感谢我的支持者。这个视频将重点关注 `Patreon` 支持者，但是在下个视频，我们将看到用 `YouTube 会员` 如何使用 `YouTube API` 来做相同的事情。

[在 VS Code 中带有热加载的 Flask 调试](https://blog.theodo.com/2020/05/debug-flask-vscode/) 

学习如何为你的 `Dockerized Flask 应用` 设置一个带有热加载的强大的 `VS Code` 调试器。

[计算机视觉与深度学习的伦理应用](https://www.pyimagesearch.com/2020/05/11/an-ethical-application-of-computer-vision-and-deep-learning-identifying-child-soldiers-through-automatic-age-and-military-fatigue-detection/)

在这篇教程中，我们将学习到如何通过自动年龄识别以及军人疲劳识别应用计算机视觉，深度学习以及 `OpenCV` 来识别潜在的儿童士官。

[从 PyTorch 转到 PyTorch Lightning](https://www.youtube.com/watch?v=QHww1JH7IDU) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（41min）

在本视频，`William Falcon` 重构了一个 `PyTorch VAE` 到 `PyTorch Lightning`。从视频就能明显看出，这是在没有预先知识的情况下重构新的 `repository` 的真实尝试。尽管如此，整个转化用了不到 `45` 分钟。

[静态代码分析的实践介绍](https://deepsource.io/blog/introduction-static-code-analysis/)

看到代码中的常见问题了吗？让我们创建一个分析器来自动检测它们。

[RSVP for the ONLY Python Web Conference (Virtual) | June 17-19, 2020](https://pythonwebconference.com/) 
Experts discuss hard web production problems. 40+ talks on Django, Plone, CI/CD, Containers, Serverless, REST APIs, microservices, etc. Join JetBrains and Six Feet Up to discuss what the future holds. SPONSOR

[利用 InnoDB 架构优化 Django 模型设计](https://t.co/GO1oixzPnO)

每个开发人员都应该了解 `InnoDB`。

[Python 中神经网络的介绍(你梭需要知道的东西)](https://www.youtube.com/watch?v=aBIGJeHRZLQ) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（1h）

在这段视频中，我们将从一些基础开始。我们看看我们为什么使用神经网络以及它们是如何工作的。我们做了一个网络结构的概述（输入层，隐藏层，输出层）。我们讨论了一下如何选择隐藏层和神经元的数量。我们还看了一下超参数，如批处理大小、学习率、优化器（`adam`）、激活函数（`relu、sigmoid、softmax`）和 `dropout`。

[使用Python的concurrent.futures实现无障碍并发。](https://rednafi.github.io/digressions/python/2020/04/21/python-concurrent-futures.html)
用 `concurrent.futures` 并发运行简单任务。

[如何建立一个神经网络将手语翻译成英语](https://www.digitalocean.com/community/tutorials/how-to-build-a-neural-network-to-translate-sign-language-into-english)

在这篇教程中，你将使用计算机视觉为你的网络摄像头来构建一个 `American` 手语翻译器。当你学完教程，你将使用 一个计算机视觉库 `OpenCV、PyTorch` 来构建一个深度神经网络和 `onnx` 来导出你的神经网络。

[面试初学者的完整的 Python 教程](https://www.youtube.com/watch?v=sxTmJE4k0ho) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（6h21min）

这个 `Python` 课程目标是在 `Python` 语言方面让你从初学者晋升为专家。这个 `Python` 课程会教你你需要知道的 `Python` 的一切。不需要前置知识，对于 `Python` 初学者来说是一个完美的教程。

[重新映射 Python 操作码](https://medium.com/tenable-techblog/remapping-python-opcodes-67d79586bfd5)

这篇文章将带你逐步了解作者是如何恢复重新映射编译 `Python` 操作码的源代码。

[如何使用 Python 3 中的 collections Module](https://davidmuller.github.io/posts/2020/05/08/collections-module-Python3.html)

在这篇教程中，我们将通过 `collections module` 中的三个类来帮你处理元组，字典以及列表。我们将使用 `nametuples` 来创建带有 `named` 字段的元组，`defaultdict ` 来简单在字典中进行分组，以及 `deque` 可以高效的将元素添加到类列表对象的两边。



[使用 Python 的 SQLite 数据库](https://www.youtube.com/watch?v=byHcYRpMgI4) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（1 h 29 min）

在这课程中你将学习到在 `Python` 使用 `SQLite3` 的基础知识。`SQLite` 是 `Python` 附带的一个非常使用使用的数据库。你将学习如何来创建数据库以及表，数据添加，数据排序，创建 `reports` ，提取特定数据等。

[如何使用 Django and Vue.js 实现一个 Web App 原型](https://www.sitepoint.com/web-app-prototype-django-vue/)

学习如何使用 `Django and Vue.js` 来创建一个自定义的，响应快的，反应灵敏的 `web` 应用原型，并使用一个功能完整的后台网站来管理内容。

[使用 Markdown 和 Python 库 Pelican 来创建和部署一个静态站点](https://shahayush.com/2020/03/web-pelican-intro/)

了解如何使用 `markdown and the Python library pelican` 不要任何 `HTML and CSS` 能力来创建你的静态站点。

[理解 K-近邻 (KNN) 算法的基本原理](https://heartbeat.fritz.ai/understand-the-fundamentals-of-the-k-nearest-neighbors-knn-algorithm-533dc0c2f45a)

介绍著名的机器学习算法 `KNN` 使用 `scikit-learn`。

[Plasma: 基于 Jupyter 的一个学习平台](https://blog.jupyter.org/plasma-a-learning-platform-powered-by-jupyter-1b850fcd8624)

[用于模拟吉他效果的深度学习](https://teddykoker.com/2020/05/deep-learning-for-guitar-effect-emulation/)

[讨论中: Python 的性能](https://www.welcometothejungle.com/en/articles/btc-performance-python)

[Using FastAPI with Django](https://www.stavros.io/posts/fastapi-with-django/)

[用自定义参数修补 HTTP 请求的钩子](https://seds.nl/posts/http-hooks-with-custom-arguments/)

[用于展示桌面提醒的 HTTP 服务](https://julienharbulot.com/notification-server.html)

[用 CircuitPython and AWS Lambda 构建一个无服务的 Martian 天气展示](https://aws.amazon.com/blogs/compute/build-a-serverless-martian-weather-display-with-circuitpython-and-aws-lambda/)

[利用 NVIDIA Tensor Cores and TensorFlow 2 来加速医学图像分割](https://devblogs.nvidia.com/accelerating-medical-image-segmentation-tensor-cores-tensorflow-2/)

[Using Rust to Power Python Importing With oxidized_importer](https://gregoryszorc.com/blog/2020/05/10/using-rust-to-power-python-importing-with-oxidized_importer/)



### 有趣的项目、工具和库

[MicroscoPy](https://github.com/IBM/MicroscoPy)

一个利用 `LEGO` 积木， `Arduino, Raspberry and 3D printing` 的开源，电动，模块化的显微镜。

[ar-cutpaste](https://github.com/cyrildiagne/ar-cutpaste)
使用 `AR· 剪切并粘贴您的周围环境。

[this-word-does-not-exist](https://github.com/turtlesoupy/this-word-does-not-exist)

这是一个允许人们训练 `GPT-2` 变体的项目，它从零开始组成单词、定义和例子。

[fastpages](https://github.com/fastai/fastpages)

一个易于使用的博客平台，增强了对 `Jupyter Notebooks` 的支持。它通过 `GitHub Actions`自动创建博客文章的过程，所以你不必再大惊小怪地使用转换脚本。

[AI-basketball-analysis](https://github.com/chonyy/AI-basketball-analysis)

基于目标检测概念的人工智能应用。通过挖掘从物体检测中收集的数据来分析篮球投篮。

[spycheck-linux](https://github.com/BjornRuytenberg/spycheck-linux)
验证您的支持 `Thunderbolt` 的 `Linux` 系统是否容易受到 `Thunderspy` 攻击。

[xxh](https://github.com/xxh/xxh)
无论你走到哪里，都带上你最喜欢的 `shell`。

[slack-watchman](https://github.com/PaperMtn/slack-watchman)

监控你的 `Slack` 工作空间来获取敏感信息。

[open_lth](https://github.com/facebookresearch/open_lth)
为开源彩票假设代码做准备的存储库。

[AxCell](https://github.com/paperswithcode/axcell)

从报纸中提取表格和文本的工具。

[senator-filings](https://github.com/neelsomani/senator-filings)
抓取美国参议员的买入+卖出单的公开文件，计算出他们的回报。

[timeglass](https://github.com/mountwebs/timeglass)
简单而不显眼的菜单栏定时器，适用于macOS。

[pandas_alive](https://github.com/JackMcKew/pandas_alive)
使用 `Matplotlib` 对 `Pandas` 进行动画绘图扩展。

[pyp](https://github.com/hauntsaninja/pyp)
轻松运行 `Python` 在 `shell` 上运行! 神奇，但绝不神秘。

[sheet2api-python](https://github.com/odwyersoftware/sheet2api-python/)
Google/Excel Sheets API Python.

[DataGene](https://github.com/firmai/datagene) 
识别数据集的相似性。

[Fluent](https://github.com/breitburg/fluent)
`Fluent` 让您轻松、快速地构建美丽的移动应用。



### 最近更新

[Python in Visual Studio Code – May 2020 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-may-2020-release/)
在这个版本中，我们解决了42个问题，它包括了在选择时浏览或输入解释器路径的能力。你可以在修改日志中查看完整的改进列表。

### 那些活动

[Virtual: Wagtail Space US 2020](https://us.wagtail.space/)
实际上，今年我们将举行我们的会议！我们期待在几周内启动我们的征集提案活动，并在 7 月的第一周宣布我们的日程安排。`Wagtail Space US` 将包括会谈、训练和冲刺。

[Virtual: PyData Madison Meetup May 2020](https://www.meetup.com/PyData-Madison/events/270204693/)
会有一个使用 `mybinder` 的演示。`Mybinder` 可以让你把你的 `jupyter` 笔记本变成一个环境，你可以在任何地方的任何机器上运行，并安装了所有的依赖性软件。

[Virtual: Oops! I’ve Just Spent the Entire AWS Budget](https://www.meetup.com/PyData-Edinburgh/events/270582907/)
本讲座记录了演讲者在为一家度假公司开发一个仪表盘应用程序期间的个人发展。它包括了导致最终设计的关键决策（和错误）和障碍。这个旅程从零数据科学知识、零R知识的和零云计算知识开始。它强调了在应用从概念到原型，再到最终商业交付的过程中，所需要的数据安全和云架构的关键领域。


#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-449.html)
- 改进: [issue-449.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23449.md)

