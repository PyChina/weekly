Title: PyCoder 512
Slug: issue-512
Date: 2022-02-17 11:42
Tags: Weekly,Python,pycoders,ZH


> Twisted 22.1.0 发布...


原文: [PyCoder's Weekly - Issue #512](https://pycoders.com/issues/512)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220217 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220217 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [文档 Unit Tests](https://pycoders.com/link/8019/web)
    + SIMON WILLISON

Interesting approach to keeping documentation and code in sync: introspecting the code to figure out what needs to be documented, then parsing the documentation to see if each item has been covered.




- [改善您的 Django 和 Python 开发者体验](https://pycoders.com/link/8029/web)
    + REAL PYTHON 
    + PODCAST


How often have you thought about your Developer Experience (DX)? How do you improve your workflow, find documentation, and simplify code formatting? This week on the show, Adam Johnson is here to talk about his new book, “Boost Your Django DX.”


(`是也乎:`

![PODCAST](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2014.08.47.jpg)

UX 重要, 还是 DX 重要?


)


- [Python’s zipfile: 有效地操作 ZIP 文件](https://pycoders.com/link/8033/web)
    + REAL PYTHON

In this guided tutorial, you’ll learn how to manipulate ZIP files using Python’s zipfile module from the standard library. Through hands-on examples, you’ll learn how to read, write, compress, and extract files from your ZIP files quickly.


(`是也乎:`

![zipfile](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2014.07.15.jpg)

)

- [PEP 673: 自我类型已接受](https://pycoders.com/link/8010/web)
    + PYTHON.ORG

This PEP introduces a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach specified in PEP 484 but is more concise and easier to follow. Related Twitter thread by core dev Raymond Hettinger.

- [Twisted 22.1.0 发布](https://pycoders.com/link/8013/web)
    + TWISTEDMATRIX.COM

Twisted, the event framework for internet applications, has announced the release of 22.1.0. Mainly a bugfix release.


(`是也乎:`


淦.... 还在稳定升级, 超长寿 巨型模块...
)

- [Django 项目用 Black 重新格式化整个代码库](https://pycoders.com/link/8014/web)
    + GITHUB.COM/DJANGO

Related discussion on Hacker News.

(`是也乎:`


淦...够卷的...
这是想用

)





-----------------------------------------
## 探讨/吐糟
> Discussions



- [Python 类型提示指南](https://pycoders.com/link/8006/web)
    + HACKER NEWS

Are type-hints overused? Discussion on if sometimes they’re too much.

- [你最近在工作中使用 Python 自动化了什么?](https://pycoders.com/link/8024/web)
    + REDDIT

From mouse-wiggling scripts to make Teams look active to RNC automation.


(`是也乎:`

这个可以有哪...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [即将推出的 Python PEPs](https://pycoders.com/link/8037/web)
    + MARTIN HEINZ

“These PEPs are a great way of getting the freshest info about what might be included in the upcoming Python releases. So, in this article we will go over all the proposals that are going to bring some exciting new Python features in a near future!”

- [Python 中的 K-Nearest](https://pycoders.com/link/8015/web)
    + NIK PIEPENBREIER 
    + • Shared by Nik Piepenbreier

A beginner-friendly guide to the K-Nearest Neighbor algorithm implemented in Python using Scikit-Learn. The tutorial assumes no prior knowledge of machine learning and guides through developing a classifier, evaluating its performance, and hyper-parameter tuning.



- [Python’s all(): 检查迭代的真实性](https://pycoders.com/link/8028/web)
    + REAL PYTHON

Learn how to use Python’s all() function to check if all the items in an iterable are truthy. You’ll also code various examples that showcase a few interesting use cases of all() and highlight how you can use this function in Python.

(`是也乎:`


![all](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2012.06.25.jpg)
)


- [如何在 Python 中检查数字是否同时为素数](https://pycoders.com/link/8008/web)
    + JASON BROWNLEE

“The ProcessPoolExecutor class in Python can be used to check if multiple numbers are prime at the same time. This can dramatically speed-up your program compared to checking if numbers are prime, one-by-one.”

- [作为数据科学家进行测试的方式](https://pycoders.com/link/8034/web)
    + PETER BAUMGARTNER

“Knowing what to test requires some experience in knowing what can go wrong.” Peter describes testing with a Data Scientist’s perspective.

- [Python 中的结构子类型](https://pycoders.com/link/8040/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

Along with nominal typing, Protocol classes now allow you to take advantage of structural subyping in Python. This post explores that.




- [如何对 Python 对象腌制和反腌制](https://pycoders.com/link/8036/web)
    + MOHAMMAD WASEEM

Learn how to serialize and deserialize data in Python with the pickle module, including working with serialization in Pandas.


(`是也乎:`

除非对象非常非常固定,
否则, 能序列化到数据库中, 是最稳的;



)


- [Python 切片综合指南](https://pycoders.com/link/8038/web)
    + BAS STEINS

Introduction to slicing in Python, covers slices, negative indexes, slice(), and how to make your own classes slice-able.



- [ Python Logging 的来龙去脉](https://pycoders.com/link/8016/web)
    + CESAR URIBE 
    + • Shared by Erin McLaughlin

A multi-part guide to using logging in Python. The fundamental concepts are discussed and illustrated with simple examples.


(`是也乎:`


魔鬼在细节
)

- [链接比较运算符](https://pycoders.com/link/8043/web)
    + RODRIGO GIRÃO SERRÃO

“Learn the ins and outs of comparison operator chaining, and especially the cases you should avoid.”




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [Django REST Framework 备忘录](https://pycoders.com/link/8032/web)
    + CDRF.CO

(`是也乎:`


DRF 作弊条...

![CDRF](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2012.01.26.jpg)


)



- [PaddleOCR: 基于 PaddlePaddle 的多语言 OCR 工具包](https://pycoders.com/link/8026/web)
    + GITHUB.COM/PADDLEPADDLE



(`是也乎:`


![PaddleOCR](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2011.59.29.jpg)

终于有个支持亚洲文字的 OCR 了...

![CKJ](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2012.00.18.jpg)



)

- [pytube: 用于下载 YouTube 视频的无依赖 Python 库](https://pycoders.com/link/8023/web)
    + GITHUB.COM/PYTUBE

(`是也乎:`

`youtube-dl` 之后, 叕一个想彻底解决 视频下载问题的工具...

)



- [YT-Spammer-Purge: 按用户在 YouTube 上的评论进行扫描和删除](https://pycoders.com/link/8007/web)
    + GITHUB.COM/THIOJOE

(`是也乎:`


![Spammer](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2011.56.16.jpg)

anti-spam 叕一作品

)


- [plane-notify: 通知飞机起飞或降落](https://pycoders.com/link/8011/web)
    + GITHUB.COM/JXCK-S

(`是也乎:`

逼疯 Musk 的系统开源了?

![notify](https://ipic.zoomquiet.top/2022-02-17-zshot%202022-02-17%2011.55.08.jpg)

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/8035/web)
    + February 15 to February 16, 2022

- [⋅ PyCon Iran 2022](https://pycoders.com/link/8041/web)
    + February 16 to February 19, 2022

- [⋅ PyLadies Dublin](https://pycoders.com/link/8044/web)
    + February 17, 2022

- [⋅ PyCon Sri Lanka 2022](https://pycoders.com/link/8018/web)
    + February 22 to February 23, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 512 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-512.html)
- 修订: [issue-512.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-512.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF512D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF512D4Q90XdDA7g):



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





