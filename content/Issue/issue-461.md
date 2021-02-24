Title: Issue 461
Slug: issue-461
Date: 2021-02-24 11:42
Tags: Weekly,Python,pycoders,ZH


> Happy Birthday, Python;-)


原文: [PyCoder's Weekly - Issue #461](https://pycoders.com/issues/461)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210224 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210224 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Python 并发: 棘手问题](https://pycoders.com/link/5790/web)
    + HAMEL HUSAIN

An exploration of threads, processes, and coroutines in Python, with interesting examples that illuminate the differences between each.

(`是也乎:`

类似 CAP 法则,
嫑想同时什么好处都有;

通过其它经过考验的高并发能力系统转移矛盾,
Py 安心作自己擅长的事儿就好.

)


- [为什么真的需要升级 Pip](https://pycoders.com/link/5798/web)
    + ITAMAR TURNER-TRAURING

If you’re using an old version of pip, installing the latest version of a Python package might fail—or install in a slower, more complex way. Learn what the problem is exactly, how to solve it, and what causes it.

(`是也乎:`

官方广告..

其实, 不用任何 pip 指令就能完备部署的系统才是合格的生产系统.

)


- [用 Python 每秒12个请求](https://pycoders.com/link/5805/web)
    + SUADE.ORG

How much should we trust framework benchmarks? And to what extent should they influence your choice of technology?

(`是也乎:`

嗯哼? 这就是打脸了...
标准化是技术到一个大平台期了,
大家无法作到差异化时...

![toto](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.55.15.jpg)

)


- [Python & APIs: 读取公共数据的成功组合](https://pycoders.com/link/5803/web)
    + REAL PYTHON

Learn what APIs are and how to consume them using Python. You’ll also learn some core concepts for working with APIs, such as status codes, HTTP methods, using the requests library, and much more.

(`是也乎:`

![Public](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.51.34.jpg)

其实, 开放数据接口, 最要命的一点就是:

    嫑乱变

嘦是一个版本的接口, 无论多不合理, 发布后就没改,
否则, 对应下游系统就囧了.


)



- [Python 字符串如何工作](https://pycoders.com/link/5786/web)
    + VIKTOR SKVORTSOV

Learn the ins and outs of how Python strings work, with a focus on how text is encoded and represented internally.

(`是也乎:`

老爹最心塞的一次架构,
导致最后 2->3 无法兼容

)


- [Python 3.X至3.9.1的缓冲区溢出可能导致远程执行代码](https://pycoders.com/link/5816/web)
    + NIST.GOV

Upgrade to 3.8.8 or 3.9.2 to avoid the issue.


## 探讨/吐糟
> Discussions



- [Happy Birthday, Python!](https://pycoders.com/link/5791/web)
    + REDDIT

- [回顾 Python 的第一个 Beta 版本](https://pycoders.com/link/5799/web)
    + TWITTER.COM/SFERMIGIER

In celebration of Python’s 30th anniversary, Stefane Fermigier has posted the code for Python’s first beta release on GitHub.

(`是也乎:`

就好象回顾 Bill 第一个 VB 程序一样
)


- [从 print('Hello World!') 到获得第一份工作](https://pycoders.com/link/5780/web)
    + REDDIT

(`是也乎:`

其实, 多数情况和技术无法,
看因缘了

)



## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Happy Birthday, Python, 本周已30岁了!](https://pycoders.com/link/5797/web)
    + THOMAS CLABURN

Via interviews with Armin Ronacher, Brett Cannon, and Ewa Jodloski, this piece of technical journalism takes a look at where Python has been, where it is, and where it is going.

(`是也乎:`

所以:
[30 周岁的 Python，“虐”我 20 年](https://mp.weixin.qq.com/s/bOOeRZNnClXQ-IrwlPeSoA)

)


- [Python 编程和数值方法: 面向工程师和科学家的指南](https://pycoders.com/link/5793/web)
    + QINGKAI KING, 
    + TIMMY SIAUW, 
    + ALEXANDRE BAYEN

This open-source book from Berkeley discusses numerical methods with Python. Numerical methods are essential for engineering and science, making this book a fantastic resource for folks in STEM fields.


- [抽象语法树在 Python](https://pycoders.com/link/5808/web)
    + ALESSANDRO FINAMORE 
    + • Shared by Bob Belderbos

Learn about abstract syntax trees (ASTs), some of their use cases, and how to use the ast module in the Python standard library.


(`是也乎:`


![Syntax](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.45.03.jpg)

Python 之后现代语言,基本都尽可能将语法解析能力内建,
以便大家更加自在的拓展自身.


)


- [随机梯度下降和在 Web 上部署 Python 脚本](https://pycoders.com/link/5814/web)
    + REAL PYTHON 
    + podcast

Do you know the initial steps to get your Python script hosted on the web? You may have built something with Flask, but how would you stand it up so that you can share it with others? This week on the show, guest Martin Breuss shares his recent article titled, “Python Web Applications: Deploy Your Script as a Flask App”. David Amos also returns, and he’s brought another batch of PyCoder’s Weekly articles and projects.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.44.23.jpg)

)


- [Dictionaries 和 Arrays: 选择理想的数据结构](https://pycoders.com/link/5784/web)
    + REAL PYTHON 
    + course

Learn about two of Python’s data structures: dictionaries and arrays. You’ll look at multiple types and classes for both of these and learn which implementations are best for your specific use cases.

(`是也乎:`

![Dictionaries](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.43.58.jpg)

)

- [Python 的函数式编程: 何时以及如何使用它](https://pycoders.com/link/5807/web)
    + REAL PYTHON

Learn what functional programming is, how it’s supported in Python, and how you can use it in your Python code.

(`是也乎:`

![FP](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.42.30.jpg)

简单说: 能,但别多用


)

- [理解 Django: 测试您的应用](https://pycoders.com/link/5810/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

Learn how to use automated tests to verify the correctness of your Django site.

(`是也乎:`


Django 成为工业化标准关键指标就是测试自动化程度...

)


- [用 Chart.js 将图表添加到 Django](https://pycoders.com/link/5779/web)
    + NIK TOMAZIC 
    + • Shared by Michael Herman

Learn how to add interactive charts to Django with Chart.js.

(`是也乎:`

丑, 用点儿专业的图表库吧...

)


## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [scikit-image: Python 中的图像处理](https://pycoders.com/link/5789/web)
    + GITHUB.COM/SCIKIT-IMAGE


(`是也乎:`

> License (Modified BSD)

哈?

)

- [python-precisely: Python 测试中更好的断言](https://pycoders.com/link/5782/web)
    + GITHUB.COM/MWILLIAMSON

(`是也乎:`


很有想法, 就看哪个测试框架先吸收了

)


- [Freewire: “自由”有线神经网络的实验](https://pycoders.com/link/5778/web)
    + GITHUB.COM/NOAHTREN

(`是也乎:`

> Freely

比 free 看起来要贵

)

- [CompreFace: 免费和开源 的 人脸识别系统](https://pycoders.com/link/5800/web)
    + GITHUB.COM/EXADEL-INC

(`是也乎:`

放心对黄色人种效果一般?

![Pg](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2010.32.45.jpg)


)


- [eth2.0-specs: 以太坊2.0规范](https://pycoders.com/link/5794/web)
    + GITHUB.COM/ETHEREUM

- [metaflow: 轻松构建和管理现实生活中的数据科学项目](https://pycoders.com/link/5792/web)
    + GITHUB.COM/NETFLIX

(`是也乎:`

> ..现实生活..

最关键的是数据的有效稳定获得,
注意, 为什么是 `奶飞` 开源的?

![奶飞](http://ydlj.zoomquiet.top/ipic/2021-02-24-ScreenShot%202021-02-24%2011.29.50.jpg)

)



- [ptpython: 更好的 Python REPL](https://pycoders.com/link/5785/web)
    + GITHUB.COM/PROMPT-TOOLKIT

(`是也乎:`

叕一个 REPL 增强,
其实,这类单品的竞争对手就是 IDE 大厂们;

)


- [orator: 一个简单而美丽的 ActiveRecord 实现](https://pycoders.com/link/5813/web)
    + GITHUB.COM/SDISPATER

(`是也乎:`

模型复刻工,
好象也是一种专门工种了. 

)

## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5802/web)
    + February 17, 2020

(`是也乎:`

即便是线上的, 一样收费.

)


- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)

- [⋅ Python Web Conference 2021 (Virtual)](https://pycoders.com/link/5761/web)
    + March 22 – 26, 2021



- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


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


# PS:
- 首发: [Issue 461 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-461.html)
- 修订: [issue-461.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-461.md)


-------------

好文笔,感叹号年度配额: **2/3**

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
>> NN 4285


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/461)






