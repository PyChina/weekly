Title: 蠎加载 42
Slug: importpython-42
Date: 2015-08-14 17:17
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 42](http://importpython.com/newsletter/no/42/)



## 该读
~ 文章, Blog, 教程...

- [Python 绑定的 SQLite4 LSM Key/Value 存储](http://charlesleifer.com/blog/python-bindings-for-the-sqlite4-lsm-key-value-store/)
    + sqlite

SQLite4 文档有曰,
全新的 K/V 数据库将成为默认储存层.
于是,作者不淡定了,直接根据文档,
分析 LSM 头文件(非常小)完成编码,
变成了 [python-lsm-db](https://github.com/coleifer/python-lsm-db) 发布在 github 上.
当然的,文档在 RTFD.org : [lsm-db docs](http://lsm-db.readthedocs.org/)


(`是也乎:`

喜大普奔!-) redis 毕竟是第三方软件, SQLite 可一直内置在 Py VM 中的哪!

SQLite 毕竟小巧,追加新特性任性的多,
这次是 [log-structured merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree) 基于结构 log 的树合并 ?

嗯哼,此 log 非彼 log 参考: [The Log: What every software engineer should know about real-time data's unifying abstraction | LinkedIn Engineering](http://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)


)

- [Flask-Debug-API: 用Flask-DebugToolbar调试你的 REST API ](https://github.com/kevinbeaty/flask-debug-api)
    + flask

Flask-DebugToolbar 接口一览

- [在 AWS 设置队列服务: Django, RabbitMQ, Celery ](http://kronosapiens.github.io/blog/2015/04/28/rabbitmq-aws.html)
    + celery

文章带领我们在 AWS 上,
用 Django, RabbitMQ, Celery 用设置任务队列.
我们可以发现各个专门文档,但是,很少有联接起来组成完成服务的整体性文档.

- [Django 在 AWS 的负载均衡](https://www.caktusgroup.com/blog/2015/08/10/aws-load-balancers-django/)
    + aws

最近正好在 AWS 中折腾负载均衡,
虽然设置这项服务不复杂,
但是,还是有各种坑,所以,记录下来分享给大家.


-[Django Girls 代码之冬](http://blog.djangogirls.org/post/126496144993)
    django

"... Django Girls 主邮箱经常收到的问题是各个公司来咨询是否有靠谱的程序媛.
另一方面,又是程序媛在咨询是否有靠谱的职位.
所以,我们决定在网站上发布 工作 信息!"


- [PyGotham 2015 (NYC Python 大会) 演讲日程已发布!](https://pygotham.org/2015/talks/schedule)
    + conference

在 NY 的话,一定要上!

- [Flask API](http://www.flaskapi.org/)
    + flask

Flask API 是类似 Django REST 框架提供 web 浏览接口.
当前开发中,但是已经可用.
只是要关注新版本的发布说明,以免不兼容.

- [用 Python 生成素数列表](http://howchoo.com/g/ztk0mzq0mdy/generate-a-list-of-primes-numbers-in-python)
    + core python

素敉的寻找一向用作编程挑战的题目,
这里收集了一些有趣的方式, 来提取 50 以内的素数.

- [你的 Django 故事: 遇到 Cynthia Monastirsky](http://www.reddit.com/r/pyladies/comments/3ghj2s/your_django_story_meet_cynthia_monastirsky/)
    + django

Cynthia 来者阿根廷的 布宜诺斯艾利斯.
现为  Python/Django  程序媛.
Cynthia 是很多技术活动的参与者: Django/Python/基础设施/建筑/持续交付/前端...
以及各种当地社区.


- [Python 3.5.0 候选版本1 发布](http://feedproxy.google.com/~r/PythonInsider/~3/a1yIx-RxQW4/python-3.html)
    + new release

Python 3.5.0rc1 已经可下载,
预览版本,不建议用在生产环境中.
但是,作为 rc 已经足够接近最终版本了.
正式版本将在 9月中旬发布.

- [django_linter](https://github.com/geerk/django_linter)
    - django

只是个 Plylint 的简单扩展,
但是,针对 Django 工程.

(`是也乎:`

连 Django 都选择了 Pylint 看来可以决定了!

)

### 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...

- [big-list-of-naughty-strings](https://github.com/minimaxir/big-list-of-naughty-strings)
    - 3898 Stars, 135 Fork

`淘气字串大列表` ~ 收集了用户输入时经常出错的字串,
包含 py 脚本和 JSON 格式数据.


- [twitter-contest-bot](https://github.com/kurozael/twitter-contest-bot)
    - 34 Stars, 19 Fork

轮询推内容并转发,
灵感来自 http://www.hscott.net/twitter-contest-winning-as-a-service/

- [twitter-contest-enterer](https://github.com/robbiebarrat/twitter-contest-enterer)
    - 18 Stars, 1 Fork

输入 "Re-tweet to win"-式 内容

- [slashgif](https://github.com/karan/slashgif)
    - 7 Stars, 0 Fork

向 Twitter 发布 GIFs 
by doing "@slashgif coffee break".

- [flask-hashing](https://github.com/ThaWeatherman/flask-hashing)
    - 15 Stars, 0 Fork

Flask-Hashing 
作为 Flask 的扩展,
提供了方便的函式来完成各种 HASH 数据处理.


- [onedrive-d](https://github.com/xybu/onedrive-d)
    - 15 Stars, 1 Fork

Microsoft OneDrive 在 linux 上的客户端.

(`是也乎:`

嗯哼,希望 M$ 足够大肚,不会象当前 qq 一样禁止相关接口.
)
- [PlotSummary](https://github.com/MartinPaulEve/PlotSummary)
    - 12 Stars, 1 Fork

PlotSummary 用来扫描指定目录的文件,
并根据文件内容词汇生成相关 词频/分布 的图表!

(`是也乎:`

![JohnBarthExample](https://github.com/MartinPaulEve/PlotSummary/raw/master/docs/JohnBarthExample.png?raw=true)

目测不支持中文...

)


- [pocketmon](https://github.com/dufferzafar/pocketmon)
    - 6 Stars, 2 Fork

对标记的 Pocket 文章基于时间来提醒.

## DAMA 无责任推荐

# 是也乎

- 150814 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 150814 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
