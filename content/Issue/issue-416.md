Title: Issue 416
Slug: issue-416
Date: 2020-04-15 14:42
Tags: Weekly,Python,pycoders,ZH

>  嫑再将你 Python 模块命名为 utils



原文: [PyCoder's Weekly - Issue #416](https://pycoders.com/issues/416)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200415 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200415 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [用 Python 和 OpenCV 开源工具实现虚拟背景](https://pycoders.com/link/3932/web)
    + BENJAMIN ELDER

With so much of the world stuck at home thanks to the COVID-19 pandemic, more and more workplaces are using video conferencing solutions—such as Zoom—to bring work to your living room. Or kitchen. Or bedroom. Or bathroom. OK… hopefully not that last one! Why not spice up your video conferencing with some awesome, homemade virtual backgrounds built with Python and OpenCV?

(`是也乎:`

用一个简单例子来描述, 开源世界机械视觉最常见的应用...

![OpenCV](http://ydlj.zoomquiet.top/ipic/2020-04-15-ScreenShot%202020-04-15%2012.56.19.jpg)

)


- [继承与组成: Python OOP指南](https://pycoders.com/link/3955/web)
    + REAL PYTHON 
    + course

Learn about inheritance and composition in Python. You’ll improve your object-oriented programming (OOP) skills by understanding how to use inheritance and composition and how to leverage them in their design.


(`是也乎:`


![OOP](http://ydlj.zoomquiet.top/ipic/2020-04-15-ScreenShot%202020-04-15%2012.53.55.jpg)

很多 OOP 概念都是在特殊场景中才感觉舒服的...
但是,我们学习使用却反过来, 先尝试理解各种模型,
再去撞场景...


)


- [嫑再将你 Python 模块命名为 utils](https://pycoders.com/link/3919/web)
    + SEBASTIAN BUCZYŃSKI 
    + opinion

“Do not use utils as a name for your Python module neither put it into a class name. Try to be more specific about the role of code – e.g. create a place for validators, services or factories. If the role criterion doesn’t help and you really dealing with utils, try grouping code by its theme.”


(`是也乎:`

utils 已经变成垃圾箱了...
最好给出真正有意义的模块名

)


- [从分块到并行: 借助 Dask 加速 Pandas](https://pycoders.com/link/3918/web)
    + ITAMAR TURNER-TRAURING

In a recent article, Itamar Turner-Trauring discussed how to read large datasets with Pandas using a chunking technique to reduce memory overhead. Chunking has another advantage: it enables parallelism, which can dramatically speed up processing time. Learn why and how to enable parallelism for your Pandas processing code using the Dask library.

- [数据科学: 现实不符合预期](https://pycoders.com/link/3926/web)
    + DAN FRIEDMAN 
    + opinion

“Seven common ways a data science role may not meet your expectations through tens of data scientist interviews and anecdotes from popular media.” Also see the related discussion on Hacker News

- [如何在 pytest 中为 Django 模型提供测试装置](https://pycoders.com/link/3945/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to use fixtures to simplify your testing in pytest. If you use Django, pytest fixtures can help you write tests that are painless to update and maintain even as you make changes to your models.

- [PyPy 7.3.1 发布](https://pycoders.com/link/3961/web)
    + PYPY BLOG








































## 讨论
> Discussions

- [可以从不等长的生成器中检索 zip() 的静默消元吗? ](https://pycoders.com/link/3914/web)
    + STACK OVERFLOW

If you pass two generators to zip(), then the iterator returned by zip() stops whenever the shorter of the two generators runs out of values. If the generator passed to zip() in the first position is larger than the second, then there is an “extra” value consumed from the larger generator. Why does this happen, and is it possible to retrieve the extra value consumed by zip()?

- [如何简化重复的 if / elif ?](https://pycoders.com/link/3959/web)
    + STACK OVERFLOW

Comparing a single value against a number of conditions can result in long if/elif blocks. Is there a short and clean way to handle these comparisons?

- [多个 pytest 维护者离开 pytest](https://pycoders.com/link/3920/web)
    + REDDIT

(`是也乎:`

因为终于有资金注入了?

)









































## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [CuPy 在 UPU 上加速 NumPy ? 嗯哼? 竟然得 Clojure!](https://pycoders.com/link/3952/web)
    + DRAGAN DJURIC

NumPy is fast, but it doesn’t play well with GPUs. For that, you can use CuPy, a drop-in NumPy replacement for GPUs developed by Nvidia. Now, what if I told you to crunch those numbers in Clojure on a GPU instead? Surely a language that compiles to Java couldn’t beat C++ optimized for CUDA, could it? Dragan Djuric, author of Numerical Linear Algebra for Programmers compares CuPy and Clojure on a GPU, with some surprising results.


(`是也乎:`

见到 Clojure 很惊讶嘛?

)


- [在 Python 中测试 S3 的3种方法](https://pycoders.com/link/3931/web)
    + SANJAY SIDDHANTI

Testing an application’s interaction with a third-party service can be difficult and frustrating. But sometimes a lot of business logic is wrapped up in those interactions, so testing them is important for building trust in the application. This article compares and contrasts three options for testing Amazon S3 integration using the pytest framework.


(`是也乎:`

弄S3 三法宝:
moto/boto3/Localstack

其实, 还是官方给的 SDK 放心哪

)


- [用 textX 基于 Python 快速构建领域特殊语言(DSL)](https://pycoders.com/link/3937/web)
    + FEDERICO TOMASSETTI

Domain-specific languages (DSL) bring the power of high-level programming to domain experts (read: non-programmers). In this article, Federico Tomassetti walks you through the process of creating a DSL with the textX Python library. As a bonus, you’ll also learn how to create syntax highlighting extension for VS Code that understands your language.

(`是也乎:`

VSCode 也纳入了自己的生态圈,
非常聪明了.

)


- [用 Python 可视化决策树](https://pycoders.com/link/3934/web)
    + MICHAEL GALARNYK 
    + • Shared by Michael Galarnyk

“Decision trees are a popular supervised learning method for a variety of reasons. Benefits of decision trees include that they can be used for both regression and classification, they don’t require feature scaling, and they are relatively easy to interpret as you can visualize decision trees. This is not only a powerful way to understand your model, but also to communicate how your model works. Consequently, it would help to know how to make a visualization based on your model.”

- [John Conway, 生命游戏的发明者, 死于COVID-19](https://pycoders.com/link/3960/web)
    + ARSTECHNICA.COM

John Horton Conway was one of the most influential mathematicians of the 20th and 21st centuries. His “Game of Life” spawned countless implementation—nearly becoming a rite of passage for programmers in any language. Sadly, the world lost this brilliant mind on April 11 due to complications from COVID-19. Renowned mathematician Terry Tao has also published a memoir in honor of John Conway on his blog.

(`是也乎:`

大家都知道了, 生命游戏创始人, 可人家真的不是电子游戏...
)


- [用 Python 建模股票投资组合](https://pycoders.com/link/3916/web)
    + MATT GRIERSON

After reading an article about comparing a stock portfolio to the S&P 500, Matt Grierson wanted to go deeper and model a portfolio’s performance by analyzing buys and sells from a CSV file and calculating the rate of return relative to an index across any specified timeframe. This turned out to be more involved than Matt first thought it would be! Fortunately, Matt decided to share his experience—and his solution.

- [操纵 Python AST 的历险记](https://pycoders.com/link/3944/web)
    + GEORGE HO

George Ho proposed a change to PyMC4’s model specification API that he thought would help make the user experience more straightforward. Although those changes weren’t ultimately accepted by his fellow PyMC4 core developers, the process led him into some interesting explorations into Python’s abstract syntax tree.

- [RPP Episode #4: 通过错误学习Python](https://pycoders.com/link/3935/web)
    + REAL PYTHON 
    + podcast

An interview with Martin Breuss on getting started with Django, and how to learn Python through errors, and how errors really are your friends. Martin talks about his work with Coding Nomads, and teaching Python around the world. He also provides some tips on debugging and writing good questions.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-04-15-real-python-logo-square.28474fda9228.png?imageView2/2/w/360)


podcast 在国外一直是个稳定的交流渠道,
在中国好象因为电台专营, 长期没了这个习惯.

)

- [在 Pandas 合并数据](https://pycoders.com/link/3951/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn three techniques for combining data in Pandas: merge, join, and concat. Combining Series and DataFrame objects in Pandas is a powerful way to gain new insights into your data.


(`是也乎:`

![Pandas](http://ydlj.zoomquiet.top/ipic/2020-04-15-ScreenShot%202020-04-15%2012.09.41.jpg)

两个函式, 就一大篇文章, 真蟒是真用心哪

)


- [Python 分析工具概述](https://pycoders.com/link/3927/web)
    + MIKE DRISCOLL

- [用 dis 模块深入理解你的 Python 代码](https://pycoders.com/link/3928/web) 
    + FLORIAN DAHLITZ

(`是也乎:`

一个友好的中间码展示工具
)








































## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [deltapy: 表格数据增强](https://pycoders.com/link/3948/web)
    + GITHUB.COM/FIRMAI

- [twint: 高级 Twitter 抓取和 OSINT 工具](https://pycoders.com/link/3946/web)
    + GITHUB.COM/TWINTPROJECT

- [Whole-Foods-Delivery-Slot: 自动化 Whole Foods 以及 Amazon Fresh 交易](https://pycoders.com/link/3943/web)
    + GITHUB.COM/PCOMPUTO

- [textX: 轻松进行特定领域的语言和解析器](https://pycoders.com/link/3923/web)
    + GITHUB.COM/TEXTX

(`是也乎:`

创造语言的语言, 元语言, 而且提供 IDE 可视化分析...

![textX](http://ydlj.zoomquiet.top/ipic/2020-04-15-68747470733a2f2f696d672e796f75747562652e636f6d2f76692f484931346a6b304a4952302f302e6a7067.jpg?imageView2/2/w/360)

)


- [yfinance: 雅虎金融市场数据下载器](https://pycoders.com/link/3940/web)
    + GITHUB.COM/RANAROUSSI

(`是也乎:`

等等, Yahoo 还活着?

)


- [chord: Python 的中的交互式 和弦图](https://pycoders.com/link/3936/web)
    + GITHUB.COM/SHAHINROSTAMI

(`是也乎:`

![chord](http://ydlj.zoomquiet.top/ipic/2020-04-15-1.png?imageView2/2/w/360)

生成这种**和弦图**, 而且能互动.

)


- [pymc4: TensorFlow 概率的高级概率编程接口](https://pycoders.com/link/3922/web)
    + GITHUB.COM/PYMC-DEVS

- [machine_learning_examples: 机器学习示例和教程集合](https://pycoders.com/link/3925/web)
    + GITHUB.COM/LAZYPROGRAMMER

- [nimporter: 在导入时为 Python 编译 Nim Import!](https://pycoders.com/link/3949/web)
    + GITHUB.COM/PEBAZ


(`(￣▽￣):`

叕一个 Nim 的扩展了, 
无论有什么新语言诞生, Python 总是能第一时间拓展过去...

)


- [PePy.tech: 下载 python 软件包的统计信息s](https://pycoders.com/link/3942/web)
    + PEPY.TECH 
    + • Shared by Petru Rares Sincraian

- [Contextualise: 管理您的知识](https://pycoders.com/link/3938/web)
    + GITHUB.COM/BRETTKROMKAMP 
    + • Shared by Brett Kromkamp


(`是也乎:`

![Contextualise](http://ydlj.zoomquiet.top/ipic/2020-04-15-graph-view.png?imageView2/2/w/360)


看起来功能很强大...
但是,还没到可以投入使用的阶段?

)






















## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ IndyPy Mixer Meetup: Data Structures (Virtual)](https://pycoders.com/link/3929/web)
    + April 14, 2020
    + 在线

- [⋅ Virtual PythonCamp Cologne](https://pycoders.com/link/3930/web)
    + April 25 to April 26, 2020
    + 在线

- [⋅ Python Pizza Remote Conference](https://pycoders.com/link/3950/web)
    + April 25, 2020
    + 在线

- [⋅ EuroPython 2020 Online Conference](https://pycoders.com/link/3941/web)
    + July 23 to July 26, 2020
    + 在线













## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp7py 马上(4.21)截止报名(能开发票 ;-)

参考: 

- tiny4voice 的推荐 [为什么初学编程我建议从Python开始](https://mp.weixin.qq.com/s/GiCLU-bdxY3t0jqdVQ8NIQ)
- 余晟以为 的推荐 [关于在本公众号进行付费阅读的通知](https://mp.weixin.qq.com/s/XznOVioOzThdFy1NzqUM-g)




- [PyCon US 2020 来了：人生苦短，不如线上学 Python](https://mp.weixin.qq.com/s/8PDnbR0XOCDcg2xURxnDYg)
    + 4 月 15 日至 23 日
    + 线上









# PS:
- 首发: [Issue 416 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-416.html)
- 修订: [issue-416.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-416.md)


-------------
>> NN 3984

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```



-------------



