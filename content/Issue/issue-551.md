Title: PyCoder 551
Slug: issue-551
Date: 2022-11-16 11:42
Tags: Weekly,Python,pycoders,ZH


> EuroPython 2022 视频已全部上线


原文: [PyCoder's Weekly - Issue #551](https://pycoders.com/issues/551)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221116 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221116 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [重构: 准备代码以获得帮助](https://pycoders.com/link/9847/web)
    + REAL PYTHON 
    + COURSE

In this Code Conversation video course, you’ll explore the steps you can take to get help when you’re stuck while coding. You’ll investigate how to clean up your code to focus on the question you have. Along the way, you’ll learn how to handle errors and use custom exceptions.


(`是也乎:`

重构是好事儿,但是,这是在团队允许这种隐性成本前提下的...


)


- [用 Python 编写 Chrome 扩展程序!](https://pycoders.com/link/9859/web)
    + PETE FISON 
    + • Shared by Pete Fison

Until recently you could only write Chrome Extensions in JavaScript. Now with PyScript, you can write them in Python. This article shows you how to get started writing a simple extension.


(`是也乎:`

何时 PyScript 可以突破沙箱机制,象当年 FF 拓展一样豪放,
才能说明成功了.

)



- [Python Asyncio: 完整指南](https://pycoders.com/link/9856/web)
    + JASON BROWNLEE

This comprehensive guide shows you everything you’d ever want to know about asynchronous programming with coroutines and the asyncio library in Python.

(`是也乎:`

现在都谦虚了,不说终极,只曰完整了.

)


- [EuroPython 2022 视频发布](https://pycoders.com/link/9851/web)
    + YOUTUBE

(`是也乎:`

![EuroPython](https://ipic.zoomquiet.top/2022-11-16-zshot%202022-11-16%2009.11.01.jpg)

126节, 看B站何时完成复制?


)


- [PyCon US 寻找远程志愿者](https://pycoders.com/link/9871/web)
    + PYCON US 
    + GOOGLE FORM


(`是也乎:`

远程志愿者?

)




-----------------------------------------
## 探讨/吐糟
> Discussions

- [停止每个单元测试只需要一个断言的习俗](https://pycoders.com/link/9863/web)
    + HACKER NEWS

(`是也乎:`

嗯哼? 不是说越单一越好管理?

)


- [我如何找到我的“目标”?](https://pycoders.com/link/9862/web)
    + HACKER NEWS

(`是也乎:`

大哉问,一般情况下并不是自己找到的,而是撞进来的...

> Start one level up: why do you want or need a "purpose"?

高赞回答果断是一个反问.

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 Dagger Python SDK 将管道开发为代码](https://pycoders.com/link/9845/web)
    + DAGGER.IO

Dagger is a programmable CI/CD engine that uses code for configuration instead of YAML. They’ve recently released a Python SDK, you can now manage your pipeline in the same language as your code. See also the Hacker News Discussion about the launch.

- [用 Raspberry Pi 作为便携式 PyPI 服务器](https://pycoders.com/link/9860/web)
    + VUYISILE NDLOVU

At PyCon Africa, Vuyisile got into several conversations about the challenges of coding with limited or spotty internet connections. But what if you could take PyPI with you? This article shows you how to build a portable PyPI server on Raspberry Pi hardware.


(`是也乎:`

实用了,这等于方便我们自行架公司内部 PyPI 源;
非洲,果断是非洲...

)


- [Getters 和 Setters: 在 Python 中管理属性](https://pycoders.com/link/9857/web)
    + REAL PYTHON

In this tutorial, you’ll learn what getter and setter methods are, how Python properties are preferred over getters and setters when dealing with attribute access and mutation, and when to use getter and setter methods instead of properties in Python.

(`是也乎:`

老梗,当年 UliEditor 就应用了很多,然后...

![Setters](https://ipic.zoomquiet.top/2022-11-16-zshot%202022-11-16%2009.06.31.jpg)

)



- [在 Python 中构建生成器管道](https://pycoders.com/link/9875/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

Generator pipelines allow you to string calls together so that the output of one call is the input of the next one in the pipeline. The article shows you how to build generator pipelines using function composition.

- [Skybison Python 运行时中的内联缓存](https://pycoders.com/link/9852/web)
    + MAX BERNSTEIN

Inline caching is a popular technique for optimizing dynamic language runtimes. This article covers how such caching was implemented in Skybison, an experimental Python runtime.

- [如何在 Python 中构建模块化算术库](https://pycoders.com/link/9876/web)
    + ALEJANDRO SÁNCHEZ YALÍ. 
    + • Shared by Mirjam Guesgen

Learn how to create a library for modular arithmetic, using operator overloading and redefining the built-in functions for NumPy all while modeling the fun “Lights Out” game.

(`是也乎:`

大规模魔改内建运算符体系

)

- [Python 3.11 的“陷阱”](https://pycoders.com/link/9849/web)
    + JAMES BENNETT

As not all packages have caught up with the Python 3.11 release, upgrading your system early may run into problems. This article details the gotchas James ran into.


(`是也乎:`


3.11 开始,感觉 Python 值得再启蒙了?

)



- [如何对 Django QuerySets 进行过滤](https://pycoders.com/link/9861/web)
    + ALICE RIDGWAY

A tutorial on creating QuerySets with Django ORM and filtering the data. Includes how to convert QuerySets into lists with 15 different examples.

- [Django 表单使用 HTMX 的模态对话框](https://pycoders.com/link/9874/web)
    + AIDAS BENDORAITIS

This article shows you step-by-step how to use the django-crispy-forms library with HTMX to build modal dialogs with Bootstrap.

(`是也乎:`

反正 HTML 有很多问题,
只是...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [typer: 使用类型提示构建出色的 CLI](https://pycoders.com/link/9844/web)
    + GITHUB.COM/TIANGOLO

(`是也乎:`

FastAPI 团队又一力作

)


- [videocr: macOS 中的视频 OCR ](https://pycoders.com/link/9853/web)
    + GITHUB.COM/PETERC

(`是也乎:`

嗯哼?使用可以说异常直觉了:

> python videocr.py in.mp4

)


- [flastapi: 用于 Flask 的类似 FastAPI 的接口插件](https://pycoders.com/link/9868/web)
    + GITHUB.COM/MAARTEN-DP

(`是也乎:`

嗯哼? Flask 这个缝合怪真心是可以包容任何风格了

)


- [jc: JSON-ify 常用输出工具](https://pycoders.com/link/9854/web)
    + GITHUB.COM/KELLYJONBRAZIL

- [daily-python-scripts: 日常任务脚本库](https://github.com/metafy-social/daily-python-scripts)
    + GITHUB.COM/METAFY-SOCIAL


(`是也乎:`

原地址失效,可以搜索其它类似的,比如:
[BristolTopGroup/DailyPythonScripts: Python scripts for the daily tasks in particle physics](https://github.com/BristolTopGroup/DailyPythonScripts)

关键在日常任务足够稳定,多样,又都有可靠接口

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Heidelberg Python Meetup](https://pycoders.com/link/9872/web)
    + November 16, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9873/web)
    + November 16, 2022

- [PyCon US 2023 Call for Proposals](https://pycoders.com/link/9864/web)
    + November 17, 2022

- [PyLadies Dublin](https://pycoders.com/link/9869/web)
    + November 17, 2022

- [MadPUG](https://pycoders.com/link/9858/web)
    + November 17 to November 18, 2022

- [Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/9865/web)
    + November 18, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 551 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-551.html)
- 修订: [issue-551.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-551.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF551D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF551D4Q90XdDA7g):



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





