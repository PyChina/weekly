Title: 蠎周刊(PyCoder)573
Slug: issue-573
Date: 2023-04-19 11:42
Tags: Weekly,Python,pycoders,ZH


> Pandas 2.0 vs 1: 性能比较


原文: [PyCoder's Weekly - Issue #573](https://pycoders.com/issues/573)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230419 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230419 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [借助 AI 自我修复的“自我修复”程序](https://pycoders.com/link/10683/web)
    + BENJ EDWARDS

Wolverine is a Python tool that responds to script crashes by using ChatGPT to look for solutions. This brief article describes the process and links to a video demo. With the corresponding [Slashdot Discussion](https://pycoders.com/link/10677/web).

- [Pandas 2.0 vs Pandas 1: 性能比较](https://pycoders.com/link/10680/web)
    + SANTIAGO BASULTO 
    + • Shared by Santiago Basulto

Pandas 2.0 was recently released with the new pyarrow backend. In the article, we did a quick performance comparison between the new pyarrow backend in 2.0 with the standard in Pandas 1. The results were expected, a big speedup in terms of String processing and null value handling, but slower with numeric processing and aggregations.


- [用 RPA 和 RCC 自动化流程和分发工具](https://pycoders.com/link/10678/web)
    + REAL PYTHON 
    + PODCAST

Are you exploring automation of your repetitive business tasks with Python? How are you going to share your helpful tools with co-workers? This week on the show, Sampo Ahokas from Robocorp is here to discuss robotic process automation (RPA) and distribution of these robots.

- [PEP 695 “类型参数语法” 已接受](https://pycoders.com/link/10684/web)
    + PYTHON.ORG

(`是也乎:`


Python 向 Rust 融合不可阻挡...

)


- [欧盟提议的 CRA 对 Python 生态系统的影响](https://pycoders.com/link/10679/web)
    + PYTHON SOFTWARE FOUNDATION






-----------------------------------------
## 探讨/吐糟
> Discussions


- [Pip 23.1 发布: 对回溯的巨大改进](https://pycoders.com/link/10670/web)
    + REDDIT

(`是也乎:`


也就是说监管越来越深入了

)


- [您使用哪些鲜为人知的电脑配件?](https://pycoders.com/link/10676/web)
    + HACKER NEWS


(`是也乎:`


大家对 USB 和 无线耳机的怨念都不小

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 Python 操作 ZIP 文件](https://pycoders.com/link/10665/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to manipulate ZIP files using Python’s zipfile module from the standard library. Through hands-on examples, you’ll learn how to read, write, compress, and extract files from your ZIP files quickly.


(`是也乎:`

![Manipulating](https://ipic.zoomquiet.top/2023-04-19-zshot%202023-04-19%2010.13.39.jpg)

)

- [用 Shebang 执行 Python 脚本](https://pycoders.com/link/10656/web)
    + REAL PYTHON

In this tutorial, you’ll learn when and how to use the shebang line in your Python scripts to execute them from a Unix-like shell. Along the way, you’ll run custom scripts written in your domain-specific language interpreted by Python.


(`是也乎:`

![Shebang](https://ipic.zoomquiet.top/2023-04-19-zshot%202023-04-19%2010.28.12.jpg)

不仅仅是 Py ...

)


- [十大 Django 第三方包](https://pycoders.com/link/10666/web)
    + WILL VINCENT

Will covers a list of his favorite third-party packages for Django. Includes old favorites like Django REST Framework, and lesser known packages like django-filter and django-environ.


(`是也乎:`

其中 Wagtail 简直变成了一个大杂货铺, 专注的很...

)


- [PEP 711: 分发 Python 二进制文件的标准格式](https://pycoders.com/link/10657/web)
    + PYTHON.ORG

This PEP proposes a way of packaging pre-build interpreters “like wheels, but for python interpreters”. The intent is to re-use existing packaging standards as much as possible.

- [JavaScript、Python、SQL、R 和 Excel 中的描述性统计](https://pycoders.com/link/10669/web)
    + HORST & BUFFA

A series of comparisons on how to do common statistical methods in JavaScript, Python, SQL, R, and Excel. Includes mean, median, standard deviation, rank values, and more.

- [用 LangChain 的 BabyAGI 用户指南](https://pycoders.com/link/10672/web)
    + HARRISON CHASE

This notebook demonstrates how to implement BabyAGI by Yohei Nakajima. BabyAGI is an AI agent that can generate and pretend to execute tasks based on a given objective.

(`是也乎:`

ChatGPT 们一发布, LangChain 已经没了商业模型基础,
但是, 还有潜力可以尝试...

)


- [谁运行工程流程?](https://pycoders.com/link/10673/web)
    + WILL LARSON

Who should be in charge of engineering in your organization? The short answer: it depends. The long answer: it really depends. Read on for an even longer answer.

(`是也乎:`

除了最终交付的代码和运行时,
过程本身也是组织的知识资产, 可惜一直没有足够的认知,
实在是组成成员素质足够高, 通过自主调整就有了...
可还是有很大优化空间;

)


- [GitHub Pull Requests 语言流行度](https://pycoders.com/link/10654/web)
    + DANIEL LEMIRE

Daniel did an analysis on GitHub pull requests and ranked them by language. Together Python and JavaScript make up nearly 40% of all activity on GitHub.

- [进入管理层时你放弃了什么](https://pycoders.com/link/10658/web)
    + KARL HUGHES

“Moving into a management role may be a rewarding step in your career, but you should know about the things you’re leaving behind.”


(`是也乎:`

过于真实了, 作管理本质上等于重新开始, 将自己的技术积累,
变成团队的长期收益,
最困难的不是什么新学习, 
而是如何令上层相信你, 同时下属也相信你.

)


- [Unravelling global](https://pycoders.com/link/10664/web)
    + BRETT CANNON

Dive deep into global, how it works, its relationship with builtins and the namespace differences in Python.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [joblib: 用 Python 函数的轻量级流水线](https://pycoders.com/link/10660/web)
    + GITHUB.COM/JOBLIB

- [Auto-GPT: 让 GPT-4 完全自主的实验](https://pycoders.com/link/10659/web)
    + GITHUB.COM/TORANTULINO

(`是也乎:`

果然是 Python 构建的,
这可能是 star 增长最猛的项目了, 才几天就将突破 100K 了...

)


- [pyllms: 用于连接多个 LLM 的包装器](https://pycoders.com/link/10675/web)
    + GITHUB.COM/KAGISEARCH

- [aura: 大规模 Python 代码审计和静态分析](https://pycoders.com/link/10661/web)
    + GITHUB.COM/SOURCECODE-AI

- [PyDPainter: Python 中的像素艺术绘画程序](https://pycoders.com/link/10671/web)
    + GITHUB.COM/MRIALE


(`是也乎:`

![PyDPainter](https://ipic.zoomquiet.top/2023-04-19-zshot%202023-04-19%2009.43.29.jpg)


好象红白机时代的艺术创作哪...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [PyCon DE & PyData Berlin 2023](https://pycoders.com/link/10667/web)
    + April 17 to April 20, 2023

- [PyCon US 2023](https://pycoders.com/link/10668/web)
    + April 19 to April 28, 2023

- [NZPUG-Auckland: Python on Fire? Dash to the River](https://pycoders.com/link/10653/web)
    +April 19, 2023

- [Heidelberg Python Meetup](https://pycoders.com/link/10674/web)
    + April 19, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10662/web)
    + April 19, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/10655/web)
    + April 21 to April 22, 2023



-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 521](https://weekly.pychina.org/issue/issue-521.html)
- 2021: [蠎周刊 469](https://weekly.pychina.org/issue/issue-469.html)
    + [pythonista-weekly : Pyw 495](https://weekly.pychina.org/python-weekly/pyw-495.html)
- 2020: [蠎周刊 416](https://weekly.pychina.org/issue/issue-416.html)
    + [pythonista-weekly : Pyw 445](https://weekly.pychina.org/python-weekly/pyw-445.html)
- 2019: [蠎周刊 364](https://weekly.pychina.org/issue/issue-364.html)
- 2018: [蠎加载 171](https://weekly.pychina.org/importpython/importpython-171.html)
- 2017: [蠎加载 121](https://weekly.pychina.org/importpython/importpython-121.html)
- 2016: [蠎周刊 208: Tesla](https://weekly.pychina.org/issue/issue-208.html)
    + [蠎加载 69](https://weekly.pychina.org/importpython/importpython-69.html)
- 2015: [蠎周刊 162: Playoffs!](https://weekly.pychina.org/issue/issue-162.html)
    + [蠎加载 28](https://weekly.pychina.org/importpython/importpython-28.html)
- 2014: [Issue 111: Eggs](https://weekly.pychina.org/issue/issue-111.html))
- 2013: 空缺
- 2012: [Issue 10 ~ 反重力](https://weekly.pychina.org/issue/issue-10.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...
- [Chaos42 - YouTube](https://www.youtube.com/watch?v=fPQ6piLqMXE&list=PLToFpvpg6EgRo6naYOp-BX4So-DxOCne8&index=1)
    + VLog
    + 恢复各种嗯哼...


```
      _~~~-~_
  () /  + ?  \ ()
    '_   v   _'
    \ '--+--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```




-----------------------------------------
# PS:

- 首发: [Issue 573 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-573.html)
- 修订: [issue-573.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-573.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

## PPS:
> 不觉中蟒周刊快译已经到了第10+2个年头

开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
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

所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF573D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF573D4Q90XdDA7g):



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



