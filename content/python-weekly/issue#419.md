Title: pythonista-weekly : Pyw 419
Date: 2019-10-22 21:42
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-419

### 欢迎阅读"pythonista周刊"第419期. Let us start!
> 安全领域如何玩转 Python

原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-419](https://mailchi.mp/pythonweekly/python-weekly-issue-419)  
翻译:Dustyposa

------



### 来自赞助商(PS:原文的赞助商):
#### 使用 `Datadog` 监控你的python指标,日志,集群分析. 使用`Datadog`的应用分析,可以深入任何纬度并且能找到你所需要的信息,来进行动态诊断和快速故障排除. [马上跟踪你的python应用吧!免费试用14天哦!](https://www.datadoghq.com/dg/apm/ts-python-tracing/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Tshirt)
## 文章,教程与话题
#### [Dropbox 是如何构建威胁检测和安全事件响应工具的. ](https://blogs.dropbox.com/tech/2019/10/how-dropbox-security-builds-better-tools-for-threat-detection-and-incident-response/)
一般情况下,最常见的构建威胁检测和响应工具的方法是解耦自动化和检测部分. 根据我们的经验,这会导致大量的内存溢出. 在`Dropbox`中, 我们已经为我们的日志构建了一个公共的抽象底层,通过`Alertbox`,`Covenant`和`Forerunner`在安全响应周期内的不同阶段都可以使用. 集成并利用强大的开源工具能使我们快速地探索我们的数据并自动警报. 我们就可以专注于解决更复杂的威胁. 
> 这个安全方向有点难. . . 不太熟悉. . 一脸懵逼状态. . 
#### [Python 3.8 有什么新东西!](https://docs.python.org/3.8/whatsnew/3.8.html)
这篇文章阐述了`Python 3.8`的新特性,并和`3.7`进行比较. 
> 这个就比较熟悉啦!海象运算符(都说和 go 像,但我觉得和 c 更像,你觉得呢?),仅位置参数,`typing.TypedDict`,f 字符串打印....
#### [python的导入指南:绝对导入,相对导入 and more~](https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/)
如何规划你的代码,让导入更加干净!
> 导入也是个头痛的问题
#### [Haptic 是如何进行庞大的 python3 迁移的](https://haptik.ai/tech/how-haptik-carried-out-their-largest-python3-migration/)
这篇文章讲述了 Haptic 是如何克服 `Python 2` 代码热(无停机)迁移到 `Python 3`代码的挑战的. 
> 热迁移,高级!如果有 py2 to py3 需求,推荐一读. 
#### [python分治算法的终极指南](https://skerritt.blog/divide-and-conquer-algorithms/)
容易理解的分治算法的介绍!
> 分治. 算法绕不开的东西. 
#### [Soundcloud 推广机器人](https://www.youtube.com/watch?v=B-xvgebrB2g)
在本篇教程中,我们将介绍如何使用 python 编写一个自动在 soundcloud 上进行推广的机器人. 这真的是一个很有趣的工具,因为现在在`soundcloud`上有如此多的机器人,你可能对了解和发现机器人是如何工作的并且如何使用`python`做出属于自己的`soundcloud`是很感兴趣的. 
> 虽然没用过 `soundcloud` 但是应该和 `twitter`上面的机器人功能类似,也应该很有趣!
#### [Y组合器的简单本质(用python解释)](https://lptk.github.io/programming/2019/10/15/simple-essence-y-combinator.html)

Y组合器是λ演算的核心概念,它是函数式编程的形式基础. Y允许在没有定义引用的情况下定义一个递归的函数. 我见过的大多数专门解释Y组合器的文章都是从给你展示Y组合器开始(它本身就很难理解),然后尝试解释它是如何工作的. 我认为这样做是反的. 在本文中,我们将从另一种方式开始:我将用通俗易懂的话来描述Y组合器的本质,然后在没有递归定义的情况下如何实现递归,那时候我们就能清楚的了解一般的Y组合器了. 

> 计算机基础的教程来了. 犹豫就会败北!

#### [复杂的瀑布流](https://sobolevn.me/2019/10/complexity-waterfall)
在本文章,我将带着你找到存在复杂性的地方并且教你如何解决. 然后我们将讨论如何编写良好的简单的代码和自动化如何适应"连续重构"和"可变架构"开发风格的. 
> 代码水平也是相当重要的. 
#### [用python和django向AWS S3 上传文件](https://stackabuse.com/uploading-files-to-aws-s3-with-python-and-django/)

在本文,我们将探索`Django`如何处理文件上传和我们如何用存储使用及扩展该功能,以便适应于我们的需求. 

> Django知识扩展

#### [使用Pandas的qcut和cut进行数据分箱](https://pbpython.com/pandas-qcut-cut.html)

`Pandas`的`qcut`和`cut`都可以用来将连续值存储到离散箱或者连续箱中. 本文将解释两个命令的不同之处,并如何使用他们. 

> 数据处理小知识. 

#### [使用PyQtGraph进行绘图](https://www.learnpyqt.com/courses/graphics-plotting/plotting-pyqtgraph/)

在该教程中,我们将从使用`PyQtGraph`创建绘图小部件开始,然后演示使用线条颜色,线条类型,轴标签,背景色和复杂线条定制绘图. 

> 窗口绘图利器!

[如何使用MongoDB和Docker构建Flask应用](https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker)

在本教程中,你将在 docker 容器中使用`Flask MongoDB和nginx`构建,打包,运行你的`to-do`网络服务. 你将在`docker-compose.yml`文件中定义全部的堆栈配置,以及`Python MongoDB 和 nginx`的配置文件. `Flask`需要一个网络服务器来服务于`HTTP请求`,所以你也会使用一个叫做`Gunicorn`的`Python WSGI服务器`来服务于应用. `Nginx`充当反响代理将请求转发给`Gunicorn`进行处理. 

> 这篇文章大家应该比较感兴趣,讲解了如何部署`flask`服务,`Gunicorn`网关服务器现在也比较流行了,设置比`uwsgi`简单多了,使用更方便,首推!

[为什么我的验证损失比训练损失更小](https://www.pyimagesearch.com/2019/10/14/why-is-my-validation-loss-lower-than-my-training-loss/)

在本教程中,你将学到在训练你的深度神经网络时,你的验证损失可能低于训练损失低的三个主要原因. 

> 损失损失,你为什么不一样!

#### [一个安全并非极端耦合的方式反向私有化Api](https://blog.jonlu.ca/posts/safeway)

#### [Python属性访问和描述符约定](https://amir.rachum.com/blog/2019/10/16/descriptors/)

#### [由于对python的误解,数千篇科学论文可能无效](http://www.blog.pythonlibrary.org/2019/10/13/thousands-of-scientific-papers-may-be-invalid-due-to-misunderstanding-python)

#### [有关如何在 Django 应用中使用 Sentry 实时监控软件错误的分步教程](https://blog.hlab.tech/a-step-by-step-tutorial-on-how-to-monitor-software-errors-in-real-time-using-sentry-in-django-web-applications/)

#### [使用Spotify API 和Python分析音乐喜好](https://nvbn.github.io/2019/10/14/playlist-analysis/)



## 有趣的项目,工具和库

#### [Detectron2](https://github.com/facebookresearch/detectron2)

`Detectron2`是 Facebook AI研究的下一代软件系统,它实现了最先进的目标检测算法. 这是对老版本`Detectron2`的重写,起源于`maskrcnn-benchmark`.

> 去github官网看了看,很高级的样子,加入百宝箱. 

#### [PyTorch Mobile](https://pytorch.org/mobile/home/) 

来自python的端到端工作流程,可部署在在 iOS 和 Android

> 移动端也能玩出新花样. 

#### [pyChart.js](https://github.com/IridiumIO/pyChart.js) 

为`python`和`django`实现的`Chart.js`

> 实现网页渲染图片,用来在模版中画图的,flask也支持了哦. 例如这样的语法:
>
> ![pyw-419-pychart.png](https://i.loli.net/2019/10/28/VNxAPyFKU56rDsR.png)

#### [cast-sh](https://github.com/hericlesme/cast-sh) 

在你的浏览器中运行`terminal`窗口. 

> 用网页当作terminal界面,操作服务器. 问题点就是输入输出的传输和网络定制了. 最近在研究这方面,还可以. 

#### [CrypTen](https://github.com/facebookresearch/CrypTen) 

一个用于隐私保护性机器学习的框架. 

> 隐私隐私,最近经常上头条,AI方面的隐私处理也是很重要的. 

#### [sotabench-eval](https://github.com/paperswithcode/sotabench-eval) 

简单使用通用基准评估机器学习模型. 

> 简单是程序员的前进动力!

#### [Captum](https://github.com/pytorch/captum) 

`Captum`是针对`Pytouch`模型的一个可解释模型的库. `Captum`在拉丁语中意味着理解,它包含了针对`Pytouch`模型的实现的`integrated gradients(集成梯度),saliency maps(显著图), smoothgrad, vargrad and others `

> emmm,有点难,,太多术语看不懂了. 现在两大框架的生态也逐渐丰富起来了. 

#### [TorchBeast](https://github.com/facebookresearch/torchbeast) 

一个用来做分布式强化学习的`Pytouch`平台. 

> 除了高级我还能说什么. . . 

#### [image_to_numpy](https://github.com/ageitgey/image_to_numpy) 

使用Exif(可交换图像文件格式 )方向支持实现图片文件转 `numpy`数组. 防止图片的颠倒和侧视. 

> 看名识库!

#### [Daudin](https://github.com/terrycojones/daudin) 

一个支持python命令的shell

> 有点高级,切换`shell`和`python shell`不方便?
>
> 我们来看看官方的小示例:
>
>![pyw-419-daudin.png](https://i.loli.net/2019/10/28/UfiAeaXKgEqImBd.png)
> 只可意会,不可言传

## 新版本

#### [Python 3.8.0](https://www.python.org/downloads/release/python-380/) 

python3.8.0是现在的主要版本,包含了许多新的特性. . . 

> 好像这条有点重复

#### [Django 3.0 beta 1](https://www.djangoproject.com/weblog/2019/oct/14/django-30-beta-1-released/) 

 Django 3.0 beta 1现已推出 .  3.0发布周期的第二阶段也来了,是时候尝试Django 3.0中的变化了.  

> Now is better than never!

#### [PyPy v7.2](https://morepypy.blogspot.com/2019/10/pypy-v72-released.html) 

> 好像到支持cython 3.6版本了,想python跑得更快,值得一试. 

## 活动和网络研讨会日程

#### [Silicon Valley Python Workshops November 2019 - Palo Alto, CA](https://www.meetup.com/SV-Python-Workshops/events/265384631/)  

将会有以下的话题:

- Fanatic's 的微服务之旅:一个关于我们的分布式数据管道的故事
- Carta的新标识:我们如何让部署更简单

> 实战内容比较多呀

 #### [Boston Python Meetup October: Lightning Talks - Boston, MA](https://www.meetup.com/bostonpython/events/263971510/) 

将会有以下的话题:

- 这需要多长时间? (进度条) 
-  使用Open CV做人脸识别
-  自学Python各种档案
-  使用FitBit数据来追踪健康 状态
- 用 python 编写一个 Git Hook
- 什么时候是农历新年

> 话题种类比较多~~

#### [Snakes and Queues: Python and AMQP - London, UK](https://www.meetup.com/LondonPython/events/265681515/) 

高级消息队列协议(Advanced Message Queuing Protoco)是一种用于在线异步消息传递的开放源码标准,它通过客户机之间的消息代理提供RPC和发布/订阅模式. 在这次演讲中,我将向您介绍AMQP,看看它的一些Python客户端实现,最后现场编写一个Python微服务框架,它提供了我所见过的最优雅的AMQP抽象. 

> 感觉python微服务相关应用也慢慢变多了. 

#### [IndyPy Bytes: Applying Data Science to IoT - Indianapolis, IN](https://www.meetup.com/indypy/events/lbdfpqyznbdc/) 

数据科学有利用人工智能,数学技巧和统计学来帮助理解数据. 但随着更多更新的物联网设备出现,传统技术的可扩展性远不如它们需要的那么好,这引出了一个数学上的新方向. 本次演讲将详细介绍数据科学中用于大规模分析的方法,以及物联网作为一个行业发展所必需的有用技术和概念. 

> 数据和机会,数据和挑战

#### [San Diego Python Meetup October 2019 - San Diego, CA](https://www.meetup.com/pythonsd/events/zgtnxqyznbgc/) 

将会有以下的话题:

-  编程求职技巧  
- Python席卷全球

> 很硬核的样子

#### [DC Python Meetup October 2019 - Arlington, VA](https://www.meetup.com/dcpython/events/264994832/) 

 了解在Python中的日期和时间,实现时间序列数据模型.  



#### [Computer Generated Tweets and Other Prose Using GPT-2 - Chicago, IL](https://www.meetup.com/PyDataChi/events/265629442/) 

在这里,我们将讨论如何应用GPT-2,这是一种可生成的深度学习模型,用于生成模仿一个人的tweet输入的文本. 我们将重点准备输入文本,以便它可以理解的模型,以及如何确保没有过拟合. 然后,我们将讨论如何在谷歌Colab上使用GPT-2和GPT2-simple,这是使用库的一种简单方法,允许你训练,运行模型并管理GPT-2的改进模型. 

> AI应用试验最新实战



