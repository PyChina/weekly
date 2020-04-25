Title: pythonista-weekly : Pyw 446
Date: 2020-04-25 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-446

### 欢迎阅读《pythonista周刊》第446期。Let us start!

>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-446](https://mailchi.mp/pythonweekly/python-weekly-issue-446)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[来免费试用 14 天吧！](https://www.datadoghq.com/dg/apm/python-troubleshooting/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Troubleshooting)

### 文章、教程与话题

[我是如何做出一个怎么投篮都能进的篮框的？](https://www.youtube.com/watch?v=vtN4tkvcBMA) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(22min)
想象一下，投了一个球，如果球撞到了篮板，就会莫名其妙的直接进到篮筐里。由于物理原因，尽管你可以使球更多地进入篮筐，但是不可能使所有可能的投篮都能进。这个视频向你展示了如何编写一个程序来计算光学背板然后进行加工制作。
>  百发百中不是梦。

[在 Rust 代码中编写 Python 代码 — 第一部分](https://blog.m-ou.se/writing-python-inside-rust-1/)
大约一年前，我发布了一个叫 `inline-python` 的 `Rust create`，允许你使用 `python!{ .. }` 宏很轻松的在你的 `Rust` 代码中混入一些 `Python` 代码。在这个章节中，我将从零开始讲述这个 `create` 的开发过程。

- [Part 1A](https://blog.m-ou.se/writing-python-inside-rust-1a/) - 在第二部分继续扩展我们的 `python!{}` 宏之前，我们先详细探讨一些事情。
>  混入代码，想敲什么敲什么。

[Python的上下文管理器的新奇案例](https://rednafi.github.io/digressions/python/2020/03/26/python-contextmanager.html)
发现Python的上下文管理器的新奇之处。

[用 Python 做数据分析 - 初学者的全套课程(Numpy, Pandas, Matplotlib, Seaborn)](https://www.youtube.com/watch?v=r-uOLxNrNk8) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(4h22min)
在这篇针对初学者的综合教程中学习 `Python` 的数据分析，并包含了练习题! 在这篇教程中，你将学习到数据分析的整个过程：从各种数据源（CSVs、SQL、Excel等等）中读取数据，用 `NumPy and Pandas` 处理它们，使用 `Matplotlib and Seaborn` 对它们进行可视化，并进行清理处理来创建报告。此外，我们还包含了一个 `Jupyter Notebook` 的教程，以及一个快速的 `Python` 参考来刷新你的编程能力。

[使用Python协程构建有限状态机](https://arpitbhayani.me/blogs/fsm)
构建和实现有限状态机最直观的方式便是使用 `Python` 协程，在本文中，我们会了解如何做，以及为什么。


[在 PyTorch 中建立端到端语音识别模型](https://www.assemblyai.com/blog/end-to-end-speech-recognition-pytorch)
让我们来看看如何在 `PyTorch` 中构建自己的端到端语音识别模型。我们要建立的模型是受 `Deep Speech 2` 的启发（百度对他们现在著名的模型进行了二次改版），在架构上做了一些个人的改进。模型的输出将是一个字符的概率矩阵，我们会使用概率矩阵来解码音频中最有可能说出的字符。

[浏览器中的 Python | Brython 速成教程](https://www.youtube.com/watch?v=VJj-H4we71g) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(35min)
在这个视频中，我们将用浏览器中的 `Python` 和 `Brython` 来操作 `DOM、使用本地存储、创建 Ajax 调用等等`。
> 用 Python 完成 js 的功能，不想写 js？ 来这里看看吧

[解密 Python 的描述符协议](https://deepsource.io/blog/demystifying-python-descriptor-protocol/)
描述符协议攻略，用于理解 `properpy、classmethod、statocmethod` 的工作原理。

[safer: a safer file writer](https://t.co/EuqMd3i29N)
本文不仅描述了一个仅执行一项基本任务的小型库，还描述了它如何从某个项目中的谦虚实用程序转变为稍微不那么谦虚的生产库的一些背景故事。

[使用 Python 动态地图 COVID-19 的发展过程](https://www.youtube.com/watch?v=vLEA8dCfusQ) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(49min)
在这篇教程中，你将学习如何使用 `GeoPandas and Pandas Python` 库，利用世界各地的 `Coronavirus` 感染时间序列数据创建一个动态地图。时间序列数据来自 `Johns Hopkins CSSE` 的 `2019` 年新型冠状病毒 `COVID-19（2019-nCoV）` 数据存储库。

[在 Django 中使用 Webpack](https://pascalw.me/blog/2020/04/19/webpack-django.html)
如何在 `Django` 中设置 `Webpack`，使用 `Django static and Webpack` 不用插件就能将它们连在一起，

[Ensemble Modeling - Bagging](https://michael-fuchs-python.netlify.app/2020/03/07/ensemble-modeling-bagging/)
集成学习是一种机器学习范式，在这个范式中，多个模型（也被称为”弱学习者“）被训练来解决同一个问题并结合在一起来取得更好的结果。这里有三种最常见的组合方式：`+ Bagging + Boosting + Stacking`。在这篇文章中，我们将从 `bagging` 开始，转而再到独立的 `publications` 中进行 `boosting and stacking`。

[用 Docker 连接  Flask and Nginx](https://www.youtube.com/watch?v=Vkqz2hK4fKg) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(13min)
这个视频将介绍用 `docker-compose` 来连接 `nginx` 容器和 `flask应用` 容器。
>  遵循容器单进程模型～

[如何使用 Python 抓取你贡献过的 GitHub Organizaitons](https://florian-dahlitz.de/blog/scrape-github-orgs-using-python)
带有真实世界案例的抓取教程。
>  实战操作

[使用静态分析生成 Robust Jupyter 报告](https://ploomber.io/posts/nb-static-analysis/)

[不用 setup.py 进行打包](https://pgjones.dev/blog/packaging-without-setup-py-2020/)

[More fun with NumPy, CuPy, Clojure and GPU acceleration. Hold my Cider 2!](https://dragan.rocks/articles/20/Clojure-Numpy-Cupy-CPU-GPU-2)

[有坚固基础的构建：确保可重复的Docker构建适用于Python](https://pythonspeed.com/articles/reproducible-docker-builds-python/)

[ ndindex 简介, 用于操作 ndarray 索引的 Python 库](https://labs.quansight.org/blog/2020/04/introducing-ndindex-a-python-library-for-manipulating-indices-of-ndarrays/)





### 有趣的项目、工具和库

[MONAI](https://github.com/Project-MONAI/MONAI) 
`MONAI` 是一个免费提供的、由社区支持的、基于 `PyTorch` 的深度学习框架，用于医疗成像领域的深度学习。它为在原生 `PyTorch` 范式中开发医疗影像培训工作流程提供了领域优化的基础能力。

[PyBoy](https://github.com/Baekalfen/PyBoy)
用 `Python` 编写的 `Game Boy` 模拟器。

[hexapod-robot-simulator](https://github.com/mithi/hexapod-robot-simulator)
一个简单的基于浏览器的六足机器人模拟器，是基于第一原理构建的。
> 真 六足机器人 还会自己摇摆！

[tauthon](https://github.com/naftaliharris/tauthon)
`Python 2.7 ` 的 `Fork`，带有新的语法、内建库和从 `Python 3` 中移植过来的库。

[Django Template Tags and Filters](https://www.djangotemplatetagsandfilters.com/)
一个网站，提供了关于 `Django` 的 `57` 个内置模板过滤器和 `27` 个内置模板标签的有用文档。虽然官方的文档非常好，但我们试图以更有意义的方式组织这些标签和过滤器，并让用户更好地了解如何使用、是否使用和何时使用每一个标签。
> 可以作为模版的快速学习教程了。

[DenseDepth](https://github.com/ialhashim/DenseDepth)
通过转移学习进行高质量的单眼深度估计。

[Downloads-organizer](https://github.com/JanB0/Downloads-organizer)
一个 `Python` 脚本，根据文件扩展名来组织一个像 `Download` 这样的文件夹。

[cheekymonkey](https://github.com/richstokes/cheekymonkey)
Literally a Chaos Monkey for your Kubernetes clusters.

[clikan](https://github.com/kitplummer/clikan)
clikan 是一个运行在 `CLI` 中的超级简单的个人看板仪表。

[QuickSQL](https://github.com/trustedsec/quicksql)
`QuickSQL` 是一个简单的 `MSSQL` 查询工具，允许你连接到 `MSSQL` 数据库，不需要管理级别的权限就能使用。

[bird-bot](https://github.com/natewong1313/bird-bot)
一个任天堂 `Switch` 的结账机器人。目前支持沃尔玛和百思买
> Nintendo 也要霸榜了。

[MyHandWriting](https://github.com/bannyvishwas2020/MyhandWriting)
将文本转换为你自己的手写字。

[Flpc](https://github.com/asrp/flpc)
`Forth Lisp Python Continuum`: 一种小型的高度动态的自引导语言。

[covid19_dashboard](https://github.com/Unicorndy/covid19_dashboard)
Covid19 Dashboard Web App using Python (Plotly Dash).

[TorchServe](https://github.com/pytorch/serve)
`TorchServe` 是一个灵活且易于使用的工具，用于为 `PyTorch` 模型提供服务。

### 最近更新

[pip 20.1b1 beta release](https://discuss.python.org/t/announcement-pip-20-1b1-beta-release/3960)
此次发布的要点是:

- 在构建本地目录时，通过改变行为来执行就地构建，而不是复制到临时目录，显著提高了速度。
- `pip` 列表中的显著加速——通过并行网络访问过时了。这是 `pip` 代码库中的第一个并行代码实例。
- 新的 `pip` 缓存命令，可以对 `pip` 的缓存目录进行内省和管理。
- 通过 `PEP 610` 的实现，更好地冻结了从直接 `URL` 安装的包的 `pip` 冻结。


[PyTorch 1.5](https://t.co/0DlxDEQQsP)
该版本有几个主要的新 `API` 添加和改进，包括对 `C++` 前端的重大更新，计算机视觉模型的 `Channel Last` 内存格式，以及用于模型并行训练的分布式 `RPC` 框架的稳定发布。

[Python in Visual Studio Code – April 2020 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-april-2020-release/)
这是一个简短的版本，我们解决了 `43` 个问题，包括 `Jypyter Notebooks` 中的 `ipywidgets` 支持和 `Django` 和 `Flask` 自动加载的调试器支持。你可以在我们的更新日志中查看完整的改进列表。

[Python 2.7.18, the last release of Python 2](https://blog.python.org/2020/04/python-2718-last-release-of-python-2.html)



### 那些活动

[Virtual: Hack the Virus](https://hackthevirus.splashthat.com/)
一个由开发者和设计师与医学界专家以及其他在抗击冠状病毒前线的专家组成的黑客马拉松。

[Virtual: SciPy 2020](https://www.scipy2020.scipy.org/) 
`SciPy 2020` 是第19届科学计算与Python年会，将于 `2020年7月6日` 至 `12日` 举行的虚拟会议。一年一度的 `SciPy` 会议允许来自各类组织的与会者展示他们的最新项目，向熟练的用户和开发者学习，并在代码开发方面进行合作。 

[Virtual: Python Web Conference 2020](https://2020.pythonwebconf.com/)
第二届 `Python Web` 大会是一个虚拟的活动，国际技术专家将就微服务、身份管理、机器学习和CI/CD等40个主题进行演讲。讲座分为3个精彩的轨道。每个频道都可以通过 `Zoom` 进行直播，与会者可以通过 `Slack` 渠道进行聊天。演讲和会后录音将只提供给注册参会者。

[Virtual: PyData Lancaster Meetup April 2020](https://www.meetup.com/PyData-Lancaster/events/270006544/) 
There will be a talk, Changepoints to Improve Forecasts (Estimation Window Selection for A&E Arrivals Forecasts)



#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-446.html)
- 改进: [issue-446.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23446.md)

