Title: Issue 117: 3 > 2
Slug: issue-117
Date: 2014-06-02 17:22
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Py万物 的周刊

亲们,

目测,上周有部分邮件被Spam 了,俺们猜可能是标题的原因,
请检查你的过滤器,如果修订为非垃圾的,对我们是个非常大的帮助.

向俺们分享[文章](http://pycoders.com/submissions/)
呗,如果上了周刊,
你滴大名会被高亮显示出来啊!

另,用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--

原文: [Pycoder's Weekly (Issue #117): 3 > 2](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=1be31a84b1&e=889f3f6a05)


## 新闻

[Continuum Analytics 发布 Anaconda 2.0](http://continuum.io/blog/anaconda-2-released)

此版本包含了 Python 3 的直接安装,
并从 PySide 迁移到了 PyQt.

continuum.io

Shared by @myusuf3

## 讨论
[为毛遍历字串比列表慢?](http://stackoverflow.com/questions/23861468/why-is-it-slower-to-iterate-over-a-small-string-than-a-small-list/23864108#23864108)

stackoverflow.com

Shared by @myusuf3


## 项目

- [django-reportmail](https://github.com/hirokiky/django-reportmail)


我们总是要在夜间进行各种管理命令,
这一应用,能在完成后,将结果告诉你...

github.com

Shared by @myusuf3
 

- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation)

Flask 应用的基础模样,
充分利用之,你可以方便的折腾出各种来.

github.com

Shared by @mgrouchy
 

- [pyminifier](https://github.com/liftoff/pyminifier)

压缩/混淆/精简 你的Python 代码

github.com

Shared by @mgrouchy
 
(`译注:`竦么屌, 能生成这种代码:

    #!/usr/bin/env python
    ﵛ=ImportError
    ࡅ=print
    㮀=False
    搓=object
    try:
     import demiurgic
    except ﵛ:
    ...

)

- [sql4pandas](https://github.com/keeganmccallum/sql4pandas)

超COOL,
支持对 pandas 的 data frames 对象执行 SQL 查询.

github.com

Shared by @mgrouchy

(`译注:` 略屌,不过,现在要屌丝到什么地步,非要对 NoSQL 数据集进行 SQL 哪...) 

- [easyplot](https://github.com/HamsterHuey/easyplot)

为 Matplotlib 生成简便/可复用的包装.

github.com

Shared by @mgrouchy
 

- [openduty](https://github.com/ustream/openduty)


开源的类似 PagerDuty 的付费产品警告提示/升级工具

github.com

Shared by @mgrouchy
 

- [grako](https://bitbucket.org/apalala/grako/src)


解析器生成器!
Grako 接受 EBNF 格式语法,
输出Python 用的 PEG 报告.

bitbucket.org

Shared by @mgrouchy

(`译注:` 从此创造自个儿的语言,也变成了 Py 脚本写作...
ps: 作者Juancarlo Añez的头像是:
![avatar](https://secure.gravatar.com/avatar/51dcf0a6e20c2734423118e7eee9e45d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F9d3d19e361c2%2Fimg%2Fdefault_avatar%2F96%2Fuser_blue.png&s=96)
) 

- [onionshare](https://github.com/micahflee/onionshare)

安全/匿名的共享任意大小的文件...

github.com

Shared by @myusuf3
 

(`译注:` 其实了,嘦在中国内网中,你共享的出来,别人也下载不能哪,,,)

- [everyonepanic](https://github.com/doublemap/everyonepanic)

你的网站一担挫了,就能快速告诉你的一种应用.

github.com

Shared by @myusuf3
 

- [pdfminer](https://github.com/euske/pdfminer)

kind of project I love finding in open source. we all need it, but no one wants to write it. Unlike other PDF-related tools, it focuses entirely on getting and analyzing text data, also provides exact location of text on page.

这是那种俺最爱的开源项目:

- 人人都需要
- 但是没人愿意写

不像其它 pdf 相关的项目, pdfminer 专注获取和分析文本数据,
还提供了页面上文本确切位置的信息.

github.com

Shared by @myusuf3

(`译注:` 专门为 CJK 语言进行了支持...良心哪,,)

- [ratticweb](https://github.com/tildaslash/RatticWeb)

作为rattic 口令管理方案,
可让你轻松管理用户和口令.

github.com

Shared by @myusuf3

## 文章

- [在Python 中压倒一切的方法](http://lgiordani.github.io/blog/2014/05/19/method-overriding-in-python/)

漂亮的解决在Python 中继承的重载问题.

github.io

Shared by @tw_lgiordani
 

- [如何令Python 3 向前进](http://nothingbutsnark.svbtle.com/my-view-on-the-current-state-of-python-3)

Python 核心开发者 Brett Cannon
给出了自个儿的想法,
如果你纠结于移植 Python 应用/库的依赖问题时,
一定要认真理解...

svbtle.com

Shared by @mgrouchy
 

- [Python 2 和 3 的核心差异](http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/key_differences_between_python_2_and_3.ipynb?create=1)


用 iPython notebook 展示了 Python 2/3 间的核心差异,
如果你正在寻找 从Python 2 迁移到3 的素材,这是极好的.

ipython.org

Shared by @mgrouchy
 

- [Gevent 应该怎么整?](http://blog.hownowstephen.com/post/50743415449/gevent-tutorial)


Gevent 中最好的教材!
提供了大量的背景资料,
通过创建一个简单的 网络爬虫 展示了 Gevent 的利弊,究竟如何工作的...


hownowstephen.com

Shared by @mgrouchy
 

- [Python 3 在杀灭 Python 2](https://medium.com/@deliciousrobots/5d2ad703365d/)

非常自我的断言,
有关Python 3 应该消亡,Python 2 系列应该继续的分析,
有一些论据,但是,元芳? 你怎么看?

medium.com

Shared by @myusuf3
 

- [Python 3 能复兴 Python](https://medium.com/p/2a7af4788b10)


分析 Python 3 中有什么令人兴奋的特性,
以及开发商可能高兴的要点...

medium.com

Shared by @mgrouchy

(`译注:` 有关 Py2/3 之争,目测将持续到 2020 年了,其实,有
`BDFL` 在,其它的折腾个毛线哪,,,享受Python 世界的丰富就对了) 


- [为毛应该给 PonyORM 一次机会](http://jakeaustwick.me/why-you-should-give-ponyorm-a-chance/)

一篇真诚的软文.

jakeaustwick.me

Shared by @mgrouchy
 

- [Python中的模拟](http://www.drdobbs.com/testing/using-mocks-in-python/240168251)

广泛的介绍了 Python 中各种 mock 库,
如果你在决策使用哪个系列的,此文值得一观...

drdobbs.com

Shared by @myusuf3

## DAMA
(`大妈私人无责任播报`)






# 是也乎

- 140602 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 140602 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

 
