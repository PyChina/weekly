Title: PyCoder 568
Slug: issue-568
Date: 2023-03-15 11:42
Tags: Weekly,Python,pycoders,ZH


> 22年 Django 开发者调查报告来了


原文: [PyCoder's Weekly - Issue #568](https://pycoders.com/issues/568)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230315 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.
- 230315 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译

------



- [用 BeeWare 跨平台共享你的 Python 应用程序](https://pycoders.com/link/10481/web)
    + REAL PYTHON 
    + PODCAST

Are you interested in deploying your Python project everywhere? This week on the show, Russell Keith-Magee, founder and maintainer of the BeeWare project, returns. Russell shares recent updates to Briefcase, a tool that converts a Python application into native installers on macOS, Windows, Linux, and mobile devices.

(`是也乎:`

![PODCAST](https://ipic.zoomquiet.top/2023-03-15-zshot%202023-03-15%2010.09.26.jpg)

)


- [Python Asyncio 任务的开销](https://pycoders.com/link/10462/web)
    + WILL MCGUGAN

The Textual library uses a lot of asyncio tasks. In order to determine whether to spend time optimizing them, Will measured the cost of creating asyncio tasks. TLDR; optimize something else. This article also spawned a conversation on Hacker News.


- [Julia 和 Python 更好地结合](https://pycoders.com/link/10472/web)
    + BOGUMIŁ KAMIŃSKI

Julia is a popular programming language among data scientists, but if you ever code in that space and miss some of the key Python libraries, this article is for you. Julia packages can wrap other languages, so you can have the best of both worlds.


(`是也乎:`

原先不是说要超越的?
现在就在一起了?


)


- [Python 3.12.0 Alpha 6 发布](https://pycoders.com/link/10494/web)
    + CPYTHON DEV BLOG



- [2022 年 Django 开发者调查结果可用](https://pycoders.com/link/10464/web)
    + DJANGO SOFTWARE FOUNDATION


(`是也乎:`

是的, Django 开发者已经是 web 应用代表了,
Flask 不是...

![DJANGO](https://ipic.zoomquiet.top/2023-03-15-zshot%202023-03-15%2010.06.52.jpg)

比较有趣的是最后的联系网络入口...有微信呢.

)


-----------------------------------------
## 探讨/吐糟
> Discussions

- [近 40% 的软件工程师在远程工作](https://pycoders.com/link/10493/web)
    + HACKER NEWS


(`是也乎:`

好事儿? 

神奇的是, 类似讨论都是在 news.ycombinator.com
这个频道的流量可能比 Yc 投资的各种项目的流量还大...

)

-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用化学性质预测葡萄酒质量](https://pycoders.com/link/10483/web)
    + ALFREDO GONZÁLEZ-ESPINOZA

Alfredo discovered some datasets about wine quality including chemical properties and decided it was time to do some predictive model building. This article walks you through what he did with torch, sklearn, numpy, pandas, and seaborn to predict wine quality.

- [这些数字是真实的还是虚假的？ 尝试使用 Benford 定律来鉴别](https://pycoders.com/link/10482/web)
    + JASON ROSS

How can you tell whether a set of figures is trustworthy? It’s not always simple, but Benford’s Law gives you one way to find out. There’s even a Python Package to help you check: [randalyze](https://pycoders.com/link/10466/web).


(`是也乎:`

Benford定律是指在一组数字中，以数字1开头的数字出现的概率最高，随着数字的增大，出现的概率逐渐降低。 Benford定律可以应用于各种领域，如财务、科学、统计等，用于检测数据的真实性和完整性。

所以, 可以用代码自动分析出文章中的数据是否是真实的...

)


- [用 Python 构建基于 ChatGPT 的助手](https://pycoders.com/link/10467/web)
    + FAIZANBASHIR.ME 
    + • Shared by Faizan Bashir

This article demonstrates a workflow for integrating multiple AI services to perform speech-to-text (STT), natural language processing (NLP), and text-to-speech (TTS) using OpenAI’s ChatGPT and Whisper API’s in Python.

- [如何使用 Python 装饰器绞杀旧代码](https://pycoders.com/link/10480/web)
    + JON JAGGER

The “strangler pattern” is a way of simultaneously running old and replacement code to determine through live behavior whether the replacement works. This article shows you how to use decorators to help.



(`是也乎:`


![kosli](https://ipic.zoomquiet.top/2023-03-15-zshot%202023-03-15%2010.15.44.jpg)

创作团队全员漫画形象...应该是一个模型统一生成的..

)

- [将 Django 应用部署到 Azure 应用服务](https://pycoders.com/link/10484/web)
    + NIK TOMAZIC

This tutorial looks at how to deploy a Django application to Azure App Service. Includes details on configuring your Django and what Azure services to use to get going quickly.

(`是也乎:`

不是, 这种文章不在 Azure 官网上就差点儿意思...
这方面, DigitalOcean 是真的标杆儿了...

)

- [Python 的可变类型与不可变类型: 有什么区别?](https://pycoders.com/link/10487/web)
    + REAL PYTHON

In this tutorial, you’ll learn how Python mutable and immutable data types work internally and how you can take advantage of mutability or immutability to power your code.

(`是也乎:`

![Immutable](https://ipic.zoomquiet.top/2023-03-15-zshot%202023-03-15%2009.30.31.jpg)

)


- [Formatting 出错](https://pycoders.com/link/10465/web)
    + KOJO IDRISSA

Your code formatter may have reformatted your API key. This can cause confusing errors. Read Kojo’s tale to learn what happened and how he figured it out.



- [在维护顺序的同时删除重复列表](https://pycoders.com/link/10470/web)
    + TREY HUNNER 
    + • Shared by Trey Hunner

There’s more than one way deduplicate an iterable in Python. Which approach you take will depend on whether you care about the order of your items.



- [Python 断言，或检查猫是否是狗](https://pycoders.com/link/10492/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

The articles explains the rules of using assertions in Python, and when not to use them. Includes details on the __debug__ object.

- [用 Matplotlib 在 Python 中绘制 XKCD-style](https://pycoders.com/link/10460/web)
    + RODRIGO GIRÃO SERRÃO 
    + • Shared by Rodrigo Girão Serrão

This short article shows how to add a twist to your matplotlib plots by styling them like the web-famous comic xkcd.


(`是也乎:`


> with plt.xkcd():


然后世界就变得友好很多...

![xkcd](https://ipic.zoomquiet.top/2023-03-15-zshot%202023-03-15%2008.59.44.jpg)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [通过单文件 Python 脚本与 ChatGPT 交互](https://pycoders.com/link/10495/web)
    + GITHUB.COM/REORX • Shared by Reorx




- [meerkat: 非结构化数据的交互式数据框架](https://pycoders.com/link/10497/web)
    + GITHUB.COM/HAZYRESEARCH



- [sketch: Pandas 的 AI 代码编写助手](https://pycoders.com/link/10475/web)
    + GITHUB.COM/APPROXIMATELABS

(`是也乎:`

Jupter 真的可以是 GPT 们控制世界的最好入口了...

)


- [replbuilder: 用于构建自定义 REPL 的工具](https://pycoders.com/link/10488/web)
    + GITHUB.COM/APEROCKY



(`是也乎:`

非常实用了, 
以往得自己用 dict 之类拼...

AWS 工程师日用品...?

)


- [pylyzer: Python 的快速静态代码分析器](https://pycoders.com/link/10463/web)
    + GITHUB.COM/MTSHIBA


(`是也乎:`

是的, Rust 实现...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Python Web Conf 2023](https://pycoders.com/link/10489/web)
    + March 13 to March 18, 2023

- [The Long White Computing Cloud](https://pycoders.com/link/10468/web)
    + March 15, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10478/web)  
    + March 15, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/10496/web)
    + March 16, 2023

- [PyLadies Dublin](https://pycoders.com/link/10477/web)
    + March 16, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/10476/web)
    + March 17 to March 18, 2023

- [PyCascades](https://pycoders.com/link/10498/web)
    + March 18 to March 20, 
    + 2023 in Vancouver, 
    + BC + Remote



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



```
            _~~+`~_
        \) /  - ◴  \ (/
          '_   ⌐   _'
          / '--.--' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 568 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-568.html)
- 修订: [issue-568.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-568.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF568D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF568D4Q90XdDA7g):



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



