Title: pythonista-weekly : Pyw 426
Date: 2019-12-08 15:16
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-426

### 欢迎阅读"pythonista周刊"第426期. Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-426](https://mailchi.mp/pythonweekly/python-weekly-issue-426)  
>翻译:Dustyposa

### 来自赞助商(PS:原文的赞助商):
使用 `Datadog` 监控你的python指标,日志,集群分析. 使用`Datadog`的应用分析,可以深入任何纬度并且能找到你所需要的信息,来进行动态诊断和快速故障排除. [马上跟踪你的python应用吧!免费试用14天哦!](https://www.datadoghq.com/dg/apm/ts-python-tracing/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Tshirt)
> 是 select 还是 epoll 呢 

## 新闻

#### [Mozilla and Chan Zuckerberg Initiative 赞助 pip](https://pyfound.blogspot.com/2019/12/moss-czi-support-pip.html)

`Python 软件基金会`将在 2020 年获得 `$407,000 USD`来支持`pip`的开发工作. 这种基础性,转换型的工作将使`Python`开发者和用户能专注于他们在制作或者使用的工具,而不是解决依赖冲突. 具体来说,`CZI and Mozilla`正在资助用户体验,交流/宣传和测试的工作(包括开发完备的测试基础设施)以及核心功能的开发和审查. 

> 官方出手,资金提升,pip 稳了吗!

#### [两个恶意的Python库被发现正在窃取SSH和GPG密钥](https://www.zdnet.com/article/two-malicious-python-libraries-removed-from-pypi/)

`Python 安全团队`从`PyPI(Python包索引)`中移除了两个木马库,这些库北发现会从受感染者的项目中获取`SSH 和 GPG`密钥. 这两个库是被同一个开发者创建,并且模仿了其他的更流行的库---用了一个叫做 `typosquatting`的技术来注册名字相似的名字. 第一个叫做`python3-dateutil`,模仿了一个流行的`dateutil`库. 第二个名字叫`jeIlyfish(第一个 L 是 I),模仿了`jellyfish`库. 

> `Python`太收欢迎?


## 文章,教程与话题
#### [端到端机器学习: 从数据收集到部署](https://ahmedbesbes.com/end-to-end-ml.html)

在这篇文章,我们将通过一些必要的步骤去构建和部署一个机器学习应用. 这将从数据收集开始再到部署,你将看到的全貌,是令人兴奋并且有趣的. 

> ML 部署 get

#### [用 Qiskit 进行量子计算机编程](https://www.youtube.com/watch?v=aPCZcv-5qfA) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(48min)

量子计算机编程实用型介绍,使用`IBM`的免费的云量子计算机和`Qiskit`.

> 尝鲜
>
> 最近经常出现在 python thrending 中

#### [框架模式](https://blog.startifact.com/posts/framework-patterns.html)
配置一个框架有很多方法. 每个方法都有自己的优缺点. 这篇文章描述了一些框架配置模式,并提供了一些简单的例子和折中的方案. 

> 太过自由也会让人比较难

#### [用法Python 和 Facebook Prophet做预测](https://t.co/RnFPZKiaWf) 

如何使用领域知识去调整和优化`Prophet`,让你的预测更可控. 



#### [Django 3.0有什么新特性](https://www.youtube.com/watch?v=_BBNVFirvTY) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(5min)

`Django`刚刚发布了他们的下一个主要版本`django 3.0`. 这对你有什么影响?什么是`ASGI`?让我们讨论一下. 

> 异步来啦!

#### [高效的Python](https://strangemachines.io/articles/performant-python)

看一看如何用简单的方式编写高效的`Python`代码,以及每个改进有多少效果. 

> 刚优化了 pandas 索引方式代码的我留下了不学无术泪水. 

#### [OpenCV 车辆检测, 追踪和速度估算](https://www.pyimagesearch.com/2019/12/02/opencv-vehicle-detection-tracking-and-speed-estimation/)
在这篇教程中,你将学习如何使用`OpenCV和深度学习`在视频流中进行车辆检测,并追踪他们并且利用速度估测去检测移动车辆的`MPH/KPH`. 

> 这个很刺激的样子. 

#### [使用 Python创建一个全能的 Indeed Bot ](https://www.youtube.com/watch?v=jp0eiGn4jto) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(25min)
使用 Python创建一个全能的 Indeed Bot. 

> 都越来越喜欢机器人了. 

#### [Excel vs Python: 如何执行常见数据分析任务](https://www.dataquest.io/blog/excel-vs-python/)

`Excel and Python`的不同之处是什么?在这篇文章中,我们将通过观察在两个平台执行基准任务来进行比较. 

> 问我选什么?
>
> 这不是很明显吗!成年人,当然两个都要!

#### [在Visual Studio Code使用 Python](https://channel9.msdn.com/Shows/Visual-Studio-Toolbox/Getting-Started-with-Python-in-Visual-Studio-Code) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(32min)

在这一集,`Tyreke White`为我们展示了如何使用`Visual Studio Code`开始`Python`开发. 他讲解了你需要安装什么并且如何配置你的环境,也分享了如何对你的`Python代码debug`的小技巧. 

> VSC 还是比较省内存的. 

#### [给长时间运行的 Jupyter Notebook Cells 加上通知](http://www.blog.pythonlibrary.org/2019/12/04/adding-notifications-to-long-running-jupyter-notebook-cells/)

如果你使用`Jupyter Notebook`去运行长时间运行的进程,例如:机器学习的训练,然后你可能想知道什么时候`cell`运行结束了. 这里有一个叫做`jupyter-notify`的简洁的浏览器插件你可以使用,帮助解决这个问题. 当`cell`执行结束时,你的浏览器会发出一个弹窗信息通知你. 

> 痛点解决!

#### [词袋模型的简单解释](https://victorzhou.com/blog/bag-of-words/)

一个快速,简单的关于词袋模型的介绍,以及你如何在`Python`中实现. 



#### [Python 字节码: 一个介绍教程](https://www.youtube.com/watch?v=mE0oR9NQefw) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(12min)

这是开始深入了解`Cpython`内部实现原理(实际上`Python`参考实现)的好方法. 不要让你之前的误解或者让你知道的一些知识阻碍你. 如果你想学习更多关于`Python`的知识,那么这 10 分钟是值得的. 

> 不要被已知知识束缚. 

#### [如何用Python分析笔记本电脑上的100 GB数据](https://t.co/52y7IjNSqm)

了解如何使用`Python`中的`Vaex`开源数据框架探索,可视化和分析 100GB 的表格数据. 

> 躲不过的大量数据. 

#### 使用Elasticsearch,Logstash,Kibana(ELK)+ Filebeat进行Django集中式日志记录t](https://binaroid.com/blog/django-centralised-logging-using-elasticsearch-logstash-kibana-elk-filebeat)

在这篇教程,我们将学习如何从我们的`Django`应用中把应用日志放到`Elasticsearch`存储,并且能够在`Kibana`web工具中以可读的方式展示. 本文的主要目的是使用另一种工具`Elastic - Filebeat`在`Django`服务和`ELK堆栈 (Elasticsearch, Kibana, Logstash) `建立一个连接. 我们也会简要的介绍之前的步骤,例如日志记录的背后的原因,在`Django`中配置日志以及安装`ELK stack`. 

> 推推推!

#### [使用Python构建Windows快捷方式](https://pbpython.com/windows-shortcut.html)

使用`Python`去构建一个`Windows`快捷方式来运行`conda`环境. 

[如何在AWS Elastic Beanstalk上部署Django Channels 2.x](https://t.co/HiZSXhJMYP)

[nbdev: 万事皆用 Jupyter Notebooks ](https://www.fast.ai/2019/12/02/nbdev/)

> Jupyter 称霸天下?

[我们如何使用Elasticsearch & PostgreSQL 功能组织Django APIs](https://t.co/qBVSBuB0jA)

[PyCon Sweden Videos](https://www.youtube.com/playlist?list=PLQYPYhKQVTvetDJZFGY8RfYlPBLQmbt-T) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)

[降低 Pandas 使用内存  #2: 有损压缩](https://pythonspeed.com/articles/pandas-reduce-memory-lossy/)

## 有趣的项目,工具和库

#### [Metaflow](https://metaflow.org/) 
由`Netfilx`开发,用于`real-life`的数据科学框架. `Metaflow`让构建和管理`real-life`数据科学项目变得更快和简单. 



#### [TensorBoard.dev](https://tensorboard.dev/)
一份管理 `TensorBoard` 的经验,可以让你上传和分享 ML 实验结果给任何人. 

> 数据方面项目的功能也越来越强了

#### [Assembly](https://mardix.github.io/assembly/) 
一个基于`Flask`的` Pythonic` 的面向对象的`Web框架`.   

#### [emoji_trends](https://github.com/enric1994/emoji_trends)

`emoji` 在推特上的使用. 

> 关于表情符号的趋势
>
> 商机!?

#### [Lightbus](https://github.com/adamcharnock/lightbus/) 

`Lightbus`允许你的后台进程通信,运行后台任何并且公开内部`APIs`.尽管最终可能会增加对其他平台的支持,但目前`Lightbus`使用`Redis`作为其基础传输. 

> 异步时间框架 37+

#### [cusignal](https://github.com/rapidsai/cusignal)
`cuSignal GPU`使用`CuPy(GPU加速的NumPy)`和自定义的`Numba CUDA`内核来加速流行的`SciPy Signal`库. 

> 还是速度重要!

#### [tlaplus_jupyter](https://github.com/kelvich/tlaplus_jupyter)
适用于TLA⁺和Pluscal规范语言的Jupyter内核. 

> 大佬们喜欢的混合语法!

#### [emacs-application-framework](https://github.com/manateelazycat/emacs-application-framework)
`Emacs Application Framework (EAF) `是一个应用框架,可以将`GNU Emacs`扩展到一个全新的功能强大的`GUI PyQt`应用程序领域. 

> 亚古兽超进化!

#### [friendly-traceback](https://github.com/aroberge/friendly-traceback)

针对Python初学者:用更容易理解,可翻译成各种语言的东西代替标准回溯. 

> 更友好的回溯,有错误原因及更正方法,初学者可以 have a try. 

#### [django-skinny-deploy](https://github.com/viewflow/django-skinny-deploy)

简单,单文件即可将Django部署到Ubuntu主机. 

> !!部署福音?

[Pytasking](https://github.com/TokenChingy/pytasking)
一个简单的`Python 3.5+`多任务库. 

[MinerClub](https://github.com/0Hughman0/MinerClub)

一个`Webapp`,用于自动管理仅`Minecraft`成员和朋友的服务器. 

[Whatsapp-Net](https://github.com/OfirKP/Whatsapp-Net)

从`WhatsApp groups `数据生成连接的网络图. 

[pytexexam](https://github.com/vungocbinh2009/pytexexam)

一个简单的`Python`包,用于创建和输出考试内容. 

## **New Releases**

#### [Django 3.0](https://www.djangoproject.com/weblog/2019/dec/02/django-3-released/)
发行说明详细介绍了许多新功能,但其中一些要点是:

- `Django 3.0`通过支持作为一个`ASGI`应用运行,`Django`也打开了完全支持异步的新的篇章. 

- `Django`现在正式支持`MariaDB 10.1`及更高版本. 
- 自定义枚举类型`TextChoices,IntegerChoices和Choices`现在可以作为定义模型字段选择的一种方式使用. 

> 终终终于来了!
>
> 它带着异步来了!

## 活动和网络研讨会日程

#### [PyLadies/PyData Year End Talk Night - Toronto, ON](https://www.meetup.com/pydatato/events/266595041/)
将会有以下的话题:

- 在`AWS`中设置简单的`Python`服务器
- 用`Python`再写一个编程语言
- 用`Altair`实现数据可视化


#### [Austin Python Meetup December 2019 - Austin, TX](https://www.meetup.com/austinpython/events/lgrbmqyzqbpb/)
将会有以下的话题:

-  Go For Pythonistas
- ` Python`切片对象


#### [PyMNtos Python Presentation Night #79 - Minneapolis, MN](https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/events/266893889/)
将会有以下的话题:

- 先分析住房
- 用`Python and gRPC`构建微服务
- 使用`Python`从放射学报告中提取临床发现的`NLP`方法


[Boulder Python Meetup December 2019 - Boulder, CO](https://www.meetup.com/BoulderPython/events/vcmckryzqbnb/)

[Cleveland Python Meetup December 2019 - Cleveland , OH](https://www.meetup.com/Cleveland-Area-Python-Interest-Group/events/wrwphqyzqbmb/)

[PyAtl Meetup December 2019 - Atlanta, GA](https://www.meetup.com/python-atlanta/events/xzzgcryzqbqb/)


## Posa:
> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

Django 3.0来啦!

[戳这里](https://docs.djangoproject.com/en/3.0/)



----- 分割线 -----

> 如果你发现哪里翻译有误的话,请务与我联系!感谢!
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-426.html)
- 改进: [issue-426.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23426.md)


