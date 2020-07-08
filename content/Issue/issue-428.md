Title: Issue 428
Slug: issue-428
Date: 2020-07-08 11:42
Tags: Weekly,Python,pycoders,ZH


> Pylance/ VSCode 全新 Python 支持扩展


原文: [PyCoder's Weekly - Issue #428](https://pycoders.com/issues/428)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200708 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200708 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [发布 Pylance: Visual Studio Code 对 Python 快速/功能丰富的语言支持](https://pycoders.com/link/4460/web)
    + SAVANNAH OSTROWSKI

Pylance is a new Python language server for VS Code based on Microsoft’s Pyright static type checking tool. With Pylance, you get type information in function signatures and when hovering on symbols, auto import suggestions, type checking diagnostics, and so much more!

(`是也乎:`

官方推出更加强大的 Python 支持扩展,
更多的分析, 更多的提示, 以及更多的内存抢占....

> 俺是什么 Py 支持扩展都不安装的.

)


- [Python 异步框架:超越开发者部落](https://pycoders.com/link/4458/web)
    + TOM CHRISTIE

In light of some recent and, at times, heated discussions regarding asynchronous programming in Python, Django Rest Framework’s creator Tom Christie calls on the community to embrace a more collaborative spirit.


(`是也乎:`

在异步大浪中, 没有人原意和同步粘边儿.

)


- [关闭文件的相反观点](https://pycoders.com/link/4465/web)
    + ARIC COADY 
    + opinion

You’ve may have heard that the “right” way to open a file in Python is to use the open() function inside of a with statement. But is that always the right choice?

- [Flask 项目设置: TDD/Docker/Postgres/...](https://pycoders.com/link/4445/web)
    + LEONARDO GIORDANI

Learn one way to set-up a Flask project, including how to handle project requirements, configuration and environment variables, writing and running tests, and containerizing the application with Docker. When you’re done reading part one at the link above, check out part two.

- [Django 入门第2部分: 用户管理](https://pycoders.com/link/4448/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to extend your Django application with a user management system, complete with email sending and third-party authentication.

(`是也乎:`


![Django](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2010.01.10.jpg)

)


- [用 FastAPI 和 Heroku 部署和托管机器学习模型](https://pycoders.com/link/4462/web)
    + MICHAEL HERMAN 
    + • Shared by Michael Herman

Getting machine learning models into production is an often-overlooked topic. Learn how to serve a model in just a handful of lines of Python using FastAPI and Heroku.

(`是也乎:`

FastAPI 是好的, 
Heroku 就嗯哼了...

)


- [2020年 Python 软件基金会董事会选举回顾及后续](https://pycoders.com/link/4447/web)
    + ERNEST W. DURBIN III

(`是也乎:`

DURBIN 三世, 这名字大气哪.
)


- [Python 3.9.0b4 已可测试](https://pycoders.com/link/4454/web)
    + CPYTHON DEV BLOG




## 讨论
> Discussions

- [Python 语言核心是什么?](https://pycoders.com/link/4443/web)
    + HACKER NEWS

Last week we featured Brett Cannon’s article with the same title. Well, the post has generated quite a discussion on Hacker News.

(`是也乎:`

上周触发的大讨论还在继续

)


- [为什么 NaN 值使 min() 和 max() 对顺序敏感?](https://pycoders.com/link/4446/web)
    + STACK OVERFLOW

How NaNs compare to numerical values and the implications of that in min() and max() might be surprising.

- [为毛 f-Strings 存在时人们还要用 format()?](https://pycoders.com/link/4438/web)
    + REDDIT

f-Strings aren’t exactly a drop-in replacement for .format().


(`是也乎:`

显性和隐性调用, 
一般为了管理, 还是显性来的明确.

)


## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [谎言的迷宫](https://pycoders.com/link/4464/web)
    + MOSHE ZADKA

What should you do after watching 1986’s puppet-laden musical fantasy Labyrinth? Code up the guard scene in Python, of course! After you read Moshe’s solution to the infamous “Two Door Riddle” at the link above, check out Glyph Lefkowitz‘s “professionalized” version of the code.

(`是也乎:`

Python 一直没离开过艺术界

)


- [大量内存开销: Python 中的数字以及 NumPy 如何提供帮助](https://pycoders.com/link/4467/web)
    + ITAMAR TURNER-TRAURING

In Python, everything is an object. Even numbers. While this has advantages, objects have a memory overhead that might be unexpected. While this overhead is often negligible, it might be the difference between 8GB and 35GB in extreme cases.


- [用 StaticFrame 替代 Pandas 的十个理由](https://pycoders.com/link/4453/web)
    + CHRISTOPHER ARIZA 
    + • Shared by Christopher Ariza

For those coming from pandas, StaticFrame offers a more consistent interface and reduces opportunities for error. This article demonstrates ten reasons you might use StaticFrame instead of Pandas.

- [如何用 Python 筛选器](https://pycoders.com/link/4456/web)
    + KATHRYN HANCOX

Python’s built-in filter() function can be used to create a new iterator from an existing iterable with certain elements removed based on some criterion.




- [思索 Pandas: Python 数据分析是正确的方法](https://pycoders.com/link/4466/web)
    + REAL PYTHON 
    + podcast

Are you using the Python library Pandas the right way? Do you wonder about getting better performance, or how to optimize your data for analysis? What does normalization mean? This week Hannah Stepanek joins the podcast to discuss her new book “Thinking in Pandas”.

(`是也乎:`

> 正确的路线...

一切都应该在内存中.


)




- [面向对象编程 (OOP) 在 Python 3](https://pycoders.com/link/4440/web)
    + REAL PYTHON

In this freshly updated OOP tutorial, you’ll learn all about object-oriented programming in Python. You’ll learn the basics of the OOP paradigm and cover concepts like classes and inheritance.

(`是也乎:`

![OOP](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.49.03.jpg)


嗯哼? 特意看了一下日期...
2020 了, 还要忽悠 OOP 嘛?

)


- [教程: 基于 If-Else 条件将列添加到 Pandas DataFrame](https://pycoders.com/link/4457/web)
    + CHARLIE CUSTER 
    + • Shared by Charlie Custer

If you’re new to pandas, you might be tempted to add a column to a DataFrame based on a condition using an if statement. But there’s a better way!

- [Darts: 用 Python 简化时间序列](https://pycoders.com/link/4461/web)
    + JULIEN HERZEN

Darts is a new library from Unit8 that offers a single package for end-to-end machine learning on time series.


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [EasyOCR: 即用型OCR，支持40多种语言，包括中文，日文，韩文和泰文](https://pycoders.com/link/4452/web)
    + GITHUB.COM/JAIDEDAI


(`是也乎:`

42国语言 OCR 支持.

![EasyOCR](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.42.11.jpg)

>  Afrikaans (af), Azerbaijani (az), Bosnian (bs), Simplified Chinese (ch_sim), Traditional Chinese (ch_tra), Czech (cs), Welsh (cy), Danish (da), German (de), English (en), Spanish (es), Estonian (et), French (fr), Irish (ga), Croatian (hr), Hungarian (hu), Indonesian (id), Icelandic (is), Italian (it), Japanese (ja), Korean (ko), Kurdish (ku), Latin (la), Lithuanian (lt), Latvian (lv), Maori (mi), Malay (ms), Maltese (mt), Dutch (nl), Norwegian (no), Polish (pl), Portuguese (pt),Romanian (ro), Slovak (sk) (need revisit), Slovenian (sl), Albanian (sq), Swedish (sv),Swahili (sw), Thai (th), Tagalog (tl), Turkish (tr), Uzbek (uz), Vietnamese (vi)

)

- [python-keyboard: 由 Python 驱动的手造双模键盘](https://pycoders.com/link/4473/web)
    + GITHUB.COM/MAKERDIARY


(`是也乎:`

![Powered.py](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.39.32.jpg)

嗯哼? 现在定制键盘厂商已经硬核到这种程度了?


![keyboard](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.39.46.jpg)

--> [python-keyboard: 手焊的、跑 Python 的 USB + 蓝牙双模键盘](https://gitee.com/makerdiary/python-keyboard)

)

- [static-frame: 具有自对准标记轴的一维和二维计算的不可变数据结构](https://pycoders.com/link/4455/web)
    + GITHUB.COM/INVESTMENTSYSTEMS

Calculations With Self-Aligning, Labelled Axes


- [isort: 用于对导入进行排序的实用程序](https://pycoders.com/link/4472/web)
    + GITHUB.COM/TIMOTHYCROSLEY

- [darts: 一个易于操作和预测时间序列的 Python 库](https://pycoders.com/link/4468/web)
    + GITHUB.COM/UNIT8CO


(`是也乎:`


嗯哼, 这名起的...太纠缠了.
)

- [pygooglenews: 如果 Google 新闻具有 Python 库](https://pycoders.com/link/4449/web)
    + GITHUB.COM/KOTARTEMIY


(`是也乎:`

如果...

)

- [guietta: 制作简单 Python GUI 的工具](https://pycoders.com/link/4444/web)
    + GITHUB.COM/ALFIOPUGLISI

(`是也乎:`

叕一个 GUI 框架出现,
是否针对最终用户的 GUI 框架活跃,
说明一个技术生态开始向终端市场倾斜了?

等等,只是 Qt 的一种包裹?

)


- [texthero: 从零到雄奇 的文本预处理/表示和可视化](https://pycoders.com/link/4469/web)
    + GITHUB.COM/JBESOMI

(`是也乎:`


![texthero](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.35.01.jpg)

文本豪杰 ~ Pandas 的方面方言.


![Hero](http://ydlj.zoomquiet.top/ipic/2020-07-08-ScreenShot%202020-07-08%2009.34.52.jpg)

)

- [ether-automaton: 基于生命游戏制作漂亮像素动画](https://pycoders.com/link/4450/web)
    + GITHUB.COM/ETHER-AUTOMATON 
    + • Shared by anfederico

(`是也乎:`

彩色动画版 生命游戏.

)

- [strongtyping: Python 函数运行时类型检查装饰器](https://pycoders.com/link/4474/web)
    + GITHUB.COM/FELIXTHEC

(`是也乎:`

运行时检验, 永远 bigger 不够哪.

)


- [django-pgtrigger: Postgres 触发器与 Django 模型集成](https://pycoders.com/link/4479/web)
    + GITHUB.COM/JYVEAPP 
    + • Shared by Wes Kendall

(`是也乎:`

好象现在对 Pg 上心, 才是政治正确的姿态.

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ SciPy 2020 (Virtual Conference)](https://pycoders.com/link/4442/web)
    + July 6 to July 13, 2020

- [⋅ PyMNTos (Virtual Meetup)](https://pycoders.com/link/4478/web)
    + July 9, 2020

- [⋅ Python Atlanta (Virtual Meetup)](https://pycoders.com/link/4475/web)
    + July 9, 2020


(`是也乎:`

中国也已经接到有关通知, 允许线下集会申报了...

而且今年程序员节(10.24)可能有超级大会.
)




## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp10py 开始报名

![报名](ydlj.zoomquiet.top/ipic/2020-06-22-200622reg10py-zip.jpg)

```

课程规划:
    报名截止 2020.7.20
    正式开课 2020.7.26
    课程结束 2020.9.06

```
详情 => [蟒营™ Python 入门班第10期](https://py.101.camp/)

> 提醒: 首周报名再优惠 420 元.


# PS:
- 首发: [Issue 428 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-428.html)
- 修订: [issue-428.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-428.md)


-------------
>> NN 4068

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

![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/428)






