Title: Issue 485
Slug: issue-485
Date: 2021-08-11 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.10RC 发布


原文: [PyCoder's Weekly - Issue #485](https://pycoders.com/issues/485)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210811 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210811 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [在 pypi 上发布时该怎么来?](https://pycoders.com/link/6824/web)
    + BRETT CANNON

Mistakes happen to everyone. But what do you do if you make a mistake when releasing a package to PyPI? Don’t panic! There are a number of things you can do to fix a bad release. This article walks you through several scenarios and suggested solutions.





- [用 Mock Server 扩展 E2E 测试](https://pycoders.com/link/6838/web)
    + YAEL MINTZ

End-to-end (E2E) testing is a crucial step in delivering high-quality software, but the ins and outs of E2E can be challenging. You often need multiple, separate services to talk to each other during tests, and coordinating this can be difficult. Learn some approaches for E2E test development and how the new Cornell Python package can help make your life easier.


(`是也乎:`


![E2E](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2012.02.27.jpg)

问题在如何保证 Mock 和真实系统反应一致?


)


- [Track Requests to Your Python Applications End-to-End With Datadog APM](https://pycoders.com/link/6810/web)
    + DATADOG
    + sponsor

Analyze your Python apps’ performance by drilling into error traces with Datadog’s App Analytics to debug and optimize Python code. Trace requests end-to-end across web servers, databases, and services in your environment and start visualizing your apps’ performance with Datadog APM free →

- [海象运算符:= Python 3.8赋值表达式](https://pycoders.com/link/6831/web)
    + REAL PYTHON

In this tutorial, you’ll learn about assignment expressions and the walrus operator. The biggest change in Python 3.8 was the inclusion of the := operator, which you can use to assign variables in the middle of expressions. You’ll see several examples of how to take advantage of this new feature.


(`是也乎:`

![Assignment](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2011.58.36.jpg)


海象表达式, 关键问题是可计算的范畴...
真.自由的话,
就变成 JS 那种无限 函式嵌套了...

![Walrus](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2011.58.55.jpg)


)


- [2021 Django 开发者调查](https://pycoders.com/link/6827/web)
    + DJANGO SOFTWARE FOUNDATION

Are you a Django user? The Django Software Foundation wants to hear from you!

(`是也乎:`

无论是不是 Django 用户,
都可以去填写...

)


- [Python 3.10 第一个 Release Candidate 发表](https://pycoders.com/link/6820/web)
    + PYTHON.ORG




-----------------------------------------
## 探讨/吐糟
> Discussions



- [Reddit AMA With Will McGugan/Rich 和 Textual 作者](https://pycoders.com/link/6816/web)
    + REDDIT

Learn all about Rich and Textual in this Q&A thread with the libraries’ author. Ever wondered what Will thinks of the new pattern matching feature coming in Python 3.10, or whether plots will ever come to Rich or Textual? Find out here!



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Django Rest Framework 食谱](https://pycoders.com/link/6833/web)
    + JUSTYNA ILCZUK

The Django Rest Framework (DRF) allows you to build REST APIs on top of Django. This article explores some recipes for various tasks in DRF taken from the author’s real-world experience.

- [从 FastAPI 开始并检查 Python 的 Import 系统](https://pycoders.com/link/6837/web)
    + REAL PYTHON 
    + podcast

Have you heard of FastAPI? An application programming interface is vital to make your software accessible to users across the internet. FastAPI is an excellent option for quickly creating a web API that implements best practices. This week on the Real Python Podcast, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.


(`是也乎:`

FastAPI 替代 Flask 变成新.Django 接替人选了..

![FastAPI](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2011.56.23.jpg)

)


- [NumPy Views: 保存内存/内存泄漏和微妙的错误](https://pycoders.com/link/6821/web)
    + ITAMAR TURNER-TRAURING

NumPy has a built-in memory view feature that helps reduce memory usage for large arrays. But in some cases, memory views can cause higher memory usage, and even cause bugs by mutating data in unexpected ways. Learn how memory views work, what common issues are, and some takeaways to help you decide when memory views are a good choice.

(`是也乎:`

毕竟底层还是有 C 代码...

)



- [有效地使用 Python 返回声明](https://pycoders.com/link/6835/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn how to use the Python return statement when writing functions. Additionally, you’ll cover some good programming practices related to the use of return. With this knowledge, you’ll be able to write readable, robust, and maintainable functions in Python.

(`是也乎:`


![return](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2011.52.59.jpg)

万物皆可返回...

)


- [Django代理让自己体验更好](https://pycoders.com/link/6814/web)
    + NICCOLÒ MINEO 
    + • Shared by Niccolò Mineo

Ah, Django proxy models and the power they hold! Yet, the implementation aftermath can highlight a number of unwanted side-effects. Here’s a couple of tips when working with Django proxies that will make end-users grateful and developers sigh in relief.

(`是也乎:`

对的蟒周刊可以自己推荐自己的文章...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [catanatron: 实现强大 AI 播放器的快速构建者](https://pycoders.com/link/6826/web)
    + GITHUB.COM/BCOLLAZO




- [python-ftfy: Fixes Mojibake and Other Glitches in Unicode Text, After the Fact](https://pycoders.com/link/6834/web)
    + GITHUB.COM/LUMINOSOINSIGHT

(`是也乎:`

嗯哼? Glitches,
Joel 的神奇脑洞,
又将成功流行了?

)


- [cornell: 用于端到端测试的记录和重播模拟服务器](https://pycoders.com/link/6830/web)
    + GITHUB.COM/HIREDSCORELABS

(`是也乎:`

e2e 测试太重要了,
可惜一直没什么很好的自动化测试框架,
俺是说 Ajax 之后,
之前软件都是 CLI 到 CLI 很容易模拟和测试...


![cornell](https://ipic.zoomquiet.top/2021-08-11-ScreenShot%202021-08-11%2011.51.28.jpg)

用自己美丽的头像作项目 logo...

)


- [bagua: 用以 PyTorch 和 Blazing 快速构建的分布式训练库](https://pycoders.com/link/6825/web)
    + GITHUB.COM/BAGUASYS 
    + • Shared by Xiangru Lian

- [Refactor: Python 源代码重构工具包](https://pycoders.com/link/6841/web)
    + GITHUB.COM/ISIDENTICAL 
    + • Shared by Batuhan Taskaya


(`是也乎:`

重构也不是银弹,
但是,
不妨碍形成这种错觉...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

NIL
 
-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:

- 首发: [Issue 485 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-485.html)
- 修订: [issue-485.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-485.md)


-------------

好文笔,感叹号年度配额: **2/3**

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





