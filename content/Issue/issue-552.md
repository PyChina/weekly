Title: PyCoder 552
Slug: issue-552
Date: 2022-11-23 11:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.11 微基准测试


原文: [PyCoder's Weekly - Issue #552](https://pycoders.com/issues/552)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221123 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221123 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [用 WebAuthn 使项目远离密码](https://pycoders.com/link/9896/web)
    + REAL PYTHON 
    + PODCAST

What if you didn’t have to worry about managing user passwords as a Python developer? That’s where the WebAuthn protocol and new hardware standards are heading. This week on the show, Dan Moore from FusionAuth returns to discuss a password-less future.


(`是也乎:`

![WebAuthn](https://ipic.zoomquiet.top/2022-11-23-zshot%202022-11-23%2009.13.26.jpg)

问题就在并不是所有场景都必须联网哪...


)


- [Python 开发者的 Mastodon](https://pycoders.com/link/9912/web)
    + KENNEDY, 
    + HÄUSSGE, 
    + WILLISON, 
    + & RODRÍGUEZ 
    + PODCAST

Want more information about Mastodon and how Python folks are interacting with it? This interview with multiple Python programmers discusses how they’re using Mastodon and what that community is like in comparison to other social media platforms.

(`是也乎:`

叕一个想替代 Slack 的 code social 平台?

)



- [Python 3.12 有什么新鲜东西?](https://pycoders.com/link/9902/web)
    + PYTHON.ORG

This article in the Python development docs outlines all the changes coming in Python 3.12: even more error message improvement, support for the Linux profiler, improvements to many modules, and more.

- [PyTexas 2023 提前注册和论文征集](https://pycoders.com/link/9889/web)
    + PYTEXAS.ORG 
    + • Shared by Mason Egger







-----------------------------------------
## 探讨/吐糟
> Discussions


- [通过编码和技能赚钱的替代方法?](https://pycoders.com/link/9894/web)
    + HACKER NEWS


(`是也乎:`

所以 Musk 们来了之后,国外程序猿们也开始紧张了?

> Building and selling macOS apps

好吧,这的确是个最省心的渠道,
虽然 Apple 抽成不少,但是, 整体生态是真的非常健康无匹.

说穿了, 不再出售时间和精力,而是成品.
)


- [Python 3.12.0 将删除长期弃用的项目](https://pycoders.com/link/9883/web)
    + HACKER NEWS

(`是也乎:`

嘦大部分现有第三方模块/库兼容,怎么折腾都行

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [首先构建模块化单体](https://pycoders.com/link/9882/web)
    + CHRIS KLUG

“Even talking about building a monolith today, is a bit taboo. It is all about microservices at the moment, and has been for a few years. But they aren’t a silver bullet.” Coding samples in the article are not Python, but the architectural advice is cross language.


(`是也乎:`

monolith ~ 巨石系统,
从各种DDD 想划分原有 monolith 系统之后,
就没成功过,所以, 又回来, 重新思考...

)

- [重写 Python 代码的工具](https://pycoders.com/link/9885/web)
    + LUKE PLANT

An annotated list for tools that improve your Python code. Includes a variety of linters, type hint tools, upgrade scripts, refactoring tools and more. Luke gives you a quick description of each and makes some recommendations.


(`是也乎:`

得益于 Python 内建的语法解析能力,
只是, 我们需要工具快速对自己的代码动手嘛?
除了缩进的自动对齐, 其它的就象一个老婆婆反复提醒无聊的真理...

)


- [直接从 Python 调用 Windows 消息框](https://pycoders.com/link/9911/web)
    + MATT CALLAHAN

Want a pop-up message box on Windows without having the overhead of a GUI library? Using the built-in ctypes library you can get at Windows internals and show a dialog box.


(`是也乎:`

Linux 系统的桌面消息服务,一直是公开可调用的,
Win10 们的,就是魔法了...

)


- [用 Gunicorn 和 Nginx 部署 Django 应用程序](https://pycoders.com/link/9886/web)
    + REAL PYTHON 
    + COURSE

Ready to take your Django app beyond development? Learn how to deploy your Django web app in production on a real-world public domain with Gunicorn and Nginx.


(`是也乎:`

![Gunicorn](https://ipic.zoomquiet.top/2022-11-23-zshot%202022-11-23%2009.05.21.jpg)


Gunicorn 这名儿真好,每次都想起来很多大片儿...

)


- [如何对 (Python) 代码进行基准测试](https://pycoders.com/link/9893/web)
    + SEBASTIAN WITOWSKI

There are plenty of ways to measure the speed of your code. This article shows a few that Sebastian considered working with in his “Writing Faster Python” series.


(`是也乎:`

开始 Benchmark Py 代码时,如果不是太闲了,
就是业务真的爆发起来了...

)


- [Infosys 在 PyPI 上泄露 AWS 密钥超过一年](https://pycoders.com/link/9903/web)
    + TOM FORBES

Tom got a bit of an odd pull request and as he dug in he found AWS Keys in places they shouldn’t be. Read on for a bit of advice on what not to do yourself.


(`是也乎:`

呃,都是咖啡量不够时发生的事儿...

)

- [向大型 Python 代码库添加类型](https://pycoders.com/link/9901/web)
    + SEAN MACKESEY

Moving an existing Python code base to 100% typed can be a lot of work. This article talks about the steps and challenges gone through in one such project.

(`是也乎:`

感谢这些活跃的老项目,
积累的工具可以给各种新人使用...

)




- [Python 3.11 微基准测试](https://pycoders.com/link/9887/web)
    + KRACEKUMAR 
    + • Shared by Kracekumar

Unless you’ve been asleep, you’ve probably heard that Python 3.11 is faster. This article digs into the details on how certain IO operations have sped up.

(`是也乎:`

![Micro](https://ipic.zoomquiet.top/2022-11-23-zshot%202022-11-23%2009.01.08.jpg)

开始自我部卷了

`微基准` 又一个具备流行性的好词儿

)


- [Python中的并行化: 简单的方法](https://pycoders.com/link/9904/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

The article introduces parallelization in Python using multiprocessing.Pool() in combination with the map() function and processing pipelines.


(`是也乎:`

其实都没什么轻松途径的,
底层机制就这样,
不过是用的人多了,才有动力逐层自动化...

)




-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [johnnycanencrypt: OpenPGP 的 Python 模块](https://pycoders.com/link/9895/web)
    + GITHUB.COM/KUSHALDAS

- [pyjanitor: 用于数据清理的 Clean API](https://pycoders.com/link/9905/web)
    + GITHUB.COM/PYJANITOR-DEVS

- [常见的 Python 备忘单](https://pycoders.com/link/9888/web)
    + GITHUB.COM/AFIZS

(`是也乎:`

或是说作弊条, 以往 Py2 时代的,很多都过时了,
现在,随着 Python 本身的突飞猛进, 也值得持续更新了...

)


- [dbt-coverage: DBT 项目的文档和测试覆盖率](https://pycoders.com/link/9914/web)
    + GITHUB.COM/SLIDOAPP 
    + • Shared by Marek Suppa

- [chat-miner: 聊天数据的精益解析器和可视化](https://pycoders.com/link/9899/web)
    + GITHUB.COM/JOWEICH

(`是也乎:`

这种东西,中国各大厂早就配置充分了,
毕竟要瞬间完成和谐嘛...

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [NZPUG-Auckland Coding Challenge “Office Hours”](https://pycoders.com/link/9910/web)
    + November 23, 2022

- [PyKla Monthly Meetup](https://pycoders.com/link/9898/web)
    + November 23, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9907/web)
    + November 23, 2022

- [SPb Python Drinkup](https://pycoders.com/link/9908/web)
    + November 24, 2022

- [Pyjamas Conf 2022](https://pycoders.com/link/9891/web)
    + November 26 to November 28, 2022

- [Django Girls Groningen](https://pycoders.com/link/9884/web)
    + November 26, 2022

- [PyData Global 2022](https://pycoders.com/link/9909/web)
    + December 1 to December 4, 2022





-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 552 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-552.html)
- 修订: [issue-552.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-552.md)


## PPS:
> 不觉中蟒周刊快译已经到了第11个年头

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

-------------

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF552D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF552D4Q90XdDA7g):



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





