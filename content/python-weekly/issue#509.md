Title: pythonista-weekly : Pyw 509
Date: 2021-07-23 16:11
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-509

### 欢迎阅读《pythonista周刊》第509期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-509](https://mailchi.mp/pythonweekly/python-weekly-issue-509)  
>翻译：Dustyposa

### 文章、教程与话题

[Python中最重要的3个傅里叶变换](https://www.youtube.com/watch?v=GKsCWivmlHg) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
本视频深入研究了 `sympy` 和 `scipy` 库，以了解 `python` 中的傅里叶分析，并具体研究了1.傅里叶变换，2.傅里叶数列，以及3.离散傅里叶变换。离散傅里叶变换。

[用AlphaFold进行高精度的蛋白质结构预测](https://www.nature.com/articles/s41586-021-03819-2_reference.pdf)
Nature 杂志发表了 `AlphaFold` 的最新情况，这是一种采用机器学习的计算方法，用于高精确度地预测全链蛋白质结构。

[Beautiful ideas in programming: generators and continuations](https://www.hhyu.org/posts/generator_and_continuation/)
这篇文章总结了作者在尝试深入理解编程中的两个重要概念时的心得。`Python` 的生成器和 `Scheme` 的 `continuation`。

[namedtuple in a post-dataclasses world](https://death.andgravity.com/namedtuples)
`namedtuple` 已经存在了很久，随着时间的推移，它的便利性使它的使用远远超出了它最初的目的。随着数据类现在覆盖了这些用例的一部分，人们应该把 `namedtuple` 用于什么？在这篇文章中，我们将通过几个真实代码的例子来看看这个问题。

[使用Django的指南（第二部分）。GeoDjango、PostGIS和Leaflet](https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/)
一个快速入门指南，使用基于 `Python` 的网络框架 `Django` 创建一个网络地图，使用其模块 `GeoDjango`，`PostgreSQL` 数据库及其空间扩展 `PostGIS` 和 `Leaflet`，一个用于互动地图的 `JavaScript` 库。

[Monitor your home's temperature and humidity with Raspberry Pis and Prometheus](https://opensource.com/article/21/7/home-temperature-raspberry-pi-prometheus)
在 `Raspberry Pi` 上用 `Python` 测试一个 `Prometheus` 应用程序，收集温度传感器数据。

[Making Sense Of Settings](https://www.mattlayman.com/understand-django/settings/)
所有的 `Django` 应用程序都需要进行配置，以便正常运行。在这篇文章中，我们将深入探讨 `Django` 如何让您使用设置模块来配置您的项目。我们还将探讨如何更有效地使用设置。

[Complete Glossary of Keras Neural Network Layers (with Code)](https://analyticsarora.com/complete-glossary-of-keras-neural-network-layers-with-code)
Learn the purpose and instantiation for Core layers, Pooling layers, Preprocessing layers, etc.

### 有趣的项目、工具和库

[AlphaFold](https://github.com/deepmind/alphafold)
这个包提供了 `AlphaFold v2.0` 推理管道的实现。

[MVT](https://github.com/mvt-project/mvt)
`MVT` 是一个寻找智能手机设备感染迹象的取证工具。

[MaskFormer](https://github.com/facebookresearch/MaskFormer)
Per-Pixel Classification is Not All You Need for Semantic Segmentation.

[shillelagh](https://github.com/betodealmeida/shillelagh/)
使得通过 `SQL` 查询 `API` 变得容易。

[Chameleon](https://github.com/klezVirus/chameleon) 
`Chameleon` 是另一个 `PowerShell` 混淆工具，旨在绕过 `AMSI` 和商业反病毒解决方案。

[Parallelformers](https://github.com/tunib-ai/parallelformers)
一个高效的模型平行化部署工具包。

[PIX](https://github.com/deepmind/dm_pix)
`PIX` 是一个 `JAX` 中的图像处理库，用于 `JAX`。

[byp4xx](https://github.com/lobuhi/byp4xx)
用于绕过 `HTTP 40X` 响应的 `Pyhton` 脚本。特点。动词篡改、头文件、#bugbountytips技巧和2454用户代理。

[Multimerge](https://github.com/sweeneyde/multimerge)
`Multimerge` 是一个 `Python` 包，它实现了一种算法，可以将几个排序的迭代器懒散地组合成一个较长的排序迭代器。它是 `Python` 标准库中 `heapq.merge` 的一个直接替代。

[CodeGen](https://github.com/facebookresearch/CodeGen)
来自 `Facebook AI Research` 的代码生成项目的参考实现。将机器学习应用于代码的通用工具箱，从数据集创建到模型训练和评估。配有预训练的模型。

[Muler](https://github.com/PizzaMyHeart/muler)
用 `Flask` 建立的一个药物信息搜索引擎。

### 最近更新


[Python in Visual Studio Code – July 2021 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-july-2021-release/)
这些是该版本中引入的一些值得注意的变化。

- A faster way to configure project roots via a new Pylance quick fix
- Selecting a Python interpreter no longer changes settings
- New debugger features: step into targets and function breakpoints

### 活动

[Virtual: Scale EDA & ML Workloads To Clusters & Back With Dask](https://www.meetup.com/PyData-Calgary/events/279465823/)
在本次演讲中，您将学习如何使用 `Dask` 以最小的代码改动来扩展您的 `PyData` 工作负载，这样您就可以专注于您的工作而不必学习新的 `API`。

[Virtual: Machine Learning and its Potential to Improve Epilepsy Diagnosis](https://www.meetup.com/PyData-Edinburgh/events/279576429/)
本讲座概述了 `ML` 的新应用如何能很快为生理学家提供更好的定量工具，以改善工作流程和诊断的准确性。

[Virtual: PyData Berlin & PyData Hamburg July 2021 Meetup](https://www.meetup.com/PyData-Berlin/events/279302584/)
将会有以下话题:

- AI based visual assistance system
- Introducing Elyra: Extending JupyterLab for AI


Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果您发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-509.html)
- 改进: [issue-509.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23509.md)

