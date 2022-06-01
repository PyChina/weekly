Title: PyCoder 527
Slug: issue-527
Date: 2022-06-01 11:42
Tags: Weekly,Python,pycoders,ZH


> 对数据科学家有用的 Python 装饰器


原文: [PyCoder's Weekly - Issue #527](https://pycoders.com/issues/527)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220601 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220601 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python 的“函数”有时是类](https://pycoders.com/link/8787/web)
    + TREY HUNNER

Ever use list() or enumerate()? Think of them as functions? They’re not, they’re classes. Sometimes we call classes functions in Python. Why? And what’s a “callable”?

- [探索 Python 中的作用域和闭包](https://pycoders.com/link/8803/web)
    + REAL PYTHON COURSE

In this Code Conversation video course, you’ll take a deep dive into how scopes and closures work in Python. To do this, you’ll use a debugger to walk through some sample code, and then you’ll take a peek under the hood to see how Python holds variables internally.

(`是也乎:`

![COURSE](https://ipic.zoomquiet.top/2022-06-01-zshot%202022-06-01%2010.14.45.jpg)

是的, 套娃,
幸好 Python 严密的用缩进进行了可视化先...

)


- [所有关于星号在 Python 中需要知道的](https://pycoders.com/link/8818/web)
    + BAS STEINS

The `*` is for more than multiplication, it is also the basis for the two deconstruction operators: `*` and `**`. Learn the ins-and-outs of using 
`*args`, `**kwargs`, deconstruction, and forcing keyword-arguments-only in functions.


- [ctx 库被劫持以窃取 AWS 密钥](https://pycoders.com/link/8805/web)
    + AX SHARMA


(`是也乎:`


全新 Hijacked 姿势...

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [对数据科学家有用的 Python 装饰器](https://pycoders.com/link/8792/web)
    + HACKER NEWS

Marton Trencseni posted Useful Python decorators for Data Scientists, a follow-up to the article included in Issue #525. It got posted on Hacker News and strong opinions ensued. Read the article, then weigh in.

(`是也乎:`


[Bytepawn - Marton Trencseni – Useful Python decorators for Data Scientists](https://bytepawn.com/python-decorators-for-data-scientists.html)

数据科学常用修饰符函式

一键追加实用观察

)


- [近年来 Python 标准库的变化](https://pycoders.com/link/8815/web)
    + HACKER NEWS

Discussion based on the previously linked article Python Standard Library Changes in Recent Years.


(`是也乎:`

变化太多, 基本只用基本数据结构, 其它都用第三方模块了...
)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks






- [如何使用 argparse 创建命令行应用程序](https://pycoders.com/link/8823/web)
    + MIKE DRISCOLL

Scripts often need either configuration or data to proceed and for many situations this can be passed in on the command line. The standard library argparse helps you parse arguments, add help info, and even alias your commands.


(`是也乎:`


推荐还是用类似 invoke 之类高度封装后的 CLI 开发框架

)


- [Python Plots 设置动画的快速方法](https://pycoders.com/link/8804/web)
    + CHRISTOPHER TAO

There are lots of choices when developing animated plots, many of which have a steep learning curve. Learn how to create animated GIFs through matplotlib and ImageIO to bash something out quickly.



- [鲜为人知的 Django 管理命令](https://pycoders.com/link/8799/web)
    + GONÇALO VALÉRIO

You probably know about runserver, migrate and shell, but there are lots more Django management commands. Learn about diffsettings, sendtestemail, inspectdb, and showmigrations.

(`是也乎:`


为什么 `鲜为人知` ? 

)


- [用 Python 和 Graphviz 对正则表达式动画化](https://pycoders.com/link/8790/web)
    + AYDIN SCHWARTZ

Visualizing regular expressions can help you understand how they work and what a particular expression accomplishes. Read on to learn how to use Graphviz to better understand your regex.


(`是也乎:`


[aydinschwa/Regex-Engine: Educational, animated regular expression engine](https://github.com/aydinschwa/Regex-Engine)

亮了, 用 Python 分析清楚正则表达式的匹配顺序, 
然后逐步用 Graphviz 可视化,
最后拼为动画

![demo](https://github.com/aydinschwa/Regex-Engine/raw/main/demo.gif)

看起来更加乱了...

)


- [用 Django/React 和 Docker 构建 CRUD 应用程序](https://pycoders.com/link/8797/web)
    + MANGABO KOLAWOLE

Step-by-step instructions on creating a web application with a React front-end and the Django Rest Framework as a back-end and all tied together with Docker for distribution.

(`是也乎:`


虽然听起来 Low , 但是, CRUD 的确是绝大多数系统的核心使命,
真想作到也不容易...

)



- [Python 中有什么/各版本...](https://pycoders.com/link/8808/web)
    + NED BATCHELDER

A quick listing of what features were added in which version of Python, going back to Python 2.1 and including links to corresponding PEPs.


(`是也乎:`


Python 3 以来关键版本的关键使命规划...

)


- [Python 中的本机类型/Dunder 方法](https://pycoders.com/link/8806/web)
    + THEODOROS KARASAVVAS

Learn how to make your classes act like native data types through the implementation of double-underscore magic methods.




- [f-strings and re.VERBOSE 不合理效果](https://pycoders.com/link/8812/web)
    + ANDGRAVITY.COM

A look at one or two ways to make life easier when working with Python regular expressions.




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [import-tracker: 跟踪库中的第 3 方依赖项](https://pycoders.com/link/8798/web)
    + GITHUB.COM/IBM


(`是也乎:`

IBM 作品

)

- [dowsing: 不运行就能提取元数据](https://pycoders.com/link/8788/web)
    + GITHUB.COM/PYTHON-PACKAGING

(`是也乎:`

为了避开 PEP517 而构建

)


- [lineapy: 捕获/分析和自动化数据科学工作流程](https://pycoders.com/link/8795/web)
    + GITHUB.COM/LINEALABS

- [电脑正念应用程序](https://pycoders.com/link/8789/web)
    + GITLAB.COM/MINDFULNESS-AT-THE-COMPUTER

(`是也乎:`

是的, 越来越多开源工程迁移到 GitLab 上来了

)

- [PyDaddy: 从时间序列数据中发现 SDE 方程](https://pycoders.com/link/8796/web)
    + GITHUB.COM/TEE-LAB 
    + • Shared by Ashwin Karichannavar



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [STL Python](https://pycoders.com/link/8817/web)
    + June 1, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/8810/web)
    + June 1, 2022

- [PyCon Italy 22](https://pycoders.com/link/8813/web)
    + June 2 to June 6, 2022

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/8824/web)
    + June 2, 2022

- [Reunión Python Valencia](https://pycoders.com/link/8816/web)
    + June 2, 2022

- [Virtual PythonCamp Cologne 2022](https://pycoders.com/link/8819/web)
    + June 4 to June 6, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅

![ACM-O](https://ipic.zoomquiet.top/2022-04-27-zshot%202022-04-27%2009.22.46.jpg)

(`是也乎:`


谈崩了, 之前通过 ACM 会员可以每年 $25 享受 O'REILLY 在线图书馆服务...现在没了

)

-----------------------------------------
# PS:

- 首发: [Issue 527 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-527.html)
- 修订: [issue-527.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-527.md)


## PPS:
> 不觉中蟒周刊快译已经到了第10个年头

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

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF527D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF527D4Q90XdDA7g):



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





