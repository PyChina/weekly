Title: 蠎周刊(PyCoder)584
Slug: issue-584
Date: 2023-07-05 11:42
Tags: Weekly,Python,pycoders,ZH


> 第一位 PSF 常驻安全开发人员


原文: [PyCoder's Weekly - Issue #584](https://pycoders.com/issues/584)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230705 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230705 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------


- [为什么 Python 中 range() 的成员资格测试如此快？](https://pycoders.com/link/11062/web)
    + REAL PYTHON

In Python, range() is most commonly used in for loops. However, ranges have some other use cases too, as they share many properties with lists. In this tutorial, you’ll explore why it’s so fast to perform a membership test on a Python range.

(`是也乎:`

![range](https://ipic.zoomquiet.top/2023-07-05-zshot%202023-07-05%2015.10.48.jpg)

)


- [CPython、Pypy、MicroPython、Jython…有什么关系？](https://pycoders.com/link/11068/web)
    + BITE CODE

This comprehensive article introduces you to all the different ways you can Python. CPython isn’t the only choice, learn what else is out there and why you might choose an alternative.

(`是也乎:`

妯娌关系?

)

- [第一位 PSF 常驻安全开发人员](https://pycoders.com/link/11069/web)
    + SETH LARSON

Seth was recently hired as the first Security Developer-In-Residence at the PSF. His blog post talks about what his responsibilities are and how he defines success for the position.

- [PSF 董事会选举结果](https://pycoders.com/link/11053/web)
    + PYTHON SOFTWARE FOUNDATION

- [已发布 Django 安全版本：4.2.3、4.1.10 和 3.2.20](https://pycoders.com/link/11078/web)
    + DJANGO SOFTWARE FOUNDATION

- [FOSS United Conference Hyderabad, 印度主题征文](https://pycoders.com/link/11057/web)
    + INDIAFOSS.NET 
    + • Shared by Poruri Sai Rahul

- [PyLadies 会议（2023 年 12 月）招募志愿者](https://pycoders.com/link/11075/web)
    + PYLADIES.COM





-----------------------------------------
## 探讨/吐糟
> Discussions


- [Python 中的 TKinter：高级概念](https://pycoders.com/link/11054/web)
    + DAN KOLIS

(`是也乎:`

googlegroups 列表讨论线索页面...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [如何在 Python 中展平列表列表](https://pycoders.com/link/11064/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to flatten a list of lists in Python. You’ll use different tools and techniques to accomplish this task. First, you’ll use a loop along with the .extend() method of list. Then you’ll explore other tools, including reduce(), sum(), itertools.chain(), and more.


(`是也乎:`

![展平](https://ipic.zoomquiet.top/2023-07-05-zshot%202023-07-05%2014.57.32.jpg)

)


- [Jinja 模板](https://pycoders.com/link/11058/web)
    + REAL PYTHON 
    + COURSE

With Jinja, you can build rich templates that power the front end of your web applications. But you can use Jinja without a web framework running in the background. Anytime you want to create text files with programmatic content, Jinja can help you out.


(`是也乎:`

![Jinja](https://ipic.zoomquiet.top/2023-07-05-zshot%202023-07-05%2014.57.42.jpg)

)


- [估算 Wagtail 网站的排放量](https://pycoders.com/link/11047/web)
    + WAGTAIL.ORG 
    + • Shared by Thibaud Colas

This article describes quantifying the carbon footprint of websites built with Wagtail, the Python CMS, based on a dataset of 4,000 websites. Wagtail is looking at potential improvements that could be rolled out to a large number of projects.

(`是也乎:`

然后...收銭?

)


- [隐藏在 Python 标准库中的 CLI 工具](https://pycoders.com/link/11059/web)
    + SIMON WILLISON

There are several modules in Python that are directly callable from the command line, including the ability to gzip and pretty print JSON. This article introduces you to what is available and how Simon discovered them.


(`是也乎:`

问题是能力还行, 可是拿来编写自己的工具就困难了...

)

- [当 NumPy 太慢时](https://pycoders.com/link/11049/web)
    + ITAMAR TURNER-TRAURING

Sometimes just switching to NumPy just isn’t enough of a speed boost, what then? Before you contemplate parallelism, there are other approaches. This articles shows you other ways of improving performance.

(`是也乎:`

算法和代码值得优先优化...

)


- [弃用 bdist_egg 格式上传到 PyPI](https://pycoders.com/link/11072/web)
    + PYPI.ORG

PEP 715 has been accepted and as of August 1, 2023, the .egg format will no longer be accepted as an upload. Existing eggs on PyPI will remain in place.

- [机器学习系统设计：200 个案例研究](https://pycoders.com/link/11073/web)
    + EVIDENTLY AI

A collection of links to 200 different blog posts / case studies from leaders in the ML space. Learn how companies such as Netflix and Airbnb implement and use ML in their organizations.



- [用 Kubernetes SDK 自动化部署](https://pycoders.com/link/11067/web)
    + FAIZAN BASHIR 
    + • Shared by Faizan Bashir

Learn how to use the Python Kubernetes SDK to automate application deployments, including creating Kubernetes resources like deployments, services, secrets, config maps, and ingress.

(`是也乎:`

反正能不写 yaml 就嫑写...

)


- [用 collections.Counter 计算 Python 中的出现次数](https://pycoders.com/link/11051/web)
    + TREY HUNNER 
    + • Shared by Trey Hunner

Python’s collections.Counter objects are helpful for counting occurrences of iterable items. They’re especially helpful when paired with generator expressions.

(`是也乎:`


内置的好东西太多了,值得重新学习一下

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [polars-cookbook: 用 Python 的 Polars 库的技巧](https://pycoders.com/link/11074/web)
    + GITHUB.COM/ESCOBAR-WEST

- [symbex: 在 Python 中搜索要输出到 LLM 的符号](https://pycoders.com/link/11045/web)
    + GITHUB.COM/SIMONW

- [jupyterlab-theme-editor: Theme Editor for Jupyter
jupyterlab-theme-editor：Jupyter 的主题编辑器](https://pycoders.com/link/11071/web)
    + GITHUB.COM/JUPYTERLAB-CONTRIB

- [bark: 文本提示的生成音频模型](https://pycoders.com/link/11070/web)
    + GITHUB.COM/SUNO-AI

(`是也乎:`


神奇, 这下连接上声音也在提示工程范畴了, 不过, 有韩语 demo 没见中文的...

)


- [llama_index: 将您的LLM与外部数据连接起来](https://pycoders.com/link/11052/web)
    + GITHUB.COM/JERRYJLIU




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11061/web)
    + July 5, 2023

- [Sydney Python User Group (SyPy)](https://pycoders.com/link/11077/web)
    +July 6, 2023

- [Django Girls Abraka Workshop](https://pycoders.com/link/11050/web)
    + July 7 to July 8, 2023

- [DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/11060/web)
    + July 8, 2023

- [SciPy 2023](https://pycoders.com/link/11065/web)
    + July 10 to July 17, 2023




-----------------------------------------
## 历史上的这周


- 2022: [蠎周刊 PyCoder 532](https://weekly.pychina.org/issue/issue-532.html)
- 2021: [蠎周刊 479](https://weekly.pychina.org/issue/issue-479.html)
    + [pythonista-weekly : Pyw 506](https://weekly.pychina.org/python-weekly/pyw-506.html)
- 2020: [蠎周刊 426](https://weekly.pychina.org/issue/issue-426.html)
    + [pythonista-weekly : Pyw 456](https://weekly.pychina.org/python-weekly/pyw-456.html)
- 2019: [蠎周刊 375](https://weekly.pychina.org/issue/issue-375.html)
- 2018: [蠎周刊 324](https://weekly.pychina.org/issue/issue-324.html)
- 2017: [蠎加载 131](https://weekly.pychina.org/importpython/importpython-131.html)
- 2016: [蠎加载 80](https://weekly.pychina.org/importpython/importpython-80.html)
- 2015: [蠎周刊 173](https://weekly.pychina.org/issue/issue-173.html)
    + [蠎加载 39](https://weekly.pychina.org/importpython/importpython-39.html)
- 2014: [Issue 122](https://weekly.pychina.org/issue/issue-122.html)
- 2013: 空缺
- 2012: [Issue 21 One does not simply write a python script.](https://weekly.pychina.org/issue/issue-21.html)


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [@Chaos42DAMA - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + VLog
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊
- [LDS❤️💀🤖](LDS42.PODCAST.XYZ)
    + 播客:小宇宙
    + 收集各种嗯哼...



```
          _~^+~~_
      \) /  ☉ ^  \ (/
        '_   V   _'
        > '--+--' /

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 584 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-584.html)
- 修订: [issue-584.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-584.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF584D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF584D4Q90XdDA7g):



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



