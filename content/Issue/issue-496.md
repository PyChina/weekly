Title: PyCoder 496
Slug: issue-496
Date: 2021-10-27 11:42
Tags: Weekly,Python,pycoders,ZH


>  Django 4.0 Beta 1 发布


原文: [PyCoder's Weekly - Issue #496](https://pycoders.com/issues/496)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211027 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211027 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Python 惯用型](https://pycoders.com/link/7301/web)
    + REAL PYTHON 
    + course

What are the programming idioms unique to Python? This course is a short overview for people coming from other languages and an introduction for beginners to the idiomatic practices within Python. You’ll cover truth values, looping, DRY principles, and the Zen of Python.

(`是也乎:`

虽说, Python 是多范式语言, 
用什么习惯来撰写 Python 代码都可以,
不过, 最好还是用 Pythonic 形式来.

![Idiomatic](https://ipic.zoomquiet.top/2021-10-27-ScreenShot%202021-10-27%2008.44.34.jpg)


)



- [从 Python GIL 删除 Python Core 和 Sam 粗略的注意事项](https://pycoders.com/link/7302/web)
    + ŁUKASZ LANGA


“During the annual Python core development sprint we held a meeting with Sam Gross, the author of nogil, a fork of Python 3.9 that removes the GIL. This is a non-linear summary of the meeting.”

- Analyze Code-Level Application Performance Across Your Entire Environment With Datadog APM
    + DATADOG
    + sponsor
Datadog’s distributed tracing and APM generates flame graphs from real requests, enabling you to visualize app performance and pinpoint hard-to-reproduce problems in your production code. Without switching tools, you can pivot to related logs and metrics for full context. 
[Try Datadog APM free →](https://pycoders.com/link/7272/web)


- [PEP 660: 基于 PyProject.Toml 的版本可编辑安装 (Wheel Based)](https://pycoders.com/link/7275/web)
    + PYTHON.ORG

“Now that PEP 517 provides a mechanism to create alternatives to setuptools, and decouple installation front ends from build backends, we need a new mechanism to install packages in editable mode.”


(`是也乎:`

.ini
.py
.ymal
... 现在是 .toml

都是 SGML 的徒子徒孙...

)


- [Django 4.0 Beta 1 发布](https://pycoders.com/link/7288/web)
    + DJANGO SOFTWARE FOUNDATION

Check out the work-in-progress development release notes for more details.


(`是也乎:`

还好 Django 没学 Chrome,
否则, 今天至少是 v104 了

)


- [PyCon US 2022: 会议网站上线](https://pycoders.com/link/7287/web)
    + PYCON.ORG

PyCon US 2022 takes place in Salt Lake City, Utah from April 27, 2022 to May 5, 2022.

- [Vicky Twomey-Lee 获得 2021Q3 PSF社区服务奖](https://pycoders.com/link/7280/web)
    + PYTHON SOFTWARE FOUNDATION



-----------------------------------------
## 探讨/吐糟
> Discussions

- [你最具争议的 Python 相关意见是什么?](https://pycoders.com/link/7294/web)
    + REDDIT

“I like lambdas.”


(`是也乎:`

格式化字串
)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [遗传原则的组成](https://pycoders.com/link/7274/web)
    + BRANDON RHODES

“In Python as in other programming languages, this grand principle encourages software architects to escape from Object Orientation and enjoy the simpler practices of Object Based programming instead.”




- [在 Python 中使用 “not” Boolean 运算符](https://pycoders.com/link/7297/web)
    + REAL PYTHON


In this step-by-step tutorial, you’ll learn how Python’s “not” operator works and how to use it in your code. You’ll get to know its features and see what kind of programming problems you can solve by using “not” in Python.

(`是也乎:`


![Boolean](https://ipic.zoomquiet.top/2021-10-27-ScreenShot%202021-10-27%2008.32.50.jpg)

)

- [在 Python 中使用 len() 函式](https://pycoders.com/link/7303/web)
    + REAL PYTHON

In this tutorial, you’ll learn how and when to use the len() Python function. You’ll also learn how to customize your class definitions so that objects of a user-defined class can be used as arguments in len().


(`是也乎:`

![len](https://ipic.zoomquiet.top/2021-10-27-ScreenShot%202021-10-27%2008.31.11.jpg)

没事儿 len() 一下就好

)



- [PEP 670 \[Draft\]: 将宏转换为在 Python C API 中的函数](https://pycoders.com/link/7310/web)
    + PYTHON.ORG

“Converting macros and static inline functions to regular functions makes these regular functions accessible to projects which use Python but cannot use macros and static inline functions.”


(`是也乎:`

卫生宏的另一个思路?

)



- [A NASA TV Still Frame Viewer in Python](https://pycoders.com/link/7292/web)
    + PAOLO AMOROSO

Spacestills is a Python program for viewing NASA TV still frames. It’s a learning project based on the PySimpleGUI GUI framework.


(`是也乎":`

PySimpleGUI/Tk/... NASA 一向关注效率而不是美观


)



- [用 Arduino 和 Python (Differential Manchester Encoding) 将数据存储到盒式磁带上](https://pycoders.com/link/7307/web)
    + ZENINSTRUMENTS.BLOGSPOT.COM




- [全局声明在 Python 中真的意味什么?](https://pycoders.com/link/7308/web)
    + LUCA CHIODINI

- [在 Postgres 中用 Python and Pandas 内建一个推荐引擎](https://pycoders.com/link/7305/web)
    + CRAIG KERSTIENS


(`是也乎:`

淦...这不会拖累 Pg 的引擎嘛?


)


- [忘了设置自定义异常挂钩?  也许它还不太晚](https://pycoders.com/link/7285/web)
    + ANDRE ROBERGE




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [noaa-apt-decoder: 用 Python 解码 NOAA 天气卫星图像](https://pycoders.com/link/7273/web)
    + GITHUB.COM/JCH15



- [nMigen: Python 工具箱/用于构建复杂的数字硬件](https://pycoders.com/link/7295/web)
    + GITHUB.COM/NMIGEN




- [traviscli: 在 TravisCI 语义化版本你的 Python Project ](https://pycoders.com/link/7279/web)
    + GITHUB.COM/HASII2011 
    + • Shared by Humberto Sanchez II

(`是也乎:`

TravisCI 好久不见.
)


- [Ordained: Python 软件包的一种自由的模板](https://pycoders.com/link/7309/web)
    + BRYAN WOOD 
    + • Shared by Bryan Wood

- [staircase: 和 Mathematical Step Functions 一起折腾数据分析和操纵](https://pycoders.com/link/7284/web)
    + STAIRCASE.DEV 
    + • Shared by Riley Clement


(`是也乎:`

Mathematical ... Wolframe 经济支柱

)


- [django-dynamic-admin-forms: 给 Django Admin 追加简单交互](https://pycoders.com/link/7300/web)
    + PYPI.ORG

(`是也乎:`


再简单的交互也比没交互要好?


)



- [fork-purger: 删除你在 Github 中 所有 Forked Repositories](https://pycoders.com/link/7289/web)
    + GITHUB.COM/REDNAFI 
    + • Shared by Redowan Delowar

(`是也乎:`

嗯哼? 真,钢需

)


- [DearPyGui 1.0.0: 有 GPU 加速的 Python GUI 框架](https://pycoders.com/link/7282/web)
    + GITHUB.COM/HOFFSTADT


(`是也乎:`

![DearPyGui](https://ipic.zoomquiet.top/2021-10-27-ScreenShot%202021-10-27%2008.17.53.jpg)

发现1.0 了,
叕一个 GUI 框架,
对桌面 Python 从来没放弃.

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [⋅ Plone Conference 2021 Online](https://pycoders.com/link/7276/web)
    + October 23 to November 1, 2021

(`是也乎:`

活久见...真的在继续

)


- [⋅ PyData Global 2021](https://pycoders.com/link/7296/web)
    + October 28 to October 31, 2021

- [⋅ PythOnRio Meetup](https://pycoders.com/link/7277/web)
    + October 30, 2021

- [⋅ Melbourne Python Users Group](https://pycoders.com/link/7312/web)
    + November 1, 2021

- [⋅ PyCon Chile](https://pycoders.com/link/7291/web)
    + November 5 to November 8, 2021

- [⋅ deploy by DigitalOcean](https://pycoders.com/link/7290/web)
    + November 16 to November 17, 2021



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- COSCon21珠海
    + 10.30
    + 云创园

- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 496 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-496.html)
- 修订: [issue-496.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-496.md)


## PPS:
> 不觉中蟒周刊快译已经到了第9个年头

去年开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
从来没提醒过, 可就这么默默坚持下来了...

问为什么:

    [皱眉]每周新闻资讯 怎么能错过 
    看看有什么新东西 
    当有新的发现时：
        what f**k 还能这样玩？ 还有这东西？
        每周开彩蛋[吃瓜]

`无法同意更多`...
很多社区贡献看起来辛苦,
其实受益最多的,
就是主动承担者也.

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF496D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF496D4Q90XdDA7g):



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





