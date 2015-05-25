Title: 蠎加载 33
Slug: importpython-33
Date: 2015-05-22 22:22
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 33](http://importpython.com/newsletter/no/33/)

## 该读
~ 文章, Blog, 教程...


- [PyCharm 4.5: 集中提供所有 Py 工具](https://www.jetbrains.com/pycharm/whatsnew/?rss)

PyCharm 4.5 包含更多生产力工具,
特别是和 Django 一起工作时...


- [PyCon Sweden 2015](http://ilian.io/pycon-sweden-2015/)
    + pycon

对 PyCon 瑞典的感受? 就一个字: `真棒` !
这是笔者首次参加的 PyCon,
真心希望还有下一次,
能和各种伟大的人物在一些讨论把村/宇宙和一切,感觉不能更加好了!

- [Django 最新 Postgres 功能之趣 - Real Python](https://realpython.com/blog/python/fun-with-djangos-new-postgres-features/)
    + postgres

本文介绍了 Django 1.8 针对 Postgres 发布的最新功能:
ModelFields,
包含 ArrayField, HStoreField, 以及 Range Fields 特性.



- [Celery 和 Flask 应用的工厂模式](http://blog.miguelgrinberg.com/post/celery-and-the-flask-application-factory-pattern)
    + flask

总是有读者询问如何在 Flask 应用中,
利用工厂模式,包含进来更多的特性.

Celery 一向很难被包含到现行框架中,
因为有个延迟访问的问题,
直到 工厂模式 的引入.

- [有兴趣来组织 DjangoCon 欧洲 2016?](https://www.djangoproject.com/weblog/2015/may/18/interested-organizing-djangocon-europe-2016/)
    + django

DjangoCon Europe 2015 
再几周就要举行了,
但是,我们已经开始筹备明年的了!
每次筹委会都是志愿者组成的,所以,你也有机会!


- [有关 IPython 的生存分析 : R vs. Python](https://plot.ly/ipython-notebooks/survival-analysis-r-vs-python/)
    + ipython

在此 notebook 中, 
尝试对比 R 和 Python,
作为开发语言,以及图形化平台等等方面,进行了深入分析.


- [有关利用 Grok Learning 进行 Py 教学的广播](http://www.talkpythontome.com/episodes/show/8/teaching-python-at-grok-learning-and-classrooms)
    + podcast

澳大利亚 已经要求高中学生必须掌握一种编程语言了?!

Dr. James Curran 正在构建一个 Grok Learning 平台,
以及辅助教程,让学生们轻松的完成学习.



- [Opbeat 谈论 Lincoln Loop](https://twitter.com/opbeat/status/598174804349308928/photo/1)
    + performance

来自 Pycon 蒙特利尔的视频.

Peter Baumgartner (@ipmb) Lincoln Loop 创始人,
谈论堆桟技术,
以及3 种优化 Django 应用的技巧.


- [用 pandas/notebook 来分析俺住过的地方气候](https://blog.wearewizards.io/comparing-the-weather-of-places-ive-lived-in)
    + ipython


俺住过3大洲4个国家,
每当人们问及时,能想起来的总是天气,
那么如何简洁的对比这些地方的气候呢?

嗯啍!? 还有什么比在 notebook 上 用 pandas 快速可视化表述更加方便的呢?


- [解析 C, 类型声明以及 fake headers](http://eli.thegreenplace.net/2015/on-parsing-c-type-declarations-and-fake-headers/)
    + core python

pycparser 过去几年间已经流行起来了(特别是配合 cffi 使用).
就也意味着作者越来越多的收集各种邮件发送过来的提问.

所以,这里提供了一篇最全面的 FAQ 集锦,你值得拥有!



- [用线程(Py的)列表文件来处理 OS 命令的超时](http://code.activestate.com/recipes/579056-run-os-command-with-timeout-on-a-list-of-files-usi/)
    + core python

通过两个并行的线程文件,
当其中一个超时时,程序进入下一个,
并能编辑/追加异常处置.

- [Python coroutines 和异步以及等待](http://lwn.net/SubscriberLink/643786/9c0bd83dff0df3b8/)
    + core python

Python 已经能创建 coroutines 来异步处理.
只是还没有提升到语言层面,
只是个类型生成器.

现在提议追加两个关键词: async 以及 await,
彻底解决这事儿!


(`是也乎:`
细思恐极的是, Guido 老爹一直也是 golang-style 哪,
内置库可以自在点,但是,关键字,那是真心越少越好.
所以,....
)

- [当周 PyDev: Vasudev Ram](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/KRxZ8XxqVgM/)
    + interview

Vasudev Ram (@vasudevram) 作为当周 PyDev 之星,
一直在 blog 中坚把分享各种技术内容,
也是 xtopdf 的创始人.

## New Books


## 项目
~ 包/模块/库/片段...

- [slack-overflow](https://github.com/karan/slack-overflow)
    - 342 Stars, 12 Fork

程序猿最好的朋友!?现在是 Slack.

- [dnsdiff](https://github.com/joshenders/dnsdiff)
    - 199 Stars, 6 Fork

对 DNS 进行 diff.

- [pynab](https://github.com/aldanor/pynab)
    - 32 Stars, 0 Fork

对 YNAB 数据进行访问的简约 Py 库.


- [wepy](https://github.com/DeliangFan/wepy)
    - 16 Stars, 4 Fork

天气查询客户端, CLI 的


- [hn](https://github.com/walkr/hn)
    - 11 Stars, 1 Fork

在命令行中阅读 HN 

- [embedding-matching-word-segmenter](https://github.com/Jianqiang/embedding-matching-word-segmenter)
    - 9 Stars, 3 Fork

来自讨文 ACL-2015 的代码: "Accurate Linear-Time Chinese Word Segmentation via Embedding Matching"

- [badactors](https://github.com/jgamblin/badactors)
    - 8 Stars, 1 Fork

建立公共 IP 黑名单



- [simplesam](https://github.com/mdshw5/simplesam)
    - 8 Stars, 0 Fork

简单的纯 SAM 解析器,以及记录对象


- [marker](https://github.com/pindexis/marker)
    - 8 Stars, 1 Fork

终端里的书签


- [oi](https://github.com/walkr/oi)
    - 8 Stars, 0 Fork

有 CLI 界面的,可长期运行的应用进程编辑框架


(`是也乎:`

这个可以!
)

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

- 150525 [Zoom.Quiet](http://zoomquiet.io) 完成
- 150522 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

