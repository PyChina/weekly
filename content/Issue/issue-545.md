Title: PyCoder 545
Slug: issue-545
Date: 2022-10-05 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 版 Rust/内置 linter clippy 来了


原文: [PyCoder's Weekly - Issue #545](https://pycoders.com/issues/545)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221005 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221005 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [用 Django Channels 和 WebSocket 构建实时聊天](https://pycoders.com/link/9635/web)
    + MUHAMMED ALI

Building stateful web applications can be tricky, unless you use a framework, of course. Django to the rescue! In this article, learn how to build a real-time chat app using Django Channels and WebSockets.

- [用 Python 生成二维码](https://pycoders.com/link/9648/web)
    + JERRY ZHU

QR codes are two dimensional bar codes that allow you to embed URLs in images. Learn how to make a QR code using the qrcode library.

(`是也乎:`

奇怪知识总是在增长

)


- [用 Django Ninja 构建鬼鬼祟祟的 REST API](https://pycoders.com/link/9646/web)
    + REAL PYTHON COURSE

In this video course, you’ll learn how to use Django Ninja, a FastAPI inspired tool for turning Django views in REST API endpoints. With Ninja, you can quickly build API endpoints.

(`是也乎:`


![Ninja](https://ipic.zoomquiet.top/2022-10-05-zshot%202022-10-05%2010.03.45.jpg)

)

-----------------------------------------
## 探讨/吐糟
> Discussions


- [如何修复 Python](https://pycoders.com/link/9650/web)
    + AL SWEIGART    

Al appears to be bored and decided to start a flame war. As his suggestions include 1-based indexing and using “x” instead of “*” for multiplication, he’s likely being sarcastic. The joy of text is you’re never quite sure.


(`是也乎:`

标准引战断言...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [PEP 698: 覆盖静态类型的装饰器](https://pycoders.com/link/9649/web)
    + PYTHON.ORG

This Python Enhancement Proposal describes the use of a new decorator, @override, which would be used as a type-hint for methods in a sub-class that override a parent’s method. This type hint would introduce a level of safety if the parent method is refactored without corresponding changes to the child method.


(`是也乎:`

引入一个新语法, 发现一类新问题, 然后再来一个新语法来防止...

嗯哼? 这个故事好象在哪儿听说过...
好象澳州原先没有猫...

)


- [5 种姿势定期嗯哼 Jupyter Notebooks](https://pycoders.com/link/9631/web)
    + PIOTR PŁOŃSKI 
    + • Shared by Piotr Płoński

A Jupyter Notebook is an excellent tool for creating computational documents. There is often a requirement to update the notebook’s results at a selected time interval and publish it to the rest of the team. Piotr summarizes five different approaches for Jupyter Notebook scheduling.


(`是也乎:`


基本上都是外部工具绕...

)


- [mypyc 探险](https://pycoders.com/link/9626/web)
    + STEVE BRAZIER

The type annotation tool, mypy comes with a compiler called mypyc which uses Python type hints to generate C-extensions automatically. This blog posting describes how Steve used it to compile some of his code, the problems he ran into, and how he fixed them.

- [弹性分布式系统](https://pycoders.com/link/9644/web)
    + GERGELY OROSZ

This blog posting contains a brief summary and then two chapters from the book “Understanding Distributed Systems” by Roberto Vitillo. It describes how to make distributed systems more resilient from both the client’s and server’s perspectives.

- [自定义 Python 字符串： str 与 UserString 继承](https://pycoders.com/link/9621/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to create custom string-like classes in Python by inheriting from the built-in str class or by subclassing UserString from the collections module.


(`是也乎:`

![UserString](https://ipic.zoomquiet.top/2022-10-05-zshot%202022-10-05%2009.53.48.jpg)
)


- [Django Apps 生产技巧](https://pycoders.com/link/9636/web)
    + RAUNAQ SINGH

This blog post describes seven concepts Django programmers should keep in mind when writing production ready code. Hints include information on custom user models, configuring Gunicorn, problems with serializers, and more.

- [在 KerasCV 中用  Stable Diffusion 生成图像](https://pycoders.com/link/9647/web)
    + CHOLLET, ET AL

Stable Diffusion is a powerful, open-source text-to-image generation model. This guide shows you how to generate novel images using the KerasCV Python interface.


(`是也乎:`


![KerasCV](https://ipic.zoomquiet.top/2022-10-05-zshot%202022-10-05%2009.51.56.jpg)

)


- [将 Python Web 应用程序部署为 AWS Lambda 函数](https://pycoders.com/link/9628/web)
    + SIMON WILLISON’

A step-by-step guide on how to deploy Python in the AWS Lambda environment. Details include managing dependencies and dealing with an ASGI application.




- [初学者的 Pytest](https://pycoders.com/link/9633/web)
    + ŠPELA GIACOMELLI 
    + • Shared by Michael Herman

This article introduces you to using pytest for testing Python code. Learn how to improve your development process and write better automated tests.





- [想代码更简洁? 这儿有六法则](https://pycoders.com/link/9624/web)
    + DAVIDAMOS.DEV

This article outlines six things every developer should keep in mind when coding, hopefully resulting in easy to read, more maintainable Python.



(`是也乎:`


![Cleaner](https://ipic.zoomquiet.top/2022-10-05-zshot%202022-10-05%2009.41.53.jpg)

事实反复证明, 程序猿开始文艺时, 
就没设计师什么事儿了


)



- [用 Python 和 Flask 开发 RESTful API](https://pycoders.com/link/9655/web)
    + KREBS & MARTINEZ 
    + • Shared by Juan Cruz Martinez

A step-by-step article that guides you through everything you need to know to write your first REST API using Flask. From installing the requirements, through mapping models, to implementing security.

(`是也乎:`


Flask 好象又突然积极起来

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [difftastic: A Structural Diff That Understands Syntax](https://pycoders.com/link/9653/web)
    + GITHUB.COM/WILFRED

- [minestrone: Search, Modify, and Parse Messy HTML](https://pycoders.com/link/9634/web)
    + GITHUB.COM/ADAMGHILL

(`是也乎:`

历史遗迹拯救机?

)


- [refurb: Refurbish and Modernize Python Codebases](https://pycoders.com/link/9651/web)
    + GITHUB.COM/DOSISOD


(`是也乎:`


PEP8 衍生工具?

```
$ refurb main.py
main.py:3:17 [FURB109]: Use `in (x, y, z)` instead of `in [x, y, z]`
main.py:4:5 [FURB101]: Use `y = Path(x).read_text()` instead of `with open(x, ...) as f: y = f.read()`
main.py:10:40 [FURB102]: Replace `x.startswith(y) or x.startswith(z)` with `x.startswith((y, z))`
main.py:16:9 [FURB105]: Use `print() instead of `print("")`
```

给出各种最新 Pythonic 式代码建议,
不动手, 算是优雅版 Black ?

> 很大程度上受到了 Rust 的内置 linter clippy 的启发.

)


- [isort: Sort Your Imports](https://pycoders.com/link/9642/web)
    + GITHUB.COM/PYCQA


(`是也乎:`

这种直接修改源代码的工具, 
总是感觉哪儿有危险...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [STL Python](https://pycoders.com/link/9632/web)
    + October 5, 2022
    + 圣路易斯

(`是也乎:`

就是那个反复出现在各种 SiFi 剧集中, 
西部拱门所在地;

)


- [Crafting Software](https://pycoders.com/link/9645/web)
    + October 5, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9625/web)
    + October 5, 2022

- [Smart Iterator Challenge (Week 2)](https://pycoders.com/link/9656/web)
    + October 8 to October 17, 2022

- [PyCon MEA @ Global DevSlam 2022](https://pycoders.com/link/9629/web)
    + October 10 to October 14, 2022

- [PyCon Ghana 2022](https://pycoders.com/link/9627/web)
    + October 13 to October 16, 2022

- [PyCon ZA 2022](https://pycoders.com/link/9643/web)
    + October 13 to October 15, 2022



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

- 首发: [Issue 545 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-545.html)
- 修订: [issue-545.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-545.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF545D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF545D4Q90XdDA7g):



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





