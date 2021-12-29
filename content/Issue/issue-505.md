Title: PyCoder 505
Slug: issue-505
Date: 2021-12-29 11:42
Tags: Weekly,Python,pycoders,ZH


> PyO3 ~ 被 Py 氧化的 Rust


原文: [PyCoder's Weekly - Issue #505](https://pycoders.com/issues/505)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211229 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211229 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------





- [Python Zip 导入: 快速分发模块和包](https://pycoders.com/link/7707/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn what Zip imports are and how to use them in Python. You’ll learn to create your own importable ZIP files and make them available for use. Finally, you’ll learn how to use the zipimport module to dynamically import code from ZIP files.


(`是也乎:`

传统手工艺, 发布应用发行版

![Imports zip](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2010.27.19.jpg)

)


- [用 Python 编写高速异步 HTTP 请求](https://pycoders.com/link/7716/web)
    + JONLUCA DECARO

Different formats and code snippets to make a large amount of network requests locally, with controls for rate limiting and error handling.

Shortcut Provides Speedy Task Management, Reporting, and Collaboration for Software Teams
Shortcut is project management built for developers. Whether you’re a startup that iterates quickly by providing every engineer with a free pallet of Red Bull, or a large org that has strict ship dates to hit, give us a try for free →
SHORTCUTSPONSOR

(`是也乎:`


aiohttp 的硬广

)


- [应该使用版本上限约束吗?](https://pycoders.com/link/7714/web)
    + HENRY SCHREINER 
    + • Shared by Henry Schreiner

package>=7 vs package>=7,<8: Should you be adding upper bounds to dependency version constraints in Python packages?




- [PEP 669: CPython 的低影响监控](https://pycoders.com/link/7739/web)
    + PYTHON.ORG

sing a profiler or debugger in CPython can have a severe impact on performance. Slowdowns by an order of magnitude are common. This PEP proposes an API for monitoring of Python programs running on CPython that will enable monitoring at low cost.





-----------------------------------------
## 探讨/吐糟
> Discussions


- [现代优秀示例 Python 项目阅读推荐?](https://pycoders.com/link/7719/web)
    + HACKER NEWS


(`是也乎:`

面向阅读的工程?


[tiangolo (Sebastián Ramírez)](https://github.com/tiangolo) 被推

![tiangolo](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2010.23.21.jpg)

必然是德国人哪...

)


- [为毛 Pandas Operations 不是就地进行?](https://pycoders.com/link/7726/web)
    + STACK OVERFLOW

(`是也乎:`

因为...懒?

)




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Head First Taichi: 面向Python的高性能计算初学者指南](https://pycoders.com/link/7723/web)
    + DUNFAN LU

“The Taichi Programming Language is an attempt to extend the Python programming language with constructs that enable general-purpose, high-performance computing. It is seamlessly embedded in Python, yet can summon every ounce of computing power in a machine — the multi-core CPU, and more importantly, the GPU.”


(`是也乎:`


![Taichi](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2010.20.05.jpg)

少见的 太极 宣传文章哪,
这的确是国产知名物理引擎.

)

- [如何加速 XGBoost 模型训练](https://pycoders.com/link/7718/web)
    + MICHAEL GALARNYK 
    + • Shared by Michael Galarnyk

XGBoost is an open-source implementation of gradient boosting designed for speed and performance. However, even XGBoost training can sometimes be slow. There are quite a few approaches to accelerating this process like changing tree construction algorithm leveraging cloud computing, and distributed XGBoost.


(`是也乎:`



)


- [测试 argparse 应用/更好的方法](https://pycoders.com/link/7735/web)
    + JÜRGEN GMACH 
    + • Shared by Jürgen Gmach

“When you are creating command-line applications in Python, you probably heard of argparse, which is a great library for exactly doing this, and it is even included in Python’s standard library. But have you ever tried to create tests for a command-line application?”

- [用图论和 Python 排序电影片尾字幕](https://pycoders.com/link/7708/web)
    + ENDCRAWL.COM

How do you order movie end credits? “This is surprisingly hard to answer. Pick any two films and you’ll find conflict in how screen credits are ordered. There are so many minor disagreements, in fact, that a human can’t hope to reconcile them.”


(`是也乎:`


![字幕](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2010.33.48.jpg)


电影工业的强大可见一斑...

)


- [使用 ConfZ 对 FastAPI 进行无缝配置](https://pycoders.com/link/7734/web)
    + SILVAN MELCHIOR

“ConfZ is a new configuration management library for Python. It is based on pydantic, which makes it perfect to use together with FastAPI.”





- [Pyodide 中的函数指针转换处理](https://pycoders.com/link/7711/web)
    + HOOD CHATHAM

Why previous versions of Pyodide had a low recursion limit and how the upcoming version 0.19 supports a much higher one.


(`是也乎:`


叕一个追求简洁的图表库, 最终都会被现实打败...

)


- [用 Python 探索 Google Analytics 实时数据](https://pycoders.com/link/7727/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

Taking full advantage of Google Analytics features and data using its REST API and Python.

- [用 PyO3 从 Python 调用 Rust](https://pycoders.com/link/7715/web)
    + SAID VAN DE KLUNDERT

(`是也乎:`

凡是能和 C 流畅交流的, Python 也都能掺合进来

PyO3 ~ 被 Py 氧化的 Rust

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [poetry-kernel: 基于 Poetry 制作可复制笔记本的 Python Jupyter 内核 ](https://pycoders.com/link/7724/web)
    + GITHUB.COM/PATHBIRD


(`是也乎:`

嗯哼? poetry 就这么上位了?

![jupyter-lab](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2009.59.28.jpg)

几乎叕一个 VSCode 平台了...


)


- [primify: 将 ASCII 艺术图像嵌入质数](https://pycoders.com/link/7713/web)
    + GITHUB.COM/LEVIBORODENKO

(`是也乎:`

![primify](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2009.56.33.jpg)

也是刚需了...
效率够的话, 就可以在终端里用 ASCII-art 看电影了


)


- [pythons-gc-and-orms: 基本 ORM 工作时探索 GC 的数量](https://pycoders.com/link/7722/web)
    + GITHUB.COM/MIKECKENNEDY

- [glide-text2im:  基于 Diffusion-Based 文本条件图像合成模型](https://pycoders.com/link/7737/web)
    + GITHUB.COM/OPENAI

- [Box: 具有高级点符号访问的 Python 词典](https://pycoders.com/link/7731/web)
    + GITHUB.COM/CDGRIFFITH

- [ItsDangerous: 签署和验证任意数据](https://pycoders.com/link/7720/web)
    + PALLETSPROJECTS.COM

(`是也乎:`

武断数据? ~ 将数据发送到危险环境再取回时必要操作是什么?

这个模块的名字很屌, MJ 范儿

![ItsDangerous](https://ipic.zoomquiet.top/2021-12-29-zshot%202021-12-29%2009.54.03.jpg)
)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ SPb Python Drinkup](https://pycoders.com/link/7730/web)
    + December 30, 2021
    + 酒

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/7728/web)
    + January 1, 2022
    + 印度

- [⋅ Melbourne Python Users Group, Australia](https://pycoders.com/link/7712/web)
    + January 3, 2022

- [⋅ Introduction to the Python Programming Language (In Persian)](https://pycoders.com/link/7736/web)
    + January 4, 2022
    + 波斯

- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/7710/web)
    + January 4, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅
- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 505 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-505.html)
- 修订: [issue-505.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-505.md)


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

好文笔,感叹号年度配额: **3/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF505D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF505D4Q90XdDA7g):



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





