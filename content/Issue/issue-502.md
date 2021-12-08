Title: PyCoder 502
Slug: issue-502
Date: 2021-12-08 11:42
Tags: Weekly,Python,pycoders,ZH


> CPython 3\.10\.1 发布


原文: [PyCoder's Weekly - Issue #502](https://pycoders.com/issues/502)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211208 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211208 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Advent of Code: 用 Python 解决你的难题](https://pycoders.com/link/7577/web)
    + REAL PYTHON

Advent of Code is an online advent calendar that shares new programming puzzles each day from December 1st to the 25th. In this tutorial, you’ll learn why solving programming puzzles can be beneficial and how you can get started with Advent of Code using Python.


(`是也乎:`

![Puzzles](https://ipic.zoomquiet.top/2021-12-08-zshot%202021-12-08%2010.30.34.jpg)

)


- [各种语言的错误信息风格指南](https://pycoders.com/link/7564/web)
    + CARL FRIEDRICH BOLZ-TEREICK

“PyPy has been trying to produce good SyntaxErrors and other errors for a long time. CPython has also made an enormous push to improve its SyntaxErrors in the last few releases. These improvements are great, but the process feels somewhat arbitrary sometimes. To see what other languages are doing, I asked people on Twitter whether they know of error message style guides for other programming languages.”


(`是也乎:`

PyPy 比 CPython 更加关注这事儿

)

- [Python 中的二进制/字节和位运算符](https://pycoders.com/link/7558/web)
    + REAL PYTHON 
    + COURSE

In this course, you’ll learn how to use Python’s bitwise operators to manipulate individual bits of data at the most granular level. With the help of hands-on examples, you’ll see how you can apply bitmasks and overload bitwise operators to control binary data in your code.


(`是也乎:`

![Bitwise](https://ipic.zoomquiet.top/2021-12-08-zshot%202021-12-08%2010.29.56.jpg)

)


- [Django 4\.0 发行说明](https://pycoders.com/link/7565/web)
    + DJANGO SOFTWARE FOUNDATION

New built-in RedisCache backend, forms are now rendered using the template engine to enhance customization, Python standard library’s zoneinfo is now the default timezone implementation.

(`是也乎:`

zoneinfo ?
不是 UTC ?

)


- [A Message From the PSF’s Outgoing Executive Director](https://pycoders.com/link/7569/web)
    + PYTHON SOFTWARE FOUNDATION

- [CPython 3\.10\.1 发布](https://pycoders.com/link/7573/web)
    + CPYTHON DEV BLOG


(`是也乎:`

从 2.X 到 3.X 用了10年,
看起来, 从 3.X 到 4.X 用不了5年...

)




-----------------------------------------
## 探讨/吐糟
> Discussions



- [在字符串中 “交换” 单词/多字符 的最佳方法?](https://pycoders.com/link/7580/web)
    + STACK OVERFLOW

(`是也乎:`


简直就是 LISP/Elixir 的日常..

    def swap_words(s, x, y):
        return y.join(part.replace(y, x) for part in s.split(x))


)


- [你的 Python 坏习惯是什么?](https://pycoders.com/link/7563/web)
    + REDDIT

(`是也乎:`

可能就是到哪儿, 都想上 PyENV...

...[You aren't gonna need it \- Wikipedia](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

)


- [从 1991 年到 2006 年 Python 使用了多少? 做什么的?](https://pycoders.com/link/7581/web)
    + HACKER NEWS

(`是也乎:`

mailman/MoinMoin/...
YYdS

)





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 Python 中的漂亮打印美化数据结构展示](https://pycoders.com/link/7579/web)
    + REAL PYTHON

The pprint module, Python’s data pretty printer, is a useful part of the standard library. You can work with it for debugging data structures and increasing the readability of your output. In this tutorial, you’ll find that pprint is both straightforward to use and also highly customizable.


(`是也乎:`


虽然只是给程序猿看,
但是, 程序猿也是人, 值得越来越优美的对待...

![Prettify](https://ipic.zoomquiet.top/2021-12-08-zshot%202021-12-08%2009.37.36.jpg)

)


- [Jython 旧事\[2002\]](https://pycoders.com/link/7582/web)
    + JIM HUGUNIN

“The story of Jython begins one summer in Ashland, Oregon. I was juggling in a park behind a theater when I met Pavel Curtis, a scientist at Xerox PARC, who wanted to pass clubs. While we were juggling together he told me about a wonderful new programming language called Python. Writing code in Python felt like writing the sort of natural informal code that developers would use when they wanted to quickly share ideas. It was executable pseudo-code.”


(`是也乎:`

这不是悲伤故事, 只是无奈...
其实在 04年就尝试用 Jython 开发坦克大战游戏的;

果然还是硕士作品, 果然还是有 SUN 的身影...

)


- [与 Luciano Ramalho 讨论 Python 中类型提示/协议和鸭子类型](https://pycoders.com/link/7554/web)
    + REAL PYTHON PODCAST

There seem to be three kinds of Python developers: those unaware of type hints or have no opinion, ones that embrace them, and others who have an allergic reaction at the mention of them. Python is famously a dynamically typed language, but there are advantages to adding type hints to your code. This week on the show, it’s Luciano Ramalho discussing his recent talk titled, “Type hints, protocols, and good sense.”


(`是也乎:`


![Ducks](https://ipic.zoomquiet.top/2021-12-08-zshot%202021-12-08%2009.33.09.jpg)

鸭子/海象/...
Python 吞食的动物越来越多...

)


- [如何在 Python 中创建病毒?](https://pycoders.com/link/7574/web)
    + DAVIDE MASTROMATTEO 
    + • Shared by Davide

“I was relaxing on a beach during my summer leave when I received a mail from a reader that asked me if it is technically possible to write a virus using Python. The short answer: YES. The longer answer: yes, BUT…”

(`是也乎:`

不是, 好吧, 这的确要高级技巧...

而且最大渠道就是 PyPI...

)


- [为你的 Command\-Line\-Phobe CLI依赖症同事编写简单的 Python GUI](https://pycoders.com/link/7578/web)
    +  NASH REILLY

“These are some of the lessons I’ve learned on how to package rudimentary Python scripts into simple Windows GUIs for your […] coworkers to use.”

(`是也乎:`


两年前的分享了...
)


- [创建更好的火焰图](https://pycoders.com/link/7557/web)
    + ITAMAR TURNER-TRAURING

Flamegraphs are a great way to visualize performance and memory bottlenecks, but with a little tweaking, you can make them even more useful.

(`是也乎:`

火焰图的萌化...

)


- [Python 的 None 问题, 以及 Mypy 如何帮你搞掂](https://pycoders.com/link/7575/web)
    + JR HEARD

(`是也乎:`

None/null/NIL/...

零值一直是个问题

)







-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [emacs\-python\-coverage: 直接在 Emacs 中显示 Python 覆盖率信息](https://pycoders.com/link/7551/web)
    + GITHUB.COM/WBOLSTER


(`是也乎:`

Emace 和 Vim 宇宙中发生点儿什么都不奇怪...

)


- [pip\-audit: 审计 Python 环境和依赖树的已知漏洞](https://pycoders.com/link/7570/web)
    + GITHUB.COM/TRAILOFBITS

(`是也乎:`


    $ pip-audit
    Found 2 known vulnerabilities in 1 packages
    Name  Version ID             Fix Versions
    ----  ------- -------------- ------------
    Flask 0.5     PYSEC-2019-179 1.0
    Flask 0.5     PYSEC-2018-66  0.12.3


)


- [numpy\-financial: NumPy 中的财务函数](https://pycoders.com/link/7555/web)
    + NUMPY.ORG


(`是也乎:`

果然, 因为金融领域 Pythoneer 越来越多, 所以,,,

)

- [PyXIRR: 金融函数的集合](https://pycoders.com/link/7585/web)
    + GITHUB.COM/ANEXEN 
    + • Shared by Alexander


(`是也乎:`

等等, 这不是有专用库的...?

)


- [latexrun: 21 世纪的 LaTeX 包装器](https://pycoders.com/link/7552/web)
    + GITHUB.COM/ACLEMENTS


(`是也乎:`


![latexrun](https://ipic.zoomquiet.top/2021-12-08-zshot%202021-12-08%2008.56.30.jpg)

转换机制...
LaTeX 原本只是为写一本书, 而创建的排版语言,
现在变成了最高段位的独立出版工具集...

)


- [pkgversions: 在开发过程中更新 Python 包版本](https://pycoders.com/link/7560/web)
    + GITHUB.COM/HASII2011 
    + • Shared by Humberto Sanchez II

(`是也乎:`

叕一个包版本依赖管理工具...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Atlanta](https://pycoders.com/link/7586/web)
    + December 9, 2021

- [⋅ Python Miami](https://pycoders.com/link/7584/web)
    + December 11 to December 12, 2021

- [⋅ DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/7567/web)
    + December 11, 2021

(`是也乎:`

Pythonic 工程师, 当年俺用 `Pythoneers` 这词儿时,
都以为是个错写...

)


- [⋅ Edmonton Python User Group](https://pycoders.com/link/7561/web)
    + December 13, 2021

- [⋅ IndyPy Monthly Meetup](https://pycoders.com/link/7556/web)
    + December 14, 2021

- [⋅ TuPLE \(Tucson Python Language Enthusiasts\)](https://pycoders.com/link/7562/web)
    + December 14, 2021



- [⋅ Edmonton\.py: The Edmonton Python User Group](https://pycoders.com/link/7561/web)
    + December 14, 2021
    + 英国?




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 502 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-502.html)
- 修订: [issue-502.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-502.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF502D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF502D4Q90XdDA7g):



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





