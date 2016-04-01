Title: 蠎加载 47
Slug: importpython-47
Date: 2015-09-18 18:18
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 47](http://importpython.com/newsletter/no/47/)

## 该读
~ 文章, Blog, 教程...


- [Python 中使用 SQLite 的 JSON 扩展](http://charlesleifer.com/blog/using-the-sqlite-json-extension-with-python/)
    + sqlite

文章中将构建一个 SQLite 全新的 JSON 扩展,
这样通过 pysqlite 就能令 SQLite 读入 JSON 了.

- [为 Flask 在 Travis-CI 构建持续集成以及开发环境 (x-post /r/python)](https://github.com/dpraul/flask-continuous-env)
    + flask

用 Grunt 构建 Flask 的前端构建环境,
持续测试则用 Travis-CI 驱动.
用 Nginx + Gunicorn 构建永续不宕的运行环境,
Fabric 进行简洁的配置管理.


- [mbentley/docker-django-uwsgi-nginx](https://github.com/mbentley/docker-django-uwsgi-nginx)

基于debian:jessie 的 Docker 镜像,
包含 Django (uwsgi) 和 nginx.

- [用 Falcon 和 PyPy 构建可大规模扩展的应用](https://impythonist.wordpress.com/2015/09/12/build-massively-scalable-restful-api-with-falcon-and-pypy/)

非常赞的方案!
但是,并没有给出基准测试报告

- [用 Python AST 和 Pandas 构建通用数据查询](http://tech-blog.serenytics.com/building-generic-data-queries-using-python-ast.html)
    + pandas

Paris.py 上一个非常赞的分享,
如何使用 Python AST 配合 Pandas 生成 SQL！
用 Serenytics 合理的追加数据列,更好的探索你的数据,
并能方便的输出为 CSV 或是给SQL 服务.


- [Djangocon 2015 上的 Django 1.8 和 PostgreSQL ](http://thebuild.com/presentations/django-1.8-postgresql-djangocon-2015.pdf)

幻灯!

- [全新 PSF Community 邮件列表](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/3hJuwVsNOYw/new-psf-community-mailing-list.html)
    + community

去年 PSF 通过决议,使社区更加开放,
嘦热爱 Python 都可以加入社区.
老的 psf-members 列表已经停止,
发布两个全新列表: psf-community 和 psf-vote


- [发布 PyCharm Edu 2: 简单胜过复杂](http://feedproxy.google.com/~r/Pycharm/~3/rva4EAbeemU/) 
    + pycharm

昨天发布的 PyCharm Edu 2, 是第二个免费版本,
专业又易用的 IDE, 内置了使用教程.

- [更好的交互式数据科学环境: Beaker 和 Rodeo](http://blog.dominodatalab.com/interactive-data-science/)

Domino 早已支持 IPython/Jupyter,
不过,刚刚追加支持了全新界面: Beaker Notebooks, 和 Rodeo,
文章给出案例来表述如何在新交互环境中使用 Domino.

(`是也乎:`
那个 莲花公司的 Domino ?!
)

- [用 Python 对 Markdown Headers 进行 Titlecases](http://pydanny.com/titlecasing-markdown-headers-with-python.html)

问题就在如何从复合目录和文件中,
用编程的方式,提取所有 md 文件的标准,进行自动化分析?


- [PeachPy: 用汇编生成高阶 Python](http://www.reddit.com/r/Python/comments/3lavrf/peachpy_assembly_code_generation_in_highlevel/)

PeachPy 是专注编写高性能内核组件的 Python 模块

(`是也乎:`

将 C 的事儿都作了,让 go 无力可出
)

- [构建自包含的 Python 3 应用来运行 PyPy](http://www.giantflyingsaucer.com/blog/?p=5680)

之前作者曰过 如何构建一种 Python 3 微型环境
(简单的 Minecraft 服务),
现在则是要构建一种 独立的自我包含的应用.
细节链接中.

- [为 Python 程序猿的 Julia](http://feedproxy.google.com/~r/TheEndeavour/~3/RrKfz4HZ6Tg/)

因为有客户在用 Julia,
所以,作者重新用为了起来,感觉就象一种 Python 的方言.

(`是也乎:`

细思恐极的是, Julia 的目标是成为更好那用的 R 方言哪.
)

- [图书章节: "用异步 Coroutiones 实现 web 爬虫"](http://feedproxy.google.com/~r/emptysquare/~3/-AB6aMVciZs/)

此章节是和 Guido van Rossum 同著的,
论述异步协程的应用,
书已上架, 此章可预览.


- [PyDev 之星: Christopher Clarke](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/0vDQxEOxCp4/)

本周我们欢迎 Christopher Clarke (@realchrisdev)
成为当周 PyDev 之星,
可能从他的 github 已经发觉了很多有趣的方面,
让我们挖掘更多趣点吧
!


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


- [videodigest](https://github.com/agermanidis/videodigest)
    - 89 Stars, 2 Fork

自动视频摘要.

- [pycaffe-recurrent](https://github.com/kuprel/pycaffe-recurrent)
    - 40 Stars, 8 Fork

在 ipynb 上训练用 pycaffe 折腾 LSTM 和 RNN 网络


- [django-rest-marshmallow](https://github.com/tomchristie/django-rest-marshmallow)
    - 22 Stars, 1 Fork

Marshmallow schemas for Django REST framework

- [retext](https://github.com/retext-project/retext)
    - 10 Stars, 0 Fork

Markdown 和 rST 的编辑器

(`是也乎:`

Qt 实现界面的...
)

- [Falcon-REST-API-Pattern](https://github.com/narenaryan/Falcon-REST-API-Pattern)
    - 8 Stars, 0 Fork

基于 Falcon 和 PyPy 可大规模扩展的 RESFul 接口框架

- [plotdf](https://github.com/jmoy/plotdf)
    - 5 Stars, 0 Fork

用以绘制2D微分方程相图 的 Python 模块.

- [strif](https://github.com/jlevy/strif)
    - 3 Stars, 1 Fork


为 strings+files 使用创建的简洁可用 Python 模块

- [twilio-fb-notification](https://github.com/sandipbgt/twilio-fb-notification)
    - 3 Stars, 1 Fork

能免费用 短信 接收 Facebook 提醒的脚本!

- [nfl-stats](https://github.com/jeremyjbowers/nfl-stats)
    - 3 Stars, 0 Fork

NFL 团队提供的工具,
包含播放器和游戏数据,
能准实时的获得状态!


## DAMA 无责任推荐

# 是也乎

- 150919 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 150918 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
