Title: Issue 450
Slug: issue-450
Date: 2020-12-09 11:42
Tags: Weekly,Python,pycoders,ZH


> ORM 到底值得嘛?


原文: [PyCoder's Weekly - Issue #450](https://pycoders.com/issues/450)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201209 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201209 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [为什么要使用 ORM (对象关系映射器)?](https://pycoders.com/link/5305/web)
    + KARIM MARZOUQ 
    + • Shared by Karim Marzouq

Budding web developers learning Model-View-Controller frameworks are taught that they should use an Object Relational Mapper (ORM) to interface with their databases. But the “why” is often brushed aside or omitted entirely, leaving a fledgling programmer with burning questions like ”What are ORMs, anyway?” and “What problems do they solve?”

(`是也乎:`

直觉上, 为了节省 SQL 培训时间, 以及将 SQL 安全隐藏到 ORM 模块中.

)


- [降低 Python 中的数值精度会影响现实世界的数据集吗?](https://pycoders.com/link/5329/web)
    + MARTIN JONES 
    + • Shared by Martin Jones

Reducing numerical precision is a way to save memory in pandas, but does it make a difference to the conclusions that we might draw from real-world datasets?


(`是也乎:`

这才是真正的千年虫本身

)


- [用PyQt处理SQL数据库:基础](https://pycoders.com/link/5332/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to use PyQt’s built-in SQL support to create GUI applications that effectively manage SQL databases.

(`是也乎:`


![PyQt](http://ydlj.zoomquiet.top/ipic/2020-12-09-ScreenShot%202020-12-09%2010.48.23.jpg)

连接以及读写DB 简单,
问题是 GUI 自动生成表格..


)


- [用 TensorFlow 2 对象检测 API 令已打印链接可点击](https://pycoders.com/link/5331/web)
    + OLEKSII TREKHLEB

Learn how to turn your phone’s camera into a link detector on printed media using Tensor Flow 2’s Object Detection API.





## 探讨/吐糟
> Discussions



- [可用 Python 在家实现什么自动化?](https://pycoders.com/link/5304/web)
    + REDDIT

A good mix of genius, boredom, and absurdity

(`是也乎:`

如果不惜成本, 几乎是一切.

)


- [能在终端上打印出 "Hello World" 的最长代码是什么?](https://pycoders.com/link/5310/web)
    + REDDIT

An inspiring thread of how not to write code

(`是也乎:`

如果乐趣可以无限长....

)


## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [真蟒办公时间: 实时与 Python 专家一起学习](https://pycoders.com/link/5321/web)
    + REAL PYTHON

Come learn with Python experts at the Real Python Office Hours, a weekly video call that offers Real Python members the chance to get help with Python-related questions, meet new Pythonistas, learn about new and trending topics in the community, and get feedback and tips on Python code and projects.

(`是也乎`:

![Office](http://ydlj.zoomquiet.top/ipic/2020-12-09-ScreenShot%202020-12-09%2009.27.18.jpg)

嗯哼,发现和 自怼圈 付费定期聊天类似,
如果大家学不动, 和专家们聊天儿也是好的.

嘦付费.

)





- [如何在 Heroku 上的 Django 中设置 Tailwind CSS](https://pycoders.com/link/5326/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

Have a Django app on Heroku and want to use Tailwind CSS? In this tutorial, you’ll see how to configure Tailwind for a Django project and set up Heroku to build your CSS file.

(`是也乎:`

> Tailwind ~ 尾风? -> 顺风

Bootstrap 式傻瓜框架,
只是, 对类命名进行了更加直觉的嗯哼.

问题是引用资源是否够大家任性使用...
Bootstrap 有 github 支持, CDN 到处所有,
新人上来...

)



- [在 PyQt 用 enumerate( ) 和 Python GUI 循环](https://pycoders.com/link/5320/web)
    + REAL PYTHON 
    + podcast

If you’re coming to Python from a different language, you may not know about a useful tool for working with loops, Python’s built-in enumerate function. This week on the show, David Amos is here, and he has brought another batch of PyCoder’s Weekly articles and projects. Along with the Real Python article covering the details of the enumerate function, we also talk about another article about constructing Python graphical user interface elements in PyQt.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-12-09-ScreenShot%202020-12-09%2010.24.34.jpg)

)


- [Atheris Python Fuzzer 发布](https://pycoders.com/link/5319/web)
    + IAN ELDRED PUDNEY

Get started with fuzzing, a technique for automatically finding bugs in Python code by repeatedly trying various inputs to your program, using Google’s newly open-sourced Python fuzzer called Atheris.

(`是也乎:`

fuzzing ~ 模糊测试, 也变成显学了,


)


- [在int中存储列表](https://pycoders.com/link/5333/web)
    + IAN TAYLER

For a fun exercise, learn how you can leverage Python’s unlimited integer precision to encode and store lists of any size as a single integer. Because, why not?

(`是也乎:`

> ...如何利用Python无限的整数精度将任意大小的列表编码和存储为单个整数...

这个思路令人想起一则 SiFi 情节:

> 宇宙间最大图书馆

将所有图书文字加密, 编辑为一个连续数字,
作为一个无理小数本体;

然后,找到这个无理数的精确整数比, 
类似 113/355 这种,

然后, 将这个比例, 刻为一个稳定材料制造的小棍上,
那么, 整个儿图书馆的所有内容,
就变成了一个小棍物理外观上携带的一个点儿;

到任何稳定环境中, 只要精确测量出来那个点所在位置分割小棍的比例,
一除就获得了所有加密数字,
再根据解密原则就能还原出所有内容了,

很简洁吧?


)




- [Bazel 可复刻环境版本](https://pycoders.com/link/5322/web)
    + GASPARE VITTA 
    + • Shared by Gaspare Vitta

Learn how to identify sources of non-determinism in your project and to use Bazel to create reproducible, hermetic builds with Python.

- [Python+Websocket 高通量游戏消息服务器](https://pycoders.com/link/5318/web)
    + EDAQA MORTORAY

Learn how to create a message server using the Python WebSockets library capable of handling over 12,000 messages per second.


(`是也乎:`

look good,
不过, 想替代游戏行业 OTP 内部进程消息自动广播,
还早...

)

- [用 Python 和 Redis 构建 Markov-Chain IRC Bot](https://pycoders.com/link/5323/web)
    + CHARLES LEIFER

Looking for a fun project to tackle? Learn how to build an IRC bot!



   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [bodywork-core: ML-Ops 框架](https://pycoders.com/link/5324/web)
    + GITHUB.COM/BODYWORK-ML

(`是也乎:`


DevOps 之后, MLOps 来了,
然后 AIOps 也可以期待了?

)


- [atheris: Python 模糊测试框架](https://pycoders.com/link/5311/web)
    + GITHUB.COM/GOOGLE

(`是也乎:`

Google 出品,必须小心...

)


- [PyTCP: Python 的功能性 TCP/IP 堆栈](https://pycoders.com/link/5306/web)
    + GITHUB.COM/CCIE18643

(`是也乎:`

等等,为什么没有 PyUDP ?

)


- [Skybolt: 渲染引擎和航空航天仿真工具](https://pycoders.com/link/5325/web)
    + GITHUB.COM/PIRAXUS

(`是也乎:`

所以, 流畅的飞行, 不再是 GHIBLI 的专属特技了?

)


- [irc: 从头开始搞的 Irc 库](https://pycoders.com/link/5307/web)
    + GITHUB.COM/COLEIFER

(`是也乎:`

当年 GTalk 多火哪, 什么库都有,
结果多源头自宫后, 什么都没留下来;

IRC 的问题是...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5313/web)
    + December 9, 2020

(`是也乎:`

![Office](http://ydlj.zoomquiet.top/ipic/2020-12-09-ScreenShot%202020-12-09%2009.27.18.jpg)

每周定期了?

> ...members only

)

- [⋅ PyCode Conference 2020 (Online)](https://pycoders.com/link/5327/web)
    + December 11 to December 13, 2020

- [⋅ PyCon Tanzania 2020](https://pycoders.com/link/5312/web)
    + December 14 to December 16, 2020
    + 非洲


![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)

- [PyCon2020中国, 明年见](https://mp.weixin.qq.com/s/9u4NP0CAzZMqy96C9y-OHg)
    + 11.28~29
    + 在线

(`是也乎:`

[PyCon20深圳 大妈 暖场小单口](https://mp.weixin.qq.com/s/OrHA4vimeHUYDROQ9G75GA)

并实锤可用神器:
[NixOS - NixOS Linux](https://nixos.org/)

nix 可以跨语言非Docker 将开发和运行时环境精确锁定.

以及 PyCon19广州 的坑终于填上了:

- [欢迎使用 lightning ](https://gitmen.gitee.io/lightning-doc/)
    + [GitHub](https://github.com/git-men/lightning)
    + [OSC](https://gitee.com/gitmen/lightning)

基于Django的无代码Admin + 低代码开发框架


)


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

None 

# PS:
- 首发: [Issue 450 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-450.html)
- 修订: [issue-450.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-450.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



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
>> NN 4222


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/450)






