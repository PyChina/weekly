Title: 蠎加载 46
Slug: importpython-46
Date: 2015-09-12 18:18
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 46](http://importpython.com/newsletter/no/46/)


## 该读
~ 文章, Blog, 教程...


- [D3.js 和 .ipynb 的五大互动](http://blog.plot.ly/post/128662310992/analyze-data-five-ways-you-can-make-interactive)


Plotly 全新的地图制作工具,
赋予地理数据故事的讲述能力.
文章展示了如何在 等高线/子图/散点/气泡/线图 五种情景中使用风格;
而且,同时支持 R 和 Py 的接口...


- [为 Serpy 放弃 Django REST Framework Serializers  · BetterWorks Engineering Blog](https://engineering.betterworks.com/2015/09/04/ditching-django-rest-framework-serializers-for-serpy/)

故事回顾了为什么放弃 Django REST Framework Serializers,
却能在兼容所有接口同时提升性能!

- [PyData NYC 2015 议题征集](http://nyc2015.pydata.org/cfp/)
    + conference

PyData纽约2015 大会已经开放了主题提交,
汇集 分析师/科学家/开发者/工程师/建筑师 等等
从数据科学角度进行 数据管理/分析/可视化 的技术和工具交流.


- [你的 Django Story: 遇见 Lucie Daeye](http://blog.djangogirls.org/post/128559723068)
    + django

Lucie 的博士是进行地理研究,
在韩国的 EHESS 继续进行研究.
刚刚决定改变职业发展.
她组织了  DjangoGirls 巴黎,四月又推出了 PyLadies 巴黎.

去年在 Europython 中参与了 DjangoGirls 活动,
被感召,立即成为了 Bilbao 的 Django Girls 工作坊教练.

她在 DjangoDoc 欧洲 分享过 Django 的社会化工程, 
2015 她成为 DjangoGirls 的魅力大使.

![Lucie Daeye](http://36.media.tumblr.com/4552acfca8c5d1302a602509a6dad230/tumblr_inline_nrfk9ksKZl1sescfp_500.png)


- [PyParallel 实验: 多核 Python 解决方案之一](https://github.com/pyparallel/pyparallel)

PyParallel 处于概念验证期,
使用 Python 3.3.5 分支,
旨在针对现代硬件优化:
多 CPU ,SSD 硬盘, NUMA 架构和高速 I/O 通道
(万兆以太/Thunderbolt 等等).
核心亮点在, 无需实际删除 GIL .


- [PyScaffold - 轻松完成 Python 项目部署的幸福](http://peter-hoffmann.com/2015/pyscaffold-easy-setup-of-a-python-project-with-a-bliss.html)

配置好 Python 项目的过程,
对于初学者, 创建包目录树,测试文档结构,生成 `__init__.py`
等等是绝对枯燥/繁琐/重复 又易错!
而 PyScaffold 正好解决了所有问题.

- [PEP-498 获准!](https://www.python.org/dev/peps/pep-0498/)
    + core python

Python 支持多种方式来格式化文本字串.
包含
`%-formatting` , `str.format()` , 以及 `string.Template` . 
每种都有其优点,以及问题,
以至实践中都无法真正解决问题.

刚刚准备的 PEP 建议增加一个全新的字符串格式化机制:
文本插值 (Literal String Interpolation).

- [Python 实现 NSA 的 Simon & Speck 分组密码](http://git.io/vZWZi)

纯 Python 实现的
Simon and Speck block ciphers!
由美国国家安全局在限制性硬件环境中使用为目标设计的,
例如 微型控制器,或是 小型 ASICs/FPGAs.


- [令 Django 真真的安全](http://nerd.kelseyinnis.com/blog/2015/09/08/making-django-really-really-ridiculously-secure/)

DjangoCon 2015 上演讲涉及的资源.


- [Django Slingshot - Home](http://www.djangoslingshot.com/)
    + django

Slingshot 是一套工具 ,
用来帮助大家更快/简单的掌握 Django


- [节目 22 - Bryan Van de Ven on Bokeh](http://podcastinit.podbean.com/e/episode-22-bryan-van-de-ven-on-bokeh/)
    + podcast

Bryan Van de Ven 
是来自 Bokeh 的项目管理器,
通过图表以及可视化工具,
帮助开发者轻松的创建有吸引力的界面.
文章说明了项目历史,
以及有趣的实用案例,以及近期进展.


- [PyPy warmup 增强](http://feedproxy.google.com/~r/PyPyStatusBlog/~3/Gb67J00bbNM/pypy-warmup-improvements.html)

整体上达到了 50% 的提速!
降低了 10~30% 的启动预热.
预热 时间和内存有望进一步得了也得.


- [神经网络的快速编程](http://andrew.gibiansky.com/blog/machine-learning/coding-intro-to-nns/)
    + machine learning

此教程中, 使用 Python 的 numpy 和 Theano
来体验 机构计算.
通过相关库的简要介绍,
然后快速编码对当前数据属性进行训练
用 神经网络 实现  Logistic 回归.



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

- [robinhood](https://github.com/benkroop/robinhood)
    - 139 Stars, 14 Fork

通过 Robinhood 接口的操作,
完成免佣金自动化股票交易.

- [twittor](https://github.com/PaulSec/twittor)
    - 64 Stars, 10 Fork

Twitter 全功能后门 C&C 服务.

- [hillary-clinton-emails](https://github.com/benhamner/hillary-clinton-emails)
    - 60 Stars, 6 Fork

用代码将
Hillary 的邮件从 PDF 原案转化为 SQLite 数据库


- [minimal-docker-python-setup](https://github.com/OrangeTux/minimal-docker-python-setup)
    - 32 Stars, 2 Fork

最小的 Nginx-uWSGI-Flask-Redis 
工作桟 Docker 镜像,
仅仅 42 mb.


(`是也乎:`

[Demo of Nginx-uWSGI-Flask-Redis stack. - asciinema](https://asciinema.org/a/26061)
)

- [Album-Splitter](https://github.com/crisbal/Album-Splitter)
    - 16 Stars, 1 Fork

支持从 YouTube 下载,
将单 MP3 文件分解为专辑.


- [because-moe](https://github.com/mczub/because-moe)
    - 13 Stars, 2 Fork

动漫流媒体搜索引擎

anime streaming search engine

- [ped](https://github.com/sloria/ped)
    - 13 Stars, 1 Fork

从命令行打开 Python 模块

- [password_scrambler](https://github.com/hasherezade/password_scrambler)
    - 12 Stars, 4 Fork

Password scrambler - 
命令行上的 `1Password` ,
更加轻松的进行复杂口令的管理!

- [snaql](https://github.com/semirook/snaql)
    - 10 Stars, 1 Fork

在 Python 中无痛使用原始 SQL


(`是也乎:`

Python 行文中 SQL 的 DSL :

    {% sql 'users_by_country', note='counts users' %}
        SELECT count(*) AS count
        FROM user
        WHERE country_code = ?
    {% endsql %}


嗯哼,好象哪里有不对的...

)

## DAMA 无责任推荐

# 是也乎

- 150912 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 150912 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
