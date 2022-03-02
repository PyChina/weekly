Title: PyCoder 514
Slug: issue-514
Date: 2022-03-02 11:42
Tags: Weekly,Python,pycoders,ZH


> Numba 两行代码13x加速


原文: [PyCoder's Weekly - Issue #514](https://pycoders.com/issues/514)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 220302 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 220302 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------





- [Python’s 断言: 像专业人士一样调试和测试代码](https://pycoders.com/link/8164/web)
    + REAL PYTHON

Learn how to use Python’s assert statement to document, debug, and test code in development.


(`是也乎:`

![Assert](https://ipic.zoomquiet.top/2022-03-02-zshot%202022-03-02%2011.29.16.jpg)

)

- [如何从古腾堡项目同时下载多个书籍](https://pycoders.com/link/8163/web)
    + JASON BROWNLEE

Using threads to download multiple books from Project Gutenberg at the same time.

Troubleshoot Python Application Performance Errors Fast With Datadog’s end-to-end Tracing
Datadog’s APM generates detailed flame graphs to help you identify bottlenecks and latency in your code. Navigate seamlessly between Python application traces to relevant logs and metrics to troubleshoot and resolve the application error without switching tools or context. Try Datadog APM free →
DATADOGSPONSOR

- [用 Pandas, Seaborn and Ipywidgets 实现交互式可视化](https://pycoders.com/link/8149/web)
    + ZOLTAN GUBA

Creating interactive visual output using ipywidgets.

(`是也乎:`

其实动态影响的可视化没有多少应用场景,
一般政府大楼中的大数据屏,都不是触屏, 
而且也没有动机去改变什么参数...

)


- [PyPy v7.3.8 发布, 支持 Python 2.7, 3.7-3.9](https://pycoders.com/link/8162/web)
    + PYPY.ORG


(`是也乎:`


是的, 广大 Py 2.7 项目依然可以稳定使用

)


- [Python Core 将 Bug 追踪迁移入 Github](https://pycoders.com/link/8147/web)
    + PYTHON.ORG


(`是也乎:`

是的, 放弃了开源系统, 还是给有钱的 M$ 平台来追踪吧,
反正免费的.

)


- [Tomli TOML Parser 将进入 Python 3.11 Standard Library](https://pycoders.com/link/8157/web)
    + GITHUB.COM/HUKKIN 
    + • Shared by Markku Leiniö

(`是也乎:`


WoW 转正了...



    ------------------------------------------------------
        parser |  exec time | performance (more is better)
    -----------+------------+-----------------------------
         rtoml |    0.891 s | baseline (100%)
      pytomlpp |    0.969 s | 91.90%
         tomli |        4 s | 22.25%
          toml |     9.01 s | 9.88%
         qtoml |     11.1 s | 8.05%
       tomlkit |       63 s | 1.41%


等等,竟然不是 github 官方的?

)



-----------------------------------------
## 探讨/吐糟
> Discussions


- [如何用 Python 编写更好的科学代码 ?](https://pycoders.com/link/8134/web)
    + HACKER NEWS

Discussion about Oleg Żero’s article of the same name.

- [日志记录级别: 分配日志级别的经验法则](https://pycoders.com/link/8159/web)
    + STACK OVERFLOW

(`是也乎:`

流变, 看项目阶段..

)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [从 Python 中的线性回归开始...嗯哼](https://pycoders.com/link/8135/web)
    + REAL PYTHON 
    + COURSE

Linear regression is a statistical and machine learning technique, learn how to do it in Python.


(`是也乎:`

![Linear](https://ipic.zoomquiet.top/2022-03-02-zshot%202022-03-02%2011.22.38.jpg)

)


- [Python 异常值检测指南](https://pycoders.com/link/8136/web)
    + SADRACH PIERRE

Outlier detection is the process of identifying data points that have extreme values compared to the rest of the distribution. Python offers a number of packages for carrying this analysis out.

(`是也乎:`

测试边界值锚定技巧, 不过类似 Fuzzing 模块都能自动嗯哼出来了?

)


- [如何在 Windows 上使用 Python 的 Py Launcher](https://pycoders.com/link/8166/web)
    + SERDAR YEGULALP

“Take control of multiple Python installations in Windows with the py launcher, available as part of a standard Python installation.”


(`是也乎:`

简单来说, 用 docker/WSL 在一个正常的开发环境中用吧...

)


- [加入数据团队时要注意的危险信号](https://pycoders.com/link/8154/web)
    + EUGENE YAN

What to consider for in terms of the current data situation, roadmaps, role and expectations, tooling, and more.

(`是也乎:`

伪大数据项目识别技巧

)


- [如何将 Jupyter Notebook 部署到 Docker](https://pycoders.com/link/8142/web)
    + EDEM GOLD

What Docker is, why you should use it, and how to deploy a Jupyter notebook in a container.





- [三十分钟法则](https://pycoders.com/link/8143/web)
    + DANIEL ROY GREENFELD

What to do when you get stuck on a coding issue for more than 30 minutes.


(`是也乎:`

在蟒营®一直说 `42分钟` 法则,
完全一致的劝戒

)


- [NumPy 示例/ 45 个练习题](https://pycoders.com/link/8129/web)
    + JOHN LOCKWOOD

Practice questions to perfect your NumPy skills. Answer key available.

- [在 Python 中模拟从未如此简单](https://pycoders.com/link/8158/web)
    + PETER KOGAN 
    + • Shared by Peter Kogan

How to use Pytest’s Mock Generator to simplify your test writing.


(`是也乎:`

没错, 所以, 有趣的哪...

[pksol/pytest-mock-generator: A pytest fixture wrapper for https://pypi.org/project/mock-generator](https://github.com/pksol/pytest-mock-generator)

)


- [使用 Strava API 和 Python 进行马拉松训练分析](https://pycoders.com/link/8145/web)
    + CONAN MERCER

How to use the Strava API and Python to analyze race day data.



- [通过 Numba 加速 NumPy](https://pycoders.com/link/8130/web)
    + ITAMAR TURNER-TRAURING

Using Numba, a just-in-time compiler for NumPy arrays.

(`是也乎:`


NumPy 是 Pandas 的性能瓶颈, 所以...
)


- [测试弱引用](https://pycoders.com/link/8137/web)
    + PAUL GANSSLE

Testing when using weak-referenced objects.

(`是也乎:`

淦...多么痛的领悟...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code




- [blacken-docs: 在文档文件中的 Python 代码块上运行 black](https://pycoders.com/link/8140/web)
    + GITHUB.COM/ASOTTILE




- [codecat: 开源静态代码分析](https://pycoders.com/link/8138/web)
    + GITHUB.COM/COOLERVOID

(`是也乎:`

叕一个静态代码分析器,
最近火起来的 开发效能, 
都集中在各自代码分析结论基础上,



)


- [pyTermTk: Python 终端工具包, TUI 小部件库](https://pycoders.com/link/8133/web)
    + GITHUB.COM/CECCOPIERANGIOLIEUGENIO


(`是也乎:`



![pyTermTk](https://ipic.zoomquiet.top/2022-03-02-zshot%202022-03-02%2011.05.57.jpg)


猛烈哪, 几乎将 Tk 所有能力都迁移到 终端里来了

)


- [mercury: 将 Python Notebook 转换为 Web 应用程序的工具](https://pycoders.com/link/8150/web)
    + GITHUB.COM/MLJAR 
    + • Shared by Piotr

- [Python 项目实用书](https://pycoders.com/link/8160/web)
    + YASOOB.ME 
    + • Shared by Yasoob Khalid

(`是也乎:`

简直就是项目笔记...作者经历过的项目, 用过什么模块, 都整理出来了...

)


- [Cheat Sheets for Django Class-Based-Views](https://pycoders.com/link/8165/web)
    + CCBV.CO.UK




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ STL Python](https://pycoders.com/link/8153/web)
    + March 2, 2022

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/8152/web)
    + March 2, 2022

- [⋅ Sydney Python User Group (SyPy)](https://pycoders.com/link/8128/web)
    + March 3, 2022

- [⋅ Edmonton.py: The Edmonton Python User Group](https://pycoders.com/link/8168/web)
    + March 8, 2022

- [⋅ Python Web Conference 2022 (Virtual)](https://pycoders.com/link/8172/web)
    + March 21 to March 25, 2022



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅




-----------------------------------------
# PS:

- 首发: [Issue 514 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-514.html)
- 修订: [issue-514.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-514.md)


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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF514D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF514D4Q90XdDA7g):



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





