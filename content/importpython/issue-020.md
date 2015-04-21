Title: 蠎加载 20
Slug: importpython-20
Date: 2015-02-06 17:17
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 20](http://importpython.com/newsletter/no/20/)


## 该读
~ 文章, Blog, 教程...


- [Django 技巧: 如何找到视图的性能瓶颈?](http://djangotricks.blogspot.com/2015/01/performance-bottlenecks-in-django-views.html)
    + django

一旦有长期运行的 Django 项目,
就得开始持续的性能优化了,
经验是先定位瓶颈, 
用更加地道的代码替换,
然后用 DB/缓存/其它技术来消解之.


- [IPython 2.4 以及 IPython 3.0b1 发布](http://ipython.org/ipython-doc/dev/whatsnew/version3.html#release-3-0)
    - new release

3.X 将是 IPython 最后一个独立版本系列,
未来专注和语言无关的组件升级
(notebook, qtconsole, ..)
由名为 `Jupyter` 的全新项目统领.
而 Python 相关的
(交互 Shell, 内核, 并发...)
还在 IPython 下持续


- [PostgreSQL 技巧集](http://blog.endpoint.com/2015/01/a-few-postgresql-tricks.html)
    - postgres

俺们刚刚遇到了点有趣的状况,
并用靠谱的技巧摆平了,
自然得分享出来.

(`是也乎:`
只有两条...)

- [用 Python 通过抓取网页数据用机械学习来进行情感分析](http://blog.monkeylearn.com/kimono-monkeylearn-sentiment-analysis-with-machine-learning-and-web-scraped-data/)
    - pandas,machine learning

基于 Kimono Labs, 对分布式结构数据,
以 MonkeyLearn 提供的机械学习能力,
将数据转化为概念结论.

> Kimono 是智能 web 爬虫,将网站数据变成 API 来调用
> MonkeyLearn 是个平台,专注从文本中挖掘相关数据

- [如何使用 Django 的 Proxy Models](http://feedproxy.google.com/~r/TheWellfireInteractiveBlog/~3/kpJQuyT_Dyw/)
    - django

proxy 模块其实是 Django 中最关键的功能了, 
但是,关注不多?!
作者分享了如何不用变更 DB 就获得干净的接口数据.

- [Django Girls 华沙编程工作坊](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/dGvUHnM1kK8/django-girls-warsaw-carrot-coding.html)

PSF 支持的工作坊,
为 华沙的 Django Girls 活动捐助了 1千刀.
虽然不多, 但是能产生足够的影响.

- [Wing IDE 5.1 发布](http://wingware.blogspot.com/2015/01/wing-ide-51-released.html)
    - new release

Wingware 发布 Wing IDE 5.1 版本!
作为一种跨平台全部功能 IDE,
包含 vi/emacs/VS 键绑定,
自动完成, 调用提示, 上下文敏感编辑器,
跳至定义, 使用定位, 重构....
以及版本控制/单元测试/内置搜索/项目管理.

(`是也乎:`
很久没有听到这位的消息了.
)


- [flask 的先进理念](http://www.syncano.com/advanced-concepts-flask/)
    - flask

A lot of the concepts we mention in this article can be found in Armin Ronacher's presentation on advanced Flask patterns. Mr.Ronacher did great job enumerating the concepts. Advanced Flask concepts are used to build applications that scale, so let's talk a little bit about what scaling an application means.

(`是也乎:`
参考 [HOA.9 LitePyCon | GDG Livin ZhuHai Life;-)](http://blog.zhgdg.org/2014-08/et-hoa9-summary/)  赖总 "python web dev 的困惑与突破" 
就是分享的这方面的成果呢.
不应该拼框架,
而应该是一个可以产生次级市场的杀手级运行环境.
)

- [Python & Memoization](http://www.python-course.eu/python3_memoization.php)
    - core python

Memoization 可以由程序猿编程实现,
但是,有的编程语言,比如 Python 就任性的内置了这种能力!

(`是也乎:`

...细思恐极, 首次知道这一老概念
[Memoization - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Memoization)

简单说就是 沈游侠惯用的技巧,
将髙频使用的函式,干脆将执行态压入数据对象中,
以便不用初始化就能使用.

)

- [你的 Django 故事: 遇见 Magdalena Noffke](http://blog.djangogirls.org/post/109880858623/your-django-story-meet-magdalena-noffke)

Magdalena 是位柏林的 Python web 程序媛,
她对开放数据,数据可视化,
以及公民科技很有兴趣,
在大学里,她就开始使用 Python 了.
所以开发 Web 应用时自然想找个基于 Python 的,
于是选择了 Django.


## 项目
~ 包/模块/库/片段...

- [supporting-python-3](https://github.com/regebro/supporting-python-3)
    - 149 Stars, 7 Fork

又来一个, 指点你怎么转向 Py3 的书.

- [stackit](https://github.com/lukasschwab/stackit)
    - 100 Stars, 4 Fork

智能 Stack Overflow 问题查询
的 CLI 工具!

(`是也乎:`
![stackit](https://camo.githubusercontent.com/ed0b4a52cad6a555e8088ae12d964e7d9947e8e8/687474703a2f2f692e67697068792e636f6d2f33726758424132716f416177483662416a4b2e676966)

程序猿只要 CLIL.
)


- [overloading.py](https://github.com/bintoro/overloading.py)
    - 8 Stars, 0 Fork

在 Py3 中对函式进行重载.


- [muffin](https://github.com/klen/muffin)
    - 5 Stars, 0 Fork

Muffin -- 基于 Asyncio 协议桟的又一个 web 框架
(`可惜还处于早期状态`)


- [donkey](https://github.com/bcho/donkey)
    - 3 Stars, 0 Fork

cron 样的简洁工具库,
用来定期执行任务.

- [django-tinyschedule](https://github.com/jgeskens/django-tinyschedule)
    - 3 Stars, 0 Fork

用 Django 实现的进行日程管理的小应用



## DAMA
(`大妈私人无责任播报`)

- [像Python专家一样编程: 道地的Python](http://www.ch-linghu.me/article/idiomatic/handout_cn.html)

(`是也乎:`

精译自: [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)

大妈收藏了有4年多了,一直想翻译的,
结果还是给老行者给翻译了,,,
严正推荐!

)


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150206 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150206 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
