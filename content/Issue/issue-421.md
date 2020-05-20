Title: Issue 421
Slug: issue-421
Date: 2020-05-20 11:42
Tags: Weekly,Python,pycoders,ZH


> 2019 Python 开发者问卷结果出来了


原文: [PyCoder's Weekly - Issue #421](https://pycoders.com/issues/421)

![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/421)


![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200520 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200520 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [给 Pythonistas 的分析 Python vs JavaScript for  – Real Python](https://realpython.com/python-vs-javascript/)
    + REAL PYTHON

Python and JavaScript are two of the most popular programming languages in the world. In this tutorial, you’ll take a deep dive into the JavaScript ecosystem by comparing Python vs JavaScript. You’ll learn the jargon, language history, and best practices from a Pythonista’s perspective.

(`是也乎:`


![Pythonistas](http://ydlj.zoomquiet.top/ipic/2020-05-20-ScreenShot%202020-05-20%2009.29.15.jpg)


没什么可比的, JS 除了是现今唯一一个真正全栈开发语言之外, 基本没什么吸引力,
而且这点也在被 Py 慢慢赶上...

PS: node.js 创始人放弃 node 另开新坑也说明问题所在了.

)


- [Python 开发调查2019年结果](https://pycoders.com/link/4154/web)
    + JETBRAINS.COM

The results of the 2019 Python Developers Survey, a joint effort from JetBrains and the Python Software Foundation, have been released. Some interesting takeaways: Flask continues to grow as the most popular web framework, about half of Python developers report using pytest for testing, and VS Code continues to grow rapidly in popularity with almost 1/4 Python developers using it as their main editor. Check it out!


(`是也乎:`

仅仅根据 jetbrain 一家内部数据, 也算是代表一部分真实了.

)

- [通过在公共存储库中反编译 Python 字节码来发现秘密](https://pycoders.com/link/4143/web)
    + JESSE LI

If you commit .pyc files to GitHub, or other public source control repositories, then all of your application secrets, such as AWS credentials and database passwords, can be reconstructed from the bytecode contained in these files.

- [Python 缓存整数](https://pycoders.com/link/4140/web)
    + ARPIT BHAYANI

Did you know that Python caches integers between -5 and 256? That is, these integer values are singletons, which means that any reference to one of them in your code references the same object in memory. Learn why Python does this and more in this short, but informative, article.

(`是也乎:`

老爹自己从来不说这种技术细节...

)


- [优化Django ORM查询](https://pycoders.com/link/4153/web)
    + ROCIO ARAMBERRI

The Django ORM is powerful, but also abstract. It can give the illusion that operations are inexpensive. Learn how the ORM works under the hood and how you can optimize Django ORM queries to improve the performance of your web apps.

- [Python GitHub迁移工作组在呼吁志愿者！](https://pycoders.com/link/4157/web)
    + PYTHON SOFTWARE FOUNDATION

The PSF is looking for volunteers to participate in a workgroup that will be involved with Python’s migration from bugs.python.org to GitHub.

- [Python 3.9.0b1 现在可用于测试](https://pycoders.com/link/4164/web)
    + CPYTHON DEV BLOG

“Python 3.9 is still in development. This release, 3.9.0b1, is the first of four planned beta release previews. Beta release previews are intended to give the wider community the opportunity to test new features and bug fixes and to prepare their projects to support the new feature release.”

- [Django 3.1 Alpha 1 发布](https://pycoders.com/link/4174/web)
    + DJANGO SOFTWARE FOUNDATION

(`是也乎:`

Django 千秋万代一统江湖,
不过, 俺还在用 Bottle.

)


- [Python 3.8.3 已发布](https://pycoders.com/link/4141/web)
    + CPYTHON DEV BLOG


(`是也乎:`

昨晚刚刚安装上, 编译速度比 2.7.12 还要快

)





































## 讨论
> Discussions


- [在 CSV,JSON,XML和SQL/NoSQL数据库之间的决策流程是什么？](https://pycoders.com/link/4165/web)
    + REDDIT

With so many formats for storing structured data, how do you choose which one to use?

(`是也乎:`

历史,都是历史,
现在不都是上 gRPC 用 protobuffer 了?

)


- [为什么这两个函数具有不同的输出?](https://pycoders.com/link/4152/web)
    + REDDIT

How well do you know how generator expressions and for loops work?

- [是否在项目中使用Walrus运算符 := ?](https://pycoders.com/link/4150/web)
    + REDDIT

Do you walrus, coo coo ca choo?

(`是也乎:`

才嫑.

象海象很 益rz.

)



























































## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [如何弃用 PyPI 软件包](https://pycoders.com/link/4138/web)
    + PAUL MCCANN

How do you deprecate a Python package that you’ve published to PyPI and want people to stop using? Should you just delete? Check out this guide to several ways to accomplish this task. You can also try the new yank feature supported by PyPI.


(`是也乎:`

yank 的广告.

)


- [Python 的子解释器](https://pycoders.com/link/4172/web)
    + JAKE EDGE

PEP 554 exposes Python’s existing subinterpreter support so that Python programs can use multiple separate interpreters. The PEP was created in 2017, and the author Eric Snow thinks it’s time to finally accept or reject the proposal.



- [团队采用 Python 的经验教训](https://pycoders.com/link/4169/web)
    + AKSHAY PRABHU

How do you go about rewriting legacy ETL jobs in Python when you’re not Python developers?

(`是也乎:`

简单说, 嫑用 Python 2
)


- [提升 Python 素养并找到值得研究的 Python 项目](https://pycoders.com/link/4167/web)
    + REAL PYTHON 
    + podcast

In your quest to become a better developer, how do you find Python code that is at your reading level? What are good code bases or projects to study? What are the things holding you back from leveling up your Python literacy? This week we have Cecil Phillip on the show to discuss all of these common questions. Cecil is a Senior Cloud Advocate at Microsoft.

(`是也乎:`

不能简单看 Star 数量了 .

)


- [用 Python 实施 gRPC 服务器](https://pycoders.com/link/4173/web)
    + TOWARDSDATASCIENCE.COM 
    + • Shared by Martin Heinz

Your next API doesn’t need to be built with REST and JSON. How about gRPC and Protocol Buffers for better performance and structure?

(`是也乎:`

等等, 为什么呢? 怎么就不应该上 RESTful 了?

)


- [用 Python 构建 Markdown 到 HTML 转换管道](https://pycoders.com/link/4155/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz

(`是也乎:`

可惜没有哪个项目托管平台内置这类流水线.

)


- [解开 Python 装饰器](https://pycoders.com/link/4160/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

- [Data Elixir: 数据科学通讯](https://pycoders.com/link/4137/web)
    + DATAELIXIR.COM

Data Elixir is an email newsletter that keeps you on top of the tools and trends in Data Science. Curated weekly with top picks from around the web.


(`是也乎:`

等等, 这个难道不是 Elixir 的广告?

)



















































## 好物
> Interesting Projects, Tools and Libraries, Projects & Code



- [azure-sdk-for-python: 适用 Python 的 Azure SDK](https://pycoders.com/link/4145/web)
    + GITHUB.COM/AZURE

(`是也乎:`

想用来的, 结果发现本地测试开发环境比 Heroku 复杂100倍,
退散了.

)


- [py-spy: Python 程序的采样探查器](https://pycoders.com/link/4147/web)
    + GITHUB.COM/BENFRED

(`是也乎:`

叕一个性能检验器,
不过,这个神奇的能象 htop 那样儿动态展示整个儿运行时资源变化情况排名,
很666

)


- [kneed: Python 中的拐点检测](https://pycoders.com/link/4148/web)
    + GITHUB.COM/ARVKEVI


(`是也乎:`

![kneed](http://ydlj.zoomquiet.top/ipic/2020-05-20-ScreenShot%202020-05-20%2011.13.08.jpg)

一键找到 `膝盖`;
这名字起的太传神了.


)

- [detectron2: FAIR 的下一代物体检测和分割平台](https://pycoders.com/link/4159/web)
    + GITHUB.COM/FACEBOOKRESEARCH

- [zipfly: 编写没有内存膨胀的大型 ZIP 存档](https://pycoders.com/link/4151/web)
    + GITHUB.COM/BUZONIO

(`是也乎:`

意思是, 解开巨型 .zip 早已不用看内存眼色了?

)


- [macropy: Python中的宏：准引号，案例类，LINQ等！](https://pycoders.com/link/4171/web)
    + GITHUB.COM/LIHAOYI

(`是也乎:`

```
print(list(map(f[_[0]], ['omg', 'wtf', 'bbq'])))
# ['o', 'w', 'b']

print(list(reduce(f[_ + _], ['omg', 'wtf', 'bbq'])))
# 'omgwtfbbq
```

嗯哼? 宏这根魔法大棍也混入 Python 了?

![macropy](http://ydlj.zoomquiet.top/ipic/2020-05-20-ScreenShot%202020-05-20%2009.56.49.jpg)

神奇的是, Python 自古就有 AST 自省,
但是, 一直没有成熟的宏机制...


)

- [py-pdf-parser: 从PDF提取信息的新工具](https://pycoders.com/link/4162/web)
    + GITHUB.COM/JSTOCKWIN 
    + • Shared by Jake Stockwin

(`是也乎:`

永远的 pdf , 很难想象很多技术, 都是一发明就已经完满, 几乎没有改进的余地.

)


- [Little Ball of Fur: 用于图形采样的NetworkX扩展库](https://pycoders.com/link/4166/web)
    + GITHUB.COM/BENEDEKROZEMBERCZKI 
    + • Shared by Benedek Rozemberczki


(`是也乎:`

所以叫小毛球.

)













































## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ Python Web Conf 2020 (Remote)](https://pycoders.com/link/4146/web)
    + June 17–19, 2020

(`是也乎:`

真正名副其实的网络大会

)







## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp8py 已经开始报名(能开发票 ;-)

![报名](http://ydlj.zoomquiet.top/ipic/2020-04-21-camp8py-barnner-zip.jpg)

```

课程规划:
    报名截止 2020.5.24
    正式开课 2020.5.31
    课程结束 2020.7.12

```
详情 => [蟒营™ Python 入门班第8期](https://py.101.camp/)



- [技术雷达 Vol.22 / 有态度的前沿技术解析](https://assets.thoughtworks.com/assets/technology-radar-vol-22-cn.pdf)
    + ThoughtWorks

# PS:
- 首发: [Issue 421 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-421.html)
- 修订: [issue-421.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-421.md)


-------------
>> NN 4019

好文笔,感叹号年度配额: **1/3**

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



