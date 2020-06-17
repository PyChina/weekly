Title: Issue 425
Slug: issue-425
Date: 2020-06-17 10:42
Tags: Weekly,Python,pycoders,ZH


> 令机器学习投入生产


原文: [PyCoder's Weekly - Issue #425](https://pycoders.com/issues/425)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200617 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200617 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------






- [令机器学习投入生产](https://pycoders.com/link/4283/web)
    + VICKI BOYKIS

Millions of web apps get deployed to production every day. But machine learning models aren’t web apps. And very few people are talking about deployment. Learn how tools like Streamlit can help take the edge off deploying your machine learning models.

- [Python 生成器介绍](https://pycoders.com/link/4285/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn about generators and yielding in Python. You’ll create generator functions and generator expressions using multiple Python yield statements. You’ll also learn how to build data pipelines that take advantage of these Pythonic tools.


(`是也乎:`


![Generators](http://ydlj.zoomquiet.top/ipic/2020-06-17-ScreenShot%202020-06-17%2009.48.30.jpg)

)



- [皮尤研究中心的 Python 库](https://pycoders.com/link/4313/web)
    + PATRICK VAN KESSEL

The Pew Research Center’s Data Labs team has open sources two Python libraries for wrangling files and cleaning up text documents.

(`是也乎:`

目测, 这个研究库, 马上将被和谐.

)



- [异步 Python 并不快](https://pycoders.com/link/4277/web)
    + CAL PATERSON

Performance optimization is a tricky subject and silver bullets are rare. This article shines a light on some of the common misconceptions around async Python, like “async is always faster.” Related discussion on Hacker News.

(`是也乎:`

初学者困境...

就是非常容易被这种看似公允的测试说明相信一个断言.

> 真实场景中：

1、异步 web 服务器不可使用 reverse proxy，因为 async server 性能高于 reverse proxy。瓶颈位置在 reverse proxy 和 wsgi 层而非 web server。使用 reverse proxy 是因为多线程 context 切换成本高，开不了很多，所以需要一个能无限开 context 的异步服务器（nginx）挡在前面。而本身异步的服务器不需要。

2、异步 web server 不可使用 connection pool 和消息队列，因为无论是协程还是纯单线程异步，协程数和连接数都用不完。由于不存在多线程或者多进程的 context 切换成本，导致只能起有限的线程数，所以需要连接池。异步的连接数用不完，所以不需要连接池，否则会成为瓶颈。

3、异步服务器在并发数超过 1000 时才会明显体现出来，sync 服务器即使在使用 reverse proxy 的情况下由于中间的代理损耗也很难处理 1000 以上的并发。我在对异步服务器做性能测试的时候，是测试程序先挺不住，真实测试异步服务器的性能的技术含量不低，初学者做不到。

这篇作品槽点太多，先说以上几点。一个个讲过来，要打一天的字。

<-- 摘录隔壁群中对此文章的部分观点.

简单说, 对异步和协程的理解, 文章测试出发点就有问题.

)


- [新的 LEGO Mindstorm 机器人套件当然支持 Python](https://pycoders.com/link/4299/web)
    + LEGO.COM

In Fall 2020, LEGO will release a new Mindstorm Robot Inventor kit that allows children of all ages to build robots out of LEGO and program them with Python.


(`是也乎:`


LEGO 可能才是 Python 流行的最大推手.

)


- [Django 3.1 Beta 1 发布](https://pycoders.com/link/4293/web)
    + DJANGO SOFTWARE FOUNDATION

“Django 3.1 beta 1 is now available. It represents the second stage in the 3.1 release cycle and is an opportunity for you to try out the changes coming in Django 3.1. Django 3.1 has a potpourri of new features which you can read about in the in-development 3.1 release notes.”

- [太空科学与 Python](https://pycoders.com/link/4312/web)
    + THOMAS ALBIN

Explore and analyze the wonders and mysteries of space… with Python!


(`是也乎:`

其实, 一直有支持,
只是在 Musk 之后, 大家才以为是真的.

)





















































## 讨论
> Discussions


- [Python 是否禁止使用两个外观相似的 Unicode 标识符?](https://pycoders.com/link/4286/web)
    + STACK OVERFLOW

Set 𝑓 = 1729. Now print(f) prints 1729! Excuse me, but I have questions!



- [如何获得列表列表中每个项目的计数?](https://pycoders.com/link/4297/web)
    + STACK OVERFLOW

collections.Counter and itertools to the rescue!

- [git 如何知道 Python 函数/类定义的不同?](https://pycoders.com/link/4307/web)
    + TWITTER.COM
    + /SIMONW

Hint: Regular expressions. Lots of them.





















































## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [Python 关键字: 简介](https://pycoders.com/link/4302/web)
    + REAL PYTHON

Python keywords make up the fundamental building blocks of any Python program. In this tutorial, you’ll learn the basic syntax and usage for each of Python’s thirty-five keywords so you can write more efficient and readable code.

(`是也乎:`

![Keywords](http://ydlj.zoomquiet.top/ipic/2020-06-17-ScreenShot%202020-06-17%2009.10.51.jpg)

好绿...

)

- [在 Python 中调试 Out-Of-Memory 的崩溃](https://pycoders.com/link/4303/web)
    + ITAMAR TURNER-TRAURING

If your program crashes because it’s out of memory, how do you figure out where the memory issue occurs? The Fil memory profiler can help you out!


(`是也乎:`

俗称`验尸`技法.

)


- [使 Python 整数可迭代](https://pycoders.com/link/4292/web)
    + ARPIT BHAYANI

You can’t loop over an integer in Python… unless you change the source code! Learn how to make integers iterable by altering the CPython source code. Also learn why this is a bad idea.

- [Pandas 中的 SettingWithCopyWarning : 视图与副本](https://pycoders.com/link/4279/web)
    + REAL PYTHON

In this tutorial, you’ll learn about views and copies in NumPy and Pandas. You’ll see why the SettingWithCopyWarning occurs in Pandas and how to properly write code that avoids it.

(`是也乎:`

![SettingWithCopyWarning](http://ydlj.zoomquiet.top/ipic/2020-06-17-ScreenShot%202020-06-17%2009.08.08.jpg)

高级技巧.

)


- [使用此 Python 加密算法永远不会忘记密码](https://pycoders.com/link/4296/web)
    + MOSHE ZADKA

Share your passwords safely with friends and family, even if you don’t trust a couple of them, just as an ancient and wise king well versed in Python once did.

(`是也乎:`


加密和口令, 本身就是矛盾的事儿吧...

安全和麻烦成正比的.

)


- [Go 与 Python 的数据工程观点](https://pycoders.com/link/4298/web)
    + CHRISTIAN HOLLINGER

See how Go and Python stack up from the perspective of a data engineer by implementing the Mandelbrot set in both languages.


- [Raspberry Pi 上的 Python 处理 PDF 的项目](https://pycoders.com/link/4284/web)
    + REAL PYTHON 
    + podcast

Have you wanted to work with PDF files in Python? Maybe you want to extract text, merge and concatenate files, or even create PDFs from scratch. Are you interested in building hardware projects using a Raspberry Pi? Then check out this episode of the Real Python Podcast.

(`是也乎:`

![David Amos](http://ydlj.zoomquiet.top/ipic/2020-06-17-ScreenShot%202020-06-17%2009.06.43.jpg)

)


- [当心 SQLAlchemy 中 JSON 字段](https://pycoders.com/link/4282/web)
    + ADRIÀ MERCADER 
    + • Shared by Adrià Mercader

“PostgreSQL JSON fields are a really convenient way of storing structured data alongside traditional row/column values, but when using them in SQLAlchemy you should be mindful of how changes are detected.”




- [用 Python 和 Streamlit 分析梅西和罗纳尔多的游戏](https://pycoders.com/link/4314/web)
    + ADIL MOUJAHID

Build an interactive dashboard exploring Messi and Ronaldo’s games during the 2017-18 LaLiga season using Python and Streamlit.

- [TLDR 通讯: 针对技术人员的字节新闻](https://pycoders.com/link/4276/web)
    + TLDRNEWSLETTER.COM

TLDR is a daily, curated newsletter with links and TLDRs of the most interesting stories in tech, science, and programming.

- [Python 中基于属性的测试](https://pycoders.com/link/4304/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz







































































































## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [MicroscoPy: 用乐高积木/Arduino/Raspberry Pi 和 3D打印构建的开源/电动和模块化显微镜](https://pycoders.com/link/4309/web)
    + GITHUB.COM/IBM

(`是也乎:`


![MicroscoPy](http://ydlj.zoomquiet.top/ipic/2020-06-17-ScreenShot%202020-06-17%2008.59.52.jpg)

提供微雕精度的开源 3D 打印系统.

)

- [SpiceyPy: SPICE 工具包的 Pythonic 包装器](https://pycoders.com/link/4295/web)
    + GITHUB.COM/ANDREWANNEX

- [genetic-drawing: 用于绘图的遗传算法实验项目](https://pycoders.com/link/4280/web)
    + GITHUB.COM/ANOPARA

(`是也乎:`

模拟自然绘制过程的嗯哼...
)


- [pewtils: Pew研究中心的通用编程实用程序](https://pycoders.com/link/4305/web)
    + GITHUB.COM/PEWRESEARCH

- [pewanalytics: Pew研究中心的文本和统计实用程序](https://pycoders.com/link/4308/web)
    + GITHUB.COM/PEWRESEARCH

(`是也乎:`

pew 连击...
事实库, 开放各种社会现实数据给大家研究.

是 pew 慈善信托的子公司出资运维的.


)


- [chalice: 适用于 AWS 的 Python 无服务器微框架](https://pycoders.com/link/4311/web)
    + GITHUB.COM/AWS

(`是也乎:`

叕一个 AWS 生态衍生品.

)


- [dexplot: 包装 Matplotlib 并与 DataFrames 集成的简单绘图库](https://pycoders.com/link/4278/web)
    + GITHUB.COM/DEXPLO

- [streamlit: 构建自定义 ML 工具的最快方法](https://pycoders.com/link/4290/web)
    + GITHUB.COM/STREAMLIT

- [newtdb: 在 PostgreSQL 中具有基于 JSONB 访问和搜索功能的 Python 面向对象的数据库](https://pycoders.com/link/4306/web)
    + GITHUB.COM/NEWTDB


(`是也乎:`

基于  PostgreSQL JSONB ?
应该就是个 Pg 的拓展包?

怪不得项目名起的这么随便.

)













































## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


NIL 




(`是也乎:`

又一周空窗;

中国也已经接到有关通知, 允许线下集会申报了...

而且今年程序员节可能有超级大会.

)







## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp9py 在报名(能开发票 ;-)

![报名](http://ydlj.zoomquiet.top/ipic/2020-05-25-9py-reg-zip.jpg)

```

课程规划:
    开始报名 2020.5.31
    报名截止 2020.6.21
    正式开课 2020.6.28
    课程结束 2020.8.09

```
详情 => [蟒营™ Python 入门班第9期](https://py.101.camp/)




# PS:
- 首发: [Issue 425 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-425.html)
- 修订: [issue-425.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-425.md)


-------------
>> NN 4047

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 创始组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------

![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/425)






