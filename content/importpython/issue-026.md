Title: 蠎加载 26
Slug: importpython-26
Date: 2015-04-04 23:32
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 26](http://importpython.com/newsletter/no/26/)

## 该读
~ 文章, Blog, 教程...


- [Python 代码库保护](http://bits.citrusbyte.com/protecting-a-python-codebase/)
    + core python

Python 的语言本质使代码仓库的保护变成异常复杂.
作为一种解释语言,
源代码应该有种保护机制,以便安全执行.
作者在此文中描述如何试图找到到种机制来有效的
保护 Python 代码库.

- [PyCharm 4.0.6 RC 已可用](http://feedproxy.google.com/~r/Pycharm/~3/zqHWETobnx8/)
    + pycharm

这天, PyCharm 4.0.6 RC 发布漏洞修复版.
发布说明中包含详细说明:
主要是针对 Django 的 ORM 检查,
为 ManyToManyField 的 bug 修复.


- [功能聚焦: 用 PyCharm 进行远程开发](http://feedproxy.google.com/~r/Pycharm/~3/ObAFl6CPM8w/)
    + pycharm

周五快乐, 亲们, PyCharm 已经支持了远程开发,
为了展示,使用了个简单的 Flask web 应用开发/调试.

(`是也乎:`
还是够复杂的,,,
至少要配置十几处.
IDE 去死去死!
)

- [高性能 Django 基础设施预览](http://feedproxy.google.com/~r/LincolnLoop/~3/iorgEgsweiQ/)
    + django

咱们用 Salt 进行配置管理有三年了.
近几周,我们在 Salt 之上折腾出一种 可复用/可扩展 的系统,
包含了我们多年来所有来自客户的经验教训.
能在约一刻钟的时间里,
帮助任何人建立/发布出一个完备的 Python 应用网站:
包含 负载均衡,网络加速,高速缓存,数据库,任务队列...

- [介绍 mod_wsgi-express.](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html)
    + apache

和传统的 `mod_wsgi` 最大的区别就是:
`mod_wsgi-express` 能
使用 `pip install` 命令,
直接从 PyPi 安装, 
甚至于可以追加到 'requirements.txt' 文件中.

- [接触 Scout, 用 SQLite 驱动搜索服务](http://charlesleifer.com/blog/meet-scout-a-search-server-powered-by-sqlite/)
    + sqlite,text search

在俺 SQLite 冒险的经历中,
俺被迫使用 SQLite 的全文搜索折腾出一个
RESTful 搜索引擎.
可以认为是穷人的 ElasticSearch
~ 嗯啍,非常非常穷的那种.


- [PSF 研究员识别程序](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/wC01hCZ8GtY/for-shes-jolly-good-psf-fellow.html)
    + PSF

该PSF研究员识别程序的目的是:
管理不断增长的全球 Python 社区以及成员.
当然,想掺合,先通过提名再说了.



- [Django tastypie 入门](http://agiliq.com/blog/2015/03/getting-started-with-django-tastypie/)
    + rest

Django tastypie 
是个辅助完成 RESTful 接口的库.
这是篇很靠谱的入门教程.


- [Django 1.8 发布](https://www.djangoproject.com/weblog/2015/apr/01/release-18-final/)
    + django

经过几个月的折腾, Django 团队高兴的按计划发布了 1.8,
明确是 LTS ~ 长期支持版本!
这意识味着,专注安全和数据保护的这一版本,
将至少进行三年的持续支持.

- [Celery 是如何解放同步任务的?!](http://blog.untrod.com/2015/03/how-celery-chord-synchronization-works.html)
    + celery

Celery 是 Python 界中一种强大的异步任务管理平台.
基本模式是在同步任务代码中,
将任务(以序列化消息的形式)
推送到消息队列中,
( Celery 中的 "broker", 可基于丰富的技术
~ Redis/RabbitMQ,Memcache 或是其它数据库)
而工作进展,则分布式的从队列中提取并执行.

- [Webcast: 用 Python 在 GCP 上构建可扩展的 web 应用](http://www.oreilly.com/pub/e/3388)
    + webcast

在幻灯中,
Google 工程师及 OREILLY 作者
Dan Sanderson 同学,
展示 Google Cloud Platform 作为 Python 开发平台,
如何 构建/部署/管理 一个可扩展的 web app.

- [Webcast: 用 Python 和 Ansible 构建实效网络自动化体系](http://www.oreilly.com/pub/e/3386)
    + webcast

在 Wednesday, April 15, 2015
(Time 10AM PT, San Francisco
1pm - New York | 6pm - London | 10:30pm - Mumbai | Thu, Apr 16th at 1am - Beijing | Thu, Apr 16th at 2am - Tokyo | Thu, Apr 16th at 3am - Sydney 
)
![kirk_byers](http://cdn.oreillystatic.com/images/people/154/kirk_byers.jpg)

将分享如何使用 Py+Ansible 
自动化各种网络任务;
包括配置模板,收集网络设备信息,并执行批量配置更改...


- [学习 redis-py](http://agiliq.com/blog/2015/03/getting-started-with-redis-py/)
    + python,redis

此文, 展示了如何
通过 redis-py 在 py 脚本中使用各种 redis 命令.


- [Jython 2.7 发布第一个候选版本!](http://fwierzbicki.blogspot.com/2015/03/jython-27-release-candidate-1-available.html)
    + jython

虽然是候选版本,
但是,已经非常接近最终正式版本! 




## 项目
~ 包/模块/库/片段...

- [reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
    - 947 Stars, 36 Fork

快速,离线反向地理编码


- [InsideReCaptcha](https://github.com/ReCaptchaReverser/InsideReCaptcha)
    - 187 Stars, 10 Fork

对 ReCaptcha 系统逆向出来的
新 ""captchaless"

- [spectra](https://github.com/jsvine/spectra)
    - 142 Stars, 2 Fork

简易色阶和颜色转换

-[Green](https://github.com/CleanCut/green)
    - 141 Stars, 10 Fork

Green 是种测试框架,
可类比为 nose/trial.


- [palladium](https://github.com/ottogroup/palladium)
    - 86 Stars, 2 Fork

预测分析服务 的架设框架.


- [bulby](https://github.com/sontek/bulby)
    - 75 Stars, 6 Fork

phillips hue lightbulb 的管理库.

- [cron-metrics](https://github.com/manugarri/cron-metrics)
    - 57 Stars, 2 Fork

在 Python 中进行系统监控以及定期任务管理.

- [gist](https://github.com/jdowner/gist)
    - 29 Stars, 1 Fork

Gist 的命令行工具.


- [fontawesome-to-android](https://github.com/deepankarb/fontawesome-to-android)
    - 11 Stars, 0 Fork

能将字体中超赞的图标,
转换为 png 图片,
并安置到 android density buckets
中的 py 脚本.

- [ReactiPy](https://github.com/logandhead/ReactiPy)
    - 11 Stars, 0 Fork

Compile React Components Server Side using Python

- [Email-Autoresponder](https://github.com/SlightlyCyborg/Email-Autoresponder)
    - 8 Stars, 1 Fork

嗯啍,俺撸了个 AI 来自动应答邮箱中重复性的问题.
事实上俺不怎么用邮箱的,
所以,俺时常问朋友们,如果有一个能阅读他们邮件的 AI,
接下来想作什么?!

(`是也乎:`
细思恐极! 这个谁都需要哪!
)

- [rietveld](https://github.com/rietveld-codereview/rietveld) 
    - 6 Stars, 2 Fork

代码复审, 架在 GAE 上的.

(`是也乎:`
Guido 老爹遗作!
)

- [jsonschema-test](https://github.com/kylef/jsonschema-test)
    - 5 Stars, 0 Fork

从给定的 JSON 概念文本,
自动编写测试并运行.



## 工作

- [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
四月急招 N 名有服务端开发经验的 **gopher**!


- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

## DAMA
(`大妈私人无责任播报`)

~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 150404 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150403 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
