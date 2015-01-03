Title: Issue 16 ~ 规则胜于特例 
Date: 2012-06-01 
Tags: Weekly,Pycoder,Zh 
Slug: issue-16 
# Hi Pythonistas. 

本周的新闻并不是很多,不过贴纸的事情倒是有很多要说的,我们这星期会收到新设计的贴纸,所以赶快给我们寄来回邮吧,我们的地址是:

    44 Byward Market Square, Suite 210

    Ottawa, Ontario Canada

    K1P 7A2

RSS 订阅和存档可以在 [这里](http://feeds.feedburner.com/pycodersweekly) 和 [这里](http://pycoders.com/archive.html) 找到. 

[戳这里](https://twitter.com/#!/pycoders) 和我们签订契约成为魔法少女(少年).  (◕‿‿◕)



Enjoy!


--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #16) : Special cases aren't special enough to break the rules.](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=07c5d1307c)


## 新闻与开发动态

- [Light Table](http://www.kickstarter.com/projects/ibdknox/light-table?ref=users)
虽然这个东西在之前的邮件中已经说过了,但是现在还是有必要再说一下, Light Table 现在已经筹集到足够的资金来开发 Python 支持,我们很高兴能够看到像视频中一样的 Flask 支持. 

- [Radio Free Python - 第八期](http://radiofreepython.com/episodes/8/)
最新一期的 Radio Free Python ( Python 每月 Podcast ),本期采访了来自冰岛 CCP 公司(以制作 Eve Online & DUST 514 知名的游戏公司)的 
[Kristjan Valur Jonsson](http://blog.ccpgames.com/kristjan/)
,讨论了关于 
[Stackless Python](http://www.stackless.com/)
 以及其应用在 Eve Online 中的话题. 


## 讨论

- [Python 与 C](http://www.reddit.com/r/Python/comments/u9by4/coming_to_python_from_c_writing_this_finally_made/)
当一个 C 程序员开始学习 Python 的时候会出现什么样的情况呢?在这篇讨论里,作者贴了一段很简单的从 C 语言转换到 Python 的代码,从而引出了一系列对这段代码的优化,从这篇讨论中,我们或许能够了解如何用更加 Python 的方式来解决问题,如果你刚开始学习 Python,认真的读一下这篇讨论吧. 



## 项目

- [workflow](https://github.com/mdipierro/workflow)
Workflow 是一个单文件的小项目,用于解决某些周期性的工作,比如删除或移动文件,运行脚本之类的. 

- [webxray](https://github.com/hackasaurus/webxray)
这个项目的文档中写道:"Web X-Ray 眼睛为非技术宅提供了一个简单的方式去剖析页面,了解他们是如何运作的", webxray 提供了一个书签,在你需要的页面点一下书签就可以方便快捷的得到关于这个页面的所有信息了. 

- [django-discover-runner](https://github.com/jezdez/django-discover-runner)
一个基于 unittest2 的 Django 单元测试模块,
它解决了如何运行基于Django项目结构的测试问题. 
让你把测试可以放置Django项目的结构外,仍然可以随时运行测试套件. 

- [dnspython](https://github.com/rthalley/dnspython)
dnspython 是一个用 Python 写的 DNS 工具箱,换言之, dnspython 是一个一站式的 DNS 解决方案,它几乎支持所有的记录类型,同时也可以被用作解析,区域转移 (zone transfers)和动态更新(Dynamic updates)等. 


## 文章

- [Mongrel2&Circul = web栈的完全控制](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue16/mongrel2-amp-circus-full-control-of-your-web-stack.html)
由于配置 [Gunicorn](http://gunicorn.org/) 失败.. Tarek Ziadé 决定用 Mongrel2 & Circus 来建立一个 WSGI 栈,自己的进程管理器. 这篇文章介绍了如何建立一个网络堆栈,如果你并不想使用传统的 Gunicorn ,可以读一下这篇文章. 

- [不要使用散点图!](http://www.chrisstucchio.com/blog/2012/dont_use_scatterplots.html)
在这篇文章里,作者讨论了为什么散点图对于可视化数据来说很不好,并且建议应该绘制密度图而不是散点图,同时作者也提供了一些生成图形的 Python 代码,这些代码对你的数据展示工作或许会有帮助. 

- [奇怪的 Python 本地线程](http://emptysquare.net/blog/pythons-thread-locals-are-weird/)
这篇文章很好的解释了 Python 中本地线程的奇怪之处,作者比较了新版本与旧版本 Python 的本地线程的不同之处,读一下吧. 

- [RQ Tips](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue16/rq-tips.html)
[RQ](http://nvie.com/posts/introducing-rq/)
是最近发布的一个任务队列处理库,对于任务队列我们更常用 [Celery](http://celeryproject.org/)
 ,不过 [RQ](http://nvie.com/posts/introducing-rq/) 仍然是一个不错的选择,因为他仅仅依赖 Redis ,所以比起 [Celery](http://celeryproject.org/)
  , [RQ](http://nvie.com/posts/introducing-rq/) 要更易于管理,这篇文章中介绍了许多关于在生产环境中部署 [RQ](http://nvie.com/posts/introducing-rq/) 的提示. 


# 是也乎

转自: [Issue #16: 规则胜于特例 — PyCoder's Weelky CN](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue16/index.html)



