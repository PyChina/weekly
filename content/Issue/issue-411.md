Title: Issue 411
Slug: issue-411
Date: 2020-03-12 11:42
Tags: Weekly,Python,pycoders,ZH

> 2020 应该如何享用 Jupyter?



原文: [PyCoder's Weekly - Issue #411](https://pycoders.com/issues/411)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200311 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200311 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------



- [Post-Mortem Python 绘图](https://pycoders.com/link/3749/web)
    + ANDY JONES

Who loves debugging things that only fail occasionally? Just me? Maybe you need to check out Andy Jones’ extract() function that “magically” extracts a caller’s environment into an IPython interpreter session. Mix in a little post-mortem debugging with Jupyter’s %debug magic command, and you’ll be painlessly debugging finicky code in no time.

(`是也乎:`

神奇的事后验尸, 
`extract()` 能将调用者环境装配人 Jupyter 进行细致的检验.


)


- [2020 年如何用 Jupyter 笔记本](https://ljvmiranda921.github.io/notebook/2020/03/06/jupyter-notebooks-in-2020/)
    + LJ MIRANDA

In this first of a three-part blog post, LJ Miranda surveys the data science landscape and discusses the forces that push data science tools to evolve.

(`是也乎:`

一个系列, 刚刚发布第一篇, 
1: 数据科学的笔记本
/2: 2020我的笔记本
/3: 笔记本的未来..

是的, 笔记本从实体的, 到电脑形态, 现在又是一种可计算文档的指代了...

其实, 对 Jupyter 的发展是看好的, 但是, 对其最终产品形态不明朗,
因为 notebook 形式非常创意的将 开发/调试/笔记/发行 很好的揉合在一起;
唯独没对运行时有考虑...这就比较尴尬了...

![Jupyter](http://ydlj.zoomquiet.top/ipic/2020-03-12-axis_with_jupyter_forces.png)

)

- [思考 psycopg3](https://pycoders.com/link/3735/web)
    + DANIELE VARRAZZO

A core maintainer of the popular psycopg2 PostgreSQL adapter for Python discusses breaking changes he would like to see in a hypothetical pyscopg3 project, including better query/parameter separation, more sensible context manager behavior with connections, and async support.


(`是也乎:`


![psycopg3](http://ydlj.zoomquiet.top/ipic/2020-03-12-architecture.jpg)


当大家大规模从 MySQL 迁移到 Pq , 各种模块就大发展起来了...

)


- [Alexa Python 开发: 构建和部署 Alexa Skill](https://pycoders.com/link/3744/web)
    + REAL PYTHON

In this tutorial, you’ll become an Alexa Python developer by deploying your own Alexa skill. You’ll build an application that users will interact with using voice commands to Amazon Alexa devices. Your skill will respond back with a random joke when invoked by the user!


(`是也乎:`

![Alexa](http://ydlj.zoomquiet.top/ipic/2020-03-12-ScreenShot%202020-03-12%2015.33.02.jpg)

Amazon 全家桶开发环境...


)


- [PyCon 2020 为 COVID-19 更新](https://pycoders.com/link/3748/web)
    + PYCON.BLOGSPOT.COM

“PyCon continues to closely monitor the Coronavirus (also known as COVID-19) situation. As of March 6, PyCon 2020 in Pittsburgh, Pennsylvania is scheduled to take place.”

(`是也乎:`

PyCon 官方还在使用 BLOGSPOT.COM,
最早也最稳定的 blog 服务.

)



## 讨论
> Discussions




- [关于 Windows CPython 安装程序中的“将Python 3.X添加到PATH”复选框…](https://pycoders.com/link/3733/web)
    + TWITTER.COM/BITECODE_DEV

An epic Twitter thread. It’s still active almost two weeks later, with tons of heavyweights chiming in.

(`是也乎:`

哦...Windows 永远的编程之敌.

)


- [什么导致了 \[*a\] to Overallocate?](https://pycoders.com/link/3746/web)
    + STACK OVERFLOW

Stefan Pochmann investigates memory allocation for three methods of creating a list from an iterable a: list(a), [x for x in a], and [*a]. The last method, [*a], always overallocates memory for the list.






## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [Python 在 GitHub Actions](https://pycoders.com/link/3745/web)    
    + HYNEK SCHLAWACK

“GitHub’s own CI called GitHub Actions has been out of closed beta for a while and offers generous free quotas and a seamless integration with the rest of the site. Let’s have a look on how to use it for an open source Python package.”


(`是也乎:`

GitHub 进入 微软后, 果然必定上了云, 
那么 AWS Lambda 对标物也就来了...

只是, 刚刚开始, 一切都会有的.

)



- [在 Python 模拟异步函数](https://pycoders.com/link/3723/web)
    + DINO COSTA

As the adoption of asynchronous Python grows, the ability to reliably test asynchronous code is increasingly important. In this tutorial, Dino Costa shows you how to leverage Future objects in Python 3.7 and the AsyncMock object added in Python 3.8 to easily test asynchronous functions.


- [语法统一很容易 !-)](https://pycoders.com/link/3751/web)
    + CASSIE JONES

Syntactic unification is the process of solving equations between symbolic expressions. Unification has applications in type systems and logic programming. In this article, Cassie Jones shows you how to implement a unification algorithm in just 30 lines of Python!


(`是也乎:`

呵..JONES, 语法问题不在系统, 而在人...

)

- [定义自己的 Python 函数](https://pycoders.com/link/3736/web)
    + REAL PYTHON

In this beginner tutorial, you’ll learn how to define and call your own Python functions. You’ll also learn about passing data to your function, and returning data from your function back to its calling environment.




- [从 Linux 发行版删除 Python 2 的叕一个冲击](https://pycoders.com/link/3753/web)
    + CHRIS SIEBENMANN 
    + opinion


“Everyone’s insistence on getting rid of Python 2 is magically transforming all of this perfectly functional and useful Python 2 code we have from an asset to a liability. You can imagine how I feel about that.”

(`是也乎:`

想正直替代 Python2 ? 还早...

)


- [理解 Django: Views 中的 Views](https://pycoders.com/link/3743/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

Django URLs expect to send a response back to a user.  Where does that response come from?  A Django view. This article looks into the fundamentals of views and how to use them in your project.

- [从头开始梯度下降](https://pycoders.com/link/3739/web)
    + PHILIPP MUENS

Gradient descent is one of the most fundamental optimization techniques used in machine learning. Learn the ins and outs of gradient descent by implementing it from scratch in Python.

(`是也乎:`

![Gradient Descent](http://ydlj.zoomquiet.top/ipic/2020-03-12-ScreenShot%202020-03-12%2014.58.37.jpg)

梯度下降来龙去脉...

)


- [咱们必须谈论这个Python/Gunicorn/Gevent/...](https://pycoders.com/link/3730/web)
    + RACHELBYTHEBAY.COM 
    + opinion

“Here’s what happens when you build around Python, Gunicorn, Gevent, and web requests instead of something more sensible.” Although pessimistic, this was an interesting read.

(`是也乎:`

一个悲观而有趣的观点...

)


- [Python 中定义 main 函式](https://pycoders.com/link/3732/web)
    + REAL PYTHON 
    + video

Learn how Python main functions are used and some best practices to organize your code so it can be executed as a script and imported from another module.

(`是也乎:`

![main](http://ydlj.zoomquiet.top/ipic/2020-03-12-ScreenShot%202020-03-12%2014.54.48.jpg)

真蟒, 开始加大短视频的输出了...

)



- [Episode #171: PEP 614 冷却 Python Decorators](https://pycoders.com/link/3728/web)    
    + PYTHON BYTES 
    + podcast

Real Python and PyCoder’s own David Amos guest hosts Python Bytes, talking about PEP 614, macOS menu bar apps with Python, test coverage, and more.

(`是也乎:`


真蟒 和 PyCoder 联合出品..
不过, 是真感觉 老爹 退休后, EPE 的接受加速了.

)


- [在 ZIP 压缩包中捆绑 Python 依赖项](https://pycoders.com/link/3725/web)
    + JÜRGEN HERMANN 
    + • Shared by Jürgen Hermann


Shipping dependencies for your scripts as a single file, built with shiv.

(`是也乎:`

![shiv](http://ydlj.zoomquiet.top/ipic/2020-03-12-python-shiv.png)

这个实用,算是最简洁的一种发行形式了...

```python
Using Pandas from .shiv/_lib-pandas_23b2…d2/site-packages/pandas 

Python path:
                                                Path
0                                  ~/bin/_lib-pandas
1                              /usr/lib/python38.zip
2                                 /usr/lib/python3.8
3                     /usr/lib/python3.8/lib-dynload
4  ~/.shiv/_lib-pandas_23b2bb7d64c26139950435a64d...
```

除了首次运行要解开和加载有点儿慢, 其它没什么不同.

)



- [信号处理在机器学习中的应用](https://pycoders.com/link/3754/web)
    + VAIDHEESWARAN ARCHANA



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [enum-switch: Python 基于枚举的Switch实现](https://pycoders.com/link/3747/web)
    + ROBERTO ALSINA

- [posthog: 开发人员友好的开源产品分析](https://pycoders.com/link/3719/web)
    + GITHUB.COM/POSTHOG

(`是也乎:`

![posthog](http://ydlj.zoomquiet.top/ipic/2020-03-11-ScreenShot%202020-03-11%2019.50.44.jpg)

针对开源项目的自动化分析;
收集并可视化网站/app 的所有事件, 以便辅助决策...
基于 Django.

)


- [karateclub: 关于图结构数据的无监督学习](https://pycoders.com/link/3722/web)
    + GITHUB.COM/BENEDEKROZEMBERCZKI

- [papermill: 参数化/可执行的分析笔记本](https://pycoders.com/link/3731/web)
    + GITHUB.COM/NTERACT

- [covid-19-analysis: 用于生成新冠趋势可视化报告的 Python 包](https://pycoders.com/link/3729/web)
    + GITHUB.COM/AARONWARD

(`是也乎:`


![covid](http://ydlj.zoomquiet.top/ipic/2020-03-11-ScreenShot%202020-03-11%2019.33.03.jpg)

可以说是 wuhan2020 的模块版.

)



- [aiohttp-swagger3: 根据不同 UI 后端显示对应 Swagger 文档](https://pycoders.com/link/3724/web)
    + GITHUB.COM/HH-H 
    + • Shared by hh-h

- [portion: 间隔时间的数据结构和操作](https://pycoders.com/link/3726/web)
    + GITHUB.COM/ALEXANDREDECAN 
    + • Shared by Alexandre Decan

- [pytest-responsemock: Pytest的简化请求模拟](https://pycoders.com/link/3742/web)
    + GITHUB.COM/IDLESIGN 
    + • Shared by pythonz









## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ EuroPython 2020: Call for Proposals Now Open](https://pycoders.com/link/3717/web)
    + 爱尔兰

- [⋅ PyMNTos](https://pycoders.com/link/3755/web)
    + March 12, 2020
    + USA
    + 明尼苏达

(`是也乎:`


![PyMNTos](http://ydlj.zoomquiet.top/ipic/2020-03-11-ScreenShot%202020-03-11%2019.25.42.jpg)

经常活动的 MeetUP, 场地也非常亲切...

)

- [⋅ Python Atlanta](https://pycoders.com/link/3740/web)
    + March 12, 2020
    + USA

- [⋅ HackBVICAM National Student’s Convention 2k20](https://pycoders.com/link/3720/web)
    + March 13 to March 14, 2020
    + ?

- [⋅ Python Miami](https://pycoders.com/link/3750/web)
    + March 14 to March 15, 2020
    + USA

- [⋅ DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/3741/web)
    +  March 14, 2020
    + USA,TX

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/3737/web)
    + March 14, 2020
    + 印度



## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [Academic-nCoV/2019-nCoV Wiki](https://github.com/Academic-nCoV/2019-nCoV/wiki)
    + github


(`是也乎:`

![nCoV 最新海外信息](http://ydlj.zoomquiet.top/ipic/2020-03-11-ScreenShot%202020-03-11%2019.32.08.jpg)


文科生的战斗, 虽然没办法象 wuhan2020 们那样快速组织工程师,
先于国家完成各种实用系统;

但是, 文科生通过大量海外报道的浏览/对比/翻译/报道/...

可以帮助人们通过真实世界的反应, 来更好的理解当前状态.

而且, 一个完全没有技术基础的文科团队, 自然通过 github 完成所有协同,
实在..感动 -> github 太好用了.

)


# PS:
- 首发: [Issue 411 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-411.html)
- 修订: [issue-411.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-411  .md)


-------------
>> NN 3949

好文笔,感叹号年度配额: **1/3**

-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):


```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
全国大会: PyChina (订阅号: PyChinaOrg)
本地社区: 
    GDG珠海 (订阅号: GDG-ZhuHai)
    TFUG珠海 (订阅号: ZH_TFUG)
历史吐糟: Chaos42 (订阅号 PythoniCamp)
```

-------------



