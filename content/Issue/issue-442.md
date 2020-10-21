Title: Issue 442
Slug: issue-442
Date: 2020-10-14 11:42
Tags: Weekly,Python,pycoders,ZH


> PyOxidizer 0.8 发布


原文: [PyCoder's Weekly - Issue #442](https://pycoders.com/issues/442)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201014 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201014 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [Python 3.9 新特性巡礼](https://pycoders.com/link/5027/web)
    + REAL PYTHON 
    + podcast

Python 3.9 has arrived! Real Python contributors Geir Arne Hjelle and Christopher Trudeau are walking you through changes and new features in Python 3.9, such as time zone improvements, merging dictionaries, the new parser, type hints, and more.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.50.58.jpg)

75 分钟, 大家高兴的谈及各种自己平时用不上的特性...


)

- [用 PostgreSQL 和 Python 将 USENET 磁带存档转换为网站](https://pycoders.com/link/5007/web)
    + JOZEF JAROSCIAK

“There were approximately 2.1 million posts in these archives created between Feb 1981 and June of 1991. This article describes the journey of converting those tapes into fully searchable PostgreSQL database and later also into the usenetarchives.com website.”

(`是也乎:`

可以偷看爷爷们当年的嗯哼了...

)


- [2020年 Python 程序猿调查](https://pycoders.com/link/5038/web)
    + PSF & JETBRAINS

“This is the fourth iteration of the official Python Developers Survey. With this survey, we aim to understand how the world of Python development looks today and how it compares to last year. In 2019, over 24,000 Python developers from 150 countries responded sharing their opinions and helping us get an accurate picture of the Python community.”

(`是也乎:`

官方联合 JETBRAINS 的调查, 
当然是有一定倾向的...

)


- [pip 20.2 对依赖项解析器的更改](https://pycoders.com/link/5012/web)
    + PYPA.IO

Changes in the behavior of pip install will reduce inconsistency and make it stricter. Pip will no longer install a combination of packages that is mutually inconsistent and if you ask pip to install two packages with incompatible requirements, it will refuse (rather than installing a broken combination, like it did in previous versions). These changes will become the default in pip 20.3, due to be released in October.



- [pip 用户反馈调查分析](https://pycoders.com/link/5031/web)
    + PIP TEAM

The pip team are considering removing pip search, or changing the way that it works. To help inform our decision, please tell us about your experience using pip search.

- [PyOxidizer 0.8 发布](https://pycoders.com/link/5025/web)
    + GREGORY SZORC

(`是也乎:`

好东西哪, 去年 PyCon 时发布的原型,
受到关注,
然后就炸裂了...

也就是用 Rust 制造了一个 mini Python 运行时,
可以高效随应用一起发行,
解决以往 Python 应用发行时, 必须包含复杂的 Python 安装过程.

)


- [Python 可视化发布周期](https://pycoders.com/link/5041/web)
    + DUSTIN INGRAM


(`是也乎:`

![Release](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.45.37.jpg)

也就是说, Python 现在的版本发布工程终于有 KPI 了?

)





## 探讨/吐糟
> Discussions



- [用 Python 作个工具/现在儿子恨屎了](https://pycoders.com/link/5014/web)
    + REDDIT

“I use it to generate endless random basic math questions for him to practice…”

(`是也乎:`

![math](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.42.58.jpg)

[januschung/math\-worksheet\-generator: Create basic addition, subtraction and multiplication practice questions with the answer sheet](https://github.com/januschung/math-worksheet-generator)

嗯哼, 王珢当年入坑是自己构造了解题器,
可以理解并理代数/几何题, 
这位老爹则是联合学校制造无限出题机...

)

## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [用 Beautiful Soup 和 Python 爬取网页](https://pycoders.com/link/5017/web)
    + REAL PYTHON 
    + video

In this course, you’ll walk through the main steps of the web scraping process. You’ll learn how to write a script that uses Python’s requests library to scrape data from a website. You’ll also use Beautiful Soup to extract the specific pieces of information that you’re interested in.

(`是也乎:`

美汤当年因为糟糕的性能没人用,
没想到现在变成标准了.
![Beautiful](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.34.47.jpg)


)


- [了解和防止 Web 应用程序中的 DoS](https://pycoders.com/link/5013/web)
    + JACOB KAPLAN-MOSS

This article provides a framework for engineering and application security teams to think about denial-of-service (DoS) risk, breaks down DoS vulnerabilities into high-, medium-, and low-risk classes, and has recommendations for mitigations at each layer.


- [查找和修复 Python 代码错误: 用 IDLE 进行调试](https://pycoders.com/link/5009/web)
    + REAL PYTHON

Learn how to identify and fix logic errors, or bugs, in your Python code. You’ll use the built-in debugging tools in Python’s Integrated Development and Learning Environment to practice locating and resolving bugs in an example function.

(`是也乎:`

![IDLE](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.33.19.jpg)

不是, 等等, 为什么是 IDLE?
Tk 的伟大制品,
早已不值得使用了,

怎么还在使用?

嗯哼内建, 又不支持中文, 所以是非常好的调试界面.

)


- [如何尝试减少 Pylint 内存使用](https://pycoders.com/link/5039/web)
    + @RTPG_

“[Pylint] was consuming a lot of memory, causing OOM failures if we tried to run it too much in parallel. I decided to roll up my sleeves and figure out: What exactly was consuming so much memory? Is there a way to avoid doing this?”



- [在 Python 中用 ggplot: 用 plotnine 可视化数据](https://pycoders.com/link/5033/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use ggplot in Python to build data visualizations with plotnine. You’ll discover what a grammar of graphics is and how it can help you create plots in a very concise and consistent way.

(`是也乎:`

![ggplot](http://ydlj.zoomquiet.top/ipic/2020-10-14-ScreenShot%202020-10-14%2010.28.30.jpg)

ggplot 是比 matplotlib 更加古老而优秀的可视化工具,
现在 Python 也有稳定支持模块了.

)


- [有序词典惊吓](https://pycoders.com/link/5032/web)
    + NED BATCHELDER

“Since Python 3.6, regular dictionaries retain their insertion order. […] Here are two surprising things about these ordered dicts: You can’t get the first item and OrderedDict is a little different.”

(`是也乎:`

数组天然有序,
字典丰富自由就是难以排序,
所以....

)


- [案例研究: 用 Python 处理历史天气模式数据](https://pycoders.com/link/5018/web)
    + CHRIS MOFFITT

This article is a case study showing how to use Python to download and process historical temperature data in order to do analysis on the relationship between air temperature and power consumption.




- [以 Python 实现 Xkcd 的 “StackSort” ](https://pycoders.com/link/5015/web)
    + DAVID BUCKLEY

“StackSort connects to StackOverflow, searches for ‘sort a list’, and downloads and runs code snippets until the list is sorted.” This is obviously not safe for production use ;-)

(`是也乎:`

为什么大家在大力研究一位漫画家提出的算法?

有趣才是第一生产力哪.

![Ineffective](http://ydlj.zoomquiet.top/ipic/2020-10-14-ineffective_sorts.png)

即便人家标题是:`无效排序`

)


- [将 Launchpad 移植到 Python 3: 进度报告](https://pycoders.com/link/5035/web)
    + COLIN WATSON

“Launchpad still requires Python 2, which in 2020 is a bit of a problem. Unlike a lot of the rest of 2020, though, there’s good reason to be optimistic about progress.”

(`是也乎:`

作为 Ubuntu 等重量开源项目托管平台,
Launchpad 这么长时间都没作好迁移, 
已经证明...

)

- [在 Go 中嵌入 Python](https://pycoders.com/link/5008/web)
    + CHRISTIAN KORNECK 
    + • Shared by Christian Korneck

A practical example for executing Python code in a Golang program and exchanging data between Go and Python. Shows how to use the Python C API in Go.


(`是也乎:`

之前有人将 go 嵌入在 Python 代码中运行,

)

- [PySDR: Python 的 SDR 和 DSP 指南](https://pycoders.com/link/5036/web)
    + DR. MARC LICHTMAN

A detailed guide / online textbook to Software-Defined Radio (SDR) and Digital Signal Processing (DSP) with Python.

- [Python 哈希表: 了解字典](https://pycoders.com/link/5028/web)
    + DAVIDE MASTROMATTEO 
    + • Shared by Davide Mastromatteo


An overview of Python hash tables and their main implementation: the dict object.

(`是也乎:`

理解构造机制并可以帮助大家正确使用嘛?

)


- [Python PEPs Graph 图可视化](https://pycoders.com/link/5034/web)
    + VINAYAK MEHTA 
    + • Shared by Vinayak Mehta

Click on a PEP to see other PEPs it mentions.


- [是什么构成了健康的 Python 代码库?](https://pycoders.com/link/5026/web)
    + VLAD TEMIAN

(`是也乎:`

健康基础?
好读易维护,
说穿了, 代码是写给人看的.

)

- [PySide vs PyQt: 了解差异](https://pycoders.com/link/5021/web)
    + RAAHIM SIDDIQI 
    + • Shared by Raahim Siddiqi


(`是也乎:`

其实, 没什么不同, 都是相同技术桟, 
GUI 工具, 现在真的没什么指望了...

)


   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [aioupnp: 使用 asyncio 与 UPnP 网关进行交互](https://pycoders.com/link/5005/web)
    + GITHUB.COM/LBRYIO

(`是也乎:`

好久没见 asyncio 的消息了...


)

- [math-worksheet-generator: 自动构造基本加法/减法和乘法练习题](https://pycoders.com/link/5037/web)
    + GITHUB.COM/JANUSCHUNG



- [argparse Builder: 用基于表单的便捷 GUI 创建复杂 argparse 接口](https://pycoders.com/link/5019/web)
    + KITAKITSUNE.ORG

(`是也乎:`

等等, python 2.7 only?
CLI 参数过于复杂又不是什么好事儿,
有很多 CLI 工具框架, 提供了更加 Pythonic 的参数声明/解析形式,
为什么要用 argparse?

)


- [Konfik: 熟悉的配置分析器](https://pycoders.com/link/5011/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

- [python-doc: CLI 工具可在浏览器中打开 Python 文档](https://pycoders.com/link/5024/web)
    + GITHUB.COM/VINAYAK-MEHTA 
    + • Shared by Vinayak Mehta

(`是也乎:`

这是书签不会用的程序猿的朋友...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

None

## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

蟒营®编程思维提高班 Python版/13期已发布

时间规划:

+ 报名截止 **2020.10.19**
+ 正式开课 **2020.10.25**
+ 课程结束 **2020.12.06**


> 10.1 特价: 2642元/人

1. 老学员或是其它有效推荐, 再惠 **500元**
1. 在校生, 再优惠 **1000元**
    + 出示学生证即可
1. **复读** 5折
1. 组团:
    + 4人及以上(建议直接联系 蟒营®开`绿色`通道.)

(注意: 以上优惠政策不可叠加;-)


**报名流程: 微信扫码报名→付学费→入微信群**

![reg13py](http://101.zoomquiet.top/res/13py/reg-zip.jpg)

详情 => [蟒营®编程思维提高班 Python版/ 第13期](https://py.101.camp/)


# PS:
- 首发: [Issue 442 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-442.html)
- 修订: [issue-442.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-442.md)


-------------

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

as 创始组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------
>> NN 4166


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/442)






