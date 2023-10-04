Title: 蠎周刊(PyCoder)597
Slug: issue-597
Date: 2023-10-04 21:42
Tags: Weekly,Python,pycoders,ZH


> 3.12: 值得尝试的酷炫新功能


原文: [PyCoder's Weekly - Issue #597](https://pycoders.com/issues/597)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 231004 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 231004 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------



- [Python 3.12: 值得尝试的酷炫新功能](https://pycoders.com/link/11517/web)
    + REAL PYTHON

In this tutorial, you’ll learn about the new features in Python 3.12. You’ll explore how the new release extends the better error messages and faster code execution found in the previous version, and you’ll try out the improvements to f-strings and type variable syntax.


(`是也乎:`


![3.12](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.51.17.jpg)

)


- [Python 3.12: 静态类型改进](https://pycoders.com/link/11522/web)
    + REAL PYTHON

In this tutorial, you’ll see the new static typing features in Python 3.12. You’ll learn about the new syntax for type variables, making generics simpler to define. You’ll also see how @override lets you model inheritance and how you use typed dictionaries to annotate variable keyword arguments.


(`是也乎:`


![Static](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.50.22.jpg)

)



- [Python 3.12: Subinterpreters/子解释器](https://pycoders.com/link/11539/web)
    + REAL PYTHON

In this tutorial, you’ll see one of the new features of Python 3.12 and a proposed change to Python 3.13, addressing how subinterpreters work in the CPython program. The changes are described in PEP 684 and PEP 554.

(`是也乎:`

![Subinterpreters](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.47.54.jpg)


)



- [Python 3.12.0 发布](https://pycoders.com/link/11548/web)
    + PYTHON.ORG

(`是也乎:`


Wow 3.12 时代正式到来

)


- [2022 年 Python 开发者调查结果](https://pycoders.com/link/11545/web)
    + JETBRAINS.COM



-----------------------------------------
## 探讨/吐糟
> Discussions


- [Excel 中的 Python AMA](https://pycoders.com/link/11532/web)
    + REDDIT

Folks at Microsoft participated in an Ask-Me-Anything session on the new Python in Excel over Azure feature. See also the Slashdot post which has a good summary.

- [PEP 722 和 PEP 723 用户研究讨论](https://pycoders.com/link/11531/web)
    + PYTHON.ORG

User studies were conducted on on PEP 722 – Dependency specification for single-file scripts and PEP 723 – Embedding pyproject.toml in single-file scripts , this discussion summarizes the results.


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks





- [考虑 ChatGPT 对一本编程书籍的评论](https://pycoders.com/link/11529/web)
    + REAL PYTHON 
    + PODCAST

What can you learn from feeding an entire book on Python programming into ChatGPT-4 and asking it to provide a technical review? What are the potential pitfalls of using an LLM as a learning tool? This week on the show, author Al Sweigart talks about his recent experiments using ChatGPT and Python.

(`是也乎:`

![ChatGPT](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.40.34.jpg)

)


- [Mojo: 与 Python 和 Numba 正面交锋](https://pycoders.com/link/11535/web)
    + MAXIM SAPLIN

This article covers a Mandelbrot-based benchmark of Python, variations of Numba, and the newly available Mojo. Although Mojo is fast it takes a lot more work than the author expected to translate Python to it, and with the right parameters Numba still beats it.



- [探索Wordle](https://pycoders.com/link/11538/web)
    + GEORGE REILLY 
    + • Shared by George Reilly

Explores how to programmatically find eligible answers for a Wordle game using Python, based on some guess-score pairs. Works through various bugs and subtleties, showing how to infer tighter constraints and explain why words were rejected.

- [大多数复制的 StackOverflow 代码片段都有缺陷！](https://pycoders.com/link/11520/web)
    + ANDREAS LUNDBLAD

“In a recent study titled Usage and Attribution of Stack Overflow Code Snippets in GitHub Projects, an answer I wrote almost a decade ago was found to be the most copied snippet on Stack Overflow. Ironically it happens to be buggy.”


(`是也乎:`


等等, 这是必然的哪, 别人的场景不可能正好吻合自己当前所有条件的哪...
但是, 可用, 可参考就足够了...

)


- [科学家Python开发指南](https://pycoders.com/link/11536/web)
    + SCIENTIFIC-PYTHON.ORG 
    + • Shared by Henry Schreiner

This article talks about the release of the “Scientific-Python Development Guide” which documents Python package development. It includes cookie-cutter templates and repo tools.


(`是也乎:`

不是科学的开发 Python,
而是科学家如何用 Python 折腾...

)


- [Python 和 HTMX 的 3 个 IRL 用例](https://pycoders.com/link/11542/web)
    + BITE CODE

This blog post summarizes three recent uses where the author has applied HTMX to his websites, and how they simplified his process.

- [用 Python 类型提示进行战斗](https://pycoders.com/link/11519/web)
    + MILOSLAV POJMAN

Miloslav wanted to properly type-hint a decorator. Turns out, it wasn’t the easiest thing to do. Read on for his solution.

- [AB 测试入门](https://pycoders.com/link/11527/web)
    + JONATHAN FULTON

A comprehensive deep dive on AB Testing including the math behind knowing whether your tests are significant.

(`是也乎:`

![AB](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.34.27.jpg)

是的, 你得有一点儿概率的控制计算...

)


- [在 Git 存储库中，您的文件存放在哪里？](https://pycoders.com/link/11521/web)
    + JULIA EVANS

Write some Python to explore the data objects Git uses to store your content.

(`是也乎:`


所以, Rust 社区将这堆东西变成了 SQL 就....爆了...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [Concourse 工具: Concourse CI 的自定义资源类型](https://pycoders.com/link/11543/web)
    + GITHUB.COM/GCHQ 
    + • Shared by GCHQ

- [Baserow: OSS Airtable 替代方案](https://pycoders.com/link/11533/web)
    + GITLAB.COM/BASEROW

- [pyobd: 开源 Obd2 自动诊断程序](https://pycoders.com/link/11526/web)
    + GITHUB.COM/BARRACUDA-FSH

- [upiano: 终端中的钢琴](https://pycoders.com/link/11528/web)
    + GITHUB.COM/ELIASDORNELES

(`是也乎:`


![Piano](https://ipic.zoomquiet.top/2023-10-04-zshot%202023-10-04%2021.31.12.jpg)

一眼就看到中央C

)


- [PyWa: 使用 WhatsApp Cloud API 构建机器人](https://pycoders.com/link/11518/web)
    + GITHUB.COM/DAVID-LEV 
    + • Shared by David Lev






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11546/web)
    + October 4, 2023

- [PyConZA 2023](https://pycoders.com/link/11541/web)
    + October 5 to October 7, 2023

- [Canberra Python Meetup](https://pycoders.com/link/11534/web)
    + October 5, 2023

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/11547/web)
    + October 5, 2023

- [PyCon ES Canarias 2023](https://pycoders.com/link/11537/web)
    + October 6 to October 9, 2023

- [Django Day Copenhagen 2023](https://pycoders.com/link/11515/web)
    + October 6 to October 7, 2023

- [DjangoCongress JP 2023](https://pycoders.com/link/11516/web)
    + October 7 to October 8, 2023




-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 545](https://weekly.pychina.org/issue/issue-545.html)
- 2021: [蠎周刊 492](https://weekly.pychina.org/issue/issue-492.html)
    + [pythonista-weekly : Pyw 519](https://weekly.pychina.org/python-weekly/pyw-519.html)
- 2020: [蠎周刊 439](https://weekly.pychina.org/issue/issue-439.html)
    + [pythonista-weekly : Pyw 469](https://weekly.pychina.org/python-weekly/pyw-469.html)
- 2019: [蠎周刊 388](https://weekly.pychina.org/issue/issue-388.html)
- 2018: [蠎周刊 337](https://weekly.pychina.org/issue/issue-337.html)
- 2017: [蠎加载 144](https://weekly.pychina.org/importpython/importpython-144.html)
- 2016: [蠎加载 93](https://weekly.pychina.org/importpython/importpython-93.html)
- 2015: [蠎周刊 186](https://weekly.pychina.org/issue/issue-186.html)
    + [蠎加载 52](https://weekly.pychina.org/importpython/importpython-52.html)
- 2014: [Issue 135](https://weekly.pychina.org/issue/issue-135.html)
- 2013: [Issue 87 ~ 感谢贡献](https://weekly.pychina.org/issue/issue-87.html)
- 2012: 空缺


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + @Chaos42DAMA
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊





```
         _~∽&~~_
     \/ /  ◴ ◴  \ (/
       '_   ♢   _'
       | '--#--' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 597 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-597.html)
- 修订: [issue-597.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-597.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF597D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF597D4Q90XdDA7g):



```python
全职嗯哼: 大妈的多重宇宙 - https://www.youtube.com/@Chaos42DAMA
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开社群: 蟒营 (订阅号: Mainium)

as 创始组织者:
    CPyUG (mailling-list: python-cn@googlegroups.com)
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        AIGC珠海 

```

-------------



