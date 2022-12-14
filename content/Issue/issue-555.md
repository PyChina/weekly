Title: PyCoder 555
Slug: issue-555
Date: 2022-12-14 11:42
Tags: Weekly,Python,pycoders,ZH


> 简单是一种优势，但遗憾的是复杂性更好卖...人艰不拆


原文: [PyCoder's Weekly - Issue #555](https://pycoders.com/issues/555)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221214 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221214 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [用 pyproject.toml 打包 Python 代码并使用 pathlib 列出文件](https://pycoders.com/link/10022/web)
    + REAL PYTHON PODCAST

How do you start packaging your code with pyproject.toml? Would you like to join a conversation that gently walks you through setting up your Python projects to share? This week on the show, Christopher Trudeau is here, bringing another batch of PyCoder’s Weekly articles and projects.


(`是也乎:`

打包/分发, 是一个开发语言最关键的输出形式,
但是, Python 这么多年了,一直在变化,
`pyproject.toml` 是否能替代 `setup.cfg`/`setup.py` 统一所有打包工具,
还得看 M$ 的决心了?

)


- [谁控制并行性? 导致放缓的分歧](https://pycoders.com/link/10005/web)
    + ITAMAR TURNER-TRAURING

In complex systems there may be a fight between the parallelism in your code vs the parallelism in the libraries you’re using. This fight can cause things to slow down. This article shows some examples and what you can do about it.


- [在 AWS 免费套餐上制作 Mastodon 机器人](https://pycoders.com/link/10020/web)
    + MAT DUGGAN

This article walks you through everything you need to know to get a Mastodon bot set up in on the AWS Free tier through DynamoDB and AWS Lambdas.

- [PyPy v7.3.10 发布](https://pycoders.com/link/9998/web)
    + PYPY.ORG

(`是也乎:`

PyPy 也开始努力了,毕竟不能比 CPython 还要慢吧?

)


- [Django Bugfix 发布: 4.1.4](https://pycoders.com/link/10007/web)
    + DJANGO SOFTWARE FOUNDATION

- [Python 3.11.1, 3.10.9, 3.9.16, 3.8.16, 3.7.16 发布](https://pycoders.com/link/10002/web)
    + CPYTHON DEV BLOG


(`是也乎:`

感觉到集团军样的气势,
看起来 M$ 投入了正规编制来推动?


)


- [XtremePython 2022 线上大会 12.27th](https://pycoders.com/link/9992/web)
    + XTREMEPYTHON.DEV 
    + • Shared by Haim Michael



-----------------------------------------
## 探讨/吐糟
> Discussions



- [软件架构师: 您典型的一天是什么样的?](https://pycoders.com/link/10016/web)
    + HACKER NEWS


(`是也乎:`

哈哈哈...

)


- [您使用什么风格的导入语句?](https://pycoders.com/link/9991/web)
    + TWITTER.COM/BBELDERBOS 
    + • Shared by Bob Belderbos


(`是也乎:`

等等,这种还有风格的?

)






-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [I/O 不再是瓶颈](https://pycoders.com/link/10014/web)
    + BEN HOYT

A common interview question Ben asks candidates is to write a program that counts the frequency of words in a file, as a follow-up question he asks where the bottleneck is in the code. The most common answer, I/O, is not necessarily true on modern hardware. Read on to see the comparisons between Python and GO and where the program actually spends its time.


(`是也乎:`

喜大普奔?

)


- [要避免的 Django 设置模式](https://pycoders.com/link/10004/web)
    + ADAM JOHNSON

The settings module is key to getting your Django project up and running, storing the info your project needs to run. As with all code, there are both good and bad habits. This article details some of the patterns you should avoid.


(`是也乎:`


![ADAM](https://ipic.zoomquiet.top/2022-12-14-zshot%202022-12-14%2009.25.00.jpg)


和图书装潢类似,
一个视觉上设计良好的网站,更能留住读者...

)


- [简单是一种优势，但遗憾的是复杂性更好卖](https://pycoders.com/link/9993/web)
    + EUGENE YAN

This opinion piece from Eugene Yan discusses why complexity is often touted over simplicity: the effort is more obvious and therefore must be superior. This is a trap in thinking. Eugene makes the tougher argument for simplicity.


(`是也乎:`

怪不得 Oracle/SAP 们一直卖的不错, 但是 SQLite 却没什么商业模式

)


- [Python 基础:字典](https://pycoders.com/link/10012/web)
    + REAL PYTHON 
    + COURSE

One of the most useful data structures in Python is the dictionary. In this video course, you’ll learn what a dictionary is, how dictionaries differ from lists and tuples, and how to define and use dictionaries in your own code.

(`是也乎:`


![Dictionaries](https://ipic.zoomquiet.top/2022-12-14-zshot%202022-12-14%2009.21.10.jpg)

)


- [用 Python 制作漂亮的二维码](https://pycoders.com/link/10001/web)
    + PETE FISON 
    + • Shared by Pete Fison

QR codes don’t have to look ‘industrial’ and they’re trivially easy to create in Python. This article focuses on personal, social, and human applications for the trusty old QR code.


(`是也乎:`

其实还有很多类似图形数据码,
但是, QR 码就象 JavaScript 已经内置到无数软件中,
开始了市场自我强化, 也只能继续在这个方向上内卷了...

)


- [PyTorch 2.0 入门](https://pycoders.com/link/10015/web)
    + PYTORCH.ORG

PyTorch has released a new Getting Started guide with all the info you need to begin your PyTorch 2.0 journey.

(`是也乎:`

现在其它 ML/DL/... AI 框架的问题在,
拿不出类似 ChatGPT 的作品来,
再怎么加强宣传和教程, 也难以匹敌 TF 象当年 Chrome 一样快速统治市场?

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [git-bug: 嵌入在 Git 中的分布式/离线优先的错误跟踪器](https://pycoders.com/link/10011/web)
    + GITHUB.COM/MICHAELMURE

(`是也乎:`

git 本质上就是 `分布式文件系统`,
当然应该可以任意修订历史上各种信息的,
以往没有很好的界面,全靠指令摸索,
现在 go 开发了 TUI 

)


- [kangas: 大规模探索多媒体数据集](https://pycoders.com/link/10003/web)
    + GITHUB.COM/COMET-ML

(`是也乎:`

![kangas](https://ipic.zoomquiet.top/2022-12-14-zshot%202022-12-14%2009.16.23.jpg)

对AI 处理过程数据的探索界面

)


- [whitebox: 端到端机器学习监控平台](https://pycoders.com/link/10006/web)
    + GITHUB.COM/SQUAREDEV-IO

- [takahe: 一个 ActivityPub/Fediverse 服务器](https://pycoders.com/link/10009/web)
    + GITHUB.COM/JOINTAKAHE

(`是也乎:`

之前还感觉 JAVA 是术语发源地/模式创造工厂,
现在, 无论什么模型/模式,
Python 都能立即给出可用方案来...

)


- [NansAreNumbers: 一种基于 NaN 的深奥数据类型](https://pycoders.com/link/9999/web)
    + GITHUB.COM/THOPPE






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Python North East](https://pycoders.com/link/10018/web)
    + December 14, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9995/web)
    + December 14, 2022

- [PyData Bristol Meetup](https://pycoders.com/link/10000/web)
    + December 15, 2022

- [PyLadies Dublin](https://pycoders.com/link/10017/web)
    + December 15, 2022

(`是也乎:`

PyLadies 已经变成常设活动了,
其实对于传统的大家相互吐糟,
帮助小姐姐们很明显更加和谐...


)


- [Python Pizza Holguín](https://pycoders.com/link/10010/web)
    + December 17 to December 18, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 555 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-555.html)
- 修订: [issue-555.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-555.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF555D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF555D4Q90XdDA7g):



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





