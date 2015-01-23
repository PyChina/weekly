Title: Issue 1 ~ 亮了吧! 
Date: 2012-02-17 
Tags: Weekly,Pycoder,Zh 
Slug: issue-1 

# Hi Pythonistas. 

面对超过3000的订阅,
还在继续汹涌而来的请求,我们真的已经不堪重负!
当前我们只有几个毛人在进行收集以及发送工作.
不过,大家这么给力,我们一定为大家作好这事儿!

希望你喜欢这儿!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #1) : Let there be light.](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=e9564edf16)


## 新闻与开发动态

- [Tornado 2.2](http://www.tornadoweb.org/documentation/releases/v2.2.0.html)

本次发布,对 Twisted的兼容 以及 WebSocket 的支持进行了高大升级



- [Django 1.4 Beta 1 发布](https://www.djangoproject.com/weblog/2012/feb/15/14-beta-1/)

James Bennett, 已经宣告最新版本已经进入测试阶段. 
[James](https://twitter.com/#!/ubernostrum)
正式呼吁社区帮忙折腾,杀虫,以便在三月完成 1.4 版本的发布.
可以从 [这儿](https://www.djangoproject.com/download/).
获得最新clone, 嗯嗯嗯,他们已经不在对 Python2.4 进行测试了..



- [Mock 0.8](http://www.voidspace.org.uk/python/weblog/arch_d7_2012_02_11.shtml#e1234)

大家最爱的 模拟庉已经发布最新版本!
[Michael Foord](https://twitter.com/#!/voidspace)
曰,这是一次非常巨大的变化,
并应允将通过 Blog 详细说明,



- [最新 Pip and Virtualenv 发布](https://twitter.com/#!/carljm/status/170249145376980993)

Carl Meyer, 宣布最新pip 以及 virtualenv将包含更多优秀工具.



- [Py3K 状态更新](http://morepypy.blogspot.com/2012/02/py3k-status-update.html)

Antonio Cuni, 一直以来孜孜不倦的支持 PyPy 成功迁移到 Python3 上.
[Antonio](https://twitter.com/#!/antocuni)
刚刚更新了捐助列表,感谢大家对项目的支持!


- [Pypy 1.8 -- 照常发布](http://morepypy.blogspot.com/2012/02/pypy-18-business-as-usual.html)

PyPy 的小伙伴们没有升级的要赶紧了!
成吨的bug 已经修复,太多更新以及内存效率的提升,是时候离开 1.7 了


## 讨论

- [SQLAlchemy Vs. Django ORM](http://www.reddit.com/r/Python/comments/p03yh/sqlalchemy_vs_django_db/)

此问题引发的一系列讨论收集在:
[/r/python](http://www.reddit.com/r/Python/)
最初还比较 Naive, 但是,很快引发了有关 两者稳定性和鲁棒性的深入对比
[Mike Bayer](https://twitter.com/#!/zzzeek)
 (SQLAlchemy's 作者) 介入讨论相当早,并给出了他的看法.

- [PyCon Web Development Summit 2012 Panel Discussions](http://www.google.com/moderator/#16/e=1c9a94)

如果你错过了今年 PyCon 的注册,现在可以通过此表单提交你的问题,并针对今年的讨论议题投票.

## 项目

- [Django-JHouston](https://github.com/pennersr/django-jhouston)

"休斯敦,我们有一个Javascript的问题!"
这个项目能将浏览器中的JS 错误抓到数据库中,支持调试以及日志.
这对以往测试过程中难以追踪的JS 错误将非常有帮助.
[@pennersr](https://twitter.com/#!/pennersr)


- [mitmproxy](https://github.com/cortesi/mitmproxy)

mitmproxy 是支持 SLL 的中间件(man-in-the-middle-proxy).
支持 HTTP(等)协议在传输过程中进行编辑以及调试.
不仅仅是对路由的判定,允许你探知远程服务器接收到的是类型的数据!
[@cortesi](https://twitter.com/#!/cortesi)


- [Django Pancake](https://github.com/adrianholovaty/django-pancake)

关注性能的 Dj 模板.
存储展开后的模板, 在某些情况下比默认的模板能更快的执行.
[@adrianholovaty](https://twitter.com/#!/adrianholovaty)


- [PBS](https://github.com/amoffat/pbs)

PBS 是种特殊的子进程包装模块,
能将Python 的动态函式绑定到系统软件!
可以非常方便的将调用系统中的常见软件比如: ls, curl, cd 等等.
PBS 提供了很干净的界面,帮助我们应用在脚本代码中.


## 文章

- [Running Sentry on DotCloud](http://kencochrane.net/blog/2012/01/running-sentry-on-dotcloud/)

Sentry 是开源实时软件日志聚合系统.
Ken 提供了如何在 DotCloud 进行安装运行的全套教程.
只需要一步步照作就可以完成,
并提供了一个 DotCloud 的可部署仓库,来引导完成 Sentry 的安装.
感谢 Ken 的工作!


- [Advice for PyCon Speakers.](http://readthedocs.org/docs/ref/en/latest/advice_for_pycon_speakers/index.html)

想在 PyCon 上演讲,首先要提升你的演讲水平!
[Eric Snow.](http://ericsnowcurrently.blogspot.com/)
分享了其中的秘诀, 针对演讲的构思,幻灯的制作 等等方面提供了建议,
甚至于过程中,应该注意的以及避免的要点!


- [Virtualenvwrapper 3.0 with Python 3 support.](http://blog.doughellmann.com/2012/01/virtualenvwrapper-30-python-3-support.html)

Virtualenvwrapper 是
[Ian Bicking](https://twitter.com/#!/ianbicking)
的 virtualenv 的扩展工具集.
随着3.0 的发布,已经支持了 Py3, 这令大家感到, 社区在全力支持 Py3 的实用化.



- [Generator Tricks for System Programmers[2008].](http://www.dabeaz.com/generators/)

由
[David Beasley](https://twitter.com/#!/dabeaz)
贡献的教程, 探讨了 "生成器" 以及 "生成器"表达式在编程上下文中的各种技巧.
每一节都提供了现实世界真实的工程案例代码段.

- [Defining a WSGI App Deployment Standard](http://tarekziade.wordpress.com/2012/02/10/defining-a-wsgi-app-deployment-standard/)

[Tareq Zaide](https://twitter.com/#!/tarek_ziade) 
将分享有关 WSGI 应用如何标准化以及他在 Mozilla 的实践.
俺是非常有兴趣在 PyCon 上 [Tareq](https://twitter.com/#!/tarek_ziade) 的演讲的.



- [Pythons Valentines day gift to Clojure](http://sunng.info/blog/2012/02/pythons-valentines-day-gift-to-clojure/)

嗯嗯嗯,空气中弥漫着浓浓的爱!
[Sung Ning](https://twitter.com/#!/sunng)
听说在 Ruby 社区已经在广泛的尝试 Clojure,
于是发布了开源工程:
 [Pyclj](https://github.com/sunng87/pyclj)
用Python 来读写 Clojure 的数据文本.


- [Python Performance Tips - Pt.1.](http://blog.monitis.com/index.php/2012/02/13/python-performance-tips-part-1/)

文章开头就吼,Python 的运行速度比不过那些编译型语言.
明显作者没听说过 PyPy. 
不过,给出的一系列技巧,值得我们反复体验!

- [Python Web Framework Roundup](http://www.konstruktor.ee/blog/python-web-framework-roundup)

收集了很多 Python web 框架,
以及特性/发布日期等等描述, 统一使用 COOL 等级标注.
当然的, 少不了的'Hello World!' 的示例.
Thanks 
[Madis Väin](http://www.konstruktor.ee/about)!


- [Who's on Python 3?](http://py3ksupport.appspot.com/)

是个伟大的仪表板,
可以关注前50大Python 项目对 Python 3 的支持程度.
你可以从 [这儿](http://bcannon.googlecode.com/hg/sites/py3ksupport-hrd/)
获得源代码!
由 [Brett Cannon](https://plus.google.com/115362263245161504841/about).
贡献!

- [Python Logging Best Practices](http://www.robg3d.com/?p=906)

想对内置日志模块最细微处也能理解一,这绝对是篇好文章!
[Rob](http://www.robg3d.com/)
还同时提供了幽默的阅读体验!



# 是也乎

第一篇 Pythonista 周刊,现在再看,依然可以感受到澎湃的 Pythonner 豪情!

- 131019 用时57分钟完成翻译.
- 131019 [Zoom.Quiet](http://zoomquiet.org/) 用时57分钟完成快译.
