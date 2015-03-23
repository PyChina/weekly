Title: 蠎加载 24
Slug: importpython-24
Date: 2015-03-14 14:41
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 24](http://importpython.com/newsletter/no/24/)

## 该读
~ 文章, Blog, 教程...

- [功能聚焦: 用 Pycharm 的 intentions 来重构 Py 代码](http://feedproxy.google.com/~r/Pycharm/~3/ywC7fki6avU/)
    + pycharm

PyCharm 的 代码 inspections 和 intentions 最大的不同在:
虽然目标都是改进代码质量,
但是 intentions 是直接动手, 
当然,可能自动修订的都是好的...

(`是也乎:`
细思恐极, PyCharm 也终于走到这一步了,,,,
也上了俺的黑名单了!-)

- [安全及提案发布,Django 家的](https://www.djangoproject.com/weblog/2015/mar/09/security-releases/)
    + django,security release

Django 团队刚刚发布了多个版本 
-- 1.7.6 以及 1.8.b2
可从 PyPI 以及官方下载到.
建议用户尽快升级,
因为包含多处安全相关的增强.



- [Pandas 格式化技巧](http://blog.henryhhammond.com/pandas-formatting-snippets/)
    + pandas

大爱 IPython 和 Pandas,
但是,想输出漂亮的报表总是要折腾一下的,
这里收集了一些常用片段,可以帮忙.


- [不用 Sphinx 组织 Python 文档](http://evennia.blogspot.com/2015/03/documenting-python-without-sphinx.html)

当前,嘦看到 "Python" 以及 "文档" 出现在同一先段落中,
肯定也包含 Sphinx 这个关键词了!
虽然 Sphinx 组织文档很好,
但是....

- [Python 101 半价!](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/yU5oyDUsrKs/)

从三月开始,
如果使用代码: `march15` 将享受半价优惠.
书的目标读者是初级用户,
但是,有 3/2 的内容也是面向中级的.

- [中阶 Python: 描述符](http://intermediatepythonista.com/classes-and-objects-ii-descriptors)
    + core python


Descriptors 是个广泛用在 Python 核心代码,
却显得深奥的概念.
此文很好的总结了,作为一名靠谱的 Python 程序员,
至少应该在自个儿的工具箱中包含的有关技巧.

- [你的 Django 故事: 遇到 Cea Stapleton](http://blog.djangogirls.org/post/113170919528/your-django-story-meet-cea-stapleton)
    + django

Cea 的编程经验起源自私人网站的构建,
以及形式语言的深迷.
哲学有关的经验(语言和形式逻辑特别是哲学)
已经永久性的影响了她的代码.
当前,她在 威斯康星大学麦迪逊分校 攻读 计算机科学硕士,
同时, 应用她的技能,帮忙完善图书馆管理框架.



- [Python 的卡尔曼和贝叶斯过滤器](http://nbviewer.ipython.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb)
    + machine learning

当然的, 使用 IPython notebook 组织的,
还有比这种形式更好的学习渠道嘛!?
可运行的文章!
随时可以修订代码印证理解.

- [Python 中的 Monkey 补丁.](http://blog.dscpl.com.au/2015/03/safely-applying-monkey-patches-in-python.html)
    + core python

Monkey 补丁的用途远不只是问题修复.
虽然常见的使用方式都是描述修订,
并应用模拟库来协助单元测试的运行.
另一个不常见的情况是为现有应用追加仪表盘,
以追加监察功能.


## 项目
~ 包/模块/库/片段...

- [reverse](https://github.com/joelpx/reverse)
    - 166 Stars, 17 Fork

Reverse engineering for x86 binaries (elf-format). Generate a more readable code (pseudo-C) with colored syntax. Warning, the project is still in development, use it at your own risks. This tool try to disassemble one function (by default main). The address of the function, or its symbol, can be passed by argument.

对 x86 二进制逆向工程(ELF格式)
生成具有可读性的代码(伪-C,有彩色语法).
注意! 该项目仍处于早期发展, 用在实际工程中有风险.

- [httpswatch](https://github.com/gutworth/httpswatch)
    - 67 Stars, 21 Fork

HTTPSWatch 专注追踪网站的 HTTPS 支持情况.

- [Nscan](https://github.com/OffensivePython/Nscan)
    - 60 Stars, 16 Fork

Nscan 是受 Masscan 和 ZMAP 启发,构建的高速 互联网扫描和优化工具.
使用自己完成的精简版 TCP/IP 协议.
使用原始套接字发送TCP SYN探测,
但不依赖 SYN Cookies, 
所以,不用等待反馈检验,
这使之比同类工具扫描的要快.

- [white](https://github.com/thomashuang/white)
    - 43 Stars, 2 Fork

Anchor-cms 样的 Blog CMS 系统,
拥有 Anchor-cms 主要功能,
但是,用 Python 完成.


- [slouch](https://github.com/venmo/slouch)
    - 22 Stars, 0 Fork

又一个轻型框架,
专门用来实现 Slack 的命令行扩展.

- [gj2ascii](https://github.com/geowurster/gj2ascii)
    - 16 Stars, 1 Fork

支持在命令界面生成
ASCII 编码的 GeoJSON.

## DAMA
(`大妈私人无责任播报`)


![PyCon Asia-Pacific 2015](http://zoomq.qiniudn.com/CPyUG/PyCon2015China/pycon-apac2015-logo.png)

- [亚太Py大会 6-5~7 在台北举行!](http://pycontw.blogspot.tw/2015/02/pycon-asia-pacific-2015-in-taiwan-save.html)

[PyCon APAC/Taiwan 2015 - Call for Proposals](https://tw.pycon.org/2015apac/en/call-for-proposals/) 议题召集已经释放,想去宝岛体验社区交流的,可以下手了!


## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...



### 回收

- [用 Fabric 在 Ubuntu 上自动部署 Django](http://ilian.io/automated-deployment-with-ubuntu-fabric-and-django/)
    + django,deployment

几个月前,俺只是体验 Fabric 一个简单的脚本来自动化创建一个 Django 项目.
现在,已经变成一个值得推广的全功能栈的 Django 工程部署自动化框架了.


(`是也乎:`
3年前的老文...
经举报,下架 ;-)

# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150315 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150314 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
