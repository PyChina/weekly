Title: pythonista-weekly : Pyw 505
Date: 2021-06-25 16:25
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-505

### 欢迎阅读《pythonista周刊》第505期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-505](https://mailchi.mp/pythonweekly/python-weekly-issue-505)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**[
Get Your Weekly Dose of Programming](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)
A weekly newsletter featuring the best hand curated news, articles, tutorials, talks, tools and libraries etc for programmers. [Join For Free](https://www.programmerweekly.com/?utm_source=pwad&utm_medium=newsletter)

### 新闻


[Sonatype Catches New PyPI Cryptomining Malware](https://blog.sonatype.com/sonatype-catches-new-pypi-cryptomining-malware-via-automated-detection)
Sonatype has identified malicious typosquatting packages infiltrating the PyPI repository that secretly pull in cryptominers on the affected machines.

[DjangoCon US 2021 Call for Proposals](https://www.papercall.io/djangocon-us-2021)
DjangoCon US 2021 call for proposals for talks and tutorials is open until July 18, 2021.

[PyGotham TV Call for Proposals](https://cfp.pygotham.tv/)
As an online-only event, PyGotham TV talks will be pre-recorded, should be 10 or 25 minutes long, and will be presented in a single track.The call for proposals is open until June 30, 2021.

### 文章、教程与话题

[使用Python的动作识别识别手语](https://www.youtube.com/watch?v=doDUihpj6ro) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
想让你的手语模型更进一步吗？在这个视频中，你将学习如何利用动作检测来做到这一点! 你将能够利用一个关键点检测模型来建立一个关键点序列，然后将其传递给一个动作检测模型来解码手语 作为模型建立过程的一部分，你将能够利用 `Tensorflow` 和 `Keras` 来建立一个深度神经网络，利用 `LSTM `层来处理关键点序列。

[A from-scratch tour of Bitcoin in Python](https://karpathy.github.io/2021/06/21/blockchain/)
我们将用纯 `Python` 语言创建、数字签名和广播一个比特币交易，从零开始，并且没有任何依赖性。在这个过程中，我们将学到很多关于比特币如何代表价值的知识。让我们来了解一下。

[Subclassing in Python Redux](https://hynek.me/articles/python-subclassing-redux/)
子类和组合之间的冲突与面向对象编程一样古老。最新的一批语言，如 `Go` 或 `Rust`，证明了你不需要子类化来成功地编写代码。但是在 `Python` 中，具体来说，有什么实用的子类化方法呢？

[Django for Startup Founders](https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html)
为 `SaaS` 初创企业和消费者应用程序提供更好的软件架构。

[Hugging face Course](https://huggingface.co/course/chapter1)
本课程将教你使用 `Hugging Face` 生态系统的库-- `Transformers`、`Datasets`、`Tokenizers` 和 `Accelerate`--以及 `Hugging Face Hub`，了解自然语言处理（`NLP`）。它是完全免费的，没有广告。

[测量Python中的内存使用量：很棘手!](https://pythonspeed.com/articles/measuring-memory-python/)
在这篇文章中，你会学到。关于内存如何工作的一个简化但内容丰富的模型，两种衡量内存的方法--驻留内存和分配内存--以及如何在 `Python` 中衡量它们，以及两者之间的权衡。

[The best Python HTTP clients for 2021](https://www.scrapingbee.com/blog/best-python-http-clients/)
有大量可用于 `Python` 的 `HTTP` 客户端--在 `Github` 上快速搜索 "`Python HTTP`客户端 "会得到1700多个结果（！），你如何理解所有这些客户端并找到一个适合你的特定用例的客户端？在这篇文章中，我们将介绍目前可用于 `Python` 的五个最好的HTTP客户端，并详细说明为什么它们中的每一个都可以成为你考虑的对象。

[Usages of underscore](https://mathspp.com/blog/pydonts/usages-of-underscore)
了解下划线在 `Python` 中的用途，以及如何用它们编写更多的习惯性代码。

[Python Web Conf 2021 Videos](https://www.youtube.com/playlist?list=PLt4L3V8wVnF4iB8pGfkR7eozIJPwCM7vv) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
`Python Web Conf 2021` 的讲座和教程的视频现已发布。

[Protocol Types in Python 3.8](https://auth0.com/blog/protocol-types-in-python/)
快速介绍 `Python 3.8` 中新的 `Protocol` 类，以及它如何实现结构类型化。

[How to run Django applications with Docker](https://www.youtube.com/watch?v=UV55ehkX16A) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
这个视频是关于用 `Docker` 运行你的 `Django` 应用程序，这是一个完整的指南，在开发你的应用程序时，你的Django服务器会在每次你添加一些代码时自动同步。

### 有趣的项目、工具和库

[AugLy](https://github.com/facebookresearch/AugLy)
一个用于音频、图像、文本和视频的数据增强库。

[palanteer](https://github.com/dfeneyrou/palanteer)
用于 `C++` 和 `Python` 的高性能可视化剖析器、调试器和测试工具。

[pinout](https://github.com/j0ono0/pinout)
一个开源的 `Python` 软件包，可将硬件引脚图生成为 `SVG` 图像。

[gjf](https://github.com/yazeed44/gjf)
一个用于修复无效的 `GeoJSON` 对象的工具。

[Kats](https://facebookresearch.github.io/Kats/) 
在 `Python` 中进行时间序列分析的一站式服务。

[schwifty](https://github.com/mdomke/schwifty)
`schwifty` 是一个 `Python` 库，可以让你轻松地处理 `ISO` 规定的 `IBAN` 和 `BICs`。`IBAN` 是国际银行账户号码， `BIC` 是商业识别码。两者都是用于国际汇款的。

[auto-all](https://github.com/jongracecox/auto-all)
自动管理 `Python` 模块中的 `__all__` 变量。

[muttlib](https://github.com/MuttData/muttlib) 
一个包含辅助代码的库，用于启动一个与数据相关的项目。

[sierra](https://github.com/BrainStormYourWayIn/sierra)
`Sierra` 是一个轻量级的 `Python` 框架，用于构建和整合网络应用。

[ARTIF](https://github.com/CRED-CLUB/ARTIF)
一个先进的实时威胁情报框架，在IP信誉和历史数据的基础上识别威胁和恶意的网络流量。

[RLCard](https://github.com/datamllab/rlcard)
纸牌游戏中强化学习的工具包。

### 最近更新

[Python in Visual Studio Code – June 2021 Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-june-2021-release/)
该版本包括对 `VS Code` 的工作区信任的支持，使用 `PyTorch` 剖析器的 `Jump-To-Source` 代码以及使用 `Pylance` 的字典键的补全。

[Python 3.10.0b3 is available](https://pythoninsider.blogspot.com/2021/06/python-3100b3-is-available.html)

### 活动

[Virtual: PyData Montreal #20](https://www.meetup.com/PyData-MTL/events/278770112/) 
将会有以下话题:

- Small Big Data: using NumPy and Pandas when your data doesn't fit in memory
- Zero to Production-Ready: a best-practices process for Docker packaging


[Virtual: PyData Edinburgh July 2021](https://www.meetup.com/PyData-Edinburgh/events/278787661/)
在 `FreeAgent` 上将会有一个讲座，采用 `Amazon SageMaker` 进行机器学习。

[Virtual: PyData DC PyData DC](https://www.meetup.com/PyData-DC-Virtual/events/279002132/)
将会有一个讲座，《检测偏见和增加ML模型的透明度的开源工具》。


Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-505.html)
- 改进: [issue-505.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23505.md)

