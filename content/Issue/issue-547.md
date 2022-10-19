Title: PyCoder 547
Slug: issue-547
Date: 2022-10-19 11:42
Tags: Weekly,Python,pycoders,ZH


> Pythoneer 2022调查问卷来了, 值得冲哪...


原文: [PyCoder's Weekly - Issue #547](https://pycoders.com/issues/547)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 221019 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 221019 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [ChatterBot: 用 Python 构建聊天机器人](https://pycoders.com/link/9708/web)
    + REAL PYTHON

Chatbots can help to provide real-time customer support and are a valuable asset in many industries. When you understand the basics of the ChatterBot library, you can build and train a self-learning chatbot with just a few lines of Python code.


(`是也乎:`

![ChatterBot](https://ipic.zoomquiet.top/2022-10-19-zshot%202022-10-19%2008.31.29.jpg)

)


- [为数据和机器学习流水线编写健壮的测试](https://pycoders.com/link/9723/web)
    + EUGENE YAN

This deep article talks about why some kinds of tests break more frequently than others and how to set the appropriate granularity of your test suites.

Migrating Postgres From Heroku to Crunchy Bridge
Developers of a growing business were looking to migrate Postgres. They wanted a new vendor at least as good at Heroku, with new features and developer tools. They tested Amazon RDS and several others. Find out why they chose Crunchy Bridge for their cloud Postgres. Read the case study →
CRUNCHY DATASPONSOR

- [在 Python 中使用 LaTeX](https://pycoders.com/link/9714/web)
    + JOHN LOCKWOOD

Python has great support for LaTeX: in Jupyter, in symbolic math tools, and in third party libraries. Learn about how easy it is to get started.

- [2022 年 Python 开发者调查](https://pycoders.com/link/9721/web)
    + PYTHON SOFTWARE FOUNDATION

- [Python 3.10.8 错误修复版发布](https://pycoders.com/link/9698/web)
    + PYTHON.ORG






-----------------------------------------
## 探讨/吐糟
> Discussions

- [这几年最好的编程书籍？](https://pycoders.com/link/9712/web)
    + HACKER NEWS


(`是也乎:`

不是出版社引战文,
SQLite 以及 The Rust Programming Language ISBN-13: 9781718500440
得到关注...

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [在 Python 类中搞多个构造函数](https://pycoders.com/link/9724/web)
    + REAL PYTHON COURSE

In this video course, you’ll learn how to provide multiple constructors in your Python classes. To this end, you’ll learn different techniques, such as checking argument types, using default argument values, writing class methods, and implementing single-dispatch methods.

(`是也乎:`


![Providing](https://ipic.zoomquiet.top/2022-10-19-zshot%202022-10-19%2008.29.29.jpg)
)


- [Python 集合终极指南](https://pycoders.com/link/9725/web)
    + JACOB FERUS

“The set class is one of the key data structures in Python. It is an unordered collection of elements without duplicates. It represents, to a certain degree, a mathematical set, and many of the common mathematical operations for sets exist in Python.”


(`是也乎:`

Ultimate ~ 究极...
古早潮词儿

)


- [通过自动重构追加类型注释](https://pycoders.com/link/9705/web)
    + JIMMY LAI

Jimmy’s team at Carta decided they wanted to add type annotations to their large code base, but doing so manually would have taken a very long time. This post shows you how they built automated refactoring tools to add type annotations to their code.

(`是也乎:`

实战来了...

受了不了...

)


- [Python 类型提示: 朋友、敌人还是只是头疼?](https://pycoders.com/link/9715/web)
    + MARCIN KOZAK 
    + • Shared by Marcin

You can use type hinting to increase code readability, but you must do it wisely. Type hints can make things better, or they can be misleading and decrease code readability. Marcin offers suggestions on how to use type hints for clearer code.

- [在 Django 中接受文件](https://pycoders.com/link/9700/web)
    + MATT LAYMAN

Maybe your app needs to handle files from users like profile pictures. Accepting files from others is tricky to do safely. See the tools that Django provides to manage files safely.

- [装饰器快捷方式](https://pycoders.com/link/9710/web)
    + NED BATCHELDER

“When using many decorators in code, there’s a shortcut you can use if you find yourself repeating them. They can be assigned to a variable just like any other Python expression.”

(`是也乎:`


```
# in helpers.py
xfail_pypy_3749 = pytest.mark.xfail(
    env.PYVERSION[:2] == (3, 8) and env.PYPY and env.PYPYVERSION >= (7, 3, 10),
    reason="Avoid a PyPy bug: https://foss.heptapod.net/pypy/pypy/-/issues/3749",
)

...


# in src.

from tests.helpers import xfail_pypy_3749

@xfail_pypy_3749
def test_something():
    ...

@xfail_pypy_3749
def test_something_else():
    ...
```

好吧, 这才是魔术...


)



- [从任意网站摄取任意公共数据的 13 种方法](https://pycoders.com/link/9702/web)
    + DMITRIY ZUB

There are many libraries for scraping and parsing from web content out there. This guide shows you several different techniques and why you would choose from among them.

(`是也乎:`

现在这堆工具, 到 WASM 流行时, 是否可用?

)



- [10 个 Python 迷你自动化项目](https://pycoders.com/link/9699/web)
    + HAIDER IMTIAZ

Automate some common tasks, such as: sending email, converting PDF to audio with text-to-speech, get weather information, and seven more.






-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [red-box: 下一代邮箱管理器](https://pycoders.com/link/9709/web)
    + GITHUB.COM/MIKSUS

(`是也乎:`

古老的需求...

)

- [pyscript 现在有 REPL 了](https://pycoders.com/link/9703/web)
    + PYSCRIPT.NET


(`是也乎:`


当然 Jupter 风格...

)

- [panel: Python 高级应用程序和仪表板解决方案](https://pycoders.com/link/9728/web)
    + GITHUB.COM/HOLOVIZ




- [fpdf2: 极简 PDF 创建库](https://pycoders.com/link/9716/web)
    + PYFPDF.GITHUB.IO

- [zython: 用于服务器和浏览器的 WebAssembly Python](https://pycoders.com/link/9717/web)
    + GITHUB.COM/SAGEMATHINC


(`是也乎:`

叕一个 WASM.py 

![zython](https://ipic.zoomquiet.top/2022-10-19-zshot%202022-10-19%2008.11.55.jpg)

居然还用上了 Zig 

)




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9704/web)
    + October 19, 2022

- [PyData Bristol Meetup](https://pycoders.com/link/9707/web)
    + October 20, 2022

- [PyLadies Dublin](https://pycoders.com/link/9718/web)
    + October 20, 2022

- [MadPUG](https://pycoders.com/link/9727/web)
    + October 20 to October 21, 2022

- [Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/9713/web)
    + October 21, 2022

- [Chattanooga Python User Group](https://pycoders.com/link/9726/web)
    + October 21 to October 22, 2022






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

- 首发: [Issue 547 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-547.html)
- 修订: [issue-547.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-547.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF547D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF547D4Q90XdDA7g):



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





