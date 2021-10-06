Title: PyCoder 492
Slug: issue-492
Date: 2021-09-29 11:42
Tags: Weekly,Python,pycoders,ZH


> Django 4.0 来了


原文: [PyCoder's Weekly - Issue #492](https://pycoders.com/issues/492)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 210929 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210929 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 背景: GIL 以及其对 Python Multithreading 的影响](https://pycoders.com/link/7101/web)
    + VICTOR SKVORTSOV


GIL stands for the Global Interpreter Lock, and its job is to make the CPython interpreter thread-safe. This post tells you more about non-obvious effects of the GIL. Along the way, you’ll see what the GIL really is, why it exists, how it works, and how it’s going to affect Python concurrency in the future.

(`是也乎:`

沈游侠也曰过类似的断言,
毕竟 Guido 老爹不傻...

)


- [Django 模板语言: 标签和过滤器](https://pycoders.com/link/7109/web)
    + REAL PYTHON

Django templates use their own mini-language that’s inspired by Python. This tutorial covers Django template tags and filters, explaining how to compile and use templates. It covers conditional blocks, looping, and inheritance in tags as well as filters for strings and filters for lists.

(`是也乎:`

![DTL](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.41.08.jpg)

)

- [ Django 4.0 中的新测试功能](https://pycoders.com/link/7107/web)
    + ADAM JOHNSON

Django 4.0 had its first alpha release last week and the final release should be out in December. It contains an abundance of new features, which you can check out in the release notes. This post looks at the changes to testing in a bit more depth.


(`是也乎:`

就象 Py3 ?


)


- [教程中有关 PyPI 从不说的4件事儿](https://pycoders.com/link/7115/web)
    + PAOLOA AMOROSO

“Although it’s well known PyPI is unforgiving for good reasons, the package publishing process is not as straightforward as the tutorials make it seem. I run into a few unexpected minor bumps none of the guides mention.”

(`是也乎:`

PyPI 公开的机密

)


- [Django 4.0 Alpha 1 发布](https://pycoders.com/link/7106/web)
    + DJANGO SOFTWARE FOUNDATION

See the full changelog here.




- [scikit-learn 1.0 发布亮点](https://pycoders.com/link/7108/web)
    + SCIKIT-LEARN.ORG

(`是也乎:`

竟然出 1.0 了...
好象永远不发布1.0 的才是最Nb 的?


)


-----------------------------------------
## 探讨/吐糟
> Discussions



- [Stack Overflow: Python 刚刚超过 Java 作为问题最多的第二语言](https://pycoders.com/link/7114/web)
    + REDDIT

(`是也乎:`

所以, 第一是谁?

)

- [Zappa 不再维护](https://pycoders.com/link/7117/web)
    + REDDIT

(`是也乎:`

淦...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 作为构建工具](https://pycoders.com/link/7093/web)
    + NIKITA TONSKY

“Normally, when starting a Java project (or any other programming project, really), you don’t want to reinvent the wheel. You go with the de-facto build system, folder structure, environment, etc. The ones that the rest of the world is using. Yet, both Skija and JWM are built using Python scripts instead of more traditional Ant/Maven/Gradle/SBT. Why? Let’s find out!”

(`是也乎:`

大型 JAVA 项目为毛用 Python 来管理构建?

)


- [测量您的 Python 学习进度](https://pycoders.com/link/7083/web)
    + REAL PYTHON 
    + podcast

Where are you along the path of learning Python? Do you feel like you’re making progress? What are ways you can put the learning path into a more precise focus? This week on the show, a discussion with Martin Breuss about his recent article “How Long Does It Take to Learn Python?”



(`是也乎:`
![Measuring](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.36.36.jpg)

衡量是最困难也最值得的学习行为


)


- [Rock, Paper, Scissors With Python: 命令行游戏](https://pycoders.com/link/7103/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn to program rock paper scissors in Python from scratch. You’ll learn how to take in user input, make the computer choose a random action, determine a winner, and split your code into functions.

(`是也乎:`

![Rock](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.34.30.jpg)

)


- [在 Python 反转字符串: reversed() , Slicing, 等等](https://pycoders.com/link/7084/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to reverse strings in Python by using available tools such as reversed() and slicing operations. You’ll also learn about a few useful ways to build reversed strings by hand.

(`是也乎:`

![Reverse](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.32.42.jpg)

其实, 这种翻转

)


- [了解 Django: User File 使用](https://pycoders.com/link/7095/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

Maybe your Django app needs to handle files from users like profile pictures. Accepting files from others is tricky to do safely. In this article, you’ll see the tools that the framework provides to manage files safely.

- [Django REST Framework Views - APIViews](https://pycoders.com/link/7102/web)
    + ŠPELA GIACOMELLI 
    + • Shared by Špela Giacomelli

Django REST Framework (DRF) has its own flavor of views that inherit from Django’s View class. This article explores the most basic of the views: APIView. APIView is the base for every other DRF view.

(`是也乎:`

随着业务拓展, 各种元需求才能正确识别并实现.

)


- [为毛 Black 坚持重新格式化我的整个项目?](https://pycoders.com/link/7097/web)
    + ŁUKASZ LANGA


Why Black recommends adopting it by reformatting your entire codebase in one go and refuses to do “region reformatting.” Thoughts from the creator for the popular Python auto-formatter.

(`是也乎:`

因为 => 从不妥协

)


- [使用 Borb 拆分/合并和旋转 PDF 文件](https://pycoders.com/link/7098/web)
    + JORIS SCHELLEKENS 
    + • Shared by Joris Schellekens


Split, merge and rotate PDF documents using borb, the open-source pure Python PDF library.

(`是也乎:`

嗯哼? 发票构建库, 当然也可以干其它的事儿../.

)



- [Type Check 你的 Django App](https://pycoders.com/link/7086/web)
    + KRACEKUMAR RAMARAJU 
    + • Shared by Kracekumar Ramaraju

How to add gradual typing to your Django app, focusing on Django views and Django models.




- [Unravelling the async with Statement](https://pycoders.com/link/7089/web)
    + BRETT CANNON

- [游戏在 Python: PyGame vs Arcade vs PyGame Zero](https://pycoders.com/link/7116/web)
    + SHANTNU TIWARI




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [logparser: 用于常用日志格式的命令行解析器](https://pycoders.com/link/7099/web)
    +     GITHUB.COM/LUCIANMARIN

- [MPLG: Matplotlib GUI, 视觉设计绘图并输出 Python 代码](https://pycoders.com/link/7088/web)
    +     EVERYDAYANCHOVIES.GITHUB.IO

(`是也乎:`


![MPLG](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.21.46.jpg)
无代码 思想产物...
不过, 资深用户一定还是不得不回到代码中来吧...


)

- [PDM: 支持PEP 582 的 Python 包管理器](https://pycoders.com/link/7096/web)
    + FMING.DEV

(`是也乎:`


对 NPM 的致敬?

)


- [clang-format: 代码格式化器Python绑定](https://pycoders.com/link/7081/web)
    + GITHUB.COM/SSCIWR 
    + • Shared by Henry Schreiner

- [hist: Pythonic Notebook-Ready Histograms Built on boost-histogram](https://pycoders.com/link/7085/web)
    + GITHUB.COM/SCIKIT-HEP 
    + • Shared by Henry Schreiner


(`是也乎:`

不是, 为什么突然怼上 Histogram 了呢?

)

- [boost-histogram: 强大直方图对象 for Python](https://pycoders.com/link/7092/web)
    + GITHUB.COM/SCIKIT-HEP 
    + • Shared by Henry Schreiner



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyConTW 2021](https://pycoders.com/link/7105/web)
    + October 2 to October 4, 2021

(`是也乎:`

![PyConTW](https://ipic.zoomquiet.top/2021-09-29-ScreenShot%202021-09-29%2011.17.51.jpg)

)


- [⋅ Melbourne Python Users Group, Australia](https://pycoders.com/link/7111/web)
    + October 4, 2021

- [⋅ Introduction to the Python Programming Language (In Persian)](https://pycoders.com/link/7094/web)
    + October 5, 2021

- [⋅ PyCon ZA 2021](https://pycoders.com/link/7091/web)
    + October 7 to October 9, 2021





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

- 首发: [Issue 492 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-492.html)
- 修订: [issue-492.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-492.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF492D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF492D4Q90XdDA7g):



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





