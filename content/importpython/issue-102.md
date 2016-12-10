Title: 蠎加载 102
Slug: importpython-102
Date: 2016-12-10 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 102](http://importpython.com/newsletter/no/102/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [如何用 Python 代码来捕获环线地铁上的流氓?](https://blog.data.gov.sg/how-we-caught-the-circle-line-rogue-train-with-data-79405c86ab6a)
    + pandas

Singapore’s MRT Circle Line was hit by a spate of mysterious disruptions in recent months, causing much confusion and distress to thousands of commuters. Like most of my colleagues, I take a train on the Circle Line to my office at one-north every morning. So on November 5, when my team was given the chance to investigate the cause, I volunteered without hesitation.

(`是也乎:`

通过一系列的数据分析,将非法乘车的人群行为可视化,
相关 ipynb 下载:[datagovsg-blog/circle-line-analytics](https://github.com/datagovsg-blog/circle-line-analytics)

问题是, 新加坡哪! 传说中治安最好的国家之一呢...

)

- [线程异步魔法以及具体的折腾](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32?source=rss-138c0eb26be5------2)
    + python3, asyncio

A dive into Python’s asyncio tasks and event loops. The asyncio package allows us to define coroutines. These are code blocks that have the ability of yielding execution to other blocks. They run inside an event loop which iterates through the scheduled tasks and executes them one by one. A task switch occurs when it reaches an await statement or when the current task completes.

(`是也乎:`

Py3 也就只能将这拿来说事儿了
)

- [Python 加载语句中的命名约定.用 BigQuert 对 Github DB Dump 进行探索](https://medium.com/@baditaflorin/naming-conventions-in-python-import-statements-a-bigquery-adventure-using-the-github-db-dump-d900159ab680#.rz4i3ko5a)
    + github, bigquery


Fun article by Florin Badita using BigQuery over entire github hosted Python project's code base.


(`是也乎:`

细思恐极~ [GitHub Data  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/public-data/github)

GitHub 应该是拿到了 Google 的免费接口支持,
所以能实时的将所有开源项目的仓库数据同步到 BigQuery 上,
这带来了一个直接后果: 我们提交的代码已经变成了互联网意识的一部分!

嗯哼,各种代码代码风格的优劣,现在有了直接的数据支持,可以客观的知道当前世界上程序猿们的真实心理动态了....

比如: 这个月使用 tab 的多过空格的, 可能是 win13 发布带来的小高潮...etc.

[Tabs or spaces](https://medium.com/@hoffa/400-000-github-repositories-1-billion-files-14-terabytes-of-code-spaces-or-tabs-7cfe0b5dd7fd#.a3y5j7hi5)(圣战分析)

![Tabs vs spaces](https://img.readitlater.com/i/cdn-images-1.medium.com/max/1600/1*Aaqc9L1Hc62hBg_dpNgBKg/RS/w844.png?&ssl=1)

当然有很多技巧的, 主表 [bigquery-public-data:github_repos.contents] 已经 1.5 TB,
不是一般人承担的了查询费用的...



![data4github](https://camo.githubusercontent.com/d947c404d57303324a8b15bb26fd3da2b06f7e24/687474703a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031322f6769746875622e73746174732e706e673f323d32)
)


- [Tensorflow: 如何用 Python 接口冻结模型并使用](https://blog.metaflow.fr/tensorflow-how-to-freeze-a-model-and-serve-it-with-a-python-api-d4f3596b3adc#.n8b5wb720)
    + tensorflow, machinelearning

We are going to explore two parts of using a ML model in production. How to export a model and have a simple self-sufficient file for it ? How to build a simple python server (using flask) to serve it with TF ?.

(`是也乎:`

又一个用 Flask 落地 TF 服务的案例
)


- [四大 Python 可能的未来之纠缠](http://www.infoworld.com/article/3146967/application-development/4-likely-future-twists-for-python.html)

What does the future hold for Python, aside from new versions of the language ?

(`是也乎:`

嗯哼, Py2 LL&P
)


- [基于 Microsoft Cognitive 服务和 Python 构建私人 ChatBot](https://blogs.msdn.microsoft.com/uk_faculty_connection/2016/11/28/creating-my-first-chatbot-using-microsoft-cognitive-services-and-python/)
    + chatbots

ChatBot is the new buzz word for a while. Microsoft Cognitive Services API allows you to built ones that allow your app to process natural language and learn how to recognize what users want.


(`是也乎:`

就是这种邪恶的免费接口,将程序猿训练为了向企业 AI 投食的机械人!
嗯哼,俺也将给 Cognitive 输入整个儿红楼梦,是否能变成可吟诗的 Bot ?

(￣▽￣) 也支持 Jupyter ... M$ 一点儿也不落后.
)

- [用 Python 可视化 Tweet 向量](http://www.johnwittenauer.net/visualizing-tweet-vectors-using-python/)
    + data-mining, gensim, tweets

I created a semi-practical application that reads from the Twitter stream, parses tweets, and does some machine learning magic to score the tweet’s sentiment and project it into a two-dimensional grid, where tweets with similar content will appear closer to each other. It does all of this more or less in real time using asynchronous messaging.

(`是也乎:`

实时获得 Twitter 的情绪变化

![example](http://www.johnwittenauer.net/content/images/2016/12/example.png)
)


- [在 Xcode 中跑 Python : 步骤 — Erica Sadun](http://ericasadun.com/2016/12/04/running-python-in-xcode-step-by-step/)
    + xcode, apple

As I’m preparing for a project that will involve Python programming, I need to get up to speed with at least a basic level of Python mastery. However, I’m not a big fan of using the interactive Python REPL. I decided to use Xcode instead, and I’m finding it a much better solution for my needs:

(`是也乎:`

Hummm 何苦泥...
)

- [用 Pickle 进行对象序列化](https://medium.com/the-python-corner/object-serialization-in-python-1d49c6ad071#.5yzvlas8x)
    + pickle

Introductory article on usage of pickle module.

(`是也乎:`

之前曰过 [eevee/camel: Python serialization for adults](https://github.com/eevee/camel) 更加嗯哼.
)


- [和 AWS Lambda 一起用 Numba](https://medium.com/hudl-data-science/using-numba-with-aws-lambda-c114a1307813#.38ndbqdbj)
    + aws, lambda, numba

In a recent project, we decided to use Lambda to execute some fairly math-y Python code in response to user click events on a webpage. Originally this back-end Python code had utilized the Numba library to speed up its execution. However, we quickly found that it was not trivial to make Lambda and Numba play nicely together.

(`是也乎:`

事实一再证明 AWS 工程师不是吃素的...

Numba 这种基于 LLVM 加速的并发分析工具,都可以简单的移植到 Lambda 中跑起来...
)

- [unittest 中最赞的你应该知道却不一定知道的特性](https://hackernoon.com/the-best-new-feature-in-unittest-you-didnt-know-you-need-e0d26c213dce#.vwhl89x6e)
    + subTest

From time to time I like to read documentation of modules I think I know well. The python documentation is not a pleasant read but sometimes you strike a gem.

(`是也乎:`

所谓灯下黑呗.

终于有子测试了...

)


- [Pytho 中的高级句式匹配](https://medium.com/@sumn2u/advance-sentence-matching-in-python-c78d86f65aa7#.ulzxiokes)
    + string_maching

FuzzyWuzzy is a fantastic Python package which uses a distance matching algorithm to calculate proximity measures between string entries.

(`是也乎:`

使用距离算法来对整句进行相似度分析,当然不支持 中文先...
)

- [通过异常类定义另你的自制类更加可读](https://dbader.org/blog/python-custom-exceptions#py)
    + video, screencast, exception_handling

In this short screencast I’ll walk you through a simple code example that demonstrates how you can use custom exception classes in your Python code to make it easier to understand, easier to debug, and more maintainable.

(`是也乎:`

其实吧,还是代码写简单点儿最好了.
)

## 好物
~ 包/模块/库/片段...

- [universe](https://github.com/openai/universe)
    - 2867 Stars, 213 Fork

Universe is a software platform for measuring and training an AI's general intelligence across the world's supply of games, websites and other applications. This is the universe open-source library, which provides a simple Gym interface to each Universe environment. Universe allows anyone to train and evaluate AI agents on an extremely wide range of real-time, complex environments.

(`是也乎:`

统一通过 Gym 接口,训练各种 AI 在世界上各种游戏中自我训练.
喂! `No Zuo No Die!`
)


- [tensorflow_chatbot](https://github.com/llSourcell/tensorflow_chatbot)
    - 120 Stars, 36 Fork

This is the full code for 'How to Make an Amazing Tensorflow Chatbot Easily' by @Sirajology on Youtube. In this demo code, we implement Tensorflows Sequence to Sequence model to train a chatbot on the Cornell Movie Dialogue dataset. After training for a few hours, the bot is able to hold a fun conversation.

(`是也乎:`

如何创造惊人的 TF 图表一文对应的所有代码...

)

- [showmemore](https://github.com/polm/showmemore)
    - 9 Stars, 1 Fork

ShowMeMore is an automated researcher. Given a list of tags to start with, it goes hunting for images, and over time grows its model in response to reactions, slowly reaching out to find things you weren't aware you already liked.

(`是也乎:`

死也不能给女友看到的东西!
)


- [speedtest-tweet-bot](https://github.com/kmarima/speedtest-tweet-bot)
    - 8 Stars, 1 Fork

monitors internet speed and tweets when its slow

(`是也乎:`

一但 Twitter 变慢,立即监察网速的工具
)

- [alfredworkflow-capkeystone](https://github.com/alexhude/alfredworkflow-capkeystone)
    - 7 Stars, 1 Fork

Alfred Workflow to convert hex string to assembly and vice versa 

(`是也乎:`

在 `Alfred` 工作流中快速将 16进制和汇编代码进行相互转换.

![capkeystone](https://github.com/alexhude/alfredworkflow-capkeystone/raw/master/Resources/screenshots/workflow.png?raw=true)

`Alfred` 简直就是本地的 PIPE 服务
)

# 是也乎

- [The End Of Coder Influence \| Zed A\. Shaw](https://zedshaw.com/2016/11/24/the-end-of-coder-influence/)

(`嗯哼:`

这真是一个悲哀的故事...
)

- 161210 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161210 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


