Title: Issue 475
Slug: issue-475
Date: 2021-06-02 11:42
Tags: Weekly,Python,pycoders,ZH


> "硅谷"剧情变真...


原文: [PyCoder's Weekly - Issue #475](https://pycoders.com/issues/475)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210602 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210602 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [从卫星图像检测森林砍伐](https://pycoders.com/link/6439/web)
    + ANDRÉ FERREIRA

How would you go about detecting deforestation — a contributor to climate change — from satellite images? In this article, you’ll learn how one team built a machine learning (ML) solution to do just that, using FastAI for the modeling and Streamlit to create a dashboard. The article discusses methodology and results, and is a great read about building an ML solution. The project code is a available on GitHub.


(`是也乎:`

非常 Kaggle 式问题

)


- [用 conda 管理 Python 虚拟环境指南](https://pycoders.com/link/6451/web)
    + WHITEBOX

Learn everything you need to know to get up and running with conda for Python in this in-depth guide. You’ll learn how conda compares to pip, how to install conda, how to install Python and other languages using conda, how to manage conda environments, and even how to package conda environments for distribution.

(`是也乎:`

如果网络是通畅的,
conda 的模块管理比 PiPy 是好不少,
不过,呵呵...

)


- [用 plt.scatter() 可视化数据](https://pycoders.com/link/6466/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to create scatter plots in Python, which are a key part of many data visualization applications. You’ll get an introduction to plt.scatter(), a versatile function in the Matplotlib module for creating scatter plots.

(`是也乎:`

![plt](http://ydlj.zoomquiet.top/ipic/2021-06-02-ScreenShot%202021-06-02%2010.39.00.jpg)

可视化模块早已足够丰富了,
现在主要问题是:
大家都能绘制出相同范式图表,
但是,
PPT 专家要的是越来越3D/抓睛 的图表效果,
就看谁的可定制性深度了...

如果能通过142 个参数,
精细调节图表的所有细节是最好的,

当然更加好的是每年根据财报要求的格式,
将默认风格调整到 世界500强 日常会议中就使用的样式...


)


- [EuroPython 2021 会议列表已发布](https://pycoders.com/link/6459/web)
    + EUROPYTHON.EU

- [pipx 已是 PyPA 成员项目](https://pycoders.com/link/6446/web)
    + TWITTER.COM/PRADYUNSG

- [Python 3.10.0b2 可用](https://pycoders.com/link/6440/web)
    + CPYTHON DEV BLOG





-----------------------------------------
## 探讨/吐糟
> Discussions


- [为毛老爹说 Python 4.0 可能永远不会到来](https://pycoders.com/link/6476/web)
    + REDDIT

Redditors discuss Guido van Rossum’s thoughts on why he and the core development team aren’t thrilled about a Python 4 release.

(`是也乎:`

老爹才是营销高手哪...

其实, Python 又不是 Chrome 没有版本数 KPI,
就算是每半年升级一个版本,
用 Python 3.420 是很 COOL 的.


)



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks

- [如何迭代 DataFrame 数据行/ 值得这样做吗?](https://pycoders.com/link/6467/web)
    + MATT WRIGHT

How to iterate over pandas DataFrame rows is one of the top voted questions with the pandas tag on Stack Overflow. That question is also the most copied answer with a code block on the entire site. Clearly, lots of people want to iterate over the rows in a DataFrame. But should you do this, or are there better options?

(`是也乎:`

其实已经内部优化过了,
别自己折腾, 
用 Pandas 内置函式就好.

)



- [选择理想的数据结构并用 pass 和 with 展开](https://pycoders.com/link/6481/web)
    + REAL PYTHON 
    + podcast

How do you know you’re using the correct data structure for your Python project? There are so many built into Python and even more that are importable from the collections module. This week on the show, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects. We discuss a recent three-part video course on selecting the ideal data structure.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-06-02-ScreenShot%202021-06-02%2010.33.28.jpg)

)


- [用 Pandas 探索您的数据集](https://pycoders.com/link/6444/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn how to start exploring a dataset with Pandas and Python. You’ll learn how to access specific rows and columns to answer questions about your data. You’ll also see how to handle missing values and prepare to visualize your dataset in a Jupyter Notebook.


(`是也乎:`

![Dataset](http://ydlj.zoomquiet.top/ipic/2021-06-02-ScreenShot%202021-06-02%2010.32.37.jpg)


前提是当前数据集能加载到内存中,
否则 Pandas 简直了...

)


- [pyFLAC: Python 中的实时无损音频压缩](https://pycoders.com/link/6470/web)
    + JOE TODD

The Free Lossless Audio Codec, or FLAC, is the go-to compression algorithm for lossless audio. Learn how FLAC is used at Sonos, a company that makes connected speakers, and their newly open-sourced project PyFLAC that you can use for real-time lossless audio compression in Python.

- [Python News: 新闻：2021 年 5 月有什么新变化?](https://pycoders.com/link/6471/web)
    + REAL PYTHON

May 2021 was filled with important Python-related events. In this article, you’ll get a rundown of all the major happenings in the world of Python, including new versions of all six Pallets Projects core projects and, of course, PyCon US 2021.

(`是也乎:`


![News](http://ydlj.zoomquiet.top/ipic/2021-06-02-ScreenShot%202021-06-02%2010.30.49.jpg)


真蟒 的月刊;-)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [leafmap: 地理空间分析和交互式制图](https://pycoders.com/link/6478/web)
    + GITHUB.COM/GISWQS

- [pipx: 在隔离环境中安装和运行 Python 应用程序](https://pycoders.com/link/6448/web)
    + GITHUB.COM/PYPA


(`是也乎:`

叕一个 Python 模块隔离工具,
不过, 这个只是专注模块树管理, 
并不关心和当前项目环境的自动融合

)

- [pyFLAC: Python 中的实时无损音频压缩](https://pycoders.com/link/6464/web)
    + GITHUB.COM/SONOS


(`是也乎:`

硅谷 的剧情变成真实项目了...
![pyFLAC](http://ydlj.zoomquiet.top/ipic/2021-06-02-ScreenShot%202021-06-02%2010.25.39.jpg)

)


- [pynguin: Python 的单元测试生成器工具](https://pycoders.com/link/6433/web)
    + GITHUB.COM/SE2P

(`是也乎:`

可以自动生成合规的测试案例是刚需...

)


- [vaex: 用于 Python 的核外混合 Apache Arrow/NumPy DataFrame](https://pycoders.com/link/6468/web)
    + GITHUB.COM/VAEXIO




- [ray: 用于构建分布式应用程序的通用 API](https://pycoders.com/link/6488/web)
    + GITHUB.COM/RAY-PROJECT


(`是也乎:`

通用最吓人, 也最好用了...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6484/web)
    + June 2, 2020

(`是也乎:`

即便是线上的, 一样收费.

)



- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021


- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:
- 首发: [Issue 475 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-475.html)
- 修订: [issue-475.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-475.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



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
>> NN 4390


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28475fda9228.png?imageView2/2/w/475)






