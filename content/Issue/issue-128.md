Title: Issue 128: 对,你能!
Slug: issue-128
Date: 2014-08-18 10:15
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Py万物 的周刊

亲,

这周Py社区又有很多好消息,值得关注.

大家的分享[文章](http://pycoders.com/submissions/) 
才能折腾出美好的一周呢.

另,用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!
以及 [twitter](http://www.twitter.com/pycoders)


--

原文: [Pycoder's Weekly (Issue #128): Yes you can!](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=339ce67508&e=889f3f6a05)

## 新闻

- [建议: 用mypy语法进行函式声明](https://mail.python.org/pipermail/python-ideas/2014-August/028618.html)

Jukka Lehtosalo(mypy 作者)在 Dropbox 中的谈话诱发下,
Guido 打开了有关使用 mypy 语法进行函式注释的 讨论.

python.org

Shared by @mgrouchy
 
(`译注:`又一个试图平衡Py 动态语言和静态编译优化矛盾的方案!
大妈认为,进行有限的静态式声明支持,从而大幅度的提升 Py3 的效能,
进而推动整体Py 社区的跃迁,是好事儿!-)


- [DjangoCon US 2014 大会议程发布](http://www.djangocon.us/schedule/)

今年是在 Portland , 俄勒冈州,
详细议程可以查阅鸟!

djangocon.us

Shared by @mgrouchy
 

- [欢迎新的联合主席以及明年的PyCon 城市!](http://pycon.blogspot.ca/2014/08/welcoming-new-co-chair-and-next-pycon.html)

Brandon Rhodes 已被任命为 PyCon2015 的 co-chair .
并且明年的主办城市也已明确  Portland, Oregon!

blogspot.ca

Shared by @myusuf3
 

- [Visual Studio Python 工具 2.1 RC](https://pytools.codeplex.com/releases/view/123624)


给 VC 配置的 Python 开发工具 2.1 候选发布版本刚刚释放,
如果你是 M$ 死忠,可以下载尝试了.

codeplex.com

Shared by @mgrouchy

  

## 讨论

- [Python 中 SLL 的 not-so-sorry](http://www.reddit.com/r/Python/comments/2dh026/the_notsosorry_state_of_ssl_in_python/)

reddit.com

Shared by @myusuf3

- [Python 中 SLL 的 not-so-sorry(原文)](https://developer.rackspace.com/blog/the-not-so-sorry-state-of-ssl-in-python/)

引发 reddit 上大讨论的文章来自:
Alex Gaynor 和 David Reid 
写的有关Py2.X 中TLS实现的问题,
以及他们准备从 Py3 降级回 Py2 在 2.7.9 版本中进行的增补.


rackspace.com

Shared by @mgrouchy


## 项目

-[turnstile](https://github.com/klmitch/turnstile)

实用! 分布式限速 WSGI 中间件.
用 redis 进行用户命中率管理和限速配置.

github.com

Shared by @mgrouchy
 

- [mypy](https://github.com/JukkaL/mypy)

支持在Python代码中,可选的静态类型声明.

github.com

Shared by @mgrouchy
 

- [pyrasite](https://github.com/lmacken/pyrasite)

对运行中的Py进程,注入代码!

github.com

Shared by @myusuf3
 

- [pythonpy](https://github.com/Russell91/pythonpy)

`python -c`, 
用 tab 键完成以及速记.


github.com

Shared by @mgrouchy
 

- [PyAPNs](https://github.com/djacobs/PyAPNs)

用于 APNs(Apple推送服务) 交互的 Python 库.

github.com

Shared by @myusuf3
 

- [queries](https://github.com/gmr/queries#readme)


psycopg2 的一个包装,包含简化API,
PyPy 支持, Tornado 的异步支持,以及更多.

github.com

Shared by @mgrouchy
 

- [hashids-python](https://github.com/davidaurelio/hashids-python)


JavaScript hashids 实施的 Py 支持.

github.com

Shared by @mgrouchy

(`译注:`
非常实用的 Youtube 式 hashid 的生成库,
省的我们自个儿折腾内置的缩址算法了.)

- [flocker](https://github.com/ClusterHQ/flocker)

Easily manage Docker containers & their data! Check out the main site here

轻松管理 Docker 容器及其数据!
看
[这儿](https://clusterhq.com/)
有详情.

github.com

Shared by @myusuf3
 

- [ipython-vimception](https://github.com/ivanov/ipython-vimception)

令你在 `IPy[:]nodebooks` 中用 Vim 的快捷键来折腾.
够装逼.

github.com

Shared by @mgrouchy

(`译注:`不日 Emcas 的键绑定也必然会出现;-) 

- [pip-autoremove](https://github.com/invl/pip-autoremove)

自动移除实际上没有用的包.

github.com

Shared by @myusuf3
 
(`译注:` 这个超级实用哪) 

- [jumprun](https://github.com/itsnauman/jumprun)

A command-line tool for running scripts from any directory in terminal with a single command

命令行工具,用于在任何目录下,从终端运行脚本.

github.com

Shared by @itsnauman


## 文章
- [如何: 结合 Apache Spark 折腾IPython Notebook](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)

非常有范儿的教程!

cloudera.com

Shared by @mgrouchy

- [如果用Py编写TCP堆桟将发生什么?](http://jvns.ca/blog/2014/08/12/what-happens-if-you-write-a-tcp-stack-in-python/)


好文,描述如果你亲自实现了 TCP 桟,
就会发现你学会了一堆东西.

jvns.ca

Shared by @myusuf3
 

- [用 Django Shell 协同 IPython Notebook 增强你的提示符](http://opensourcehacker.com/2014/08/13/turbocharge-your-python-prompt-and-django-shell-with-ipython-notebook/)


这个小教程展示了如何在 `IPy[:]notebook` 中包含Django和Python 的shell

opensourcehacker.com

Shared by @myusuf3
 

(`译注:` WoW
![Screen-Shot-2014-08-13-at-14.12.25](http://opensourcehacker.com/wp-content/uploads/2014/08/Screen-Shot-2014-08-13-at-14.12.25.png)
)


- [配置 Sublime Text 3 为全桟Py开发](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)


强文! 精细描述了怎么基于 subl 3 打造自个儿的Py 开发环境.

realpython.com

Shared by @myusuf3

(`译注:`买了 subl 的行者们,必须认真实操的好文章)

- [作弊条儿: 编写Python 2-3 兼容代码](http://python-future.org/compatible_idioms.html)

真,良心好文!
将 Py 2-3 兼容的常见问题和解决整理为了速查表.
如果你正在折腾 Py2-3 兼容的库,必须看.

python-future.org

Shared by @mgrouchy
 

- [用closures 来整体重构 if/else 过滤](http://www.startmake.com/refactoring-monolithic-ifelse-filters-with-closures/)

漂亮的案例,
用一个人尽可知的小例子来说明这一问题.

startmake.com

Shared by @scottallenon
 


## DAMA
(`大妈私人无责任播报`)


# 是也乎

- 140818 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 140818 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
