Title: 蠎周刊 158: Madness
Slug: issue-158
Date: 2015-03-21 21:12
Tags: Weekly,Pycoder,Zh 


![Pycoder's Weekly](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #158): Madness](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=342d2cd3c5&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,

又是一年春花时,
是时候从代码中抬头看看世界在发生什么了哈!

大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


## 新闻



- [Django 再发安全版本](https://www.djangoproject.com/weblog/2015/mar/18/security-releases/)

又一周, Django 发布了一堆安全升级,适当的情况下,
及时升级吧,亲! Django 1.4.20, 1.6.11, 1.7.7 or 1.8c1.

djangoproject.com

Shared by @mgrouchy
 
(`是也乎:`
细思恐极的是, Django 这么热烈的进行安全版本的高速发布,
意味着原先都有多少安全隐患哪)


- [Requests 漏洞批露](http://docs.python-requests.org/en/latest/community/updates/#id1)

是时候升级到 Requests 2.6.0 了!
对 cookie 的处理以往有漏洞哪.
详细在链接内.

python-requests.org

Shared by @mgrouchy
 



## 讨论

- [Python 哪个 "独特" 的特性令你深深的爱上了她?](http://www.reddit.com/r/Python/comments/2zg57n/learning_python_coming_from_many_other_languages/)

reddit.com

Shared by @myusuf3
 

(`是也乎:`
reddit 上列出了很多梗, IPython 提及的次数不少,
对于大妈私人而言按动心程度:

> 缩进
> 内置库
> 动态

)

## 项目

- [cerberus](https://github.com/nicolaiarocci/cerberus)

对 Python 字典数据能进行类型控制的库.

github.com

Shared by @mgrouchy
 

- [PyTricks](https://github.com/brennerm/PyTricks)

这是反复推荐的收集 Py 相关技巧和冷门知识的仓库.

github.com

Shared by @mgrouchy
 

- [AstroBuild](https://github.com/lhartikk/AstroBuild)

基于 planets alignments 进行项目部署

github.com

Shared by @mgrouchy
 

- [governor](https://github.com/compose/governor)

针对 etcd 构建的部署模板,
专门支持 PostgreSQL HA!

github.com

Shared by @mgrouchy
 

- [django-db-mailer](https://github.com/LPgenerator/django-db-mailer)

得趣的项目,
支持你在管理员界面中创建邮件模板,存储在 DB 中,
并支持各种发送功能.

github.com

Shared by @mgrouchy
 

- [holoviews](https://github.com/ioam/holoviews)

自述中曰: holoviews 
乃:"可组合的,数据结构声明,用以方便构建复杂的可视化"

github.com

Shared by @mgrouchy
 

- [equals](https://github.com/toddsifleet/equals)

模糊对等测试支持
Mock.Any 的严格版本.

github.com

Shared by @mgrouchy
 

- [django-GNU-Terry-Pratchett](https://github.com/aaronbassett/django-GNU-Terry-Pratchett)

Sir Terry Pratchett 己作古.
这个 reddit 线索中,
追加 `X-Clacks-Overhead` 标签来纪念 Terry Pratchett 吧.

github.com

Shared by @aaronbassett
 

- [aiomysql](https://github.com/aio-libs/aiomysql)

通过 asyncio 来使用 MySQL 的库.

github.com

Shared by @isinf

(`是也乎:`
支持 Py3, 从请求方进行异步,能提高 MySQL 的能量嘛?)

## 文章


- [发现谁创建了临时文件](http://nedbatchelder.com//blog/201503/finding_temp_file_creators.html)

笔者注意到项目中有很多临时文件,在测试过程中产生,
于是, 利用 `monkeypatch` 追加了一个 `mkdtmp` 事务,
来追踪临时文件的生产.
佷 COOL.

nedbatchelder.com

Shared by @mgrouchy
 

- [PyMongo 子文档的键序](http://emptysqua.re/blog/pymongo-key-order/)

发源自一个好问题:
"为毛查询总是在 shell 中折腾,
而不能在 PyMongo 中!?"

emptysqua.re

Shared by @mgrouchy
 

- [Ordering issues when monkey patching in Python.](http://blog.dscpl.com.au/2015/03/ordering-issues-when-monkey-patching-in.html)

An approach to solve ordering issues when monkey patches are applied by the use of post import hooks.

dscpl.com.au

Shared by @mgrouchy
 

- [在 Django 中使用 gevent-socketio 和 RabbitMQ 实现实时消息](http://www.machinalis.com/blog/rt-notifications-gevent-gis/)

非常完备的教程,
展示了如何在 Django 中组合应用 gevent-socketio 和 RabbitMQ 
令实时通知变得如此简单.

machinalis.com

Shared by @mgrouchy
 

- [俺的 Class Based Views](http://lukeplant.me.uk/blog/posts/my-approach-to-class-based-views/)

Luke Plant 展示如何自制 approach
来在 Django 中折腾 class based views .

lukeplant.me.uk

Shared by @mgrouchy
 

- [映射你的音乐收藏](http://www.christianpeccei.com/musicmap/)

通过 numpy 和其它工具,
对你收藏的音乐进行可视化映射.

christianpeccei.com

Shared by @mgrouchy

(`是也乎:`

![music map small](http://www.christianpeccei.com/musicmap/res/img/musicmapsmall.png)

基于 频谱 分析出音乐情绪的倾向性,
来组织为色谱矩阵.

)

- [Threading 和 Multiprocessing 教程](http://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python)

教程针对初学者非常友好.
涉及对 Python 中并行计算的详尽介绍.


toptal.com

Shared by @mgrouchy
 

- [用 Py 对 Twitter 数据进行分析](http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)

这是系列文章中第一部分,
将用三篇文章,展示如何组合使用 Py 相关工具,
对 Twitter 公开数据,
分析出有趣的结论.

marcobonzanini.com

Shared by @myusuf3

(`是也乎:`
唯一问题是,没有用 IPython notebook 发布,
差评!-)


## DAMA
(`大妈私人无责任播报`)


### 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
最后一周急招5名 gopher/pythonista !


# 是也乎

- 150325 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 150321 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
