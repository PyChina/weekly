Title: PyCoder 488
Slug: issue-488
Date: 2021-09-01 11:42
Tags: Weekly,Python,pycoders,ZH


> IEEE#1 开发语言 -> Python


原文: [PyCoder's Weekly - Issue #488](https://pycoders.com/issues/488)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 210901 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210901 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [Python在IEEE“顶级编程语言”中排名第一](https://pycoders.com/link/6935/web)
    + IEEE.ORG

“Python dominates as the de facto platform for new technologies” and “Learn Python. That’s the biggest takeaway we can give you from its continued dominance of IEEE Spectrum’s annual interactive rankings of the top programming languages. You don’t have to become a dyed-in-the-wool Pythonista, but learning the language well enough to use one of the vast number of libraries written for it is probably worth your time.”

- [skybison: Instagram 的实验性能面向 Feenfield Python 实现](https://pycoders.com/link/6920/web)
    + GITHUB.COM/FACEBOOKEXPERIMENTAL

“Skybison is experimental performance-oriented greenfield implementation of Python 3.8. It contains a number of performance optimizations, including: small objects; a moving GC; hidden classes; bytecode inline caching; type-specialized bytecode; an experimental template JIT.”



- [如何在定义 Python 函数时使用可选参数](https://pycoders.com/link/6916/web)
    + REAL PYTHON

In this tutorial, you’ll learn about optional arguments in Python and how to define functions with default values. You’ll also learn how to create functions that accept any number of arguments using args and kwargs.

(`是也乎:`

![Arguments](https://ipic.zoomquiet.top/2021-09-01-ScreenShot%202021-09-01%2010.42.51.jpg)

)


- [Python Project-Local 虚拟环境管理](https://pycoders.com/link/6910/web)
    + HYNEK SCHLAWACK

On UNIX-like operating systems you can have the Python equivalent of node_modules today, for every Python version, without changing your workflows.

- [谦虚的软件BUNDLE: Python Superpowers 2021](https://pycoders.com/link/6943/web)
    + HUMBLEBUNDLE.COM

Pick up the awesome programming potential of Python with software like Mastering PyCharm (2021 Edition) & Object-Oriented Programming (OOP) in Python. Pay what you want & support charity!

- [加入Pycon US 2022团队!](https://pycoders.com/link/6917/web)
    + PYCON US

The PyCon US organizers are looking for motivated volunteers who want to contribute their time and knowledge to make this year’s conference a great success.

- [Python 3.9.7 和 3.8.12 现已推出](https://pycoders.com/link/6921/web)
    + CPYTHON DEV BLOG

More info in the full changelog.




-----------------------------------------
## 探讨/吐糟
> Discussions



- [math.sqrt vs numpy.sqrt vs x ** 0.5 性能讨论](https://pycoders.com/link/6923/web)
    + TWITTER.COM/KARPATHY

Andrej Karpathy (Director of AI at Tesla) shares an interesting performance observation on this Twitter thread that turns into a tale about accurate benchmarking. Calculating math.sqrt(1337.0) appears to be 10x faster than numpy.sqrt(1337.0). Python’s built-in square root (x ** 0.5) appears to be even faster. However, most of the performance differences seem to come from the benchmark setup, as Ishan Bhatt explains in this writeup.


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Apple Silicon Transition 的 Python 数据科学家指南](https://pycoders.com/link/6909/web)
    + STANLEY SEIBERT

A break down of what Apple Silicon means for Python users today, especially those doing scientific computing and data science: what works, what doesn’t, and where this might be going.

- [150 行 Python 完成一个 SQL 查询生成器](https://pycoders.com/link/6912/web)
    + ANDGRAVITY.COM

“This is the fourth article in a series about writing my own SQL query builder. Today, we’ll rewrite it from scratch, explore API design, learn when to be lazy, and look at worse and better ways of doing things – all in 150 lines of Python!”



- [用 scikit-searn 和 train_test_split() 拆分数据集](https://pycoders.com/link/6925/web)
    + REAL PYTHON 
    + video

Learn why it’s important to split your dataset in supervised machine learning and how to do that with train_test_split() from the widely used scikit-learn package.


(`是也乎:`

![Splitting](https://ipic.zoomquiet.top/2021-09-01-ScreenShot%202021-09-01%2010.16.17.jpg)

)

- [用 CircuitPython 和 Python 为微控制器的约束构建](https://pycoders.com/link/6914/web)
    + REAL PYTHON 
    + podcast

Can you make a version of Python that fits within the memory constraints of a microcontroller and have it still feel like Python? That is the intention behind CircuitPython. This week on the show, Scott Shawcroft, who is the project lead for CircuitPython.

(`是也乎:`

![podcast](https://ipic.zoomquiet.top/2021-09-01-ScreenShot%202021-09-01%2010.15.43.jpg)

)


- [在 Python 中解析: 可以使用的工具和库](https://pycoders.com/link/6927/web)
    + GABRIELE TOMASSETTI

“We present and compare all possible alternatives you can use to parse languages in Python. From libraries to parser generators, we present all options.”


(`是也乎:`

用  Python 编译一切语言,

)

- [Django 中的低级缓存 API](https://pycoders.com/link/6928/web)
    + J-O ERIKSSON

Caching in Django can be implemented on different levels (or parts of the site). This article looks at how to use the low-level cache API in Django.

(`是也乎:`


从根儿上缓存 Django 的一切?

)


- [幕后的Python: Async/Await 如何在 Python 工作?](https://pycoders.com/link/6930/web)
    + VICTOR SKVORTSOV

“The async/await pattern can be explained in a simple manner if you start from the ground up. And that’s what we’re going to do today.”

- [用 libsqlite3 直接从 python 与 ctypes](https://pycoders.com/link/6931/web)
    + GITHUB.COM/MICHALC

How to use ctypes to run SQLite queries without using the built-in sqlite3 Python package, and without compiling anything.


(`是也乎:`

等等,为什么不用编译?

```
for row in query('my.db', 'SELECT * FROM my_table WHERE a = ?;', ('b',)):
    print(row)
```

成果就是可以直接用 SQL 了...

)


- [Python 处理环境变量](https://pycoders.com/link/6945/web)
    + BOB BELDERBOS

- [在 Python 中模拟直接数字频率合成器](https://pycoders.com/link/6947/web)
    + NASH REILLEY

(`是也乎:`

叕一个音频模拟项目,
用 Python 在内存中复活前苏联独有电子变音器吧

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [kmk_firmware: 由 Python 支持的 Claction 键盘](https://pycoders.com/link/6941/web)
    + GITHUB.COM/KMKFW

(`是也乎:`

嗯哼? 专用键盘驱动? Python 这么任性的?

)


- [ordered: Entropy-Controlled Contexts in Python](https://pycoders.com/link/6919/web)
    + GITHUB.COM/HYPERC-AI

- [gopygo: 纯粹 Python Go 解析器, AST 以及 Unparser Library](https://pycoders.com/link/6915/web)
    + GITHUB.COM/UP9INC

(`是也乎:`

也就是说, 可以直接用 Py 来自动生成 Go 代码了,
等等, Py 本身内置 AST 为什么没有 Golang 来解析 Py 代码自动生成?

)


- [cattrs: 为 attrs 提供的复杂定制类转换器](https://pycoders.com/link/6949/web)   
    + GITHUB.COM/TINCHE

- [msl-apollo-entry-guidance: 用 NASA 的 MSL SpaceCraft 使用的 Apollo 进入引导算法的 Python实现](https://pycoders.com/link/6937/web)
    + GITHUB.COM/THOMASANTONY

(`是也乎:`

![apollo](https://ipic.zoomquiet.top/2021-09-01-ScreenShot%202021-09-01%2010.06.16.jpg)

叕一个薅NASA 经验的项目,
不过, 这都是60年前的数据了,
要不是 天宫 发射成功,
照样不会公开...

)


- [pylectronics: 在 Python 中重现数字电子产品](https://pycoders.com/link/6946/web)
    + GITHUB.COM/FGARCI03

- [sqlmodel: Python 中的 SQL 数据库, 专为简单，兼容性和鲁棒性而设计](https://pycoders.com/link/6948/web)
    + GITHUB.COM/TIANGOLO

(`是也乎:`

FastAPI 团队作品,
基于 SQLAlchemy 给出更加 Pythonic 的 SQL 使用形式.

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

NIL
 
-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 488 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-488.html)
- 修订: [issue-488.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-488.md)


## PPS:
> 不觉中蟒周刊快译已经到了第9个年头

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

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF488D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF488D4Q90XdDA7g):



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





