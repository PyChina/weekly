Title: Issue 470
Slug: issue-470
Date: 2021-04-28 11:42
Tags: Weekly,Python,pycoders,ZH


> 开源的社会契约


原文: [PyCoder's Weekly - Issue #470](https://pycoders.com/issues/470)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210428 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210428 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [开源的社会契约](https://pycoders.com/link/6173/web)
    + BRETT CANNON 
    + opinion

What is open source software, and what is the relationship between a maintainer and a user? Python core developer and steering council member Brett Cannon tackles some questions about the open source, raises concerns about bad actors, and shares some thoughts about handling abuse.

(`是也乎:`

大学研究僧将目光投向开源社区后...

)


- [Python’s map() 函式: 转换可迭代对象](https://pycoders.com/link/6196/web)
    + REAL PYTHON 
    + course

Learn how Python’s map() works and how to use it effectively in your programs in this video course. You’ll also learn how to use list comprehension and generator expressions to replace map() in a Pythonic and efficient way.


(`是也乎:`


![map](http://ydlj.zoomquiet.top/ipic/2021-04-28-ScreenShot%202021-04-28%2008.42.50.jpg)


)

- [教大家用 Hedy 编码](https://pycoders.com/link/6193/web)
    + JOSHUA ALLEN HOLM

Hedy is a new programming language designed specifically for teaching people to code. What makes Hedy special is its notion of “levels” that start with the most basics concepts and gradually introduce new features that eventually become more Python-like. Hedy is not designed to compete with languages designed for real-world projects. It is 100% focused on teaching.


(`是也乎:`

> print Hello World

这很 Pythonic.

)


- [Pyodide 分解 + 0.17释放](https://pycoders.com/link/6200/web)
    + MOZILLA.ORG

The Pyodide project consists of CPython 3.8 compiled to WebAssembly so that Python can run in the browser. Originally developed by Mozilla, Pyodide is now a fully independent project. The latest version 0.17 brings asyncio support and error handling, as well as other improvements.

(`是也乎:`

嗯哼 **WSAM.py** 来了.


    function jsfunc(array) {
      array.push(2);
      return array.length;
    }

    pyodide.runPython(`
    from js import jsfunc
    from pyodide import to_js

    def pyfunc():
      mylist = [1,2,3]
      jslist = to_js(mylist)
      return jsfunc(jslist) # returns 4
    `)


呃...真的要这么来写 Py ?

)



- [PEP 563 基于字符串的默认类型注释 延迟到 Python 3.11](https://pycoders.com/link/6192/web)
    + PYTHON.ORG

The Python steering council has decided to roll back changes that made PEP 563’s string-based type annotations the default in Python 3.10. The PEP’s default change is now slated to roll out in Python 3.11.

(`是也乎:`

string 样数据折腾了30年了, 还没折腾明白,
还是 Plan9 强,
干脆将整个儿世界文本化了.

)


- [EuroPython 2021 建议征集](https://pycoders.com/link/6202/web)
    + EUROPYTHON.EU

Proposals for talks will be accepted until May 9. If you’re a new speaker, be sure to check out the Speaker Mentorship Program.




-----------------------------------------
## 探讨/吐糟
> Discussions



- [你在用 Python 自动执行哪些例行任务?](https://pycoders.com/link/6182/web)
    + REDDIT

Do you use Python to automate anything in your day-to-day life? This Reddit discussion thread is full of ideas for automation and has tons of links to GitHub repos where you can explore ideas get some inspiration.

(`是也乎:`

各种网站的编译发布...
之前 fabric, 现在 invoke,
以后可能 Ansible...

> 网友们就奔放了:

Telegram bot to send me daily analysis of S&P500 index. Lots of other goodies in this repo https://github.com/namuan/trading-utils

Script to download complete thread from PHP BB https://github.com/namuan/bin-utils/blob/master/phpbb_thread.py

Bot for downloading videos from Reddit/Twitter. Anything supported with YouTube-dl https://github.com/namuan/tele-tube-rider

Bot to convert videos to mp3 https://github.com/namuan/tele-vdo-rider

Alfred plug-in for common tasks https://github.com/namuan/alfred-genie

News aggregator to email myself a compiled list from different sources https://github.com/namuan/news-rider

...

[namuan/alfred\-genie: Genie for Alfred](https://github.com/namuan/alfred-genie)
以及这种将 Alfred 当成万能召唤入口的各种嗯嗯嗯
)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 QtQuick 的动画和转换构建 Python 模拟时钟](https://pycoders.com/link/6195/web)
    + MARTIN FITZPATRICK

Qt is a powerful cross-platform GUI toolkit and you can develop with it in Python using PyQt. In this article, you’ll learn how to work with animations and transformations by drawing a live analog clock face. The tutorial builds upon concepts explained in the 
[companion article](https://pycoders.com/link/6198/web) about creating applications with QtQuick and the Qt Modeling Language.

(`是也乎:`

一步一步完成透明底图的传统指针桌面时钟...
当然 macOS 环境.

)


- [Python 游戏开发的下一步](https://pycoders.com/link/6190/web)
    + REAL PYTHON 
    + podcast

Are you interested in creating video games but feel limited in what you can accomplish within Python? Is there a platform where you can take advantage of your Python skills and provide the benefits of a dedicated game engine? Real Python author Paweł Fertyk discusses all of this and his game studio Miskatonic Studio in this episode of the Real Python Podcast.


(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-04-28-ScreenShot%202021-04-28%2008.34.27.jpg)


> ...GOAT: Godot Open Adventure Template

)



- [PyPy 用 Graphviz 的一些方式](https://pycoders.com/link/6201/web)
    + CARL FRIEDRICH BOLZ-TEREICK

Graphviz is an open-source graph — or, network — visualization tool. You can use Graphviz to visualize the structure of your applications and programs, and it’s a great way to better understand how code works. In this article, you’ll learn how PyPy uses Graphviz to visualize everything from control flow to parse trees. While the article doesn’t include any source code, there are a number of illustrations and links to whet your appetite and point you to more information.


(`是也乎:`

强强联合

)


- [For-Else: Python 中一个奇怪但有用的功能](https://pycoders.com/link/6180/web)
    + YANG ZHOU

Python for loops have an unusual feature: they support an else block that only executes if there is no break in the loop. The pattern isn’t used very often with the argument against it being that it is a bit weird and potentially difficult to understand. But there may be times when for/else makes sense. This article presents three situations where for/else is useful and argues that, in these situations, the pattern makes the code more readable.

- [Python Basics: 现在提供平装本!](https://pycoders.com/link/6181/web)
    + REAL PYTHON

After years of writing, reviewing, and testing, we’re delighted to announce that Python Basics: A Practical Introduction to Python 3 is now available in paperback! In this article, you’ll see how you can level up your Python with Python Basics and how other Pythonistas have already been doing it.

(`是也乎:`

![Basics](http://ydlj.zoomquiet.top/ipic/2021-04-28-ScreenShot%202021-04-28%2008.31.28.jpg)

真蟒用一年打造出来的新书...

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [natsort: 在 Python 中简单而灵活的自然排序](https://pycoders.com/link/6175/web)
    + GITHUB.COM/SETHMMORTON

- [PythonPlantsVsZombies: 用 Pygame 构建的植物大战僵尸游戏](https://pycoders.com/link/6197/web)
    + GITHUB.COM/MARBLEXU

(`是也乎:`

Pygame ~ 良心 GUI 框架

)

- [hedy: Hedy 是种渐进式编程语言/ 语法元素逐级增加](https://pycoders.com/link/6186/web)
    + GITHUB.COM/FELIENNE

(`是也乎:`

HADY,HIDY,HEDE,...

反正蹭变身博士梗的项目命名一直有.

)


- [secure: 适用于 Python Web 框架的安全标头](https://pycoders.com/link/6178/web)
    + GITHUB.COM/TYPEERROR

- [wasp-os:基于MicroPython的智能手表开发环境](https://pycoders.com/link/6188/web)
    + GITHUB.COM/DANIEL-THOMPSON

(`是也乎:`

嵌入式系统,
将手表也开辟为一个越来越宏大的战场了...
等视网膜投影技术成熟了,
这也是主战场.

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6189/web)
    + April 28, 2020

(`是也乎:`

即便是线上的, 一样收费.

)


- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
    +  May 2 – 3, 2021

(`是也乎:`

以色列, 全球创新热点地区...

)



- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021


- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



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

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:
- 首发: [Issue 470 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-470.html)
- 修订: [issue-470.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-470.md)


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
>> NN 4341


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/470)






