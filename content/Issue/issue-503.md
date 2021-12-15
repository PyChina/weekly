Title: PyCoder 503
Slug: issue-503
Date: 2021-12-15 11:42
Tags: Weekly,Python,pycoders,ZH


> RIP:effbot/Fredrik Lundh 


原文: [PyCoder's Weekly - Issue #503](https://pycoders.com/issues/503)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211215 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211215 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python 特性小回顾](https://pycoders.com/link/7636/web)
    + BRETT CANNON

“To help those who wish for the ‘good old days’ of some older Python version, I thought I would write down a bunch of the major language features that were added in Python in reverse chronological order. Start from top and work your way down until you come across a feature you aren’t willing to give up. The Python version which has that feature is the version you would be okay going back to.”


(`是也乎:`


这几年
![Chronology](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.44.02.jpg)

Python 中追加的特性是过去30年追加的总合还要多吧?


)


- [在 Heroku 上托管您的 Django 项目](https://pycoders.com/link/7651/web)
    + REAL PYTHON 
    + COURSE

In this course, you’ll learn how to host your Django project in the cloud for free and with little hassle. You’ll use Heroku, which takes the burden of infrastructure management off your shoulders.


(`是也乎:`

Heroku 真良心, 
俺5年前部署的应用, 一直免费低频使用中,
除了唤醒时, 要等一下, 其它时刻都正常, 要知道是 Py 2.7.10 的脚本...

只是, 本身是闭源的, 规模运行时效能真比不上其它公有云,
作为 练习平台足够了

)


- [PyPI 用户反馈总结](https://pycoders.com/link/7629/web)
    + PYTHON SOFTWARE FOUNDATION

“The PSF conducted a series of three surveys to identify key user requirements that have not been addressed so far. We used this round of surveys to engage with the PyPI community and understand ways to support community needs better. This post summarizes the feedback we have received and key decisions we have made based on the feedback.”


(`是也乎:`


注意: 使用 blogspot 发布.



)


- [Python 核心开发者 Fredrik “effbot” Lundh 去世](https://pycoders.com/link/7648/web)
    + GUIDO VAN ROSSUM

“Fredrik was an early Python contributor (e.g. Elementtree and the re module) and his enthusiasm for the language and community were inspiring for all who encountered him or his work. He spent countless hours on comp.lang.python answering questions from newbies and advanced users alike.”

(`是也乎:`

呜呼: PIL 创始人走了,

这算是白发人送黑发人嘛?

Guido 老爹专门邮件悼念.

![Guido](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.40.31.jpg)

R.I.P

)



- [pytest\-7\.0\.0rc1 预发行版 已推出](https://pycoders.com/link/7655/web)
    + PYTEST.ORG

- [Python in Visual Studio Code – December 2021 Release](https://pycoders.com/link/7635/web)
    + SAVANNAH OSTROWSKI

(`是也乎:`

是的, 对 Python 2.7 有专门支持


)





-----------------------------------------
## 探讨/吐糟
> Discussions


- [多个列表一起就地排序](https://pycoders.com/link/7628/web)
    + STACK OVERFLOW

“I have lists a,b,c,… of equal length. I’d like to sort all of them the order obtained by sorting a.”

- [哪3个 Django 包是每个人都应该知道的?](https://pycoders.com/link/7641/web)
    + REDDIT

(`是也乎:`

各有心头好:

    Django cookiecutter
    Django Rest Framework
    Django Allauth

等等,  DRF 只是个包?好象是独立产品了吧?


)


- [曾研究过“银行 Python”系统. 唉嘛\. AMA\.](https://pycoders.com/link/7632/web)
    + REDDIT







-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 Python 解决代码迷题](https://pycoders.com/link/7638/web)
    + REAL PYTHON 
    + PODCAST

Are you ready to break open the first days of puzzles from the annual Advent of Code challenge? Advent of Code is an advent calendar of twenty-five programming puzzles published each December. Practicing solving puzzles is a great way to build your Python skills. This week on the show, we have previous guest and Real Python author Geir Arne Hjelle to discuss his recent article titled, “Advent of Code: Solving Your Puzzles With Python.”


(`是也乎:`


![PODCAST](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.32.37.jpg)

)


- [有关 Go 翻译注意事项 of Reposurgeon](https://pycoders.com/link/7637/web)
    + ERIC S. RAYMOND

“This is an experience report on a Python-to-Go translation of a program with significant complexity, written in attempted conformance with the Go community’s practice for grounding language enhancement requests not in it-would-be-nice-to-have abstractions but rather in a description of real-world problems.”



- [Java vs Python: 面向 Java 开发人员的 Python 基础](https://pycoders.com/link/7654/web)
    + REAL PYTHON

Are you an experienced Java developer who wants to know more about Python? In this tutorial, you’ll compare Java vs Python and get to know the similarities and differences between the languages. You’ll also learn how to figure out when Python is a good choice for your specific use cases.

(`是也乎:`

没什么可比的:

![vs](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.33.07.jpg)


想赚钱? 用 JAVA,
想快乐? 上 Python.

)



- [介绍堆栈图/Stack Graphs \(GitHub\)](https://pycoders.com/link/7627/web)
    + DOUGLAS CREAGER

“With stack graphs, we can generate code navigation data for a repository without requiring any configuration from the repository owner, and without tapping into a build process or other CI job. In this post, I’ll dig into how stack graphs work, and how they achieve these results.”

(`是也乎:`


![Stack](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.27.37.jpg)

嗯哼? GitHub 被 M$ 收了后, 越来越象一个科技公司了,
TOML 之后, 各种自动化代码工具都在折腾,
这种, 明显是给 企业版 github 先上的代码自动化分析图谱用的.
不是, 等等, 这是 Rust 开发的?
为毛首先分析对象是 Python 代码? 好象包含了什么重大暗示...

=> [stack\_graphs \- Rust](https://docs.rs/stack-graphs/0.3.0/stack_graphs/)

)

- [从面向对象的 Ruby 切换到面向过程的 Python](https://pycoders.com/link/7622/web)
    + NICOLAS ZERMATI

“At first sight, one could say that Ruby and Python are very similar, they’re both dynamic languages, they’re both multi-paradigm, object-oriented, and so on. There are subtle differences setting them more apart from each other than it might seem…”

(`是也乎:`

因为 Ruby 没更新了?

)


- [用 Matplotlib 在 Python 中模拟 3D 太阳系](https://pycoders.com/link/7624/web)
    + STEPHEN GRUPPETTA

In this article, you’ll simulate a 3D solar system in Python using the popular visualisation library Matplotlib. By the end of this article, you’ll be able to create your own 3D solar system in Python with as many suns and planets as you wish.


(`是也乎:`


淦...太南了, 这是不想依赖任何3D特效技术, 高精度控制三维示意生成哪...

![Matplotlib](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.25.00.jpg)

)

- [为毛你的 multiprocessing Pool 卡住了? \(It’s Full of Sharks\!\)](https://pycoders.com/link/7643/web)
    + ITAMAR TURNER-TRAURING

“On Linux, the default configuration of Python’s multiprocessing library can lead to deadlocks and brokenness. Learn why, and how to fix it.”

- [是时候停止使用 Python 3\.6](https://pycoders.com/link/7640/web)
    + ITAMAR TURNER-TRAURING

“Python 3.6 will stop getting security updates in December 2021. Given the existence of 3.7, 3.8, 3.9, and 3.10, you really should upgrade.”

(`是也乎:`

可 Python 2.7 依然无法放弃...

)


- [PyTorch vs TensorFlow in 2022](https://pycoders.com/link/7639/web)
    + RYAN O'CONNOR

Should you use PyTorch vs TensorFlow in 2022? This guide walks through both popular frameworks, and when to choose PyTorch vs TensorFlow.


(`是也乎:`

关键看谁的广告费用多了...

)


- [Poetry, FastAPI, and \(Beta\) 都在 PyCharm 2021\.3 支持远程开发了](https://pycoders.com/link/7619/web)
    + JETBRAINS
    + SPONSOR

This release brings long-awaited features, including out-of-the-box support for Poetry, the new FastAPI project type, beta support for remote development, and a new Jupyter notebook experience. Find out What’s New in PyCharm 2021.3

(`是也乎:`

开发 Python 真的要这么复杂的界面嘛?

)


- [Python 构建系统和 Gentoo Linux 的未来](https://pycoders.com/link/7623/web)
    + MICHAŁ GÓRNY

”[…] how the Python packaging changes are going to affect Gentoo, and what is my suggested plan on dealing with them.”

(`是也乎:`

这种 螃蟹 也真只有 Gentoo 敢吃,
当年能吃的 豆瓣, 现在...

)



- [负载均衡的  xdist](https://pycoders.com/link/7645/web)
    + NED BATCHELDER

A pytest plugin to evenly balance tests across xdist workers.

- [在 Git 历史记录中查看 Python 函数随时间的更动](https://pycoders.com/link/7646/web)
    + BHUPESH VARSHNEY


(`是也乎:`

git 从最初几个指令, 到现在, 简直了...
一个宇宙级别的工具生态..

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [Diagrams: 用 Python 代码绘制云系统架构](https://pycoders.com/link/7656/web)
    + MINGRAMMER.COM

(`是也乎:`

用过, 占面积太大,
只有少数云厂商的图标, 其它的都要自己追加...


![Diagrams](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.54.42.jpg)

)


- [Edifice: 声明式 UI 库](https://pycoders.com/link/7657/web)
    + PYEDIFICE.ORG

(`是也乎:`

嗯哼? 1.0 之前, 就别指望了...

![Edifice](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.05.39.jpg)

)

- [EasyAuth: 身份验证和授权令牌服务器](https://pycoders.com/link/7652/web)
    + GITHUB.COM/CODEMATION 
    + • Shared by Joshua Jamison

(`是也乎:`

之前 SSO 还得考虑权限管理,
现在有单纯的身份检验, 其它的不管, 也是种解决.

![EasyAuth](https://ipic.zoomquiet.top/2021-12-15-zshot%202021-12-15%2009.04.54.jpg)

logo 走心了

)


- [dbt\-coverage: DBT 项目的文档和测试覆盖率](https://pycoders.com/link/7634/web)
    + GITHUB.COM/SLIDOAPP 
    + • Shared by Marek Suppa






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ PyData Bristol Meetup](https://pycoders.com/link/7625/web)
    + December 16, 2021

- [⋅ Python Northwest](https://pycoders.com/link/7647/web)
    + December 16, 2021

- [⋅ PyLadies Dublin](https://pycoders.com/link/7653/web)
    + December 16, 2021



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅
- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 503 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-503.html)
- 修订: [issue-503.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-503.md)


## PPS:
> 不觉中蟒周刊快译已经到了第10个年头

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF503D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF503D4Q90XdDA7g):



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





