Title: 蠎加载 66
Slug: importpython-66
Date: 2016-03-31 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 68](http://importpython.com/newsletter/no/66/)

## 该读
~ 文章, Blog, 教程...


- [在社交图片中自动寻找武器 - 第一部分](http://goo.gl/qXpmgM)
    + image processing

嗯哼,应该有办法从社交渠道的照片中发现枪支或其它武器
(`是也乎`: 社会化反恐?!)

文章描述了如何将照片发送给 `Imagga API`
并获得包含对象的准确描述.
以及如何利用 Python 提高标记的准确性.

- [如何在 Django 中用 Elasticsearch (第 2 节), 填充数据](https://qbox.io/blog/elasticsearch-python-django-database/)

系列文章中,已经基于 Elasticsearch 在 Django 中创建了应用.
接下来就是数据的填充,
否则搜索是徦的了.


- [PyDataLondon 数据科学会议日程 (五月 6-8) - 发布 (videos made public post-conf)](http://pydata.org/london2016/schedule/)
    pycon

如果在 London, 应该参加,
太多髙能讨论

- [Anaconda 和 Hadoop --- 我们如何在一起的故事. ( Offtopic )](http://technicaldiscovery.blogspot.com/2016/03/anaconda-and-hadoop-story-of-journey.html)

第一次集群计算的体验发生在 1999,
在 Mayo Clinic 作研究生期间.
真心美好时光海苔, 导师是 Dr. James Greenleaf.
非常耐心的引导我们,搞定了 Mac Performa 老爷机,
建立了本地集群.
还免费给我们使用了半年的实验室空间....

- [构建有地理位置感应的 GeoDjango 应用](http://matthewdaly.co.uk/blog/2016/03/26/building-a-location-aware-web-app-with-geodjango/)
    + postgres

PostgreSQL 有非常赞的内置 PostGIS 扩展,
Django 的 GeoDjango 项目则能任性的享受之!
教程展示了如何快速集成 PostGIS ,支持用户搜索附近的演出.


- [如何使用 Tornado 构建简单的 Python WebSocket 服务](http://python-resources.pythonblogs.com/304_python_resources/archive/1529_how_to_create_a_simple_python_websocket_server_using_tornado.html)
    + tornado

随着实时 web 应用的增长,
WebSockets 在日益成为关键技术.
必须人工刷新来从服务器接收数据的日子早已过去.
实时更新不再需要从客户端轮询,
而是相反,从服务端直接下推!
强大的 Web 框架也开始支持 WebSockets 的开箱即用.

- [Django vs Moya 逐项对比](https://www.willmcgugan.com/blog/tech/post/django-comparison/)

嗯哼,不是定性哪, 只是进行类比.
通过代码对比演示,大家可以得到自己的结论,
条目包含: 模型/URLs/视图/模板...

(`是也乎:`

图样图森破了, Django 的强大从来不是其代码,
而是其无比坚实的生态链,
Moya 还想用 XML 来进行通用描述,实在....
)

- [用新加坡的 Smart Nation APIs 规划巴士班次](http://www.lihaoyi.com/post/PlanningBusTripswithPythonSingaporesSmartNationAPIs.html)

Singapore Smart Nation 是政府推动,
尝试改进国家运行效率的计划.
推出了一系列公开的实时数据接口,无论个人还是企业,
都可以来创造解决市政问题的方案.


- [Pythonic 的展示你项目的技能 Badges, 已支持 PyPI & ArchLinux AUR](http://forum.kloud51.com/d/52-badge-kloud51-com-a-pythonic-way-to-show-your-project-s-badges)

非常实用也 COOL,
"如果你有一个开源项目,那么自动展示你项目的 Badge/Pins/Shields/Medal"

(`是也乎:`
任何小事情标准化后,都是非常可喜的项目了


[![Build Status](https://secure.travis-ci.org/Alir3z4/html2text.png)](http://travis-ci.org/Alir3z4/html2text)
[![Coverage Status](https://coveralls.io/repos/Alir3z4/html2text/badge.png)](https://coveralls.io/r/Alir3z4/html2text)
[![Downloads](http://badge.kloud51.com/pypi/d/html2text.png)](https://pypi.python.org/pypi/html2text/)
[![Version](http://badge.kloud51.com/pypi/v/html2text.png)](https://pypi.python.org/pypi/html2text/)
[![Wheel?](http://badge.kloud51.com/pypi/wheel/html2text.png)](https://pypi.python.org/pypi/html2text/)
[![Format](http://badge.kloud51.com/pypi/format/html2text.png)](https://pypi.python.org/pypi/html2text/)
[![License](http://badge.kloud51.com/pypi/license/html2text.png)](https://pypi.python.org/pypi/html2text/)


)

## 新书
~ New Books




## 项目
~ 包/模块/库/片段...


- [pytrader](https://github.com/owocki/pytrader)
    - 519 Stars, 50 Fork

cryptocurrency 交易机器人

- [tmux2html](https://github.com/tweekmonster/tmux2html)
    - 63 Stars, 3 Fork

cat2: 渲染整个儿 tmux 窗口/格 为 HTML

(`是也乎:`

e.g: [color](https://share.esdf.io/FGlV4sufpt/color.html)

嗯哼! 能结合入 [asciinema](https://github.com/asciinema/asciinema) 就赞了!

)

- [Metaphor](https://github.com/NorthBit/Metaphor)
    - 84 Stars, 30 Fork

Metaphor - Stagefright with ASLR bypass

- [fail2ban](https://github.com/oussemos/fail2ban-dashboard)
    - 78 Stars, 9 Fork

Flask 编写的 Fail2ban web 仪表盘.


- [missingno](https://github.com/ResidentMario/missingno)
    - 58 Stars, 6 Fork

Missing data visualization module for Python.

- [reddit-is-gtk](https://github.com/samdroid-apps/reddit-is-gtk)
    - 51 Stars, 3 Fork

Reddit 的 GNOME 客户端 (使用 Gtk+ 和 Python)

- [stylenet](https://github.com/machrisaa/stylenet)
    - 48 Stars, 3 Fork

神经网络和 Style Synthesis

- [nbflow](https://github.com/jhamrick/nbflow)
    - 8 Stars, 1 Fork

一键式可重复工作流,
基于 Jupyter Notebook + Scons.

(`是也乎:`

Jupter 已经开始入侵各种实际生产场景了...
)

- [ifconfig-parser](https://github.com/tripples/ifconfig-parser)
    - 8 Stars, 0 Fork

解析 ifconfig 的输出,并更好的检索

- [python-sqlite-orm](https://github.com/fernandojunior/python-sqlite-orm)
    - 6 Stars, 2 Fork

A Python object relational mapper for SQLite

- [django-inline-svg](https://github.com/mixxorz/django-inline-svg)
    - 4 Stars, 0 Fork

A simple SVG template tag for Django

- [TwitterBot_Framework](https://github.com/NephyProject/TwitterBot_Framework)
    - 3 Stars, 0 Fork

Only little knowledge in programming, you can run Twitter Bot.

## DAMA 无责任推荐

- [10个最好用的 Python 工具/插件/库 - Livecoding.tv Blog](http://blog.livecoding.tv/2016/03/24/the-ten-10-best-python-productivity-tools-plugins-and-libraries)
    + 以及同类最10好的 C/C++/C#/JAVA/JS/Angular/H5 推荐....
    + 当然,都是 Livecoding.tv 一家之言...没有 github 的统计精确哈...

### 工作

....


# 是也乎

- 160401 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160331 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


