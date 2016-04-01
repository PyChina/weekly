Title: 蠎加载 16
Slug: importpython-16
Date: 2015-01-09 20:20
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


原文: [Import Python Weekly Newsletter - Issue No 16](http://importpython.com/newsletter/no/16/)


## 该读
~ 文章, Blog, 教程...

- [你的 Django 故事: 遇见 Ana Krivokapi?](http://blog.djangogirls.org/post/106894578478)

Ann 是 Red Hat 的工程师,
也是 `@OpenStack Horizon` 核心贡献者,
自行车手以及魔方教练.
是在 柏林首次掺合 `Django Girls` ,
`@infraredgirl` 可以发推给她.
在业余时间折腾 Django,
不过,下两个项目已经准备真正上 Django 了.


- [Falcon - 极简 Python WSGI 框架](http://falconframework.org/)

Falcon (`猎鹰`) 遵从 REST 架构风格,
这意味着你可以将所有事物,
视为资源和状态的转换,并自然映射到 HTTP 元语上.

(`是也乎:`
![silhouettes](file:///Users/zoomq/mnt/%E5%BF%AB%E7%9B%98/zScrapBook/zqPythonic/data/20140105010924/flight-silhouettes.gif)

旁的不说,这设计是用心了..
只是用 `Class` 来组织用户代码就...
)



- [用 Pandas 来分析 Python 职位市场](http://pawelmhm.github.io/python/pandas/2015/01/01/python-job-analytics.html)

作者新坑,
用 Pandas 结合就业市场的公开数据,
来分析 Python 方面的趋势.

(`是也乎:`
够 bigger,
但是和天朝无关...)

- [在你的 Django 项目中集成前端工具](http://feedproxy.google.com/~r/LincolnLoop/~3/xFT-Rzte1NU/)

类似  Grunt 和 Gulp
的前端工具越来越普及,
已经令前端代码不能再视作静态的了,
CSS/JS模块的预处理已经成为标配,
Browserify 甚至于 coffeescript 也在兴起,
在 `Lincoln Loop`
我们就将 Gulp 结合到了 Django 中.

- [配置 ElasticSearch 用 Python 使用基本 Auth 和 SSL ](http://charlesleifer.com/blog/setting-up-elasticsearch-with-basic-auth-and-ssl-for-use-with-python/)

涉及 ElasticSearch 
如何使用自制签名,
完成互联网访问.

- [PyCharm 发布 4.0.4 更新](http://feedproxy.google.com/~r/Pycharm/~3/e73S5go3PNg/)

随着 2015 第一周即将过去,
> PyCharm 团队兴奋的发布了
> PyCharm 4.0.4 build 139.1001 .
> 包含了很多改进:
> IPython notebook 的集成
> 调试器
> 嵌入式本地终端
> git/svn 的支持
> 类引用的反射
> 支持 Lettuce
> CSS 支持

等等,我们关注的好物

- [Python 挑战赛](http://slott-softwarearchitect.blogspot.com/2015/01/the-python-challenge.html)

对于 `Python Challenge` 什么是重要的?
那就是不仅仅只 Python !
任何编程语言,都可以来挑战.
俺已经发现用 Pillow 能更好的解决问题 7和11,
俺肯定类似 PIL/Pillow 的工具包, 对任何语言都一样重要.

- [virtualenvwrapper 4.3.2 -- virtualenv 的增强](http://feeds.doughellmann.com/~r/DougHellmann/~3/XjEQZFVLnHg/virtualenvwrapper-4-3-2-enhancements-to-virtualenv.html)

virtualenvwrapper 是 virtualenv 的一组扩展.
用以创建和清除虚拟环境,
来配合你的工程管理流程,
令你进行多项目开发时,不会引入依赖的冲突.

(`是也乎:`
大妈的体验是: 用 `pyenv`
而且, `pyenv` 也可以嵌入 virtualenvwrapper 命令的)

- [多期望学 Python 时就知道这些事儿](http://bugra.github.io/work/notes/2015-01-03/i-wish-i-knew-these-things-when-i-first-learned-python/)

有时,俺发现总是在问自己

> 为毛俺总是不知道在 Python3 中可以这么简单的 "做" 这事儿?

每毎俺四处寻求方案时,
总能发现比之前知道的更加优雅/高效/无虫的代码,
这才只是开始,
慢慢的才进一步知道,要追求的是

> 可用/简单/可维护 的代码!

- [PyCon 2015 议程释放!](http://pycon.blogspot.com/2015/01/pycon-2015-schedule-announced.html)

PyCon 2015 的日程已经可访问!

教程的时间表已经上线好几周了,
还制作了海报反馈良好.
最重要的部分也已完成:
用5个房间调度好了 95 位讲者!

## 项目
~ 包/模块/库/片段...


- [sphinx](https://github.com/sphinx-doc/sphinx)
    - 29 Stars, 5 Fork

没人不知道这模块吧!
官网: http://sphinx-doc.org/.

- [markovify](https://github.com/jsvine/markovify)
    - 21 Stars, 0 Fork

Pythonic 的可扩展的 马尔可夫链发生器.
主要用以构建 Markov 模式的大型语料库,
生成随机的句子,
当然,理论上,可以用以其它应用.

- [3102](https://github.com/fooying/3102)
    - 11 Stars, 6 Fork

域名/ip 
模糊测试工具
用来挖掘漏洞, http://www.fooying.com

- [django-api-tools](https://github.com/szpytfire/django-api-tools)
    - 9 Stars, 0 Fork

(`是也乎:`
前期 蠎周刊 已经报道过了.)


- [edify](https://github.com/chilcote/edify) 
    - 5 Stars, 0 Fork

对 OS X 系统管理员非常有用的脚本,
能存储和显示 CLI 参数的简短说明.

- [mysql-python-class](https://github.com/nestordeharo/mysql-python-class)
    - 5 Stars, 2 Fork

又一个用来连接 MySQL 数据库的模块,
获得查询结果,
诸如: SELECT (一或多条), INSERT, UPDATE, DELETE.

- [homeimages](https://github.com/rmuslimov/homeimages)
    - 4 Stars, 1 Fork

从 SD 卡中同步所有照片和视频

- [immut](https://github.com/jcomo/immut) 
    - 4 Stars, 0 Fork

又一个不可变对象库.

- [k](https://github.com/bfontaine/k) 
    - 2 Stars, 0 Fork

Python 的枚举类型支持库.

(`是也乎: 
有道是...

> 名字起的好
> 项目活的了

这种单字母的项目名称,就是自绝于搜索引擎哪,无人知简直是必须的哪.
)

## 曰了
~ Tweets


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150109 用时 51 分钟完成快译.
- 150109 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
