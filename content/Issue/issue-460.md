Title: Issue 460
Slug: issue-460
Date: 2021-02-17 11:42
Tags: Weekly,Python,pycoders,ZH


> PEP 8 之歌


原文: [PyCoder's Weekly - Issue #460](https://pycoders.com/issues/460)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210217 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210217 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [PEP 634: 结构模式匹配 ( match / case )](https://pycoders.com/link/5772/web)
    + PYTHON.ORG

A few links related to PEP 634, which will add structural pattern matching to Python via a new match/case statement: PEP 634 (Specification), PEP 635 (Motivation and Rationale), PEP 636 (Tutorial & Examples)

- [Python 字符串是不可变的/但仅在有时是](https://pycoders.com/link/5750/web)
    + AUSTIN HENLEY

It turns out you can mutate a string in Python… sort of.


(`是也乎:`

困难的总是不时点

)



- [用 Pandas 轻松解决困难的数据分析问题](https://pycoders.com/link/5744/web)
    + MARTIN 
    + • Shared by Martin

A great strategy to use when faced with a tricky data analysis problem is to reshape the dataset into a format that turns it into an easy problem. In this article, you’ll look at an example involving a simple calculation and extensive reshaping in pandas.


(`是也乎:`

数据分析并不难,
难就难在: 如何清洁原始数据, 以及事先形成偏见.

)


- [用 Pandas 有效清洗文本](https://pycoders.com/link/5745/web)
    + CHRIS MOFFITT

In this article, you’ll see some examples of cleaning text fields in a large data file and learn several strategies for efficiently cleaning unstructured text fields using Python and pandas.

(`是也乎:`

Pandas 也变成一个通用数据清洁机了..,..

)


- [构建富终端仪表板](https://pycoders.com/link/5759/web)
    + WILL MCGUGAN

Learn how to use the Rich CLI library’s new terminal dashboard feature.

(`是也乎:`

![Terminal](http://ydlj.zoomquiet.top/ipic/2021-02-17-ScreenShot%202021-02-17%2018.41.46.jpg)


基本上这种界面也只有影视作品中值得用,
现实中, 包含一点儿中文就全部错行了...


)


- [带 gRPC 的 Python 微服务](https://pycoders.com/link/5754/web)
    + REAL PYTHON

Learn how to build a robust and developer-friendly Python microservices infrastructure using gRPC and Kubernetes. You’ll also explore advanced topics such as interceptors and integration testing.

(`是也乎:`

![gRPC](http://ydlj.zoomquiet.top/ipic/2021-02-17-ScreenShot%202021-02-17%2018.40.24.jpg)

这个插图比较马虎...

)



- [Python 3.7.10 和 3.6.13 安全更新现已发布](https://pycoders.com/link/5755/web)
    + CPYTHON DEV BLOG




## 探讨/吐糟
> Discussions

- [新 match/case 令人耳目一新](https://pycoders.com/link/5756/web)
    + RUSSELL KEITH-MAGEE 
    + & BRANDON RHODES

Numerous people opine on Twitter about the new match/case statement expected in Python 3.10. While some folks welcome the powerful new syntax, others lament the syntax bloat and potential for confusion they see in the new feature.

(`是也乎:`

和 Erlang/Elixir 相比还差点儿意思

)


- [Python 模式匹配的接收](https://pycoders.com/link/5769/web)
    + HACKER NEWS

Discussion of last week’s acceptance of PEP 634.





## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 加密 , Rust, 和 Gentoo](https://pycoders.com/link/5767/web)
    + JAKE EDGE

A recent update to the Python cryptography library, which has started replacing some of its C code with Rust, stirred up some controversy among users and library maintainers.


(`是也乎:`

好久没有 Gentoo 出镜了

)


- [和 Brett Cannon 一起阐明 Python 语法至其核心](https://pycoders.com/link/5739/web)
    + REAL PYTHON 
    + podcast

Brett is a Python core developer and he’s been working on a series of articles where he is unraveling the syntax of Python. His series is a fantastic resource for those wanting to learn how Python is structured and works at its core.REAL PYTHON podcast

(`是也乎:`

![Unraveling](http://ydlj.zoomquiet.top/ipic/2021-02-17-ScreenShot%202021-02-17%2018.49.15.jpg)

)

- [PEP 8 之歌](https://pycoders.com/link/5741/web)
    + LEON SANDØY 
    + video

A songification of that most holiest of Python Enhancement Proposals.


(`是也乎:`

唉嘛都有专用歌曲了...

最神圣的...
)


- [Pandas Sort: 数据排序指南](https://pycoders.com/link/5763/web)
    + REAL PYTHON

Learn how to sort data in a pandas DataFrame using the pandas sort functions sort_values() and sort_index().

- [关于一个有趣的使用问题->Python 的字面量](https://pycoders.com/link/5730/web)
    + CHRIS SIEBENMANN

When you use is to compare a value to a literal, such as the empty string '', you’ll see a SyntaxWarning that tells you not to use is that way, but your code may still work as intended. Learn why your code still works, and why you really should heed the warning.

- [为 GUI 应用程序创建 PyQt 布局](https://pycoders.com/link/5735/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn how to use PyQt layouts to arrange and manage the graphical components on your GUI applications. With the help of PyQt’s layout managers, you’ll be able to create polished and professional GUIs with minimal effort.

- [无法离开的Python“技巧”](https://pycoders.com/link/5734/web)
    + SEBASTIAN OPAŁCZYŃSKI

Learn some fun and useful Python “tricks” that can help you write cleaner and more maintainable code.

(`是也乎:`

既然是 Tricks 就不应该多用.

)


- [用 Nim 加速 Python 代码](https://pycoders.com/link/5757/web)
    + WULF

You need to speed up some Python code, but don’t know C and don’t have time to learn it. Enter Nim!

(`是也乎:`

叕一个 Python 运行加速器.

)


- [向 Flask 添加社会网络认证](https://pycoders.com/link/5737/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

Learn how to add social authentication with GitHub and Twitter to a Flask application.

(`是也乎:`

印度弟兄的思考...

)


- [Earley Parser](https://pycoders.com/link/5733/web)
    + RAHUL GOPINATH

Here’s an article for the computer science-minded folks. Learn how to create an Earley parser from scratch in Python, which allows you to use any context-free grammar to parse a string and recover all of the parse trees that correspond to the grammar from the generated parse forest. Heady stuff, I know!

(`是也乎:`

如何从0开始构造一个解析器...

叕一个本科基础科目练习题解

)


## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [dependabot-bot: 满足特定条件时/自动合并PR](https://pycoders.com/link/5736/web)
    + GITHUB.COM/TONYBALONEY


(`是也乎:`


自动 merge?
那 PR 的意义何在?

)

- [trustme: TLS 证书 for the Discerning Tester](https://pycoders.com/link/5731/web)
    + GITHUB.COM/PYTHON-TRIO

- [sdf: Python 中简单的SDF网格生成](https://pycoders.com/link/5747/web)
    + GITHUB.COM/FOGLEMAN

- [Spokestack: 语音应用程序库](https://pycoders.com/link/5738/web)
    + GITHUB.COM/SPOKESTACK 
    + • Shared by Will Rice

(`是也乎:`

对方言没办法的, 都是不可用的.

)


- [NAVis: 神经元分析和可视化](https://pycoders.com/link/5765/web)
    + GITHUB.COM/SCHLEGELP 
    + • Shared by Philipp Schlegel

(`是也乎:`

叕一个可视化神经元分析器,
其实, 可视化对于生产并不重要,
只是在教学中有意义...

)

- [geovoronoi: 绘制在地理区域](https://pycoders.com/link/5752/web)
    + GITHUB.COM/WZBSOCIALSCIENCECENTER 
    + • Shared by Markus Konrad


(`是也乎:`


![Geographic](http://ydlj.zoomquiet.top/ipic/2021-02-17-ScreenShot%202021-02-17%2018.32.16.jpg)


Q 的
)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5740/web)
    + February 17, 2020

(`是也乎:`

即便是线上的, 一样收费.

)


- [⋅ WeAreDevelopers Live (Virtual)](https://pycoders.com/link/5758/web)
    + February 17 – 18, 2021


- [⋅ Python Web Conference 2021 (Virtual)](https://pycoders.com/link/5761/web)
    + March 22 – 26, 2021


- [⋅ PyCascades 2021 (Virtual)](https://pycoders.com/link/5609/web)
    + February 19 – 21, 2021

(`是也乎:`

![Diamond](http://ydlj.zoomquiet.top/ipic/2021-01-20-ScreenShot%202021-01-20%2009.40.38.jpg)


)


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
- 首发: [Issue 460 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-460.html)
- 修订: [issue-460.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-460.md)


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


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/460)






