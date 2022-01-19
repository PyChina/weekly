Title: PyCoder 508
Slug: issue-508
Date: 2022-01-19 11:42
Tags: Weekly,Python,pycoders,ZH


> FastAPI 0.72.0 来也


原文: [PyCoder's Weekly - Issue #508](https://pycoders.com/issues/508)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220119 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220119 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [解析 “\[\]” 在 Python 中的嗯哼](https://pycoders.com/link/7853/web)
    + BRETT CANNON

“It’s quite possible you’re not familiar with this formal term, but you are probably familiar with the syntax: the square brackets used for indexing lists and tuples (sequence[4]), accessing the value of a specified dictionary (dictionary["key"]), etc. To cover this topic we will break up into three parts: general subscriptions, slicing, and multiple arguments.”

(`是也乎:`

老爹真的是在这对符号中玩出花儿了...


)


- [用 Pipenv 干活](https://pycoders.com/link/7848/web)
    + REAL PYTHON COURSE

Pipenv is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and requirements.txt. In this course, you’ll go over what problems Pipenv solves and how to manage your Python dependencies with it.


(`是也乎:`

![Pipenv](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2010.10.11.jpg)

)


- [70 行 Python 实现概率编程语言](https://pycoders.com/link/7835/web)
    + ANDREA COGNOLATO

Learn how Probabilistic Programming Languages (PPLs) work by building a simple one in Python.


(`是也乎:`


之前 50 行已经可以构造出不得了的东西了,现在 70行...

)


- [Python News: 2021 12月新鲜事儿?](https://pycoders.com/link/7857/web)
    + REAL PYTHON

The Python community elected its fourth steering council in December 2021. In this article, you’ll catch up on the results of the election as well as news about new maintenance releases of Python and about end-of-life for Python 3.6.





- [2021 年 Django 开发者调查结果](https://pycoders.com/link/7831/web)
    + DSF + JETBRAINS




- [FastAPI 0.72.0 发布](https://pycoders.com/link/7842/web)
    + TIANGOLO.COM

(`是也乎:`

叕一个永远不发布 1.0 的好东西

)



-----------------------------------------
## 探讨/吐糟
> Discussions



- [IPython 8 CLI 运行 “Black” 对 REPL Code 自动格式化](https://pycoders.com/link/7858/web)
    + RAYMOND HETTINGER

This Twitter thread explores concerns about using the IPython REPL with autoformatting enabled for education purposes and interactive math.

(`是也乎:`

恶心...不妥协的自动格式化, 对程序猿

)



- [谁人可解释清楚 _ 和 __ i?](https://pycoders.com/link/7838/web)
    + REDDIT

(`是也乎:`

情怀, 只是情怀...

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [Python 预发布和 Pip 缓存的测试问题](https://pycoders.com/link/7851/web)
    + SETH MICHAEL LARSON

“Pip was caching a wheel built using CFFI and Python 3.11.0-alpha2 and was installing that same wheel for the now Python 3.11.0-alpha3 both on our local machines and in our test suite. By clearing the pip cache on our machines and our CI we were able to get a passing test suite.”


(`是也乎:`

pip 为什么要缓存上?

)


- [和 Brett Cannon 聊如何解决 Python 启动/虚拟环境和锁定依赖项](https://pycoders.com/link/7830/web)
    + REAL PYTHON 
    + PODCAST

Would you like a simple command to launch your Python programs using v the newest version of the language installed on your machine? This week on the show, we continue our conversation with Brett Cannon. Brett discusses his project, the Python Launcher for Unix.

(`是也乎:`

![PODCAST](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2009.51.13.jpg)

运行时选择, 在 Python 一直是种幸福的苦恼, 选择太多, 这次又给出一堆值得对比体验的:
Flit,
pip-tools,
venv,
virtualenvwrapper ,
pdm ,
pyflow ,
pipenv,
python-wasm,
Pyodide ...

可能永远没有尽头...

)


- [用 Django 构建和提交 HTML 表单（4/4）](https://pycoders.com/link/7833/web)
    + REAL PYTHON

In the final part of this tutorial series, you’ll continue to build out a social network with Django. You’ll wrap up by working with Django forms, learning how to display helpful error messages, setting up dynamic URLs in your app, and more.

(`是也乎:`

![Django](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2009.50.23.jpg)

)


- [Pydbantic 数据验证和存储说明](https://pycoders.com/link/7840/web)
    + JOSHUA JAMISON 
    + • Shared by Joshua Jamison

Walk through the basics of pydbantic and discover how to create, query, update, and remove data from models. Review how pydbantic handles migrations after detecting any changes and how to integrate pydbantic with Redis for caching.

(`是也乎:`

叕一个专注数据关系自动调节的模块

)


- [在 iPad 上使用 Python 的 5 种方法](https://pycoders.com/link/7850/web)
    + DAVID AMOS 
    + • Shared by David Amos

“It turns out that it’s actually pretty easy to code in Python on the iPad, especially if you’re willing to work in Jupyter Notebooks. […] Here are five ways you can code in Python on any iPad right now.”


(`是也乎:`


其实还有中国原创的: [QPython](https://github.com/qpython-android)

)




- [Python 用 Cog 生成文本文件](https://pycoders.com/link/7843/web)
    + PODCAST.__INIT__ 
    + PODCAST


An interview with Ned Batchelder about the interesting history of the Cog project and how you can use it to automate the work of generating text with arbitrary Python code.


(`是也乎:`

![PODCAST](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2009.41.54.jpg)

理论上可以生成一切其它代码...


)


- [嫑用 functools.lru_cache 装饰器包装实例方法](https://pycoders.com/link/7829/web)
    + REDOWAN DELOWAR 
    + • Shared by Redowan Delowar

Wrapping instance method in Python suffers from one giant gotcha—class instances don’t get garbage collected properly. This post explores that.




- [用 Pandas 分析事件附近的股票数据](https://pycoders.com/link/7834/web)
    + MATT WRIGHT

Stock market returns are heavily impacted by some events, like FOMC announcements, and we can use Pandas to understand this impact.

- [What’s Your Favorite Programming Language?](https://pycoders.com/link/7828/web)
    + SLASHDATA LTD
    + SPONSOR

Take the Developer Nation survey, share your views and make an impact on the developer ecosystem. Plus, you get a chance to win cool prizes, licenses, gaming accessories, vouchers and many more.


(`是也乎:`

![SPONSOR](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2009.39.37.jpg)

赞助商的网页作的都很漂亮

)


- [用 SimpleNamespace 构造简单的模拟](https://pycoders.com/link/7854/web)
    + ADAM JOHNSON

“When testing Python code you may need a mock object. That’s okay! But what’s the best way to build a simple mock?”

- [自动文档化 Makefiles](https://pycoders.com/link/7861/web)
    + DANIEL ROY GREENFELD

(`是也乎:`

每个程序猿都有值得维护一生的 Makefile

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [av_hubert: 视听语音的自我监督学习框架](https://pycoders.com/link/7844/web)
    + GITHUB.COM/FACEBOOKRESEARCH

(`是也乎:`


淦, 根据口型, 自动识别并输出文字,
这是聋哑人的能力哪...

当然, 仅英文...
)


- [tplot: 终端中创建基于文本的图形](https://pycoders.com/link/7841/web)
    + GITHUB.COM/JEROENDELCOUR


(`是也乎:`


![tplot](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2009.34.28.jpg)

这是集成到 CLI 监察系统中关键能力,
问题只是, 有时, 想输出为文档就没闪和好办法,
原则上 Markdown 的代码引用就可以,

可惜, 等宽字体并不那么容易自动同步到领导浏览器上

)

- [mae: Masked 自动拼图的 PyTorch 实现](https://pycoders.com/link/7845/web)
    + GITHUB.COM/FACEBOOKRESEARCH

(`是也乎:`

![Masked](https://ipic.zoomquiet.top/2022-01-19-zshot%202022-01-19%2010.28.15.jpg)

)


- [python_communism: 对每个 Python 模块中发起 Communist Revolution](https://pycoders.com/link/7855/web)
    + GITHUB.COM/JOKTEUR

(`是也乎:`

击穿 类声明壁垒

)


- [teyit: Python 单元测试的格式化器](https://pycoders.com/link/7862/web)
    + GITHUB.COM/ISIDENTICAL

(`是也乎:`

讲真, 能格式化, 就应该能进一步自动生成了...

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ PyData Bristol Meetup](https://pycoders.com/link/7832/web)
    + January 20, 2022

- [⋅ Python Northwest](https://pycoders.com/link/7847/web)
    + January 20, 2022

(`是也乎:`

每次都感觉应该是 Northface

)

- [⋅ PyLadies Dublin](https://pycoders.com/link/7852/web)
    + January 20, 2022

- [⋅ MadPUG](https://pycoders.com/link/7863/web)
    + January 20 to January 21, 2022

- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/7849/web)
    + January 21, 2022





-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 508 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-508.html)
- 修订: [issue-508.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-508.md)


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

好文笔,感叹号年度配额: **0/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF508D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF508D4Q90XdDA7g):



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





