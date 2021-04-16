Title: pythonista-weekly : Pyw 495
Date: 2021-04-16 16:25
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-495

### 欢迎阅读《pythonista周刊》第495期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-495](https://mailchi.mp/pythonweekly/python-weekly-issue-495)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**

[REST APIs with Flask and Python](https://click.linksynergy.com/link?id=x9UsEHf2tls&offerid=507388.970600&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Frest-api-flask-and-python%2F)
Build professional REST APIs with Python, Flask, Flask-RESTful, and Flask-SQLAlchemy

### 新闻

[The PSF is hiring a Python Packaging Project Manager!](https://pyfound.blogspot.com/2021/04/the-psf-is-hiring-python-packaging.html)
Thanks to a two-year grant commitment from Bloomberg, our second 2021 Visionary Sponsor and a long term committed supporter of the Python ecosystem, The Python Software Foundation (PSF) is hiring a full-time project and community manager for the Python Packaging ecosystem, with a specific focus on the Python Package Index (PyPI).

[Unifying the CUDA Python Ecosystem](https://developer.nvidia.com/blog/unifying-the-cuda-python-ecosystem/)
到目前为止，通过 `Python` 访问 `CUDA` 和 `NVIDIA GPU` 只能通过第三方软件来实现，例如 `Numba、CuPy、Scikit-CUDA、RAPIDS、PyCUDA、PyTorch` 或 `TensorFlow` 等等。每个人都在 `CUDA API` 和 `Python` 之间写了自己的互操作层。通过发布 `CUDA  Python`，英伟达让这些平台提供商能够专注于自己的增值产品和服务。英伟达还希望降低其他 `Python` 开发者使用英伟达 `GPU` 的准入门槛。

### 文章、教程与话题

[一个人科技创业公司背后的架构](https://anthonynsimon.com/blog/one-man-saas-architecture/)
非常棒的一篇文章，从负载均衡刀任务监控及订阅，完全剖析了 `SaaS` 的背后。

[How I built a €25K Machine Learning Rig](https://www.emilwallner.com/p/ml-rig)
如何规划、购买、构建和存储你的2-10台 `GPU` 机器学习服务器和 `PC`。

[Porting VaccinateCA to Django](https://simonwillison.net/2021/Apr/12/porting-vaccinateca-to-django/)
最初，`VaccinateCA` 是由一个严重定制的 `Airtable` 实例驱动的，伴随着一个定制的 `JavaScript` 应用程序的调用者，通过一些 `Netlify` 函数与 `Airtable API` 通信。了解它是如何被移植到一个新的自定义 `Django` 后端，运行在 `PostgreSQL` 之上。 

[如何使用FastAPI抽象来查询AWS数据湖](https://hackernoon.com/how-to-use-a-fastapi-abstraction-to-query-aws-data-lake-4k3m35uq)
数据湖提供了无数的好处。它们是不可知的数据，不需要你预先定义一个模式。然而，如果没有一个合适的结构，要找到你需要的数据可能会很困难。在本文中，我们将通过创建一个 `FastAPI` 抽象来解决这个问题，使我们能够查询 `AWS Glue` 元数据目录。

[Python的dataclasses将为你节省时间，还具有attrs的特点](https://www.youtube.com/watch?v=vBH6GRJ1REM) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
在这个视频中，我们了解了数据类以及如何使用它们，以及数据类所基于的相关 `attrs` 库。

[Python Typing with mypy](https://t.co/zLx6DyRmMb)
大型代码库上的渐进式类型检查。

[Python 3 Types in the Wild: A Tale of Two Type Systems](https://www.cs.rpi.edu/~milanova/docs/dls2020.pdf)
本文探讨了开发者如何使用这些类型注释，类型检查和推理工具提供的类型系统语义，以及这些工具的性能。我们在 `GitHub` 公共仓库的语料库上评估了这些类型和工具。我们回顾了 `MyPy` 和 `PyType` 这两个典型的静态类型检查和推理工具，以及它们不同的类型分析方法。然后，我们讨论了三个研究问题。(i) 开发者使用 `Python 3` 类型的频率和方式是什么？(ii) 开发者会犯哪些类型错误？(三) 不同工具的类型错误如何比较？

[Integrating Rust into Python](https://www.vortexa.com/insight/integrating-rust-into-python)
这篇文章详细介绍了将 `Rust` 与 `Python` 集成的具体机制，以提高性能，而且不费吹灰之力。 

[Using PyTorch + NumPy? You're making a mistake.](https://tanelp.github.io/posts/a-bug-that-plagues-thousands-of-open-source-ml-projects/)
一个困扰着成千上万的开源 `ML` 项目的 `bug`。

[深度学习模型压缩](https://rachitsingh.com/deep-learning-model-compression/)
这篇文章涵盖了从2021年3月开始在广度和深度上的模型推理优化或压缩。这包括像模型量化和二值化这样的工程主题，像知识提炼这样的更面向研究的主题，以及众所周知的小技巧。

[如何使用Python创建像3Blue1Brown这样的数学动画](https://t.co/SSCIDe3qhI)
利用你的 `Python` 技能来创建美丽的数学动画。

[Python + AWS Lambda](https://www.youtube.com/playlist?list=PL0dOL8Z7pG3L4hi2SLJqojxshXNtsJQ_r) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
该系列将涵盖。编写一个 `Python` 脚本，从 `API` 中提取当前一天的天气情况，将脚本打包到 `Docker` 容器中，使用 `CI/CD` 自动将 `Docker` 容器推送到 `AWS` 上，在 `AWS Lambda` 上运行，安排 `AWS Lambda` 函数自动运行，编写基础设施 `YAML` 文件自动创建组件。 

[如何用Scikit-Learn构建机器学习流水线？又为何必不可少？](https://lifewithdata.com/2021/04/02/how-to-build-machine-learning-pipeline-with-scikit-learn-and-why-is-it-essential/)
在这篇文章中，你将了解什么是管道，如何使用 `scikit-learn` 管道？如何用流水线进行网格搜索和特征选择？如何用流水线进行列式变换？

[Raspberry Pi Pico上的MicroPython入门指南](https://www.makeuseof.com/getting-started-micropython-raspberry-pi-pico/)
`Pi` 基金会的第一个微控制器来了! 学习如何使用 `MicroPython` 对它进行编程。

[如何用Python和Telegram烹饪](https://www.youtube.com/watch?v=FYfX9Wn76_E) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
冰箱里有一些材料，但不知道做什么？有心情来一杯新的、有趣的鸡尾酒？我们将在这个手把手的 `python` 教程中把这些都构建成一个 `telegram` 机器人。

[在Python中编写机器视觉和天文相机的脚本](https://rk.edu.pl/en/scripting-machine-vision-and-astronomical-cameras-python/)

[[用多线程和Boto3从S3下载文件](https://emasquil.github.io/posts/multithreading-boto3/)

[用Go共享对象实现更快的Python (简单的方法)](https://blog.kchung.co/faster-python-with-go-shared-objects/)

[A Bot that Bird Watches so You Don’t Have To](https://t.co/OtU9TOnihS)

[通过阅读代码学习。Python标准库设计决策解读(适合高级初学者)](https://death.andgravity.com/stdlib)

### 有趣的项目、工具和库

[gProfiler](https://github.com/Granulate/gprofiler)
`gProfiler` 结合了多个采样剖析器，以统一的可视化方式显示 `CPU` 所花费的时间，显示本地程序、 `Java` 和 `Python` 运行时和内 核例程的进程堆栈记录。

[MMOCR](https://github.com/open-mmlab/mmocr) 
基于 `PyTorch` 和 `mmdetection` 的工具箱，用于文本检测、文本识别以及相应的下游任务，包括关键信息提取。

[SkinDeep](https://github.com/vijishmadhavan/SkinDeep)
使用深度学习去除纹身。

[Logica](https://logica.dev/) 
`Logica` 是一种逻辑编程语言，可以编译成 `StandardSQL`，并在 `Google BigQuery` 上运行。

[certomancer](https://github.com/MatthiasValvekens/certomancer)
使用简单的声明式配置快速构建、模拟和部署 `PKI` 测试配置，包括 `CRL、OCSP` 和时间戳服务配置。包括 `CRL、OCSP` 和时间戳服务供应。

[Rotten-Scripts](https://github.com/HarshCasper/Rotten-Scripts)
`Rotten Scripts` 包含了用 `Python`、`JavaScript`、`Bash`、`Powershell` 等编写的令人惊奇和赞叹的脚本。

[opal](https://github.com/authorizon/opal)
`OPAL` 是开放策略代理（`OPA`）的管理层，实时检测策略和策略数据的变化，并向代理推送实时更新。

[label-studio](https://github.com/heartexlabs/label-studio)
`Label Studio` 是一个开源的数据标签工具。它可以让你用简单直接的用户界面为音频、文本、图像、视频和时间序列等数据类型打上标签，并导出为各种模型格式。

[POT](https://github.com/PythonOT/POT)
一个为信号、图像处理和机器学习的最优传输相关优化问题提供若干解的库。

[layout-parser](https://github.com/Layout-Parser/layout-parser)
一个用于文档布局理解的 `Python` 库。 

[torchtyping](https://github.com/patrick-kidger/torchtyping)
`PyTorch Tensors` 的形状、`dtype` 等运行时类型注释。

[DivideAndScan](https://github.com/snovvcrash/DivideAndScan) 
分割全端口扫描结果，并将其用于有针对性的 `Nmap` 运行。

[omni](https://github.com/mattogodoy/omni)
一个非常轻量级的监控系统，用于运行 `Kubernetes` 的 `Raspberry Pi` 集群。

[jurigged](https://github.com/breuleux/jurigged)
对 `Python` 进行热重载

### 最近更新

[PyPy v7.3.4: release of Python 2.7 and 3.7](https://www.pypy.org/posts/2021/04/pypy-v734-release-of-python-27-and-37.html)

### 活动

[Virtual: PyBerlin 28](https://www.meetup.com/PyBerlin/events/277541034/) 
将会有一个讲座，`Retro Gamedev`：用 `Python` 制作自己的 `NES` 编译语言。

[Virtual: PyLadies Dublin Meetup April 2021](https://www.meetup.com/PyLadiesDublin/events/276397145/)
将会有以下话题:

- `NLP` 中的偏见：利用语言学和计算机科学来提高 `AI/ML` 的公平性。
- 用 `Python` 和 `Mako` 自动化社交媒体内容。


[Virtual: PyData Berlin Meetup April 2021](https://www.meetup.com/PyData-Berlin/events/277549703/)
将会有以下话题:

- How we task satellites to take pictures
- 如何检测ML模型中的沉默故障


[Virtual: PyData Montreal Meetup April 2021](https://www.meetup.com/PyData-MTL/events/277244278/)
将会有以下话题:

- `Pandas` 的文本扩展
- Introducing Elyra: Extending JupyterLab for AI


Posa：
> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-495.html)
- 改进: [issue-495.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23495.md)

