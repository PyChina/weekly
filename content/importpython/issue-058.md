Title: 蠎加载 58
Slug: importpython-58
Date: 2016-01-22 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 58](http://importpython.com/newsletter/no/58/)

## 该读
~ 文章, Blog, 教程...



- [ImportPython 工作委员会更新 以飨读者](http://www.importpython.com/jobboard/)
    + job market

工作栏启用已有半年,
至少收到了3封正式的感谢信,因为帮助团队找到了合适的程序猿.
无法更加高兴了!
去年一共25则岗位信息,平均每期3则.
如果你对全球靠谱的程序猿/媛有需求,
请尝试我们这儿完全免费的工作栏吧!

(`是也乎:`

只是鉴于中文世界,大家都没什么好渠道直接肉身翻越出去,
所以,工作栏这一章节,一般是清空的,间或有朋友委托发布过几则信息.
当然的,如果你想在 蠎周刊上发布免费的 Pythonista 招聘信息,请向大妈邮件说明:

    zoomquiet+HR[AT]gmail.com

)


- [讨论 - 对于 WSGI 2.0 你认为应该和不应该的?!](https://mail.python.org/pipermail/web-sig/2016-January/005357.html)
    + web framework

又是新的一年, 对于 WSGI 2.0 也更加急迫了.
可惜的是过去一年, 在 Rob Collins 领导下并没有完成相关承诺.
在网络中引发的讨论,也反映出开发者们对 WSGI 的限制很不舒服,
直接体现在应用和服务开发者都在尝试就 WSGI 的退出整理为一个框架,
以便更加契合现代 web 开发.
特别是  Andrew Godwin 在 Django 中提出的 channels 概念,
这代表应用开发者在远离 WSGI 的一种选择....


- [用 Python, Selenium, Django 测试 Web Apps. 对 Harry Percival 的采访.](http://pythontesting.net/podcast/harry-percival-pt009/)
    + podcast

如果在开发/测试 web 应用,特别是基于 Django 的,
一定非常喜欢这一期的内容.

嗯哼, Harry Percival 还是 "The GOAT book" 的作者 !-)


- [[教程]: 部署 Python 3, Django, PostgreSQL 到 AWS Elastic Beanstalk | Jameson Ricks](https://jamesonricks.com/?p=159)
    + django , aws

大家都知道 AWS 的服务切换是怎么来的.
能搜索出来有关使用 Elastic Beanstalk 部署 Django 应用的文章都太老旧了,
所以最新的有关 Python 3 的部署手册来了


- [通过补丁来理解 CPython – 第一部分](https://orenmn.wordpress.com/2016/01/16/understanding-cpython-by-patching-part-4/)
    + core python

过去一年多的时间里, 作者对 CPython 进行了一些尝试
整理为四篇文章的系列,值得一观!

(注意,提及的精彩之处都是在 Python 3 背景中的 CPython). 


- [PyCharm 入门视频教程](http://feedproxy.google.com/~r/Pycharm/~3/jF-S83DB134/)
    + pycharm

一直以来都是用户在热烈的为 PyCharm 制作教程的,
现在终于有官方的系列视频教程了!

- [3分钟实用 Python GIL](https://blog.ssundarraj.me/the-python-gil-in-2-minutes-80d74d56a1a0)
    + gil

多线程一直是很多新人或是老手都困惑的概念.
Python 使用的 GIL 又追加了一层混乱.
从来没有被清晰的阐述过.
那么尝试用 3分钟 说清楚这几个对象!

(`是也乎:`

又一位印度程序猿在 PyCon 上的演讲;
当然不止 3分钟,哥整整曰了46分钟!

)

- [Django 中的 SQL 查询检验器](https://github.com/dobarkod/django-queryinspect#readme)
    + django

Query Inspector 是个中间件,
对 Django 应用中所有 web 请求涉及的 SQL 查询进行检验和报告.

- [在 Python 中学习函数式编程的资源?](http://www.reddit.com/r/Python/comments/4144js/resources_for_learning_functional_programming_in/)
    + core python

来自伟大的 reddit!

- [无需停机平滑部署 Django 应用](https://medium.com/@healthchecks/deploying-a-django-app-with-no-downtime-f4e02738ab06#.1fcfu4907)
    + django

当 healthchecks.io 
开始承受每秒超过一次要求时,
就不能随意重启服务了.
对于监控服务,当然不能错过任何一次 http 请求!
所以,...


- [PyCon 现在接受财政援助](http://pycon.blogspot.com/2016/01/now-accepting-financial-aid-applications.html)
    + pycon

如果你在寻求 票务或是其它财务援助,现在就有了.


## 新书
~ New Books

- [现实世界的机器学习](http://importpython.com/books/525/real-world-machine-learning/)

现今, 大数据已经是 `近实时` 决策关键支撑了,
机器学习(ML)是数据工作流的重要组成部分.

ML 可以快速从海量信息中提取和匹配决策,
甚至于超过人的直觉认知.

这些系统使用复杂的计算和统计工具来建立模型,
可以识别可视化的模式,预测结果,并提出建议!

## 项目
~ 包/模块/库/片段...



- [TrumpScript](https://github.com/samshadwell/TrumpScript)
    - 1033 Stars, 48 Fork

令 Python 再次伟大!
特别针对美国读者: 请认真理解 Donald trump 吧!

(`是也乎`:

基于唐纳德·特朗普的修辞手法的编程语言 [Coders Assimilate Donald Trump to a Programming Language | Inverse](https://www.inverse.com/article/10448-coders-assimilate-donald-trump-to-a-programming-language)

真爱!

![examplescripttooutput](http://i1.wp.com/media.boingboing.net/wp-content/uploads/2016/01/examplescripttooutput-shows-a-more-complex-bit-of-trumpscript-at-the-top-after-the-first-cat-comm1.png?w=970)

)


- [spaceShooter](https://github.com/prodicus/spaceShooter)
    - 71 Stars, 11 Fork

用 Pygame 重制的经典游戏!

- [pick](https://github.com/wong2/pick)
    - 59 Stars, 3 Fork

帮助我们在终端中进行交互式列表选择的库.


- [tornaREST](https://github.com/nekocode/tornaREST)
    - 44 Stars, 4 Fork

:cyclone: 基于 Tornado 实现的简洁 RESTful web 服务.

- [kaggle-right-whale](https://github.com/felixlaumon/kaggle-right-whale)
    - 25 Stars, 5 Fork

2nd place solution to the Kaggle Right Whale challenge

- [reality-of-Dream-of-Red-Mansions](https://github.com/Huangtuzhi/reality-of-Dream-of-Red-Mansions)
    - 20 Stars, 12 Fork

对红楼梦前80章和后40章的用词进行比对!

- [PrettyPandas](https://github.com/HHammond/PrettyPandas)
    - 17 Stars, 0 Fork

美化 Pandas 表格输出的样式表


- [github_reviewer](https://github.com/gabrielhora/github_reviewer)
    - 16 Stars, 1 Fork

使用 GitHub Webhooks 以及 Commit Status API 
来控制 pull requests 的评审


- [fython](https://github.com/nicolasessisbreton/fython)
    - 9 Stars, 0 Fork

fython 就是用 Python 语法的 Fortran 

(`是也乎:`

老树新花儿!
)

- [git-money](https://github.com/21hackathon/git-money)
    - 7 Stars, 0 Fork

通过 github 中的 pull requests 来赚钱!

- [loadcf](https://github.com/singpenguin/loadcf)
    - 6 Stars, 1 Fork

python 配置文件加载器

- [notebook-api](https://github.com/jefersondaniel/notebook-api)
    - 5 Stars, 0 Fork

Rest API for notes, uses Python Flask, Mongo, Behave and Docker-Compose

- [logen-trace](https://github.com/perhapsspy/logen-trace)
    - 5 Stars, 0 Fork

Delivery confirmation for Logen(https://www.ilogen.com)



## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 160122 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160122 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


