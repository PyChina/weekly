Title: PyCoder 534
Slug: issue-534
Date: 2022-07-20 11:42
Tags: Weekly,Python,pycoders,ZH


> 是的,俺对侬的开源贡献有意见...


原文: [PyCoder's Weekly - Issue #534](https://pycoders.com/issues/534)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220720 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220720 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [衡量代码质量/简单性和可维护性](https://pycoders.com/link/9132/web)
    + REAL PYTHON 
    + PODCAST

How maintainable is your Python code? Is it possible to hold the code for your functions in your head? When is it appropriate to use measurements in a code review? This week on the show, Reka Horvath and Ben Martineau from Sourcery are here to discuss their recent PyCon talk, “Actionable insights vs ranking: How to use and how NOT to use code quality metrics.”

(`是也乎:`


![PODCAST](https://ipic.zoomquiet.top/2022-07-20-zshot%202022-07-20%2011.39.38.jpg)

其实, 如果不从小作品开始养成这种习惯, 到大团队, 基本上不可能适应, 或是推进类似品质管理

)


- [Subtests 在 Python](https://pycoders.com/link/9150/web)
    + PAUL GANSSLE

“unittest.TestCase.subTest was originally introduced in Python 3.4 as a lightweight mechanism for test parameterization; it allows you to mark a section of your test as a separate test in its own right using a context manager.” Learn all about sub-tests in both the unittest module and pytest.


(`是也乎:`

单元测试下, 还有一层测试...

)

- [在 Python 中并行处理大文件](https://pycoders.com/link/9134/web)
    + ABID ALI AWAN

When working with large amounts of data, using more than one CPU can lead to significant speed gains. Learn about various techniques that reduce data processing time by using multiprocessing, joblib, and tqdm.

- [Python 3.11.0b4 发布](https://pycoders.com/link/9143/web)
    + PYTHON.ORG





-----------------------------------------
## 探讨/吐糟
> Discussions



- [不在允许 Packages 能 PyPI 中的东西?](https://pycoders.com/link/9144/web)
    + PYTHON.ORG

- [学习新语言/框架时值得撰写什么](https://pycoders.com/link/9135/web)
    + HACKER NEWS

(`是也乎:`

官方教程,官方教程,官方教程...以及拿自己以往作品, 
改写过来, 最快乐...

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [SQLite 和 SQLAlchemy 在 Python: 超越 Flat Files](https://pycoders.com/link/9131/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to store and retrieve data using Python, SQLite, and SQLAlchemy as well as with flat files. Using SQLite with Python brings with it the additional benefit of accessing data with SQL. By adding SQLAlchemy, you can work with data in terms of objects and methods.

(`是也乎:`

![SQLAlchemy](https://ipic.zoomquiet.top/2022-07-20-zshot%202022-07-20%2011.30.40.jpg)

不过, 还是直写 SQL 最爽直

)


- [NumPy 的 max() 以及 maximum(): 查找极值](https://pycoders.com/link/9138/web)
    + REAL PYTHON

In this introduction to NumPy, you’ll learn how to find extreme values using the max() and maximum() functions. This includes finding the maximum element in an array or along a given axis of an array, as well as comparing two arrays to find the larger element in each index position.

(`是也乎:`

![max](https://ipic.zoomquiet.top/2022-07-20-zshot%202022-07-20%2011.30.01.jpg)

)

- [是的, 我对您的开源贡献有意见](https://pycoders.com/link/9155/web)
    + JAMES BENNETT 
    + OPINION

James Bennett weighs in on the Internet’s response to PyPI starting to roll out 2FA and in particular to Armin Ronacher’s 
[Congratulations: We Now Have Opinions on Your Open Source Contributions](https://pycoders.com/link/9151/web)

- [Python 和 TOML: 新好朋友](https://pycoders.com/link/9136/web)
    + REAL PYTHON

TOML is a configuration file format that’s becoming increasingly popular in the Python community. In this tutorial, you’ll learn the syntax of TOML and explore how you can work with TOML files in your own projects.

(`是也乎:`

汤小明的小巧明晰语言...
其实就是 GitHub 统治开发世界叕一个先锋...

![TOML](https://ipic.zoomquiet.top/2022-07-20-zshot%202022-07-20%2011.23.27.jpg)

网友们总结的好:

ini 太简单, json 太难编辑, yaml 太复杂, .py 或是其它太专有,
结果, TOML 就钻了这个空, 并根据这个配置格式, 在逐步统治各种语言和 k8s 生态...

)



- [Pip 约束文件](https://pycoders.com/link/9161/web)
    + LUMINOUSMEN

Sometimes, it is difficult to determine what the original dependencies of a Python application are. Since version 7.1, pip has supported the use of a constraints file which can help solve this problem.

(`是也乎:`

已经在用 pip 21.x.x 了, 也从来没用过这一特性
)


- [优化 Django 管理分页器](https://pycoders.com/link/9157/web)
    + HAKI BENITA

The Django Admin is a powerful tool for quickly making changes to your data, but at scale it can require some tweaking. Learn what you can do to improve the performance of pagination in the admin.


(`是也乎:`

加速100倍, Wow

)

- [在迁移到微服务之前单体应用的准备](https://pycoders.com/link/9148/web)
    + TOMAS FERNANDEZ

“Like tidying up a house before a total renovation, preparing your monolith is the first step towards transitioning to microservices.” Learn more about what you should do before you transition.


(`是也乎:`

不, 可以不迁移的
)

- [制作热图](https://pycoders.com/link/9163/web)
    + MARK LITWINTSCHIK

Learn how to build a heatmap diagram using the ClickHouse and QGIS libraries. The article includes step-by-step instructions for building a heatmap using CSV data.

(`是也乎:`

![Heatmaps](https://tech.marksblogg.com/theme/images/qgis-heatmap.png)

)


- [在 Mac 上发布 PyGame 应用程序的小技巧](https://pycoders.com/link/9164/web)
    + GLYPH

Got some awesome PyGame you want to share with a Mac user? This post walks you through the ins-and-outs of using pyapp to ship to macOS.





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [django-awl: 用于管理/标签/测试等的杂项工具](https://pycoders.com/link/9140/web)
    + GITHUB.COM/CLTRUDEAU

- [readysetdata: 清理特定数据集的脚本](https://pycoders.com/link/9149/web)
    + GITHUB.COM/SAULPW

- [design-by-contract: 编写 Design-by-Contract 的装饰器](https://pycoders.com/link/9137/web)
    + GITHUB.COM/STEFANULBRICH 
    + • Shared by Stefan Ulbrich

- [tasktiger: 使用 Redis 的 Python 任务队列](https://pycoders.com/link/9141/web)
    + GITHUB.COM/CLOSEIO


(`是也乎:`

感觉, 现在 Queus 不带 Redis 都是邪恶的?

)


- [reloadium: Python 的高级热重载](https://pycoders.com/link/9133/web)
    + GITHUB.COM/RELOADWARE

(`是也乎:`

重载素, 可以在各种框架/模块中作用;
PyCharm 配套插件, 也可以独立使用;


)





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Heidelberg Python Meetup](https://pycoders.com/link/9129/web)
    + July 20, 2022

- [PyStaDa](https://pycoders.com/link/9146/web)
    + July 20, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9139/web)
    + July 20, 2022

- [PyLadies Dublin](https://pycoders.com/link/9152/web)
    + July 21, 2022

- [MadPUG](https://pycoders.com/link/9154/web)
    + July 21 to July 22, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅

![ACM-O](https://ipic.zoomquiet.top/2022-04-27-zshot%202022-04-27%2009.22.46.jpg)

(`是也乎:`


谈崩了, 之前通过 ACM 会员可以每年 $25 享受 O'REILLY 在线图书馆服务...现在没了

)

-----------------------------------------
# PS:

- 首发: [Issue 534 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-534.html)
- 修订: [issue-534.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-534.md)


## PPS:
> 不觉中蟒周刊快译已经到了第11个年头

开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
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

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF534D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF534D4Q90XdDA7g):



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





