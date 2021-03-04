Title: Issue 462
Slug: issue-462
Date: 2021-03-03 11:42
Tags: Weekly,Python,pycoders,ZH


> 运行在火星直升机上


原文: [PyCoder's Weekly - Issue #462](https://pycoders.com/issues/462)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210303 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210303 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [语义版本化不会挽救您](https://pycoders.com/link/5856/web)
    + HYNEK SCHLAWACK

Semantic versioning aims to both communicate the version of software as well as promise that certain versions won’t break anything. Sounds great, right? In a lot of cases it is, but a blind reliance on semantic versioning can come back to haunt you.

(`是也乎:`

也就是说, 软件考古学, 并不依赖优雅的版本号.

)


- [Python 和 MongoDB: 连接到 NoSQL 数据库](https://pycoders.com/link/5822/web)
    + REAL PYTHON

Learn how to use Python to interface with the NoSQL database system MongoDB. You’ll get an overview of the differences between SQL and NoSQL, and you’ll also learn about related tools, including PyMongo and MongoEngine.

(`是也乎:`

讲真, Python 内置的 BSDDB 

)



- [用 Python 生成可定制的PDF报告](https://pycoders.com/link/5843/web)
    + MARTIN FITZPATRICK

Learn how to generate custom PDF reports using reportlab and pdfrw with a PyQt GUI.

(`是也乎`

实用

)



- [Python 在火星直升机上运行](https://pycoders.com/link/5857/web)
    + NASA.GITHUB.IO

(`是也乎:`

俺不相信 JPL 已经放弃了 LISP

)


- [Python 3.10.0a6 现在可用于测试](https://pycoders.com/link/5848/web)
    + CPYTHON DEV BLOG

Now including structural pattern matching!

- [Arrow 1.0.0 发布ed](https://pycoders.com/link/5824/web)
    + ARROW.READTHEDOCS.IO

(`是也乎:`

嗯哼? 终于 1.0 了,
就看何时被 Python 官方内建了,
那才是真正融入历史.
)

- [Python 开发人员2020调查结果](https://pycoders.com/link/5827/web)
    + JETBRAINS.COM

(`是也乎:`

为了多卖些许可证, 喷脑 很拼了...

)

- [祝 Python 和 Python 软件基金会周年快乐!](https://pycoders.com/link/5828/web)
    + PYTHON SOFTWARE FOUNDATION




## 探讨/吐糟
> Discussions


- [Python 马上可能支持:索引编制关键字参数](https://pycoders.com/link/5858/web)
    + RAYMOND HETTINGER

For example, you could do matrix[row=20, col=40]. Read more about it in PEP 637.



- [Spyder 是一个被低估 IDE](https://pycoders.com/link/5823/web)
    + REDDIT

(`是也乎:`

Spyder 又开始吹了,
其实 UliEditor 也被 `Underrated` 的;

或是说一切 IDE 都是被低估的?

)


- [+= 运算符在 Python 中返回什么?](https://pycoders.com/link/5845/web)
    + STACK OVERFLOW


## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 中的导航名称空间和范围](https://pycoders.com/link/5862/web)
    + REAL PYTHON 
    + course

Learn about Python namespaces, the structures used to store and organize the symbolic names created during the execution of a Python program. You’ll learn when namespaces are created, how they are implemented, and how they define variable scope.

- [Friendly-traceback: 用真实 Python 进行测试](https://pycoders.com/link/5829/web)
    + ANDRÉ ROBERGE

See how friendly-traceback improves syntax error reporting by comparing the output from friendly-traceback with examples in the Real Python tutorial Invalid Syntax in Python: Common Reasons for SyntaxError.

(`是也乎:`

基本语法使用习惯, 是无论多友好的提示也无法加速习惯的.
习惯,只能在足够数量练习中形成.

)

- [成为 Python 专业人员的挑战](https://pycoders.com/link/5842/web)
    + REAL PYTHON 
    + podcast

What’s the difference between writing code for yourself and developing for others? What new considerations do you need to take into account as a professional Python developer? This week on the show, we talk to Dane Hillard about his book “Practices of the Python Pro”.


(`是也乎:`

![Professional](http://ydlj.zoomquiet.top/ipic/2021-03-03-ScreenShot%202021-03-03%2010.33.07.jpg)


职业与否在技术上本质差异,
可能就象建筑师是否正经类似:
    
    愿意终生为写出来的代码负责嘛?


)


- [Brython: 浏览器中的 Python](https://pycoders.com/link/5854/web)
    + REAL PYTHON

Learn how to use Brython to run Python code in the browser. Although most front-end web applications are written in JavaScript, you can use Brython to access JavaScript libraries and APIs and deploy Python-based applications to the web.

(`是也乎:`

![Brython](http://ydlj.zoomquiet.top/ipic/2021-03-03-ScreenShot%202021-03-03%2010.30.17.jpg)


WebAssembly/wasm 之前的想法,
现在...呵
)


- [使测试成为您应用程序的一部分](https://pycoders.com/link/5825/web)
    + NIKITA SOBOLEV

Have you ever written a test that re-implements a library-specific case? What if that test was just a part of the library code? See how tightly integrating tests into your library code can save users time and help them find bugs.

(`是也乎:`

FastAPI 就率先融合进来了.

)

- [在 Django 中的 Postgres 高效全文搜索](https://pycoders.com/link/5849/web)
    + ADEYINKA ADEGBENRO 
    + • Shared by Manuel Weiss

Learn how to optimize a Full Text Search implementation with Django and Postgres. Even on a small table, you can reduce the query execution time from 0.045 seconds to 0.001 seconds!


(`是也乎:`

是的, Pg 这功能就很不讲 `武德` 了,
抢了多少搜索引擎的生意哪.

)


- [用 line_profiler 分析 Python 代码](https://pycoders.com/link/5861/web)
    + MATT WRIGHT

Use line_profiler to see line-level execution time for your python code. It may surprise you where your code is slow and what it takes to speed it up!



## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [fprime: 飞行软件和嵌入式系统框架](https://pycoders.com/link/5855/web)
    + GITHUB.COM/NASA

(`是也乎:`

期待 DJI 的开源

)

- [arrow: 为 Python 更好的日期和时间](https://pycoders.com/link/5836/web)
    + GITHUB.COM/ARROW-PY


(`是也乎:`

叕一次被推荐, 日期/时间, 太常见数据了,
但是, 能直觉吻合的处理, 实在又太不简单.

)

- [dnc: 用于检查域名配置的 CLI 工具](https://pycoders.com/link/5859/web)
    + GITHUB.COM/FCAMBUS


- [Gradient-Free-Optimizers: 简单可靠优化 数值搜索空间 ](https://pycoders.com/link/5840/web)
    + GITHUB.COM/SIMONBLANKE



- [line_profiler: 适用于Python的逐行分析](https://pycoders.com/link/5850/web)
    + GITHUB.COM/PYUTILS

(`是也乎:`

等等? 有必要嘛?

)


- [absolufy-imports: 自动将将相对 引入 转换为绝对 引入](https://pycoders.com/link/5837/web)
    + GITHUB.COM/MARCOGORELLI 
    + • Shared by Marco Gorelli

(`是也乎:`

类似要配置 .pre-commit-config.yaml:

```
-   repo: https://github.com/MarcoGorelli/absolufy-imports
    rev: v0.2.2
    hooks:
    -   id: absolufy-imports
```

怎么说呢? 想法是好的,现实是现实

)

- [django-reversion-compare: Django-Reversion 修订的比较/差异视图](https://pycoders.com/link/5835/web)
    + GITHUB.COM/JEDIE

- [NBShare: 分享您的 Python Notebooks](https://pycoders.com/link/5832/web)
    + NBSHARE.IO 
    + • Shared by John Ludhi

(`是也乎:`

叕一个 `IPy[NB]` 分享服务,
只是,这个更加朴素, 不可运行, 只是展示,
那么, 一定有人拿来当私人文章/网站发布平台的,
然后, 就和谐了...

)

## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5839/web)
    + March 3, 2020

(`是也乎:`

即便是线上的, 一样收费.

)


- [⋅ Python Web Conference 2021 (Virtual)](https://pycoders.com/link/5761/web)
    + March 22 – 26, 2021


- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)


- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)


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

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)


# PS:
- 首发: [Issue 462 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-462.html)
- 修订: [issue-462.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-462.md)


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


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/462)






