Title: Issue 477
Slug: issue-477
Date: 2021-06-16 11:42
Tags: Weekly,Python,pycoders,ZH


> Excel+Py 就是数据科学的未来?


原文: [PyCoder's Weekly - Issue #477](https://pycoders.com/issues/477)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210616 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210616 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Excel/Python 和数据科学的未来](https://pycoders.com/link/6545/web)
    + MATT ASAY

What’s the most widely used tool in data science? Is it pandas or NumPy? Is it the Python language itself? Not really. It’s Excel. You might argue that data scientists aren’t using Excel as their primary tool, and you might be right. But Excel enables non-technical users, like small business owners, to gain insights into their data. In this article, Anaconda CEO Peter Wang discusses his goal of making Python and PyData the “conceptual successor” to Excel.

(`是也乎:`


对的, 无论 Jupyter 怎么折腾,
如果 Excel 嵌入 Python,
那么瞬间, 没 notebook 什么事儿了...

)



- [数据分析用实 SQL](https://pycoders.com/link/6552/web)
    + HAKI BENITA

If you need to do some data analysis, what tool do you reach for first? Is it pandas? While pandas is great, it comes with some costs that you might not be aware of, including large memory overhead that can quickly get in the way of your projects. Using databases with SQL can alleviate memory issues. In this tutorial, you’ll learn how to do common data analysis tasks in SQL, which opens the door to mixing SQL and pandas to create lightweight programs that are also fast!


(`是也乎:`

SQL 永远的语言

)


- [Python 实践题: 解析CSV文件](https://pycoders.com/link/6548/web)
    + REAL PYTHON

In this tutorial, you’ll prepare for future interviews by working through a set of Python practice problems that involve CSV files. You’ll work through the problems yourself and then compare your results with solutions developed by the Real Python team.

(`是也乎:`


常年手工解析 .csv 的俺...

)



- [Jazzband 加入 PSF 财政赞助计划](https://pycoders.com/link/6544/web)
    + JAZZBAND.CO

- [微软为加速 Python 专门开展招聘](https://pycoders.com/link/6542/web)
    + TWITTER.COM/GVANROSSUM

(`是也乎:`

嗯哼?
这个热点蹭得专业哪...

)


- [Mypy 0.900 发布](https://pycoders.com/link/6550/web)
    + MYPY-LANG.BLOGSPOT.COM

(`是也乎:`

**打死也不发布 1.0 党**

)





-----------------------------------------
## 探讨/吐糟
> Discussions



- [为什么注释不能出现在换行符后?](https://pycoders.com/link/6538/web)
    + STACK OVERFLOW

Chaining together many object methods can create long tines that break the PEP 8 79-character line length recommendation. You can use \ to break the chain of methods onto individual lines, but if you want to leave comments at the end of some of the lines, you’re out of luck. There’s another pattern, though, that solves this.

- [在内部分发 Python 包的一些常见方法是什么?](https://pycoders.com/link/6543/web)
    + TWITTER.COM/BRIANOKKEN

Brian Okken, co-host of the Python Bytes podcast, asks Twitter users about internal package distribution, and the Twitterverse responds.

(`是也乎:`

S3->GCP->Devpi

还是用 Devpi 发布内源 PyPI 最简洁了.

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 PyMC3 用对乐高积木价格进行贝叶斯分析](https://pycoders.com/link/6553/web)
    + AUSTIN ROCHFORD

Follow along with this in-depth analysis of LEGO prices to see Bayesian analysis in action. Along the way, you’ll how pooled and unpooled linear models can be used to determine if a LEGO set is fairly priced. The article is quite technical, so experience with Bayesian statistics is recommended.

(`是也乎:`

PyMC 原先只是作为课堂讲义,
没想到慢慢的, 变成了 Bayes 标准库了...

)


- [如何在公共实验室的 Raspberry Pi 400 上教授 Python](https://pycoders.com/link/6546/web)
    + DON WATKINS

Community-based programming courses are a great way to introduce folks to computer programming that otherwise may not have the means to do so. One of the barriers to learning to code is cost. You need a computer to program on, after all. But with the advent of tiny computers like the Raspberry Pi, computers aimed at education are more affordable than ever.

(`是也乎:`


![RPi 400](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2011.02.22.jpg)

用 RPi 替代主机配合显示屏+mouse+键盘,
形成只能学习编程的环境,
这下学员没办法安装游戏来玩了?


)


- [用 Pandas 在 Python 中制作成绩簿](https://pycoders.com/link/6547/web)
    + REAL PYTHON 
    + course

With this Python project, you’ll build a script to calculate grades for a class using pandas. The script will quickly and accurately calculate grades from a variety of data sources. You’ll see examples of loading, merging, and saving data with pandas, as well as plotting some summary statistics.

(`是也乎:`

![Gradebook](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2011.00.14.jpg)

)


- [用 Python 检测森林砍伐并在 Django 和 Vue 中使用 GraphQL](https://pycoders.com/link/6554/web)
    + REAL PYTHON 
    + podcast

Are you looking for an in-depth data science project to practice your skills on? Perhaps you would like to add new tools to your Python web development projects instead? This week on the show, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.


(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.59.18.jpg)

Vue 真自成一派了.

)

- [Python Sentinel 对象/类型提示和 PEP 661](https://pycoders.com/link/6558/web)
    + DEATH AND GRAVITY 
    + • Shared by Adrian

PEP 661 proposes adding a utility for defining sentinel values in the standard library. In this article, you’ll get a summary of PEP 661, learn what sentinel objects are with real-world examples, and see how to use them with type hints.

- [Python 之 filter() : 从可迭代对象中提取值](https://pycoders.com/link/6537/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how Python’s filter() works and how to use it effectively in your programs. You’ll also learn how to use list comprehension and generator expressions to replace filter() and make your code more Pythonic.

(`是也乎:`

![filter](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.58.02.jpg)

还是得配合 lambda 才能有麽幻感觉


)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [novelWriter: 跨平台编辑器/用 Python 和 Qt 构建的专为编写小说而设计](https://pycoders.com/link/6534/web)
    + GITHUB.COM/VKBO

(`是也乎:`


真小说生成器

![novelWriter](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.56.21.jpg)
)

- [speechbrain: 基于 PyTorch 的语音工具包](https://pycoders.com/link/6533/web)
    + GITHUB.COM/SPEECHBRAIN



- [pyWhat: 用 Python 识别任何东西](https://pycoders.com/link/6551/web)
    + GITHUB.COM/BEE-SAN


(`是也乎:`

![pyWhat](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.51.46.jpg)

宇宙版反向 UUID ?


)


- [textual: 具有丰富渲染器的文本用户界面](https://pycoders.com/link/6539/web)
    + GITHUB.COM/WILLMCGUGAN

(`是也乎:`

![textual](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.48.30.jpg)

TUI (Text User Interface) 比 GUI 越来越嗯哼了...

![rich](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.50.26.jpg)

基于 Rich/富豪 框架

)

- [pyrgg: Python 随机图生成器](https://pycoders.com/link/6532/web)
    + GITHUB.COM/SEPANDHAGHIGHI

(`是也乎:`

![Random](http://ydlj.zoomquiet.top/ipic/2021-06-16-ScreenShot%202021-06-16%2010.37.10.jpg)

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6541/web)
    + June 16, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ PyFest](https://pycoders.com/link/6555/web)
    + June 16 – 19, 2021

- [⋅ DigitalOcean deploy: Power Your Business](https://pycoders.com/link/6529/web)
    + June 29, 2021

- [⋅ PyCon Namibia 2021](https://pycoders.com/link/6497/web)
    + June 18 to June 20, 2021
    + 非洲


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

- 首发: [Issue 477 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-477.html)
- 修订: [issue-477.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-477.md)


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





