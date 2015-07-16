Title: 蠎加载 38
Slug: importpython-38
Date: 2015-07-03 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 38](http://importpython.com/newsletter/no/38/)


**翻译ing...**

## 该读
~ 文章, Blog, 教程...

- [Build a better batching UI with Morepath and Jinja2](http://blog.startifact.com/posts/morepath-batching-example.html)
    - web framework
Morepath is a Python web micro framework with some very interesting capabilities. What we'll look at today is what you can do with Morepath's link generation in a server-driven web application. While Morepath is an excellent fit to create REST APIs, it also works well server applications. So let's look at how Morepath can help you to create a batching UI.

- [pip -t: A simple and transparent alternative to virtualenv](http://blog.zoomeranalytics.com/pip-install-t/)
    - pip
Often, virtualenv is overkill for the basic task of installing project dependencies and keeping them isolated. We present a simple alternative.

- [Proxying to a Python web application running in Docker.](http://blog.dscpl.com.au/2015/06/proxying-to-python-web-application.html)
    - docker
I have seen a few questions of late being posed about how to setup Apache to proxy to a Python web application running in a Docker container. The questions seem to be the result of people who have in the past previously run Apache/mod_wsgi on the host, with potentially multiple Python web applications, now making use of Docker to break out the individual web applications into separate containers.

- [Python 101: Episode #7 – Exception Handling](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/V8q86BPZaOs/)
    - core python, video
I recently recorded the next episode of Python 101. This one is on Exception Handling. I hope you like it.

- [Testing Django applications using Hypothesis](https://skillsmatter.com/skillscasts/6475-testing-django-applications-using-hypothesis)
    - django, testing
David MacIver will be discussing testing Django applications using Hypothesis.

- [Installing a custom Python version into a Docker image.](http://blog.dscpl.com.au/2015/06/installing-custom-python-version-into.html)
    - core python
It is a growing problem with Linux distributions that many packages they ship quickly become out of date, and due to the policies of how the Linux distributions are managed, the packages do not get updates. The only hope for getting a newer version of a package is to wait for the next version of the Linux distribution and hope that they include the version of the package you do want.

- [Your Django Story: Meet Iulia Chiriac](http://blog.djangogirls.org/post/122760203063)
Iulia is a full-stack web developer and open-source enthusiast. She’s been working with Python for the last three years (and loving every minute of it), but before that she tried a series of other languages and technologies, including C/C++, C#, PHP and Java. Iulia currently work as a web developer for the Romanian company Eau de Web (http://www.eaudeweb.ro), based in Bucharest.

- [Django Security advisory: simple_tag does not do auto-escaping](https://www.djangoproject.com/weblog/2015/jun/29/simple_tag-security-advisory/)
    - django
As per our documentation, the simple_tag decorator used for creating custom template tags does not run auto-escaping on its contents (up to and including Django 1.8). The team has noticed, however, that this makes it very easy to introduce XSS vulnerabilities when using simple_tag, and we have found examples of vulnerable code in the wild.

- [Learning resource at Intermediate to Advanced level. Experiences and Recommendations.](http://www.reddit.com/r/Python/comments/3bcfba/learning_resource_at_intermediate_to_advanced/)
    - core python
Discussion on reddit. Worth reading and participating in.

- [Use pylint and flask without spurious errors](https://github.com/jschaf/pylint-flask)
    - flask
pylint-flask is Pylint plugin for improving code analysis when editing code using Flask. Inspired by pylint-django.

- [EuroPython 2015: Call for On-site Volunteers](http://blog.europython.eu/post/122845271022)
    - community
EuroPython is organized and run by volunteers from the Python community, but we’re only a few and we will need more help to make the conference run smoothly.

- [Python descriptors made simple](http://www.smallsurething.com/python-descriptors-made-simple/)
    - core python
Descriptors, introduced in Python 2.2, provide a way to add managed attributes to objects. They are not used much in everyday programming, but it’s important to learn them to understand a lot of the “magic” that happens in the standard library and third-party packages. 



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


- [cnn-vis](https://github.com/jcjohnson/cnn-vis)
    - 180 Stars, 18 Fork
Inspired by Google's recent Inceptionism blog post, cnn-vis is an open-source tool that lets you use convolutional neural networks to generate images.

- [autosub](https://github.com/agermanidis/autosub)
    - 72 Stars, 4 Fork
Auto-generated subtitles for any video file

- [cli-github](https://github.com/harshasrinivas/cli-github)
    - 71 Stars, 9 Fork
Github within the CLI :computer:

- [ascii_py](https://github.com/ProfOak/ascii_py)
    - 20 Stars, 0 Fork
Make some ascii arts

(`是也乎:`

![pizza_in](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/pizza_in.jpg)

变成:

![ascii_pizza](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/ayy_lmao_pizza.jpg)

)

- [django-rest-framework-braces](https://github.com/dealertrack/django-rest-framework-braces)
    - 13 Stars, 0 Fork
Collection of utilities for working with django rest framework (DRF)

- [geog](https://github.com/jwass/geog)
    - 10 Stars, 0 Fork
Quick and easy geographical functions in Python

- [scli](https://github.com/davecarpie/scli)
    - 7 Stars, 0 Fork
A selectable, scrollable list interface for terminal applications built using curses

- [Stock_advisor](https://github.com/robbiebarrat/Stock_advisor)
    - 3 Stars, 0 Fork
This program uses the Yahoo_finance api for python to get basic stock info for a company the user inputs, and then looks at how the company's stock has been doing to give the user advice on whether they should buy some of that company or not. 

## DAMA 无责任推荐

- [lvsoft/enhanced_logging](https://github.com/lvsoft/enhanced_logging)
    - 9 星, 0 支

当年就有人黑 print 哪....


# 是也乎

- 1507?? 老高/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150707 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
