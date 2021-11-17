Title: PyCoder 499
Slug: issue-499
Date: 2021-11-17 11:42
Tags: Weekly,Python,pycoders,ZH


> OLPC 编程教育方面的遗产


原文: [PyCoder's Weekly - Issue #499](https://pycoders.com/issues/499)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211117 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211117 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [PSF 正寻求下一位执行董事](https://pycoders.com/link/7412/web)
    + PYTHON SOFTWARE FOUNDATION

After announcing earlier this summer that Ewa Jodlowska is leaving after ten years of service, the PSF has begun its search for the organization’s next Executive Director. Interested? You can apply here.

- [选择编程语言总是会被过早优化](https://pycoders.com/link/7408/web)
    + BRETT CANNON 
    + opinion

“Have you ever been told that Python couldn’t be used for a project because it wouldn’t be fast enough? I have, and I find it a bit frustrating as big banks, YouTube, Instagram, and plenty of other places that are performance-sensitive still manage to select Python and be happy.”

(`是也乎:`

在没深入理解前, 被市井传说忽悠是必然;
当年从 PHP 转入 Python 也纯粹因为 Plone,
进来才发现, Python 的世界远大于 CMS

)



- [Python 开发者的高级 VSCode](https://pycoders.com/link/7427/web)
    + REAL PYTHON

In this tutorial, you’ll learn how you can configure, extend, and optimize Visual Studio Code for a more effective and productive Python development environment. By digging into this customizable code editor and IDE, you’ll put yourself on track to be a VS Code power user.


(`是也乎:`


![Advanced](https://ipic.zoomquiet.top/2021-11-17-zshot%202021-11-17%2009.49.13.jpg)

嗯哼, 现在只想关闭自动提醒...


)



- [用 Gunicorn/Nginx 和 HTTPS 安全部署 Django 应用](https://pycoders.com/link/7406/web)
    + REAL PYTHON

Ready to take your Django app beyond development? Learn how to securely deploy your Django web app in production over HTTPS with Gunicorn and Nginx. Along the way, you’ll explore how HTTP headers can fortify your app’s security.


(`是也乎:`

其实, 一直以来关键问题都是 SSL 证书的生成和管理.

![Securely](https://ipic.zoomquiet.top/2021-11-17-zshot%202021-11-17%2009.49.01.jpg)

)


- [Python 列表数据结构如何真正有效](https://pycoders.com/link/7405/web)
    + ANTON ZHIYANOV 
    + • Shared by Anton Zhiyanov

This article explores the nuts and bolts of Python list operations, their time complexity, and underlying data structures.


(`是也乎:`

经典老书: 源代码鉴赏 可刷

)


- [Django Bugfix 发布: 3.2.9](https://pycoders.com/link/7420/web)
    + DJANGO SOFTWARE FOUNDATION



-----------------------------------------
## 探讨/吐糟
> Discussions


NIL




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [OLPC 编程教育方面的遗产](https://pycoders.com/link/7435/web)
    + REAL PYTHON 
    + podcast

Do you remember the One Laptop Per Child program? What went wrong, and what can we learn from the program’s failure? What are the potential pitfalls of charismatic technology, and how can we avoid them when introducing students to programming? This week on the show, former guest Al Sweigart and author Morgan Ames are here to talk about her book “The Charisma Machine - The Life, Death, and Legacy of One Laptop per Child.”


(`是也乎:`


![podcast](https://ipic.zoomquiet.top/2021-11-17-zshot%202021-11-17%2009.44.50.jpg)


OLPC ~ 传奇项目,
当年 RMS 日常也用,
俺也折腾到过一台,
只是键盘太小, 没办法成为日常;
的确, 主要界面以及应用都是 Pyhton 嗯哼的

)


- [Ruby vs Python Comes Down to the for Loop](https://pycoders.com/link/7413/web)
    + DOUG TURNBULL

“Contrasting how each language handles iteration helps understand how to work effectively in either.” Related discussion of this article on Hacker News.


- [用 Google Maps API 创建距离矩阵](https://pycoders.com/link/7430/web)
    + JUAN ACOSTA 
    + • Shared by Juan Acosta

This article describes step by step how to use the Google Maps Distance Matrix API, how to parse its data to create a distance table and finally, how to store the parsed data in a data base.

(`是也乎:`

前提是可以访问到 G 字全家桶

)


- [Cython, Rust, 等等: 为 Python Extensions 选择一种语言](https://pycoders.com/link/7431/web)
    + ITAMAR TURNER-TRAURING

You can write Python extensions with Cython, Rust, and many other tools. In this article you’ll learn which one you should use, depending on your particular use case and needs.

(`是也乎:`

不是, 难道拓展开发语言最好的, 不就是 Py 自己?

)


- [Async Python 并不快](https://pycoders.com/link/7414/web)
    + CAL PATERSON

“Async Python is slower than ‘sync’ Python under a realistic benchmark. A bigger worry is that async frameworks go a bit wobbly under load.”




- [Monads and Python](https://pycoders.com/link/7404/web)
    + ROBERT COLLINS


“Porting Monads to Python is a common hobby. But should we really do it?”

(`是也乎:`

Python 作为多范式典范, 当然也支持下上 Monads 的,
只是, 日常并没注意到,


)



- [Python 和 Dataclasses 以及 Union 惯用代数数据类型](https://pycoders.com/link/7418/web)
    + EDWARD Z. YANG


(`是也乎:`

Idiomatic 其实都是老司机的习惯,
之所以形成也都是为了节省精力...

)


- [无限嵌套的字典](https://pycoders.com/link/7407/web)
    + SUSAM PAL

(`是也乎:`

是可以无限,
不过, GraphQL 中也证明了, 别套件太多层,
除非你是 LISP 运动员

)


- [用 Pytorch 的 Seq2seq 模型来德语翻译](https://pycoders.com/link/7416/web)
    + JOHN LUDHI





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [pyAirtable: Python Client for the Airtable API](https://pycoders.com/link/7425/web)  
    + PYAIRTABLE.READTHEDOCS.IO

- [kuroko: Python 方言/具有显式变量声明和块范围](https://pycoders.com/link/7426/web)
    + GITHUB.COM/KUROKO-LANG

(`是也乎:`

一个能嵌入滴运行的 Python 解析引擎

)

- [python-mini-projects: 迷你项目/提升您的Python技能](https://pycoders.com/link/7432/web)
    + GITHUB.COM/PYTHON-WORLD

(`是也乎:`

500行之后, 又一个示例项目集锦;
关键参考是各种领域问题解决项目结构;

)


- [Model Bakery: Smart Fixtures 用于更好的测试](https://pycoders.com/link/7436/web)
    + MODEL-BAKERY.READTHEDOCS.IO



- [s3-credentials: 为 S3存储桶 创建凭据的工具](https://pycoders.com/link/7428/web)
    + SIMONWILLISON.NET

(`是也乎:`

AWS yyds ~ 俺是说收费领域

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Women Who Code CONNECT Forward 2021](https://pycoders.com/link/7419/web)
    + November 18 to November 20, 2021

- [⋅ PyData Bristol Meetup](https://pycoders.com/link/7417/web)
    + November 18, 2021

- [⋅ Python Northwest](https://pycoders.com/link/7421/web)
    + November 18, 2021

- [⋅ PyCon APAC 2021](https://pycoders.com/link/7409/web)
    + November 19 to November 24, 2021

- [⋅ Xtreme Python](https://pycoders.com/link/7439/web)
    + November 24 to November 25, 2021




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 499 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-499.html)
- 修订: [issue-499.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-499.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF499D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF499D4Q90XdDA7g):



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





