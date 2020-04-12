Title: pythonista-weekly : Pyw 444
Date: 2020-04-12 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-444

### 欢迎阅读《pythonista周刊》第444期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-444](https://mailchi.mp/pythonweekly/python-weekly-issue-444)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:**
使用 `Datadog` 监控你的python指标，日志，集群分析。使用`Datadog`的应用分析，可以深入任何纬度并且能找到你所需要的信息，来进行动态诊断和快速故障排除。[通过免费的Datadog APM试用版来提高应用程序性能。](https://www.datadoghq.com/dg/apm/ts-python-tracing/?utm_source=Advertisement&utm_medium=Advertisement&utm_campaign=PythonWeekly-Tshirt)

### 新鲜事

**[宣布一项新的 Python Packaging 赞助计划](https://pyfound.blogspot.com/2020/04/sponsoring-python-packaging.html)**

`Python` 软件基金会的 `Packaging` 工作组正在启动一个全新的赞助计划，来支持及改善 `Python` 的 `packaging` 生态。通过该计划筹集的资金将直接用于提升你的公司每天都在使用的工具，并维持 `Python Package Index` 的持续运营。通过这个计划，我们希望那些依赖 `Python`、封装工具生态系统以及 `PyPI` 的公司，来帮助我们构建一个牢固的基础以继续工作。



**[EuroPython 2020: CFP for the Online Event](https://blog.europython.eu/post/614296142774173696/europython-2020-cfp-for-the-online-event)**

由于我们之前是在举办线下会议的前提下开始举办了 `CFP`，而现在我们吧 `EuroPython 2020` 转为线上活动，我们将把 `CFP` 的时间再延长两周，直到 4 月 12 日，让每一个想参加这个新形式活动的人都有机会来提交会议提案。



### 文章、教程与话题

**[100% 声控 Halo](https://www.youtube.com/watch?v=Qy8PYfYoP6s) ![img](https://gallery.mailchimp.com/e2e180baf855ac797ef407fc7/images/8def3887-e9e9-4a48-95e0-74045a6a23fc.png)（9min）**

如何通过你的麦克风来控制你的鼠标键盘，完全由音量和音高控制。

> 让我想起了 八分音符酱
>
> 不过这个难度就更高了，锻炼声带的时候到了！

**[维持性能](https://tomaugspurger.github.io/maintaing-performance.html)**

和 `pandas` 文档说到的一样：`pandas` 提供了高性能的数据结构。但是我们如何验证说法是正确的？以及我们如何确保在很多版本中都是正确的？本文将介绍：1) `pandas` 目前监控性能的设置。 2) 我个人的用于理解和修复当发生性能下降的调试策略。



**[用户界面的模板](https://www.mattlayman.com/understand-django/templates-user-interfaces/)**

当你的 `Django` 应用用你的用户界面返回一个响应的时候，模版就是你用来制作用户界面的工具。这篇文章介绍了什么时候模版以及如何使用模版。



**[如何用 Libabigail 编写 ABI 规范性检查程序](https://developers.redhat.com/blog/2020/04/02/how-to-write-an-abi-compliance-checker-using-libabigail/)**

编写一个基于 `Python` 应用二进制接口 (ABI) 检查器来确保在 `Linux` 系统中共享库之间的向后兼容性。



**[在 Docker Compose 中构建 secrets，以安全的方式](https://pythonspeed.com/articles/build-secrets-docker-compose/)**

这篇文章演示了一种技术，可以允许你使用相同的 `Dockerfile` 既能使用 `secrets` 构建生产镜像又能使用 `Docker Compose` 轻松开发。



**[如何使用 pyenv 在 Mac 运行多个 Python 版本](https://opensource.com/article/20/4/pyenv)**

如果你需要使用一个你没有在 `macOS` 上安装的 `Python` 版本来运行一个项目，试试 `pyenv`。

> 环境管理之痛，一把辛酸泪。
>
> 工具太多太多。

**[用 Python NumPy 进行 Array Oriented](https://t.co/A36eU8Tb32)** 
Goodbye Plain, Old For-loops! Hello Numpy Arrays!

**[从 PyTorch 到 PyTorch Lightning — 一份面向所有人的介绍](https://t.co/BQvNafrdOX)**

这篇文章回答了关于一个最常见的问题，为什么你使用 `PyTorch` 时你需要 `Lightning` ？



**[用 Python 测试 S3 的 3 种方法](https://www.sanjaysiddhanti.com/2020/04/08/s3testing/)**

测试与外部系统（比如数据库或者 S3）交互的代码，需要付出更多的努力。然而，重要的业务逻辑经常都在这些代码中。这篇文章讲探讨 3 种在 `Python` 中测试 `S3` 的方法。



[Python 101 – Working with Strings](https://www.blog.pythonlibrary.org/2020/04/07/python-101-working-with-strings/)

[ pyproject.toml 到底是什么?](https://snarky.ca/what-the-heck-is-pyproject-toml)

[用 React 前端部署 Django 后端的3种方法](https://mattsegal.dev/django-spa-infrastructure.html)

[使用OpenCV和Python对人脸进行模糊化和匿名化](https://www.pyimagesearch.com/2020/04/06/blur-and-anonymize-faces-with-opencv-and-python/)

[在Python中重做StringIO的串联运算](https://lwn.net/SubscriberLink/816415/74bda9c0f1d7e55b/)

### 有趣的项目、工具和库

**[Whole-Foods-Delivery-Slot](https://github.com/pcomputo/Whole-Foods-Delivery-Slot)**

是的，在`COVID-19`还在的现在，试图获得`Whole Foods`和`Amazon Fresh`的送货时段可能会很麻烦。为了让你摆脱不断检查空位的麻烦（几乎永远找不到空位），这个自动脚本可以通知你（是的，口头通知你，这样你就可以去执行你的任务）新的送货空位何时开放。



**[CenterTrack](https://github.com/xingyizhou/CenterTrack)**

使用中心点同时检测和追踪物体。



**[audiomatch](https://github.com/unmade/audiomatch)**

一个小巧的命令行工具，用于发现相似的音频文件。



**[HIIT PI](https://github.com/jingw222/hiitpi)**

一款健身训练器 `Dash/Flask` 应用，通过分析来你的 `sweet Pi` 实时的视频流用机器学习和 `Edge TPU` 帮助追踪你的 `HIIT` 锻炼情况。



**[DeepMatch](https://github.com/shenweichen/DeepMatch)**

一个用于推荐一辑广告的深度匹配模型库。可以很简单地训练模型并导出用户和 `item` 的表示向量，并可以用于 `ANN` 搜索。



**[mplcyberpunk](https://github.com/dhaitz/mplcyberpunk)**
"Cyberpunk style" for matplotlib plots.

**[django-anon](https://github.com/Tesorio/django-anon)**

对生产数据进行匿名化，以便在不是非常安全的环境使用。



**[Throttler](https://github.com/uburuntu/throttler)**

支持 `Asyncio` 的简单调节器。



**[smartsnek](https://github.com/gigamarr/smartsnek)**

`Python CLI` 工具，用于查找单词定义。

Python CLI tool for looking up word definitions.

**[create-flask-service](https://github.com/amickael/create-flask-service)**

简单设置 `Flask` 微服务。

> 难得的脚手架～

**[NeRF-pytorch](https://github.com/yenchenlin/nerf-pytorch)**

`NeRF（Neural Radiance Fields）` 的 `PyTorch` 实现，可以重现结果。

**[chord](https://github.com/shahinrostami/chord)**
围绕着 `d3-chord` 的 `Python` 封装器。

**[2fa](https://gist.github.com/MineRobber9000/722a902f67bbd1a1c8c57f7ec0b5034e)**
用 `Python` 开发的双因素认证终端应用。

**[DeltaPy](https://github.com/firmai/deltapy/)** 
表格数据增强与特征工程。




### 那些活动

**[Virtual: Python Pizza Conference](https://remote.python.pizza/)**

`Python Pizza` 是由 `Python` 社区举办的微会议。



**[Virtual Nationwide Django Meetup](https://www.meetup.com/The-San-Francisco-Django-Meetup-Group/events/269878541/)**

旧金山 `Django Meetup` 将与全国各地的兄弟分会合作，于美国东部时间4月15日下午5点/东部时间8点举办首次全国性的虚拟 `Django` 聚会。我们将与纽约市和波士顿分会合作，提供引人入胜的节目。



**[Virtual: IndyPy Mixer Meetup: Data Structures](https://www.meetup.com/indypy/events/hwstlrybcgbsb/)**

将会有一个讲座，用 `112092` 次 `UFO` 目击事件来理解概率数据结构。

[Webinar: Creating a distributable software with basic Python skills](https://www.meetup.com/PyData-Madison/events/269151398/)

[Virtual: Edmonton Python Meetup April 2020](https://www.meetup.com/startupedmonton/events/dtflxjybcgbrb/)

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  

暂无。

----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！
>




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-444.html)
- 改进: [issue-444.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23444.md)


