Title: PyCoder 549
Slug: issue-549
Date: 2022-11-02 11:42
Tags: Weekly,Python,pycoders,ZH


> PyCon US 2023 开始召唤议题


原文: [PyCoder's Weekly - Issue #549](https://pycoders.com/issues/549)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221102 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221102 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [如何从 Python 列表或可迭代对象中获取第一个匹配项](https://pycoders.com/link/9790/web)
    + REAL PYTHON

In this tutorial you’ll learn about the best ways to get the first match from a Python list or iterable. You’ll look into two different strategies, for loops and generators, and compare their performance. Then you’ll end up by creating a reusable function for all your first matching needs.

(`是也乎:`

![First](https://ipic.zoomquiet.top/2022-11-02-zshot%202022-11-02%2008.59.29.jpg)
)


- [用 Pillow 生成模因/MEME和信息图表](https://pycoders.com/link/9783/web)
    + PIOTR MALIŃSKI

Pillow is great for doing image resizing, adding borders or composing. This makes it a natural fit for creating tools for memes and infographics. This step-by-step article shows you what Pillow code you need to write to turn any image into a meme.


(`是也乎:`


![MEME](https://ipic.zoomquiet.top/2022-11-02-zshot%202022-11-02%2009.01.50.jpg)

给定一张图,快速自动追加各种网络梗

)


- [什么时候应该升级到 Python 3.11?](https://pycoders.com/link/9773/web)
    + ITAMAR TURNER-TRAURING

Python 3.11 has been released, when should you switch to using it? This posting covers the complications you can run into when moving to the latest release of any Python and how to know when it is best for you to upgrade.


(`是也乎:`

很明显 Py 3.12.1 发布时

)


- [Python 3.12.0 Alpha 1 发布](https://pycoders.com/link/9776/web)
    + PYTHON.ORG

- [PyCon US 2023 提案征集开始](https://pycoders.com/link/9796/web)
    + PYCON.ORG

(`是也乎:`

PyCon22中国 刚刚开始主题召唤...



)




-----------------------------------------
## 探讨/吐糟
> Discussions


- [最爱哪个 Python 3.11 新功能?](https://pycoders.com/link/9777/web)
    + REAL PYTHON 
    + ON TWITTER

(`是也乎:`

先有吐糟说常用库不支持了...
然后: TOML as first class citizen,...

看来老爹回聘入 M$ 对 TOML 的江湖地位有极其重要的影响?


)


- [Python 3.11 比 3.8 快](https://pycoders.com/link/9798/web)
    + HACKER NEWS


(`是也乎:`

和 Python 1.3/2.7 相比呢?

)





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Django 应用程序中的缓存](https://pycoders.com/link/9780/web)
    + ESTHER VAATI

Caching can make a big difference in the performance of your application. This blog post describes how to apply caching to a Django project and what the benefits are. It is part 4 in a series with entries on Django performance improvement for the database, your code, and your front-end.

- [Python 3.11 中很酷的新功能](https://pycoders.com/link/9779/web)
    + REAL PYTHON
    + COURSE

In this video course, you’ll explore what Python 3.11 brings to the table. You’ll learn how Python 3.11 is the fastest and most user-friendly version of CPython yet, and learn about improvements to the typing system and to the asynchronous features of Python.


(`是也乎:`


![New](https://ipic.zoomquiet.top/2022-11-02-zshot%202022-11-02%2008.53.53.jpg)

网课的鮗不修养=>**跟热点**

毕竟学习冲动不是那么简单可以撞上的


)


- [Lambdas 不支持类型提示，但没关系](https://pycoders.com/link/9792/web)
    + ADAM JOHNSON

Python has no syntax to add type hints to lambdas, but that doesn’t mean you can’t use them in type-checked code. This post looks at how mypy can infer the types for lambdas, based on where they’re used.

(`是也乎:`

毕竟已经闭包了...

)



- [重新审视 12 个应用因子](https://pycoders.com/link/9793/web)
    + MAHDI YUSUF

The Twelve-Factor App methodology is a methodology for building software-as-a-service applications by Adam Wiggins. This article covers how it has evolved and what you can learn from it today.


(`是也乎:`


![Factor](https://ipic.zoomquiet.top/2022-11-02-zshot%202022-11-02%2008.46.29.jpg)


SaaS 没这么简单,只能一步步进化过来...

[The Twelve-Factor App （简体中文）](https://12factor.net/zh_cn/)
嗯哼? 居然已经翻译好了

)


- [Python 中简单、理智和明智的日志](https://pycoders.com/link/9795/web)
    + PETE FISON 
    + • Shared by Pete Fison

Get started with Logging in Python or deploy advanced, flexible loggers without the boiler-plate code. Learn all about log2d, a third-party wrapper for the Python logging library.


(`是也乎:`

S3 logging ?

```
log_success = Log("success", to_file=True)
log_success("log2d for the win!")
Log.success.critical("Alert! Alert!")

(Creates and updates ./success.log)
```

WoW 这真的就是一直想要的 logging.


)


- [PyCon US 2022 回顾和公告录制](https://pycoders.com/link/9769/web)
    + PYCON.BLOGSPOT.COM

This posting contains a recap of PyCon US 2022 along with links to their YouTube channel containing many of the talks from the conference.


(`是也乎:`

BLOGSPOT.COM -> 当年第一个国际 blog 平台,
没想到这么多年过去了居然和 googlegroups 一样,
还没被 google 单方删除.

)



- [如何在 Starlette 中设置 WebSockets](https://pycoders.com/link/9784/web)
    + SIDDHANT GOEL 
    + • Shared by Siddhant Goel

Starlette is a relatively new entrant to the world of Python web frameworks. This blog post talks about how you can set up (and test) a WebSocket backend using Starlette.


(`是也乎:`

`눈_눈`? 好象是那个当年输给 FastAPI 的 SCGI 框架?

)


- [应该在 Python 中使用自定义异常吗?](https://pycoders.com/link/9767/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

The article discusses whether or not to use custom exceptions in Python development. It shows how to create custom exceptions and when they can be useful.


(`是也乎:`

当前是 Yes & NOT;

如果在特殊场景中,使用自制拓展加强的微型DSL可以提高生产效能,当然值得上;
不过一但上了,对应程序猿提桶跑路可就惨了...


)





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [django-emoji: Django 应用网站上使用表情符号](https://pycoders.com/link/9775/web)
    + GITHUB.COM/GAQZI

- [pycopy: 轻量级 Python 方言](https://pycoders.com/link/9781/web)
    + GITHUB.COM/PFALCON

(`是也乎:`

和 Python 的关系,
如同 Scheme 和 Common Lisp...

所以,是对 Py3 以来越来越复杂的形式,叕开始了逆变?

不过,形式上, 的确没有哪个语言更加象 LISP 了.

)

- [inline-sql: 可内联到任何 Python 程序中的 SQL](https://pycoders.com/link/9791/web)
    + GITHUB.COM/EKZHANG

(`是也乎:`


```
from inline_sql import sql, sql_val

assert sql_val^ "SELECT 1 + 1" == 2

x = 5
assert sql_val^ "SELECT $x * 2" == 10

df = sql^ "SELECT * FROM (VALUES (1, 10), (2, 20)) df (x, y)"
assert sql_val^ "SELECT SUM(x) + SUM(y) FROM df" == 33
```

嗯哼? DBA 的 Python 之旅?

)


- [reals: 实数算术库](https://pycoders.com/link/9766/web)
    + GITHUB.COM/RUBENVANNIEUWPOORT


(`是也乎:`


![reals](https://ipic.zoomquiet.top/2022-11-02-zshot%202022-11-02%2009.09.54.jpg)

这个工程量其实不小...

)


- [absurd-django: Pyodide 实验中的 Django](https://pycoders.com/link/9785/web)
    + GITHUB.COM/PATRICK91





-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [STL Python](https://pycoders.com/link/9788/web)
    + November 2, 2022

- [NZPUG-Auckland: Crafting Software](https://pycoders.com/link/9771/web)
    + November 2, 2022

(`是也乎`:

当年好看薄创始人移民过去,
应该也会参加...

)


- [Heidelberg Python Meetup](https://pycoders.com/link/9770/web)
    + November 2, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9786/web)
    + November 2, 2022

- [PyCon PL 2022](https://pycoders.com/link/9768/web)
    + November 3 to November 7, 2022

- [PyCon Sweden](https://pycoders.com/link/9778/web)
    + November 3 to November 5, 2022




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅



-----------------------------------------
# PS:

- 首发: [Issue 549 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-549.html)
- 修订: [issue-549.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-549.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF549D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF549D4Q90XdDA7g):



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





