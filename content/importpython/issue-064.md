Title: 蠎加载 64
Slug: importpython-64
Date: 2016-03-12 12:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 64](http://importpython.com/newsletter/no/64/)

## 该读
~ 文章, Blog, 教程...


- [Django Channels 简要介绍 - 在现实开发中的应用要点.](http://www.machinalis.com/blog/introduction-to-django-channels/)
    + django

通道, 是 Django 令人兴奋的全新功能.
可以令 Django 应用网站轻松支持外部工具/库(甚至于非 Python 的)
...

(`是也乎:`

简单的说, Django 终于决意进入 API 微服务时代了
)

- [K-均值 聚类在 手写数字识别](http://johnloeber.com/docs/kmeans.html)
    + machine learning

K-Means Clustering 
是机械学习的标准数据分析算法.
值得反复通过实用案例来理解...


- [从 Py3 返回: 是否值得折腾?!](https://www.toptal.com/python/python-3-is-it-worth-the-switch)
    + python3

自从 08 年亮相, Python 3 已经走了不短的路.
当初,缺乏几乎所有重要交 模块/工具 的支持.
虽然 Py3 提供了许多惊人的改进和功能,
能令我们写出更加健壮的 Python 代码.
Toptal 工程师 Dario Bertini,
以自己的经验来阐述 Python 3 的功能,是否值得切换.



(`是也乎:`

![be2f380fe3aad41333427ecd5a1ec5c5](https://assets.toptal.io/uploads/blog/image/92216/toptal-blog-image-1457618659472-be2f380fe3aad41333427ecd5a1ec5c5.jpg)

嗯哼, 包含非常 nice 的插图...
只是 py3 这事儿,无论多美好,就是缺少 killer 级别的动力哪...


)

- [Django Rest 框架 - JSON Web Token 认证](http://getblimp.github.io/django-rest-framework-jwt/)
    + django

如何在 Django 中实施 JSON Web Token Authentication (https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

- [部署流程 - Django 和 Docker | Manuel Morejón](http://mmorejon.github.io/en/blog/deployment-diagram-docker-django/)
    + django, docker

流程图谱,展示了如何基于 Docker 来部署 Django 应用


- [如何用 Python 和 Pandas 处理大型 JSON 数据集](https://www.dataquest.io/blog/using-json-data-in-pandas/)
    + pandas, json

处理巨型 JSON 数据集,一直非常痛苦,
特别是无法全部加载到内存中时.
此时, 其实通过 命令行工具组合 Python 脚本就能进行有效的数据分析和探索.
本文展示了如何利用 Pandas 来探索和绘制 Montgomery County, Marylan 的
出警活动热点图.


- [FYI PyCon 2016 2/3 准备好了! 应该抢票了!](https://twitter.com/pycon/status/705803119494504452?s=09)
    + pycon

At this moment, exactly 2,000 people are registered for PyCon 2016 — which puts us ? of the way to capacity!. If you are planning to visit now's the time to book the tickets.

- [Python 的 afl-fuzz 段错误](http://www.tomforb.es/segfaulting-python-with-afl-fuzz)
    + core python

American Fuzzy Lop 
是非常赞的进行模糊测试的工具.
此文介绍如何使用工具
来发现 CPython 的崩溃根源.


- [Mini REST+JSON 基准测试: Python 3.5.1 vs Node.js vs C++](http://szborows.blogspot.com/2016/03/mini-restjson-benchmark-python-351-vs.html)


嗯哼,需要一个简单的结论,
对于后端服务的 JSON 处理效能:
Python 3.5.1 vs Node.js vs C++
, 基于的框架是:
Python2.7 + Django + Gunicorn
对照的是 Node.js + Express 4, 
Python3 + aiohttp 
或是 C++.


(`是也乎:`

其实吧,这事儿有点扯...
JSON 中的 J 是谁?!
现在的语言选择,从来不是速度,而是综合的生态...特别是面向 wetware 的...

)

- [哪些书有助成为 Python 专家 ? - Reddit Discussion](http://www.reddit.com/r/Python/comments/49j7rs/what_python_book_for_experienced_programmers/)
    + Reddit Discussion

对于有经验的程序猿, 什么书值得看?!
提问者背景是 Ruby, C++, JavaScript (以及一点儿 Clojure) . 
未来雇主指定使用 Python,所以,要高速成为专家!

- [PyDev of the Week: Chris Moffitt](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/-r6CoNxPxSs/)
    + interview

This week we welcome Chris Moffitt (@chris1610) as our PyDev of the Week! Chris has been an active writer about Python on his blog and a speaker at DjangoCon.




## 新书
~ New Books

- 爱上Python ([Learn Python in One Day and Learn It Well](http://www.amazon.cn/Learn-Python-in-One-Day-and-Learn-It-Well-Python-for-Beginners-With-Hands-on-Project-The-Only-Book-You-Need-to-Start-Coding-in-Python-Immediately-Chan-Jamie/dp/1506094384/ref=sr_1_1?ie=UTF8&qid=1457804766&sr=8-1&keywords=Learn+python+in+one+day))

高分入门小书, 程序媛 写就 !-) 已经完成翻译,出版中,值得期待!

## 项目
~ 包/模块/库/片段...


- [neural-doodle](https://github.com/alexjc/neural-doodle)
    - 367 Stars, 13 Fork

将你的涂鸦转换为艺术品!

(`是也乎:`

![Landscape_example.png（PNG 图像，960x385 像素）](https://raw.githubusercontent.com/alexjc/neural-doodle/master/docs/Landscape_example.png)

莫纳风速成!

)

- [SSHKeyDistribut0r](https://github.com/Fachschaft07/SSHKeyDistribut0r)
    - 97 Stars, 7 Fork

自动化用户授权密钥分发!

(`是也乎:`

对于要管理大量不同系统/平台的开发者而言,
SSH Key 的丢失是世界崩溃!

)

- [resume](https://github.com/masasin/resume)
    - 33 Stars, 2 Fork

通过 YAML 文档,自动生成多种格式的简历

- [ascii_qgis](https://github.com/NathanW2/ascii_qgis)
    - 9 Stars, 3 Fork

ASCII QGIS 地图查看器


(`是也乎:`

![newrender](https://raw.githubusercontent.com/NathanW2/ascii_qgis/gh-pages/images/newrender.png)

作者曰了,创建工程的原因是:

    ...why not

好任性!俺喜欢!

curses+Qt 的小作品! 800 行...

~ [Custom QGIS Forms - YouTube](https://www.youtube.com/watch?v=Z84GMcQV3EM)

)

- [pyphoon](https://github.com/chubin/pyphoon)
    - 8 Stars, 0 Fork

ASCII Art 月相图 (Python version)

- [AnimeWatch](https://github.com/abhishek-archlinux/AnimeWatch)
    - 6 Stars, 1 Fork

mplayer 和 mpv 的前端

- [shahinday](https://github.com/BU-Computing/shahinday)
    - 6 Stars, 0 Fork

Python 实现基于终端的游戏.
可扩展,发展非常快...but kind-of self-documenting...

- [slackStocks](https://github.com/savala/slackStocks)
    - 5 Stars, 1 Fork

股票价格的 Slackbot 

- [packtSnatch](https://github.com/tjadanel/packtSnatch)
    - 4 Stars, 0 Fork

从 packtpub 免费学习页面
自动下载电子书的脚本...



## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 160313 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160312 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


