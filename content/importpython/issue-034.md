Title: 蠎加载 34
Slug: importpython-34
Date: 2015-05-30 23:32
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 34](http://importpython.com/newsletter/no/34/)

## 该读
~ 文章, Blog, 教程...


- [Python 实现的 Redis样数据库](http://charlesleifer.com/blog/alternative-redis-like-databases-with-python/)
    + redis

Rlite 之于 Redis ,就象 SQLite 和 Postgresql.
意味着, 可以提供一个 Redis 功能相同的无服务器数据库,
轻易嵌入到你的应用中.

- [Djangui](http://www.reddit.com/r/Python/comments/37f0s9/djangui_a_djangopowered_ui_for_python_scripts/)
    + django, core python

为你的应用, 提供 Django 支持的界面.
很漂亮,细节链接内部.

- [如何正确的开源自制 Python 库](https://www.endgame.com/blog/open-sourcing-your-own-python-library-101)
    + core python

对创建一个靠谱的 Python 开源项目,
给出了完备的建议,包含版权控制/代码包装/安装分发....

- [加速不可变的 Python 部署过程 | Lincoln Loop](https://lincolnloop.com/blog/fast-immutable-python-deployments/)
    + pip

对于 wheels 在我们服务上没有提供软件附加层的事儿,
我们非常兴奋!
因为这意味着, 在 Python 大型系统部署方面,
依然有创新空间!
我们期待着下一步的改进!



- [为 Django 给 MySQL 构建更好的数据库缓存](http://adamj.eu/tech/2015/05/17/building-a-better-databasecache-for-django-on-mysql/)
    + mysql

用 MySQL 完成缓存,细节链接中

- [PyCon JP 2015 议题征集](http://pycon.blogspot.com/2015/05/pycon-jp-2015-call-for-proposals.html)
    + pycon

投稿截止为 7月15,
细节官网中.

- [PyPy.js: 是什么为什么以及如何 by Ryan Kelly (PyCon 2015 必看演讲: 5/6)](https://www.caktusgroup.com/blog/2015/05/26/pypyjs-what-how-why-ryan-kelly/)
    + javascript

在研究了 Ryan Kelly 的演讲后,
确认实际可行!
直接在浏览器中运行 Python
(不是通常的以 Python 语法编写,然后转化为 js 来运行).

PyPy.js 结合了两项目技术:
PyPy(用 Python 实际的 Python 解释器!),
以及 Emscripten
(LLVM 到 JavaScript 的转换器,通常用以开发浏览器中运行的游戏),
从而在浏览器中运行  PyPy


- [给 Python 程序猿的 Rust](http://lucumr.pocoo.org/2015/5/27/rust-for-pythonistas)

当前 Rust 已经 1.0 相当稳定,
是时候向 Python 程序猿介绍 Rust 了,
本教程越过语言基础,
直接对比常见结构的不同,以及表现.


- [PEP8 交给机械来照顾,人关注更高层次的吧!](http://www.avilpage.com/2015/05/automatically-pep8-your-python-code.html)
    + PEP

对懒惰的人而言,更希望有人来自动格式化代码.

(`是也乎:`

细思恐极的是, golang 天然内置了 gofm 工具,
这就是老鸟更加洞察人心的证据嘛!?
)


- [对 WSGI 应用的实际流量进行监察.](http://blog.dscpl.com.au/2015/05/performance-monitoring-of-real-wsgi.html)
    + wsgi

无论在生产/测试或是QA环境中,
我们都需要收集的所有 WSGI 流量导出,以便进行分析以及可视化展示

- [面向初学者的 Flask web 应用开发](http://www.reddit.com/r/flask/comments/3733x2/flask_web_application_development_introduction/)
    + flask

教程目标是一个简单的 TODO 系统,
基于 Flask/SQLalchemy/PostgreSQL 9.3 以及 Vertabelo,
并最终部署到 Heroku.
当然,代码无法用作生产系统,
只是用来展示 Python 开发 web 应用的思路.


(`是也乎:`

![Patrycja Dybka](http://www.vertabelo.com/_file/blog/authors/patrycja_dybka.png)

又一位MM 程序媛写的教程!
)

- [为 Django 前端现代化贡献我们的力量吧](http://owaislone.org/blog/modern-frontends-with-django/)
    + django

Django 已经足够伟大了,
但是,其前端工具链依然非常原始.
有理由怀疑,类似 GWT 是可行的...

- [优化 Python 案例研究](https://www.airpair.com/python/posts/optimizing-python-code)
    + python

想撰写运行快的 Python ,
首先瞧不起知道是程序什么上花费了时间,
什么操作将拖慢你的系统?

- [Django 中的精简和优化迁移](http://www.rkblog.rk.edu.pl/w/p/squashing-and-optimizing-migrations-django/)
    + django

随着 Django 7.1 的发布,
我们面临一组必须构建的迁移和优化工具,
必须更快的测试数据库,完成旧代码/历史的迁移和精简.
当前还比较粗糙,但是配合手工作业,
已经可以获得一个最精简的迁移,细节链接中.



- [能令 Django 应用卓越的 33 个项目 | elweb](http://elweb.co/33-projects-that-make-developing-django-apps-awesome/)
    + django

这是一个不完备的列表,
收集了口碑上佳以及亲自测试过的项目.
能切实帮助我们完成卓越的应用




- [Ned Batchelder 访谈](http://www.podcastinit.com/)
    + podcast

Podcast from 
来自 podcastinit 的播客节目


## New Books


## 项目
~ 包/模块/库/片段...

- [HTTPLang](https://github.com/Max00355/HTTPLang)
    - 233 Stars, 15 Fork

HTTP 请求的脚本化


(`是也乎:`

非常象 Gopher 大会上批露的,老许用 go 实现的 http 测试 DSL.


    set URL http://google.com
    loop 5
    do GET /
    show $STATUS
    endloop

)

- [kindle-highlight-scraper](https://github.com/mieubrisse/kindle-highlight-scraper)
    - 43 Stars, 7 Fork

对 Kindle 中高亮以及笔记的下载脚本,
json 格式的


- [colorblocks](https://github.com/zzggbb/colorblocks)
    - 25 Stars, 2 Fork

生成颜色/尺寸的随机块


- [DiscoverHiddenSSID](https://github.com/linvex/DiscoverHiddenSSID)
    - 19 Stars, 13 Fork

发现隐藏 wifi 热点 SSID 

- [killallbtn](https://github.com/sakura26/killallbtn)
    - 15 Stars, 3 Fork

一个实体的解决反查水表的瞬间清除所有主机/服务/数据的
超级作品!

(`是也乎:`

![大红钮](https://raw.githubusercontent.com/sakura26/killallbtn/master/pics/button_sample.JPG)

)

- [drf-tracking](https://github.com/aschn/drf-tracking)
    - 15 Stars, 0 Fork

追踪 Django Rest Framework API 请求的工具.

- [CollaborativeFiltering](https://github.com/saimadhu-polamuri/CollaborativeFiltering)
    - 10 Stars, 9 Fork

基于 Collabrative Filtering 方法
实现的推荐引擎.

- [liberapay.com](https://github.com/liberapay/liberapay.com)
    - 4 Stars, 0 Fork

通用捐助平台

- [penrose](https://github.com/xnx/penrose)
    - 2 Stars, 0 Fork

Penrose 贴画的 python 生成包.


## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)

### 工作

-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
急招 N 名有服务端开发经验的 **gopher**!




# 是也乎

- 150601 [Zoom.Quiet](http://zoomquiet.io) 完成
- 150530 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

