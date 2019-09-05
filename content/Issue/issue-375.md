Title: Issue 375
Slug: issue-375
Date: 2019-07-03 11:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #375](https://pycoders.com/issues/375)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [更频繁的 Python 版本?](https://pycoders.com/link/1915/web)
    + JAKE EDGE

"Łukasz Langa, who is the release manager for the upcoming 3.8 release, as well as the manager for the date-to-be-determined release of 3.9, has proposed PEP 596 ("Python 3.9 Release Schedule (doubling the release cadence)"). As its name would imply, the PEP proposes halving the current release cycle to nine months, which would make the 3.9 release happen in June 2020."

(`是也乎:`

事实证明, 开源项目版本攀爬速度,和基金会储备金数额呈正比关系

)



- [Python 标准库模块之间的依赖关系](https://pycoders.com/link/1914/web)
    + DOUG HELLMANN

What would a minimal Python standard library (only enough code to successfully download and install other packages) look like? Nice research and writeup.

(`是也乎:`

这也算红学变种...

其实, miniPy 之类项目早已完成了这种鉴定


)



- [Python 中的函数编程](https://pycoders.com/link/1916/web)
    + REAL PYTHON 
    + video

Learn how to approach functional programming in Python. You'll cover what functional programming is, how you can use immutable data structures to represent your data, as well as how to use filter(), map(), and reduce().

(`是也乎:`

真蟒的 FP.py 嗯哼...

)



- [如何构建 Raspberry Pi + Python 机器人](https://pycoders.com/link/1937/web)
    + AUGUST R. GARCIA

"Building robots seems expensive and complicated. However, it turns out that it's relatively straightforward. Do you have an IQ higher than 90 and assorted random garbage lying around your house? Then you too can make a robot in a reasonably small amount of time."

(`是也乎:`

叕一则和 RPi 来相关的嗯哼

)



- [如何通过 Python 用 Redis](https://pycoders.com/link/1932/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll cover how to use both Redis and its Python client library. You'll learn a bite-sized slice of Redis itself and master the redis-py client library.


(`是也乎:`


![Redis.py](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2015.51.33.jpg)

)


- [检测用 Python,Go 和 Rust 编写的程序](https://pycoders.com/link/1925/web)
    + NICOLAS HAHN

"This is a subjective, primarily developer-ergonomics-based comparison of the three languages from the perspective of a Python developer"


(`是也乎:`

WoW 可见, Python 性能并没差太多...在数据量足够大时...

另外, 还有一种可能没测试:

[indygreg/PyOxidizer: A modern Python application packaging and distribution tool](https://github.com/indygreg/PyOxidizer)

用 Rust 将 Python 再编译后...


)


- [SymPy 再次让数学变得有趣](https://pycoders.com/link/1930/web)
    + WORDSANDBUTTONS.ONLINE

Intro to SymPy, a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible.

(`是也乎:`

目标不是数值计算,
而是 计算机代数系统 (CAS)

)


## 讨论
> Discussions


- [选择无聊技术](https://pycoders.com/link/1945/web)
    + BORINGTECHNOLOGY.CLUB

Text version of an interesting talk about making technology choices by Dan McKinley. Related Hacker News discussion here.

(`是也乎:`

所以, 俺一直说 PHP 是最好的语言

)


- [Python Now Beating Java on Google Trends Worldwide](https://pycoders.com/link/1919/web)
    + REDDIT

(`是也乎:`

WoW 超越 JAVA...可以说, Python 已经变成更加无聊的技术了

)

## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [用 标记R-CNN 和 Python 来嗯哼停车位](https://pycoders.com/link/1926/web)
    + ADAM GEITGEY

Adam built a high-accuracy parking space notification system with Python and Deep Learning. Very cool!




- [用 GDB Python API 自动调试](https://pycoders.com/link/1923/web)
    + CHRIS COLEMAN

How to add custom GDB commands and pretty printers using the Python API.

(`是也乎:`

是否用 TDD 和是否上 GDB 是Python 开发阶段两大分水岭...

)


- [如何用 Docker 构建 CI/CD 管道](https://pycoders.com/link/1946/web)
    + CIRCLECI
    + sponsor

This post walks through the demo code from a talk given at DockerCon. It includes a CI/CD pipeline for a Python Flask app. The pipeline builds a Docker image, pushes the image to Docker Hub, and kicks off a deployment script which will run the app in a container on a DigitalOcean server.

(`是也乎:`

这么搞很磨硬盘就是了...

)


- [在 Raspberry Pi 上用 Python 构建 CO₂ 监视器](https://pycoders.com/link/1933/web)
    + NATHAN GOLDBAUM

"I've definitely experienced situations where I had to sit in a room with lots of people and felt more and more tired the longer I spent in the room. I had never considered that this is more than just being bored, that there might be a physiological reason for this feeling."

(`是也乎:`

随着 Raspberry Pi 4 的上市,
主力板上开发语言 Python 也就嗯哼起来了

![CO₂ Monitor](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2015.29.31.jpg)

)


- [用 Python 和 XGBoost 构建 机器学习 进行电子邮件签名检测](https://pycoders.com/link/1928/web)
    + ALESSANDRO WOLLEK

Extracting contact information from emails using supervised machine learning algorithms.

(`是也乎:`

Spam 识别基础姿势, 经典.

)


- ["Python 并发" 测试](https://pycoders.com/link/1908/web)
    + REAL PYTHON

Test your understanding of concurrency and parallel programming concepts in Python, such as the difference between CPU-bound and I/O-bound programs, the GIL, and more.

(`是也乎:`

![Concurrency"](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2015.21.14-1.jpg)

)


- [可视化介绍 NumPy 以及数据表达](https://pycoders.com/link/1911/web)
    + JAY ALAMMAR

A look at some of the main ways to use NumPy and how it can represent different types of data like tables, images, text, etc.

(`是也乎:`

![numpy-color-image](https://jalammar.github.io/images/numpy/numpy-color-image.png)

走心了, 非常好的可视化概念系列图...


)

- [用 Python 从头嗯哼持续集成和部署](https://pycoders.com/link/1918/web)
    + TOMAS FERNANDEZ

Learn how to set up continuous integration and deployment for your Python projects using Semaphore, a cloud-based CI/CD service.

(`是也乎:`

徒手 CI ?

)


- [如何用 Python 制作智能婴儿监视器](https://pycoders.com/link/1912/web)
    + RYAN KAUFFMAN

Learn to build your own smart baby monitor using Python, a Raspberry Pi, peripheral sensors and the Twilio API for sending SMS.

(`是也乎:`

这个明显用国内 AliYun 相同功能 API 也可以快速完成的

![Baby Monitor](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2015.39.13.jpg)

)


- [Raspberry Pi(或Amazon EC2)上的远程Python开发](https://pycoders.com/link/1931/web)
    + ADRIAN ROSEBROCK

How to configure your host machine to connect to these systems and remotely perform Python development.

(`是也乎:`

嗯哼? 硬件和 VPS 一视同仁了?
嚓, CV 专家给出了一系列远程嗯哼的姿势,
可以说非常嗯哼了...

)


- [初学Python程序员常见 5 种错误](https://pycoders.com/link/1913/web)
    + PYTHONCIRCLE.COM

(`是也乎:`

叕一组新手常见手残行为检查表...
其实... PEP8 相关守则足够了.

)


- [处置 Multipart/Form-Data Natively in Python](https://pycoders.com/link/1941/web)
    + JULIEN DANJOU

- [在 Python 2 库中使用类型提示](https://pycoders.com/link/1935/web)
    + MARKUS UNTERWADITZER



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [riposte: Wrap Python Apps Inside a Tailored Interactive Shell](https://pycoders.com/link/1924/web)
    + GITHUB.COM/FWKZ

(`是也乎:`

叕一个交互 CLI 构造辅助库,
强化连续引导的嗯哼...

)


- [PyMathProg: Mathematical Programming Environment for Python](https://pycoders.com/link/1909/web)
    + SOURCEFORGE.NET

(`是也乎:`

古早味儿专用模块.

)

- [easyfile: Python Random File Access for Humans](https://pycoders.com/link/1917/web)
    + GITHUB.COM/YASUFUMY

(`是也乎:`


    import easyfile

    data = easyfile.TextFile('/path/to/text')

    data[0] # Access the first line of your text
    data[-1] # Access the last line of your text
    data[10:100] # Access the 10th line to the 100 the line of your text

等等, 怎么就随机了?

一个日本程序猿写给自己用的模块...都被发现了...


)


- [heroku-load-balancer: Load Balancer for Your Heroku Pipeline Applications](https://pycoders.com/link/1920/web)
    + GITHUB.COM/DMYTROSTRILETSKYI

(`是也乎:`

Heroku 次生兵器...可见其生态多丰茂

)


- [catcher: Microservices Test and Univeral Migrations Tool](https://pycoders.com/link/1910/web)
    + GITHUB.COM/COMTIHON

(`是也乎:`

![catcher](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2014.49.32.jpg)

微服务不是已经凉了?

)


## 📆🐍 活动/大会
> Events


- [⋅ Caipyra 2019](https://pycoders.com/link/1929/web)
    + July 7 to July 11, 2019

(`是也乎:`

![Caipyra](https://ipic.zoomquiet.top/2019-07-03-ScreenShot%202019-07-03%2014.44.24.jpg)

西班牙...拼写...

)

- [⋅ SciPy 2019](https://pycoders.com/link/1938/web)
    + July 8 to July 15, 2019
    + Austin, Texas
    + USA

- [⋅ EuroPython 2019](https://pycoders.com/link/1943/web)
    + July 8 to July 15, 2019
    + BASEL
    + 瑞士

![EuroPython](https://ep2019.europython.eu/static/img/ep2019-logo-720px-alpha-brighter.png)

- [⋅ PyData London 2019](https://pycoders.com/link/1940/web)
    + July 12 to July 15, 2019
    + 英国
    + 差点能去...

- [⋅ Dash Conference](https://pycoders.com/link/1949/web)
    + July 16 to July 17, 2019 
    + in NYC



## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 第2期

> 应该 190704 开始报名



[![PyScaffold](https://pyscaffold.org/en/latest/_images/logo.png)](https://pyscaffold.org/en/latest/)

~ helps you setup a new Python project


- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
    + FAQ

(`是也乎:`

![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)

总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...

其实, 本质上并不是对应技术是否有什么能力,
而是相反...

)




### Jobs:
> ...

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
    + 北京
    + anti-996


# 是也乎

- 190703 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190703 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
