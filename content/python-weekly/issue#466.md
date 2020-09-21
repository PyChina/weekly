Title: pythonista-weekly : Pyw 466
Date: 2020-09-18 16:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-466

### 欢迎阅读《pythonista周刊》第466期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-466](https://mailchi.mp/pythonweekly/python-weekly-issue-466)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
[Ray Summit: Scalable Python & ML for everyone](https://events.linuxfoundation.org/ray-summit/?utm_source=pythonweekly&utm_medium=newsletter&utm_campaign=raysummit&utm_content=sep17)
See how Ray, the open-source Python framework, is used for building distributed apps & libraries, including backend infrastructures & ML platforms. Connect with the Ray community and learn to build any application at any scale at [Ray Summit—it's free.](https://events.linuxfoundation.org/ray-summit/?utm_source=pythonweekly&utm_medium=newsletter&utm_campaign=raysummit&utm_content=sep17)

### 新闻

[All Python versions less than 3.6 are now EOL](https://devguide.python.org/#status-of-python-branches)

### 文章、教程与话题

[如何使用Django 3构建一个简单的Hacker News克隆体](https://www.youtube.com/watch?v=292GB6snFYo) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（1h20min）
该 `Django` 教程将向你展示如何使用 `Django 3` 构建简单的 `Hacker News` 克隆。它将首先建立一个虚拟环境以供使用，然后逐步构建项目。

[用 NumPy 做 Array 编程](https://www.nature.com/articles/s41586-020-2649-2)
讨论了 `NumPy` 的最新论文，该论文回顾了其基本概念，并探讨了其如何在日益专业化的计算库之间演变为灵活的互操作性层。

[在从Python调用C / C ++的幕后](https://azhpushkin.me/posts/python-c-under-the-hood)
遍历 `ctypes，libffi`，二进制扩展以及支持 `CPython` 和 `C` 无缝互操作性的其他工具的内部。

[Django 及其默认值](https://t.co/Q1u2MgOl1R)
关于 `Django` 常见陷阱的小故事。

[实时车牌识别系统](https://github.com/cortexlabs/cortex/tree/master/examples/tensorflow/license-plate-reader)
了解如何实施车牌识别系统。 在资源受限的系统上，运行推断可能证明在计算上过于昂贵。 一种解决方案是在云中运行 `ML` ，并使本地（嵌入式）系统充当这些服务的客户端。

[跨计算机的防火墙禁止共享](https://chown.me/blog/acacia)
如何在多台计算机上同时阻止一个 `IP`？

[在30分钟内使用数据访问控制构建Django应用](https://www.osohq.com/post/django-access-control)
在本文中，我们将探讨如何构建一个简单的社交应用程序，该应用程序允许用户共享 `Twitter` 等帖子。 与 `Twitter` 不同，我们的应用程序将包含帖子可见性控制。 我们将使用 `oso` 实现此访问控制，`oso` 是嵌入在您的应用程序中的开源策略引擎。 `django-oso` 包使您无需进行任何配置即可在 `Django` 应用中使用oso。

[Reading HTML tables with Pandas](https://pbpython.com/pandas-html-table.html)
本文介绍如何从 `Wikipedia` 或其他站点读取 `HTML` 表并将它们转换为 `pandas DataFrames` 进行进一步分析。 

[使用Python教程自动化Excel](https://www.youtube.com/watch?v=YwIX8w9i2DM) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（7min）
这个视频向你展示了一些方法，通过这些方法你可以自动化你的excel工作簿。它向你展示了我们如何有效地利用它们来检索信息，合并、搜索和过滤数据，以及在 `excel` 中进行计算操作。

[U-Net: 60行代码中的PyTorch实现方法](https://amaarora.github.io/2020/09/13/unet.html)

[PyConline AU 2020 Videos](https://www.youtube.com/playlist?list=PLs4CJRBY5F1IEFq-wumrBDRCu2EqkpY-R)

[Searching for RH Counterexamples — Setting up Pytest](https://jeremykun.com/2020/09/11/searching-for-rh-counterexamples-setting-up-pytest/)

[使用Python、Django、React和Docker构建一个完全生产就绪的机器学习应用。](https://t.co/Engyzm30Nc)

[在Python中进行面向数据的编程](https://www.moderndescartes.com/essays/data_oriented_python/)

[忽略所有的网络性能基准，包括这个基准](https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one)



### 有趣的项目、工具和库

[Eiten](https://github.com/tradytics/eiten) 
`Eiten` 是一个实现各种统计和算法投资策略的工具包，如 `Eigen Portfolios、Minimum Variance Portfolios、Maximum Sharpe Ratio Portfolios` 和基于遗传算法的 `Portfolios`。

[VizTracer](https://github.com/gaogaotiantian/viztracer) 
`VizTracer` 是一个低开销的日志/调试/分析工具，它可以跟踪和可视化你的 `python` 代码执行。

[jupyter-text2code](https://github.com/deepklarity/jupyter-text2code)
一个概念验证的 `jupyter` 扩展，可以将英文查询转换为相关的 `python` 代码。

[freki](https://github.com/crhenr/freki)
`Freki` 是一个免费的、开源的恶意软件分析平台。

[kb](https://github.com/gnebbia/kb)
一个最简约的知识库管理器

[Lucid](https://github.com/gaasedelen/lucid) 
一个交互式的十六进制微码浏览器。

[rororo](https://github.com/playpauseandstop/rororo)
用 `schema first` 的方法实现 `aiohttp.web OpenAPI 3` 服务器应用。

[jazzit](https://github.com/sangarshanan/jazzit)
你想过你的 `Python` 脚本在运行/出错时播放音乐吗？有了 `Jazzit`，你只需在你的函数中添加一个装饰器，就可以让它变得更炫。

[Hfinger](https://github.com/CERT-Polska/hfinger) 
恶意软件 `HTTP` 请求的指纹识别工具。基于 `Tshark`，用 `Python3` 编写。 

[pytorch_block_sparse](https://github.com/huggingface/pytorch_block_sparse)
Fast Block Sparse Matrices for Pytorch.

### 新活动

[Virtual: PyCon Turkey 2020](https://tr.pycon.org/) 
PyCon土耳其2020不仅仅是一个演讲和演示的流。除了两个轨道的演讲外，你还将有机会向演讲者提问，会见我们的赞助商，并与其他与会者进行随机聊天。

[Virtual: PyBerlin 20 - Autumn event](https://www.meetup.com/PyBerlin/events/272532025/)
将会有以下话题"

- 如何避免成为一个10倍的工程师
- Sets and Frozen Sets


[Virtual: PyData Hamburg September Meetup](https://www.meetup.com/PyData-Hamburg/events/272638097/)
将会有以下的话题:

- 为什么AI行业需要一个版本控制图数据库
- Writing production-level Machine Learning code from the gecko with least effort

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-466.html)
- 改进: [issue-466.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23466.md)

