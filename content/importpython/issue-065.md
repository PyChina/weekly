Title: 蠎加载 65
Slug: importpython-65
Date: 2016-03-24 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 65](http://importpython.com/newsletter/no/65/)

## 该读
~ 文章, Blog, 教程...



- [用 Python 巡查目标 Twitter 行为](http://kldavenport.com/examining-your-presence-on-twitter-with-python/)
    + data science


文档展示了 赞助/营销 经理如何追踪他们的运动员或是品牌大使.
虽然写这种代码无法获得地区营销大奖.(嗯哼)

只是希望文章引导那些想合理对 Twitter 数据进行追踪挖掘的同学们,
不用迷失在各种 R/Py 的模块大洋中...


- [Startup Row: UtilityAPI 赢得了 SF Python pitch event](http://pycon.blogspot.com/2016/03/startup-row-utilityapi-won-sf-python.html)
    + startup

PyCon 2016’s Startup Row got our campaign on the road on March 9th in San Francisco, meeting with the local SF Python user group at Yelp headquarters. Six early-stage companies that use Python gave their pitches, competing for an opportunity to exhibit in the PyCon Expo Hall on Startup Row. The roster of candidate startups included Alpaca, Bauxy, Beansprock, Opsulutely, Watt Time, and UtilityAPI.

- [Python 3 使用 Google Cloud Vision API 提取照片中文字实例](https://gist.github.com/dannguyen/a0b69c84ebc00c54c94d)

快速用 Python 3 进行测试
(通过 Requests)
Google Cloud Vision 是否能良好的完成 OCR 数据处理.
对比类似 ABBYY FineReader 
能输出 Excel 表格.

- [你的 Django 故事: 遇见 Sarah Holderness](http://blog.djangogirls.org/post/141433577888)
    + djangogirls

Sarah Holderness is the Python instructor at Code School. Although she originally planned to be a high school math teacher, Holderness found her love of programming during a required programming class in college and has been hooked on creating things ever since.

- [Django 权限管理](http://kracekumar.com/post/141377389440)
    + django

Admin 仪表板一向是 Django .
能支持用户对数据对象进行自由的 创建/读取/更新/删除.
对数据库的全面掌控!
但是新手总是无法从界面中获得数据.
其实,嘦完成合理的数据注册,一切尽在眼前...

- [Django 迁移和冲突管理](https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/)
    + django

迁移也是 Django 的常用功能之一...
(`是也乎:` 因为经常不兼容升级嘛?!)
对多数人而言, 这是一个可怕的任务.
尽管阅读了所有文档,依然害怕迁移冲突引发的数据丢失,
或是手工修改迁移文件等等.
其实, 迁移工具很赞的, 嘦理解了她,
就没有任何挂碍的了.

- [qutebrowser 集资活动 ~ Python 开发的绑定 Vim 快捷键开源浏览器](https://www.indiegogo.com/projects/qutebrowser-a-keyboard-focused-vim-like-browser#/)

qutebrowser 是拥有宏大社区异常活跃的项目:

超过60人贡献超过250次变更(Pull-Rewuests),
数百积极用户.
在过去5年积累了超过7500次提交.
目前核心任务是优化 QtWebKit 渲染引擎.
通过活动期望能全职为之工作一个月(或更多时间).
目标是增加最新基于 Chromium 项目的 QtWebEngine 后端!

(Google Chrome 使用相同引擎.)

(`是也乎:`

![cheatsheet-big](http://qutebrowser.org/img/cheatsheet-big.png)

程序猿永远的野望! 用键盘控制一切...
浏览器一直没有攻陷...所以 Pythoneer 来也...
基于 Py3+Qt5 !
)

- [Python 反思: 如何列出模块以及检查函式s](http://tomassetti.me/python-reflection-how-to-list-modules-and-inspect-functions/)
    + core python

最近在折腾 Python 代码静态分析,
以及如何在 Jetbrains MPS 上创建 Python 编辑器.
首先得完成 Python 代码的模型解析.
虽然代码已可解析,问题是要考虑所有引用的包代码.
有的是内建的,有的是通过 C 编译出来的.
这意识着根本没有 Python 代码来解析.
文章记述了这方面的折腾...

(`是也乎:`

**MPS** ~ Meta Programming System !
Jetbrains 折腾出来了太多优秀的开发语言 IDE,
但是,发现 DSL 语言的创建越来越频繁,
所以,干脆给出了个通用的 DSL 语言构建系统!
嗯哼, 虽然已经有了 PyCharm, 但是用 MPS 再折腾出一个自制版本的来也没有为什么...

)


- [可插入式 Py 生成器 (Python)](http://code.activestate.com/recipes/580628-pluggable-python-generators/)
    + core python

简单的示例,
展示了 生成器 也是可插入的,
即,能作为参数传送给 函式来从内部使用!


- [实时 Django & Django Channels](http://djangolinks.com/detail/real-time-django-django-channels-488)
    + django

今天是 Jacob Kaplan-Moss 的分享.
Jacob 来自 Herokai ,长期为 Django 贡献核心代码.
他认为框架的未来在于 Channels!
为 Django 引入了全新概念.
Channels 本质上是任务队列:
消息由生产者压入,
然后消费者能从指定 Channels 中获得.
如果在 Go 中使用过 `channel`, 就非常熟悉这种思路.
和 golang 的 `channel` 主要区别在,
Django 的 Channels 主要通过网络进行,
允许生产者和消费者在很多 dynos 以及/或 机器上透明运行.
此网络称为 `channel layer`

(`是也乎:`

嗯哼?! Django 在走 node.js 的老路?
将同步代码,变成异步执行?
还跨网络/主机!?
那这安全性就呵呵了...而且调试起来简直无法更加酸爽了 !
)

- [datetime — 日期和时间值操作 — PyMOTW 3](http://feeds.doughellmann.com/~r/DougHellmann/~3/Ny2-7gE3JX8/)
    + core python

datetime 模块包含各种日期/时间的处理/格式化/计算 的函式和类.
是的, `PyMOTW` ~ 每周一模块 系列在升级到 Py3 ;-) 


- [Scrapy Tips from the Pros: March 2016 Edition](https://blog.scrapinghub.com/2016/03/23/scrapy-tips-from-the-pros-march-2016-edition/)

scrapy 的用户,应该关注最新的技巧集

- [Python 201: 中级 Python](https://www.kickstarter.com/projects/34257246/python-201-intermediate-python)

如果已经有 Python 的基础知识.
想提升到新水平,
那么这书正是你需要的...
当前唯一的 中级 Python 图书!

Kickstarter 中...

(`是也乎:`

目标 10万$,已经 KS 到了 7万多,
只是男主太丑...
)

## 新书
~ New Books

- 爱上Python ([Learn Python in One Day and Learn It Well](http://www.amazon.cn/Learn-Python-in-One-Day-and-Learn-It-Well-Python-for-Beginners-With-Hands-on-Project-The-Only-Book-You-Need-to-Start-Coding-in-Python-Immediately-Chan-Jamie/dp/1506094384/ref=sr_1_1?ie=UTF8&qid=1457804766&sr=8-1&keywords=Learn+python+in+one+day))

高分入门小书, 程序媛 写就 !-) 已经完成翻译,出版中,值得期待!

## 项目
~ 包/模块/库/片段...


- [variational-text-tensorflow](https://github.com/carpedm20/variational-text-tensorflow)
    - 223 Stars, 15 Fork

TensorFlow 实现
Neural Variational Inference 
的文本处理!

(`是也乎:`

![variational](https://github.com/carpedm20/variational-text-tensorflow/raw/master/assets/model.png)

不知道能处理 红楼 卟!?

)

- [quantum](https://github.com/karldray/quantum)
     - 203 Stars, 5 Fork

利用 quantum suicide 进行反向因果分析


- [try](https://github.com/timofurrer/try)
    - 125 Stars, 5 Fork

非常赞的 Python 模块尝试 CLI 工具...


- [datedelta](https://github.com/aaugustin/datedelta)
    - 44 Stars, 3 Fork

类似 datetime.timedelta, 折腾日期计算 `for Humans™`

(`是也乎:`


    >>> datetime.date(2016, 3, 23) - datedelta.datedelta(years=-1, months=-1, days=1)
    datetime.date(2017, 4, 22)

    >>> datetime.date(2020, 2, 29) - datedelta.datedelta(years=2)
    datetime.date(2018, 3, 1)


嗯哼,说人话的日期计算模块...收!

)

- [SwiftKitten](https://github.com/johncsnyder/SwiftKitten)
    - 34 Stars, 1 Fork

Swift autocompleter for Sublime Text, via the adorable SourceKitten framework

- [channels-examples](https://github.com/andrewgodwin/channels-examples)
    - 29 Stars, 1 Fork

使用 Django Channels 的示例工程

- [CNN-for-Sentence-Classification-in-Keras](https://github.com/alexander-rakhlin/CNN-for-Sentence-Classification-in-Keras)
    - 10 Stars, 4 Fork

在Keras中
用
卷积神经网络(Convolutional Neural Networks)
折腾 句子分类


- [DigitalOceanFlask](https://github.com/jabbalaci/DigitalOceanFlask)
    - 7 Stars, 0 Fork

将 Flask webapp 安装到  Digital Ocean (or Linode, etc.) Ubuntu box

- [Selective-Unhide](https://github.com/RayMairlot/Selective-Unhide)
    - 6 Stars, 1 Fork

Replaces the default unhide operator in blender with a menu, allowing selective unhiding.

- [hashtag-scraper](https://github.com/tampe125/hashtag-scraper)
    - 4 Stars, 1 Fork

从 Twitter 抓取 `long hashtags` 
用作口令

- [checkdns](https://github.com/felipebhz/checkdns)
    - 4 Stars, 0 Fork

Python 完成的 DNS 检验工具.

## DAMA 无责任推荐

- [10个最好用的 Python 工具/插件/库 - Livecoding.tv Blog](http://blog.livecoding.tv/2016/03/24/the-ten-10-best-python-productivity-tools-plugins-and-libraries)
    + 以及同类最10好的 C/C++/C#/JAVA/JS/Angular/H5 推荐....
    + 当然,都是 Livecoding.tv 一家之言...没有 github 的统计精确哈...

### 工作

....


# 是也乎

- 160325 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160324 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


