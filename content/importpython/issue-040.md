Title: 蠎加载 40
Slug: importpython-40
Date: 2015-07-27 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 40](http://importpython.com/newsletter/no/40/)



## 该读
~ 文章, Blog, 教程...

- [Pycon 中国](http://cn.pycon.org/)
    + pycon

已经是第5届!
由 PyChina.org 主办, 相关社区合办,今年将在北上广三城,
分别举行,官网已经开始征集分享议题, 请积极参与,营造自个儿的大会.

ps:
中文版的 ImportPython Newsletter 也是 PyChina 社区主持快译的:
http://weekly.pychina.org/importpython/index.html

- [如何在 Ubuntu 14.04 中令 Django 协同 Postgres, Nginx, 和 Gunicorn on Ubuntu 14.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04)
    - postgres, django

详细演示如何安装/配置一系列组件,令Django 流畅运行起来

- [用 Python 检查恶意软件](https://www.endgame.com/blog/examining-malware-python)

之前就曰过, 想开发格哪学习来解决安全问题,
缺乏开放和标记数据库是个巨大的隐患.

这里就是立志解决这一问题的标记工作.


- [介绍全新的高速 UnQLite Python 绑定库](http://charlesleifer.com/blog/introduction-to-the-fast-new-unqlite-python-bindings/)
    - cpython

UnQLite 是种无服务的 JSON 式文档 键/值 数据库.
一年前,作者用 Python 创建了这一项目,
现在用 Cython 重写了整个儿库,
完成了速度上数量级的提高.


- [定量分析: 使用 Notebooks](http://feedproxy.google.com/~r/Pycharm/~3/uzryswOBBMw/)
    - pycharm

这是运用 Python 进行定量分析的系列blog.
本文先介绍了 IPy 的 notebook,
一个当前最流行的结构化计算工具.

- [uWSGI 瑞士军刀](https://lincolnloop.com/blog/uwsgi-swiss-army-knife/)
    + wsgi

uWSGI 是那种即使每个版本都在增加新功能,但是工程却没有变的臃肿/缓慢/不稳定的项目.

文中分享了一些技巧来利用 uWSGI 优化你的服务.


- [从自行车计数分析西雅图的工作习惯](https://jakevdp.github.io/blog/2015/07/23/learning-seattles-work-habits-from-bicycle-counts/)
    + machine learning

去年作者写文章论述了通过研究在 西雅图 自行车骑行的趋势,
以及和 天气/星期 等其它因素的关联.
现在从另外一个角度进行分析,
并构建了无监督的机械学习模型,
来进一步探索

- [Guido Van Rossum 在 europython 2015 的演讲](http://www.reddit.com/r/Python/comments/3e1ppr/guido_van_rossum_live_at_europython_2015/)
    + video

3小时! 必看.

https://www.youtube.com/watch?v=yCg3EMf9EYI


- [Django 和 Python 3 用 Pyenv 完成多环境配置](http://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/)
    + python3

需要 Python 3 环境来开发 Django 应用,
但是,同时又得兼顾几个运行在 2.7 环境中的老应用.
幸运的是 Pyenv 能完成良好的环境猜测和自动切换.


- [用 Apache Spark 和 Flask 构建电影推荐系统 - 第一部分 | Codementor](https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1)
    + machine learning

此教程,一步步引导如何使用 MovieLens 数据集,
用 Spark 的协同过滤器完成分析,形成推荐.
主要由两部分组成:
第一个是获取和分析电影的收视率数据,并导入为 Spark RDDs.
第二个是构建推荐,并通用化为其它应用也可以使用.

- [理解 Django 中间件](http://agiliq.com/blog/2015/07/understanding-django-middlewares/)
    + django

同以往 Agiliq 贡献的好文一样.
假设读者已经阅读过 Django 中间件相关文档.
这里进一步详细阐述涉及的各种关键概念.

- [Mesos & Django (以及 Aurora 和 CircleCI) — Michael Twomey](http://www.twoistoomany.com/blog/2015/7/16/mesos-django-and-aurora-and-circleci-too)
    + django

在 Ireland 大会上有曰,
综合 Aurora 以及 CircleCI 让 Django 应用部署幸福起来.
这里有进一步的笔记.



- [一些快速技巧](http://b-list.org/weblog/2015/jul/22/couple-quick-tips/)
    + django

这天,你又花了不少时间梳理开源代码/维护/发布,以确保所有实例都用上了最新代码.
这一路,其实有很多小技巧能加速这一过程的.
那么,以 编写和发布 Django 应用为例来实践一下吧.


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

- [rockstar](https://github.com/avinassh/rockstar)
    - 1558 Stars, 96 Fork

2分钟以内创建 Rockstar C++ 程序!
虽然和 Python 无关,但是相当有趣.

- [tushe](https://github.com/ericls/tushe)
    - 36 Stars, 9 Fork

用 Flask 完成的web 服务 专注图库的浏览/分享.

- [DQN-chainer](https://github.com/ugo-nama-kun/DQN-chainer)
    - 36 Stars, 3 Fork

Python 用 Chainer 实现的 Deep Q-Networks 来自动玩
ATARI 游戏.

- [pyside2](https://github.com/PySide/pyside2)
    - 23 Stars, 0 Fork

pyside 在 github 的仓库

- [SpeechBot](https://github.com/Martyn96/SpeechBot)
    - 15 Stars, 1 Fork

用 Python 来朗读 Telegram 文字的机械人

- [django-sabot](https://github.com/rosarior/django-sabot)
    - 15 Stars, 0 Fork

在你的 Django 项目中管理可预见的错误


- [Elemental](https://github.com/ElementalCode/Elemental)
    - 8 Stars, 1 Fork

为前端 web 技术完成的可拖放块.

- [PyPhantom](https://github.com/ryanskidmore/PyPhantom)
    - 8 Stars, 1 Fork

PhantomJS 的基础接口

(`是也乎:`

爬虫必备武器,也是无头浏览器的关键组件.

)


- [textcom](https://github.com/TachyonNZ/textcom)
    - 5 Stars, 2 Fork

Python 用 XCOM: Enemy Unknown 实现的基于文本的 Roguelike 

- [reddit_authorship](https://github.com/aehaynes/reddit_authorship)
    - 4 Stars, 4 Fork

对 Bitcoin 多帐号的交易检验 ,
报告全文参考 andrehaynes.me/portfolio 

## DAMA 无责任推荐

# 是也乎

- 150727 [Zoom.Quiet](http://zoomquiet.io) 完成快译
- 150727 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
