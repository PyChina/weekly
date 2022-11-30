Title: PyCoder 553
Slug: issue-553
Date: 2022-11-30 11:42
Tags: Weekly,Python,pycoders,ZH


> 用 VSCode 折腾 Jupyter 的16个理由...需要嘛?


原文: [PyCoder's Weekly - Issue #553](https://pycoders.com/issues/553)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221130 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221130 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Microsoft Power BI 和 Python: 两个超级大国的结合](https://pycoders.com/link/9922/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to install and configure Microsoft Power BI to work with Python. Using Python, you’ll import data from a SQLite database, transform and augment your dataset with pandas, and visualize it with Matplotlib.


(`是也乎:`

![Power](https://ipic.zoomquiet.top/2022-11-30-zshot%202022-11-30%2009.16.53.jpg)


VSCode 绝对为是 M$ 中兴关键之举...

)

- [Python 中的并行嵌套 for-Loops](https://pycoders.com/link/9939/web)
    + JASON BROWNLEE

Nested for-loops often are an opportunity for parallel code. This article covers when it is a good idea to split them up and the variety of different parallel coding approaches you can use.


(`是也乎:`

值得收藏日用,一个多重循环,可以用这么多种姿势来完成,
感觉 Python 一直说的:"毎件事儿,总是有一种最靠谱姿势",好象有些站不住...

)


- [我们如何在数百种环境中快速运行测试](https://pycoders.com/link/9921/web)
    + ANTON PIRKER

Anton describes the test setup at Sentry and how they use both tox in parallel as well as GitHub actions to run a large test suite quickly.


(`是也乎:`

嗯哼? Sentry白女票党技巧?

)




-----------------------------------------
## 探讨/吐糟
> Discussions


- [Python 起源](https://pycoders.com/link/9928/web)
    + HACKER NEWS

This discussion is around the excellent article by Lambert Meertens called The Origins of Python that delves into Python’s history.


(`是也乎:`

老爹只是退休,又没死,已经开始立传了...
![Origins](https://ipic.zoomquiet.top/2022-11-30-zshot%202022-11-30%2009.23.48.jpg)

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 pyproject.toml 打包日常项目](https://pycoders.com/link/9933/web)
    + REAL PYTHON 
    + COURSE

In this Code Conversation video course, you’ll learn how to package your everyday projects with pyproject.toml. Playing on the same team as the import system means you can call your project from anywhere, ensure consistent imports, and have one file that’ll work for many build systems.

(`是也乎:`

统一在一个配置文件中当然有好处,
只是, 为什么是 .toml 以及为什么叫 pyprojrct ?

这种历史潮流的构建,才是大厂核心竞争力了

)



- [始终使用 `[closed, open)` 声明区间](https://pycoders.com/link/9940/web)
    + FERNANDO HURTADO CARDENAS

“Intervals or ranges pop-up everywhere in the programming world. The classic example is picking a start and end date, like you would when booking an AirBnB or a flight. Have you ever wondered why they are always implemented as [closed, open) as opposed to [closed, closed]?”

(`是也乎:`

等等 `[..)` 叕一个奇怪的语法?
直接打破了成对原则?

)




- [用 VS Code 开发 Jupyter 笔记本的 16 个理由](https://pycoders.com/link/9932/web)
    + CHRIS MOFFITT

“Visual Studio Code is one of the most popular text editors with a track record of continual improvements. One area where VS Code has been recently innovating is its Jupyter Notebook support.” Read on to see how this might help you.

(`是也乎:`

Jupyter 现在的问题不是在开发/调试阶段吧?
而是没有一个稳定靠谱的运行时框架?
可以不用修改直接使用 .ipynb 文件加载成项目长久运行?

)



- [Python 字节码解释](https://pycoders.com/link/9931/web)
    + MOSER MICHAEL

When a Python program is run, the interpreter first parses your code and checks for syntax errors, then it translates it into bytecode instructions. This article explains some of the features of Python bytecode.

- [plydata: Pandas 的管道](https://pycoders.com/link/9943/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

The plydata Python package enables you to use the pipe operator, ">>", to chain operations on a pandas dataframe. Read on to learn how to use it and how it compares to the equivalent operation in R.

(`是也乎:`

REPL 式 Pandas 使用界面?

不过,这种也很难阻止写出堆积很多的联合查询...

)


- [REPL 驱动开发](https://pycoders.com/link/9934/web)
    + DAVID VUJIC 
    + • Shared by David Vujic

REPL Driven Development is about fast feedback loops during development. It is not about typing code into a terminal window. David talks about this coding workflow and how it is similar to TDD.

(`是也乎:`

说反了,不是 TDD 向, 而是幸福向,
参考: [Glamorous Toolkit](https://gtoolkit.com/docs/start/)

如果一个语言生态,可以将开发/测试/运行/备份/迁移/存储/....
所有生命周期状态可以在一个交互界面中管理,那有多幸福?

)



- [Python JSONPath 示例](https://pycoders.com/link/9930/web)
    + SRINIVAS RAMAKRISHNA

JSONPath is an expression language that is used to parse the JSON data in Python, similar to XPath in XML. This article covers the basics of finding paths in JSON using the library.

(`是也乎:`

TOML 在兴起, TPath 已经在路上了..
不过, 为什么 XPath 一直想在各种场景中复活呢?

)



- [用 Docker-Compose 部署 Django、Celery、Redis 和 Postgres](https://pycoders.com/link/9941/web)
    + PIOTR PŁOŃSKI 
    + • Shared by Piotr Płoński

Deployments can be painful. This article describes one approach to deploying Django, Celery, Redis, and Postgres with docker-compose so you can reuse it in your app!

(`是也乎:`

`LDCRPN` ~ 追加 Linux 和 Nginx ,这就是最新 `LAMPs` 常用架构了...

不过,总是感觉哪儿里有不对...

)



- [揭秘 Python 中私有的、“受保护”的属性](https://pycoders.com/link/9935/web)
    + AMIR AFIANIAN 
    + • Shared by Amir Afianian

A guide to private and protected attributes in Python, learn all about when to use and when not to use leading underscores and double underscores (dunder).

(`是也乎:`

这么发展下去, Python 总有一天有能力控制所有变量所有权变迁过程的哪...

)


- [调查针对 FastAPI 的后门 PyPI 包](https://pycoders.com/link/9944/web)
    + TURCKHEIM 
    + & TAFANI-DEREEPER

Using an open source security scanner, the authors found a backdoored package on PyPI. Read on for details about how they found it and what it contained.



(`是也乎:`

Datadog 的软广, 不过, 的确点出了一个真实问题场景

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [quickadd: 解析自然语言时间和日期表达式](https://pycoders.com/link/9936/web)
    + GITHUB.COM/ACREOM

(`是也乎:`

也就对拼音语言有用, 怼上中文各种年号, 或是艳电那种阶段约定, 屎定了...

)


- [Polylith 架构的 Python 工具](https://pycoders.com/link/9919/web)
    + GITHUB.COM/DAVIDVUJIC • Shared by David Vujic

- [django-virtual-models: Django ORM 预取层](https://pycoders.com/link/9942/web)
    + GITHUB.COM/VINTASOFTWARE

(`是也乎:`


ORM 能复杂到 Django 这个地步也算是空前的了

)


- [Colossal-AI: 大模型时代的统一深度学习系统](https://pycoders.com/link/9937/web)
    + GITHUB.COM/HPCAITECH

- [pytorch-image-models: 模型、脚本、预训练权重](https://pycoders.com/link/9925/web)
    + GITHUB.COM/RWIGHTMAN

(`是也乎:`


pytorch 一直在发力

)






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [NZPUG-Auckland Coding Challenge “Office Hours”](https://pycoders.com/link/9926/web)
    + November 30, 2022

- [Deep Learning With PyTorch](https://pycoders.com/link/9945/web)
    + November 30, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9948/web)
    + November 30, 2022

- [PyDelhi User Group Meetup](https://pycoders.com/link/9947/web)
    + December 3, 2022

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/9950/web)
    + December 1, 2022






-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 553 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-553.html)
- 修订: [issue-553.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-553.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF553D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF553D4Q90XdDA7g):



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





