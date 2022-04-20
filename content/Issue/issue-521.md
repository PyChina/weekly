Title: PyCoder 521
Slug: issue-521
Date: 2022-04-19 11:42
Tags: Weekly,Python,pycoders,ZH


> WASM, Python Keywords, PyInstaller...


原文: [PyCoder's Weekly - Issue #521](https://pycoders.com/issues/521)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220419 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220419 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [用 Python 和 WebAssembly 构建编辑器](https://pycoders.com/link/8534/web)
    + AMIR TADRISI 
    + • Shared by Amir Tadrisi

Step-by-step instructions on how to build a code editor in the browser using Python and WebAssembly (WASM), via Pyodide, and CodeMirror.


(`是也乎:`


[Pyodide](https://pyodide.org/en/stable/)硬广.
 a port of CPython to WebAssembly/Emscripten...

其实是期待能替代 React/Vue 们嘛?


)

- [探索 Python 中的关键字](https://pycoders.com/link/8505/web)
    + REAL PYTHON 
    + COURSE

Python keywords make up the fundamental building blocks of any Python program. In this video course, you’ll learn the basic syntax and usage for each of Python’s thirty-five keywords so you can write more efficient and readable code.


(`是也乎:`

![Exploring](https://ipic.zoomquiet.top/2022-04-20-zshot%202022-04-20%2011.44.29.jpg)

)

- [用 PyInstaller 为 Windows 打包 PyQt6 应用程序](https://pycoders.com/link/8531/web)
    + MARTIN FITZPATRICK

It isn’t much fun creating your own desktop applications if you can’t share them with other people: learn how to turn your PyQt6 application into a distributable installer for Windows using PyInstaller and InstallForge.

(`是也乎:`

嗯哼? win11 ? 祝你好运...

)


- [Django 安全版本: 4.0.4, 3.2.13, and 2.2.28](https://pycoders.com/link/8530/web)
    + DJANGO SOFTWARE FOUNDATION



-----------------------------------------
## 探讨/吐糟
> Discussions

- [2038 日期问题（有趣/且真实）](https://pycoders.com/link/8522/web)
    + TWITTER.COM/XSSFOX

Coders old enough to remember Y2K are already dreading 2038, join the conversation.

(`是也乎:`

千年虫之后, 还有很多同类, 
不过, 很怀疑, 到时, 人类是否存在
)


- [是否创建过仅供个人使用的程序?](https://pycoders.com/link/8507/web)
    + HACKER NEWS


(`是也乎:`

很多吧, 只有自己在用的小脚本...

)

- [了解 Python 可以从事哪些工作?](https://pycoders.com/link/8515/web)
    + HACKER NEWS

(`是也乎:`

> ...Using frameworks is a must. Writing maintainable code is a must.

DevOps - you'll quickly run into requirements to write parallel work. Not using something like fabric is a waste of your employer's money hiring you. You'll quickly run into requirements to use ansible/terraform/other. Same applies here; surrounding tools with subprocess and parsing stdout/stderr is a waste of your employer's money. Use appropriate packages, instead.

DataScience - all the cool toys, from simple stuff like pandas, or more focused ones like working with spark and the plethora of big data libraries require indepth knowledge of both the library and the underlying datastore. Combined, you make the most of your time and hardware. Not doing so, and only writing something that works on a small scale is a common costly mistake.

Security - python is just a helper tool. Your requirements, depending on position, will be focal knowledge about a domain and its set of tools. From highly skilled domains like research onward to threat hunting, PT and to the entry level stuff like NOC.

You're better off enjoying the little wins in life and dealing with the less pleasant moments. That'll give you a nice career in anything you choose.



)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [是如何测试的?](https://pycoders.com/link/8540/web)
    + CARL BOLZ-TEREICK

PyPy is a popular alternative implementation of Python and with a project of this size testing is always a challenge. This blog post highlights the testing philosophy used at PyPy, how the tests are organized, and how they avoid performance regressions.


(`是也乎:`

灵魂追问...

)


- [Python 虚拟环境: 入门](https://pycoders.com/link/8524/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use a Python virtual environment to manage your Python projects. You’ll also dive deep into the structure of virtual environments built using the venv module, as well as the reasoning behind using virtual environments.


(`是也乎:`

![Primer](https://ipic.zoomquiet.top/2022-04-20-zshot%202022-04-20%2011.29.29.jpg)

这一点儿也不Primer...
其实, Py 运行时, 最困难的并不是合理分离,
而是, 快速部署以及迁移复用

)


- [叕一个优化故事](https://pycoders.com/link/8512/web)
    + ZACH MITCHELL

“I wanted to make a physics simulation 100x faster. I got it 4x faster exercising my best NumPy skills, and 50x faster after rewriting in Rust with a couple of other optimizations. I’d probably get to 100x if I had more than 2 cores.”


(`是也乎:`

优化其实很容易上瘾,
不过, 更加容易忘记, 这得是业务足够稳定, 
不提高性能就亏的场景中, 才合理...


)


- [Threading in Python: 完整指南](https://pycoders.com/link/8521/web)
    + JASON BROWNLEE

A very deep guide to all things threading in Python. Covers: differences between threads and processes, thread life-cycles, getting thread information, configuring threads, handling exceptions, locks, and all with many many examples.

(`是也乎:`

其实吧, 有资源就上进程...

)


- [用更快的硬件: 权衡和替代方案](https://pycoders.com/link/8538/web)
    + ITAMAR TURNER-TRAURING

Throwing hardware at a software performance is often an easy solution, and sometimes the right one. Learn how to approach the decision, and some alternatives.

- [Django 中的权限](https://pycoders.com/link/8497/web)
    + OLUWOLE MAJIYAGBE 
    + • Shared by Oluwole Majiyagbe

Django comes with a robust permission system built-in. Learn about authentication, authorization, users, groups, and model level permissions.


- [Python 和弃用 Redux](https://pycoders.com/link/8542/web)
    + LWN.NET

A deep dive on how the core team manages deprecations in Python, and how complications in a Fedora package were dealt with.

(`是也乎:`

LWN 的文章一向硬核,
实在是个古老的新闻组,
形式决定内容, 这么古板的界面也只好认真写点儿什么

> Linux is a registered trademark of Linus Torvald

)


- [通过量化彩色图像学习 K-Means 聚类](https://pycoders.com/link/8527/web)
    + BALA PRIYA C 
    + • Shared by Bala Priya C

Learn about the K-Means Clustering algorithm by coding an image quantizer in Python.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [用代码整洁的 Python 库](https://pycoders.com/link/8529/web)
    + ISAAK UCHAKAEV


(`是也乎:`

各种大力自动修改你撰写代码的工具...
为什么能有人可以忍受工具来改动自己写的文章?

)

- [TigerLily: 用 TigerGraph 在 Silico 中寻找药物相互作用](https://pycoders.com/link/8514/web)
    + GITHUB.COM/BENEDEKROZEMBERCZKI 
    + • Shared by Benedek Rozemberczki


(`是也乎:`


![TigerLily](https://ipic.zoomquiet.top/2022-04-20-zshot%202022-04-20%2011.22.26.jpg)


药物检验自动机

)

- [SaaS 的现代 Flask 样板](https://pycoders.com/link/8519/web)
    + GITHUB.COM/NUVIC • Shared by Nuvic




- [Durin’s Box: 语音激活/密码保护/ Wooden Box](https://pycoders.com/link/8499/web)
    + JOHN PENDER

- [ThinkDSP: 关于 Python 数字信号处理的免费书籍](https://pycoders.com/link/8523/web)
    + GITHUB.COM/ALLENDOWNEY

(`是也乎:`

DSP/Digital Signal Processing 数字信号处理,
前苏联 Maker 们最爱的领域...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Heidelberg Python Meetup](https://pycoders.com/link/8506/web)
    + April 20, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8544/web)
    + April 20, 2022

- [Python Northwest](https://pycoders.com/link/8511/web)
    + April 21, 2022

- [PyLadies Dublin](https://pycoders.com/link/8498/web)
    + April 21, 2022

- [PyDelhi User Group Meetup](https://pycoders.com/link/8517/web)
    + April 23, 2022

- [PyCon US 2022](https://pycoders.com/link/8516/web)
    + April 27 to May 6, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 521 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-521.html)
- 修订: [issue-521.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-521.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF521D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF521D4Q90XdDA7g):



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





