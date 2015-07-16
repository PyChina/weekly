Title: 蠎加载 37
Slug: importpython-37
Date: 2015-06-26 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 37](http://importpython.com/newsletter/no/37/)


## 该读
~ 文章, Blog, 教程...

- [Twitter 从 2011 起就用 PEX 方式将整个儿 Python virtualenv 打到一个 zip 中](https://pex.readthedocs.org/en/latest/index.html)

pex 包括 Python 的包管理和分发,
原先是 Twitter 内部公用服务,已经开源为独立项目.

核心组件是和 .pex(Python EXecutable) 相关的 PEX 工具.
提供了类似 virtualenv 的通用虚拟环境.

Twitter 已规模使用了4年!

(`是也乎:`

电影: [WTF is PEX? - YouTube](https://www.youtube.com/watch?v=NmpnGhRwsu0)

嗯哼,就是利用了 Python 内置的 zip 无缝解压能力,
将一切随时用 PEX 折腾到可命名/可执行/可升级/可部署的 .zip 文档中.

)

- [LOST 演员基本分析 - IPython Notebook](http://nbviewer.ipython.org/github/pmbaumgartner/LOST/blob/master/WE%20HAVE%20TO%20GO%20BACK.ipynb)
    - ipynb

不禁在想 LOST 演员们的事业发展,现在如何?!
于是基于 IMDB 数据分析了一下下


- [mod_wsgi-express 集成为 Django 管理命令](http://blog.dscpl.com.au/2015/04/integrating-modwsgi-express-as-django.html)
	+ mod_wsgi

通过这种集成命令,
可以直接查询 Django 的模块配置.

- [virtualenvwrapper.django 0.4.1](http://feeds.doughellmann.com/~r/DougHellmann/~3/NTInBNBM7so/virtualenvwrapper-django-0-4-1.html)
	+ django

virtualenvwrapper.django 
作为模板插件,配合 virtualenvwrapper
可以高速完成 virtualenv 的环境部署


- [Djangocon: 对 web 应用进行负载测试 - Yulia Zozulya](http://reinout.vanrees.org/weblog/2015/06/02/07-load-test.html)
    + testing

其实用 Python 来构建负载测试也很容易的.


- [IPython 技巧](http://blog.endpoint.com/2015/06/ipython-tips-and-tricks.html)
    + ipython

IPython 是种魔性交互界面.
强大到无法想象...



- [PyCharm 4.5.3 RC 发布](http://feedproxy.google.com/~r/Pycharm/~3/SaURFg9dISo/)
    + pycharm

今天 PyCharm 4.5.3RC发布了漏洞修复更新. 
发行说明中列出了从以前的PyCharm4.5.2更新所有修补程序. 

其中最引人注目的是:对一些Django支持的修复,主要涉及
manage.py 的持续读写.


- [Django线路图](https://www.djangoproject.com/weblog/2015/jun/25/roadmap/)
    + django

通过对3000Django开发者的调查和在Django开发者邮件列表讨论,Django团队公布了特性计划列表(根据需要变化). 


- [Echo, 一个集成路由的微型框架,1.0版本已发布](http://labstack.com/blog/echo-production-ready/)
    + webframwork

Echo 高兴地宣布 V1.0.0 发布. 自从Echo诞生以来,我们已经经历了多次迭代,接受来自世界各地的人们的反馈,解决了Issue并接收pull-request超过100个. 

(`是也乎:`

又一个框架轮子
)

- [扩展Django - 80亿页面浏览量| Disqus:官方博客](http://blog.disqus.com/post/62187806135/scaling-django-to-8-billion-page-views)
    + django

每月请求已近 80亿, 45K/秒.
我们坚持使用 Django.
当然也学到了更多技巧.


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

- [telebot](https://github.com/yukuku/telebot)
    - 95 Stars, 16 Fork

Telegram机器人,可使用GoogleAppEngine快速安装


- [2015-06-22-s2i2-git](https://github.com/chendaniely/2015-06-22-s2i2-git)
    - 35 Stars, 8 Fork

s2i2 的 git 教学项目.
Daniel and Tommy 向学生展示 git 的各种奇迹.

如此酷炫,以至 github 应该付费给我们.


- [shadertoy-render](https://github.com/alexjc/shadertoy-render)
    - 27 Stars, 0 Fork

用 ShaderToy 直接渲染成视频

- [engarde](https://github.com/TomAugspurger/engarde)
    - 22 Stars, 1 Fork

防守数据分析库.


- [pcbre](https://github.com/davidcarne/pcbre)
    - 21 Stars, 3 Fork

集成印刷电路板逆向工程工具包


- [Toontown-Level-Editor](https://github.com/JawhnL5/Toontown-Level-Editor)
    - 16 Stars, 8 Fork

Disney 的 Toontown 关卡编辑器,
基于 Panda3D 1.6.2


- [vial-http](https://github.com/baverman/vial-http)
    - 12 Stars, 0 Fork

为 vim 准备的 http rest 工具

- [django-admin-tools](https://github.com/django-admin-tools/django-admin-tools)
    - 9 Stars, 1 Fork

扩展了 Django 的管理器.
追加了 扩展面板以及菜单

- [es-graphite-shim](https://github.com/distributed-system-analysis/es-graphite-shim)
    - 8 Stars, 3 Fork

ElasticSearch / Graphite 插件

能将 Graphite 查询转换为 ElasticSearch 映射

- [rgp](https://github.com/emehrkay/rgp)
    - 8 Stars, 0 Fork

RGP 在 Redis 基础上提供了简单的向量图数据库.
发布一组 Py 函式为界面.
可以基于顶点和边进行查询.

- [pbl](https://github.com/plamere/pbl)
    - 7 Stars, 0 Fork

构建 playlists 的库.


- [ebook-isbn](https://github.com/EugenePig/ebook-isbn)
    - 7 Stars, 0 Fork

eBook 工具.
能自动从 ISBN 提取元数据并重命名


- [TakeStock](https://github.com/sgerhardt/TakeStock)
    - 6 Stars, 0 Fork

项目提供股票的邮件报告.
通过抓取 NASDAQ 网站数据,
来获取股票价格等信息


- [codeofconductlink](https://github.com/emilyhorsman/codeofconductlink)
    - 6 Stars, 5 Fork

对软件社区进行追踪,自动分析出 成员的代码贡献

(`是也乎:`

嗯哼?! 国内的 [gurudigger](http://gurudigger.com/) 已经折腾了很多年了
)

- [django-dynamic-preferences](https://github.com/EliotBerriot/django-dynamic-preferences)
    - 4 Stars, 0 Fork

为 Django 项目进行动态全局/实例配置.

- [RedditTwitterPoster](https://github.com/rbalakit/RedditTwitterPoster)
    - 2 Stars, 0 Fork

从 reddit 订阅并发布为 twitter 嵌入式消息


- [jwords](https://github.com/kungsalman/jwords)
    - 1 Stars, 0 Fork

小程序,用来辅助单词记忆

- [markiavelli](https://github.com/justincosentino/markiavelli)
    - 1 Stars, 0 Fork

A Reddit bot that posts to /r/politics using text generated with Markov chains.

# 是也乎

- 150708 老高/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150704 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
