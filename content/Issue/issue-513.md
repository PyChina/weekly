Title: PyCoder 513
Slug: issue-513
Date: 2022-02-22 11:42
Tags: Weekly,Python,pycoders,ZH


> 百倍加速 Python API 


原文: [PyCoder's Weekly - Issue #513](https://pycoders.com/issues/513)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220222 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [如何优化 Python API 服务器代码 100x](https://pycoders.com/link/8092/web)
    + VADIM MARKOVTSEV 
    + • Shared by Vadim Markovtsev

Tricks we used to speed up calls to our analytical API written in Python: asyncio, SQLAlchemy, asyncpg, Cython plugins, improved data structures, and replaced some Pandas with NumPy.


(`是也乎:`

在需要时...


![Optimized](https://ipic.zoomquiet.top/2022-02-23-zshot%202022-02-23%2009.55.26.jpg)

反正都是些祖传手艺,
在电脑只有1K内存时...

)


- [在 Python 类中提供多个构造函数](https://pycoders.com/link/8117/web)
    + REAL PYTHON

Learn how to provide multiple constructors in your Python classes, including: checking argument types, using default argument values, writing class methods, and implementing single-dispatch methods.


(`是也乎:`

![Multiple](https://ipic.zoomquiet.top/2022-02-23-zshot%202022-02-23%2009.52.00.jpg)


模式匹配哪, 这是函式语言基本能力, 在 Python 中也可以模拟出来了...

基于 `singledispatchmethod`

```
from datetime import date
from functools import singledispatchmethod

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise ValueError(f"unsupported date format: {birth_date}")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.date = birth_date

    @__init__.register(str)
    def _from_isoformat(self, birth_date):
        self.date = date.fromisoformat(birth_date)

    @__init__.register(int)
    @__init__.register(float)
    def _from_timestamp(self, birth_date):
        self.date = date.fromtimestamp(birth_date)

    def age(self):
        return date.today().year - self.date.year
```

)

- [将 Django 和 Postgres, Gunicorn, and Nginx 一起 Docker 起来](https://pycoders.com/link/8094/web)
    + MICHAEL HERMAN

Tutorial on configuring Django to run on Docker using Postgres, Nginx, and Gunicorn. All the ins-and-outs of Django in production.

(`是也乎:`

Docker 越来越象那个可以三步装入宇宙的冰箱了...

)



- [PEP 654 接受: Exception Groups](https://pycoders.com/link/8118/web)
    + PYTHON.ORG

New standard for grouping exceptions together

- [PSF 正在招聘构建 PyPI Features](https://pycoders.com/link/8090/web)    
    + PYTHON SOFTWARE FOUNDATION


(`是也乎:`

每年都发愿要解决的事儿...

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [如何从 Python 初学者到精通 Python?](https://pycoders.com/link/8085/web)
    + HACKER NEWS

(`是也乎:`

进入真实项目, 并快速完成, 再进入另外一个完全不同的项目

)


- [ Django 中最爱的功能或附加组件是什么?](https://pycoders.com/link/8087/web)
    + MIKE DRISCOLL

(`是也乎:`

admin 永远的 admin;
不过, 关联推荐给出很多神仙推荐:

> How to run your website for less than $6/year.

    Domain
    - Namecheap

    FREE Static Site hosting
    - Netlify
    - Vercel
    - Github Pages
    - Render
    - Firebase Hosting
    - Surge
    - Cloudflare pages

    Free DB
    - Supabase
    - Mongo Atlas

    FREE Backend
    - Netlify functions
    - Vercel
    - Google functions


)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python’s functools.wraps 装饰器的内部结构](https://pycoders.com/link/8119/web)
    + REDOWAN DELOWAR

The functools.wraps decorator keeps your function’s identity intact after it’s been wrapped by a decorator. Ever wondered how it works?





- [使用天气 API 绘制分形](https://pycoders.com/link/8099/web)
    + REAL PYTHON 
    + PODCAST

Have you been wanting to explore fractals and complex numbers in Python? Would you like to practice working with APIs in Python through a new project? This week on the show, Christopher Trudeau discusses a fresh batch of PyCoder’s Weekly articles and projects.


(`是也乎:`


![PODCAST](https://ipic.zoomquiet.top/2022-02-23-zshot%202022-02-23%2009.47.12.jpg)

)


- [希望开始使用 Python 时就知道的 10 个工具](https://pycoders.com/link/8112/web)
    + KEVIN YLU

Learn about how venvs, flake8, black, isort, pytest, commitizen, semantic-release, pre-commit hooks, and Github Actions work together!

(`是也乎:`

嗯哼?
每年都值得更新一批, 这种悔不当初的工具集,
不过, 如果从20年前开始用 Python 的话, 
又应该是什么呢?

)



- [为什么你不能反转 国旗表情符号 字符串?](https://pycoders.com/link/8101/web)
    + DAVID AMOS 
    + • Shared by David Amos

What’s the output of "🇺🇸"[::-1]? A deep dive into the world of Unicode and how Python reverses strings.

(`是也乎:`

eomji 党派

)


- [理解 Python 中的 Attributes, Dicts and Slots](https://pycoders.com/link/8113/web)
    + BAS STEINS

Python classes can have arbitrary attributes. How are they stored and how do they impact performance?


(`是也乎:`

是的, Python 中包含太多独有的 `糖` ,只是依赖正确的消化姿势...

)


- [游览 Python’s itertools Library](https://pycoders.com/link/8100/web)
    + MIKE DRISCOLL

Tour Python’s itertools module and learn about cycle(), groupby(), chain(), and more.


(`是也乎:`

叕一个 itertools 科普文,
其实, 使用这些内置函式可以提高生产效能,
问题是, 并不一定提高代码撰写效率...


)




- [Futures 简易并行化](https://pycoders.com/link/8102/web)
    + JAIME BUELTA

“Futures are a convenient abstraction in Python for running tasks in the background.”

(`是也乎:`

并发/迸发能力, 简直成为现代语言的基本操作素质了

)


- [Bite-Sized 重构](https://pycoders.com/link/8121/web)
    + RODRIGO GIRÃO SERRÃO

Wye refactoring your code is important and hints on what to look for.




- [用 Email-Validator 验证电子邮件地址](https://pycoders.com/link/8120/web)
    + DIMITRIJE STAMENIC

Using the email-validator library to validate an email address

(`是也乎:`

专项治理模块,
只是, 看是否支持 gmail 的 .+ 模式了

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [DevToys: 基于 Windows 的开发工具； JSON 格式化、文本比较、正则表达式…](https://pycoders.com/link/8086/web)
    + DEVTOYS.APP 
    + • Shared by Ian Currie


(`是也乎:`

![DevToys](https://ipic.zoomquiet.top/2022-02-23-zshot%202022-02-23%2009.31.41.jpg)

就是将各种流行免费小工具集成为一个软件来发售,
很可以了...

)


- [spyql: 使用类似 SQL 的 SELECT 和 Python 表达式的命令行数据查询数据工具](https://pycoders.com/link/8095/web)
    + GITHUB.COM/DCMOURA

- [ssort: Python 语句排序/组织你的代码](https://pycoders.com/link/8109/web)
    + GITHUB.COM/BWHMATHER

(`是也乎:`

这类直接改动源代码的工具,
其实对于工程管理可能有帮助,
但是, 对于程序猿自身可能是反作用.

)

- [Lurnby: 主动阅读和个人知识管理](https://pycoders.com/link/8097/web)
    + GITHUB.COM/ROZNOSHCHIK


(`是也乎:`


![Lurnby](https://ipic.zoomquiet.top/2022-02-23-zshot%202022-02-23%2009.24.09.jpg)


叕一个 PKM 方案, 
问题其实并没得到真正解决, 这些工具都是给私人一个构建私人资料网络的能力,
但是, 并没给予正确知识仓库维护的姿势...

)


- [tsfel: 时间序列特征提取库](https://pycoders.com/link/8104/web)
    + GITHUB.COM/FRAUNHOFERPORTUGAL

- [pz: 在命令行上混合使用 Python 和其他 Shell 命令](https://pycoders.com/link/8103/web)
    + GITHUB.COM/CZ-NIC

(`是也乎:`


    $ echo -e "example\nwikipedia" | pz 's += ".com"'
    example.com
    wikipedia.com

嗯哼? 这可是一直想拥有的管道能力哪...

)


- [nvelope: 用 Python 数据类定义 JSON 模式](https://pycoders.com/link/8114/web)
    + GITHUB.COM/MONOMONEDULA 
    + • Shared by Eddy G.






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ PyKla Monthly Meetup](https://pycoders.com/link/8083/web)
    + February 23, 2022

- [⋅ A Deep Dive Into Fairness in Machine Learning Using Fairlearn](https://pycoders.com/link/8084/web)
    + February 23, 2022

(`是也乎:`

活动名不短

)

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/8098/web)
    + February 23, 2022

- [⋅ PyStaDa](https://pycoders.com/link/8093/web)
    + March 2, 2022

- [⋅ Python Web Conference 2022 (Virtual)](https://pycoders.com/link/8091/web)
    + March 21 to March 25, 2022

(`是也乎:`

虽然欧洲已经准备停止 COVID-19 的感染统计,
但是...

)



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 513 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-513.html)
- 修订: [issue-513.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-513.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF513D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF513D4Q90XdDA7g):



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





