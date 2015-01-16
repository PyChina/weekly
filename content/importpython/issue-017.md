Title: 蠎加载 17
Slug: importpython-17
Date: 2015-01-16 17:17
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 17](http://importpython.com/newsletter/no/17/)


## 该读
~ 文章, Blog, 教程...

- [Django 安全发布.](https://www.djangoproject.com/weblog/2015/jan/13/security/)

今天 Django 团队释放出多个版本
-- Django 1.4.16 , 1.6.10, 1.7.3
-- 作为安全版本发布在 PyPI ,以及专用的下载页面.

- [Python 活动日历 - 敬请关注你的 2015 年活动](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/iRT_FYnRNbs/python-events-calendars-please-submit.html)

PSF 目前公布了两种日历:

Python 活动日历 - 包含各种偏重与 Python 以及相关技术的大会和大型活动.

Python 用户组日历 - 包含各种社区成员活动以及其它小型活动.

值得关注!

- [即将发布的 Apache httpd 中有关 mod_wsgi 的解读.](http://blog.dscpl.com.au/2015/01/important-modwsgi-information-about.html)


如果你在 将发布的 Apache httpd 2.4.11 中使用
`mod_wsgi` 4.4.0-4.4.5 版本,
可能引发崩溃,
这里分析了为什么.

- [移植到 Python 3 图书战役](http://www.reddit.com/r/Python/comments/2sed0g/porting_to_python_3_book_campaign/)

我们都爱 Python 3.
`迁移到 Python 3`
第三版,
是本好书,
这有个活动,得到了预览版,
正在招募贡献者来改进,
你,值得掺合!

- [介绍用 matplotlib 作为 ipython notebook 的后端和 FuncAnimation 完成图表动画](http://www.reddit.com/r/Python/comments/2s9203/summary_of_matplotlib_backends_in_ipython/)

在 IPython notebook 中,
以 matplotlib 为后端进行图表展示时,有三种模式:

    简单图表
    FuncAnimation 动画
    交互式 IPython 图表部件



- [用 iPython Notebooks 教授量子化学](http://tmarkovich.com/2015/01/11/teaching-quantum-chemistry-with-ipython/)

我们的学生,
掌握足够的 Python 知识后,
能写出足够复杂的分子式, 
并代入自己有兴趣的问题中, 解释结论.
这真是个伟大的成果!

- [IronPython 2.7.5 发布.](http://feedproxy.google.com/~r/PythonInsider/~3/eb3JkcqpXBQ/ironpython-275-released.html)

IronPython 2.7.5 终于发布了.

- [2015 Python FOSDEM Beer 和 餐厅活动](http://doodle.com/ngdeesgbr6dcx3f5)

"Aperos Python Belgium" 将于1.31 号 星期6 布鲁塞尔 举行.
在 Delirium 咖啡一层,
Impasse De La Fidélité 4, B-1000 Brussels.
如果你是 `FOSDEM` 成员,
可以在  Python devroom (H.1301 房间) 
闪电演讲之后
见到我们.

- [你的 Django 故事: 遇见 Carol Willing](http://blog.djangogirls.org/post/107597215478)
interview

Carol 目前是类似 OpenHatch 的开源项目的的积极贡献者,
也是 PyLadies圣地亚哥 的协办人,
以及硬件和软件的独立开发人.
同时喜爱 编织艺术/音乐/自然与基于Arduino的可携带智能硬件.
她正在主持一个开放硬件项目:
帮助家庭,协同富有同情心的支者,
照顾 阿尔茨海默氏症 患者.

- [所有人的编程课 (Python) - MOOC in Coursera.org](https://www.coursera.org/course/pythonlearn)

Python 的 Coursera 课程.

- [Python 曲径通幽.](http://www.reddit.com/r/Python/comments/2sbs39/the_winding_path_toward_python_proficiency/)

对于初学者,
好象有很多道路来学习,
有的通过大学课程,
有的通过参加训练营,
有的死看书.
但是,通常都迷失在其中,丧失耐心.
这里给出相对合理的,可实现的学习路径图来.


- [实效 TDD: 加速 Django 测试 (提速10倍!)](http://www.daveoncode.com/2013/09/23/effective-tdd-tricks-to-speed-up-django-tests-up-to-10x-faster/)

此文作者分享的各种技术,能令 Django 测试运行变得非常快!
(有个测试案例包含250个用例,~5秒跑完, 而不是以往的 50 秒,即加速了10倍!-)


- [用 DataTables 向你的 Django 应用中追加响应式表格(非卷动).](https://www.calazan.com/adding-responsive-tables-no-scrollbars-to-your-django-app-with-datatables/#.VLXnvK3oNSc.reddit)

DataTables 是个 jQuery 表格插件,
有很多特性.
将之用在 Django 应用中(GlucoseTracker),
很不错,
但是,对于手机浏览时,很难受,
所以,作者将之 响应化了.

- [Django Girl 教程](http://djangogirls.gitbooks.io/djangogirls-tutorial/)


此书是有关如何开展一次 `Django Grils` 活动的教程.
男子汉们应该看看.


- [(信息图) 应该先学哪种语言. Python 正好是最值得的一个.](http://cdn2.carlcheo.com/wp-content/uploads/2014/12/which-programming-language-should-i-learn-first-infographic.png)

Infographics PNG.

- [如何基于 Pelican 发布 blog - 深入教程](http://nafiulis.me/making-a-static-blog-with-pelican.html)

Pelican 支持你生成静态 blog.
作为静态网站,
所有页面是用 blog 生成器生成的.
这意味着你得将整个网站上传到服务器.

- [加速 `pip install`](http://www.reddit.com/r/Python/comments/2s9qit/speedup_pip_install/)


为 Windows 开发者能用 pip


## 项目
~ 包/模块/库/片段...

- [joe](https://github.com/karan/joe)
    - 146 Stars, 6 Fork


`.gitignore` 的 CLI 工具,
为你的情况自动生成神奇的 `.gitignore`.

- [ZeroNet](https://github.com/HelloZeroNet/ZeroNet)
    - 112 Stars, 12 Fork

使用 Bitcoin crypto 和 BitTorrent 网络
进行分布式 web 网站发布.

(`是也乎:`
![ZeroNet](https://camo.githubusercontent.com/6bfe0288417433decc2c126bfa21c64b7ae53fb3/687474703a2f2f692e696d6775722e636f6d2f51615a6855436b2e706e67)

这是不再需要 DNS 发布网站的节奏哪,,,

)

- [KeyboardCAD](https://github.com/nstamplecoskie/KeyboardCAD)
    - 12 Stars, 0 Fork

专门用来生成 FreeCAD 文件,进行键盘定制的工具,

http://www.keyboard-layout-editor.com/

可以根据此文件制造任意键盘

- [solo](https://github.com/thomashuang/solo)
    - 15 Stars, 2 Fork

基于 Gevent & Webob & Routes 的又一个 web 框架

(`是也乎:`
国货!
![avatars0](https://avatars0.githubusercontent.com/u/1823391?v=3&s=460)

同时也有同名的国货:

- [kuangyh/solo](https://github.com/kuangyh/solo)
)

- [dbpy](https://github.com/thomashuang/dbpy)
    - 11 Stars, 1 Fork

灵感来自 webpy 和 drupal,
通用数据库抽象层,
可以良好和配合 tornado 或 其它 web 框架,
值得体验!

(`是也乎:`

国货, 推荐二连发!
刚刚在 CPyUG 列表中释放,
就翻译为 E 文被推荐了!
事实反复教育我们,
想让更多的靠谱程序猿来用自个儿的作品,
给 E 文文档吧!
)

- [vat_moss-python](https://github.com/wbond/vat_moss-python)
    - 10 Stars, 0 Fork


挪威增值税数字服务处理
的 Python 版本支持库,
支持进行 VAT MOSS 的核算,
给出税号,就完成自动化汇率/发票税率, 以及货币的计算

- [iOS-Python-Project](https://github.com/clowwindy/iOS-Python-Project)
    - 9 Stars, 0 Fork

用 Python 开发 iOS 应用的实例.

(`是也乎:`
作者是 SS 团队成员,
目测也是天朝人...)

- [unix2web](https://github.com/edouardklein/unix2web)
    - 9 Stars, 1 Fork

在 web 页面上进行各种 UNIX 的过滤操作,
比如,从 .doc 生成 .pdf

- [pandoc-opml](https://github.com/edavis/pandoc-opml)
    - 4 Stars, 0 Fork

pandoc-opml 
能基于 pandoc
从 Markdown 中生成 OPML


## 曰了
~ Tweets


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150116 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150116 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
