Title: 蠎加载 54
Slug: importpython-54
Date: 2015-12-17 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 54](http://importpython.com/newsletter/no/54/)
- 嗯哼, 蠎加载终于又回归了,,,继续 happy 快译.
- (为什么说又!?)

## 该读
~ 文章, Blog, 教程...


- [高级 Python 图书](https://migrateup.com/store/advanced-python-book/)

Aaron Maxwell 已经主持 `Advanced Python Newsletter` 有段日子了,
过去一年积累了很多好文章,
结集成了: `Advanced Python`
不以入门者为目标的,
讨论各种强大模式/特点,以及语言发展的好书.



- [用 Bottle 框架 构建 Rest API](http://www.toptal.com/bottle/building-a-rest-api-with-bottle-framework)

Bottle 是最轻量级 Web 应用框架.
体积小/速度快/易用,
而且非常辞行构建 RESTful 服务.
在作者的折腾经验中,
基于 DigitalOcean 平台,用 uWSGI 服务桟,
每请求可以低至 140ms,
文章分享了这一构建过程. 

- [测试 Django 应用](http://blog.endpoint.com/2015/12/testing-django-applications.html)

文章汇集了各种 Django 应用测试相关资源和文章.
为新人能快速融入项目详细列举了具体准则.
还提供了内置单元测试库和 pytest 之间的对比.
重点是测试 Django 和数据库的交互.

- [“应用开发团队如何配合 PyCharm IDE 使用 Vagrant “](https://developer.rackspace.com/blog/a-tutorial-on-application-development-using-vagrant-with-the-pycharm-ide)

详细指导,如何使用 PyCharm + Vagrant 
组织开发.

- [PyCharm 中使用 Docker](http://feedproxy.google.com/~r/Pycharm/~3/1kuKe77FdjI/)
    + docker

现代软件工程强调开发和生产环境的隔离以及再现.
Docker 及其相关解决方案非常流行.
随着 PyCharm 专业版 5 的发布,
现在可以任性的在 IDE 管理 Docker 事务了. 

- [你的 Django 故事: 遇见 Jessamyn Smith](http://blog.djangogirls.org/post/135196284658)
    + interview

Jessamyn Smith 是领域经验超过10年的全桟软件工程师,
主要开发 web 应用后端服务.

她的专长是测试/软件设计/重构遗留代码/追加自动测试, 以及自动化櫣和部署.
是有执照的专业工程师,
同时也是 Ziversity.com 的CTO,
也是帮助 LGBTQ(土著/少数民族妇女) 构建安全空间并分享经验的组织管理者.


- [Oreilly 的 Hands-on Python workshop ](http://www.oreilly.com/pub/e/3628)

在这次由 Steven Lott 领导的 hands-on workshop 中,
通过 "Python 加密代理"
,"Python 函式编程"
,"Python 面向对象编程"
将学会 什么是命名空间?
应该尽可能使用.
使用内建命名空间别名,
还能定制.


- [PEP8 壁纸](https://dl.dropboxusercontent.com/u/7335766/wall-pep8.png)

简洁的壁纸,包含 蠎之禅.

- [Django 2016 捐助活动启动](https://www.djangoproject.com/weblog/2015/dec/17/announcing-2016-fundraiser/)

目标是 $200,000 用以资助研究员计划,
继续促进 DjangoGirls 活动,
以及年度大会等等.


- [Python 不是 C: 讨论2](http://www.reddit.com/r/Python/comments/3x32d0/python_is_not_c_take_two/)

教训是明确的: 别将 Python 写成 C.
使用 numpy 进行数组操作,而不是循环.

对于多数人而言,这意味着观念的转变;
鉴于 Python 的生态系统在高速发展,
作者决意将以往的工具链进行重构.
通过一个处理空间数据的项目,
目标在帮助 跨越美国的自行车运动(RAAM)优化路径,
要对 2015 年比赛中获得的大约 25000 个地理点,
进行经纬计算,求出最短路径....

- [自动化和 pty(4)](http://www.reddit.com/r/Python/comments/3wyo2a/automation_and_pty4/)

在 UNIX 界面中任何命令都能自动化.
文章演示如何使用 伪终端 来令应用以为接入了一个不存在的终端.
次技术原先是用以解决硬件的软件模拟的,
现在多用与测试

- [Pytz & Django 中的时区](http://tommikaikkonen.github.io/timezones)

时区!
航运软件的蠢事儿!
如果遇到过类似问题, 应该认真看看此文!
前提是熟悉相关库,
理解 自然和意识 日期,
当然得懂点 Dajngo.

- [建立并管理你 Django 应用的最简洁方式 - Aldryn](http://www.aldryn.com/en/)

基于 Django 的商业产品,
能快速建立 CMS, 值得体验. 

- [第 35 集 - Sylvain Thénault on ASTroid](http://podcastinit.podbean.com/e/episode-35-sylvain-thenault-on-astroid/)
    + podcast

Python 的 AST (抽象语法树) 是非常强大的工具.
能支持我们创建自己的语言.
ASTroid 能简化我们使用 AST 的过程.
这一集中, 采访了 ASTroid 的创始人 Sylvain Thénault,
分享了如何用ASTroid 驱动 PyLint 进行静态代码分析.


### 工作

....

## 项目
~ 包/模块/库/片段...


- [chainer-DCGAN](https://github.com/mattya/chainer-DCGAN)
    - 97 Stars, 12 Fork

Chainer 实现深卷积生成对抗性网

- [write-rnn-tensorflow](https://github.com/hardmaru/write-rnn-tensorflow)
    - 52 Stars, 6 Fork

使用 LSTM 混合密度网络与 TensorFlow 生成手写文字.


- [GoTimer](https://github.com/LangdalP/GoTimer)
    - 48 Stars, 13 Fork

Python 完成的 `CS:GO` 用简单炸弹定时器外挂

- [cyjson](https://github.com/mitghi/cyjson)
    - 28 Stars, 1 Fork

快速 JSON 解析器

- [pygamii](https://github.com/carlosmaniero/pygamii)
    - 13 Stars, 1 Fork

ASCII 游戏引擎

- [py-mysql-elasticsearch-sync](https://github.com/zhongbiaodev/py-mysql-elasticsearch-sync)
    - 9 Stars, 0 Fork

MySQL 到 Elasticsearch 同步工具

- [Stockfighter](https://github.com/Rami114/Stockfighter)
    - 9 Stars, 4 Fork

又一个 Stockfighter API 的 Python 包装.

- [python-mwviews](https://github.com/mediawiki-utilities/python-mwviews)
    - 6 Stars, 0 Fork

从静态 dump 以及在线接口,
解析并查询 Wikimedia 基金会的浏览量.


- [django-notify-x](https://github.com/v1k45/django-notify-x)
    - 6 Stars, 1 Fork

Django 的提醒/通知系统.


## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

# 是也乎

- 151218 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 151218 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


