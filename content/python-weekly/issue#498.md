Title: pythonista-weekly : Pyw 498
Date: 2021-05-7 16:25
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-498

### 欢迎阅读《pythonista周刊》第498期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-498](https://mailchi.mp/pythonweekly/python-weekly-issue-498)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**

[Get Your Weekly Dose of Programming](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)
A weekly newsletter featuring the best hand curated news, articles, tutorials, talks, tools and libraries etc for programmers. [Join For Free](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)

### 新闻


[The new TI-84 Plus CE Python graphing calculator](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-plus-ce-python)
`TI-84 Plus CE` 的一切你所知道和喜爱的，现在有了 `Python` 的助力。向学生介绍使用 `TI` 技术用 `Python` 进行编码。2021年秋季上市。

[Python also impacted by critical IP address validation vulnerability](https://www.bleepingcomputer.com/news/security/python-also-impacted-by-critical-ip-address-validation-vulnerability/)
`Python` 标准库 `ipaddress` 也存在严重的 `IP` 地址验证漏洞，与今年早些时候 "`netmask` "库中报告的漏洞相同。发现 `netmask` 关键漏洞的研究人员也在这个 `Python` 模块中发现了同样的漏洞，并获得了一个漏洞标识符。`CVE-2021-29921`。由于 `Python` 维护者在 `2019` 年的一次修改，这个回归漏洞悄然进入 `Python 3.x` 的 `ipaddress` 模块。 

[宣布六项Python科学资助项目](https://pyfound.blogspot.com/2021/04/announcing-six-scientific-python-grants.html)
`Python` 科学工作组考虑为推动 `Python` 的科学应用的提案提供资金。我们最近的提案征集已经结束，我们很高兴地宣布了六项资助。

### 文章、教程与话题

[Finding the magnetic field of any wire using python](https://www.youtube.com/watch?v=srk2YZKMn-E) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
学习如何使用 `numpy`、`scipy` 和 `sympy` 的组合来求解任何形状或大小的载流导线的磁场，只要它们可以被参数化。所有的符号数学都是在 `sympy` 中完成的，所以不需要用纸或笔。

[Multi-Tenancy in Django](https://www.viget.com/articles/multi-tenancy-in-django/)
以下是我们如何在最近的 `Python/Django` 应用构建中实现多租户的。这篇文章描述了我们的方法，分享了一些代码，并将其与我们使用不同方法的早期项目进行了比较。

[A Hitchhiker's Guide to SQLite with Python](https://arctype.com/blog/hitchhikers-guide-sqlite-python/)
为了探索 `SQLite` 和 `Python`，我们将建立一个简单的井字游戏。所以，系好安全带，准备好你的机器吧!

[OpenCV Tutorial - Develop Computer Vision Apps in the Cloud With Python](https://www.youtube.com/watch?v=iXNsAYOTzgM) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
学习如何用 `Python` 在云中使用 `OpenCV`。`OpenCV` 是一个主要针对实时计算机视觉的编程函数库。你将学习如何在 `Google Colab` 的云端创建计算机视觉应用。你将使用人工智能和机器学习。

[Idiomatic sequence slicing](https://mathspp.com/blog/pydonts/idiomatic-sequence-slicing)
本文涵盖了 `Python` 中序列切片的基础知识，并教给你一些习惯性的切片模式，以编写更优雅的代码。

[PyTorch Developer Podcast](https://pytorch-dev-podcast.simplecast.com/) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/9a9a57d0-eb4b-47f8-8af4-55ba50e8c350.png)
`PyTorch` 开发者播客是 `PyTorch` 开发团队就 `PyTorch` 的各种内部开发主题进行一口大小（10-20分钟）讨论的地方。

[Deploy MLflow with Bodywork](https://www.bodyworkml.com/posts/deploy-mlflow-with-bodywork)
虽然 `Bodywork` 专注于部署机器学习项目，但它的灵活性足以部署几乎任何类型的 `Python` 项目。我们将通过使用 `Bodywork` 在短短几分钟内将 `MLflow`（一个 `Flask` 应用）的生产就绪实例部署到 `Kubernetes` 来证明这一点。

[Why isn't Flask async](https://www.youtube.com/watch?v=bw1qeMoFBmw) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
本讲座将讨论过去在 `Flask` 中支持 `async/await` 的方法，他们在哪些方面遇到了困难，以及普遍存在的挑战。然后，它将展示如何从 `Django` 获得灵感，在即将发布的 `Flask-2.0` 中引入支持。

[Clustergam: visualisation of cluster analysis](https://martinfleischmann.net/clustergam-visualisation-of-cluster-analysis/)
这篇文章介绍了一个新的 `Python` 包，用于从聚类解决方案中生成 `clustergrams`。它与 `scikit-learn` 和 `GPU` 支持的库兼容，如 `RAPIDS.AI` 中的 `cuML` 或 `cuDF`。让我们看看一些例子，以了解 `clustergram` 的外观和如何使用它。

[Python和恶意软件。在没有混淆的情况下开发隐蔽和规避的恶意软件](https://arxiv.org/pdf/2105.00565.pdf)

[Python C扩展的隐藏性能开销](https://pythonspeed.com/articles/python-extension-performance/)

[傅立叶变换是一个神经网络](https://sidsite.com/posts/fourier-nets/)

[Fluent in Django: Get to know Django models better](https://girlthatlovestocode.com/django-model)

[3 uses for functools.partial in Django](https://adamj.eu/tech/2021/05/05/3-uses-for-functools-partial-in-django/)

[如何使用ipywidgets来使你的Jupyter笔记本具有互动性](https://www.wrighters.io/use-ipywidgets-with-jupyter-notebooks/)

### 有趣的项目、工具和库

[cinder](https://github.com/facebookincubator/cinder)
Instagram's performance oriented fork of CPython.

[PDM](https://pdm.fming.dev/) 
`PDM` 是一个现代 `Python` 软件包管理器，支持 `PEP 582`。它以类似于 `npm` 的方式安装和管理软件包，完全不需要创建一个虚拟环境

[dino](https://github.com/facebookresearch/dino)
PyTorch code for Vision Transformers training with the Self-Supervised learning method DINO.

[nbsafety](https://github.com/nbsafety-project/nbsafety)
Fearless interactivity for Jupyter notebooks.

[aws-auto-inventory](https://github.com/aws-samples/aws-auto-inventory)
`AWS` 自动库存允许你快速、轻松地生成 `AWS` 资源的库存报告。 

[PyMongoArrow](https://pypi.org/project/pymongoarrow/) 
`PyMongoArrow` 是 `PyMongo` 的一个配套库，包含了将 `MongoDB` 查询结果集加载为 `Pandas DataFrames、NumPy` 数组或 `Apache Arrow` 表的工具。它还可以轻松生成 `parquet` 文件、`csv` 文件等。

[OSAS](https://github.com/adobe/OSAS)
One Stop Anomaly Shop: 异常检测采用两阶段方法。(a) 使用统计学、自然语言处理和静态规则进行预标记；(b) 使用监督和非监督机器学习进行异常评分。

### 最近更新


[Python 3.8.10, 3.9.5, and 3.10.0b1](https://pythoninsider.blogspot.com/2021/05/python-3810-395-and-3100b1-are-now.html) 

[Django security releases issued: 3.2.1, 3.1.9, and 2.2.21](https://www.djangoproject.com/weblog/2021/may/04/security-releases/)

### 活动

[Virtual: PyCon 2021](https://us.pycon.org/2021/)
使用和开发 `Python` 编程语言的社区的最大年度盛会。

[Virtual: Austin Python Meetup May 2021](https://www.meetup.com/austinpython/events/lgrbmqycchbqb/)
将会有以下话题:

- 用基于规则的模型讲可执行的故事
- Python与大流行病的较量：在短时间内编写高性能模型


[Virtual: PyLadies Dublin Meetup May 2021](https://www.meetup.com/PyLadiesDublin/events/277629790/)
将会有一个话题，使用 `SPARQL` 和  `DBPedia` 来抓取维基百科。

[Virtual: IndyPy Meetup May 2021](https://www.meetup.com/indypy/events/mbwlbsycchbpb/)
There will be a talk, Accessibility Awareness in Tech.

[Virtual: Cleveland Python Meetup May 2021](https://www.meetup.com/Cleveland-Area-Python-Interest-Group/events/fhqrtrycchbnb/)

Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-498.html)
- 改进: [issue-498.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23498.md)

