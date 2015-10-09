Title: 蠎加载 50
Slug: importpython-50
Date: 2015-10-09 17:17
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 50](http://importpython.com/newsletter/no/50/)

## 该读
~ 文章, Blog, 教程...



- [Python 开发者文章 - 在 Django 和 PostgreSQL 中折腾 JSON (和 MongoDB 对比)](http://www.lexev.org/en/2015/trying-json-combo-django-and-postgresql/)
    + django

全新 JSONField 将追加到 Django 1.9, 
配合 PostgreSQL >= 9.4 就能爽利的用 JSON 了!


- [Juan Luis Cano: Jupyter (IPython); ipynb 是如何改变科学的 [Video]](https://www.youtube.com/watch?v=rc9uvLgwPRA)
    + ipython

IPython 原本只是作为一个 Python 交互环境在 14 年前折腾出来的.
但是,现在 `ipynb` 已经成为科学家/开发者/甚至于 记者们进行科学探索的首选界面!
现在 Jupyter 项目,作为 IPython 的重构,
对开放科学和科学出版具有更加重要的意义,
视频展示了这方面的精彩!

- ["如何令 Python 协同工作?" 来自 Open Source Bridge 2015 的编码秀视频](http://feedproxy.google.com/~r/emptysquare/~3/1SmYVjTEXwE/)
    + concurrency

在 The Open Source Bridge 大会上发布的视频,
30分钟里, 完成了 Python 3 的异步架构,
完成 非阻塞I/O 和协同程序.


- [DjangoCon 2014- AngularJS + Django = 完美匹配 - YouTube](https://www.youtube.com/watch?t=1876&v=vWJorwEQWLk)

AngularJS 是种强力 MVC 框架,
可以轻易的和 Django 模板结合,
两者梦幻般的配合, 其结果就是一种快速/动态/SPA(单页应用)

(`是也乎:`

细思恐极的是, AngularJS 原本是 Google 内部 20% 任务中诞生的先进框架,
内部被 Polymer PK 掉了,
但是, 墙里开花墙外香, 出了 Google 纯粹在社区折腾下,
反而更加壮美了.
)

- [你的 Django 故事: 遇见 Tapasweni Pathak](http://blog.djangogirls.org/post/130542018183)

Tapasweni Pathak 是 SAP 实验室的软件工程师.
同时也是 Systers 组织的 GSOC 导师.
她为促进 Linux 内核作了很多有益的工作.
当然是位 自由和开源软件爱好者.
习惯在 Quora 分享.
热爱 C 和 Python , 进行操作系统和编译方面的工作.
过去, 一直在 Qualcomm 公司担任 Outreachy Linux 内核见习工程师,
还在 Delhi 的 I.I.T 作过研究员.


- [用 Gabbi 和 Hypothesis 测试 Django APIs | Wildfish](http://wildfish.com/blog/2015/10/01/using-gabbi-and-hypothesis-test-django-apis/)
    + testing

Hypothesis 是个测试库,
能理解你的 API 说明, 自动尝试多种参数,彻底的探索你的 API.
并努力简化失败后的修复过程,
能保持失败现场, 在 DB 中反复使用,直到解决.


- [今日里程碑: 重构以及迁移 Django](http://slott-softwarearchitect.blogspot.com/2015/10/todays-milestone-refactoring-and-django.html)

Python 之禅认为, Flat 好过 Nested. 
Django, Model, Design. 
这三个词很好的概括了 Django 工程理解.

- [第 25 集 - uWSGI 核心开发者s](http://podcastinit.podbean.com/e/episode-25-uwsgi-core-developers/)
    + podcast

uWSGI 是目前最通用的应用服务器之一.
最初是为 Python 应用开发的,
但是,已经获得了 Perl/Ruby/PHP 等等令人难以置信的功能集.
这集节目中 Tobias 采访了三名核心开发者,
尝试回答为何发展的这么销魂 ;-)

- [Django 开发的最佳实践有什么? - Quora](https://www.quora.com/What-are-some-best-practices-for-Django-development)
    + django

在 Quora 的讨论.

- [PyDev 4.4.0](http://pydev.blogspot.com.br/2015/10/pydev-440-released.html)

新版本已释放,
改进了 included / improved.

- [IPython Notebooks 学 Python](https://github.com/rajathkumarmp/Python-Lectures)
    + python, ipynb

一系列 ipynb 来学习基础的 Python 编程知识.

(`是也乎:`

这是俺收集的第7个类似 ipynb 在线教程了;
看来是个趋势.
)

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



- [Gradience](https://github.com/MasoudH/Gradience)
    - 185 Stars, 0 Fork

跟随圆圈创建 gradience 效果的简单脚本


- [pytest-vw](https://github.com/The-Compiler/pytest-vw)
    - 65 Stars, 2 Fork

VW 令失败的测试案例成功,
以便使 CI 进程完成.
当你的主要目标是快速部署代码到世界各地,
而不关心过程中发生的回归或是新漏洞时.

(`是也乎:` 好任性的工具...)

- [receipt-parser](https://github.com/mre/receipt-parser)
    - 67 Stars, 7 Fork

作家庭帐目时,很麻烦,
你必须手工查找店家名称,核对日期以及所有收据的数目,
得输入,还得计算总合,
为毛不让一台机器来作这些事儿?!


- [ULNNO](https://github.com/yaolubrain/ULNNO)
    - 41 Stars, 9 Fork

无监督学习神经网络输出;
本文提出了一种新的零基础的学习方法,
来自 ImageNet fall2011 上最先进的成果


- [gitim](https://github.com/muhasturk/gitim)
    - 19 Stars, 2 Fork

用一个简单命令, clone 你的所有 github 仓库.

(`是也乎:`

会爆盘的!
)

- [Whiteboard](https://github.com/MasoudH/Whiteboard)
    - 5 Stars, 0 Fork

简单程序, 允许用户快速的在任何地方快速记录笔记.



## DAMA 无责任推荐

![PyCon2015China Slogen](http://pyconcn.qiniucdn.com/zoomquiet/res/logo/2015/150801-cnpycon-slogen.svg)

- [PyCon 2015 China](http://cn.pycon.org/2015/)
    + 北/上/广

主场分享幻灯都已释放! 另外还有纪念 TEE 零售,数量不多,先抢先有 ;-)



# 是也乎

- 151009 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 151009 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
