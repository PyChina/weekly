Title: 蠎加载 29
Slug: importpython-29
Date: 2015-04-24 00:42
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 29](http://importpython.com/newsletter/no/29/)

## 该读
~ 文章, Blog, 教程...


- [反模式python迷你书](http://docs.quantifiedcode.com/python-anti-patterns/)
    + 核心  

欢迎各位Pythoneer !这是一本讲述Python反模式和最差实践的迷你书. 学习这些反模式将会帮助你避免这种情况出现在您自己的代码中,让你成为更好的程序员(希望). 每个模式都有一个小的描述,例子和可能的解决方案. 


- [Python播客#3: Pyramid Web框架](http://www.talkpythontome.com/episodes/show/3/pyramid-web-framework)
    + pyramid  

 加入迈克尔和克里斯·麦克唐纳关于Pyramid web框架的对话. 您将了解Pyarmid是一个什么样的框架以及它和Django,Flask,Bottle等框架的差别. 

- [Python类型提示](http://feedproxy.google.com/~r/blogspot/pydev/~3/d7PzLWWGAb4/type-hinting-on-python.html)  

如果你错过了它,现在看来还有很长的线程类型提示相关PEP. 最主要的要早些时候提出正在错误的做类型检查. 

- [Customize Python Notifications For Finding Apartments and Close NBA Playoff Games](https://racketracer.wordpress.com/2015/04/17/customize-python-notifications-for-finding-apartments-and-close-nba-playoff-games/)
    + web 抓取  

NBA实时比分的API已经有了,但我想做一个使用Komono的chrome扩展来实现快速抓取. 
(`注:`我不为他们工作,他们只是有一个很酷的产品)
. 首先,我们必须抓住我们认为很重要数据的ESPN NBA主页. 其中包括主队的名字,团队名称,分数,得分时间. 

- [PyPI一年下载的分析](https://caremad.io/2015/04/a-year-of-pypi-downloads/)
    + PSF

一年多前我们开始归档所有PyPI生成的日志,今天我们会看看这些日志,看看各种事情发生了变化. 这些数据解析自从PyPI下载文件的工具的user agenet,因为它的可靠性依赖于这些数据的可靠性. 


(`是也乎:`

![pip 使用 Py 版本统计](https://caremad.io/images/a-year-of-pypi-downloads/stacked-py-pct.png)

是也乎,(￣▽￣), 果断是 Py2 赢了!

)

- [使用pytest进行测试](http://stefan.sofa-rockers.org/2015/04/22/testing-coroutines/)
    + testing  

Pytest为Python是一个很棒的测试包. 它让编写测试真的很容易,测试失败的报告功能非常有用. 然而,目前(版本2.7)并不在很大程度上帮助你测试(asyncio)协同程序. 

- [SQLAlchemy 1.0.0发布](http://www.sqlalchemy.org/blog/2015/04/16/sqlalchemy-1.0.0-released/)
    + 最新发布

- [Python在3D动画情节上](http://www.reddit.com/r/Python/comments/32rwxu/animated_3d_plots_in_python/)
    + visualization  

在这里,我将演示如何使用Python和matplotlib创建这些可视化动画. 我所有的源代码可以在IPython笔记本可以找到. 最后,我们将生成数据可视化的动画. 

- [本周PyDev: Noah Gift](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/59CppxtXJHw/)
    + 采访

对Noah Gift的采访.


## 新书

- [Python自动化测试:实用编程初学者总额](http://importpython.com/books/511/automate-the-boring-stuff-with-python-practical-programming-for-total-beginners/)
    + Albert Sweigart  

在使用Python进行自动化测试那些无聊的东西 ,您将学习如何使用Python编写做什么分钟将带你小时做手工程序. 一旦你掌握了编程的基础知识,您将创建的Python程序,轻松进行自动化的实用和令人印象深刻的壮举. 即使你从来没有写过一行代码,你可以让你的电脑做繁重的工作.  ImportPython与笔者的采访 - 阿尔伯特Sweigart我们的博客. 随意问的问题笔者在评论部分. 



## 项目
~ 包/模块/库/片段...



- [credstash](https://github.com/LuminalOSS/credstash)
    - 148 Stars, 7 Fork  

一个在云端进行证书管理的小工具

- [villoc](https://github.com/wapiflapi/villoc)
    - 101 Stars, 7 Fork  

堆操作的可视化

- [ezcf](https://github.com/laike9m/ezcf)
    - 68 Stars, 4 Fork  

配置文件导入的工具. ezcf意味着配置方便,它允许您导入JSON / YAML / INI / XML到py文件. 是非常有用当你从这些格式需要阅读的时候是非常有用的,尤其是阅读配置文件. 

(`是也乎:`
嗯啍,的确是非常实用的模块,
只是人类至今无法找到一个通用的,
开发语言无关的配置文件格式,
实在只能是醉了...

)

- [hooks](https://github.com/SirCmpwn/hooks)
    - 31 Stars, 0 Fork  

响应github的web hook请求并执行相应命令的服务

- [import-order](https://github.com/spoqa/import-order)
    - 30 Stars, 2 Fork  

对进口辞典编纂的顺序进行排序


- [segment](https://github.com/willf/segment)
    - 18 Stars, 3 Fork

一个基于频率和Viterbi算法的文本分割工具如:"#TheBoyWhoDied" => ['#', 'The', 'Boy', 'Who', 'Died']

(`是也乎:`
细思恐极! 这是代码分析的重心工具哪!
)


- [is-dirty](https://github.com/reddragon/is-dirty)
    - 15 Stars, 1 Fork  

一个简单的关键词过滤分类器

- [python-email-validator](https://github.com/JoshData/python-email-validator)
    - 2 Stars, 0 Fork  

一个强大的Python3.x电子邮件的语法验证库.


## 工作
- [SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!

- [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
四月急招 N 名有服务端开发经验的 **gopher**!


- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
5月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!



## DAMA
(`大妈私人无责任播报`)

~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 150426 [spawnris](https://gitcafe.com/spawnris) 通过 PR 完成[13160ba3](https://gitcafe.com/CPyUG/weekly/commit/13160ba3c8216f1ade4a1b3e4f17f0de4e5a198b) 
- 150423 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
