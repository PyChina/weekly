Title: PyCoder 541
Slug: issue-541
Date: 2022-09-07 11:42
Tags: Weekly,Python,pycoders,ZH


> 47+值得知道的 Py 字符串方法


原文: [PyCoder's Weekly - Issue #541](https://pycoders.com/issues/541)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220907 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220907 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [创建 Python 代码完成器和更多 AST 项目](https://pycoders.com/link/9456/web)
    + REAL PYTHON 
    + PODCAST

How does a code completion tool work? What is an Abstract Syntax Tree, and how is it created in Python? How does an AST help you write programs and projects that inspect and modify your Python code? This week on the show, Meredydd Luff, co-founder of Anvil, shares his PyCon talk, “Building a Python Code Completer.”

(`是也乎:`

![PODCAST](https://ipic.zoomquiet.top/2022-09-07-zshot%202022-09-07%2010.03.52.jpg)


AST 好东西

)



- [值得知道的 Python 字符串方法](https://pycoders.com/link/9431/web)
    + TREY HUNNER 
    + • Shared by Trey Hunner

Python’s strings have 47 methods. That’s almost as many string methods as there are built-in functions in Python! Which string methods should you learn first?

(`是也乎:`

和 Perl 类似,
字符串, 是日常最多应对场景,值得深入支持...

)




- [Python 中的龙曲线 🐍](https://pycoders.com/link/9445/web)
    + GIULIANO PERTILE 
    + • Shared by Giuliano Pertile

A Dragon Curve is a kind of fractal image. This article introduces you to the math behind the curve and how to draw one using a Python script.


(`是也乎:`


![Dragon](https://ipic.zoomquiet.top/2022-09-07-zshot%202022-09-07%2010.01.47.jpg)

龙式分形...supper cool.

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [还在购买/阅读技术书籍吗?](https://pycoders.com/link/9435/web)
    + HACKER NEWS

(`是也乎:`

Yes & Not,
有的是朋友出书, 下单支持...

)


- [推荐一个鲜为人知值得关注的图书馆?](https://pycoders.com/link/9441/web)
    + WILL MCGUGAN







-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [Python 开发人员拿来干活的 Gevent](https://pycoders.com/link/9440/web)
    + GEVENT COMMUNITY

This step-by-step tutorial runs you through the use of gevent, a Python concurrency library. It covers synchronous and asynchronous execution, determinism, timeouts, monkey-patching, and much more. It has also been translated into Italian and Japanese.

- [Python 包管理器大战](https://pycoders.com/link/9467/web)
    + PETER BAUMGARTNER

A performance based shootout for pdm, pip-tools, pipenv, and poetry. It compares installation, lock file processing, and the time to add and update packages. Speed isn’t everything for tool choice, but knowing the difference may help you choose.


(`是也乎:`

反正都离开不能官方 pip 工具, 本质上并无什么改进

)

- [为什么您的网站应小于 14kB](https://pycoders.com/link/9436/web)
    + NATHANIEL

Everyone knows that smaller sites load faster, but did you know specific limits can make a big difference? Due to how TCP works and packets are grouped, a 14kB page can load more than half a second faster than a 15kB page. Learn why.


(`是也乎:`


![14kB](https://ipic.zoomquiet.top/2022-09-07-zshot%202022-09-07%2009.26.55.jpg)

知道 14kB 法则后 应该作什么?

None

)


- [如何安装 Python 的预发布版本?](https://pycoders.com/link/9454/web)
    + REAL PYTHON

If you want to have a peek at what’s coming in the next stable version of Python, then you can install a pre-release version. In this tutorial, you’ll learn how to access the latest Python versions and help test them.


(`是也乎:`


![rcX](https://ipic.zoomquiet.top/2022-09-07-zshot%202022-09-07%2009.25.56.jpg)


这得看本地系统了...

)


- [一些提高调试能力的方法](https://pycoders.com/link/9433/web)
    + JULIA EVANS

A short summary of a couple of academic papers on how to improve your debugging skills, broken down into: learn the codebase, learn the system, learn your tools, learn strategies, and gain experience.


(`是也乎:`

其实吧, 还是多接触各种类型的工程, 在具体场景中调试不同 bug ,
才有经验积累

)



- [Jupyter Notebook 最糟糕的五件事](https://pycoders.com/link/9430/web)
    + DANIEL

Daniel talks about how, despite once loving Jupyter, things keep getting in his way. Read about the downsides of notebooks and why one data scientist is moving to other tools.

(`是也乎:`


哈, 终于有人受不了 Jupter 了,
不过, 最后一条并不成立, Docker 化早已完成的.

)



- [用 Python 在 Podcast 剧集中进行主题检测](https://pycoders.com/link/9463/web)
    + TONYA SIMS 
    + • Shared by Tonya Sims

This tutorial shows you how to transcribe a podcast using a speech-to-text Python SDK and derive a list of topics from it to quickly discover topics and meaning in text data.

- [请不要将 Python 作为工具来折腾](https://pycoders.com/link/9450/web)
    + BJØRN BORUD

This opinion piece talks about how dependency management and the lack of an executable make Python a problematic choice for writing tools.

(`是也乎:`

主要观点在嵌入式系统中, 
如果将构建软件的部分让渡给用户, 太痛苦,
应该能给出二进制成果软件出来, 这原本就是软件工程师的任务...

好吧, 嵌入式的世界不太清楚, 只知道资源受限,
这方面也有 miniPy 等工程在支持,

所以, 看口味了.

不过, 其中有个观点很认同, Perl 就是 Python 的前世

)





-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [ruff: 一个极快的 Python Linter，用 Rust 编写](https://pycoders.com/link/9468/web)
    + GITHUB.COM/CHARLIERMARSH

(`是也乎:`

毕竟 Python 的 AST 是 C 接口的...

![ruff](https://ipic.zoomquiet.top/2022-09-07-zshot%202022-09-07%2010.09.51.jpg)


)



- [django-airplane: 缓存 CDN 文件以进行离线编码](https://pycoders.com/link/9465/web)
    + GITHUB.COM/CLTRUDEAU

- [qt-async-threads: 在 Qt 中使用 Await 生成线程](https://pycoders.com/link/9437/web)
    + GITHUB.COM/NICODDEMUS 
    + • Shared by Bruno Oliveira

- [python-codext: 编码/解码任何东西](https://pycoders.com/link/9443/web)
    + GITHUB.COM/DHONDTA

(`是也乎:`

怪不得叫 codext

)


- [Regressio: 回归/插值和平滑库](https://pycoders.com/link/9446/web)
    + GITHUB.COM/BRENDANARTLEY






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [STL Python](https://pycoders.com/link/9458/web)
    + September 7, 2022

- [NZPUG-Auckland: Crafting Software](https://pycoders.com/link/9461/web)
    + September 7, 2022

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/9439/web)
    + September 7, 2022

- [PyCon SK 2022](https://pycoders.com/link/9466/web)
    + September 9 to September 12, 2022

- [PyBay 2022 Conference](https://pycoders.com/link/9447/web)
    + September 10, 2022 
    + in San Francisco

 (Use code realpython25 for 25% off)





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

- 首发: [Issue 541 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-541.html)
- 修订: [issue-541.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-541.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF541D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF541D4Q90XdDA7g):



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





