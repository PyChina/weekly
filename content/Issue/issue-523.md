Title: PyCoder 523
Slug: issue-523
Date: 2022-05-04 11:42
Tags: Weekly,Python,pycoders,ZH


> debugging 艺能


原文: [PyCoder's Weekly - Issue #523](https://pycoders.com/issues/523)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220504 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220504 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Dunder Methods 在 Python: 最丑的真棒酱](https://pycoders.com/link/8620/web)
    + JOHN LOCKWOOD

Double-underscore methods, also known as “dunder methods” or “magic methods” are an ugly way of bringing beauty to your code. Learn about constructors, __repr__, __str__, operator overloading, and getting your classes working with Python functions like len().

(`是也乎:`


致丑神招...

这其实是 老爹 设计减少自己工作量的好东西, 嘦必要时才用就对

)





- [为什么在 Python 中关闭文件很重要?](https://pycoders.com/link/8611/web)
    + REAL PYTHON

Model citizens use context managers to open and close file resources in Python, but have you ever wondered why it’s important to close files? In this tutorial, you’ll take a deep dive into the reasons why it’s important to close files and what can happen if you dont.

(`是也乎:`


![Important](https://ipic.zoomquiet.top/2022-05-04-zshot%202022-05-04%2011.11.58.jpg)


嘦不是一次性海量文件操作, 或是巨型上T级别的文件操作,
这𫚙就细节可以忽略...

)



- [当 Python 不可 Thread: 深入了解 GIL 的影响](https://pycoders.com/link/8594/web)
    + ITAMAR TURNER-TRAURING

Python’s Global Interpreter Lock (GIL) stops threads from running in parallel or concurrently. Learn how to determine the impact of the GIL on your code.

(`是也乎:`


娺一篇深入分析, 实话, 这可能是 老爹当年最灵光一闪的创造性创造了...

)



- [micro:bit 编辑器 Beta 3 发布](https://pycoders.com/link/8622/web)
    + MICROBIT.ORG

(`是也乎:`

BBC 在努力...
> ...Micro:bit 已被广泛利用到香港中小学的资讯科技课程中，亦被视为是正式课程里的一环

也可以证明, HK 至今也没阅读英联邦的自我定位...

)


- [2022 “Call for Code” 全球挑战赛接受参赛作品](https://pycoders.com/link/8602/web)
    + CALLFORCODE.ORG

- [Jupyter 社区研讨会: 征集提案](https://pycoders.com/link/8615/web)
    + JUPYTER.ORG

(`是也乎:`

是时候产品化/云原生化了...


)



-----------------------------------------
## 探讨/吐糟
> Discussions





- [Python 不应该是顶级编程语言](https://pycoders.com/link/8604/web)
    + HACKER NEWS

Discussion of the controversial article 
[Python Is Now Top Programming Language — But Shouldn’t Be](https://pycoders.com/link/8605/web)


(`是也乎:`


没有谁应该当老大, 得看时代/创始人/社区的努力...
不然为什么 C 一直是隐身 BOSS ?

以及 JS 已经是事实上的顶级语言了..

)



- [您何时会使用 Lambda 函数?](https://pycoders.com/link/8595/web)
    + REDDIT



(`是也乎:`


一般都是喝醉时...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [用 doctest 进行 Python 测试](https://pycoders.com/link/8593/web)
    + MIKE DRISCOLL

Python’s doctest module allows you to write unit tests through REPL-like sessions in your doc-strings. Learn how to write and execute doctest code. Also available in video.


(`是也乎:`


老姿势总是最优雅的, 只是不够工程化...

)


- [在 Python Requests 中处理重试](https://pycoders.com/link/8627/web)
    + MARKKU LEINIÖ 
    + • Shared by Markku Leiniö

When coding with requests and urllib3 you can automatically retry failed connections through the use of requests.adapters.HTTPAdapter and urllib3.Retry. Don’t code retry loops manually, learn how to take advantage of the features of the libraries.

(`是也乎:`

反"反爬虫"技艺...

)



- [理解训练测试拆分](https://pycoders.com/link/8601/web)
    + MICHAEL GALARNY 
    + • Shared by Michael Galarnyk

The Train-Test-Split methodology is useful for supervised machine learning with a given data set. It helps ensure that new data is more likely to be categorized correctly. Learn how to use it with Python and scikit-learn.

- [用户友好的 Django 应用程序的分页](https://pycoders.com/link/8628/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to serve paginated content in your Django apps. Using Django pagination can significantly improve your website’s performance and give your visitors a better user experience.


(`是也乎:`

![User-Friendly](https://ipic.zoomquiet.top/2022-05-04-zshot%202022-05-04%2011.03.16.jpg)

从此走上前端不归路...

)


- [Python 中的代码质量工具](https://pycoders.com/link/8612/web)
    + DOLLAR DHINGRA 
    + • Shared by Dollar Dhingra

The article describes what code quality means and introduces some cool tools to improve your Python, including a variety of linters, formatters, and IDE tools.


(`是也乎:`

可惜没有一个可以成为 KPI 的依据...

不过, isort 非常赞...

)


- [调试注意事项](https://pycoders.com/link/8616/web)
    + IONEL CRISTIAN MĂRIEȘ

All programmers have to learn how to do it, and like all skills it takes practice. Learn some hints and approaches to the bane of us all: debugging.


(`是也乎:`

调试才是编程本身, 
那些一次就运行成功的代码,
其实是在人脑中调试很多次了, 


)


- [Docker 容器中的 MicroPython](https://pycoders.com/link/8613/web)
    + BHAVESH KAKWANI

Want to play with MicroPython without a board? Learn how to use the Unix port of MicroPython in a Docker container to test out your code.

(`是也乎:`


![MicroPython](https://ipic.zoomquiet.top/2022-05-04-zshot%202022-05-04%2010.51.02.jpg)


嗯哼? 也就是说, 不用硬件就可以开始玩 MicroPython 了?

)



- [将 Julia 整合到 Python 程序中](https://pycoders.com/link/8610/web)
    + PETER BAUMGARTNER

Learn what you need to get Julia running inside your Python programs, using PyJulia, PyCall, and how to set up your environments.

(`是也乎:`


Julia 无论多大CUP, Python 温柔的包含进来就好...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [pet-python-startrek: 1977 Commodore PET Star Trek Remake](https://pycoders.com/link/8626/web)
    + GITHUB.COM/BLOGMYWIKI

- [MNE: Explore and Visualize Neurophysiological Data](https://pycoders.com/link/8623/web)
    + MNE.TOOLS

(`是也乎:`


![MNE](https://ipic.zoomquiet.top/2022-05-04-zshot%202022-05-04%2010.48.22.jpg)

淦, 脑神经运动可视化...

)



- [slipcover: Near Zero-Overhead Python Code Coverage Tracking](https://pycoders.com/link/8609/web)
    + GITHUB.COM/PLASMA-UMASS




- [exceptionite: Make Prettier Exceptions a Cinch](https://pycoders.com/link/8629/web)
    + GITHUB.COM/MASONITEFRAMEWORK


(`是也乎:`


![exceptionite](https://ipic.zoomquiet.top/2022-05-04-zshot%202022-05-04%2010.46.37.jpg)

同时支持终端与网页的运行时可视化分析

)


- [Real Time Multiplayer Bingo Game Using Django Channels](https://pycoders.com/link/8624/web)
    + GITHUB.COM/LEARNINGNOOBI


(`是也乎:`


不能支持游戏的框架不是好社区

)




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyCon US 2022](https://pycoders.com/link/8599/web)
    + April 27 to May 6, 2022

(`是也乎:`

今年老爹有大物释放了...应该

)


- [STL Python](https://pycoders.com/link/8600/web)
    + May 4, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8590/web)
    + May 4, 2022

- [Heidelberg Python Meetup](https://pycoders.com/link/8589/web)
    + May 4, 2022
    + 德国

- [Canberra Python Meetup](https://pycoders.com/link/8597/web)
    + May 5, 2022
    + 澳洲

- [PyCon Kenya Conference 2022](https://pycoders.com/link/8625/web)
    + May 6 to May 8, 2022
    + 非洲




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

- 首发: [Issue 523 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-523.html)
- 修订: [issue-523.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-523.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF523D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF523D4Q90XdDA7g):



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





