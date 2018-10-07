Title: 蠎加载 186
Slug: importpython-186
Date: 2018-10-06 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 186](http://importpython.com/newsletter/no/186/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**
- 最近官方更新的不规律, 俺也不好按时自造...

## 该读
~ 文章, Blog, 教程...

- [Flask Monthly Newsletter](https://newsletterspot.com/flask/)
    + flask, newsletter

Once a month flask newsletter. Maintained and curated by a friend.

(`是也乎:`

相比 Django 的迟了太久...

)


- [嫑在 Python 中写 lambda 表达式了 - Trey Hunner](http://treyhunner.com/2018/09/stop-writing-lambda-expressions/)
    + lambda, corepython

I’m going to explain how I see lambda expressions and why I tend to recommend my students avoid using them.


(`是也乎:`

发现各种混淆工具, 对 Lambda 都没什么办法...
)

- [Microservices 持续交付的修复策略](https://www.gocd.org/2018/09/11/cd-microservices-remediation-strategy/?utm_campaign=cd_microservices&utm_medium=newsletter_ad&utm_source=importpython&utm_content=remediation_strategy)
    + devops, ad

In systems based on microservices architecture, you have multiple services getting updated frequently. How do you respond when a deployment of a service introduces instability or bugs? Sheroy Marker offers some remediation strategies in this blog.

- [Facebook 为 PyTorch 1.0 新合作伙伴加速人工智能开发 - Facebook for Developers](https://developers.facebook.com/blog/post/2018/10/02/Facebook-accelerates-AI-development-with-new-partners-for-PyTorch-1.0/)
    + pytourch

The latest additions to the framework include a new hybrid front end that enables tracing and scripting models from eager mode into graph mode for bridging the gap between exploration and production deployment, a revamped torch.distributed library that allows for faster training across Python and C++ environments, and an eager mode C++ interface (released in beta) for performance-critical research.




- [Multi Armed Bandit 实施](http://peterroelants.github.io/posts/multi-armed_bandit_implementation/)
    + multi-armed bandit

In the multi-armed bandit (MAB) problem we try to maximise our gain over time by "gambling on slot-machines (or bandits)" that have different but unknown expected outcomes. The concept is typically used as an alternative to A/B-testing used in marketing research or website optimization. For example, testing which marketing email leads to the most newsletter signups, or which webshop design leads to the most sales. The benefit of viewing website optimization as a multi-armed bandit problem instead of an A/B-testing problem is that no pre-defined sample sizes are needed and the algorithm will start optimizing the outcome (e.g. click rate) from the beginning. While the A/B-test needs to run all predefined samples to make a conclusion.


(`是也乎:`

MAB --- 叕一个专有现象名词

)

- [A Logo-to-Python Transpiler](https://pablasso.com/logo-to-python-transpiler/)
    + logo, transpiler

Some days ago I got melancholic while using turtledemo and decided to create a project that has no practical applications whatsoever – a transpiler called chelodina1. Curator's note - I studied logo back in school and then DBase III Plus. But it's logo that got me excited about programming. Had lot of fun playing with this today.

(`是也乎:`

叕一个 Why not 的项目,
有趣, 但不一定有用

)


- [维基百科数据科学: 与世界上最大的百科全书合作](https://towardsdatascience.com/wikipedia-data-science-working-with-the-worlds-largest-encyclopedia-c08efbac5f5c)
    + wikipedia

How to programmatically download and parse the Wikipedia?

(`是也乎:`

世界最大死链网页样本集

)


- [用 websockets 轻松构建 Python 程序的 GUI](https://gist.github.com/jsomers/d32dd3507e5406c56e47b4cd6f28c60e)
    + GUI, websocket

I recently built a small agent-based model using Python and wanted to visualize the model in action. But as much as Python is an ideal tool for scientific computation (numpy, scipy, matplotlib), it's not as good for dynamic visualization (pygame?). You know what's a very mature and flexible tool for drawing graphics? The DOM! For simple graphics you can use HTML and CSS; for more complicated stuff you can use Canvas, SVG, or WebGL.

(`是也乎:`

![websockets](https://user-images.githubusercontent.com/21294/45828766-5c6d9780-bcc7-11e8-9e05-8f3e17e5ec08.gif)

其实, 只是解决了跨技术桟的消息传送, 
界面的控制/响应, 在前端领域那是比 Qt 还要大的坑...

特别是 Chrome 带头开始乱搞的现在...

)


- [面向程序员的 50+ 数据结构和算法问题](https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0)
    + offtopic, interview prep

There are a lot of computer science graduates and programmers applying for programming, coding, and software development roles at startups like Uber and Netflix; big organizations like Amazon, Microsoft, and Google; and service-based companies like Infosys or Luxsoft, but many of them have no idea of what kind of programming interview questions to expect when you’re applying for a job with these companies.

(`是也乎:`

数据/算法工程师 的面试经...

)



- [用 Python 清理和准备数据](https://towardsdatascience.com/cleaning-and-preparing-data-in-python-494a9d51a878)
    + pandas, datascience

Data Science sounds like something cool and awesome. It’s pictured as something cool and awesome. It is a sexiest job of 21st century as we all know (I won’t even add the link to that article :D). All the cool terms are related to this field?—?Machine Learning, Deep Learning, AI, Neural Networks, algorithms, models

(`是也乎:`

叕一则 Pandas 宣传教程, 但是, 至今从未见比官方 10分钟 ,更加赞的文案了...
但是, 都没好意思说, 现实项目折腾中, 80% 的时间是在 Pandas 之外, 用各种其它工具来清理原始数据...


)


- [remi](https://github.com/dddomodossola/remi)
    + GUI

Remi is a GUI library for Python applications which transpiles an application's interface into HTML to be rendered in a web browser. This removes platform-specific dependencies and lets you easily develop cross-platform applications in Python!

(`是也乎:`

![remi](https://raw.githubusercontent.com/dddomodossola/remi/development/remi/res/logo.png)


叕一则想通过 web 来实现 Pythonic GUI 构建梦想的尝试
和当年洪教授的 Ring 思路一致, 也没解决相同的问题.

)


- [命令行中的 Python : Click 教程](https://kite.com/blog/python-command-line-click-tutorial)
    + command line tool

(`是也乎:`

pocoo 出品必为佳品

)


## 好物
~ 包/模块/库/片段...

- [dbxfs](https://github.com/rianhunter/dbxfs)
    - 255 Stars, 7 Fork

User-space file system for Dropbox

(`是也乎:`

不用说 py3 为核心的...
)


- [mpc.pytorch](https://github.com/locuslab/mpc.pytorch)
    - 127 Stars, 4 Fork

A fast and differentiable model predictive control (MPC) solver for PyTorch.

(`是也乎:`

有 Fb 当爹, PyTorch 生态也发展起来了

)


- [Hierarchical-attention-networks-pytorch](https://github.com/1991viet/Hierarchical-attention-networks-pytorch)
    - 46 Stars, 23 Fork

Hierarchical Attention Networks for Document Classification


(`是也乎:`

![Hierarchical](https://github.com/1991viet/Hierarchical-attention-networks-pytorch/raw/master/demo/video.gif)

Wow ...集成化了...

)


- [Hand-Tracking](https://github.com/EvilPort2/Hand-Tracking)
    - 31 Stars, 21 Fork

Tracking hands using deep learning

(`是也乎:`

简单说现在有 ML 字样的都能有经费?

)


- [scc](https://github.com/Ziyadsk/scc)
    - 29 Stars, 1 Fork

An Offline cheat sheet and a quick reference command line tool for HTML, CSS and JS .

(`是也乎:`

![randomjs](https://github.com/Ziyadsk/scc/raw/master/screenshots/randomjs.png)

CLI 中的作弊条...只能说 终端万岁了...


)

- [bunny](https://github.com/bheinzerling/bunny)
    - 23 Stars, 1 Fork

A progress bar like tqdm, but with more bunny.

(`是也乎:`

![bunny](https://github.com/bheinzerling/bunny/raw/master/bunny.gif)

细思恐极...简单的说, 在 CLI 进度条上加载广告的日子不远了...

)



- [ibis](https://github.com/Cigna/ibis)
    - 13 Stars, 1 Fork

IBIS is a workflow creation-engine that abstracts the Hadoop internals of ingesting RDBMS data.

(`是也乎:`

![ibis_wo_logo](https://github.com/Cigna/ibis/raw/master/docs/ibis_wo_logo.png)

叕一个复杂功能, 简洁界面的工作流框架


)


- [thriftpy2](https://github.com/Thriftpy/thriftpy2)
    - 9 Stars, 1 Fork

Pure python implementation of Apache Thrift.

- [Trading-Strategies](https://github.com/lsijia0606/Trading-Strategies)
    - 6 Stars, 0 Fork

python library for trading strategies & analyzing

(`是也乎:`

领域数据分析套件, 这原本都是产品的, 没市场就开源了?

)



- [tide](https://github.com/Alekaei/tide)
    - 5 Stars, 1 Fork

TIDE is a Terminal Integrated Development Environment

(`是也乎:`

![TIDE](https://camo.githubusercontent.com/c4a871fef60fa4915bb1f4b9efbda6c9918badc7/68747470733a2f2f692e696d6775722e636f6d2f5a35704c7177362e706e67)

叕一个预定制的 vim ?


)


- [awstack](https://github.com/mazaziz/awstack)
    - 5 Stars, 1 Fork

aws cloudformation for humans

(`是也乎:`

细思恐极的是, 工具总是创建时面向机械的,
然后为了推广又面向 human, 
可是云计算最终还是要导向面向机械哪...

)


- [scratchML](https://github.com/gfgullo/scratchML)
    - 3 Stars, 0 Fork

Machine Learning from Scratch with Python and Numpy




### (￣▽￣)

- [PyCon 2018 China](http://cn.pycon.org/2018/)
    + 来了, 真的来了


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...

- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)

## 是也乎

- 181006 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 181006 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


