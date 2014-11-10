Title: Issue 139: Hero
Slug: issue-139
Date: 2014-11-01 14:15
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Py万物 的周刊

亲,

大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


--

原文: [Pycoder's Weekly (Issue #139): Hero](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=13527cc3dd&e=889f3f6a05)

## 新闻
- [Django Rest 框架 - 已准备好接纳 3.0](https://www.kickstarter.com/projects/tomchristie/django-rest-framework-3/posts/1036094)

从 Kickstarter 启动的 Django Rest 框架又完成小改进 ;-)

kickstarter.com

Shared by @myusuf3
 
- [DSF 重入: 候选人召集中](https://www.djangoproject.com/weblog/2014/oct/26/re-election-dsf-board-call-candidates/)

DSF 董事会重新开放一些职位,已经开始召幕,有兴趣的,及时申报哪.

djangoproject.com

Shared by @mgrouchy
 
- [PyCharm 教育版发布](http://blog.jetbrains.com/pycharm/2014/10/jetbrains-debuts-pycharm-educational-edition/)

PyCharm 又一自由和开源版本发布.
全部的 教育版本 中包含了特殊教育助手程序,
可以帮助教师来辅助学习.


jetbrains.com

Shared by @mgrouchy



## 讨论

- [黑魔法: 高端 OOP](http://www.reddit.com/r/Python/comments/2kknw1/black_magic_advanced_oop/)

reddit.com
Shared by @mgrouchy

(`是也乎:` OOP 你好,
OOP 再见.)



## 项目

- [didyoumean](https://github.com/dutc/didyoumean)


爽利的!
"你咩意思?"
~ 在 AttributeLookup 上的功能加强.
嘦输入一个不正当的对象属性,
didyoumean 就能建议可能的,
以便纠正你当前代码.

github.com

Shared by @mgrouchy

(`是也乎:`
实际使用起来是这样的...

```
>>> import didyoumean
>>> foo.baz
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Foo' object has no attribute 'baz'
    Maybe you meant: .bar
```

执行前,给出进一步建议,而不是只给出错误类型,
有爱!-)

)


- [hangups](https://github.com/tdryer/hangups)

支持 Google Hangouts 的第三方客户端.

github.com

Shared by @mgrouchy

(`是也乎:`

![hangups](https://github.com/tdryer/hangups/raw/master/screenshot.png)

我辈码农爱CLI,
可惜墙外的API!
)

 
- [nightmare](https://github.com/joxeankoret/nightmare)

分布式模糊测试的测试套件与网络管理

github.com

Shared by @mgrouchy
 
- [importd](https://github.com/amitu/importd)

Django based mini framework inspired from Sinatra. Get a simple web up and running quickly with no fuss.

从 Sinatra 得到启发的 微型框架,
基于 Django.
无惊奇的简单 web 启动和运行.

github.com

Shared by @mgrouchy

(`是也乎:`

```
    from importd import d
    d(DEBUG=True)

    @d("/")
    def idx(request):
        return "index.html"

    @d("/post/<int:post_id>/")
    def post(request, post_id):
        return "post.html", {"post_id": post_id}

    if __name__ == "__main__":
        d.main()
```

你还能再象点 bottle 嘛?!
)


- [mps-youtube](https://github.com/np1/mps-youtube)

命令行的 YouTube 播放和下载器.

github.com

Shared by @mgrouchy


(`是也乎:`

![mps](https://camo.githubusercontent.com/c07e843aa8530895ce9de2405253d5f7be8b8982/687474703a2f2f6e70312e6769746875622e696f2f6d707379742d696d61676573322f646f776e6c6f61642e706e67)

)

- [cider](https://github.com/msanders/cider)


很赞的对 Homebrew + cask 的简单包装,
支持你将 OSX 的配置,
并复制到另外一台新机器上 .

github.com

Shared by @mgrouchy
 
- [python-json-patch](https://github.com/stefankoegl/python-json-patch)

根据 RFC 6902 对 JSON 进行了补全的库.

github.com

Shared by @mgrouchy
 
- [template-python](https://github.com/jacebrowning/template-python)

Python 项目的模板,
为你将一个软件工程应该考虑的所有方面,都进行了预设.
包含 工具/virtualenvs/静态分析/整理/上传发布...

github.com

Shared by @mgrouchy

(`是也乎:`
这本来是一个和编辑器之争要更加绵长的议题,
只是 Pythoneer 一般都在服务端折腾,所以,没有多少关注?
也可能 7 年前就已经解决了!
[寻找更好的模板系统记 - 魏中华的日志 - 网易博客](http://blog.163.com/cqit_jsj/blog/static/651272200781104735593/)
当然 template-python 是 scaffold~工程脚手架
不是 web 应用模板,
但是, 大妈就是联想起来了呗...
)

- [coastermelt](https://github.com/scanlime/coastermelt)

coastermelt 支持开源固件, 创造性的利用了 BD-R 驱动器,
详细的有宣传片儿可看 ;-)

github.com

Shared by @myusuf3
 
- [Lost-Photos-Found](https://github.com/caio1982/Lost-Photos-Found)

非常实用的, 支持你对深藏在 Gmail 历史邮件中的图片进行挖掘.
使用 Gmail 有年头的你 值得拥有.

github.com

Shared by @caio1982


- [rencode](https://github.com/aresch/rencode)

bencode 类似的,更快的对象序列化模块.

github.com

Shared by @andrew_resch


- [pyrsistent](https://github.com/tobgu/pyrsistent/)

An implementation of a immutable data structures in Python. The collection types currently implemented are PVector (list), PMap (dict), PSet (set), PBag (Counter), PList (singly linked list) and PDeque (deque).

为 Python 实现的一系列不可变数据类型,
当前包含的有:
PVector (列表), PMap (字典), PSet (集合), PBag (计数), PList (单链表) and PDeque (双端队列)

github.com

Shared by @mgrouchy

(`是也乎:`
这是 dropbox 静态化 Py 思路方向上的小伙伴哪 ;-)

- [knockknock](https://github.com/synack/knockknock)


KnockKnock 是命令行脚本,
专门用来探查在 OS X 开机自启动的最长时间运行的进程,
当然的,用 Python ;-)

github.com

Shared by @myusuf3


## 文章

- [简单图形用 IPython 和 Pandas](http://pbpython.com/simple-graphing-pandas.html)

很赞的教程,
从头儿折腾 iPython, Pandas and Matplotlib.
用 pandas 处理数据,
用 Matplotlib 在 IPython 中图形化.

pbpython.com

Shared by @mgrouchy
 
- [Bootstrapped virtualenvs](http://codeinthehole.com/writing/bootstrapped-virtualenvs/)


简单技巧,就可以作到令你的环境可引导.
通过: `postmkvirtualenv` 即可.

codeinthehole.com

Shared by @mgrouchy
 
- [在 Django 中将文件上传到 Amazon S3](http://tech.marksblogg.com/file-uploads-amazon-s3-django.html)

在 Django 中上传文件到 S3 一直很痛苦.
现在有教程彻底解决这事儿了.

marksblogg.com

Shared by @mgrouchy
 
(`是也乎:`
又一个对墙后小伙伴不存在的痛苦.)

- [用 SQLCipher 对 SQLite 数据库进行加密](http://charlesleifer.com/blog/encrypted-sqlite-databases-with-python-and-sqlcipher/)

通过教程学习如何加密你的 SQLite 数据库,
并通过 Python 代码进行交互.

charlesleifer.com

Shared by @mgrouchy
 
 
- [终极前端 Django 开发配置](http://www.revsys.com/blog/2014/oct/21/ultimate-front-end-development-setup/)

超级详细的如何在 Django 中配置
 Gulp 和 bower,
 来支持 minifiying 和 post-processing 文件以及 LiveReload

revsys.com

Shared by @mgrouchy
 
- [Django vs Flask vs Pyramid: 选择 Python web 框架](http://www.airpair.com/python/posts/django-flask-pyramid)


此文给出了又一种比较,
以帮助你在多种 框架间进行决策.

airpair.com

Shared by @elldudley
 
 
- [在 Ubuntu 中折腾 Flask - 设置和部署](https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/)

就从这儿开始!

realpython.com

Shared by @rochacbruno
 
 
- [Fluent interface in python](http://kracekumar.com/post/100897281440/fluent-interface-in-python)

kracekumar.com

Shared by @mgrouchy


## DAMA
(`大妈私人无责任播报`)


# 是也乎

- 141103 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 141101 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
