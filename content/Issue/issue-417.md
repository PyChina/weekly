Title: Issue 417
Slug: issue-417
Date: 2020-04-22 11:42
Tags: Weekly,Python,pycoders,ZH

> 可以在 Zoom/Skype 中使用的替身



原文: [PyCoder's Weekly - Issue #417](https://pycoders.com/issues/417)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200422 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200422 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------






- [pip 20.1b1 发布, 包含新依赖性解析器](https://pycoders.com/link/3972/web)
    + GITHUB.COM/PYPA


The beta release of pip version 20.1 has dropped and included the next-generation dependency resolver! The resolver is currently turned off by default because it’s unstable and not ready for everyday use. The pip mainainters do encourage users to try it out, however, and feedback on the new resolver can be submitted by filling out a survey.

(`是也乎:`

不过默认关闭着...
)


- [Python 软件基金会新闻: 谢谢捐赠/赞助者](https://pycoders.com/link/3979/web)
    + PSF BLOG

“Thanks to [the] generosity of individual and corporate donors and decreasing PyCon 2020 expenses, we estimate that the PSF will now only need $141,713 from its financial reserve to get through 2020.”


(`是也乎:`

嗯哼? 老爹在任时, 从没见这种嗯哼?

)


- [Python 内建 Pathlib 其实很棒](https://pycoders.com/link/4003/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

Python 3’s pathlib module has taken some time to gain traction since it was introduced in Python 3.4. After all, the os.path module had been the de facto tool for working with paths in Python. Why change code that works? Learn why pathlib is a better choice for working with file paths in Python in this thorough tutorial.




- [Pytest 实效 Python 测试](https://pycoders.com/link/3971/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to take your testing to the next level with pytest. You’ll cover intermediate and advanced pytest features such as fixtures, marks, parameters, and plugins. With pytest, you can make your test suites fast, effective, and less painful to maintain.


(`是也乎:`

![Pytest](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2012.04.06.jpg)

不过, 传统场景还是 unittest 为先吧?

)


- [Python 2.7.18, 一个时代的终结](https://pycoders.com/link/3998/web)
    + BENJAMIN PETERSON


“Python 2.7.18 is a special release. I refer, of course, to the fact that ‘2.7.18’ is the closest any Python version number will ever approximate e, Euler’s number. Simply exquisite!”

(`是也乎:`

放心, 俺一定会忠诚再用 42 年的...

)



- [Python 编码面试: 提示和最佳做法](https://pycoders.com/link/3996/web)
    + REAL PYTHON 
    + course


Learn how to take your Python coding interview skills to the next level and use Python’s built-in functions and modules to solve problems faster and more easily.

(`是也乎:`

![Interviews](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2012.03.30.jpg)

关键还是用Python的内置函数和模块哪...

)

























## 讨论
> Discussions




- [故事: 为了10岁儿子和他的数学作业,所以上Python](https://pycoders.com/link/3975/web)
    + REDDIT

When his son gets assigned a menial and repetitive task for his math homework, his Dad does the only reasonable thing and introduces him to Python.

(`是也乎:`

真的是家传手艺了

)

- [新参者: Guilty 是值得拿来构建新项目的](https://pycoders.com/link/3986/web)
    + REDDIT

“So here’s the thing. I’m building some cool web apps and have a pretty good understanding of what I’m doing. However, I always feel kinda guilty because I didn’t build 100% of it from scratch. I used various libraries to achieve certain functionality. It’s like I cheated my way to completion by using these libraries. Is this normal or am I overthinking?”

- [x += 1 vs x = x + 1](https://pycoders.com/link/4002/web)
    + REDDIT

Are there certain situations where one is more useful than the other?

(`是也乎:`

其实并无差别, 但是, 程序猿为了少打字, 真的是, 什么事儿都敢干的...

)


- [实际上在 Python 中执行任何处理的速度都非常慢](https://pycoders.com/link/3976/web)
    + JOHN CARMACK ON TWITTER


(`是也乎:`

嗯哼, 隔壁也分析了, 其实运行速度只比 C++ 原创的慢一点儿...

)










































## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [面向初学者的 Python 装饰器](https://pycoders.com/link/4005/web)
    + SAM IRELAND

If you’ve used a web framework in Python, you’ve probably used a decorator before. But do you know how they work? Do you know how to make your own? Sam Ireland introduces decorators in this beginner-friendly article by first exploring a typical problem in which decorators arise, then gently walking you through a solution.



- [在Rust代码中编写Python - 第1部分](https://pycoders.com/link/3993/web)
    + MARA BOS

In this series, Mara Bos — creator of the inline-python Rust crate — walks you through developing a Rust crate for mixing Python into your Rust code from scratch. Part 1 teaches you how to work with Python from Rust, create macros, and handle white space.

(`是也乎:`

开始了, Python 从设计之初就非常重视 C 扩展,
以便可以嵌入到未来任何生态中,

果然, Rust 也逃不了的...

)



- [用 Python 协程构建有限状态机](https://pycoders.com/link/3983/web)
    + ARPIT BHAYANI

Finite state machines are a mathematical model of computation with numerous applications in both hardware and software. In this tutorial, you’ll learn what a finite state machine is and how to create one in Python using coroutines.

- [更好的 Notebooks Through CI: 自动测试图形机器学习的文档](https://pycoders.com/link/3978/web)
    + HUON WILSON 
    + • Shared by Tim Pitman

Building a data science library is walking between two worlds: data science is dominated by Python notebooks, a fast and convenient way to experiment and demonstrate code in the browser, while software engineering focuses on making software reliable and repeatable. Learn how StellarGraph, a graph machine learning library built on Tensorflow and Keras, uses continuous integration to keep the benefits of both.

- [HPy: 种面向未来的扩展 Python 方法?](https://pycoders.com/link/3977/web)
    + ANTONIO CUNI

“HPy is a joint project which is being developed by PyPy, CPython and Cython developers. It aims to design a better C API for writing Python extensions which is more friendly to alternative implementations and which would allow CPython itself more freedom to experiment (e.g. by using a real GC instead of refcounting).”


(`是也乎:`

大家无论多喜欢 Python ,生产中, 还是得和 C 系统交流, 所以...

)


- [Git Worktrees 和 Pyenv: 更快地开发 Python 库](https://pycoders.com/link/3989/web)
    + HUON WILSON

Workin on a large project means lots of context switches. During a single day, you may need to do review others’ pull requests, respond to code reviews on your own pull requests, work on features, apply small patches. Huon Wilson shares his workflow for minimizing the pain of these context switches using git worktrees and pyenv.

(`是也乎:`

![Worktrees](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2010.58.45.jpg)

嗯哼? 这脑洞可以哪...

)

- [引入 ndindex 一个用于操作 ndarray 索引的 Python 库](https://pycoders.com/link/3985/web)
    + AARON MEURER

“ndindex is a new library that provides high level objects representing the various objects that can index NumPy arrays. These objects automatically canonicalize under the assumption of NumPy indexing semantics, and can be manipulated with a uniform API.”

- [Python 中的排序算法](https://pycoders.com/link/3970/web)
    + REAL PYTHON

In this tutorial, you’ll learn all about five different sorting algorithms in Python from both a theoretical and a practical standpoint. You’ll also learn several related and important concepts, including Big O notation and recursion.


(`是也乎:`

![Sorting](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2010.53.37.jpg)

日常行为中包含大智慧.

)


- [如何窜改 GitHub Organizations 将你的贡献变为 Python](https://pycoders.com/link/4004/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz

Learn how to use the GitHub API to scrape GitHub organizations that you contribute to and create styled components that you can embed on your website.

(`是也乎:`

当 github 变成实际意义上的 程序猿 身份证.

)


- [用 Celery 和 Docker 处理 Django 中的定期任务](https://pycoders.com/link/3994/web)
    + J-O ERIKSSON 
    + • Shared by J-O Eriksson



- [如何用 Python 创建 Windows 服务](https://pycoders.com/link/3973/web)
    + DAVIDE MASTROMATTEO 
    + • Shared by Davide Mastromatteo

(`是也乎:`

不是不可以, 只是没必要.

)
































## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [LayoutX: 具有反应性数据绑定的 Python Tk 声明式 UI 框架](https://pycoders.com/link/3984/web)
    + GITHUB.COM/BOMBERUS

(`是也乎:`

Tk 永远不死.

)


- [avatarify: Zoom 和 Skype 的 Avatars](https://pycoders.com/link/3999/web)
    + GITHUB.COM/ALIEVK


(`是也乎:`


![avatarify](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2010.44.57.jpg)


这样我们就可以用任何一位历史名人作自己的实时直播了...

不过要求的算力也非常...

    GeForce GTX 1080 Ti: 33 fps
    GeForce GTX 1070: 15 fps
    Mac OSX (MacBook Pro 2018; no GPU): very slow ~1 fps


)


- [PyBoy: 用 Python 编写的 Game Boy 模拟器](https://pycoders.com/link/3974/web)
    + GITHUB.COM/BAEKALFEN

(`是也乎:`


![PyBoy](http://ydlj.zoomquiet.top/ipic/2020-04-22-ScreenShot%202020-04-22%2010.42.25.jpg)


嚓...没毛病

可以在 RPi 上运行都...

)

- [pysindy: 从数据中识别稀疏非线性动力系统](https://pycoders.com/link/3995/web)
    + GITHUB.COM/DYNAMICSLAB

- [libpython-clj: Clojure 的 Python 绑定](https://pycoders.com/link/4001/web)
    + GITHUB.COM/CLJ-PYTHON

(`是也乎:`

clj 是在 JVM 上运行的 Lisp,
能自由调用 JAVA 的一切模块;
但是, Lisp 语法还是很囧的,
所以, 就将 py 嵌入到 clj 中来融合到 JAVA 世界...

等等, 不是有 Jython 嘛?

)


- [Terminator: 在一个窗口中加载多个GNOME终端](https://pycoders.com/link/3987/web)
    + GITHUB.COM/GNOME-TERMINATOR



- [ndindex: 用于处理ndarray索引的Python库](https://pycoders.com/link/3988/web)
    + GITHUB.COM/QUANSIGHT

(`是也乎:`


ndarrays 太老了, 应该升级了...于是...
)


- [opencv-proto: 适用于 OpenCV 的 Python 快速原型制作](https://pycoders.com/link/3981/web)
    + GITHUB.COM/IDLESIGN 
    + • Shared by pythonz

(`是也乎:`

机械视觉太火了, 以往都是 C++ 的 OpenCV 为基础,
Py 看不下去了, 然后...

)


















## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [PyCon US 2020 来了：人生苦短，不如线上学 Python](https://mp.weixin.qq.com/s/8PDnbR0XOCDcg2xURxnDYg)
    + 4 月 15 日至 23 日
    + 线上


- [⋅ Remote Meetup Python Madrid](https://pycoders.com/link/4008/web)
    + April 24, 2020

- [⋅ PythonCamp 2020 (Virtual)](https://pycoders.com/link/4007/web)
    + April 25 to April 27, 2020

- [⋅ Remote Python Pizza](https://pycoders.com/link/4009/web)
    + April 25 to April 26, 2020










## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp8py 即将(4.27)开始报名(能开发票 ;-)

参考: 

- tiny4voice 的推荐 [为什么初学编程我建议从Python开始](https://mp.weixin.qq.com/s/GiCLU-bdxY3t0jqdVQ8NIQ)
- 余晟以为 的推荐 [我为什么相信周琦？](https://mp.weixin.qq.com/s/6EgDuXXT3MfR5shHxmE0KQ)









# PS:
- 首发: [Issue 417 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-417.html)
- 修订: [issue-417.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-417.md)


-------------
>> NN 3991

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

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```



-------------



