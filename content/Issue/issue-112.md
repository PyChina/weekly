Title: Issue 112: SpaceX
Slug: issue-112
Date: 2014-04-29 11:14
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Python 万物的周刊

亲们,

俺们筹备好另外一件纪念TEE 鸟,想整一件的关注我们的
[twitter](http://www.twitter.com/pycoders)
下周可能设计就出来了.


向们分享[文章](http://pycoders.com/submissions/)
呗,如果上了周刊,
你滴大名会被高亮显示出来啊!

另,用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--

原文: [Pycoder's Weekly (Issue #112): SpaceX](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=214eac5719&e=889f3f6a05)


## 新闻

- [Pylint 1.2 发布!](http://www.logilab.org/blogentry/240019)

新版本给出了新的检查点,并修复了bug,也支持了 Py3.4!
是时候开始 linting 了.

logilab.org

Shared by @mgrouchy
 

- [猕猴桃 PyCon 2014 通告!](http://kiwi.pycon.org/blog/2014/04/07/kiwi-pycon-2014-announced/)

明确本次大会在 新西兰于 9/13~14 举行.

pycon.org

Shared by @myusuf3
 

- [Django 安全版本发布](https://www.djangoproject.com/weblog/2014/apr/21/security/)

Django 团队在讨论 1.4.11/1.5.6/1.6.3/1.7 beta2 多个版的安全版.
及时更新吧.

djangoproject.com

Shared by @mgrouchy

## 讨论

[如何在本地组织百万行以上级别的工程?](http://www.reddit.com/r/Python/comments/23wbkl/how_is_your_1_million_loc_project_structured/)

reddit.com

Shared by @mgrouchy

(`译注:` 只看标题还以为是标题党,结果讨论中是真的有人在折腾 1M+ 级别的Python 工程!
当然的对策和豆瓣类似,分库吧...`NoZuoNoDieWhyUtry` 
当然,这也说明 Python 的能力早已没有什么体量的限制了.
)

## 项目

- [IPython Notebook Themes](https://github.com/nsonnad/base16-ipython-notebook)

超赞的对 `IPy[:]` Notebooks 进行样式定制!

github.com

Shared by @myusuf3
 
(`译注:`最令人感动的是 [base16-codemirror](https://github.com/idleberg/base16-codemirror) 真的流行开了..)

- [drf-extensions](https://github.com/chibisov/drf-extensions)

Django REST 框架的自制扩展合集.
包含缓存/混合类型/新字段/序列化等等.

github.com

Shared by @MyNameIss
 

- [locust](https://github.com/locustio/locust)

Python 实现的分布式负载测试工具!
支持你用Python 快速定义测试场景,然后从一个或多个分布式主机上启动.

github.com

Shared by @mgrouchy
 

- [goless](https://github.com/rgalanakis/goless)

很得趣的项目,
基于 Stackless 或是 gevent 创建类似 Go 式方言脚本.


github.com

Shared by @mgrouchy
 

- [ipython-desktop](https://github.com/mangecoeur/ipython-desktop)

`IPy[:]` notebook 的概念级桌面界面.

github.com

Shared by @mgrouchy

![Screenshot1.png](https://raw.githubusercontent.com/mangecoeur/ipython-desktop/master/assets/Screenshot1.png)

(`译注:`当然的是 MAC 的桌面绑定.) 

- [pylearn2](https://github.com/lisa-lab/pylearn2)

一个目标旨在轻松折腾机械学习的库.

github.com

Shared by @mgrouchy
 

- [geofront](https://github.com/spoqa/geofront)

SSH 密匙管理服务.允许你管理和分发在多个机器上的密匙.

github.com

Shared by @mgrouchy
 

- [terminal-webcam](https://github.com/mustafaakin/terminal-webcam)

行不行哪! 这工具能在终端展示 webcam 的图像!

github.com

Shared by @myusuf3
 
(`译注:` 果断基于 python-opencv 的,大妈在 MakerFaire2014ShenZhen 就见过类似的:
[Ascii Image from Project Polascii - Supported by SZDIY](http://polascii.szdiy.org/gallery/szmakerfaire2014/20140406121243.html)
)

- [SoCo](https://github.com/SoCo/SoCo)

很屌的项目,支持用 Python 来控制你的 Sonos 扬声器


github.com

Shared by @mgrouchy
 

- [click](http://click.pocoo.org/)

全新的命令行界面库,
同大家熟悉的 docopt.
虽然还未正式发布,但是文档已经足够丰富了.

pocoo.org

Shared by @myusuf3

(`译注:` pocoo出品,必属上品,大爱修饰器;-)

## 文章

- [用 Ansible 进行全自动的OS X 调配](http://il.luminat.us/blog/2014/04/19/how-i-fully-automated-os-x-with-ansible/)

点赞24.

luminat.us

Shared by @myusuf3
 

- [何时用 eval 不傻?](http://tech.onefinestay.com/post/82297708112/when-using-eval-isnt-evil-or-stupid)

仅指出一点 eval 的小技巧,
以测试方法调用能产生对用户可用的错误报告,
要比通用的 TypeError 反馈要可行的多.

onefinestay.com

Shared by @szotten
 

- [使用 Flask Cache](http://brunorocha.org/python/flask/using-flask-cache.html)

Flask 没有内置的缓存功能,
但是,此文介绍了通过 flash-cache 插件来提供缓存功能,
值得折腾.

brunorocha.org

Shared by @mgrouchy

 

- [Raspberry Pi 作为私有 Git Server](http://monkeyhacks.com/raspberry-pi-as-private-git-server)


简短而中肯的教程,描述如何设置 Raspberry PI 成为私有git 服务.

monkeyhacks.com

Shared by @mgrouchy
 

- [实例Flask - Part 1](http://www.realpython.com/blog/python/flask-by-example-part-1-project-setup/#.U1e8JWRdVHg)

简单的教程,向你展示如何创建 Flash 应用.

realpython.com

Shared by @myusuf3
 

- [用Twitter 数据来分析 NHL 季后赛的](http://www.danielforsyth.me/analyzing-a-nhl-playoff-game-with-twitter/)

很赞的大数据实案,
以 Twitter 数据针对 NHL 的季后赛,
基于 Python/Panda/iPython notebook 以及 vincent完成可视化.

danielforsyth.me

Shared by @mgrouchy
 
(`译注:` 哪儿哪儿都开始大规模使用 IPython Notebook 了哪...)

- [理解 Gunicorn 的并发模式](http://words.volant.is/articles/understanding-gunicorns-async-worker-concurrency-model/)

触及 gunicorn 并发模式的细节,难得的好文.

volant.is

Shared by @myusuf3


## DAMA
(`大妈私人发现的值得分享的消息`)


# 是也乎

- 140429 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 140429 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

 
