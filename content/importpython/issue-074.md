Title: 蠎加载 74
Slug: importpython-74
Date: 2016-05-28 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 74](http://importpython.com/newsletter/no/74/)
- 欢迎, 来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)

## 该读
~ 文章, Blog, 教程...

- [Python 程序猿 2016年调查: 结果](https://www.jetbrains.com/pycharm/python-developers-survey-2016/)
    + community

我们想知道当今 Python 程序猿的真实生存状态,
在调查了 1000+ Python 程序猿后,得到一些有趣的结论,
在此分享大家;

(`是也乎:`

简单的说:独自折腾的少,作为主语言和 JS 总是基在一起,
今年 Py 2 和 3 将战平,
框架中的 IPython/Falsk/numpy等科学计算框架, 在高速追上 Django;
Debug 工具依然没有性能评估工具来的认同多,,,,

嗯哼,当然调查是 JETBRAINS 发起的...
)


- [GitHub - SykoTheKiD/DockerDjangoRest: 有Travis CI 支持的 Django REST 接口 Docker镜像](https://github.com/SykoTheKiD/DockerDjangoRest)
    + docker

A Docker setup for a Django REST API with Travis CI support. Includes Python 2.X and Python 3.X, PostgreSQL, Unicorn ,Nginx, Travis CI Integration.

- [如何在 Ubuntu 16.04 上用 uWSGI+NGINX 发布 Django 应用服务? | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)
    + django

In this guide, we will demonstrate how to install and configure some components on Ubuntu 16.04 to support and serve Django applications. We will configure the uWSGI application container server to interface with our applications. We will then set up Nginx to reverse proxy to uWSGI, giving us access to its security and performance features to serve our apps.

(`是也乎:`

所有 VIP 厂商中 DigitalOcean 的文章总是清晰又专注,
而且可以直接使用.
)

- [Django Channels 作为后台任务](http://albertoconnor.ca/blog/2016/May/18/django-channels-background-tasks)
    + django

This little tutorial is what you need to add a background task processor to Django using channels. Our task for this example will just be outputting "Hello, Channels!", but you could image running a subprocess on some data or sending an email.

- [Python 101: 基准代码简介](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/_d96V9TaUXE/)
    + benchmark

The main idea behind benchmarking or profiling is to figure out how fast your code executes and where the bottlenecks are. The main reason to do this sort of thing is for optimization. You will run into situations where you need your code to run faster because your business needs have changed. When this happens, you will need to figure out what parts of your code are slowing it down. This article will cover how to profile your code.

- [用 jxmlease 在 XML 和自然 Python 数据结构间转换](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/zUML26iWcHM/jxmlease-python-xml-conversion-data-structures)
    + core python, xml

One of the important realizations we made was that Python objects also have metadata. So, we can represent the XML data as normal Python objects, but store the XML metadata as metadata in the resulting Python objects. Using jxmlease, you can easily convert XML data to Python data structures. Here, the 'xml' variable contains the XML document shown in Example 2 (below). You convert it to Python data objects and print it.

(`是也乎:`

嗯哼?! XML,现在还有什么场景一定要 XML 的!?
)

- [Python 插件管理器: Stevedore 和 Pike](http://www.giantflyingsaucer.com/blog/?p=5858)

如果折腾过 OpenStack, 那么一定不得不折腾插件管理器: stevedore;
现在介绍另一个值得折腾的: pike


- [Python 软件基金会新闻: Brett Cannon 赢得 Frank Willison Award](http://pyfound.blogspot.com/2016/05/brett-cannon-wins-frank-willison-award.html)
    + core python

This morning at OSCON, O'Reilly Media gave Brett Cannon the Frank Willison Memorial Award. The award recognises Cannon's contributions to CPython as a core developer and project manager for over a decade.

- [Kel — 用Python 和 Go 构建的基于 Kubernetes 的开源 PaaS](http://www.kelproject.com/)

Kel™ is an open-source Platform as a Service (PaaS) from Eldarion® that makes it easy to manage web application deployment and hosting through the entire software lifecycle. Kel helps DevOps professionals manage their application infrastructure through a layer of tools and components that make Kubernetes accessible and easier to use. Kel builds on Eldarion's 7+ years experience running Gondor, one of the leading Python / Django PaaS solutions.

- [探索美国交通事故数据](http://blog.yhat.com/posts/traffic-fatalities-in-us.html)
    + data science

At a ChiPy event, Nick Bennett gave an excellent talk on traffic fatalities and how he attempts to visualize the publicly available data. The accompanying GitHub repo shows how he accessed and manipulated some of that data with Python tools and then used a couple of different web mapping services to visualize it. The talk prompted some informative comments from the audience and inspired me to further analyze the data myself.

- [bisect — 用 Orderr 保持列表排序](http://feedproxy.google.com/~r/PyMOTW/~3/knL3DA02yVI/)
    + core python

The bisect module implements an algorithm for inserting elements into a list while maintaining the list in sorted order. 



## 活动
~ Upcoming Conference / User Group Meet

- [PyCon Singapore 2016](https://pycon.sg/)
- [GeoPython 2016](http://www.geopython.net/)
- [PyCon Australia 2016](http://2016.pycon-au.org/)
- [PyOhio 2016](http://pyohio.org/)
- [EuroPython 2016](http://ep2016.europython.eu/)


## 项目
~ 包/模块/库/片段...

- [bless](https://github.com/Netflix/bless)
    - 400 Stars, 12 Fork

能以 AWS Lambda 函式运行的 SSH 证书颁发服务


- [fizz-buzz-tensorflow](https://github.com/joelgrus/fizz-buzz-tensorflow)
    - 285 Stars, 16 Fork

fizz buzz in tensorflow

- [Open-Browser](https://github.com/EricsonWillians/Open-Browser)
    - 89 Stars, 22 Fork

开放/精简/高速的浏览器

(`是也乎:`

![EricsonWillians](https://camo.githubusercontent.com/af1c6e66c88ab19b96ed6b76b2106b512d0c1011/687474703a2f2f7333332e706f7374696d672e6f72672f706838337931326f762f6f70656e62726f777365722e706e67)

PyQt 作品...
)


- [pytablewriter](https://github.com/thombashi/pytablewriter)
    - 37 Stars, 2 Fork

专注生成各种格式表格的库,支持:
CSV/HTML/JavaScript/JSON/Markdown/Excel/Pandas/Python/reStructuredText

(`是也乎:`

啊! 表格! 有多少项目因你而崩溃!
)

- [HN-Saved-Links-Export](https://github.com/amjd/HN-Saved-Links-Export) 
    + 36 Stars, 1 Fork

将 [Hacker News](https://news.ycombinator.com/news) 的链接储存为 JSON/CSV 格式数据


## DAMA 无责任推荐

- [Pyston 0.5 released | The Pyston Blog](https://blog.pyston.org/2016/05/25/pyston-0-5-released/)

欢迎订阅 [python-cn(华蟒用户组,CPyUG 邮件列表) - Google 网上论坛](https://groups.google.com/forum/#!forum/python-cn) 和 Pyston 开发者直接沟通,嗯哼 ;-)

- [混乱的 Python Tyrant's Technology](http://t.cn/RUieq1O)
- [Python 模块在全局作用域里应避免任何产生副作用的语句 Tyrant's Technology](http://t.cn/RGxdl9n)


~ 嗯哼, 继续来自自荐的 [御宅暴君](http://acgtyrant.com/) 同学 ;-)




# 是也乎

- 160529 [Zoom.Quiet](http://zoomquiet.io) 92 分钟完成快译
- 160528 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


