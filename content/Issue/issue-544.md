Title: PyCoder 544
Slug: issue-544
Date: 2022-09-28 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.12 目标发布


原文: [PyCoder's Weekly - Issue #544](https://pycoders.com/issues/544)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220928 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220928 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python 实在是非开发人员的效率工具](https://pycoders.com/link/9606/web)
    + REAL PYTHON 
    + PODCAST

Are you interested in using Python in an industry outside of software development? Would adding a few custom software tools increase efficiency and make your coworkers’ jobs easier? This week on the show, Josh Burnett talks about using Python as a mechanical engineer.

(`是也乎:`

![Non-Developers](https://ipic.zoomquiet.top/2022-09-28-zshot%202022-09-28%2011.23.59.jpg)



)


- [基于 Python 应用程序的 Heroku 替代方案](https://pycoders.com/link/9581/web)
    + TESTDRIVEN.IO 
    + • Shared by Micheal Herman

Learn about alternatives to Heroku and their pros and cons. Platforms discussed include Digital Ocean, Google App Engine, AWS, Azure, PythonAnywhere, and half a dozen more.

(`是也乎:`

Heroku 实在构造的太方便了,
除非官方作死, 否则, 很难上手后迁移...

)

- [在 Kubernetes 上运行 Django](https://pycoders.com/link/9590/web)
    + MOHAMED M EL-KALIOBY

This in-depth, seven-part article covers all the ins-and-outs of getting Django running on Kubernetes in a Docker container.

- [Django REST 3.14 发布](https://pycoders.com/link/9613/web)
    + DJANGO-REST-FRAMEWORK.ORG

- [Pandas 1.5 发布](https://pycoders.com/link/9611/web)
    + PYDATA.ORG

(`是也乎:`

随着Python 本身的加速, Pandas 也将越来越快...

)


- [征集提案: Synthetic Data Dev Conference](https://pycoders.com/link/9578/web)
    + GRETEL.AI 
    + • Shared by Will Jennings

(`是也乎:`

元宇宙基础计算...

)


- [2022 年 Django 开发者调查发布](https://pycoders.com/link/9594/web)
    + DJANGO SOFTWARE FOUNDATION






-----------------------------------------
## 探讨/吐糟
> Discussions


- [你正在研究什么有趣的问题?](https://pycoders.com/link/9592/web)
    + HACKER NEWS

- [老化的程序员](https://pycoders.com/link/9599/web)
    + HACKER NEWS

(`是也乎:`


老程序猿曰...

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Python 3.12 目标: Faster-CPython Ideas Wiki](https://pycoders.com/link/9607/web)
    + GITHUB.COM/FASTER-CPYTHON

A summary of the goals for the Faster CPython initiative within the Python 3.12 release. Includes trace optimizations, shrinking object sizes, improving memory management overhead, and more. See also the associated 
[Workflow for 3.12 cycle](https://pycoders.com/link/9608/web) checklist.

(`是也乎:`


> Multi-core Python

正式提出了...

)


- [某 Python 安全修复程序破坏了/一些 Bignums](https://pycoders.com/link/9576/web)
    + JAKE EDGE

It was recently discovered that certain conversions between int and str had a denial of service capability. This was patched, but the patch itself has broken some use cases. Read on to learn more.





- [用 MkDocs 构建 Python 项目文档](https://pycoders.com/link/9589/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to build professional documentation for a Python package using MkDocs and mkdocstrings. These tools allow you to generate nice-looking and modern documentation from Markdown files and, more importantly, from your code’s docstrings.

(`是也乎:`

![MkDocs](https://ipic.zoomquiet.top/2022-09-28-zshot%202022-09-28%2010.38.23.jpg)

MkDocs 最大的好处就是不用在每篇文档顶部追加一堆 meta 声明;

)



- [Pandas 向下转换以提高内存使用效率](https://pycoders.com/link/9575/web)
    + PETROS DEMETRAKOPOULOS

When storing information in a Pandas DataFrame, you have control over what format it takes. In some cases, casting your data into a different format can make a big different on your memory footprint. Read on for three tips that may shrink your DataFrames.

- [什么时候在 Python 中使用省略号?](https://pycoders.com/link/9588/web)
    + REAL PYTHON

You may have seen three dots in Python scripts. Although this syntax may look odd, using an ellipsis is valid Python code. In this tutorial, you’ll learn when Python’s Ellipsis constant can come in handy for you.

(`是也乎:`


![Ellipsis](https://ipic.zoomquiet.top/2022-09-28-zshot%202022-09-28%2010.34.54.jpg)

> Ellipsis ...

竟然也是个标准语法了...

)


- [Python中的元编程](https://pycoders.com/link/9584/web)
    + IBM.COM

“Just like metadata is data about data, meta-programming is writing programs that manipulate programs.” Learn about the structures used to do meta-programming in Python and common use cases.


(`是也乎:`


> developer.ibm.com

嗯哼, 当年 Python 唯一咨询富集地(有中文),
另外一个就是 ActivePython 的用户论坛...



)


- [绩效测量的侵入性程序](https://pycoders.com/link/9603/web)
    + ITAMAR TURNER-TRAURING

Go beyond the capabilities of profilers by instrumenting your code to get more detailed performance information. This article shows several Python based techniques for measuring your speed.



- [到底 __name__ == "__main__" 在作什么?](https://pycoders.com/link/9610/web)
    + REAL PYTHON

In this tutorial, you’ll learn all about Python’s name-main idiom. You’ll learn what it does in Python, how it works, when to use it, when to avoid it, and how to refer to it.


(`是也乎:`

![__main__](https://ipic.zoomquiet.top/2022-09-28-zshot%202022-09-28%2010.29.15.jpg)

这梗太老...

![meme](https://files.realpython.com/media/namemain.19d27b02755e.a38f654f963f.jpg)

)


- [嗯哼? Python 的 self Argument?](https://pycoders.com/link/9605/web)
    + BETTERPROGRAMMING.PUB 
    + • Shared by Martin Heinz

Do you really know what the self method argument is in Python? Learn how it works under the covers and why it is needed in method signatures.


(`是也乎:`

self 这个迷惑性自指, 如果关注就会越陷深

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [rocketry: Python 的现代调度库](https://pycoders.com/link/9614/web)
    + GITHUB.COM/MIKSUS

(`是也乎:`

嗯哼? 很早推荐过...

![rocketry](https://ipic.zoomquiet.top/2022-09-28-zshot%202022-09-28%2011.39.58.jpg)

不能毫秒级控制...
)


- [cython-lint: Cython pyx File Linter](https://pycoders.com/link/9615/web)
    + GITHUB.COM/MARCOGORELLI 
    + • Shared by Marco Gorelli

- [Daft: 用于复杂数据的 Python DataFrame](https://pycoders.com/link/9612/web)
    + GITHUB.COM/EVENTUAL-INC

- [redframes: 用于 ML 的数据操作库](https://pycoders.com/link/9598/web)
    + GITHUB.COM/MAXHUMBER 
    + • Shared by Max

- [slack-machine: 可扩展的 Slack Bot 框架](https://pycoders.com/link/9604/web)
    + GITHUB.COM/DONDEBONAIR


(`是也乎:`

Slack 生态实在是赞...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyKla Monthly Meetup](https://pycoders.com/link/9577/web)
    + September 28, 2022
    + 乌干达

- [Python Meeting Düsseldorf](https://pycoders.com/link/9579/web)
    + September 28, 2022

- [Heidelberg Python Meetup](https://pycoders.com/link/9597/web)
    + September 28, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9595/web)
    + September 28, 2022

- [SPb Python Drinkup](https://pycoders.com/link/9591/web)
    + September 29, 2022

- [PyConEs](https://pycoders.com/link/9583/web)
    + September 30 to October 3, 2022





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

- 首发: [Issue 544 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-544.html)
- 修订: [issue-544.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-544.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF544D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF544D4Q90XdDA7g):



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





