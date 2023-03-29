Title: 蠎周刊 PyCoder 569
Slug: issue-569
Date: 2023-03-22 11:42
Tags: Weekly,Python,pycoders,ZH


> 如何评估包的质量Orz...


原文: [PyCoder's Weekly - Issue #569](https://pycoders.com/issues/569)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230322 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230322 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [如何评估 Python 包的质量](https://pycoders.com/link/10530/web)
    + REAL PYTHON

Just like you shouldn’t download any file from the Internet, you shouldn’t blindly install third-party Python packages without evaluating them first. This tutorial will give you the toolset to evaluate the quality of external Python packages before you implement them into your Python projects.


(`是也乎:`


![Evaluate](https://ipic.zoomquiet.top/2023-03-22-zshot%202023-03-22%2009.43.18.jpg)


认真是一种气味儿, 很容易嗅到 ;-)

[Libraries.io - The Open Source Discovery Service](https://libraries.io/)

我们可能没办法构建出新工具, 但是, 我们可以专业的评定工具们.

)


- [PyTorch 2.0 中新库更新](https://pycoders.com/link/10524/web)
    + PYTORCH.ORG

Learn what’s changed in the newly released PyTorch 2.0 library. Includes new data collectors, augmentation operators, vision features, and loads more.


- [惰性递归，带生成器](https://pycoders.com/link/10504/web)
    + TUSHAR SADHWANI

This article introduces your to mixing generators with recursion to improve memory usage. Includes a short snippet on using yield and yield from.


(`是也乎:`

嗯哼? 就象 麦当劳奶昔配KFC辣鸡堡?

)

-----------------------------------------
## 探讨/吐糟
> Discussions


- [Codon 实现了数量级的加速](https://pycoders.com/link/10511/web)
    + HACKER NEWS

(`是也乎:`

[exaloop/codon: A high-performance, zero-overhead, extensible Python compiler using LLVM](https://github.com/exaloop/codon "exaloop/codon: A high-performance, zero-overhead, extensible Python compiler using LLVM")

也就是说, 现在 Python 调试好后, 可以直接编译为目标机器的执行应用了?

这真的是 PyPy/Cython 之后, 又一种思路,
JVM 学派? 开发者你们怎么任性都可以,
将编译器搞扎实了,
自动优化统一编译执行, 一样可以提高效能?

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 3.12: 性能和效率的游戏规则改变者](https://pycoders.com/link/10516/web)
    + AI TUTOR

Work on Python 3.12 is well under way and much of it focuses on performance improvements. This article gives you a tour of the changes to come, including improved parallelism, better memory management, even more improved error reporting, and more.

(`是也乎:`

推荐作者名很透题了..

)


- [用 Sphinx 记录 Python 项目并阅读文档](https://pycoders.com/link/10519/web)
    + REAL PYTHON 
    + COURSE

In this video series, you’ll create project documentation from scratch using Sphinx, the de facto standard for Python. You’ll also hook your code repository up to Read The Docs to automatically build and publish your code documentation.


(`是也乎:`

是的, 这个相比 gh-pages 要复杂一点儿,也就一点儿...

![rST](https://ipic.zoomquiet.top/2023-03-22-zshot%202023-03-22%2009.41.03.jpg)

不过, 搞通后, 的确比 Markdown 要自在很多.

)



- [代码审查: 什么和什么不能自动化？?](https://pycoders.com/link/10520/web)
    + REKA HORVATH 
    + • Shared by Reka

This post tries to come up with some guidelines: Which parts of the review can be done well by our current tools? Which parts benefit from human intuition? We’re looking in details at reviewing tests, docs, code quality, and names.

(`是也乎:`

现实已经证明, 嘦样本足够多, 
人类的直觉一定可以完美复制,
不过, 这时直觉应该就升级为灵感了...

)


- [构建布隆/Bloom 过滤器](https://pycoders.com/link/10532/web)
    + KIRILL B.

Bloom filters are a data structure used to test whether an element is a member of a set. They’re commonly used in data science and are often part of interview questions. Learn how to build one and where you might use them.

(`是也乎:`

![luminousmen](https://ipic.zoomquiet.top/2023-03-22-zshot%202023-03-22%2009.35.40.jpg)

这又是另外一种风格,
作者是大数据领域专家, 那么对自己的 blog 当然也得数据分析上...

)


- [虚拟环境如何工作的?](https://pycoders.com/link/10523/web)
    + BRETT CANNON

This article attempts to demystify virtual environments, why they exist and how they work. It even delves into why Brett is heading down this alley: running into challenges with cross platform tools and microenv.


(`是也乎:`

就象 Docker 如何工作一样...

)




- [Django: 如何分析和改进启动时间](https://pycoders.com/link/10527/web)
    + ADAM JOHNSON

“Your Django project’s startup time impacts how smooth it is to work with. Django has to restart your project every time you run a management command and when runserver reloads.” Learn how to make this faster.


(`是也乎:`

![JOHNSON](https://ipic.zoomquiet.top/2023-03-22-zshot%202023-03-22%2009.27.55.jpg)

出版级 blog
-> [Colophon](https://adamj.eu/colophon/)

是的, 这是作者专门设计的配色和排版;


PS:
这时, 才发觉 Erlang 学派, 永远不停机热部署是多么的有远见...

)


- [Python 中的数据验证: Pandera 和远大前程](https://pycoders.com/link/10502/web)
    + LIAM MOONEY

Data validation is a vital step in any data-oriented workstream. This post investigates and compares two popular Python data validation packages: Pandera and Great Expectations

- [教程: 构建基于终端的 TODO 应用程序](https://pycoders.com/link/10531/web)
    + MATHSPP.COM 
    + • Shared by Rodrigo Girão Serrão

Learn how to build a simple TODO app in Python using the Textual library. The app runs inside the terminal and can be controlled from the comfort of your keyboard.


(`是也乎:`


![Textual](https://ipic.zoomquiet.top/2023-03-22-zshot%202023-03-22%2009.25.54.jpg)


淦...这效果完全不逊于 GUI 了


)


- [将 Python 3.11 与 AWS Lambda 结合使用](https://pycoders.com/link/10510/web)
    + ISTVAN SZUKACS

AWS Lambda currently limits Python to version 3.9. This article shows you how to get around that and use a more recent version of your favorite language.


(`是也乎:`

用 Docker 绕, 这很容易识别出来禁止的,
还是用 Rust 包装一下, 变成单一执行文件,
肯定就难了..

)


- [Python 列表构造函数: 如何使用以及如何不使用](https://pycoders.com/link/10512/web)
    + PYTHONMORSELS.COM 
    + • Shared by Trey Hunner

When should you use the built-in list(…) function in Python? And when shouldn’t you? The list constructor is both underused and overused in Python.

- [请给更多电池](https://pycoders.com/link/10513/web)
    + CARLTON GIBSON

This brief opinion piece from Carlton Gibson states why he thinks we need more functionality in the Python standard library rather than less.

(`是也乎:`

一边儿核心团队吼着要批量清除已经作废的内建模块,
另外用户一直叫着应该更多内置电池,
感觉, 内建模块就象政府职称, 评上了保一生太平?

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [evals: 评估和基准化 OpenAI 模型](https://pycoders.com/link/10506/web)
    + GITHUB.COM/OPENAI

(`是也乎:`

AI 带路党也是认真的...

)


- [为 Django REST Framework 生成测试](https://pycoders.com/link/10507/web)
    + GITHUB.COM/SAADMK11 
    + • Shared by Maksudul Haque


(`是也乎:`

看起来象 Puffy 测试生成器?

)


- [pybroker: 用 ML 在 Python 中进行算法交易](https://pycoders.com/link/10529/web)
    + GITHUB.COM/EDTECHRE

- [guardrails: 大型语言模型验证器](https://pycoders.com/link/10525/web)
    + GITHUB.COM/SHREYAR

(`是也乎:`


GPT 之后 LLM 又变成一大热点

)


- [duckargs: argparse 样板的代码生成器](https://pycoders.com/link/10521/web)
    + GITHUB.COM/ERIKNYQUIST


(`是也乎:`

叕一个 CLI 指令参数声明解析器

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [PyKla Monthly Meetup](https://pycoders.com/link/10526/web)
    + March 22, 2023

- [Python Meeting Düsseldorf](https://pycoders.com/link/10515/web)
    + March 22, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10528/web)
    + March 22, 2023

- [Heidelberg Python Meetup](https://pycoders.com/link/10503/web)
    + March 22, 2023

- [PyDelhi User Group Meetup](https://pycoders.com/link/10508/web)
    + March 25, 2023

- [PythOnRio Meetup](https://pycoders.com/link/10522/web)
    + March 25, 2023




-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 517](https://weekly.pychina.org/issue/issue-517.html)
- 2021: [蠎周刊 465](https://weekly.pychina.org/issue/issue-465.html)
    + [pythonista-weekly : Pyw 491](https://weekly.pychina.org/python-weekly/pyw-491.html)
- 2020: [蠎周刊 413](https://weekly.pychina.org/issue/issue-413.html)
- 2019: [蠎周刊 360](https://weekly.pychina.org/issue/issue-360.html)
- 2018: [蠎加载 167](https://weekly.pychina.org/importpython/importpython-167.html)
- 2017: [蠎加载 116](https://weekly.pychina.org/importpython/importpython-116.html)
- 2016: [蠎加载 66](https://weekly.pychina.org/importpython/importpython-66.html)
- 2015: [蠎周刊 158: Madness](https://weekly.pychina.org/issue/issue-158.html)
- 2014: [蠎周刊 107: 带来的感觉](https://weekly.pychina.org/issue/issue-107.html)
- 2013: 空缺
- 2012: [蠎周刊 6 ~ 春分](https://weekly.pychina.org/issue/issue-6.html)


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
- [42.zoomquiet.top](https://42.zoomquiet.top/)
    + 古早:周刊式分享
    + ...类似湾区日报




```
          _~^--~_
      \/ /  ☉ +  \ \/
        '_   ⏡   _'
        / '--~--' )

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 569 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-569.html)
- 修订: [issue-569.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-569.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF569D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF569D4Q90XdDA7g):



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



