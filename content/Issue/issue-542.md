Title: PyCoder 542
Slug: issue-542
Date: 2022-09-13 11:42
Tags: Weekly,Python,pycoders,ZH


> Jupyter+git 问题已解决


原文: [PyCoder's Weekly - Issue #542](https://pycoders.com/issues/542)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220913 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220913 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [List Comprehensions Are More Powerful Than You Think](https://pycoders.com/link/9497/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

List comprehensions have a lot of depth. This article takes you beyond the basics and explains nested comprehensions, multiple conditionals, exceptions, breaking the loop, and more.


(`是也乎:`

这在 [Python一行流 (2021)](https://book.douban.com/subject/35602079/)
中进行了充分的讨论...


)


- [Can Amazon’s CodeWhisperer Write Better Python Than You?](https://pycoders.com/link/9523/web)
    + BRIAN TARBOX 
    + • Shared by Adam Buggia

Amazon’s CodeWhisperer is a machine-learning based coding assistant which is currently in beta. Learn about its capabilities and limitations.


(`是也乎:`

可惜是 AWS only 的东西...

)

- [Possible DoS Exposure in Large int to str Conversions](https://pycoders.com/link/9499/web)
    + GITHUB.COM/PYTHON

“A Denial Of Service (DoS) issue was identified in CPython because we use binary bignum’s for our int implementation. A huge integer will always consume a near-quadratic amount of CPU time in conversion to or from a base 10 (decimal) string with a large number of digits. No efficient algorithm exists to do otherwise.”




- [Django Bugfix Release: 4.1.1](https://pycoders.com/link/9486/web)
    + DJANGO SOFTWARE FOUNDATION

- [Python 3.10.7, 3.9.14, 3.8.14, and 3.7.14 Released](https://pycoders.com/link/9482/web)
    + CPYTHON DEV BLOG

- [TensorFlow 2.10 Released](https://pycoders.com/link/9514/web)
    + TENSORFLOW.ORG







-----------------------------------------
## 探讨/吐糟
> Discussions




- [PyPI Is Running a Survey on the State of Python Packaging](https://pycoders.com/link/9481/web)
    + HACKER NEWS

PyPI is running a survey on the state of packaging in Python. Fill in the survey and tell the world what you told them in the HN discussion.

(`是也乎:`

    399,738     projects 
    3,773,941   releases 
    6,697,875   files 
    622,018     users

)


- [Should PIP_REQUIRE_VIRTUALENV Be the Default in pip?](https://pycoders.com/link/9513/web)
    + PYTHON.ORG





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [HTML and CSS for Python Developers](https://pycoders.com/link/9492/web)
    + REAL PYTHON

There’s no way around HTML and CSS when you want to build web apps. Even if you’re not aiming to become a web developer, knowing the basics of HTML and CSS will help you understand the web better. In this tutorial, you’ll get an introduction to HTML and CSS for Python programmers.

(`是也乎:`


![CSS.py](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.14.03.jpg)

嗯哼? HTML 从来不是问题,
问题在 CSS...


)



- [Recursion in Python With Al Sweigart](https://pycoders.com/link/9478/web)
    + REAL PYTHON 
    + PODCAST

Have you wanted to understand recursion and how to use it in Python? Are you familiar with the call stack and how it relates to tracebacks? This week on the show, Al Sweigart talks about his new book, “The Recursive Book of Recursion.”


(`是也乎:`

![Al](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.13.25.jpg)

)


- [Bluetooth Your Old Speakers With a Raspberry Pi](https://pycoders.com/link/9502/web)
    + FREDERIC DANIS

This article describes how to take an old pair of PC speakers and make them usable with Bluetooth. Learn about the PipeWire library, how to configure your Raspberry Pi, and the short Python script you need to glue it all together.

(`是也乎:`

> speaker-agent.service

    [Unit]
    Description=Bluetooth speaker agent

    [Service]
    ExecStart=python speaker-agent.py

    [Install]
    WantedBy=default.target



)



- [The Jupyter+git Problem Is Now Solved](https://pycoders.com/link/9515/web)
    + JEREMY HOWARD

Git and Jupyter just don’t get along. Merge conflicts break things, but not anymore. The nbdev2 package provides tools to allow merges in your Jupyter notebook. This article explains the problem and how it was addressed.

(`是也乎:`

好消息 ;-)

)


- [Dangerous Pickles](https://pycoders.com/link/9488/web)
    + EVAN SANGALINE

A light introduction to the Python pickle protocol, the Pickle Machine, and constructing malicious pickles. Learn why your code shouldn’t trust arbitrary serialized objects and the dangers of pickle-bombs.

(`是也乎:`

泡菜炸弹...

推荐用其它安全替代比如: marshmallow, dill, pyro ...

不过, 其中只有 marshmallow 看起来最靠谱...

)


- [Swift Was Poised to Replace Python. Then It Tanked](https://pycoders.com/link/9516/web)
    + ARI JOURY

In the early days of Swift, its growth was matching that of Python, but then it leveled out. In this opinion piece, Ari discusses why he thinks Python is still going strong and why Swift is falling away.

(`是也乎:`


![Swift](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.07.10.jpg)

只能说, 努力过...

![Swift.py](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.07.48.jpg)

)

- [Fully-Typed Decorators With Optional Arguments](https://pycoders.com/link/9503/web)
    + LEMONFOLD.IO 
    + • Shared by Stefan Ulbrich

Type annotation for decorators can be a bit more challenging than regular functions, especially if they support optional keyword arguments. Learn how to type them so that they pass mypy’s strict mode.


(`是也乎:`

Rust 向发展?


)


- [Building Command Line Interfaces With argparse](https://pycoders.com/link/9504/web)
    + REAL PYTHON 
    + COURSE

In this step-by-step Python video course, you’ll learn how to take your command line Python scripts to the next level by adding a convenient command line interface that you can write with argparse.


(`是也乎:`

![CLI](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.04.37.jpg)

其实, invoke/click 之类框架比模块好用

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [django-functest: Helpers for Functional Tests in Django](https://pycoders.com/link/9520/web)
    + GITHUB.COM/DJANGO-FUNCTEST

- [Visual Python Tkinter GUI Creator](https://pycoders.com/link/9511/web)
    + VISUALTK.COM

(`是也乎:`


![UI](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.02.05.jpg)

![Code](https://ipic.zoomquiet.top/2022-09-14-zshot%202022-09-14%2010.02.10.jpg)

怎么说呢?
好象回到 Qt ...

)


- [django-htmx-patterns: Coding Patterns for Django & HTMX](https://pycoders.com/link/9475/web)
    + GITHUB.COM/SPOOKYLUKEY

- [docquery: Extract Information From Documents](https://pycoders.com/link/9485/web)
    + GITHUB.COM/IMPIRA

(`是也乎:`

OCR 方向...

)


- [Python Conference Calendar With Proposal Deadlines](https://pycoders.com/link/9525/web)
    + PYTHONDEADLIN.ES 
    + • Shared by Geir Arne Hjelle






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyHEP 2022](https://pycoders.com/link/9500/web)
    + September 12 to September 17, 2022

- [Hybrid Panel: CI Tools We Use at IndyPy](https://pycoders.com/link/9527/web)
    + September 13 from 7-9pm ET

- [Santa Cruz Python Meetup](https://pycoders.com/link/9490/web)
    + September 14, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9529/web)
    + September 14, 2022

- [Python Northwest](https://pycoders.com/link/9494/web)
    + September 15, 2022

- [PyLadies Dublin](https://pycoders.com/link/9477/web)
    + September 15, 2022

- [MadPUG](https://pycoders.com/link/9519/web)
    + September 15 to September 16, 2022

- [PyCon UK 2022](https://pycoders.com/link/9493/web)
    + September 16 to September 19, 2022








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

- 首发: [Issue 542 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-542.html)
- 修订: [issue-542.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-542.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF542D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF542D4Q90XdDA7g):



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





