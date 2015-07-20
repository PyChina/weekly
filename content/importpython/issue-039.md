Title: 蠎加载 39
Slug: importpython-39
Date: 2015-07-17 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 39](http://importpython.com/newsletter/no/39/)



## 该读
~ 文章, Blog, 教程...


- [Orielly 免费书 - 开始用 Python 进行函式编程](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/dPL7jUJwgss/get-started-with-functional-programming-in-python.html)
    + book review

本书为读者展示了如何用函式编程来令项目更加易于创建和维护.
嗯哼,免费的!

(`是也乎:`

原版可爱的 Python 作者!

国内下载: [eBOOK-2015-07-19.zip](http://zoomq.qiniudn.com/ZQCollection/pdf/eBOOK-2015-07-19.zip)
)

- [Python 3.5 承诺新语法特性](http://www.infoq.com/news/2015/07/Python-35)
    - core python

3.5 核心开发者 Benjamin Peterse 曰了,
新语法特性以及新内建模块,等等,将显著提高库的效能.

(`是也乎:`

这是向 go 看齐的节奏哪....

)

- [在树莓派上用 Wing IDE 来调试 Python 代码](http://wingware.blogspot.com/2015/07/debugging-python-code-on-raspberry-pi.html)


Raspberry Pi 
并不是真的能跑  Wing IDE,
但是,通过远程工程的配置,可以连接到远程代码进行调试.

(`是也乎:`

坊间传说,世界上最远的调试是从地球调试月球轨道上的 LISP 应用...

)


- [EuroPython 2015: 指南 (移动版) 发布](http://blog.europython.eu/post/124165903022)
    - conference

大会新功能,
包含会场地图/完整的时间表/可创建个人日程/订阅 Twitter 标签,
可登录联络其它参会人员,
常用信息(联系人,CoC,FAQ,城市信息....)
而且能脱机使用(原生 app.)


(`是也乎:`

自从 Google I/O 2012 提供了大会专用 App. 后,
这已经成为了技术大会的标准配置了.

)


- [搜索 Approximate 最近邻居](http://developers.lyst.com/2015/07/10/ann/)
    - machine learning    

最近邻居算法有很多,
最常见的是先分离空间为多个"桶",
然后在内进一步评估.
这令计算速度是以精确度为代价的...

细节链接中.

- [芹菜和 Redis 使用入门](http://agiliq.com/blog/2015/07/getting-started-with-celery-and-redis/)
    - redis, celery

文章论及何时应该用芹菜?为什么要用?...

芹菜是 Python 世界著名的分布式计算框架,
一个原先缓慢的脚本,进入 芹菜 后能获得速度量级的提升!
芹菜又天然支持多种后端, Redis 是其中最简洁的一种.
如何配置 Redis 在不同的机器中, 通过 芹菜良好的协同起来?

细节链接中.


- [唯一键函式修饰符 (Python)](http://code.activestate.com/recipes/579079-decorator-for-defining-functions-with-keyword-only/)
    - core python

Python2.x 实施 python3's keyword-only arguments 
(即, 必须指定关键字,不受位置影响 - 参考 PEP 3102).

- [节目 15 - Damien George 曰 MicroPython](http://podcastinit.podbean.com/e/episode-15-damien-george-talks-to-us-about-micropython/)
    - podcast

不依赖 OS 的微型 Python 控制器.

- [节目 #16 Python 在 Netflix - [播客:跟俺说 Python]](http://www.talkpythontome.com/episodes/show/16/python-at-netflix)


- [Elliott 开发 Blog: Azure AD 在 Django 社会化验证](http://www.elliottmiller.me/2015/06/azure-ad-in-django-with-python-social.html)
    - django

Azure Active Directory (AAD) 
已进入 Python-Social-Auth 库.
将其结合到 Django 应用中, 出乎意料的轻松!
这篇文章比库文档更加直白的说明了整个儿过程.


- [Python 中的科学计算](http://feedproxy.google.com/~r/TheEndeavour/~3/ioZwJmNKjaM/)

科学计算在 Python 中迅速成熟中!

上周在 SciPy 2015 大会,比去年增长了两倍!
笔者连续参加了三年, 
Jake VanderPlas 的演讲, 深刻的揭示了,
科学计算能力桟在 Python 世界的发展.


- [用 zxcvbn 进行 Django 的口令强度检验 | scot hacker's foobar blog](http://birdhouse.org/blog/2015/06/16/sane-password-strength-validation-for-django-with-zxcvbn/)
    - django

Dropbox 刚刚发布了非常智能的口令强度检验库: zxcvbn
(check the bottom left row of your keyboard)

在后台运行的 zxcvbn 消除了字典的依赖,
而是引入了全部的概念:
保持后端检验的同时,确保前端的及时响应.

作者将具包装为了 Django 工具包,
同时满足以上两种期待.

(当然,必须的,有其它 zxcvbn 实现,只是还没看到过.)

- [Django 教程| i18N 和 L10N ](http://www.marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones)
    + django

讨论国际化和本地化以及时区,
展示如何为我们的网站创建针对每个人的网址/语言界面.
以及如何根据时区显示本地时间的模板.


### 工作

-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)
急招 N 名有服务端开发经验的 **gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...

- [Animator5D](https://github.com/bencbartlett/Animator5D)
    - 55 Stars, 4 Fork

非常易用的 5维 gif 动画生成器
(X,Y,Z,时间,颜色).

依赖 ImageMagick 和框架的结合.


- [rpforest](https://github.com/lyst/rpforest)
    - 27 Stars, 6 Fork

生成随机森林投影

![rpforest](https://github.com/lyst/rpforest/raw/master/rpforest.jpg)

- [Salary-API](https://github.com/narenaryan/Salary-API)
    - 11 Stars, 4 Fork

芝加哥市职工工资API,
用 Python 基于 Flask 仅一小时内完成.

- [technetium](https://github.com/DrkSephy/technetium)
    - 11 Stars, 2 Fork

Bitbucket Centralized 的提案追踪和报告生成器

(`是也乎:`

K.K 发明的 `科技元素` 终于被抢先用上了
)

- [sempervirens](https://github.com/njsmith/sempervirens)
    - 10 Stars, 4 Fork

为开放数据科学, 收集实验性质数据的工具

- [screenshot.py](https://github.com/jabbalaci/screenshot.py)
    - 10 Stars, 0 Fork

抓网页为截屏


- [pyprice](https://github.com/Parkayun/pyprice)
    - 8 Stars, 0 Fork

股票价格指数的包装


- [data-analytics-course](https://github.com/captainsafia/data-analytics-course)
    - 6 Stars, 1 Fork

用 Python 桟来进行数据分析的仓库

- [csv2tex](https://github.com/mithodin/csv2tex)
    - 6 Stars, 1 Fork

将 csv 数据变成 LaTeX 表格, WoW!


- [sympy-pycon](https://github.com/aktech/sympy-pycon)
    - 5 Stars, 3 Fork

PyCon 印度 - SymPy 幻灯

- [pireal](https://github.com/centaurialpha/pireal)
    - 5 Stars, 0 Fork

关系代数的教育工具

(`是也乎:`

![pireal logo](https://github.com/centaurialpha/pireal/raw/master/src/images/pireal_banner.png)
)


## DAMA 无责任推荐

# 是也乎

- 150720 [Zoom.Quiet](http://zoomquiet.io) 完成快译
- 150717 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
