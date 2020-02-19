Title: pythonista-weekly : Pyw 422
Date: 2019-11-10 15:16
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-422

### 欢迎阅读"pythonista周刊"第422期. Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-422](https://mailchi.mp/pythonweekly/python-weekly-issue-422)  
>翻译:Dustyposa

### 来自赞助商:
使用 `Datadog` 监控你的python指标,日志,集群分析. 使用`Datadog`的应用分析,可以深入任何纬度并且能找到你所需要的信息,来进行动态诊断和快速故障排除. [马上跟踪你的python应用吧!免费试用14天哦!](https://www.datadoghq.com/dg/apm/ts-python-tracing/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Tshirt)
> 熟悉的面孔. 
## 新闻
####  [Python 采用 12 个月的发布周期](https://pythonweekly.us2.list-manage.com/track/click?u=e2e180baf855ac797ef407fc7&id=fea677de77&e=57c131a127)
> Python 升级固定了!

#### [在银行Python 已经取代了 Excel](https://pythonweekly.us2.list-manage.com/track/click?u=e2e180baf855ac797ef407fc7&id=85e5cd4508&e=57c131a127) 

> 就是在某些银行,已经只用`Python`来处理数据了!原因其实很简单,就是`Excel`太慢了. . 想想用`Excel`处理大型文件,内心是绝望的!
>
> 该来的还是会来的!



## 文章,教程与话题
####  ["Writing a PEG parser for fun and profit" - Guido van Rossum](https://www.youtube.com/watch?v=QppWTvh7_sI)  ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(42 min)

解析表达文法(PEGs) 是一种新的用来描述适合自动生成高效解析器的文法的形式. 我对使用 基于PEG生成器的解析器来代理在`Cython`中使用近30年的"pgen"解析生成器很有兴趣. 这出现了一些有趣的问题. 我还想出了一种可视化解析过程的简单方法,它有助于调试文法和解析机制,并且我将使用它去解释一般的`PEG`解析过程. 

> 龟叔依然很忙~

####  [不要使用 utcnow and utcfromtimestamp](https://blog.ganssle.io/articles/2019/11/utcnow.html) 
关于`utcnow`和`utcfromtimestamp`的危险以及使用其替代品的好处的公共服务公告. 
> utc 的坑,国际化的Application不易呀~

####  [JWT 认证和 DjangoREST API](https://t.co/zT2Lxr3Us1) 
基于 Token  的身份认证允许服务器和前端(无论是网络,本地移动设备还是其他设备)分离,并归属于不同的域名. `JSON Web Tokens(JWT)`是基于 token 的身份认证的一种常见实现方式,在这篇文章,我们将会用它在一个基于`Django REST`框架的notes应用中的一个API进行用户认证. 
> 熟悉的实践篇章

####  [通过做5个游戏来学习 Python](https://www.youtube.com/watch?v=XGf2GcyHPhc) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)(6h43min)

在这个面向初学者的完整教程中学习`Python`. 这个课程使用的是以项目为基础的方法. 我们一共收集了5个很好的`Python`游戏教程,所以你可以在构建5个游戏的同时学习`Python`. 你如果是实践学习者,这个课程非常适合你!

> 寓教于乐

#### [Python range 指南:学习使用这个很有用的内置函数](https://www.dataquest.io/blog/python-range-tutorial/)
在这篇详细的指南中,我们将通过几个栗子来带你了解`range`函数的工作原理,并探讨它的局限及解决办法. `range`对各种各样的`Python编程任务`来说都是很有用的,该指南最后将介绍以`range函数`在数据科学的应用的几个栗子. 
> 又一篇新手推荐~

####  [通过GitHub Actions,Poetry,Black和Pytest快速实现CI](https://t.co/GiXdUiDQrm)  
为`Django`项目设置`Github Actions`
> 部署上线一条龙~

####  [通过 Python 理解 OpenGL](https://stackabuse.com/understanding-opengl-through-python/) 
如何使用`Spectrograms和GANs`将爵士乐转换成古典乐
> 不知道 MIKU 的音乐能不能转~


####  [Python Datetime 指南: 操作 Times, Dates 和 Time Spans](https://www.dataquest.io/blog/python-datetime-tutorial/)  
在本数据科学教程中使用`datetime和calender`模块成为成为`Python`中的时间和日期的大师. 

> 希望能操作虫洞!

####  [Python: 超乎想象的 typed](https://beepb00p.xyz/mypy-error-handling.html) 
`mypy`辅助错误处理,其他语言中的异常机制,模式匹配和类型差异的乐趣. 

> 何以解忧,唯有`mypy`

#### [为什么你应该使用 `python -m pip`](https://snarky.ca/why-you-should-use-python-m-pip/)
该文章揭示了什么是`python -m pip`和你为什么在运行`pip`的时候应该使用它. 

> 环境比较重要

#### [基于Keras和深度学习的交通标志分类](https://www.pyimagesearch.com/2019/11/04/traffic-sign-classification-with-keras-and-deep-learning/)

在本片指南,你讲学习到如何训练你自己的交通标志分类器/识别器,使用`Keras和深度学习`可以使其可以达到95%以上的准确率. 

> 哪里不认识训练哪里!

#### [我们如何发现并修复Python代码中的性能下降](https://blog.redash.io/how-we-spotted-and-fixed-a-performance-degradation-in-our-python-code/)

> 实践出真理

#### [用Python进行医疗保险欺诈检测](https://www.theseattledataguy.com/healthcare-fraud-detection-with-python/)

> 人心叵测～

#### [Python标准库中一些鲜为人知的地方](https://t.co/vbMM7hNrJG)

> 骚操作finding!

#### [Hugging Face: TensorFlow 2.0使用10行代码实现最先进的nlp处理](https://blog.tensorflow.org/2019/11/hugging-face-state-of-art-natural.html)

> 适合简单了解一下～

#### [在 Python 中通过源码和行号找到定义](https://julien.danjou.info/finding-definitions-from-a-source-file-and-a-line-number-in-python/)

> 文法分析,语法树～最近在看的

#### [你不需要迁移至 Python 3](https://switowski.com/blog/you-dont-have-to-migrate-to-python3)

> 所以我是升还是不升呢?



## 有趣的项目,工具和库

####  [Spleeter](https://github.com/deezer/spleeter)  

`Spleeter`是 `Deezer`的源分离库,有用`Python`使用`Tensorflow`编写的预训练模型. 让训练一个源分离模型( 假设已经有了一个隔离源的数据集 )变得容易. 并且提供了已经训练好的用于执行各种分离风格的最新模型. 

> 音轨分离!佳作. 
>
> 内置3种分离模式. 可以自由选择哦!
>
> 听不出自己声音的我估计是没戏了. 

####  [inbac](https://github.com/weclaw1/inbac) 
`inbac`是一款交互式批量裁剪器,用于快速裁剪图像. 

> 剪裁太慢?python来凑!



####  [trains-agent](https://github.com/allegroai/trains-agent) 

它是一种零配置的"一劳永逸"执行代理,与trains-server结合使用可提供完整的AI集群解决方案. 

> AI服务也是需要Dev-ops的,为什么?因为都是集群了!
>
> 
>
> 

#### [python-gift-exchange](https://github.com/sethblack/python-gift-exchange) 

Python礼物交换选择器

> 一个程序员被妻子逼迫的故事!
>
> 没办法,为什么自己这么强呢?(不是我!!!!!!)



####   [jsonfield-schema](https://github.com/viewflow/jsonfield-schema) 

将Django JSONField数据公开为虚拟模型字段



#### [lask-static-digest](https://github.com/nickjj/flask-static-digest)
`Flask`扩展,通过`md5标记和gzipping`帮助你准备好生产的静态文件. 

> 静态一条龙
>



#### [cvxpylayers](https://github.com/cvxgrp/cvxpylayers)

cvxpylayers是一个Python库,用于使用CVXPY在PyTorch和TensorFlow中构造可微凸优化层. 

## 最近更新

#### [Python 3.5.9](https://www.python.org/downloads/release/python-359/)

#### [Django bugfix releases issued: 2.2.7, 2.1.14, and 1.11.26](https://www.djangoproject.com/weblog/2019/nov/04/django-bugfix-releases-227-2114-11126/)



## 活动和网络研讨会日程

#### [CPython: from code to execution - New York](https://www.meetup.com/nycpython/events/265386351/)

通过快速浏览cpython 3.9解释器源代码,我们将了解一些python代码如何从熟悉的人类可读语法到解释器产生字节码结果. 

> 编译原理之美

#### [Effortless REST W/ Flask - Charlotte, NC](https://www.meetup.com/PyDataCharlotte/events/265952190/)

将有以下话题:

- 算法如何变得有偏见?
- Python Severless 话题:使用Zappa无基础架构的web应用程序
- Tensorflow 2.0 有什么新东西?
- Python中最好的AI包

> 种类依旧丰富～

#### [Philadelphia Python Meetup November 2019 - Philadelphia, PA](https://www.meetup.com/phillypug/events/265657211/)

Twitter的Developer Advocate-Jessica Garson将向我们展示她如何使用Python解决她在纽约的停车问题

#### [Boulder Python Meetup November 2019 - Boulder, CO](https://www.meetup.com/BoulderPython/events/vcmckryzpbqb/)

#### [PyLadies Totonto November Talk Night, Totonto ON](https://www.meetup.com/PyLadies-Toronto/events/265218106/)

####[Edmonton Python Meetup November 2019 - Edmonton, AB](https://www.meetup.com/startupedmonton/events/dtflxjyzpbpb/)




## Posa:
> ❤️ Happy Pythonic ;-(Posa私人无责任播报)
#### [测测你的python数据类型掌握了吗!](https://realpython.com/quizzes/python-data-types/viewer/)

一个测试~哎,有点难,可以试试,8道题,3分钟差不多. 是时候展现自己真正的实力了. 




----- 分割线 -----
> 如果你发现哪里翻译有误的话,请务与我联系!感谢!
>

- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-422.html)
- 改进: [issue-422.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue#422.md)


