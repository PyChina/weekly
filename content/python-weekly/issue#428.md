Title: pythonista-weekly : Pyw 428
Date: 2019-12-14 15:16
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-428

### 欢迎阅读"pythonista周刊"第428期. Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-428](https://mailchi.mp/pythonweekly/python-weekly-issue-428)  
>翻译:Dustyposa

### 来自赞助商(PS:原文的赞助商):
**[python开发者都需要的Vettery](https://www.vettery.com/tech?utm_source=newsletter&utm_medium=pythonweekly&utm_term=tech&utm_content=grouped&utm_campaign=ad-77579)**  

Vettery是一个招聘网站,它改变了人们应聘或者雇佣的方式. 准备好换工作地方了吗?免费制作简历,你的薪资你说了算,现在就和顶级雇主的HR联系吧!



## 新闻

**[SciPy 2020 意见征集](https://www.scipy2020.scipy.org/)**

征求建议书截止到2020年2月11日. 




## 文章,教程与话题
**[训练自定义dlib形状预测器](https://www.pyimagesearch.com/2019/12/16/training-a-custom-dlib-shape-predictor/)**

在本篇教程中,你将学习如何训练你自己的自定义`dlib`形状预测器*(shape predictor)*. 然后你将学习如何拿到的经过训练的`dlib`形状预测器,并使用它去预测输入的图像和实时视频流的坐标. 

> 微妙的五官捕捉. 

**[如何使用Django 框架做密码校验](https://www.youtube.com/watch?v=SRYBDmJlIck) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)*(15min)***

`Django`有内置的密码校验功能. 这个视频演示了如何开启并配置校验,自定义校验设置,编写你自己的校验器,并将验证集成到你自己的接口或者`API`中. 

> Django 内置了很多工具,来瞅一下. 

**[用数据科学的方法计算出一辆二手车的合理价格](https://t.co/sVcObePjlO)** 

使用`DS`*(译者注:应该是`data science`的缩写. . )*方法计算二手车公平价格的整个过程. 

> 似曾相识. 

**[100万对任何人来说都应该足够了](https://lwn.net/SubscriberLink/807218/7589bd420fa9cfbe/)**

编程语言在其操作的各种方面通常都会有些显示或者隐式的限制. 比如标识符*(identifier)*的最大长度或者一个变量可以存储的值的范围等明显的例子,但是还有其他的,其中许多不是语言设计者指定的,但是来自语言的各种实现. 这种模棱两可会出现问题,所以在`Python`中确定各种各样的限制是当前在`python-dev`邮件列表中持续讨论的目标. 

> 左右两难
>
> 不过巧了,最新的 捕蛇者说 (Ep09) 有提到这个问题. 



**[劫持(hijacking)Django 默认的'Through' Tables](https://typenil.com/hijacking-default-django-through-tables/)**

去年有几次我遇到了需要向一个`Django`多对多关系中添加一些元数据. 默认情况下,没有明确的模型可以添加字段,但是如果你在开发一个灵活的项目-在默认的`through`表中存在一些数据,你并不想丢失这些数据. 所以,如果你不想创建一个新的表并迁移数据该怎么解决呢?让我们劫持一个!

> 不够打补丁. 



**[为什么人们喜欢这个强大的Python新闻邮件?](https://powerfulpython.com/newsletter/?utm_source=pythonweekly&utm_medium=newsletter&utm_campaign=2019-12-19)**

"非常感谢精彩的新闻邮件!我期待着你的邮件. ""Python needs tougher treatment than what's out there. Keep going, don't ever stop."针对中级的`Python`. 现在就免费订阅吧!SPONSOR



**[我如何用旅行推销员问题拯救圣诞节](https://t.co/LGeDuqINzt)** 
圣诞老人最佳行程的可视化. 

> 圣诞老人选择路线的最优解. 

**[用Vue和Django构建一个CRUD应用](https://codesource.io/build-a-crud-application-vue-and-django/)**

这篇教程向你展示了如何用`Django REST Framework`构建一个`API`并用`Vue.js`构建一个`SPA`. 

> 熟悉的CRUD

**[使用Scrapy轻松抓取网页](https://www.scrapingbee.com/blog/web-scraping-with-scrapy/)**

`Scrapy`是`Python`中最受欢迎的爬虫框架. 在本篇教程中,我们将会看到如何用`Scrapy`从`scratch`中抓取一个电商网站. 

> 久违的爬虫教程. 

[让CPython出现段错误的5行代码 ](https://gist.github.com/coolreader18/6dbe0be2ae2192e90e1a809f1624c694)

> 太过自由?

[一个极小的 Python Exception 怪事](https://aroberge.blogspot.com/2019/12/a-tiny-python-exception-oddity.html)

> 版本的一致性不,还是比较让人困扰的. 

[用Fisher-Jenks算法查找数据的自然断点](https://pbpython.com/natural-breaks.html)

[使用pyenv管理你的Python解释器](https://www.marc-richter.info/using-pyenv-to-manage-your-python-interpreters/)

[基于约束的图形设计实验](https://www.anishathalye.com/2019/12/12/constraint-based-graphic-design/)

[通过无损压缩减少NumPy内存的使用](https://pythonspeed.com/articles/numpy-memory-footprint/)



## 有趣的项目,工具和库


**[Batea](https://github.com/delvelabs/batea)**
基于上下文检测的网络设备排名框架. 

**[BMW InnovationLab](https://github.com/BMW-InnovationLab)**

宝马已宣布发布其用于生产的人工智能算法,供任何感兴趣的人使用. 

> 宝马!原来还有这种操作. 

**[coding-problems](https://github.com/MTrajK/coding-problems)**

各种各样的编程/算法问题的解答,并有很多有用的资源用来学习算法和数据结构. 



**[NVDashboard](https://github.com/rapidsai/jupyterlab-nvdashboard)**

用于显示GPU使用情况的一个`JupyterLab插件`. 

> GPU 监听中. 

**[PrettyErrors](https://github.com/onelivesleft/PrettyErrors/)**

美化`Python`错误输出,让其更清晰. 

> 的确美多了. 

**[ward](https://github.com/darrenburns/ward)**

一个现代的Python测试框架,旨在帮助你发现并修复缺陷. 

> 待观察. 

**[YouTube-Report](https://github.com/A3M4/YouTube-Report)**

生成你的个人`YouTube`报告. 



**[attack_range](https://github.com/splunk/attack_range)**

一个允许您创建易受攻击的本地或云环境的工具,以模拟针对的攻击并将数据收集到`Splunk`中. 

> 自攻自守

**[twcloud](https://github.com/minimaxir/twcloud)**
Python 包 + CLI 来生成Twitter推特词云图.  

> 实战开启?

**[CuteUID](https://github.com/alexdredmon/cuteuid)**

生成可爱的`uid`,即在外观上与`uuid`相似的唯一标识符(ish). 

> 见名知意,看了一下,相当可爱. . 

**[ogb](https://github.com/snap-stanford/ogb)**

`Pytouch`中图机器学习的开源基准测试库. 



**[Andriller](https://github.com/den4uk/andriller)** 
带有智能手机取证工具集合的软件实用程序. 它从安卓设备上执行只读,法医学声音,无损采集. 

> 扩展业务面!

**[Neuraxle](https://github.com/Neuraxio/Neuraxle)**
`Neuraxle`是一个机器学习(ML)库,用于构建整洁的管道,提供正确的抽象来简化您的ML应用程序的研究,开发和部署. 

## 最近更新

[Django security releases issued: 3.0.1, 2.2.9, and 1.11.27](https://www.djangoproject.com/weblog/2019/dec/18/security-releases/)

[Poetry 1.0.0](https://python-poetry.org/blog/announcing-poetry-1-0-0.html)

> 它它它来了!管理工具一把手?



## 活动和网络研讨会日程

Nai

## Posa:
> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  





----- 分割线 -----

> 如果你发现哪里翻译有误的话,请务与我联系!感谢!
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-428.html)
- 改进: [issue-428.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23428.md)


