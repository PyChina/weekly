Title: 蠎周刊(PyCoder)574
Slug: issue-574
Date: 2023-04-26 11:42
Tags: Weekly,Python,pycoders,ZH


> PyPI叕开始整治...


原文: [PyCoder's Weekly - Issue #574](https://pycoders.com/issues/574)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230426 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230426 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------


- [PyPI 引入 "可信发布者""](https://pycoders.com/link/10713/web)
    + PYPI.ORG

PyPI package maintainers can adopt a new, more secure “OIDC authenticated” publishing method that does not require long-lived passwords or API tokens to be shared with external systems.

- [什么是 Python Namespace Package, 有什么用?](https://pycoders.com/link/10687/web)
    + REAL PYTHON

In this tutorial, you’ll be exploring Python namespace packages: what they are, what they’re for, and how you can use them in your package systems. Along the way, you’ll create your own set of namespace packages and explore how you might be able to use them in your own projects.

(`是也乎:`

叕是一个传统艺能...只有代码足够大时, 才有感觉

)



- [本书 ChatGPT-增强式 Python REPL](https://pycoders.com/link/10694/web)
    + LOGAN MORTIMER

This blog shows how Logan built a Python REPL augmented with ChatGPT. It details the application itself as well as speculating on software engineering patterns that might emerge in systems built on Large Language Models (LLMs).

- [Python 3.10 运行时 在 AWS Lambda 已支持](https://pycoders.com/link/10704/web)
    + AMAZON.COM


(`是也乎:`

AliYUN 早已公测 3.11 的了...
看来各家对安全的定义果断不同;

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [PEP 707: __exit__ and __aexit__ 的简化签名](https://pycoders.com/link/10714/web)
    + PYTHON.ORG

- [思路: 在 for 循环中允许理解语法 for](https://pycoders.com/link/10712/web)
    + PYTHON.ORG

(`是也乎:`

for 的表达式化?

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 中的依赖注入](https://pycoders.com/link/10707/web)
    + PATRICK KALKMAN

“Dependency Injection (DI) is a design pattern that encourages loose coupling, maintainability, and testability within software applications.” Though more often associated with statically typed languages, the pattern can be applied with Python.




- [用 Pre-Commit 改进你的代码](https://pycoders.com/link/10711/web)
    + RASUL KIREEV

This article covers a variety of tools you can attach to your repo’s pre-commit hook to validate your code. Although the article is from a Django perspective, all but one of the tools covered is Django-agnostic.



(`是也乎:`

淦, 值得每个团队本地都部署一致上;
不过, VSCode 配套下, 每次 保存 时就激活更加效率?

)

- [在 Python asyncio 中限制 Concurrency](https://pycoders.com/link/10705/web)
    + LEMON24

This article shows you how to do rate limiting when dealing with repeated tasks within asyncio. It uses a thread pool and imap_unordered() to show you why the answer may not always be to use a Semaphore.




- [使用 sum() 进行 Pythonic 式求和](https://pycoders.com/link/10706/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to use Python’s sum() function to add numeric values together. You’ll also learn how to concatenate sequences, such as lists and tuples, using sum().

(`是也乎:`

![sum](https://ipic.zoomquiet.top/2023-04-26-zshot%202023-04-26%2011.22.25.jpg)


信内建得永生

)


- [Google 的 Assured OSS Python Packages](https://pycoders.com/link/10688/web)
    + GOOGLE.COM

Google publishes a list of the Open Source packages it uses and secures within its own software supply chain. The list is made public so you can take advantage of their assessment.

(`是也乎:`

不是, 这是结局没有过程, 对于其它团队有什么参考价值?

不过, 可以肯定的是, 自行开发的不多,
加入上游开发的也不多..

)


- [在 Pandas 2.0 中读取 CSV 文件的最快方法](https://pycoders.com/link/10709/web)
    + FINN ANDERSEN

The fastest way to read a CSV file into a Pandas DataFrame isn’t pd.read_csv(). This article shows you the alternative and how the result was bench-marked.

(`是也乎:`

除非数量大到一定程度...
否则...

)


- [使用 XAR 构建可重现的 Python 环境](https://pycoders.com/link/10717/web)
    + PAVEL SENCHANKA

XAR is an archiving format that can contain a tree of files. This article details how they can be used to package Python environments for deploy-ability.

(`是也乎:`

OCaml 重度用户为 Python 工程可复现构建的工具...

)


- [Django 性能优化技巧](https://pycoders.com/link/10693/web)
    + MICHAEL HERMAN 
    + • Shared by Michael Herman

This article looks at where potential performance issues can occur in a Django application and how to address them in order to speed up your app.


(`是也乎:`

先功能后治理...

)


- [Python 包: 数据人员入门](https://pycoders.com/link/10695/web)
    + ELLIOT GUNN

This article introduces you to the concept of Python modules and packages. How and where you use them and why you should.


(`是也乎:`

老爹当年一闪念,
今天慢慢深挖掘

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [用户空间的 Mouse 滚轮加速](https://pycoders.com/link/10691/web)
    + GITHUB.COM/ALBERTZ


(`是也乎:`
这个很硬核了...加速 mouse ...

)

- [faiss: 密集向量的相似性搜索和聚类](https://pycoders.com/link/10699/web)
    + GITHUB.COM/FACEBOOKRESEARCH

- [trrex: 使用正则表达式进行高效的字符串匹配](https://pycoders.com/link/10708/web)
    + GITHUB.COM/MESEJO 
    + • Shared by Daniel Mesejo

(`是也乎:`

叕一个死磕正则表达式的...
想通过自动生成来简化学习...

)


- [pypi-diff: PyPI 包历史跟踪](https://pycoders.com/link/10701/web)
    + GITHUB.COM/ABBBI

(`是也乎:`

已经放弃维护了...

)

- [nanobind: 小巧高效的 C++/Python 绑定](https://pycoders.com/link/10702/web)
    + GITHUB.COM/WJAKOB



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [PyCon US 2023](https://pycoders.com/link/10715/web)
    + April 19 to April 28, 2023

- [PyKla Monthly Meetup](https://pycoders.com/link/10697/web)
    + April 26, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10692/web)
    + April 26, 2023

- [PyStaDa](https://pycoders.com/link/10698/web)
    + April 26, 2023

- [Python Adelaide Meetup](https://pycoders.com/link/10710/web)
    + April 27, 2023

- [SPb Python Drinkup](https://pycoders.com/link/10703/web)
    + April 27, 2023

- [PythOnRio Meetup](https://pycoders.com/link/10700/web)
    + April 29, 2023



-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 522](https://weekly.pychina.org/issue/issue-522.html)
- 2021: [蠎周刊 470](https://weekly.pychina.org/issue/issue-470.html)
    + [pythonista-weekly : Pyw 496](https://weekly.pychina.org/python-weekly/pyw-496.html)
- 2020: [蠎周刊 417](https://weekly.pychina.org/issue/issue-417.html)
    + [pythonista-weekly : Pyw 446](https://weekly.pychina.org/python-weekly/pyw-446.html)
- 2019: [蠎周刊 365](https://weekly.pychina.org/issue/issue-365.html)
- 2018: [蠎加载 172](https://weekly.pychina.org/importpython/importpython-172.html)
- 2017: [蠎加载 121](https://weekly.pychina.org/importpython/importpython-121.html)
- 2016: [蠎周刊 209](https://weekly.pychina.org/issue/issue-209.html)
    + [蠎加载 70](https://weekly.pychina.org/importpython/importpython-70.html)
- 2015: [蠎周刊 163](https://weekly.pychina.org/issue/issue-163.html)
    + [蠎加载 29](https://weekly.pychina.org/importpython/importpython-29.html)
- 2014: [Issue 112: SpaceX](https://weekly.pychina.org/issue/issue-112.html)
- 2013: 空缺
- 2012: [Issue 11 ~ Turn it Up](https://weekly.pychina.org/issue/issue-11.html)


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



```
            _~--^~_
        \) /  - ^  \ \/
          '_   v   _'
          > '-----' <

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```




-----------------------------------------
# PS:

- 首发: [Issue 574 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-574.html)
- 修订: [issue-574.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-574.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF574D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF574D4Q90XdDA7g):



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



