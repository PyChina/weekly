Title: PyCoder 525
Slug: issue-525
Date: 2022-05-18 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.11.0b1 发布了


原文: [PyCoder's Weekly - Issue #525](https://pycoders.com/issues/525)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220518 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220518 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python’s min() and max(): 查找最小值和最大值](https://pycoders.com/link/8694/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use Python’s built-in min() and max() functions to find the smallest and largest values. You’ll also learn how to modify their standard behavior by providing a suitable key function. Finally, you’ll code a few practical examples of using min() and max().

(`是也乎:`


Python 的内建函式, 其实非常实用了...

![min,max](https://ipic.zoomquiet.top/2022-05-18-zshot%202022-05-18%2010.38.04.jpg)

)



- [用 django-rich 进行测试](https://pycoders.com/link/8709/web)
    + OKKEN, 
    + JOHNSON, 
    + & SMITH 
    + PODCAST
The django-rich library adds color and formatting to Django management commands, including colorized tracebacks. Make your debugging and testing more visual.


- [Analyze Code-Level Performance Across Your app’s Environment With Minimal Performance Overhead](https://pycoders.com/link/8731/web)
    + DATADOG
    + SPONSOR

Datadog’s profiler allows you to capture code profiles for all of your production instances. Compare those profiles in the profile comparison view to see how the performance of your code changes over time. You can quantify the changes you’ve made to fix a bottleneck. 
[Analyze Code-Level Performance Across Your app’s Environment With Minimal Performance Overhead](https://pycoders.com/link/8731/web)

(`是也乎:`

FaaS ~ 功能即服务 的典范...

)

- [维护良好的测试/新依赖的 12 个问题](https://pycoders.com/link/8728/web)
    + ADAM JOHNSON

There is lots of openly available code out there, but how do you know if you should build a dependency on some random coder’s package? 12 Questions you should ask yourself before using a library.

- [DjangoCon Europe 2022 征集提案](https://pycoders.com/link/8714/web)
    + DJANGOCON.EU

- [DjangoCon US 2022 提案征集](https://pycoders.com/link/8729/web)
    + PRETALX.COM

- [Python 发布 Python 3.11.0b1](https://pycoders.com/link/8715/web)
    + PYTHON.ORG

- [Python 在 Visual Studio Code: May 2022 发布](https://pycoders.com/link/8692/web)
    + MICROSOFT.COM

(`是也乎:`

越来越重了, 感觉在 VSCode 中叕嵌入了一个 XP 系统...

)


-----------------------------------------
## 探讨/吐糟
> Discussions



- [Python 语言峰会: 没有 GIL 的 Python](https://pycoders.com/link/8702/web)
    + HACKER NEWS

What’s a language summit without a conversation about the GIL? This HN discussion is all about the 
[“nogil” conversation at the 2022 summit](https://pycoders.com/link/8717/web)



- [你最常使用哪些 Python 包?](https://pycoders.com/link/8725/web)
    + MIKE DRISCOLL

(`是也乎:`


俺这儿是 pp

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [用 Heroku 部署 Flask 应用程序](https://pycoders.com/link/8711/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to create a Python Flask example web application and deploy it using Heroku. You’ll also use Git to track changes to the code, and you’ll configure a deployment workflow with different environments for staging and production.

(`是也乎:`


![Flask](https://ipic.zoomquiet.top/2022-05-18-zshot%202022-05-18%2010.31.52.jpg)

Heroku 算是 ServerLess 鼻祖...
可惜...

)


- [Python 装饰器模式](https://pycoders.com/link/8719/web)
    + MARTON TRENCSENI

Decorators are a way of wrapping functions around functions, they’re a common technique for providing pre- and post-conditions on your code. Learn about the different ways decorators get invoked and how to write each pattern.



- [介绍 Python 中的线性规划](https://pycoders.com/link/8697/web)
    + MAXIME LABONNE

Linear programming is a technique in mathematics for optimizing multi-variable problems. This article introduces you to the world of linear programming and some Python libraries you can use to solve these kinds of problems.


(`是也乎:`

高含量 emoji 技术文章...

)


- [Gevent 性能](https://pycoders.com/link/8710/web)
    + ROY WILLIAMS

Gevent is a co-routine based networking library who’s sweet spot for performance is network-bound workloads. Learn how gevent allows you to efficiently interleave other CPU work while waiting on the network for results.


(`是也乎:`

当年 SCGI 一堆实现

)



- [REPL Python Programming and Debugging With IPython](https://pycoders.com/link/8704/web)
    + LUKE PLANT

IPython is a powerful alternative to the built-in REPL. Learn how to use it for exploratory programming and debugging, including using it in the Django shell.


(`是也乎:`


如果习惯了, 在 `IPy[:]` 中调试是很爽,
只是, 得先熟悉常用快捷键, 以及设计好

)


- [Profiling and Analyzing Performance of Python Programs](https://pycoders.com/link/8727/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

The tools and techniques for finding all the bottlenecks in your Python programs and fixing them, fast. Includes info on cProfile, py-spy, py-heat, and more.

- [How to Code a Blockchain in 6 Steps](https://pycoders.com/link/8693/web)
    + ARI COHEN

The best way to understand blockchains is to see one in action , or better yet, to build one. Learn how to use Python and hashlib to create your own.

(`是也乎:`

手工创建一条 BlockChain , 当然没有任何功能...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [ads: Store Data in Soundwaves](https://pycoders.com/link/8712/web)
    + GITHUB.COM/STACKBUFFER

(`是也乎:`

数据可以嵌入图片中, 当然也可以嵌入声波中...

)


- [TatSu: Generate Python Parsers From EBNF Grammars](https://pycoders.com/link/8724/web)
    + GITHUB.COM/NEOGENY


(`是也乎:`


[neogeny/TatSu: 竜 TatSu generates Python parsers from grammars in a variation of EBNF](https://github.com/neogeny/TatSu)



)

- [woodwork: Data Typing Namespace for Many ML Tools](https://pycoders.com/link/8700/web)
    + GITHUB.COM/ALTERYX

(`是也乎:`

和骨科类似...都是 木匠活儿

)


- [pony: Pony Object Relational Mapper](https://pycoders.com/link/8695/web)
    + GITHUB.COM/PONYORM

(`是也乎:`

pony 马一定很高兴...
)


- [open-data-anonymizer: Data Anonymization & Masking](https://pycoders.com/link/8716/web)
    + GITHUB.COM/ARTLABSS



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [PiterPy Breakfast](https://pycoders.com/link/8706/web)
    + May 18, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8698/web)
    + May 18, 2022

- [PyData Bristol Meetup](https://pycoders.com/link/8718/web)
    + May 19, 2022

- [PyLadies Dublin](https://pycoders.com/link/8707/web)
    + May 19, 2022

- [Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/8720/web)
    + May 20, 2022

- [Django Girls Malabo](https://pycoders.com/link/8703/web)
    + May 21 to May 22, 2022

(`是也乎:`

PyLaidies 的竞争品牌活动,
可惜老爹不喜欢?

)

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

- 首发: [Issue 525 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-525.html)
- 修订: [issue-525.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-525.md)


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

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF525D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF525D4Q90XdDA7g):



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





