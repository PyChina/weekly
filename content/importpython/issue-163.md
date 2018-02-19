Title: 蠎加载 163
Slug: importpython-163
Date: 2018-02-19 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 163](http://importpython.com/newsletter/no/163/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [如何用 Jupyter Notebooks 以及 pandas 来分析数据?](https://blog.webkid.io/analysing-data-with-jupyter-notebooks-and-pandas/)
    + pandas, jupyter

Last year we discovered an extensive dataset on the subject of traffic on German roads provided by the BASt. It holds detailed numbers of cars, trucks and other vehicle groups passing more than 1,500 automatic counting stations. The amazing thing about this dataset is that the records for each counting station are provided on an hourly basis and they reach back to the year 2003. As an attempt to get to know the structure and to find a good way for dealing with the massive size of the dataset, we set up some Jupyter (formerly IPython) Notebooks.

(`是也乎:`

叕一篇 ipynb 的软文,
问题在, 依然没有解决从探索到作品的转化时机和技巧问题.

)



- [编写 Unit Tests 来测试 REST APIs](https://www.codementor.io/parthshandilya/writing-unit-tests-for-rest-apis-in-python-ge8wmbofg)
    + testing

I’m working on a project called BadgeYay. It is a badge generator with a simple web UI to add data and generate printable badges in PDF. BadgeYay's back-end is now shifted to REST-APIs and to test functions used in REST-APIs, we need some testing technology that will test each and every function used in the API. For our purposes, we chose the popular unit tests Python test suite. In this blog post, I’ll be discussing how I have written unit tests to test BadgeYay's REST-API.




- [极简 AWS Lambda + Python + Terraform 配置](http://www.davidbegin.com/the-most-minimal-aws-lambda-function-with-python-terraform/)
    + aws, lambda

I want to write and deploy the simplest function possible on AWS Lambda, written in Python, using Terraform.


(`是也乎:`

是的, OSX 中实现的...

)

- [4 个途径来提升 DevOps Testing - Free eBook](https://goo.gl/yUodv2)
    + sponsor

You already know the longer it takes to detect a problem, the more expensive it is to resolve. Your testing needs to happen earlier in the development pipeline while taking into account all aspects of privacy, security and monitoring. Read the 4-part eBook to learn how to detect problems earlier in your DevOps testing processes by:...

- [用 Python 创建 Discord Bot](https://www.devdungeon.com/content/make-discord-bot-python)
    + bot

In this video we'll cover how to create a bot for Discord. This bot will be able to join a server and show up in the user list. It will be able to interact in chat rooms and private messages and respond to custom commands.

- [用 Redis+Python 创建共享单车应用](https://opensource.com/article/18/2/building-bikesharing-application-open-source-tools)
    + project, web application

Learn how to use Redis and Python to build location-aware applications.

(`是也乎:`

很久没有听到 SOLOMO/LBS 的实例了...

)


- [介绍 Datalore - 叕一则用 Python 来进行机械学习的工具](https://blog.datalore.io/introducing-datalore/)
    + data, jetbrains

This Monday, February the 12th, we launched a public beta of Datalore - an intelligent web application for data analysis and visualization in Python, brought to you by JetBrains. This tool turns the data science workflow into a delightful experience with the help of smart coding assistance, incremental computations, and built-in tools for machine learning.




- [用 Python 和 Scikit-Learn 实现 K-Nearest 邻居算法](http://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/)
    + scikit-learn

In this article, we will see how KNN can be implemented with Python's Scikit-Learn library. But before that let's first explore the theory behind KNN and see what are some of the pros and cons of the algorithm.




- [The Flask Mega-Tutorial Part XI: Facelift](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift)
    + flask

This is the eleventh installment of the Flask Mega-Tutorial series, in which I'm going to tell you how to replace the basic HTML templates with a new set that is based on the Bootstrap user interface framework.

- [Apache Airflow 作为分布式系统的外部调度程序](https://medium.com/@rako/apache-airflow-as-an-external-scheduler-for-distributed-systems-53b7354d3e48)
    + airflow

So have you ever needed a reliable External scheduler for your distributed systems? Apache Airflow (by Airbnb) has a good stable scheduler. So how can we use Airflow for this purpose, here’s how we did.

(`是也乎:`

可能是俺错觉, 凡是发布在 medium 中的技术文章都比较科普...
没有作者在自己 blog 上的文章来的有用...

)


- [什么是单元和覆盖测试以及如何在 Python 中实现和使用它们](https://medium.com/@nathanpatnam/what-is-unit-testing-code-coverage-and-how-to-implement-and-use-them-in-python-a8f029558fe7)
    + unit testing



## 好物
~ 包/模块/库/片段...


- [gnomecast](https://github.com/keredson/gnomecast)
    - 623 Stars, 19 Fork

A native Linux Chromecast GUI that supports transcoding and subtitles.

(`是也乎:`


![gnomecast](https://raw.githubusercontent.com/keredson/gnomecast/master/screenshot.png)

正义的测试片儿...

Linux 中各种 GUI 用Python 实现是常见事物,
Chromecast 的还是头一次,
bottle 作内置 API 服务器, Gtk 3.0 作界面.


)


- [ENAS-pytorch](https://github.com/carpedm20/ENAS-pytorch)
    - 398 Stars, 27 Fork

PyTorch implementation of "Efficient Neural Architecture Search via Parameters Sharing"

(`是也乎:`

用核心任务的单词首字母拼成项目名称...
好吧, 美军领导的潮流...
)


- [zroya](https://github.com/malja/zroya)
    - 63 Stars, 2 Fork

Python wrapper of win32 for creating Windows notifications.

(`是也乎:`

细思恐极, 这么多年了, 终于见到一个 win32 平台的工具,
这说明 win10 终于被大家忍到习惯了?

![notification_center](https://github.com/malja/zroya/raw/master/doc/static/notification_center.png)
)


- [django-telegram-login](https://github.com/dmytrostriletskyi/django-telegram-login)
    - 26 Stars, 1 Fork

The reusable Django application for Telegram authorization (also known as Telegram login).

- [django-drf-react-quickstart](https://github.com/valentinogagliardi/django-drf-react-quickstart)
    - 13 Stars, 1 Fork

Django REST framework/React quickstart.

(`是也乎:`

Django 撞热点的能力/冲动, 天下无双...

)

- [django-referrer-policy](https://github.com/ubernostrum/django-referrer-policy)
    - 9 Stars, 0 Fork

A Django middleware implementing the Referrer-Policy header.

- [deep-voice-vector](https://github.com/andabi/deep-voice-vector)
    - 9 Stars, 2 Fork

A deep neural network for finding text-independent speaker embedding written in tensorflow and tensorpack.

(`是也乎:`

叕一个文字->语音的嗯哼, 问题是现在几乎没有自己撸基础代码的了, 
都在用云上的 AI 框架来...

)


- [django-rest-framework-serializer-mixins](https://github.com/allisson/django-rest-framework-serializer-mixins)
    - 9 Stars, 0 Fork

Mixins for Django Rest Framework Serializer.

- [potential-puns](https://github.com/randypiper/potential-puns)
    - 4 Stars, 0 Fork

Generate puns from English phrases.

(`是也乎:`

双关语? 英语的应该没那么多...
中文的可就是另外一种深度的事儿了...

)


- [jupyter_disqus](https://github.com/vwxyzjn/jupyter_disqus)
    - 3 Stars, 0 Fork

Add Disqus to your Jupyter notebook. 


(`是也乎:`


![jupyter_disqus](https://github.com/vwxyzjn/jupyter_disqus/raw/master/demo.gif)

神器, 必装插件之一...
当然, 中国用不了...

可是, 作者是华人...这就尴尬了

![profile_picture](https://costahuang.me/_nuxt/img/profile_picture.a70c2f0.png)
当然, Furman University 在校小生.

)

### (￣▽￣)

- [Neilpang/acme.sh: A pure Unix shell script implementing ACME client protocol](https://github.com/Neilpang/acme.sh)
    + https

> 国人作品, 解决 https 部署时的证书生成问题


- [kaleguy/leovue: File viewer for the Leo open source outline editor / IDE, integrated with Vue.js](https://github.com/kaleguy/leovue#leo-vue)
    + Leo,Vue

> 猛然发现, Leo 生态已经走到这种程度了...

![leovue](https://camo.githubusercontent.com/710523b7e44c98cbffe6546278535f6665ef5cec/68747470733a2f2f6b616c656775792e6769746875622e696f2f6c656f7675652f73637265656e63617374732f6c656f7675652d636f6d706f6e656e74732e676966)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180219 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180219 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


