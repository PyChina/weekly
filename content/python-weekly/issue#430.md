Title: pythonista-weekly : Pyw 430
Date: 2020-01-04 15:16
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-430

### 欢迎阅读"pythonista周刊"第430期. Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-430](https://mailchi.mp/pythonweekly/python-weekly-issue-430)  
>翻译:Dustyposa

**来自赞助商(PS:原文的赞助商):**  
[python开发者都需要的Vettery](https://www.vettery.com/tech?utm_source=newsletter&utm_medium=pythonweekly&utm_term=tech&utm_content=grouped&utm_campaign=ad-77579)  
Vettery是一个招聘网站,它改变了人们应聘或者雇佣的方式. 准备好换工作地方了吗?免费制作简历,你的薪资你说了算,现在就和顶级雇主的HR联系吧!


## 文章,教程与话题
[Making Python Programs Blazingly Fast](https://martinheinz.dev/blog/13)

`Python`厌恶者总是说他们不想使用`Python`的理由之一就是太慢了. 是的,对于特定的程序(无论使用何种编程语言),快或者慢都是非常依赖编写它的开发者自身编写优秀和快速代码和的技能和能力. 所以,让我们证明某些人的错误观点并让他们看看我们可以如何提升我们的`Python`程序的性能,让它变得飞快!

> 性能提升第一弹!

**[Numba makes Python 1000x faster!](https://www.youtube.com/watch?v=x58W9A2lnQc)** ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)*(20min)*

在此视频中,我介绍了你需要了解的有关`Numba`的绝对最低要求,`Numba`是针对`Python`和`Numpy`子集的即时编译器. 前半段的视频是一些基本介绍和强调了一些人们使用`Numba`时经常犯的错误. 视频的剩余部分呈现了一个真实世界的模拟问题,在单和多线程的情况下使用`Numba`速度提升都达1000倍以上,最后以一个能够学习更多关于`Numba`知识的`"阅读清单"`结束. 

> 第二弹!

**[如何一起使用 gevent(uWSGI 和 Gunicorn版本) 和 Flask](https://iximiuz.com/en/posts/flask-gevent-tutorial)**

创建一个异步的`Flask`应用并在反向代理`Nginx`之后用`uWSGI 或者 Gunicorn`运行它. 

> `Flask` 异步之旅. 

**[ASGI介绍: 异步Python Web生态系统的出现](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/)**

现在在`Python web`开发生态系统中有一些激动人心的事情在发生---这项工作的主要驱动力之一是异步标准网关接口`ASGI`. 这篇文章面向的对`Python`网络开发的最新趋势感兴趣的人. 将会用导航带着你了解什么是`ASGI`,对现代的`Python web`开发意味着什么?

> 一浪高过一浪. 

**[为严重倾斜的类别分布培养直觉](https://machinelearningmastery.com/how-to-develop-an-intuition-skewed-class-distributions/)**

不平衡分类问题涉及到预测一个类标签,其中类标签在训练数据集中的分布是不相等的. 不平衡分类问题中类分布的差异会影响数据准备和建模算法的选择. 因此,对于不同的类分布的含义,实践者开发一种直觉是至关重要的. 在本教程中,您将了解如何为不平衡和高度倾斜的类分布开发实践直觉. 

> 经验的传授?

**[用 Jupyter 开发机器人](https://t.co/xe5GAgWia4)**

这篇文章展示了在`Jupyter`生态系统使用`Voilá`在`Jupyter Notebooks`和独立的网络应用中构建高级的可视化,以及如何部署这些`app`到`robotics cloud`中. 

> Jupyter 抢占开发?
>
> Not easy.

**[使用 NASA 图片和 Python 制作一个月亮动画](https://nicholasfarrow.com/Creating-a-Moon-Animation-Using-NASA-Images-and-Python/)**

这里是我们可以如何仅仅使用几行`Python`代码创作一个月亮视频. 

> 代表月亮...

**[使用Python & Tableau实现内部销售仪表板自动化|第2部分:收集实时库存数据](https://www.youtube.com/watch?v=kEVXjrt3LfA)** ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)*(36min)*

在这一部分,我们使用`pandas`数据读取器来位我们的内部交易仪表板收集实时的库存数据. 这里有很多有用的东西,比如使用`pandas`来计算移动平均线和读取`html`. 

> pandas 进阶之路
>
> 不过实战记忆效率高,不亏!

[Python字典101: 详细的可视化介绍](https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/)

> 异常详细!

[我没有感觉到异步压力](https://lucumr.pocoo.org/2020/1/1/async-pressure/)

> 我也希望没有压力. 

[用tf-idf和Python进行单词搜索](https://igor.mp/blog/2019/12/31/tfidf-python.html)

[Label smoothing with Keras, TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2019/12/30/label-smoothing-with-keras-tensorflow-and-deep-learning/)

[Meditations on the Zen of Python](https://orbifold.xyz/zen-of-python.html)

[如何在Python中使用Pandas的get_dummies 去创建虚拟变量](https://www.marsja.se/how-to-use-pandas-get_dummies-to-create-dummy-variables-in-python)

## 有趣的项目,工具和库

**[Typer](https://github.com/tiangolo/typer)**
`Typer`,可以构建出色的`CLIs`.  易于编码.  基于`Python`类型提示. 

> 正在寻找合适的,瞅一瞅. 

**[AI_Sudoku](https://github.com/neeru1207/AI_Sudoku)**

基于`GUI`的智能数独解题器,试着从一张图片中提取数独题并解决它. 

> 数独怎么解?肉眼一看就能解. 

**[klaxon](https://github.com/knowsuchagency/klaxon)**

来自`Python`的`Mac OS`通知. 



**[django-simple-task](https://github.com/ericls/django-simple-task)**

用于`Django 3`的简单的后台任务. 

> 新鲜的后台任务来了!

**[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)**

用于`FFmpeg`的`Python`绑定函数---具有复杂的过滤支持. 

> 无限调用

**[Traffic-Signal-Violation-Detection-System](https://github.com/anmspro/Traffic-Signal-Violation-Detection-System)**

使用`YOLO3 & Tkinter`及基于视频片段的计算机视觉的交通信号违章检测系统. (包括GUI)



**[pylightxl](https://github.com/PydPiper/pylightxl)**

一个轻量级,零依赖,轻量级功能的`excel`读/写的`Python`库. 



**[XSS-Finder](https://github.com/haroonawanofficial/XSS-Finder)**

重量级高级跨站点脚本扫描仪. 



**[Robatim](https://github.com/Sanseer/Robatim)**

`Robatim `是一个基于常见的练习曲模式的伪随机音乐生成器. 

> 练习曲的春天?

## 活动和网络研讨会日程

**[Austin Python Meetup January 2020 - Austin, TX](https://www.meetup.com/austinpython/events/lgrbmqybccblb/)**

`Jupyter notebooks`非常适合用来探索,尤其是分析和可视化. 然而,当用于开发一个库或者自包含代码的时候,我们可以发现我们自己会复制和粘贴到我们喜欢的文本编辑器或者`IDE`. 在本次演讲中,`Leanne Fitzpatrick`将介绍`nbdev`,这是`fast.ai`开发的解决此问题优雅的解决方案. 



**[CI/CD for Python on AWS - Glen Allen, VA](https://www.meetup.com/PyRVAUserGroup/events/kktcmrybccblb/)**

我们将会演示:

1. 如何为`Python`应用设置持续集成管道. 
2. 如何用`Python/Boto3`在`AWS`上实现持续部署. 



[PyMNtos Python Presentation Night #80 - Minneapolis, MN](https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/events/267385506/)

[San Francisco Python Meetup January 2020 - San Francisco, CA](https://www.meetup.com/sfpython/events/xkwxvqybccblb/)

[PyAtl Meetup January 2020 - Atlanta, GA](https://www.meetup.com/python-atlanta/events/xzzgcrybccbmb/)https://morepypy.blogspot.com/2019/12/pypy-730-released.html)

## Posa:
> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

热腾腾的协程翻译: **[异步爬虫](https://github.com/Dustyposa/goSpider/blob/master/python_advance/%E7%BF%BB%E8%AF%91%E8%AE%A1%E5%88%92/%E5%BC%82%E6%AD%A5%E7%88%AC%E8%99%AB)**

初次翻译,多多指教,发现问题请提提提出来!!谢谢各位大佬了. 

----- 分割线 -----

> 如果你发现哪里翻译有误的话,请务与我联系!感谢!
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-430.html)
- 改进: [issue-430.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23430.md)


