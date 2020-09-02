Title: Issue 435
Slug: issue-435
Date: 2020-08-26 11:42
Tags: Weekly,Python,pycoders,ZH


> 千万嫑在 下载 中运行Python


原文: [PyCoder's Weekly - Issue #435](https://pycoders.com/issues/435)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200826 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200826 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [用 Python 和 DVC 进行数据版本控制](https://pycoders.com/link/4731/web)
    + REAL PYTHON

In this tutorial, you’ll learn to use DVC, a powerful tool that solves many problems encountered in machine learning and data science. You’ll find out how data version control helps you to track your data, share development machines with your team, and create easily reproducible experiments!

(`是也乎:`

![DVC](http://ydlj.zoomquiet.top/ipic/2020-08-26-ScreenShot%202020-08-26%2011.29.26.jpg)

简单说, 就是将数据集的索引用 git 追踪,
数据集本身不用专门空间来管理...

![DVC](http://ydlj.zoomquiet.top/ipic/2020-08-26-ScreenShot%202020-08-26%2011.29.11.jpg)

如果 6G 普及后, 无论数据集在哪儿都可以比硬盘读取速度要快的下载,
那么, 也就不用这么折腾了...

)


- [深入研究 Python 官方 Docker 映像](https://pycoders.com/link/4723/web)
    + ITAMAR TURNER-TRAURING

Take a stroll through the Dockerfile for the official Python Docker image. Along the way you’ll see how the image uses a custom Python build and always includes the latest version of pip.



- [千万嫑在 下载文件夹 中运行Python](https://pycoders.com/link/4717/web)
    + GLYPH LEFKOWITZ

Learn about security issues that exploit how Python interacts with PATH and why you should always think twice about your current working directory.

- [Ask for Forgiveness or Look Before You Leap?](https://pycoders.com/link/4727/web)
    + SEBASTIAN WITOWSKI

Is it faster to “ask for forgiveness” or “look before you leap” in Python? And when is it better to use one over the other?

- [常见 Python 包错误](https://pycoders.com/link/4739/web)
    + JOHN WODDER

Learn about common mistakes made in creating and building a Python package and how to avoid them.




## 讨论
> Discussions


- [为什么 np.inf // 2 获得 NaN 而不是无穷大?](https://pycoders.com/link/4737/web)
    + STACK OVERFLOW

Wait, can you even divide infinity by anything?

(`是也乎:`

因为没有无限硬件...

)

- [俺的代码导致某些人失业, 感觉 Bad](https://pycoders.com/link/4740/web)
    + REDDIT

(`是也乎:`

c'est la vie (´-ι_-｀)

)



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks




- [Python mmap: 用内存映射 改进文件I/O](https://pycoders.com/link/4744/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use Python’s mmap module to improve your code’s performance when you’re working with files. You’ll get a quick overview of the different types of memory before diving into how and why memory mapping with mmap can make your file I/O operations faster.


(`是也乎:`

![mmap](http://ydlj.zoomquiet.top/ipic/2020-08-26-ScreenShot%202020-08-26%2011.18.05.jpg)


反正内存越来越大, 也就可以越来越任性了...

)


- [如何将所有人类知识放在一个盒子里?](https://pycoders.com/link/4725/web)
    + TESS MACCREA AND JUAN DIEGO CABALLERO 
    + • Shared by Tess McCrea

How to use the power of Cython to unlock the potential of both Python and C++, and help streamline the way that knowledge can be packaged and shared all over the world – even without the internet.

(`是也乎:`


![KIWIX](http://ydlj.zoomquiet.top/ipic/2020-08-26-ScreenShot%202020-08-26%2011.48.00.jpg)

竟然动用了 `希瑞` ...

用定制并发系统,将主要wiki 都拖下来变成 ZIM 格式文件,
用 Kiwix 浏览...

等等, 这难道不是 Kiwix ZIM reader 的广告?

)


- [用 AnyIO 在 Python 中进行结构化并发](https://pycoders.com/link/4721/web)
    + MATT WESTCOTT

One of AsyncIO’s weaknesses is that it doesn’t support structured concurrency, unlike competitive projects like Trio. That’s where AnyIO comes in!

- [恒定时间 LFU](https://pycoders.com/link/4730/web)
    + ARPIT BHAYANI

Caching is a popular way to improve application performance. The LRU strategy is popular, even though it is sometimes sub-optimal compared to the LFU strategy, because it has constant-time performance. However, you can improve LFU to get constant time performance, with some memory overhead as a trade-off.

- [为 Pythonista 曰 Rust, 第三部分: Python绑定](https://pycoders.com/link/4738/web)
    + DMITRY DYGALO 
    + • Shared by Dmitry Dygalo

In the third part of this series, you’ll learn how to add Python bindings to a Rust crate as well as test, package, and release a project to PyPI.

- [ETF 和卷积网络的市场预测](https://pycoders.com/link/4732/web)
    + GREGORY JANESH 
    + • Shared by Gregory Janesch

How well can convolutional neural networks and sector ETF data predict the direction of the Dow Jones Industrial Average in the future?

- [为促进机器人耕种, 对 Python 驱动 ML 工具需求在增加](https://pycoders.com/link/4742/web)
    + FINTECHDEMAND.COM

Robots driven by Python, PyTorch, and computer vision are being used to identify, map, and target weeds in a field, helping farmers increase yield and avoid widespread use of an herbicide. While this article is non-technical, it’s an interesting study of Python’s impact in the real world.




- [哪种编程语言最适合经济研究?](https://pycoders.com/link/4718/web)
    + ALVARO AGUIRRE 
    + AND JON DANIELSSON

The most widely used programming languages for economic research are Julia, Matlab, Python and R. Despite Python’s strengths, most notably its extensive ecosystem of packages, the authors settle on Julia as their preferred language.

(`是也乎:`

这种事儿, 不是看技术社区, 得看 华尔街 ...

所以, Julia 的硬广其实很无奈...
)


- [R 和Python: 数据科学动态二重奏](https://pycoders.com/link/4724/web)
    + ALEX WOODIE

The R language has seen a big comeback this summer, rising sharply in the TIOBE index. But the future of the relationship between R and Python is less about “R vs. Python” and more about “R and Python.”


(`是也乎:`

R 看 Python 一向是俯视的,
毕竟在高校中一直是 R 为正统,
不过, 上次在北大 RCon 上, 分享 Jupyter 体验后,
就知道, 这事儿, 看从哪个方向看了...

)


- [Python, Javascript, R 和 Julia 对 GDP 有贡献数十亿美元](https://pycoders.com/link/4726/web)
    + DAN KOPF

Open-source programming languages, which are incredibly valuable, are not well accounted for in economic statistics. How much economic value do you think Python has?

(`是也乎:`

GDP 和技术当然有关联,
只是如何关联以及核算, 一直没什么公认的好办法...

等等, 为什么 Julia 也掺合进来了?

)





    
## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [newspaper: Python 3 中的新闻/全文和文章元数据提取](https://pycoders.com/link/4719/web)
    + GITHUB.COM/CODELUCAS

(`是也乎:`

web 1.0 时代好工具,
也支持中文,
只是目标网站本身得足够良构哪.

)


- [anyio: 用于多个异步事件循环实现的高级兼容性层](https://pycoders.com/link/4747/web)
    + GITHUB.COM/AGRONHOLM

- [mccabe: 适用于 Python 的 McCae 复杂度检查器](https://pycoders.com/link/4741/web)
    + GITHUB.COM/PYCQA

- [databay: 用于规划数据传输的 Python 接口](https://pycoders.com/link/4728/web)
    + GITHUB.COM/VOYZ

- [strawberry: Python 的 GraphQL 库](https://pycoders.com/link/4735/web)
    + GITHUB.COM/STRAWBERRY-GRAPHQL

(`是也乎:`

士多啤梨...

![strawberry](http://ydlj.zoomquiet.top/ipic/2020-08-26-ScreenShot%202020-08-26%2011.19.36.jpg)

)


- [present: 具有色彩和效果的 终端幻灯片工具](https://pycoders.com/link/4722/web)
    + GITHUB.COM/VINAYAK-MEHTA 
    + • Shared by Vinayak Mehta


(`是也乎:`

基于 asciimatics 构造的终端幻灯工具,
之前用过几种, 
都不错, 唯一问题是无法简单的发布到网络中,
不如 Pandoc 可以编译出 H5 形式的幻灯来.

)



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon Japan 2020 ](https://pycoders.com/link/4692/web)
    + (Online Conference)
    + August 28 to August 30, 2020


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



101camp12py 即将开始报名

![报名](http://ydlj.zoomquiet.top/ipic/2020-08-26-200816-reg-zip.jpg)

```

课程规划:

    发布报名 2020.08.31
    报名截止 2020.09.21
    正式开课 2020.09.27
    课程结束 2020.11.08

```
详情 => [蟒营™ Python 入门班第12](https://py.101.camp/)


# PS:
- 首发: [Issue 435 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-435.html)
- 修订: [issue-435.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-435.md)


-------------

好文笔,感叹号年度配额: **1/3**

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
>> NN 4117


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/435)






