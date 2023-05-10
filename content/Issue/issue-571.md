Title: 蠎周刊(PyCoder)571
Slug: issue-571
Date: 2023-04-05 11:42
Tags: Weekly,Python,pycoders,ZH


> PEP 582 (Python 本地包目录) 被拒绝


原文: [PyCoder's Weekly - Issue #571](https://pycoders.com/issues/571)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230405 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230405 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [用 Graphs 在 Python 中构建迷宫求解器](https://pycoders.com/link/10597/web)
    + REAL PYTHON

In this step-by-step project, you’ll build a maze solver in Python using graph algorithms from the NetworkX library. Along the way, you’ll design a binary file format for the maze, represent it in an object-oriented way, and visualize the solution using scalable vector graphics (SVG).

- [如何进行精彩的大会演讲](https://pycoders.com/link/10599/web)
    + SEBASTIAN WITOWSKI 
    + • Shared by Reka

Sebastian has spoken at over 15 major Python conferences around the world. He also gave a workshop organized by the EuroPython conference for beginner speakers. Here, he shares lots of tips around topics related to speaking: from the CfP to the Q&A.


(`是也乎:`

老话重谈...就像相声, 是值得反复打磨的,
不过, 优化的目的嫑忘记...

收集, 对比, 抽象我们自己看过所有技术分享中喜欢的就知道:
怎么说, PPT 如何组织, 多长时间, 声音/录像技术...
一切都不重要, 重要的是分享的内容是否有趣有用有种.

)


- [在 Python 中加速文本处理 (很难)](https://pycoders.com/link/10578/web)
    + ITAMAR TURNER-TRAURING

If you need to speed up string parsing and formatting in Python you have many choices. This article covers the uses of Cython, mypyc, Rust, and PyPy and how to choose between them.

- [Django 4.2 发布](https://pycoders.com/link/10606/web)
    + DJANGO SOFTWARE FOUNDATION

- [PEP 582 (Python 本地包目录) 被拒绝](https://pycoders.com/link/10587/web)
    + PYTHON.ORG


(`是也乎:`


这属于政治正确了...讨论了好几年...

)

- [想要举办 DjangoCon Europe 2024?](https://pycoders.com/link/10580/web)
    + DJANGO SOFTWARE FOUNDATION




-----------------------------------------
## 探讨/吐糟
> Discussions

- [PEP 204: Range Literals: Getting Closure](https://pycoders.com/link/10584/web)
    + PYTHON.ORG



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Pandas 中的 Inplace 何时更快?](https://pycoders.com/link/10581/web)
    + REKA HORVATH 
    + • Shared by Reka

Several methods for the Pandas DataFrame support an inplace argument. You can find quite contradicting advice around it online. Some describe it as “good practice”, the Pandas docs says “its use is discouraged”. This article explores when inplace might improve the performance indeed and when it’s better to avoid it.


(`是也乎:`

![Pandas](https://ipic.zoomquiet.top/2023-04-05-zshot%202023-04-05%2016.43.55.jpg)

)

- [Django: 所有模型管理类的参数化测试](https://pycoders.com/link/10583/web)
    + ADAM JOHNSON

“When you declare a Django ModelAdmin class, the built-in system checks ensure that various attributes are well-defined, using the right data types and values. But they can’t cover everything, because there is so much flexibility.” This article shows you how to better test your ModelAdmin code.



- [如何在 Starlette 中配置 Auth0](https://pycoders.com/link/10588/web)
    + SIDDHANT GOEL 
    + • Shared by Siddhant Goel

This post looks at how to use Auth0 as an identity management provider in Starlette applications. Auth0 provides a secure and scalable way to manage sensitive user data. This article describes how you can integrate it into your Starlette-powered backend.

- [ViperGPT: 通过 Python 执行进行推理的视觉推理](https://pycoders.com/link/10600/web)
    + COLUMBIA.EDU

ViperGPT is a framework that composes visual and language models into code that can be used to perform queries on images. The example shows an image of children with a pile of muffins and asks how many muffins each kid should get for it to be fair.

(`是也乎:`

巧妙哪...优化投喂 GPT 们之前的流程.

)


- [YAML: Python 丢失的电池](https://pycoders.com/link/10594/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn about working with YAML in Python. By the end of it, you’ll know about the available libraries, their strengths and weaknesses, and the advanced and potentially dangerous features of YAML.


(`是也乎:`

![YAML](https://ipic.zoomquiet.top/2023-04-05-zshot%202023-04-05%2016.32.49.jpg)

还是得说 TOML 好点儿

)


- [构建和分发用 Python 编写的 macOS 应用程序](https://pycoders.com/link/10592/web)
    + GLYPH LEFKOWITZ

If you’re writing for multiple platforms, Swift may not be your best choice. So how do you do Python applications on macOS? Read on for the latest update to this advice from Glyph.

(`是也乎:`

只是记要, 没有一个可参考的现成工程

)


- [Rust in Anger: 高性能 Web 应用程序](https://pycoders.com/link/10595/web)
    + NICOLÁS HATCHER

This article covers how to quickly call Rust from Python, TypeScript, or Node.js. It includes a sample application to demonstrate how to use cross language bindings.


(`是也乎:`

配套视频: [Build Universal Libraries with Rust - YouTube](https://www.youtube.com/watch?v=uKlHwko36c4 "Build Universal Libraries with Rust - YouTube")

以往 Python 是各种场景中的胶水语言,
现在 Rust 成为云时代的胶水语言了? 各种语言现有模块可以软实力来越方便的通过 WASM 直接在浏览器中运行... JS 的地位不保哪...

已经支持17种开发语言

)

- [如何提高 Git 的性能: 完整指南](https://pycoders.com/link/10596/web)
    + BRUNO BRITO

Is your Git monorepo getting slower and slower? Have a look at all the performance improvements that you can make to speed up your Git repository.

(`是也乎:`


![Tower](https://ipic.zoomquiet.top/2023-04-05-zshot%202023-04-05%2016.23.16.jpg)


Tower 的软广,但是, 这图是很够力了..

)


- [Django 中动态搜索的“无 JS”解决方案](https://pycoders.com/link/10603/web)
    + KÁTIA NAKAMURA

This article demonstrates how to do dynamic search results in Django using the HTMX library instead of JavaScript embedded in your page.

(`是也乎:`

Great 去 NodeJS 的确也是个倾向...

)


- [恶意行为者使用 Unicode 支持来逃避检测](https://pycoders.com/link/10602/web)
    + PHYLUM.IO

Phylum uncovers a threat actor taking advantage of how the Python interpreter handles Unicode to obfuscate their malware.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [Dynamic Prompts: 文本到图像提示工具包](https://pycoders.com/link/10577/web)
    + GITHUB.COM/ADIEYAL • Shared by Adi Eyal

(`是也乎:`

提示工程师工具箱已经开始增长了...

COP ~ 面向 ChatGPT 编程时代已经开始...

)


- [Python 绑定到 Rust UUID](https://pycoders.com/link/10575/web)
    + GITHUB.COM/AMINALAEE 
    + • Shared by A

(`是也乎:`

正好要用, 这比纯 Py 要来的安定团结的多;
就是不知道部署时是否流畅...
)

- [用于构建 Web 应用程序的 Python Web 框架](https://pycoders.com/link/10576/web)
    + MADHU.INK 
    + • Shared by Madhukumar Seshadri

(`是也乎:`

talkweb,talkback,talksql 又一个朴素的 web 应用框架

)


- [pair: GPT 结对编程的 REPL 环境](https://pycoders.com/link/10590/web)
    + GITHUB.COM/JIGGY-AI

- [Raspberry Pi 寻声机械狗](https://pycoders.com/link/10582/web)
    + SUNFOUNDER.COM


(`是也乎:`

![SunFounder](https://ipic.zoomquiet.top/2023-04-05-zshot%202023-04-05%2015.50.52.jpg)

真.手把手 教授如何构建一只声音响应机械狗,
使用超声波传感器进行测距...


)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [STL Python](https://pycoders.com/link/10591/web)
    + April 5, 2023

- [Heidelberg Python Meetup](https://pycoders.com/link/10601/web)
    + April 5, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10586/web)
    + April 5, 2023

- [Canberra Python Meetup](https://pycoders.com/link/10605/web)
    + April 6, 2023

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/10604/web)
    + April 6, 2023

- [PyCamp Spain 2023](https://pycoders.com/link/10585/web)
    + April 7 to April 11, 2023




-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 519](https://weekly.pychina.org/issue/issue-519.html)
- 2021: [蠎周刊 467](https://weekly.pychina.org/issue/issue-467.html)
    + [pythonista-weekly : Pyw 493](https://weekly.pychina.org/python-weekly/pyw-493.html)
- 2020: [蠎周刊 414](https://weekly.pychina.org/issue/issue-414.html)
    + [pythonista-weekly : Pyw 443](https://weekly.pychina.org/python-weekly/pyw-443.html)
- 2019: [蠎周刊 362](https://weekly.pychina.org/issue/issue-362.html)
    + [Postgres Weekly : Issue 229](https://weekly.pychina.org/pgweekly/pgw-229.html)
- 2018: [蠎加载 169](https://weekly.pychina.org/importpython/importpython-169.html)
- 2017: [蠎加载 119](https://weekly.pychina.org/importpython/importpython-119.html)
- 2016: [蠎周刊 206: Curry](https://weekly.pychina.org/issue/issue-206.html)
    + [蠎加载 67](https://weekly.pychina.org/importpython/importpython-67.html)
- 2015: [蠎周刊 160: 蛋](https://weekly.pychina.org/issue/issue-160.html)
    + [蠎加载 26](https://weekly.pychina.org/importpython/importpython-26.html)
- 2014: [蠎周刊 109: 揍要赢](https://weekly.pychina.org/issue/issue-109.html)
- 2013: 空缺
- 2012: [蠎周刊 8 ~ 蠎之禅](https://weekly.pychina.org/issue/issue-8.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...
- [Chaos42 - YouTube](https://www.youtube.com/watch?v=fPQ6piLqMXE&list=PLToFpvpg6EgRo6naYOp-BX4So-DxOCne8&index=1)
    + VLog
    + 恢复各种嗯哼...
- [42.zoomquiet.top](https://42.zoomquiet.top/)
    + 古早:周刊式分享
    + ...类似湾区日报




```
          _~^--~_
      \/ /  ☉ +  \ \/
        '_   ⏡   _'
        / '--~--' )

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 571 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-571.html)
- 修订: [issue-571.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-571.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

## PPS:
> 不觉中蟒周刊快译已经到了第10+2个年头

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

所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF571D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF571D4Q90XdDA7g):



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



