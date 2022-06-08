Title: PyCoder 528
Slug: issue-528
Date: 2022-06-08 11:42
Tags: Weekly,Python,pycoders,ZH


> 如何摆脱教程地狱? 当然不是爱...


原文: [PyCoder's Weekly - Issue #528](https://pycoders.com/issues/528)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220608 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220608 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Django 静态文件和模板](https://pycoders.com/link/8859/web)
    + WILL VINCENT

“Static files like CSS, JavaScript, and fonts are a core piece of any modern web application. They are also typically confusing for Django newcomers since Django provides tremendous flexibility around how these files are used. This tutorial will demonstrate current best practices for configuring static files in both local development and production.”

- [用 pandas 和 NumPy 进行数据清理](https://pycoders.com/link/8858/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to clean up messy data using pandas and NumPy. You’ll become equipped to deal with a range of problems, such as missing values, inconsistent formatting, malformed records, and nonsensical outliers.

- [Optimize Python Code Inefficiencies and Latency With Datadog Application Monitoring](https://pycoders.com/link/8825/web)
    + DATADOG
    + SPONSOR

Datadog’s APM generates detailed flame graphs to provide you with deeper insights into code-level performance enabling teams to identify bottlenecks and latency in their Python code. Navigate seamlessly between app traces, logs and metrics to resolve app issues fast. 
[Optimize Python Code Inefficiencies and Latency With Datadog Application Monitoring](https://pycoders.com/link/8825/web)

(`是也乎:`

![Datadog](https://cdn.pycoders.com/a2e6b970c5925d0dbfadfdb0618f7cee)

事实证明, logo 可爱能提高转化率

)


- [简要了解 CPython 字符串](https://pycoders.com/link/8838/web)
    + ONDŘEJ MĚKOTA

“Have you ever noticed that a string with just a few characters in Python uses several dozen bytes of memory? We handle a lot of short strings and I have been wondering why Python seems to store strings seemingly so inefficiently.”

- [加速发布 Python 3.11.0b3](https://pycoders.com/link/8866/web)
    + CPYTHON DEV BLOG

- [Django Bugfix Release: 4.0.5](https://pycoders.com/link/8847/web)
    + DJANGO SOFTWARE FOUNDATION

- [请求包的域名抢注攻击](https://pycoders.com/link/8850/web)
    + JOSSEF HARUSH

- [Python News: What’s New From May 2022](https://pycoders.com/link/8833/web)
    + REAL PYTHON

(`是也乎:`

![News](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2011.45.08.jpg)

)



-----------------------------------------
## 探讨/吐糟
> Discussions



- [如何摆脱教程地狱?](https://pycoders.com/link/8860/web)
    + REDDIT

(`是也乎:`

这真的是所有在线教育的天坑,
所以, 有了 [蟒营®101.camp 开源网络课程框架](https://doc.101.camp/)

教育不在灌输, 而在召唤...召唤出自主思考以及探索...
这过程中, 课程提供的其实应该是信心: 

    我能学会

然后, 一切神奇就发生了...

)


- [Ask HN: 作为软件工程师，我们是否把自己搞砸了?](https://pycoders.com/link/8848/web)
    + HACKER NEWS

(`是也乎:`

是的 , HW 

> news.ycombinator.com

其实, 并不存在

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [嗯哼? 开源供应链安全/大家都在哪儿?](https://pycoders.com/link/8841/web)
    + JÜRGEN GMACH 
    + • Shared by Jürgen Gmach

Recent security issues with ctx on PyPI followed shortly by the discovery of some typeosquatting has everyone re-examining their package supply chain. Jurgen writes about finding weirdness with two of the most popular packages out there.

- [如何分析 Python 代码](https://pycoders.com/link/8871/web)
    + JOHN LOCKWOOD

No matter how good you are, sometimes your code just runs slow. Learning how to properly profile your software to identify and fix bottlenecks is a useful skill. This article talks about what you need to know to measure your code’s performance and how to use the cProfile, profile, and timeit libraries, along with others.


- [LBYL vs EAFP: 在 Python 中预防或处理错误](https://pycoders.com/link/8837/web)
    + REAL PYTHON

In this tutorial, you’ll learn about two popular coding styles in Python: look before you leap (LBYL) and easier to ask forgiveness than permission (EAFP). You can use these styles to deal with errors and exceptional situations in your code. You’ll dive into the LBYL vs EAFP discussion in Python.

(`是也乎:`


![Handling](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2011.25.49.jpg)

重要姿态选择:

    EAFP ~ “Easier to Ask for Forgiveness than Permission.”
        请求宽恕比许可更容易
    LBYL ~ “Look Before You Leap”
        三思而后行 

先上车再补票, 还是先结婚再上车?
普通人的选择很明显了...


)


- [用 Dask 管理大型 Python 数据科学项目](https://pycoders.com/link/8855/web)
    + REAL PYTHON 
    + PODCAST

What do you do when your data science project doesn’t fit within your computer’s memory? One solution is to distribute it across multiple worker machines. This week on the show, Guido Imperiale from Coiled talks about Dask and managing large data science projects through distributed computing.

(`是也乎:`


![Dask](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2011.23.58.jpg)

真正在开始使用互联网资源的姿势...


)


- [软件供应链中的大家](https://pycoders.com/link/8845/web)
    + SETH MICHAEL LARSON

Behind all the most popular packages you routinely pip install are a host of people whose names you likely don’t recognize. This thoughtful article talks about what we as a coding community can do to acknowledge maintainers more and contribute.


(`是也乎:`


![Chain](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2011.22.28.jpg)

pip 值得升级追加这种信息哪,
每天都值得知道自己当前工作, 有多少先贤在看着...


)


- [TDD 实践/使用 Django 时间 API](https://pycoders.com/link/8842/web)
    + BRENTON CLEELAND

This is a step-by-step coding Kata based on a workshop that Brenton ran at DjangoConEU 2018. It gives you practice in using a Test-Driven-Development approach by writing tests for a “get time” API in Django.

- [用 FastAPI/MongoDB 和 Beanie 构建 CRUD 应用程序](https://pycoders.com/link/8863/web)
    + ABDULAZEEZ ABDULAZEEZ ADESHINA 
    + • Shared by Abdulazeez Abdulazeez Adeshina

A step-by-step tutorial on developing an asynchronous API with FastAPI and MongoDB using the Beanie ODM library to interact with MongoDB .

(`是也乎:`


![ABDULAZEEZ](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2011.20.14.jpg)



)



- [让 pip 安装慢一点](https://pycoders.com/link/8839/web)
    + ITAMAR TURNER-TRAURING

Installing packages with pip, Poetry, and Pipenv can be slow. Learn how to ensure it’s not even slower, and a potential speed-up.

- [用 Python 进行 Web3 应用程序开发速成课程](https://pycoders.com/link/8828/web)
    + TYLER LANGLOIS

A step-by-step tutorial on how to send your first transaction on the Ethereum blockchain using Python and the web3 package.


(`是也乎:`

针对 [Ethereum](https://en.wikipedia.org/wiki/Ethereum)
的 Python 开发指南

)






-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [huey: Python 叕一个小任务队列](https://pycoders.com/link/8831/web)
    + GITHUB.COM/COLEIFER


(`是也乎:`

![huey](https://ipic.zoomquiet.top/2022-06-08-zshot%202022-06-08%2010.36.47.jpg)

是作者小喵的名字...

)


- [django-managerie: 在 Admin 中公开 Django 命令](https://pycoders.com/link/8869/web)
    + GITHUB.COM/AKX

- [pyAudioProcessing: 音频特征提取和分类](https://pycoders.com/link/8856/web)
    + GITHUB.COM/JSINGH811

- [pyperformance: Python 性能基准套件](https://pycoders.com/link/8852/web)
    + GITHUB.COM/PYTHON

(`是也乎:`

因为老爹承诺了提高 Py 性能, 所以各种性能检验工具就爆了...

)


- [ga-extractor: 提取 GA 数据的工具](https://pycoders.com/link/8830/web)
    + GITHUB.COM/MARTINHEINZ




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Python Meeting Düsseldorf](https://pycoders.com/link/8836/web)
    + June 8, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8861/web)
    + June 8, 2022

- [Python North East](https://pycoders.com/link/8867/web)
    + June 8, 2022

- [Python Live: An Introduction to Practical MLOps](https://pycoders.com/link/8834/web)
    + June 9, 2022

- [Python Miami](https://pycoders.com/link/8853/web)
    + June 11 to June 12, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅

![ACM-O](https://ipic.zoomquiet.top/2022-04-27-zshot%202022-04-27%2009.22.46.jpg)

(`是也乎:`


谈崩了, 之前通过 ACM 会员可以每年 $25 享受 O'REILLY 在线图书馆服务...现在没了

)

-----------------------------------------
# PS:

- 首发: [Issue 528 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-528.html)
- 修订: [issue-528.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-528.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF528D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF528D4Q90XdDA7g):



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





