Title: pythonista-weekly : Pyw 457
Date: 2020-07-12 14:22
Tags: Weekly,pythonweekly,Zh 
Slug: pyw-457

### 欢迎阅读《pythonista周刊》第457期。Let us start!


>原文: [https://mailchi.mp/pythonweekly/python-weekly-issue-457](https://mailchi.mp/pythonweekly/python-weekly-issue-457)  
>翻译：Dustyposa

**来自赞助商（PS：原文的赞助商）:** 

作为 `Python` 开发人员，你知道编写干净，安全的 `Python` 代码对您和您的用户很重要。 `SonarQube` 通过功能强大，快速且准确的静态代码分析使开箱即用的 `Python` 开发变得更加轻松。 [Register now to see for yourself in a live webinar on July 16th!](https://sonarsource.zoom.us/webinar/register/3615925068190/WN_rvO_CmpfRKigFBRue0NNCg)



### 新鲜事

[如何使用吉他编程](https://www.youtube.com/watch?v=4rbp83fJTkg) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)（7min）
学习如何用吉他......而不是键盘来编程。使用一些自定义的 `Python` 代码和一些其他插件，作者已经创建了一些东西，将原始的吉他信号变成键击。在吉他上用 `Python` 编程听起来像什么？什么时候你可以扔掉你的键盘来做这样的东西？

[Python and Go : Part II - 用 Go 扩展 Python](https://www.ardanlabs.com/blog/2020/07/extending-python-with-go.html)
在这篇文章中，我们将通过在 `Go` 中编写一个 `Python` 程序可以直接使用的共享库来降低使用 `gRPC` 的复杂性。 采用这种方法，无需进行任何网络连接，也无需依赖数据类型，也无需编组。 在使用 `Python` 共享库调用函数的几种方法中，我们决定使用 `Python` 的 `ctypes` 模块。

[Putting More Buzz in Your Python Fizz](https://www.capitalone.com/tech/software-engineering/fizz-buzz-python-type-hints/)
关于类型提示如何改进代码的四个过度工程的示例。

[用 Flask 处理文件上传](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
本文介绍了如何为 `Flask` 服务器实现强大的文件上传功能，该功能与 `Web` 浏览器中的标准文件上传支持以及很酷的基于 `JavaScript` 的上传小部件兼容。

[Multiple User Types in Django](https://www.youtube.com/watch?v=f0hdXr2MOEA) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
学习如何用 `Django` 以可维护的方式实现多种用户角色。

[Interfaces, Mixins 在 Python 中构建强大的自定义数据结构。](https://rednafi.github.io/digressions/python/2020/07/03/python-mixins.html)
增强 `Python` 的内置数据结构。   

[Fighting Coronavirus with AI](https://blog.paperspace.com/fighting-coronavirus-with-ai-building-covid-19-classifier/)
这是一个使用 `PyTorch` 从胸部 `CT` 扫描建立 `COVID-19` 分类器的分步教程。

[用这个RTOS的VSCode插件，用Python对物联网系统进行编程。](https://opensource.com/article/20/7/python-rt-thread)
像 `RTOS` 这样的实时嵌入式操作系统可以让嵌入式系统的编程变得更加简单。

[2019年YouTube热门视频分析（美国）](https://ammar-alyousfi.com/2020/youtube-trending-videos-analysis-2019-us)
对 `2019` 年全年所有热门视频进行分析（超过7万条视频）。标题，描述，缩略图，标签，浏览量，喜欢/不喜欢，和评论都被分析，以产生本文章中显示的结果。

[Introducing iommi](https://www.youtube.com/watch?v=8IwAlM9lVZc) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)
这是对 `iommi` 的介绍，它是一个基于 `Django` 的框架，它可以根据你的应用模型神奇地创建页面、表单和表格，并提供先进的开箱即用的功能，而不会牺牲灵活性和控制力。

[Deploying Django+React+Nginx to DigitalOcean with Ansible](https://www.rrebase.com/posts/deploying-knboard-to-digitalocean-with-ansible)
本文将带你了解 `Django+React+Nginx` 应用部署到 `DigitalOcean` 的过程。`Ansible` 和 `Docker` 的结合，使其成为一个优秀的自动化部署过程。

[Flask项目设置。TDD、Docker、Postgres等。](https://www.thedigitalcatonline.com/blog/2020/07/05/flask-project-setup-tdd-docker-postgres-and-more-part-1/)
一个 3 部分的系列，向你逐步展示如何使用 `TDD、Docker和Postgres` 设置一个Flask项目。请看 [part 2](https://www.thedigitalcatonline.com/blog/2020/07/06/flask-project-setup-tdd-docker-postgres-and-more-part-2/) and [part 3](https://www.thedigitalcatonline.com/blog/2020/07/07/flask-project-setup-tdd-docker-postgres-and-more-part-3/).

[Django和Nginx中无效的HTTP_HOST头错误。](https://www.borfast.com/blog/2020/07/06/invalid-http_host-header-errors-in-django-and-nginx/)
你是否有一个在 `Nginx` 后面运行的 `Django` 应用，即使你已经正确配置了 `ALLOWED_HOSTS`，但还是收到了很多无效的 `HTTP_HOST` 头错误？这是个很常见的问题，但修复起来也很简单。

[Serverless Web Apps in Python](https://www.sanjaysiddhanti.com/2020/07/05/serverless/)
在 `AWS Lambda` 上部署 `Python` 网络应用的实践指南。

[The Stable Marriage Problem and Modern Dating](https://www.arvarik.com/the-stable-marriage-problem-and-modern-dating)
尝试用稳定婚姻问题的经验来模拟现代交友的模式

[Flatter wait-free hazard pointers](https://pvk.ca/Blog/2020/07/07/flatter-wait-free-hazard-pointers/)
这篇文章展示了如何通过一点工程技巧将这个抽象平坦化，变成一些实用的东西，并拿出免等待的替代方案来替代通常的无锁危险指针，这些替代方案在最佳情况下是有竞争力的。 `Blelloch` 和 `Wei` 的见解是，危险指针可以使用任何免等待的原子内存-内存拷贝，这让我们可以在不影响普通情况下改进最坏情况！这也是我们的一个优势。

[SlicerJupyter: a 3D Slicer kernel for interactive publications](https://blog.jupyter.org/slicerjupyter-a-3d-slicer-kernel-for-interactive-publications-6f2ad829f635)
使用 `Jupyter` 和 `3D Slicer` 内核在笔记本上实现生物医学数据处理工作流程。

[Zen Guardian](https://glyph.twistedmatrix.com/2020/07/zen-guardian.html)
Let’s rewrite a fun toy Python program - in Python!

[Weaponizing favicon.ico for BugBounties , OSINT and what not](https://t.co/XT5sQnN7BT)

[FlaskCon 2020 Videos](https://www.youtube.com/playlist?list=PL-MSuSC-Kjb45rrRGL6gWGn6gv35O1mC1) ![img](https://mcusercontent.com/e2e180baf855ac797ef407fc7/images/af76283a-6e65-436c-967a-900427cf6399.png)

[Django Testing Toolbox](https://www.mattlayman.com/blog/2020/django-testing-toolbox/)

[Massive memory overhead: Numbers in Python and how NumPy helps](https://pythonspeed.com/articles/python-integers-memory/)

[Python 101 – Debugging Your Code with pdb](https://www.blog.pythonlibrary.org/2020/07/07/python-101-debugging-your-code-with-pdb/)

[Huey作为Django的最小任务队列](https://www.untangled.dev/2020/07/01/huey-minimal-task-queue-django/)



### 有趣的项目、工具和库


[EyeLoop](https://github.com/simonarvin/eyeloop) 
`EyeLoop` 是一款基于 `Python 3` 的眼动追踪器，专门为消费级硬件上的动态闭环实验量身定做。

[Dataprep](https://github.com/sfu-db/dataprep) 
`Dataprep` 让你只需几行代码就可以使用一个库来准备你的数据。

[inquest](https://github.com/yiblet/inquest)
`Inquest` 可以让你在不重启 `python` 实例的情况下向 `python` 添加日志语句。它可以帮助你快速发现问题所在。

[rat-sql](https://github.com/microsoft/rat-sql)
从英语到 `SQL` 的关系感知语义解析模式。

[Sweetviz](https://github.com/fbdesignpro/sweetviz) 
只需一行代码就可以可视化和比较数据集、目标值和关联。

[geemap](https://github.com/giswqs/geemap)
一个 `Python` 包，用于与 `Google Earth Engine、ipyleaflet和ipywidgets` 交互式地图。

[Cadmus](https://github.com/josh-richardson/cadmus)
`Cadmus` 是一个图形化的应用程序，它允许你在任何通信应用程序中实时去除音频中的背景噪音。

[carefree-learn](https://github.com/carefree0910/carefree-learn)
基于`PyTorch` 的表格式数据集的最小自动机器学习（`AutoML`）解决方案。

[Surprisify](https://github.com/StephenChou/Surprisify-Playlist-Generator) 
使用 `Spotify API` 的播放列表生成器。

[Guietta](https://github.com/alfiopuglisi/guietta)
一个用于制作简单的 `Python GUIs` 的工具。

[FavFreak](https://github.com/devanshbatham/FavFreak)
让基于 `Favicon.ico` 的 `Recon` 再次大放异彩!

[White-box-Cartoonization](https://github.com/SystemErrorWang/White-box-Cartoonization)
`CVPR2020` 论文 "Learning to Cartoonize Using White-box Cartoon Representations "的 `Tensorflow` 实现。

[Ai-Doctor](https://github.com/himanshu2406/Ai-Doctor)
开源 `Ai Discord` 机器人，只需X射线扫描，就能在几秒钟内检测出疾病。请记住，这是一个测试软件，你可以用于学习的目的，而不是用于现实生活的应用，建议一定要咨询真正的医生!

[Universities](https://github.com/ycd/universities) 
免费的 `API` 服务，您可以获取有关全球 `9600+` 所大学的信息。

[omg-badges](https://github.com/kautukkundan/omg-badges)
Gamify Livestreams - distribute badges to attendees while they watch your event's live stream on your website.

[jsmon](https://github.com/robre/jsmon)
A JavaScript Change Monitor for BugBounty.



### 新的版本

[Python 3.9.0b4](https://pythoninsider.blogspot.com/2020/07/python-390b4-is-now-ready-for-testing.html)

### 那些活动

[Virtual: PhillyPUG Meetup July 2020](https://www.meetup.com/phillypug/events/271570394/)
将会有以下话题：

- 用 `Tensorboard` 和 `PyTorch` 实现深度学习的可视化
- 自编程人工智能


[Virtual: [Workshop\] IndyPy Mixer - CI/CD 101 with CircleCI](https://www.meetup.com/indypy/events/hwstlrybckbsb/)
在本讲座中，将向学员介绍持续集成和持续交付/部署的基本原理。学员将学习 `CI/CD` 的核心原则，并有机会通过 `CircleCI` 平台的实践活动巩固所学知识。研讨会将演示 `CI/CD` 构建配置、代码提交、提交构建、代码测试和打包。

[Virtual: Cleveland Python Meetup July 2020](https://www.meetup.com/Cleveland-Area-Python-Interest-Group/events/fhqrtrybckbrb/)
将会有以下话题：

- Notebooks are still cool...with Jupyter
- Why Pattern Matching is AWESOME!


[Virtual: PyData Berlin Meetup July 2020](https://www.meetup.com/PyData-Berlin/events/259561236/)
将会有以下话题：

- Quantum Machine Learning for Programmers
- Application of NLP in the UK rail Industry

#### Posa：

> ❤️ Happy Pythonic ;-(Posa私人无责任播报)  


----- 分割线 -----

> 如果你发现哪里翻译有误的话，请务与我联系！感谢！




- 首发: [pythonista-weekly~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/python-weekly/pyw-457.html)
- 改进: [issue-457.md](https://github.com/PyChina/weekly/blob/master/content/python-weekly/issue%23457.md)

