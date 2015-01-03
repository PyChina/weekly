Title: Issue 99.5: Fugazi
Date: 2014-01-25 
Tags: Weekly,Pycoder,Zh 
Slug: issue-99-5

## Hi Pythonistas!


俺们撒谎鸟, 第100期,在下周才真正发布,亲,再等等.
当然,末期也很精彩.

一如即往,任何疑问/意见/抱怨/建议,
让我们知道就好;
 
想跟上所有 蠎界 新闻?
 [@pycoders](http://twitter.com/pycoders).

另,用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #99.5): Fugazi](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=6ad49cd999&e=889f3f6a05)

## 新闻
- [Cython 0.20 释放](https://github.com/cython/cython/blob/master/CHANGES.rst#020-2014-01-18) (github.com)

最新的 Python 到 C 编译工具 Cython 已经释放.
包含大量修正以及新特性.
 

- [PyCon 2014 演讲日程已释放](https://us.pycon.org/2014/schedule/talks/) (pycon.org)

查阅之. 
如果还没有决定今年是否参加,是时候改变想法了. 

(`译注:`#细思恐极 国际PyCon 基本是对上一年的总结,不是对当年的总结了...!-)

- [PyCon 2014 托儿所 - 将开放注册!](http://pycon.blogspot.ca/2014/01/pycon-2014-childcare-register-soon.html) (blogspot.ca)

If you are heading to PyCon 2014 in Montreal and you need Childcare during the main conference days it can be had for 50$ per child per day. This is the first time ever that PyCon has had available childcare and space is limited.
 
如果听说有过,今年在 Montreal的 PyCon2014 有提供 50$/日
的托儿服务,那就要及时下手了,
毕竟这是首次提供类似服务的大会, 而且的确空间有限!

(`译注:`#细思恐极 目测这是同为奶爸的 Guido 强烈要求下,大堆奶爸程序猿共同的争取 !-)


- [Django 1.7 alpha 1 释放](https://www.djangoproject.com/weblog/2014/jan/22/django-17-alpha-1-released/) (djangoproject.com)

首个 1.7 的 alpha 版本释放.
请查阅
[开发版发布说明](https://docs.djangoproject.com/en/dev/releases/1.7/)

了解这一个版本将带来什么新特性.


- [PyData London 2014](http://pydata.org/ldn2014) (pydata.org)


今年 PyData 将于2月21~23在伦敦举行,
已经开始征集讲师,如果你有兴趣,及时申报.

## 讨论

`无`


## 项目

- [newspaper](https://github.com/codelucas/newspaper) (github.com)
`<3`

综合应用各种高端技术,
轻快的从外部资源中抽取主要内容.

(`译注:`#细思恐极 目测华人小伙伴作品,当然海外的,而且工作经历异常漂亮 !-)


- [django-dynamic-dns](https://github.com/damianmoore/django-dynamic-dns) (github.com)
`<3`

有用!
机器配置了动态IP 时,
能让服务自动配置 DNS 无缝继续访问应用.
 

- [restcommander](https://github.com/eBay/restcommander) (github.com)

来自 Ebay 的高速并发同步 HTTP 客户端,
 用以监控大量的 web 服务.

(`译注:` 目测就是高大上的 [REST Superman](http://www.restsuperman.com/) !-)


- [faker](https://github.com/joke2k/faker) (github.com)
`<3`

介系个伟大的工程!
Faker能根据你的需要快速生成各种形式的 伪数据用来测试开发.
 

- [frosted](https://github.com/timothycrosley/frosted) (github.com)
`<3`

pyflakes 的分支,
能对你的 Python 源代码进行静态分析给出汇报.
 

- [piprot](https://github.com/sesh/piprot) (github.com)
`<3`


工程的包依赖关系已经烂了嘛?
用piprot来分析你的 requirements 文本,
来确认是否过期等等问题吧.

- [PyLaTeX](https://github.com/JelteF/PyLaTeX) (github.com)
`<3`


(`译注:` 无需多言 !-)


- [shellnoob](https://github.com/reyammer/shellnoob) (github.com) 
`<3`

(`译注:` 呵呵 shell 写手的福音 !-)


## 文章

- [别在 Heroku 上用 Gunicorn 容纳 Django 网站](http://blog.etianen.com/blog/2014/01/19/gunicorn-heroku-django/) (etianen.com)

作者给出了一些实用建议,
有关别用
[Gunicorn](http://gunicorn.org/) 
在Heroku 上折腾你的应用,
而是用
[waitress](https://pylons.readthedocs.org/projects/waitress/en/latest/) 
替代.

(`译注:` waitress 竟然是 pylons 的子项目
也已经有一定人望,Bootle 都内置了支持参考: [What WSGI servers you use?: Python](http://www.reddit.com/r/Python/comments/16tm4e/what_wsgi_servers_you_use/)
也是从 Zope3 的灰烬自救出来的好物哪,,,
!-)



- [如何在Python 中创建不可变的类](http://www.blog.pythonlibrary.org/2014/01/17/how-to-create-immutable-classes-in-python/) (pythonlibrary.org)

类在 Python 中一向是可变的,
但是,这篇文章分享了怎么创建无法变更的!
 

- [市场模拟在 iPython Notebook](http://nbviewer.ipython.org/url/norvig.com/ipython/Economics.ipynb) (ipython.org)

IP[y]:notebook 最赞的应用方式!
[Peter Norvig](http://norvig.com)
创建了一个极COOL 的模拟的经济市场.

(`译注:` #细思恐极 造谁是 Norvig?! 现为Google公司研究总监!!! 
这种人物都在玩 IP[y]:notebook 了你还在等什么?!
!-)



- [Python 和 Flask 强大的离谱!](http://jeffknupp.com/blog/2014/01/18/python-and-flask-are-ridiculously-powerful/) (jeffknupp.com)
 
Jeff 是位著名的 Blogger, 长年宣传Python 以及 Flask.
这篇文章分享了如何用 Flask 快速创建一个在线支持网站,
并顺便推荐了自个儿的书.

- [Python 101: 怎么写清除脚本](http://freepythontips.wordpress.com/2014/01/23/python-101-writing-a-cleanup-script/) (wordpress.com)


Python 一向是SA 的好帮手,
此文给出了一系列小脚本,
可以灵活的根据各种诸如 文件大小等特征清除文件.

(`译注:` 当然,文章在墙外,想看就能看的
!-)


- [牛仔优化: 均分函式](http://pythonsweetness.tumblr.com/post/74073984682/cowboy-optimization-bisecting-a-function) (tumblr.com)

 

# 是也乎

- 140125 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 140125 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.
 
