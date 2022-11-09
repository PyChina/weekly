Title: PyCoder 550
Slug: issue-550
Date: 2022-11-09 11:42
Tags: Weekly,Python,pycoders,ZH


> 是什么令 Py3.11 加速这么猛? ~ 用真心


原文: [PyCoder's Weekly - Issue #550](https://pycoders.com/issues/550)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221109 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221109 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 3.11 究竟从哪儿获得了加速?](https://pycoders.com/link/9827/web)
    + BESHR KAYALI

This deep dive into Python 3.11’s speed-up walks you through nine different optimizations that contribute to the 25% performance improvement in CPython.

- [Python 基础: 作用域](https://pycoders.com/link/9818/web)
    + REAL PYTHON COURSE

In this video course, you’ll learn what scope is and why it’s important to coding functions and loops in Python. You’ll also get to know the LEGB rule.

(`是也乎:`


![Scopes](https://ipic.zoomquiet.top/2022-11-09-zshot%202022-11-09%2009.30.47.jpg)

好象有个什么口决来判定的...--> `LEGB rule`

)


- [Python 中的 Google API 入门](https://pycoders.com/link/9820/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

A crash course in using Python and Google APIs to automate all the things you do with Gmail, Google Drive, Calendar, or any other Google API

(`是也乎:`

什么是 Google ?

)



- [PyCascades 2023 征集提案](https://pycoders.com/link/9804/web)
    + PRETALX.COM

- [Django Bugfix 发布: 4.1.3](https://pycoders.com/link/9837/web)
    + DJANGO SOFTWARE FOUNDATION

- [PyTorch 1.13 发布](https://pycoders.com/link/9816/web)
    + PYTORCH.ORG

- [PyChain 2022 演讲者公布](https://pycoders.com/link/9836/web)
    + PYCHAIN.ORG






-----------------------------------------
## 探讨/吐糟
> Discussions



- [PEP 603: 向集合添加 Frozenmap 类型](https://pycoders.com/link/9828/web)
    + PYTHON.ORG

- [哪些工具可以在不停机的情况下发现语法错误?](https://pycoders.com/link/9813/web)
    + GOOGLE.COM

(`是也乎:`

等等,难道期望包含语法错误的代码不停止?

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [更多可疑的 PyPI 包](https://pycoders.com/link/9819/web)
    + PHYLUM.IO

Researchers at Phylum have come across over a dozen new malicious uploads to PyPI. Many of them are copy-pasted versions of legitimate packages that have been renamed and had malicious code inserted. This detailed article shows some of the tactics used by the black-hats.

(`是也乎:`

其实吧,嘦 PyPI 包历史超过5年以上的, 才可以放心安装就好...

)


- [用 Strawberry 向 Starlette 添加 GraphQL API](https://pycoders.com/link/9826/web)
    + GENIEPY.COM 
    + • Shared by Siddhant Goel

GraphQL has become the de facto standard for servers to offer APIs to clients, due to the flexibility it offers. This article talks about how you can build a GraphQL API in a Starlette application using Strawberry, a new GraphQL library inspired by dataclasses.





- [优秀 Pull Request 的十种美味成分](https://pycoders.com/link/9808/web)
    + LB

LB is a core team member of the open source project Wagtail, and as such has a lot of experience dealing with community contributions. This article talks about how to be a good contributor whether for your next OSS PR or within your own organization.


(`是也乎:`

到现在见到 Delicious , 第一反应还是 De.licio.us
社区效其实就反应在这些细节的共识深度上,
也就是说, 社区参与者多少时间才能达到 90% 以上关键协作行为一致

)


- [Web 自动化: 不要使用 Selenium 上 Playwright](https://pycoders.com/link/9834/web)
    + SHANTNU TIWARI

Playwright is an open source alternative to Selenium created by Microsoft. It includes click-and-record functionality that directly generates a Python script. Read on for why Shantnu recommends it.

(`是也乎:`


天下苦硒久矣...
等等, microsoft 的作品?
好吧, 没事儿了.

)


- [应该更新到最新的 Python 修正版本吗?](https://pycoders.com/link/9838/web)
    + REAL PYTHON

What’s the significance of the third digit in a Python version number? In this tutorial, you’ll learn more about Python bugfix versions and whether you need to care about them.

(`是也乎:`

![Bugfix](https://ipic.zoomquiet.top/2022-11-09-zshot%202022-11-09%2009.06.42.jpg)

很明显,生产中别这么来,
日常学习/探索中, 值得提前体验各种最新近嗯哼

)


- [“无效语法”的含义](https://pycoders.com/link/9805/web)
    + TREY HUNNER

Python’s “invalid syntax” error message comes up often, especially when you’re first learning Python. What usually causes this error and how can you fix it?





- [在 Mac 上将 Python 3 变为默认配置的正确和错误方法](https://pycoders.com/link/9829/web)
    + BROBERG & ZADKA

“There are several ways to get started with Python 3 on macOS, but one way is better than the others.” Learn the approaches and which you should choose.


(`是也乎:`



简单的说, 别折腾,
那么多虚拟环境的办法了,
别搞乱系统运行时.

![python_environment_xkcd](https://opensource.com/sites/default/files/uploads/python_environment_xkcd.png)

毕竟原先就已经够乱了

)



- [Python Web 应用程序的缓存技巧](https://pycoders.com/link/9807/web)
    + CHARLES LEIFER

This brief article shows you how to use context managers to provide caching tools information on how long items should stay in memory.


(`是也乎:`

其实吧,服务端足够强,
可以不折腾这种东西的

)


- [Pandas 中的方法链: 糟糕的形式还是成功的秘诀?](https://pycoders.com/link/9835/web)
    + DAVID AMOS 
    + • Shared by David Amos

Python trainer Matt Harrison has been creating a bit of a stir. Some of his pandas examples have elicited criticism from different folks in the Twitterverse. Dave Amos interviews Matt to discuss the pros and cons of his approach.

(`是也乎:`

用的多了,才能发现这其中的苦...

![Pandas](https://ipic.zoomquiet.top/2022-11-09-zshot%202022-11-09%2009.39.54.jpg)


)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [可视化 CPython 3.11 的专业化、自适应解释器](https://pycoders.com/link/9810/web)
    + GITHUB.COM/BRANDTBUCHER

(`是也乎:`


![Visualize](https://raw.githubusercontent.com/brandtbucher/specialist/main/examples/output-0.png)

其实吧,这种实时提示的工具,
本质上都是在抢占工程师的实时注意力,
就象 Word 总是将角色意识进行强行扭曲,
对进入 Flow 状态是毒.


)


- [用于在项目之间共享代码的 Poetry 插件](https://pycoders.com/link/9817/web)
    + GITHUB.COM/DAVIDVUJIC 
    + • Shared by David Vujic


(`是也乎:`


非常象当年 DreamWave 中定义公共组件,然后在多个网页中复用的过程了,
通过 poetry 对依赖树的管理,
进行拟定模块的跨项目复制...

)

- [python-fido2: 通过 USB 与 FIDO 设备通信](https://pycoders.com/link/9824/web)
    + YUBICO.COM

- [PyWeb3D: 用 Python 语法探索 three.js](https://pycoders.com/link/9811/web)
    + GITHUB.COM/BRUNO-ODINUKWEZE

- [File-Injector: 使用 Steganography 将任何文件存储在图像中 ](https://pycoders.com/link/9814/web)
    + GITHUB.COM/CARLOSPUENTEG

(`是也乎:`

![Injector](https://ipic.zoomquiet.top/2022-11-09-zshot%202022-11-09%2008.55.16.jpg)

撞上微信这种自动压缩的环境不就囧了?

)




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Santa Cruz Python Meetup](https://pycoders.com/link/9832/web)
    + November 9, 2022

- [PyStaDa](https://pycoders.com/link/9803/web)
    + November 9, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9821/web)
    + November 9, 2022

- [PyCon Ireland 2022](https://pycoders.com/link/9831/web)
    + November 12 to November 14, 2022

- [PyChain 2022](https://pycoders.com/link/9833/web)
    + November 15 to November 16, 2022

(`是也乎:`

还以为是 PyChina2022 ...

)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 550 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-550.html)
- 修订: [issue-550.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-550.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF550D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF550D4Q90XdDA7g):



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





