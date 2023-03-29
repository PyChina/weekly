Title: 蠎周刊(PyCoder)570
Slug: issue-570
Date: 2023-03-29 11:42
Tags: Weekly,Python,pycoders,ZH


> ChatGPT 中断


原文: [PyCoder's Weekly - Issue #570](https://pycoders.com/issues/570)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230329 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230329 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [四年 Python 编程的经验教训](https://pycoders.com/link/10565/web)
    + REAL PYTHON 
    + PODCAST

What are the core lessons you’ve learned along your Python development journey? What are key takeaways you would share with new users of the language? This week on the show, Duarte Oliveira e Carmo is here to discuss his recent talk, “Four Years of Python.”


(`是也乎:`


![Learned](https://ipic.zoomquiet.top/2023-03-29-zshot%202023-03-29%2010.11.34.jpg)


意大利 PyCon 的背景故事...

)

- [用 Pydantic 进行数据建模、解析和验证](https://pycoders.com/link/10554/web)
    + SAMEER SHUKLA 
    + • Shared by Sameer Shukla

Pydantic is a Python library that provides data validation and settings management using Python type annotations. It allows developers to define a schema for their data, which includes the expected data types, default values, and validation rules.

- [ChatGPT 中断: 这是发生了什么](https://pycoders.com/link/10553/web)
    + OPENAI.COM

On March 20th ChatGPT had an outage. It was caused by an asyncio redis-py client bug and also resulted in a data leak. Read more for details.

(`是也乎:`

暗网的自觉行动?

)



- [Docker 不再取消免费团队计划](https://pycoders.com/link/10561/web)
    + DOCKER.COM

(`是也乎:`

看来还得等等, 看看后真相是什么

)


- [GitHub 更新了他们的 RSA SSH 主机密钥](https://pycoders.com/link/10556/web)
    + GITHUB

- [The Python Package Index 发布了一个博客](https://pycoders.com/link/10550/web)
    + PYPI.ORG

- [Django 4.2 Release Candidate 1 发布](https://pycoders.com/link/10571/web)
    + DJANGO SOFTWARE FOUNDATION



-----------------------------------------
## 探讨/吐糟
> Discussions

None


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [在 Django 禁止 1+N ](https://pycoders.com/link/10563/web)
    + ALEXANDER SCHEPANOVSKI

The 1+N database anti-pattern is common: fetch some rows from the database then re-fetch specific rows to get all the items. An ORM can hide this away and make you not realize it is happening. This article talks about how to stop it in Django. With added meta-bonus: he links to how he attempted to write the article with ChatGPT.


(`是也乎:`


ORM 毕竟不是编译器, 最大的问题就是隐藏了问题...

)


- [Deep Neural Nets: 33 年前和 33 年后](https://pycoders.com/link/10539/web)
    + ANDREJ KARPATHY

This article examines the original paper that proposed back propagation neural nets and relates what has changed and what is the same. Using that knowledge, it looks forward to what neural nets may be able to do decades from now. Includes accompanying code samples.


(`是也乎:`

和芯片制造一样, 没有几十年的持续投入,
随便炼点儿土钢, 不顶用的...

)



- [Python 和 No-async async](https://pycoders.com/link/10557/web)
    + WILL MCGUGAN

“A (reasonable) criticism of async is that it tends to proliferate in your code. In order to await something, your functions must be async all the way up the call-stack. Textual is an async framework, but doesn’t require the app developer to use the async.” Learn how Textual accomplishes async-agnosticism.

- [reduce(): 单一 Python 函数的强大功能](https://pycoders.com/link/10559/web)
    + MARTIN HEINZ

“While Python is not a pure functional programming language, you still can do a lot of functional programming in it. In fact, just one function - reduce() - can do most of it.” This article introduces you to reduce().

(`是也乎:`


```python
from functools import reduce
import operator

# Signature:
reduce(function, iterable[, initializer])

# Factorial
reduce(lambda x, y: y*x, range(1, 6), 1)
reduce(operator.mul, range(1, 6))
(((((1 * 1) * 2) * 3) * 4) * 5)
# 120
```

没错瞬间变成 LISP 的法宝


)



- [什么时候应该在 Python 中使用 .__repr__() 与 .__str__()?](https://pycoders.com/link/10548/web)
    + REAL PYTHON

In this tutorial, you’ll learn the difference between the string representations returned by .__repr__() vs .__str__() and understand how to use them effectively in classes that you define.


(`是也乎:`

![__repr__](https://ipic.zoomquiet.top/2023-03-29-zshot%202023-03-29%2010.00.30.jpg)


都是渊源的函数

)


- [将 TOML 用于 .env 文件?](https://pycoders.com/link/10545/web)
    + BRETT CANNON

Using .env files to specify configuration environments can be handy, but problematic when it comes to multiple platforms. Some toolsets are starting to explore the use of TOML instead.

(`是也乎:`

这才是趋势哪...

.toml.env 就好

)


- [开发者营销](https://pycoders.com/link/10541/web)
    + ADAM HILL

A few simple steps can make all the difference in whether your project gets noticed. This article is about Django projects, but most of the advice applies across all code bases.

- [在只读 Docker 容器中运行 Flask 服务器](https://pycoders.com/link/10560/web)
    + JON JAGGER

Learn how to run a Python server inside a read-only Docker container and how to pre-bundle the SCSS and JS files in a separate step.


(`是也乎:`

容器是个好想法, 但是, 用起来真心没有 BSD 的 jail 简洁;

)


- [高效 Python 程序员的 VSCode 快捷方式](https://pycoders.com/link/10540/web)
    + RODRIGO GIRÃO SERRÃO

Learn keyboard shortcuts that will make you a more efficient and productive Python programmer with VS Code.

- [用 OpenAI 和 DALL·E 2 生成图像](https://pycoders.com/link/10570/web)
    + IDOWU OMISOLA

Learn how to use Python to interface with OpenAI’s API to do image generation.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [alpaca-lora: Instruct-Tune LLaMA 文本模型](https://pycoders.com/link/10547/web)
    + GITHUB.COM/CHRIS-ALEXIUK

- [workedon: 从 Shell 跟踪您的工作](https://pycoders.com/link/10551/web)
    + GITHUB.COM/VISESHRP 
    + • Shared by Visesh Prasad

(`是也乎:`

所以, 英文就应该是万事万物的指令层?

这等于将以往精确的 CLI 工具参数, 变成了自然语言陈述...

)


- [chatblade: 用于 ChatGPT 的 CLI 瑞士军刀](https://pycoders.com/link/10542/web)
    + GITHUB.COM/NPIV

(`是也乎:`

应该是专门训练一个 CLI 专家模型

)


- [pooch: 获取数据文件的朋友](https://pycoders.com/link/10543/web)
    + GITHUB.COM/FATIANDO

- [nicegui: 用 Python 创建基于 Web 的 UI](https://pycoders.com/link/10549/web)
    + GITHUB.COM/ZAUBERZEUG



(`是也乎:`

![nicegui](https://ipic.zoomquiet.top/2023-03-29-zshot%202023-03-29%2009.19.46.jpg)


叕一个 web-based UI 框架,
只是, 这只已经发布到 1.0 版本, 可以尝试用了...

专注自动生成 UI , 而没考虑跨平台应用编译, 从而足够简洁.

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Heidelberg Python Meetup](https://pycoders.com/link/10552/web)
    + March 29, 2023

- [PyStaDa](https://pycoders.com/link/10567/web)
    + March 29, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10555/web)
    + March 29, 2023

- [SPb Python Drinkup](https://pycoders.com/link/10566/web)
    + March 30, 2023

- [PyTexas 2023](https://pycoders.com/link/10544/web)
    + April 1 to April 3, 2023

- [Melbourne Python Users Group, Australia](https://pycoders.com/link/10569/web)
    + April 3, 2023



-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 518](https://weekly.pychina.org/issue/issue-518.html)
- 2021: [蠎周刊 466](https://weekly.pychina.org/issue/issue-466.html)
    + [pythonista-weekly : Pyw 492](https://weekly.pychina.org/python-weekly/pyw-492.html)
- 2020: [蠎周刊 414](https://weekly.pychina.org/issue/issue-414.html)
- 2019: [蠎周刊 361](https://weekly.pychina.org/issue/issue-361.html)
- 2018: [蠎加载 168](https://weekly.pychina.org/importpython/importpython-168.html)
- 2017: [蠎加载 117](https://weekly.pychina.org/importpython/importpython-117.html)
- 2016: [蠎加载 66](https://weekly.pychina.org/importpython/importpython-66.html)
- 2015: [蠎周刊 159: Tapas](https://weekly.pychina.org/issue/issue-159.html)
- 2014: [蠎周刊 108: Rift](https://weekly.pychina.org/issue/issue-108.html)
- 2013: 空缺
- 2012: [蠎周刊 7 ~ __dunder__](https://weekly.pychina.org/issue/issue-7.html)


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

- 首发: [Issue 570 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-570.html)
- 修订: [issue-570.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-570.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF570D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF570D4Q90XdDA7g):



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



