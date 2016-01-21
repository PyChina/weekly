Title: 蠎加载 56
Slug: importpython-56
Date: 2016-01-04 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 56](http://importpython.com/newsletter/no/56/)

## 该读
~ 文章, Blog, 教程...


- [持续更新的数据科学 IPython Notebooks](https://github.com/donnemartin/data-science-notebooks)
    + data science

深度学习,SPark,Hadoop MapReduce, Kaggle, scikit-learn, matplotlib, pandas, NumPy, AWS, Python 精粹 以及各种命令行技巧,
都在 ipynb 中...

- [成为 PyCon 2016 志愿者!](http://pycon.blogspot.com/2015/12/become-pycon-2016-volunteer.html)
    + conference

PyCon 大会一直是纯粹的社区运营.
如果你有兴趣成为志愿者,有很多渠道可以达成.


- [你的 Django 故事: 遇见 Amber Brown](http://blog.djangogirls.org/post/136156887178)
    + interview

Amber Brown 
是位自由软件开发人员, 以及计算机倡导者,
多年以来坚持编程实践,
为人周知的是著名项目 Twisted 的发行经理,
应邀在各种大会上分享有关经验,
包含: PyCon Czech Republic ‘15, DjangoCon Australia ‘15, 以及 Django Under The Hood ‘15.


- [Flask Scaffold](http://www.reddit.com/r/Python/comments/3yskc5/incase_you_need_to_build_database_driven_web/)
    + flask

Flask-Scaffold 
帮助你快速建议类似 blog 的 CRUD 式 web 网站,
基于 Py3 和 Angularjs 以及简要的模块.
通过 RESTful 接口还能支持原生 移动应用.


- [Django 中的并发数据库连接 | Heroku 开发中心](https://devcenter.heroku.com/articles/python-concurrency-and-database-connections)
    + django

当使用类似 Gunicorn 的多进程服务器时,
必须知道应用将数据推送到数据库,也是多连接的,
每个进程对应一个连接.
为了适应这点,很多工具都创建了可以同时容纳很多连接的连接池.



- [缓存 Django 会话 - 性能优化 12 天 - REVSYS](http://www.revsys.com/12days/caching-django-sessions/)
    + django , performance

都知道最好别用数据库来缓存 Django 的会话吧?
这真的应该多检查几次.
对于各种规模的系统,这是最容易忽视的潜在问题.
嘦在你的配置文件中搜索(grep) `SESSION_ENGINE` ,
就知道这坑是否在了,
如果不幸没有找到,那系统将自动保留会话到数据库,
你将很快获得一个巨大的哀伤...



- [The Star Wars 星舰](http://raspberry-python.blogspot.com/2015/12/the-star-wars-star-ships.html)
    + numpy

用 Python 代码推测出哪架星舰最快!

(`是也乎:`

好科学!
)


- [Python 正则表达式 - 匹配对象](http://howchoo.com/g/ymfhmtrhyjg/python-regexes-match-objects)
    + regex

在 Python 正则表达式可以在返回对象匹配.
此振兴,介绍如何利用这一形象.



- [2015 十大最受欢迎的 Django 库](http://blog.apcelent.com/most-popular-django-library-2015.html)
    + django

又一年, 用我们的方式来回顾高科技领域趋势.
通过访问, 我们获得了去年最受欢迎的 Javascript 库,
相同方式,我们也找到了最流行的 2015 Django 库.

(`是也乎:`

top3 是 Wooey/Channels/healthchecks.io

都没听说过...
)

### 工作

....

## 项目
~ 包/模块/库/片段...


- [sketch-rnn](https://github.com/hardmaru/sketch-rnn)
    - 106 Stars, 22 Fork


应用 Multilayer LSTM 以及 Mixture Density Network 
来在 TensorFlow 中创建路径建模矢量 SVG 图形


(`是也乎:`


![sketch-rnn](https://camo.githubusercontent.com/3c5e3c5941d02a01338d22d763790c953dfa5fba/68747470733a2f2f63646e2e7261776769742e636f6d2f686172646d6172752f736b657463682d726e6e2f6d61737465722f6578616d706c652f747261696e696e672e737667)


)

- [pygogo](https://github.com/reubano/pygogo)
    - 57 Stars, 2 Fork

又一个 Py 日志库,传说很给力

(`是也乎:`

![gogo](https://raw.githubusercontent.com/reubano/pygogo/master/gogo.png)


)

- [sgio](https://github.com/kazenniy/sgio)
    - 28 Stars, 0 Fork

ATA Pass-Through library for python

- [python-qBittorrent](https://github.com/v1k45/python-qBittorrent)
    - 27 Stars, 3 Fork

qBittorrent Web API (v3.1.x 以上版本兼容) 的 Python 包装

- [xkcd11th](https://github.com/drhagen/xkcd11th)
    - 15 Stars, 1 Fork

为什么 11号 总是低于每月其它日期的出现?

- [gifmail](https://github.com/sauravtom/gifmail)
    - 15 Stars, 1 Fork

动画版的 E-mails FTW

(`是也乎:`

![gifmail](https://camo.githubusercontent.com/99d9b2c9654c4779ff64955da66d5b0640f60a3c/687474703a2f2f736175726176746f6d2e636f6d2f7374617469632f696d672f6769666d61696c2e676966)

可是,这是为什么哪,,,
)


- [poyo](https://github.com/hackebrot/poyo)
    - 11 Stars, 0 Fork

:chicken: 又一 YAML 解析器

- [vizarray](https://github.com/ellisonbg/vizarray)
    - 8 Stars, 0 Fork

对 1d 以及 2d NumPy 数组可视化的模块

(`是也乎:`

![vizarray](https://github.com/ellisonbg/vizarray/raw/master/docs/images/example1.png)
)

- [termdic](https://github.com/hzwer/termdic)
    - 7 Stars, 0 Fork

命令行上的字典.

(`是也乎:`


![termdic](https://github.com/hzwer/termdic/raw/master/example.png)

国货, 使用有道api
)

## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

# 是也乎

- 160104 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160104 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


