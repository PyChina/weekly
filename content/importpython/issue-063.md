Title: 蠎加载 63
Slug: importpython-63
Date: 2016-03-07 15:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 63](http://importpython.com/newsletter/no/63/)

## 该读
~ 文章, Blog, 教程...


- [性能, 说服, 结构: 教练曰的 PyCon 演讲经验](http://feedproxy.google.com/~r/emptysquare/~3/XkZVIHjhgCw/)
    + pycon

在通向 PyCon 的几个月里,
对于演讲俺折腾了三种境界:
自己排练,向朋友排练,向专业教练排练.
猜猜哪种最有效果?
刚刚向歌剧演唱家,演讲教练 Melissa Collom 演练了两次,
她对我的 表现力,说服和结构,给出了建议,
我想这些建议同样对你有用.


(`是也乎:`

![how-i-rehearse-a-conference-talk](https://emptysqua.re/blog/how-i-rehearse-a-conference-talk/Emmeline-Pankhurst-011.jpg)
)

- [在 Django 中整合 Linkedin 接口](https://micropyramid.com/blog/integration-of-linkedin-api-in-python-django/)
    + api

通过整合 Linkedin ,我们可以获得用户验证的电子邮件 ID,
一般信息/最近的工作经历,
并分享文章.
完成整合,要以下操作:
1.创建 Linkedin 应用

2.进行用户身份验证,获得 token

3. 通过 token获取用户信息/工作经历...

- [Django 安全版本发布: 1.9.3 和 1.8.10](https://www.djangoproject.com/weblog/2016/mar/01/security-releases/)
    + security release

根据安全发布策略, Django 团队刚刚发布了 1.9.3 和 1.8.10.
主要解决了下文描述的安全问题.
建议用户尽快升级.
Django 主分支也已经升级.

- [为 Python 应用加速 Docker 镜像的构建.](http://blog.dscpl.com.au/2016/03/speeding-up-docker-build-times-for.html)
    + docker

最近写过一篇分析櫣部署 Python 的 web 应用的体验改进.
其中建议通过 Docker 可以有效提高部署速度,
现在,详细描述如何轻松的部署 Python web 应用到
Docker 或 OpenShift 3.

- [学用 Python 来折腾数据科学](http://pythontips.com/2016/02/27/learning-python-for-data-science/)
    + data science

我们决定将这两领域的资源放在一起,
以免浪费时间收集了.

- [2016 Python 教育峰会](http://pycon.blogspot.com/2016/03/2016-python-education-summit.html)
    + pycon

嗯哼, 今年的 Python 教育峰会 演讲者/内容 已公布!
将在 5月29号,周日举行,
专注如何通过 Python 将编程知识传播给教师/教育工作者以及宽泛的其它人群.
教育各种领域的教育工作者来古人讨论,学习新技术和工具,
分享激情!
同时号召更多场地:学院,大学,社区工作坊,在线编程,政府....

- [Python 中的模拟](http://python-resources.pythonblogs.com/304_python_resources/archive/1521_an_introduction_to_mocking_in_python.html)
    + testing

Python 单元测试库包含名为
`unittest.mock` 的子库.
引用它,能模拟各种测试时难以配置的资源.

- [EuroPython 2016: 普通门票价格](http://blog.europython.eu/post/140216367077)

如果明天(周二,3月1日 23:59 CET)午夜前你抢到了票,
能享受节省 200欧的早鸟票!
否则,就只有普通票了.

- [Python 101: imports 的各种](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/jrzpgYXNpdQ/)
    + core python

作为新手,首要知道的就是如何导入其它模块/包.
然而,注意到即使是使用 Python 多年的老手,
依然不清楚 Python import 机制的合理边界.


(`是也乎:`
推荐PyCon'2015, Montreal 上
David Beazley (@dabeaz) 的演讲

    Modules and Packages: Live and Let Die!

最完备的 Import 技艺!
)

- [Python: 缓存简介](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/if91dNlzvag/)

缓存是存储数据有限制集合,
用以加速数据检索.
这里描述一种使用字典完成高速缓存的实例.
通过标准库的 `functools` 模块来创建,
首先构建一个类,来建设高速缓存字典,
然后扩展为必要时启动.


- [Python 方法链的实例 (Python)](http://code.activestate.com/recipes/580616-python-method-chaining-examples/)
    + code snippet

这一片段,展示了 Python 中如何构建方法链

By Vasudev Ram.

- [任务队列 - Full Stack Python](http://www.fullstackpython.com/task-queues.html)
    - Full Stack Python

任务队列管理,发生在普通的 HTTP 请求-响应 周期之外.
`Full Stack Python` 收集了相关的所有文章.
建议阅读

- [本周 PyDev : Brett Cannon](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/2lIowbzyQGY/)
    + interview

Brett Cannon (@brettsky) 
从 03 年开始就是 Python 的核心开发者.
同时也一直坚持 Bloging.
也一直活跃在  PyCon 上.
你可以在 YouTube 上回顾他的一些分享
(比如: 如何兼容 Python 2/3 的代码...)
目测大家怎么都见过他的演讲,
内容都不错,那么多了解哈下的出好蛋的 Brett Cannon 吧.

- [现实世界中的错误处理](http://blog.miguelgrinberg.com/post/error-handling-in-the-real-world)
    + video

包含笔者在 Python Portland 用户大会上的演讲视频.
虽然某种意义上算不得专业,
但是,嗯哼,值得一看.

(`是也乎:`
作者是 Flask 的核心开发者

视频: https://www.youtube.com/watch?v=8kTlzR4HhWo

幻灯: https://speakerdeck.com/miguelgrinberg/error-handling-in-the-real-world

代码: https://github.com/miguelgrinberg/merry
)

- [基于类的视图: 基础](https://www.chicagodjango.com/blog/class-based-views-basics/)
    + django

`Class-based views`
是作者最爱的 Django 特性!
嗯哼, 只是更加喜欢结构化的,可预测的,形式...
所以,很多情况下,这一特性是不必要的...


## 新书
~ New Books


## 项目
~ 包/模块/库/片段...


- [public_drown_scanner](https://github.com/nimia/public_drown_scanner)
    - 327 Stars, 103 Fork

提供对 TLS 的 DROWN 攻击扫描.
基于 GPLv2 ,包含特定版本的
https://github.com/tintinweb/scapy-ssl_tls
以及
https://github.com/hiviah/pyx509

感谢发布这么好的模块的作者.


- [minimal-django](https://github.com/rnevius/minimal-django)
    - 194 Stars, 10 Fork

Django 的 `Hallo World`...
其实, Django 也是可以象 Flask 般使用的,
此仓库强调了一个事实,
Django 项目,可以简化为最基本的功能,
变得象微型框架!


- [GitMiner](https://github.com/danilovazb/GitMiner)
    - 126 Stars, 29 Fork

专业的 Github 内容挖掘.
通过对 github 页面的搜索和自动化索引,
说到做到发现/研究代码/片段.


(`是也乎:`

当 github 聚集了当前世界上最有价值的开源代码后,
对代码的深入理解/搜索, 都应该内置到 github 平台,
而这是 google 难以简单的完成的...

)

- [datacleaner](https://github.com/rhiever/datacleaner)
    - 55 Stars, 7 Fork

能对数据集进行自动清理,
以便进行数据分析!

(`是也乎:`

果然是 CLI 工具,专门为 Pandas 清理掉不合格的脏数据.
)

- [pocket-cli](https://github.com/rakanalh/pocket-cli)
    - 42 Stars, 2 Fork

Pocket-CLI 是命令行工具,
用来从 CLI 管理/查阅/发布
GetPocket.com 文章.

- [bluecanary](https://github.com/voxy/bluecanary)
    - 18 Stars, 2 Fork

自动构建/管理  AWS CloudWatch Metric Alarms

- [PyConvNet](https://github.com/Eniac-Xie/PyConvNet)
    - 15 Stars, 4 Fork

Convolutional Neural Network 
的 Python 版本.


## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 160307 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160307 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


