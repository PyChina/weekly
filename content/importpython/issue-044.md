Title: 蠎加载 44
Slug: importpython-44
Date: 2015-08-28 11:11
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 44](http://importpython.com/newsletter/no/44/)



## 该读
~ 文章, Blog, 教程...


- [俺的  SQLite Python 资源索引](http://charlesleifer.com/blog/my-list-of-python-and-sqlite-resources/)
    + sqlite

索引了作者 blog 中所有相关 SQLite 文章;
以及其它珍奇的 SQLite 相关资源.

(`是也乎:`

charles leifer 是位 SQLite 痴迷者 ;-)
持续贡献了多种基于  SQLite 的神奇东西.以往 周刊都有介绍.
)

- [数据科学和 Pandas;巴尔的摩市工资分析](https://developer.rackspace.com/blog/data-science-baltimore)
    + data science

自从 2008年 McKinney 开始上手以来,
Pandas 已经成为数据科学家最流行最实用的软件组件之一.
通过 IPython/Jupyter notebook 和 Pandas 使用 Python
能令各种数据集的分析简洁/快速.
此文展示了如何基于 data.gov 提供的 巴尔的摩市工资 数据进行分析.

- [数据分析和机械学习项目 Notebook](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/example-data-science-notebook/Example%20Machine%20Learning%20Notebook.ipynb)
    + machine learning

专门为新人创建的 机械学习案例 Notebook.

目标是展示 ML 项目的真实过程.
一起来完善吧

(`是也乎:`

Notebook 已经再次被解构了, 不再指移动电脑,
而是专门指向 ipynb 的 `nb`
但是,真心无法找到一个合心的翻译: 闹书? 折腾本?

看大家是否有创意翻译好.
)

- [10 分钟上手 Tweepy 运行 Twitter Bot](http://scrolltest.com/10-minutes-to-make-our-twitter-bot-with-tweepy-in-python/)
    - twitter

Twitter 是最流行的社交平台,支持用户分享 140 字以内的任意想法并快速传播.
用 Python 可以快速完成一个 Twitter 机械人.
通过 API 获取随机的 Chuck Norris 引用,
每分钟自动张贴到你的 Twitter 上.
详见: 
http://scrolltest.com/10-minutes-to-make-our-twitter-bot-with-tweepy-in-python/#sthash.UeWWjdXT.dpuf

(`是也乎:`

只是呢...在中国 Twitter 已经成功的从人民头脑中净化走了.
)

- [在 Isolation 中测试 Django Views - Matthew Daly's Blog](http://matthewdaly.co.uk/blog/2015/08/02/testing-django-views-in-isolation/)
    + django, testing

可能大家都听说过 TTD 中应该尽可能的隔离外部系统.
但是,总是无法明确具体怎么作?!

当然,在 Django 中的 isolation 能轻易的作到!
对任意对象进行 创建/保存/检查属性.


- [Python 中持续生成文档 (教程和实例)](https://github.com/icgood/continuous-docs/)

基于 github 生态,进行文档的持续集成!

- [你的 Django 故事: 遇见 Michela Ledwidge](http://blog.djangogirls.org/post/127466985198/your-django-story-meet-michela-ledwidge)

Michela Ledwidge 
是位艺术家,在重新导演电影和游戏间的界定.
2004年, 她就获得了 NESTA创新奖 `remixable film` ,
其中包含了她在视觉和数字文化方面的尝试.
她也是 国防部工作室的联合创始人,一直领导多项产品的创新.

- [Jessica McKellar 赢得 2015 Frank Willison Award - Python 软件基金会新闻](http://pyfound.blogspot.com/2015/08/jessica-mckellar-receives-2015-frank.html?m=1)
    + Foundation News

I am extremely happy to report that this year’s Frank Willison Award was presented at OSCON 2015 to Jessica McKellar (see Award Ceremony).

- [用 Python 细分客户](http://blog.yhathq.com/posts/customer-segmentation-using-python.html)
    + machine learning

文章涉及内容其实比较简单.
但非常基础业务: 对客户进行细分.
核心目标是识别不同类型的客户,
进而发现如何找到更多用户的方法,然后就可以...
嗯哼! 获得更多客户!

展示如何分析,使用 K-均值聚类 算法,进行客户细分的探索.


- [如何编写 Django 中间件 | Andrea Grandi](https://www.andreagrandi.it/2015/08/23/how-to-write-a-custom-django-middleware/)
    - django

要理解 Django 中间件的工作原理,
霰记住 Django 的基本架构和由请求和响应构成的.
中间件顾名思义就是停留在中间的组件 ;-)
详细链接中...

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


- [cgt](https://github.com/joschu/cgt)
    - 265 Stars, 13 Fork

计算图形工具包

(`是也乎:`

基于 C++ 后端,可用 CUDA 加速的计算过程图形化分析工具!
)

- [continuous-docs](https://github.com/icgood/continuous-docs)
    - 193 Stars, 7 Fork

前文介绍的文档持续集成示例

- [postgresql-metrics](https://github.com/spotify/postgresql-metrics)
    - 73 Stars, 1 Fork

对 PostgreSQL 数据库提取指标数据.

- [shadowsocks](https://github.com/yabok/shadowsocks)
    - 39 Stars, 105 Fork

嗯哼 **https://github.com/Long-live-shadowsocks/**

(`是也乎:`

LLAP SS !-)

)

- [toproxy](https://github.com/rfyiamcool/toproxy)
    - 16 Stars, 1 Fork

用tornado实现的高性能代理服务器

(`是也乎:`

国人作品!
)


- [what-to-watch](https://github.com/dufferzafar/what-to-watch)
    - 10 Stars, 2 Fork

帮助选择看什么电影的脚本


- [numpy-tutorial](https://github.com/rougier/numpy-tutorial)
    - 9 Stars, 0 Fork

Numpy 新手教程

- [Obfuscate-SSL](https://github.com/Loachy/Obfuscate-SSL)
    - 6 Stars, 1 Fork

通过SSL流量混淆

## DAMA 无责任推荐

# 是也乎

- 150828 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 150828 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
