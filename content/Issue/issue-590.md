Title: 蠎周刊(PyCoder)590
Slug: issue-590
Date: 2023-08-16 11:42
Tags: Weekly,Python,pycoders,ZH


> 为什么 Python 如此神奇


原文: [PyCoder's Weekly - Issue #590](https://pycoders.com/issues/590)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230816 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230816 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------





- [如何注释返回 self 的方法](https://pycoders.com/link/11287/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use the Self type hint in Python to annotate methods that return an instance of their own class. You’ll gain hands-on experience with type hints and annotations of methods that return an instance of their class, making your code more readable and maintainable.


(`是也乎:`


![self](https://ipic.zoomquiet.top/2023-08-16-zshot%202023-08-16%2010.34.35.jpg)
)

- [用 Python 创建上下文管理器](https://pycoders.com/link/11283/web)
    + TREY HUNNER 
    + • Shared by Trey Hunner

Objects with __enter__ and __exit__ methods can be used as context managers in Python. This article (and screencast) explains most of what you’ll want to know when creating your own context managers.


- [PEP 723: 在单文件脚本中嵌入 pyproject.toml](https://pycoders.com/link/11291/web)
    + PYTHON.ORG

This PEP proposes a metadata format which a single-file script can use to specify dependency and tool information for IDEs and external development tools. It replaces PEP 722.

- [PyPI: 新用户注册的 2FA 强制执行](https://pycoders.com/link/11268/web)
    + PYPI.ORG

- [PSF 宣布任命新的 PyPI 安全工程师](https://pycoders.com/link/11265/web)
    + PYTHON SOFTWARE FOUNDATION

- [Python 3.12.0 RC 1 发布](https://pycoders.com/link/11272/web)
    + CPYTHON DEV BLOG










-----------------------------------------
## 探讨/吐糟
> Discussions

NULL






-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks

- [Prompt Engineering: 一个实际例子](https://pycoders.com/link/11266/web)
    + REAL PYTHON

Learn prompt engineering techniques with a practical, real-world project to get better results from large language models. This tutorial covers zero-shot and few-shot prompting, delimiters, numbered steps, role prompts, chain-of-thought prompting, and more. Improve your LLM-assisted projects today.



(`是也乎:`

![Prompt](https://ipic.zoomquiet.top/2023-08-16-zshot%202023-08-16%2010.29.44.jpg)

)

- [Why Static Languages Suffer From Complexity
为什么静态语言会变得复杂](https://pycoders.com/link/11280/web)
    + HIRROLOT

An extremely detailed, deep dive on how static type systems impact the consistency of languages. Hirrolot compares a variety of lesser known languages to see the consequences of their decisions. See also the associated Hacker News discussion.


(`是也乎:`


都是硬件的锅...

)



- [Python的 list ：深入探究示例](https://pycoders.com/link/11298/web)
    + REAL PYTHON

In this tutorial, you’ll dive deep into Python’s lists. You’ll learn how to create them, update their content, populate and grow them, and more. Along the way, you’ll code practical examples that will help you strengthen your skills with this fundamental data type in Python.


(`是也乎:`

![list](https://ipic.zoomquiet.top/2023-08-16-zshot%202023-08-16%2010.23.31.jpg)

)


- [排序算法完整比较](https://pycoders.com/link/11294/web)
    + CODERSLEGACY.COM 
    + • Shared by Raahim Siddiqi

An comprehensive comparison on the performance of 9 major Sorting Algorithms and how well they perform under varying circumstances. The aim of the article is to show you where each type of Algorithms shines, and where it does badly.


(`是也乎:`

其实排序算法远没有到达极限,
谁要提出一个有效的排序算法照样能得图灵奖.

)

- [支持 Python-Markdown 中的 Bootstrap-Alerts](https://pycoders.com/link/11297/web)
    + FLORIAN DAHLITZ 
    + • Shared by Florian Dahlitz

If you’re using Markdown on your blog, or any website, a conversion pipeline allows you to create your own rules and widgets. This article shows you how to integrate Bootstrap Alert boxes into a Markdown workflow.

- [简单的导入如何修改解释器](https://pycoders.com/link/11277/web)
    + KEN SCHUTTE

This article shows a sample module that swaps the values for 8 and 9, not something generally recommended. Learn how side effects from an import can impact your code and just what the integer object cache is.

- [优雅重要吗？](https://pycoders.com/link/11295/web)
    + MATHSPP.COM 
    + • Shared by Rodrigo Girão Serrão

In this article, the author explains why he thinks that elegance should be a fundamental driver when you are writing (Python) code, and gives a few tips on how to write elegant code.

(`是也乎:`


```
>>> import itertools
>>> list_of_lists = [[1, 2, 3], [4], [5, 6]]
>>> list(itertools.chain(*list_of_lists))
[1, 2, 3, 4, 5, 6]
```

官方的优雅是必须的...

)

- [为什么 Python 如此神奇](https://pycoders.com/link/11290/web)
    + JOS VISSER

This opinion piece by Jos is a counter to the “its a terrible language” posts you come across once and a while. Read why Jos thinks Python is amazing.


(`是也乎:`

简单的说, 你可以用很低的心智成本作出任何东西来...

)

- [从零开始搞 Llama](https://pycoders.com/link/11270/web)
    + BRIAN KITANO

This blog post provides step by step instructions on how to implement llama from scratch, using a dramatically scaled-down version for training.


- [对联合LLMs的对抗性攻击](https://pycoders.com/link/11279/web)
    + ZOU, WANG, KOLTER, & FREDRIKSON

Deep CS paper on how to abuse Large Language Models and work around restrictions where the model is refusing to answer.

- [2022年PSF年度报告](https://pycoders.com/link/11278/web)
    + PYTHON.ORG

The annual report from the Python Software Foundation details all the changes and events at the PSF last year.


(`是也乎:`



![grabt](https://ipic.zoomquiet.top/2023-08-16-zshot%202023-08-16%2010.01.45.jpg)

怪不得无感呢...

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code





- [dpv: pyenv-virtualenv 和 virtualenvwrapper 的替代方案](https://pycoders.com/link/11276/web)
    + GITHUB.COM/CAIOARIEDE 
    + • Shared by Caio Ariede


(`是也乎:`


![dpv](https://ipic.zoomquiet.top/2023-08-16-zshot%202023-08-16%2009.58.21.jpg)

)

- [nodice-cli: 没有依赖项的单词列表生成器](https://pycoders.com/link/11289/web)
    + GITHUB.COM/AVNIGO

- [briefcase: 将 Python 转换为本机应用程序](https://pycoders.com/link/11269/web)
    + GITHUB.COM/BEEWARE

(`是也乎:`

BeeWare 的衍生工具...

)

- [django_simple_notification: REST 通知系统](https://pycoders.com/link/11292/web)
    + GITHUB.COM/MAHMOUDNASSER01

- [pyOCD: 适用于 Arm Cortex-M 微控制器的 Python](https://pycoders.com/link/11285/web)
    + GITHUB.COM/PYOCD







-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11273/web)
    + August 16, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/11288/web)
    + August 17, 2023

- [PyLadies Dublin](https://pycoders.com/link/11271/web)
    + August 17, 2023

- [DjangoConAU 2023](https://pycoders.com/link/11275/web)
    + August 18 to August 19, 2023

- [PyCon AU 2023](https://pycoders.com/link/11286/web)
    + August 18 to August 23, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/11267/web)
    + August 18 to August 19, 2023

- [PyCon Latam 2023](https://pycoders.com/link/11281/web)
    + August 24 to August 27, 2023






-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 538](https://weekly.pychina.org/issue/issue-538.html)
- 2021: [蠎周刊 485](https://weekly.pychina.org/issue/issue-485.html)
    + [pythonista-weekly : Pyw 512](https://weekly.pychina.org/python-weekly/pyw-512.html)
- 2020: [蠎周刊 432](https://weekly.pychina.org/issue/issue-432.html)
    + [pythonista-weekly : Pyw 462](https://weekly.pychina.org/python-weekly/pyw-462.html)
- 2019: [蠎周刊 381](https://weekly.pychina.org/issue/issue-381.html)
- 2018: [蠎周刊 330](https://weekly.pychina.org/issue/issue-330.html)
- 2017: [蠎加载 137](https://weekly.pychina.org/importpython/importpython-137.html)
- 2016: [蠎加载 86](https://weekly.pychina.org/importpython/importpython-86.html)
- 2015: [蠎周刊 179](https://weekly.pychina.org/issue/issue-179.html)
    + [蠎加载 45](https://weekly.pychina.org/importpython/importpython-45.html)
- 2014: [Issue 128](https://weekly.pychina.org/issue/issue-128.html)
- 2013: 空缺
- 2012: [Issue 27: Stompy](https://weekly.pychina.org/issue/issue-27.html)


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
      _~-+∽~_
  () /  ◵ ^  \ \/
    '_   △   _'
    > '--.--' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```




-----------------------------------------
# PS:

- 首发: [Issue 590 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-590.html)
- 修订: [issue-590.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-590.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF590D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF590D4Q90XdDA7g):



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



