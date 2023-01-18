Title: PyCoder 560
Slug: issue-560
Date: 2023-01-18 11:42
Tags: Weekly,Python,pycoders,ZH


> PEP 703:将GIL变成一个开关选项


原文: [PyCoder's Weekly - Issue #560](https://pycoders.com/issues/560)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230118 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 230118 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [PEP 703: 在 CPython 中使 GIL 可选](https://pycoders.com/link/10176/web)
    + PYTHON.ORG

This PEP proposes changes to the CPython build process that would allow you to build a GIL-less interpreter. This kind of interpreter would not be ABI compatible with the GIL-based one, and the programmer would become responsible for some locking situations in C-extensions. If implemented, this would lead the way to being able to operate without the GIL in cases where backward compatibility issues are not important.

(`是也乎:`

嗯哼? 就象 Rust 中的 unsafe ?


)



- [Python 中的原型污染](https://pycoders.com/link/10174/web)
    + ABDULRAHEEM KHALED

Prototype pollution is a particular attack in JavaScript where the base Prototype object is modified having wide ranging effects. Unfortunately, similar things can be accomplished in Python by messing with __class__.__base__. Read on for details.


(`是也乎:`


Py 内部黑魔法, 如果不是撞上罕见问题一定要用这种解决方案,
一般没事别折腾...

)



- [从 2022 年最流行的 Python 教程和课程中学习](https://pycoders.com/link/10188/web)
    + REAL PYTHON

Revisit some of your favorite Real Python tutorials and video courses from 2022. It’s been a busy year, with new materials on topics ranging from the basics to web development, machine learning, effective coding environments, and more.

(`是也乎:`

去年构建的最受欢迎的一系列结构化教程

)


- [Python 3.12.0 Alpha 4 发布](https://pycoders.com/link/10197/web)
    + CPYTHON DEV BLOG




-----------------------------------------
## 探讨/吐糟
> Discussions


- [使用 code.interact() 在 Python 中调试](https://pycoders.com/link/10191/web)
    + TWITTER.COM/KARPATHY


(`是也乎:`

```
debugging in Python:
- `print()`s alone: too simple
- `import pdb; pdb.set_trace()`: too complex
- `import code; code.interact(local=locals())`: just right
simply drops you into interpreter, perfect for 95% of debugging

```

原文建议, 参考:
[Python Examples of code.interact](https://www.programcreek.com/python/example/715/code.interact)

[How To Debug Python with an Interactive Console | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-debug-python-with-an-interactive-console)

[code --- 解释器基类 — Python 3.11.1 文档](https://docs.python.org/zh-cn/3/library/code.html)

除了不能交互,其它基本上可以解决大部分观察要求了

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python Folium: 根据您的数据创建 Web 地图](https://pycoders.com/link/10172/web)
    + REAL PYTHON

You’ll learn how to create web maps from data using folium. The package combines Python’s data wrangling strengths with the data visualization power of the JavaScript library Leaflet. In this tutorial, you’ll create and style a choropleth world map that shows the ecological footprint per country.

(`是也乎:`


![Folium](https://ipic.zoomquiet.top/2023-01-18-zshot%202023-01-18%2009.12.32.jpg)

)


- [用 Polars 加速你的 DataFrame](https://pycoders.com/link/10177/web)
    + REAL PYTHON 
    + PODCAST

How can you get more performance from your existing data science infrastructure? What if a DataFrame library could take advantage of your machine’s available cores and provide built-in methods for handling larger-than-RAM datasets? This week on the show, Liam Brannigan is here to discuss Polars.


(`是也乎:`

![Polars](https://ipic.zoomquiet.top/2023-01-18-zshot%202023-01-18%2009.12.24.jpg)

)


- [我遵循的日志记录实践](https://pycoders.com/link/10184/web)
    + ELIRAN TURGEMAN

“No matter what kind of software you’re developing, you most definitely leverage logging to some extent, probably every single day.” This article outlines good cross-language logging practices making it easier to find bugs and understand what has happened in your software.

(`是也乎:`

0: 一定要用

1: 老实的用

2: 科学的用

)


- [相同的词，不同的含义](https://pycoders.com/link/10194/web)
    + NED BATCHELDER

One of the difficulties when comparing programming languages is that they sometimes use the same words to describe similar things, but always with differences. Sometimes the differences are large enough that we want to use different words, but often they are not.

(`是也乎:`

英文尽管已经尽力给所有概念都创建一个专用术语,
可惜, IT 行业习惯假借了...

所以, 计算机文档训诂学可能有必要发起

)


- [将 R 和 Python 与 {reticulate} 和 Quarto 相结合](https://pycoders.com/link/10196/web)
    + NICOLA RENNIE

Sometimes you might need to use R. Sometimes you might need to use Python. Sometimes you need to use both at the same time. This blog post shows you how to combine R and Python code using {reticulate} and output the results using Quarto.


(`是也乎:`

哈, 可怜的 R

)


- [用 Structlog 进行结构化日志记录](https://pycoders.com/link/10192/web)
    + MAXIMILIAN FILTENBORG

Structured logging is the idea of creating logs that are both human readable and easily machine parsable. This article introduces structured logging, its advantages, and the structlog package for Python.

(`是也乎:`

这是面向运营的日志了,
如果没有类似 ELK 的平台,
人眼看就难了..

)


- [来自地狱的 yaml 文件](https://pycoders.com/link/10198/web)
    + RUUD VAN ASSELDONK

As a data format, yaml is extremely complicated and it has many footguns. In this post Ruud explains some of those pitfalls by means of an example and suggests a few simpler and safer yaml alternatives.


(`是也乎:`

Docker 将 yaml 带到飞,
可惜太复杂了,手工撰写一定出错...
TOML 已经从另外一个方向开始了反超...

)



- [Django: 如何使用电子邮件登录用户](https://pycoders.com/link/10181/web)
    + CTRLZBLOG.COM 
    + • Shared by Alice Ridgway

Learn how to log users in with an email instead of a username with Django. This tutorial makes full use of Django’s built-in features to minimise custom code.

- [扫描 PyPI 并找到了 57 个实时 AWS 密钥](https://pycoders.com/link/10195/web)
    + TOM FORBES

Tom got stung by a leaked AWS key a while back and decided to go hunting. This article shows you how he scanned PyPI and just how many leaked keys he found.


(`是也乎:`

所以, 这种才是暗网主要经济来源?

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [nanoGPT: 训练 GPT 的存储库](https://pycoders.com/link/10180/web)
    + GITHUB.COM/KARPATHY

(`是也乎:`

GPT 变成热词后, 新项目名不带这个缩写简直就没有关注了...

)


- [用 Python 设计了一个键盘](https://pycoders.com/link/10193/web)
    + HSGW

- [fiftyone: 构建高质量数据集和计算机视觉模型](https://pycoders.com/link/10185/web)
    + GITHUB.COM/VOXEL51


(`是也乎:`

数据标注工厂基础设施...

)

- [PyChatGPT: 非官方 ChatGPT API 的 Python 客户端](https://pycoders.com/link/10189/web)
     GITHUB.COM/RAWANDAHMAD698

- [Neutron: 用 HTML 和 CSS 的 Python 跨平台应用程序](https://pycoders.com/link/10178/web)
    + GITHUB.COM/IANTERZO

(`是也乎:`

还是要手工编写 HTML,
和 Flet 们相比, 缺少生产力吸引哪

)



-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Python Meeting Düsseldorf](https://pycoders.com/link/10182/web)
    + January 18, 2023

(`是也乎:`

杜塞尔多夫（德语：Düsseldorf，德语：[ˈdʏsl̩dɔʁf] ），是德国北莱茵-威斯特法伦州首府，位于莱茵河畔。杜塞尔多夫市区人口约62万人，是德国广告、服装和通讯业的重要城市。
杜塞尔多夫也是19世纪德国诗人海因里希·海涅的出生地

)


- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/10173/web)
    + January 18, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/10199/web)
    + January 19, 2023

- [Python Northwest](https://pycoders.com/link/10190/web)
    + January 19, 2023

- [PyLadies Dublin](https://pycoders.com/link/10183/web)
    + January 19, 2023




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 560 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-560.html)
- 修订: [issue-560.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-560.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.

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

好文笔,感叹号年度配额: **0/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF560D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF560D4Q90XdDA7g):



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





