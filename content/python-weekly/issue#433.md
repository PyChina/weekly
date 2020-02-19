Title: pythonista-weekly : Pyw 433
Date: 2020-01-25 15:16
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-433

### 欢迎阅读"pythonista周刊"第433期. Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-433](https://mailchi.mp/pythonweekly/python-weekly-issue-433)  
>翻译:Dustyposa

**来自赞助商(PS:原文的赞助商):**  
[python开发者都需要的Vettery](https://www.vettery.com/tech?utm_source=newsletter&utm_medium=pythonweekly&utm_term=tech&utm_content=grouped&utm_campaign=ad-77579)  
Vettery是一个招聘网站,它改变了人们应聘或者雇佣的方式. 准备好换工作地方了吗?免费制作简历,你的薪资你说了算,现在就和顶级雇主的HR联系吧!



##   新闻

**[DjangoDay Copenhagen 2020 CFP](https://djangoday.dk/)**

来自丹麦及周边的`Djangonauts`们将齐聚一堂,参加定于2020年4月17日举行的第二届`Django Day`. `CFP`是开放的,我们正在寻找25分钟的演讲,40分钟的演讲和5分钟的闪电演讲(可以当天提交). 




## 文章,教程与话题

**[使用Python扩展Clojure](https://www.youtube.com/watch?v=vQPW16_jixs)** ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)*(30min)*

`Libpython-clj`是一个库,它允许您使用`clojure repl`中的`python`库. 我们将仔细研究使程序库工作的细节,并讨论构建它的设计决策的一些潜在后果. 



**[使用 TensorFlow 构建一个  AI-Empowered Music 库](https://blog.tensorflow.org/2020/01/building-ai-empowered-music-library-tensorflow.html)**

`QQ音乐`是`Tencent Music Entertainment Group (TME)`所有的一个音乐流服务,我们服务了全球800+M的用户. 我们拥有庞大的音乐库,其中包含大量的专辑和现场音乐(音频和视频格式). 在TensorFlow的基础上,我们能够通过实现许多用于自动音乐标记,音乐评估,语音分离,音乐缺陷检测和恢复等的机器学习算法来有效地管理音乐库.  在本文中,我们想与你分享我们如何构建这种具有AI功能的音乐库以及使用`TensorFlow`的经验. 

> tencent出品 必属

**[用Python读取二进制数据](https://reachtim.com/articles/reading-binary-data-with-python.html)**

在`Python`中处理外部二进制数据时,有两种方法可以将这些数据转换为数据结构.  您可以使用`ctypes`模块来定义数据结构,也可以使用`struct python`模块.  当您在网络上浏览工具存储库时,将看到使用的两种方法.  本文向您展示如何使用每个网络读取网络上的IPv4标头. 



**[停止基于Python的后门攻击](https://vimeo.com/383337193/65c5e52bcd)** ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)

`MechaFlounder`是与针对土耳其实体的伊朗威胁行为者有关的后门攻击.  类似的基于`Python`的后门攻击已设法规避了传统的网络安全防护,并在目标环境中传播.  了解基于`Python`的后门攻击以及为何基于软件身份验证(零信任安全性)的保护可以阻止此类攻击. 

> emmm 你懂的

**[使用Phoenix和Python进行实时对象检测](https://www.poeticoding.com/real-time-object-detection-with-phoenix-and-python/)**

这篇文章不仅仅是关于机器学习和对象检测,还有关于`Elixir`的互通性,以及我们如何利用`Python`出色的ML库集,将其功能带入`Elixir`世界. 

> 三方的世界

**[URLs Lead The Way](https://www.mattlayman.com/understand-django/urls-lead-way/)**

`Django`站点如何知道将请求发送到哪里? 你必须告诉它! 在理解`Django`系列的下一篇文章中,我们将介绍`URL`以及如何使用户到达正确的位置. 

> 深入 系列!春节必备!

[帮助IT管理AI/ML生态系统](https://hubs.ly/H0mGnnr0)
了解戴尔和`Domino`如何创建了一种令人耳目一新的简单方法来帮助公司获得他们需要的数据科学团队和技术,并以一种易于扩展的方式更快地运行. SPONSOR

**[介绍异常检测与OpenCV,计算机视觉和scikit-learn](https://www.pyimagesearch.com/2020/01/20/intro-to-anomaly-detection-with-opencv-computer-vision-and-scikit-learn/)**

在本教程中,你将学习如何使用`OpenCV,计算机视觉和scikit-learn`机器学习库在图像数据集中执行异常/新型检测. 



**[用自己的函数自动完成无聊的任务](https://t.co/l9jWcdLESU)** 

用`Python`做任务自动化是很简单的. 一旦你有了一个工作脚本,将它转换成一个函数,帮助你更有效地编写代码!

> 成长之路的必备. 

**[用蚁群绘画](http://amydyer.art/wp/index.php/2020/01/01/drawing-with-ants-generative-art-with-ant-colony-optimization-algorithms/)**

具有蚁群优化算法的生成艺术. 

> 算法之美!

**[Parens for Pyplot](http://gigasquidsoftware.com/blog/2020/01/18/parens-for-pyplot/)**
`libpython-clj`为`Clojure`直接与Python库互操作打开了大门.  这意味着我们几乎可以采用任何`Python`库,并直接在`Clojure REPL`中使用它.  但是`matplotlib`呢? `Matplotlib.pyplot`是大多数教程和`Python`数据科学代码中的标配.  我们如何与`Python`图形库互操作?

> 万物皆可画

**[在Python中准确测量代码执行时间](https://knasmueller.net/measure-code-execution-time-accurately-in-python)**

测量代码执行时间是很困难的. 了解如何消除系统的和随机的测量误差并获得更可靠的结果. 



**[编码Python: unittest对Pyhon的断言](https://t.co/8lvTXgfzOb)** 

大型的代码库需要持续的维护,但是更改分散在许多文件中的部分代码非常耗时和繁琐. 本文展示了如何使用抽象语法树编写代码示例来重构`Python`代码---获得比基本`regex和search-replace`多得多的粒度控制. 

> 深入列表 +1

**[open and CPython](http://hondu.co/blog/open-and-python)**

误用`Python`的`open`和`CPython`的`GC`和`UNIX`语义的交互可能会导致意想不到的结果!

> 到底谁的锅

[让我们用Python构建一个文件加密器](https://able-dev.com/2020/01/19/lets-build-a-file-encrypter-with-python/)

[用flask-injector做Python依赖注入](https://t.co/vtDvpI05Hv) 

[让Django测试总是重新构建数据库(如果数据库存在的话)](https://adamj.eu/tech/2020/01/13/make-django-tests-always-rebuild-db/)

[Gandiva, using LLVM and Arrow to JIT and evaluate Pandas expressions](http://blog.christianperone.com/2020/01/gandiva-using-llvm-and-arrow-to-jit-and-evaluate-pandas-expressions/)

[用Python做一些有趣的事](https://www.b-list.org/weblog/2020/jan/20/fun/)

## 有趣的项目,工具和库

**[ActionAI](https://github.com/smellslikeml/ActionAI)**

`ActionAI`是一个用于训练用于分类人类动作的机器学习模型库. 

> 变得更酷!

**[DDSP](https://github.com/magenta/ddsp)**

`DDSP`是常用`DSP`功能(例如合成器,波形处理器和滤波器)的不同版本的库.  这允许将这些可解释的元素用作深度学习模型的一部分,尤其是用作音频生成的输出层. 

**[Flytekit](https://github.com/lyft/flytekit)**

用于轻松创作,测试,部署和与Flyte任务,工作流和运行计划并可交互的库. 



**[Rich](https://github.com/willmcgugan/rich)**

`Rich`是一个`Python`库,用于在终端中显示富文本和精美格式. 

> 非常 RIch

**[JustCause](https://github.com/inovex/justcause)** 

在因果关系方法的研究中培养良好的科学实践的框架. 



**[reformer-pytorch](https://github.com/lucidrains/reformer-pytorch)**

Reformer, the Efficient Transformer, in Pytorch.

**[gpt2bot](https://github.com/polakowo/gpt2bot)**

你的新伙伴使用`DialoGPT`接受`Reddit`讨论训练. 

> 进化中

**[django-migration-linter](https://github.com/3YOURMIND/django-migration-linter)**

为你的·django·项目检测向后不兼容的迁移. 

**[pytorch-metric-learning](https://github.com/KevinMusgrave/pytorch-metric-learning)**

在应用程序中使用度量学习的最简单方法. 模块化,灵活性和可扩展性. 用`PyTorch`写的. 

> 大多见名知意

**[Fliks.XYZ](https://github.com/gokhj/Fliks.XYZ)**

简单的`Flask`应用程序,以搜索电影/电视节目跨按需服务. 

> flask  不容易!



## 活动和网络研讨会日程

[New York Python Meetup Talk Night January 2020 - New York, NYC](https://www.meetup.com/nycpython/events/267314589/)
将会有以下话题:

- CPython内部机制---内存管理
- 如何使用Densepose制作超级英雄

[Upgrading your application to Python 3 + NLP - London, UK](https://www.meetup.com/LondonPython/events/267993272/)
将会有以下话题:

- 现在是2020年,你的Python 2.7应用程序正式成为一个问题

- 自然语言处理


[PyLadies/PyData 2020 Kick-off Talk Night - Toronto, ON](https://www.meetup.com/PyLadies-Toronto/events/267691300/)
将会有以下话题:

- 提高NLP的法律解释能力
- 用Altair实现数据可视化
- PyWats



## Posa:

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

迟来的,新年快乐!!!!!



----- 分割线 -----

> 如果你发现哪里翻译有误的话,请务与我联系!感谢!
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-433.html)
- 改进: [issue-433.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23433.md)


