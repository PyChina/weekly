Title: pythonista-weekly : Pyw 478
Date: 2020-12-10 16:25
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-478

### 欢迎阅读《pythonista周刊》第478期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-478](https://mailchi.mp/pythonweekly/python-weekly-issue-478)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
Seamlessly correlate logs and traces at the level of individual requests, allowing you to quickly troubleshoot your Python application. Datadog's Continuous Profiler allows you to find the most resource-consuming parts in your production code all the time, at any scale. [Try it today with a free trial.](https://www.datadoghq.com/dg/apm/ts/profiler/continuous-profiling-ts/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-ProfilingTshirt)

### news

[Announcing PyCon US 2021](https://pycon.blogspot.com/2020/12/announcing-pycon-us-2021.html)
`PyCon US 2021` 将在原定的日期，即2021年5月12-15日进线上。Sprints将于2021年5月16-18日举行。

### 文章、教程与话题


[用Python从零开始构建云存储](https://lambdascheme.com/blocks.html)
想象一下，你的任务是建造 `Cinder` 。你会从哪里开始呢？构建一个你经常使用的系统的自己的版本，是丰富你对系统本身和一般系统设计原则的理解的好方法。对于那些像任何 `FAANG` 一样要去大型科技公司面试的人来说，这篇文章将遵循与面试中 "系统设计 "部分非常相似的流程，所以这是很好的实践。

[Exhaustiveness Checking with Mypy](https://hakibenita.com/python-mypy-exhaustive-checking)
在编译时失败，而不是在运行时。如果 `mypy` 能在 "编译时 "警告你可能出现的问题会怎样？本文分享了一个小技巧，让 `mypy` 在枚举类型中的一个值未被处理时失败。

[使用Python进行算法交易](https://www.youtube.com/watch?v=xfzGZB4HhEE) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
在这个完整的课程中学习如何使用 `Python` 进行算法交易。在学习了算法交易的基础知识后，你将学会如何建立三个算法交易项目。

[Building an Endless Spotify Playlist of the Greatest Albums of All Time](https://blog.seekwell.io/endless-spotify-playlist)
学习如何从滚石的500张历史最伟大的专辑列表中建立无限的 `Spotify` 播放列表。

[迁移Slack Airflow 到Python 3而不中断](https://slack.engineering/migrating-slack-airflow-to-python-3-without-disruption/)
这篇文章介绍了我们如何使用 `Celery` 队列将 `Apache Airflow` 基础架构和数百个 `DAG` 从 `Python 2` 转移到 `Python 3` 的更可靠的 "红黑 "部署中，从而使迁移对我们的用户完全透明。

[使用Python、Wav2Lip和Google Wavenet将视频翻译成任何语言](https://www.youtube.com/watch?v=DRXFcT48JqY) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
这段视频演示了如何使用一些真正具有突破性的人工智能，通过唇语同步，为你的视频生成30多种语言的逼真语音翻译。

[使用Django制作地图（第一部分）。GeoDjango、SpatiaLite和Leaflet](https://www.paulox.net/2020/12/08/maps-with-django-part-1-geodjango-spatialite-and-leaflet/)
使用 `Django` 模块 `GeoDjango、SQLite` 数据库及其空间扩展 `SpatiaLite` 和交互式地图的 `JavaScript` 库 `Leaflet` 来创建网络地图的快速入门指南。

[PyTorch Developer Day 2020 Video](https://www.youtube.com/watch?v=jaPVoObpdO0) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
该视频涵盖了各种主题，包括核心框架的更新以及支持多个领域开发的新工具和库。你还将听到社区对 `PyTorch` 支持的最新研究的介绍。

[使用siamese网络、Keras和TensorFlow比较图像的相似性](https://www.pyimagesearch.com/2020/12/07/comparing-images-for-similarity-using-siamese-networks-keras-and-tensorflow/)
在本教程中，你将学习如何使用 `siamese` 网络和 `Keras/TensorFlow` 深度学习库比较两张图像的相似度（以及它们是否属于相同或不同的类）。

[降低数值精度是否会影响现实世界的数据集？](https://drawingfromdata.com/pandas/numpy/kaggle/2020/12/02/Article.html)
降低数值精度是 `pandas` 节省内存的一种方式，但它对我们从现实世界的数据集中可能得出的结论有影响吗？

[如何手动优化神经网络模型？](https://machinelearningmastery.com/manually-optimize-neural-networks/)

[Automate Notion with Python](https://ayushirawat.com/automate-notion-with-python)

[如何在Heroku的Django中设置尾风CSS](https://www.mattlayman.com/blog/2020/tailwind-django-heroku/)



### 有趣的项目、工具和库

[Depix](https://github.com/beurtschipper/Depix)
从像素化的截图中恢复密码。

[Boltstream](https://github.com/benwilber/boltstream)
自带视频直播网站+后台。

[Bodywork](https://github.com/bodywork-ml/bodywork-core) 
`Bodywork` 是一个简单的框架，供机器学习工程师在 `Kubernetes` 上的容器中运行模型训练工作负载和部署模型评分服务。它将大多数机器学习工程师认为 是 `DevOps` 的重复性任务自动化，让他们专注于他们最擅长的工作--机器学习。

[Atheris](https://github.com/google/atheris)
`Atheris` 是一个覆盖式的 `Python` 模糊引擎。它支持 `Python` 代码的模糊化，也支持为 `CPython` 编写的本地扩展。 

[ArtLine](https://github.com/vijishmadhavan/ArtLine)
一个基于深度学习的项目，用于创建线条艺术肖像。

[mongraph](https://github.com/ramitmittal/mongraph)
一个将 `mongodb` 记录可视化为节点网络的工具。

[simple-ehm](https://github.com/morrolinux/simple-ehm)
一个简单的工具，可以完成一个简单的任务：从预先录制的演讲中去除填充音（"嗯"）。由人工智能驱动。

[GuitarLSTM](https://github.com/GuitarML/GuitarLSTM)
使用 `LSTM` 与 `Keras` 进行吉他音箱/踏板仿真的深度学习模型。

[Diggy](https://diggyhq.com/) 
`Diggy` 是一个非常强大、漂亮、易用的笔记本，它预装了 `SciPy` 协议栈，可以直接在浏览器中工作，而无需依赖服务器端代码。

[ghtop](https://github.com/nat/ghtop)
查看GitHub上实时发生的事情。

[WriteHat](https://github.com/blacklanternsecurity/writehat) 
一个用 `Python` 编写的 `pentest` 报告工具。把自己从微软的 `Word` 中解放出来。 

[alibi-detect](https://github.com/SeldonIO/alibi-detect)
一个 `Python` 库，专注于离群、对抗和漂移检测。该包旨在涵盖表格数据、文本、图像和时间序列的在线和离线检测器。

[sillynium](https://github.com/con-dog/sillynium)
通过在网页元素上绘制彩色方框，自动创建 `Python Selenium Scripts`。



### 新活动


[Virtual: Boston Python Meetup December 2020](https://www.meetup.com/bostonpython/events/275089088/)
将会有以下话题:

- 建立一个虚拟的雨量计
- 利用代码的展示介绍 `Pandas` 数据框架。
- 关于 `Python` 和定位。在 `Python` 中使用 `GeoPandas` 处理地理空间数据的介绍。


[Virtual: San Diego Python Meetup December 2020](https://www.meetup.com/pythonsd/events/wxfkzrybcqbgc/)
将会有以下话题:

- 用Python找到你的第一份工作
- 计算K-means法的最佳聚类数。
- Circuit Playground Express
- Getting the list length, the hard way 


[Virtual: Cleveland Python Meetup December 2020](https://www.meetup.com/Cleveland-Area-Python-Interest-Group/events/fhqrtrybcqbsb/)
将会有一个演讲，`EntityKB`：一个快速开发自定义知识库的python工具包。

[Virtual: PyData Montreal #15](https://www.meetup.com/PyData-MTL/events/274786470/)
将会有以下话题:

- 机器学习的持续集成
- 测试生产机器学习系统


[Virtual: PuPPy Meetup December 2020](https://www.meetup.com/PSPPython/events/274929261/)
将会有以下话题:

- 可解释的机器学习
- 奥运攀岩预测
- 快球：一个足球故事
- 使用CWT的CW：用小波从音频文件中解码摩尔斯码。


[Virtual: PyData Boston - Cambridge Meetup December 2020](https://www.meetup.com/PyData-Boston-Cambridge/events/274620793/)
将会有以下话题:

- 伪标签指南。如何在只有一个模型的情况下获得 `Kaggle` 奖章？
- 数据发现的主题建模。网络安全应用案例


[Virtual: PyData Cambridge Meetup December 2020](https://www.meetup.com/PyData-Cambridge-Meetup/events/274794027/)
将会有以下话题:

- 为你的深度时间序列模型选择正确的损失函数
- `GPy`用于监测洋流


[Virtual: PyData Chicago December 2020](https://www.meetup.com/PyDataChi/events/274708472/)
届时将有一个讲座《用 `Python` 进行可解释的机器学习--什么样的品质才是高评价的巧克力棒？》



Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-478.html)
- 改进: [issue-478.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23478.md)

