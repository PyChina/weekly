Title: 蠎加载 35
Slug: importpython-35
Date: 2015-06-12 14:41
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 35](http://importpython.com/newsletter/no/35/)


## 该读
~ 文章, Blog, 教程...

- [RESTful Api哪家强?Flask还是Django](http://www.reddit.com/r/Python/comments/38osar/flask_or_django_for_restful_api/)
    + REST
RESTful Api哪家强?Flask还是Django？Reddit上各路大神讨论中！值得一看！
Discussion on reddit on Flask vs Django for RESTful API. Worthy read to learn about the pros and cons of each.

- [Djangocon: What it’s really like building RESTful APIs with Django - Paul Hallett](http://reinout.vanrees.org/weblog/2015/06/03/09-restful.html)
    + REST
Paul Hallett认为自己是一名“API狂热分子”。他在开发一个卖衣服的网站，叫做lyst。他们现有的API都是通过json-rpc的方式实现的, 他们需要一套更适用于http的API。
Paul Hallett considers himself an “API fanatic”. He works for lyst, a website for buying clothes. They had an existing API, json-rpc, and wanted to have a better API that fitted better with http.

- [PyCharm 4.5: 集成Python Profiler](http://blog.jetbrains.com/pycharm/2015/05/pycharm-4-5-eap-build-141-988-introducing-python-profiler/)
    + pycharm
新版PyCharm的主要的特性是对Python Profiler的集成。你可以很方便的使用一个带颜色的函数调用图形来查看捕获的快照和详细统计信息：
The most notable brand-new feature in this build is the Python Profiler Integration which is available right away from the toolbar or Run | Profile.

- [通过闭包来优化你的Python代码](http://late.am/post/2015/05/07/optimize-python-with-closures.html)
    + core python
Magnetic的实时竞价系统,是用纯Python编写的,经常有很大的并发量。一个普通工作日,我们的应用程序处理高峰时,每秒有300000个请求并需要在10毫秒内完成响应。
Magnetic's real-time bidding system, written in pure Python, needs to keep up with a tremendous volume of incoming requests. On an ordinary weekday, our application handles about 300,000 requests per second at peak volumes, and responds in under 10 milliseconds.

- [Mark Hammond凭获杰出服务奖](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/ZBchouAdipQ/mark-hammond-receives-distinguished.html)
    + PSF
Mark Hammond。在Windows的CPython安装程序中包含了对Mark为2.x系列版本所付出表示感谢的话语,可见他在微软平台对Python支持的工作中极具影响力,。
Mark Hammond. Mark's efforts in supporting the Microsoft platform have been so influential that the CPython Windows installer contained a message thanking him in several versions in the 2.x series of releases.

- [为毛Python中没有Switch/Case?](http://pydanny.com/why-doesnt-python-have-switch-case.html)
不像我们之前学过的其他编程语言，Python中并没有switch或case语句。但为了达到同样的效果，我们使用了字典映射
Unlike every other programming language I've used before, Python does not have a switch or case statement. To get around this fact, we use dictionary mapping.

- [用k-means实现分类和聚类的可视化](http://www.galvanize.com/blog/2015/05/28/classifying-and-visualizing-musical-pitch-with-k-means-clustering/)
    + machine learning
K-means算法是硬聚类算法，是典型的基于原型的目标函数聚类方法的代表，它是数据点到原型的某种距离作为优化的目标函数，利用函数求极值的方法得到迭代运算的调整规则。
k-means clustering is a popular technique for identifying groups of related items in an unlabeled data set. Given any number k, the algorithm will divide a dataset into k groups such that each item’s distance from the center of its group is minimised.

- [使用WSGI服务器实现对请求的监控](http://blog.dscpl.com.au/2015/06/implementing-request-monitoring-within.html)
    + wsgi
在我的上一篇博文我演示了如何使用WSGI中间件来监控web请求,并对数据进行排列分析最终实现可视化。然而更好的方法是WSGI服务器自身实现监控。这是因为放在WSGI服务器实现中,可以避免需要设置WSGI中间件以及WSGI中间件所需的函数包装器的开销。
In my last blog post I showed how a WSGI middleware could be used to monitor aspects of a web request and push metric data out to statsd for collation and eventual visualisation. A better approach would be for such monitoring to be implemented down in the WSGI server itself. This is because by being implemented in the WSGI server, one can avoid the need to setup the WSGI middleware as well as the overhead of the function wrappers required by the WSGI middleware.

- [PyDev of the Week: Stephan Deibel](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/8MNS9eXLEyk/)
    + interview
欢迎本周的PyDev of the Week的嘉宾，Stephan Deibel。他是著名Python IDE,wing的制造商,Wingware的联合创始人之一。
This week we welcome Stephan Deibel as our PyDev of the Week. He is one of the co-founders of Wingware, the makers behind the popular Python IDE, Wing.

- [使用Python和Pygal制作酷炫的图表](http://impythonist.in/create-hacker-dashboards-with-python-and-pygal-with-lesser-effort/)
    + flask
Pygal是类似D3.js的SVG动态图表库。虽然它不如D3.js强大，但是它能为炫酷的图表提供强大的API。我们将介绍如何使用Pygal库创建炫酷的图表。由于示例是使用flask进行演示，所以你需要具备一些flask的相关知识！
Pygal is a python SVG graph plotting library that is similar to D3.js . Even though it is not as powerful as D3.js ,it can deliver beautiful charts driven by API’s behind them. Today we are going to see how to create beautiful charts for any dashboard using a library called Pygal. Here we use flask to see the beautiful dashbaord like gecko board. I assume you have some knowledge of Flask web framework. 


### 工作

-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
急招 N 名有服务端开发经验的 **gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...

- [chainer](https://github.com/pfnet/chainer)
    - 259 Stars, 25 Fork
灵活的神经网络框架
A flexible framework of neural networks

- [drf-chaos](https://github.com/aledista/drf-chaos)
    - 39 Stars, 0 Fork
用于测试Django Rest框架API的装饰器工具集
drf-chaos is a collection of custom decorators for testing Django Rest Framework API under unexpected circumstances

- [WWDCVideosDownloadURLCrawler](https://github.com/cielpy/WWDCVideosDownloadURLCrawler)
    - 26 Stars, 0 Fork
WWDC 2015视频下载工具
a WWDC 2015 session video's download url crawler

- [py-googletrans](https://github.com/ssut/py-googletrans)
    - 16 Stars, 0 Fork
非官方Google翻译的Python接口,免费!
Free Unofficial Google Translate API for Python. Translates totally free of charge.

- [congratsbot](https://github.com/hepwori/congratsbot)
    - 12 Stars, 0 Fork
点赞自动回复的Twitter机器人
A Twitter bot with the mission of congratulating those being congratulated

- [Mastering-Python-for-Finance-source-codes](https://github.com/jamesmawm/Mastering-Python-for-Finance-source-codes)
    - 11 Stars, 1 Fork
<<Mastering Python for Finance>>一书源代码
Accompanying source codes for my book 'Mastering Python for Finance'.

- [rcontrol](https://github.com/parkouss/rcontrol)
    - 10 Stars, 0 Fork
通过ssh实现远端任务异步执行的Python API
python API to execute asynchronous remote tasks with ssh

- [gity](https://github.com/Mnw2212/gity)
    - 9 Stars, 0 Fork
Python的Git模块，内含各种魔法！
The Git magician for Python

- [django-password-validation](https://github.com/orcasgit/django-password-validation)
    - 8 Stars, 2 Fork
对Django 1.9的密码认证系统进行移植，已经支持早期的Django版本　
Backport of Django 1.9's password validation system for use with earlier Django versions.

- [django-maintenance-mode](https://github.com/fabiocaccamo/django-maintenance-mode)
    - 7 Stars, 0 Fork
django-amintenance-mode展示了在使用维护模式(maintenance-mode)时候发生错误而显示的503页面
django-maintenance-mode shows a 503 error page when maintenance-mode is on.

- [wakadump](https://github.com/wakatime/wakadump)
    - 6 Stars, 0 Fork
将WakaTime数据导出文件转换为任意格式的命令行工具
Command line tool for converting WakaTime data dump files into various formats.

- [DjangoConEuropeTranscripts](https://github.com/evildmp/DjangoConEuropeTranscripts)
    - 5 Stars, 4 Fork
DjnagoCon Europe 2015内容整合
Proceedings from DjangoCon Europe 2015

- [mojo](https://github.com/brouberol/mojo)
    - 5 Stars, 0 Fork
当Mozilla网站招聘职位有更新的时候，你将收到相关的邮件通知
Get notified by email when new positions of interest open at Mozilla

- [devrank](https://github.com/yasikstudio/devrank)
    - 5 Stars, 0 Fork
Github上开发者的分级工具
The DeveloperRank is analysis project developer's rank on Github. We are inspired by the PageRank.

- [HiveOpener](https://github.com/miusuncle/HiveOpener)
    - 4 Stars, 0 Fork
快速打开文件或文件夹的Sublime Text3插件
A Sublime Text 3 plugin to quickly open file/directory

- [django-restapi](https://github.com/konglingkai/django-restapi)
    - 3 Stars, 0 Fork
使用django构建RESTFul API
Restful API for django

- [XKCD-Archiver](https://github.com/Flynn58/XKCD-Archiver)
    - 3 Stars, 0 Fork
根据页码自动截取xkcd.com上的漫画
Automatically scrapes xkcd.com for every xkcd, ever. 

## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 1506?? [Zoom.Quiet](http://zoomquiet.io) 完成
- 150612 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
