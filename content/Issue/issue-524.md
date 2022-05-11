Title: PyCoder 524
Slug: issue-524
Date: 2022-05-11 11:42
Tags: Weekly,Python,pycoders,ZH


> PyScript 直接在浏览器中运行 Py


原文: [PyCoder's Weekly - Issue #524](https://pycoders.com/issues/524)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220511 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220511 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [PyCon US 2022 亮点](https://pycoders.com/link/8642/web)
    + ERIC MATTHES 
    + • Shared by Eric Matthes

“It was wonderful to be back at PyCon US in person again. PyCon is way too big for any one person’s summary to tell the whole story, but I’m happy to share some of my personal highlights from this year’s event.”


(`是也乎:`


![PyLadies](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.54.31.jpg)

大图...[No1gdoQ.jpg (1500×2000)](https://i.imgur.com/No1gdoQ.jpg)


怪不得老爹一直点赞 这个活动...

)


- [顶级 Python 游戏引擎s](https://pycoders.com/link/8669/web)
    + REAL PYTHON

In this tutorial, you’ll explore several Python game engines available to you. For each, you’ll code simple examples and a more advanced game to learn the game engine’s strengths and weaknesses.


(`是也乎:`


![Engines](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.44.50.jpg)
)

Ultimate Guide to Python Pickle: How To’s, Exploits & Safety
Python’s pickle library is useful in maintaining persistence within complex data structures and objects. Learn how to safely use a pickle in application development using this comprehensive guide →
SNYK.IOSPONSOR

- [PyScript: 在浏览器中释放 Python 的力量](https://pycoders.com/link/8675/web)
    + ERYK LEWINSON

PyScript was announced at PyCon US 2022, it is a web-based application allowing you to use both Python and HTML to create applications. Discover what it can do and how it was built.


(`是也乎:`



![PyScript](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.42.45.jpg)

刷屏的大新闻,
CoffeeScript 真正的目的, 现在实现了...


)


- [Python News: 2022 年 4 月有什么新闻](https://pycoders.com/link/8688/web)
    + REAL PYTHON

In April 2022, the PyCon US conference happened in Salt Lake City. During the conference, Python developers met for the annual Language Summit, and Anaconda announced PyScript, a way to write Python directly inside HTML. In this article, you’ll learn more about what happened in the last month in the world of Python.



(`是也乎:`


![News](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.41.43.jpg)
)


-----------------------------------------
## 探讨/吐糟
> Discussions



- [现代 Python 性能注意事项](https://pycoders.com/link/8661/web)
    + HACKER NEWS

There’s nothing like talking about Python and speed to stir up a conversation. Join this discussion about Jake Edge’s [Modern Python performance considerations](https://pycoders.com/link/8671/web).

(`是也乎:`


[Modern Python performance considerations \[LWN.net\]](https://lwn.net/SubscriberLink/893686/8978976335696804/)

好文章都在 LWN.net 中...
毕竟这是上古讨论中心...

)



- [哪个 Python 包有最好的实现?](https://pycoders.com/link/8653/web)
    + TWITTER.COM/DRISCOLLIS





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 pytest 测试你的代码](https://pycoders.com/link/8686/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to take your testing to the next level with pytest. You’ll cover intermediate and advanced pytest features such as fixtures, marks, parameters, and plugins. With pytest, you can make your test suites fast, effective, and less painful to maintain.

(`是也乎:`

![pytest](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.40.23.jpg)

其实最关键的是编写代码时, 就设计好测试方案,
以免事后绕...

)


- [Cinder JIT 的函数内联如何优化](https://pycoders.com/link/8645/web)
    + MAX BERNSTEIN

Cinder is an open-sourced fork of CPython that includes optimizations like immortal objects, inline caching, Static Python, Strict Modules, and a Just-In-Time compiler. This article does a deep dive on how their JIT handles function in-lining for performance gains.

- [通过 Anaconda Nucleus 加入免费在线社区](https://pycoders.com/link/8631/web)
    + ANACONDA
    + SPONSOR

Anaconda Nucleus is our education and community engagement platform. The platform features a wealth of data science content ranging from articles to webinars to videos and more. 
[Join Our Free Online Community With Anaconda Nucleus](https://pycoders.com/link/8631/web)→

- [Python 可视化音频的初学者指南](https://pycoders.com/link/8652/web)
    + BRADEN RIGGS

Visualizing data with a spectrogram helps reveal hidden insights in the audio data that may have been less apparent in the traditional waveform representations. With some numpy, matplotlib and scipy you can visualize your audio in a few short lines.

- [PEP 690: 惰性导入](https://pycoders.com/link/8676/web)
    + PEPS.PYTHON.ORG

This PEP proposes the ability to defer the execution of imported modules until the moment when an imported object is used. Lazy imports can greatly reduce the overall number of modules initially loaded, improving startup time and memory usage.



(`是也乎:`


PEP 绝对是 Python 发展核动力中心

)


- [用 Python 探索 Google Analytics 实时数据](https://pycoders.com/link/8634/web)
    + MARTIN HEINZ

Google Analytics can provide a lot of insight into your website’s traffic and although they have dashboard tools, you may want to dive deeper. Using the Google Analytics API you can retrieve your analytics data and be in full control.

- [Python的结构模式匹配概述](https://pycoders.com/link/8639/web)
    + JAKE EDGE

Python’s match statement, which provides a C-like switch statement (though it is far more than that) was introduced in Python 3.10. Learn the history of the feature, how it is used, and how it works.

(`是也乎:`


```
    for number in range(100):
        match number % 5, number % 3:
            case _, 0: print("Spam!")
            case 0, _: print("Eggs?")
            case 0, 0: print("Spam and eggs.")
            case _, _: print(number)
```

终于可以在 Python 中写 Lisp/Elixir/Clojure/... 了

)



- [驯服大型 WebAssembly 二进制文件的技巧](https://pycoders.com/link/8665/web)
    + BRAM WASTI

WASM is great, who doesn’t want Python in the browser, but it often requires an expensive cold load of a page. Read more about how to minimize your WASM downloads for speedier Python in the web.

- [布尔短路](https://pycoders.com/link/8657/web)
    + RODRIGO GIRÃO SERRÃO

Learn how and and or are processed in your code, how Boolean short-circuiting works, how “truthy” values effect this, and how all this is handled in the all() and any() functions.



- [将 Python 库转换为 Rust](https://pycoders.com/link/8684/web)
    + ALAN TRICK

Alan describes his experience porting his Python library August to Rust. He outlines the resulting performance difference and things he learned along the way.


(`是也乎:`

不会也比自动从 Py 翻译为 C 代码复杂?
所以, 我们可以安心继续写 Py 了, 
性能着急时, 
一键生成 C/Go/Rust 代码, 编译运行一下, 看哪个性能足够就用哪个;
嗯哼? 等等, 可以先用 PyPy 跑一下,
一般性能就足够了...

)


- [Django Filter: .filter(A).filter(B) vs .filter(A, B)](https://pycoders.com/link/8643/web)
    + IVAYLO DONCHEV

Learn the different ways of chaining calls in the Django ORM, how sometimes it results in duplicate objects, and what to do about it.


(`是也乎:`

Django 本质上已经开始将自己作为一门 Python 的方言 在积累了...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [madbg: 用于 Python 的全功能远程调试器](https://pycoders.com/link/8648/web)
    + GITHUB.COM/KMAORK




- [im2cmap: 将图像转换为 matplotlib  Colormaps](https://pycoders.com/link/8683/web)
    + GITHUB.COM/ARVKEVI • Shared by Kevin Arvai


(`是也乎:`

Wow 风格化必要工具

![im2cmap](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.05.35.jpg)

)

- [pepdocs: 在终端中畅读 PEP](https://pycoders.com/link/8662/web)
    + GITHUB.COM/GAHJELLE

(`是也乎:`

是的, 积累30多年, PEPs 也变成类似
[RFC 1 - Host Software](https://datatracker.ietf.org/doc/html/rfc1)
领域思考大集锦,
其实, 作为 Pythonic , 一生能通过 PEP 给 Python 注入一个新特性,
可算得一果位也;

当然

)



- [gpt-2-simple: 在新文本上重新训练 GPT-2 文本生成模型](https://pycoders.com/link/8678/web)
    + GITHUB.COM/MINIMAXIR


(`是也乎:`

神奇人物创造新神经模式,
其它聪明人快速使用, 给出案例;
普通人就只能点赞了

)

- [HackSoft 项目中使用的 Django 样式指南](https://pycoders.com/link/8635/web)
    + GITHUB.COM/HACKSOFTWARE

(`是也乎:`

![styleguide](https://ipic.zoomquiet.top/2022-05-11-zshot%202022-05-11%2010.03.40.jpg)

程序猿的 VI 设计就是这么朴素

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Dominican Republic Python User Group](https://pycoders.com/link/8668/web)
    + May 10 to May 11, 2022

- [Santa Cruz Python Meetup](https://pycoders.com/link/8654/web)
    + May 11, 2022

- [Heidelberg Python Meetup](https://pycoders.com/link/8670/web)
    + May 11, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8687/web)
    + May 11, 2022

- [PyMNTos](https://pycoders.com/link/8649/web)
    + May 12, 2022

- [Python Miami](https://pycoders.com/link/8672/web)
    + May 14 to May 15, 2022

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

- 首发: [Issue 524 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-524.html)
- 修订: [issue-524.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-524.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF524D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF524D4Q90XdDA7g):



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





