Title: PyCoder 562
Slug: issue-562
Date: 2023-02-01 11:42
Tags: Weekly,Python,pycoders,ZH


> 箴言之禅


原文: [PyCoder's Weekly - Issue #562](https://pycoders.com/issues/562)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230201 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230201 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [用 Apache Airflow 编排大型和小型项目](https://pycoders.com/link/10241/web)
    + REAL PYTHON 
    + PODCAST

Have you worked on a project that needed an orchestration tool? How do you define the workflow of an entire data pipeline or a messaging system with Python? This week on the show, Calvin Hendryx-Parker is back to talk about using Apache Airflow and orchestrating Python projects.


(`是也乎:`

什么是编排?
为什么数据/消息的流通会变来变去?


)


(`是也乎:`

![Airflow](https://ipic.zoomquiet.top/2023-02-01-zshot%202023-02-01%2011.17.44.jpg)

)

- [为什么我喜欢 Nox](https://pycoders.com/link/10267/web)
    + HYNEK SCHLAWACK

Both nox and tox are multi-environment testing tools. This opinion piece by Hynek compares and contrasts them and explains why increasingly he is using nox.

(`是也乎:`

下一代更好的多系统测试工具应该叫 `mox`

)



- [模拟断开的数据库连接以在 Django 中进行测试](https://pycoders.com/link/10266/web)
    + NEIL KAKKAR

This article covers three different options for effectively testing Django database access and failure recovery when the database connection is not there.

- [Bleach 6.0.0 发布和弃用](https://pycoders.com/link/10250/web)
    + BLUESOCK.ORG

Bleach is an HTML sanitizing library. 6.0 has been released, along with the announcement that the package is being deprecated. The library is dependent on html5lib which is no longer maintained, the maintainers of Bleach are giving notice that their package will stop being updated after a year.

(`是也乎:`

代码好歹有 语法树, HTML 这东西怎么净化? 人家设计的就是可以乱来的

)


- [PEP 704: 默认需要虚拟环境](https://pycoders.com/link/10269/web)
    + PYTHON.ORG

(`是也乎:`

好象 Guido 退休后, PEP 增长加速了...

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [关于 Python 打包生态系统的思考](https://pycoders.com/link/10256/web)
    + HACKER NEWS

There’s been lots of chatter about packaging in Python of late, this discussion centers around Pradyun Gedam’s excellent article. For more on the same topic see last issue’s How to improve Python packaging, or why fourteen tools are at least twelve too many as well.

- [Breaking the Snake: Python 如何从 2 到 3](https://pycoders.com/link/10255/web)
    + HACKER NEWS

This discussion spawned from Diego Crespo’s article of the same name talks about the transition that somehow everyone is still interested in talking about.


(`是也乎:`

一段艰难的历史, 也是神奇的故事...

)

-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 标准 REPL: 快速尝试代码和想法](https://pycoders.com/link/10271/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use the Python standard REPL (Read-Eval-Print Loop) to run your code interactively. This tool will allow you to test new ideas, explore and experiment with new tools and libraries, refactor and debug your code, try out examples, and more.

(`是也乎:`


![REPL](https://ipic.zoomquiet.top/2023-02-01-zshot%202023-02-01%2011.00.07.jpg)

REPL 的确是 Python 一大特色,
以往只有 数据库产品才有...

)


- [Python 中的线性代数: 矩阵求逆和最小二乘法](https://pycoders.com/link/10253/web)
    + REAL PYTHON

In this tutorial, you’ll work with linear algebra in Python. You’ll learn how to perform computations on matrices and vectors, how to study linear systems and solve them using matrix inverses, and how to perform linear regression to predict prices based on historical data.


(`是也乎:`

![Algebra](https://ipic.zoomquiet.top/2023-02-01-zshot%202023-02-01%2010.59.58.jpg)

大学高等数学没通的, 看了也白看...

)



- [Python 中的距离和接近度分析](https://pycoders.com/link/10261/web)
    + KYLE WALKER

“Spatial data science projects frequently require the calculation of proximity to resources.” This article shows you how to calculate proximity in Python code using two different techniques: Euclidean and driving times. Examples use geopandas and routingpy packages.

- [我在 20 年的软件工程师生涯中学到的 20 件事](https://pycoders.com/link/10257/web)
    + JUSTIN ETHEREDGE

Justin writes a list of things he has learned over his past 20 years in development. He starts by stating how context is important and that his lessons are from small teams with an emphasis on productivity and being tool agnostic.

(`是也乎:`

20年程序猿生涯的感悟...

对于俺,只有一条: `跟对人, 跟得上` 足以飞升

当然文章是好文章,大妈快译在: [20年来作为软件工程师学到的20件事 - be Rustaceans](https://rs.101.so/log/20-things-ive-learned-in-my-20-years-as-a-software-engineer.html#important-read-this-first)

)


- [一个开源 Python 项目 CI 管道](https://pycoders.com/link/10254/web)
    + BRENTON CLEELAND

This posting describes Brenton’s Python Continuous Integration (CI) pipeline setup, from using a pyproject.toml file, to the tools such as black and coverage he uses, to GitHub actions to glue it all together.

(`是也乎:`

GHA 之后, 还有谁能超越?

)


- [用于性能优化的 Python 绑定](https://pycoders.com/link/10252/web)
    + ALEX HAGIOPOL

“This article describes techniques to accelerate a Python codebase by exposing parallelized C++ functions using PyBind.” The example in the article achieves a 3x speed-up through this technique.

- [Python 中的单引号 (') 或双引号 (") 到底怎么搞?](https://pycoders.com/link/10242/web)
    + MEDIUM.COM/PYTHONIQ 
    + • Shared by Marcin

The article addresses the following question. Many claim you should prefer single over double quotes in Python. Should you?


(`是也乎:`

是的, 其实有差别,不过,可以忽略

)


- [用 Polar 替换 Pandas。 实用指南](https://pycoders.com/link/10270/web)
    + DANIEL BEACH

Polars is becoming a popular alternative to Pandas. This article compares the two and shows you a path to Polars.

(`是也乎:`

关键是兼容 Jupyter 之类嘛?

)


- [箴言之禅](https://pycoders.com/link/10247/web)
    + LANE WAGNER

Inspired by the Zen of Python and similar lists, this is list of Zen Proverbs for programming.


(`是也乎:`

![Proverbs](https://ipic.zoomquiet.top/2023-02-01-zshot%202023-02-01%2010.54.12.jpg)

20 条偈语，有关构建更好的软件, 适用一切语言/技术桟:

```
Optimize for simplicity first
Write code for humans, not computers
Reading is more important than writing
Any style is fine, as long as it’s black
There should be one way to do it, but seriously this time
Hide the sharp knives
Changing the rules is better than adding exceptions
Libraries are better than frameworks
Transitive dependencies are a problem
Dynamic runtime dependencies are a bigger problem
API surface area is a liability
Returning early is a good thing
Use more plain text
Compiler errors are better than runtime errors
Runtime errors are better than bugs
Tooling is better than documentation
Documentation is better than nothing
Configuration sucks, but so does convention
The cost of building a feature is its smallest cost
Types are one honking great idea – let’s do more of those!
```


)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [ipyflow: Jupyter 的 IPython 内核](https://pycoders.com/link/10249/web)
    + GITHUB.COM/IPYFLOW

(`是也乎:`

追加了执行流程可视化提示的引擎

)


- [monorepo: JupyterLab 笔记本中的电子表格](https://pycoders.com/link/10246/web)
    + GITHUB.COM/MITO-DS


(`是也乎:`

在线表格化 Pandas dataframes ...

等于低代码平台又一种形态了?

)

- [fugue: 分布式计算的统一接口](https://pycoders.com/link/10262/web)
    + GITHUB.COM/FUGUE-PROJECT

- [python-benedict: 具有键列表/键路径支持的字典子类](https://pycoders.com/link/10259/web)
    + GITHUB.COM/FABIOCACCAMO

- [sematic: 一个开源机器学习管道开发工具包](https://pycoders.com/link/10240/web)
    + GITHUB.COM/SEMATIC-AI





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [STL Python](https://pycoders.com/link/10263/web)
    + February 1, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10268/web)
    + February 1, 2023

- [PyStaDa](https://pycoders.com/link/10245/web)
    + February 1, 2023

- [Canberra Python Meetup](https://pycoders.com/link/10264/web)
    + February 2, 2023

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/10260/web)
    + February 2, 2023

- [Fosdem 2023](https://pycoders.com/link/10243/web)
    + February 5 to February 6, 2023




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 562 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-562.html)
- 修订: [issue-562.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-562.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

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

好文笔,感叹号年度配额: **0/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF562D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF562D4Q90XdDA7g):



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





