Title: 蠎加载 32
Slug: importpython-32
Date: 2015-05-15 22:22
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 32](http://importpython.com/newsletter/no/32/)

## 该读
~ 文章, Blog, 教程...

- [今天 IPython notebooks 正式成为 GitHub 支持格式](https://blog.jupyter.org/2015/05/07/rendering-notebooks-on-github/)

官方 blog 非常高兴的宣布,
在 github 所有仓库中的 Jupyter/IPython notebook (.pynb) 文档,
将直接得到渲染!

(`是也乎:`

![150522-pynb-github](http://zoomq.qiniudn.com/ZQCollection/snap/150522-pynb-github.png)

真的!!!
)


- [Pipelining - 一种成功的数据处理模式 (python案例)](http://blog.stuartowen.com/pipelining-a-successful-data-processing-model)
    + python

所谓 "流水线" 就是将大任务分解为更小的一系列任务,
以便并行计算,
这在 CPU 设计领域一直在蓬勃发展,
但是,对于一般计算范畴还没通用解决方案.
笔者分享了一般化的考虑.

- [实现 Python 的修饰符](https://youtu.be/fAiN-iEsGBA)
    + video

看看用函式化编程概念,如何在 Py 中完成修饰符功能.

- [Webcast: 教孩子编程 之 Python 中的小乌龟](http://www.oreilly.com/pub/e/3422)

在这一网络广播中,
教你如何引导学前儿童,
用可视化交互式式环境来学习编程思想.


- [Django 1.8 和 Python 3: 端到端的复杂应用教程 | Hacker News](http://marinamele.com/taskbuster-django-tutorial)
    + django

非常激动的分享大家最新的 Django 教程,
可以带领大家用 Django 1.8 在 Python 3 下面,
从头建立一个应用,
特别关注管理器的使用.
目标是每个人跟教程走下来同时也建立好了自个儿的应用.

- [以 Python 程序猿角度来学习 Lua](http://bugra.github.io/work/notes/2015-05-09/learning-lua-as-a-python-developer/)
    + core python

此 Lua 教程是面向 Pythonista 的,
针对各种 Lua 的特性和概念,对比 Python 中的,
以便快速建立基本概念,复用经验.

- [关闭你的 Django 上下文处理器](http://www.peterbe.com/plog/closure-django-context-processors)
    + django

当你有复杂的网站模板要渲染时,
可能有很多自动处理的计算,
这意味着很多额外的计算,而且计算结果永远不会显示出来.

- [动态类型语言的吸引力是什么?!(以 Python 为例)](http://www.reddit.com/r/Python/comments/35iamd/what_is_the_appeal_of_dynamicallytyped_languages/)

动态类型研究好在哪儿? 有人能说明白卟!?

(`是也乎:`

至今也只有4个回复的好问题...

目测好象八成,真的没有什么明显的好处...

)

- [Python 2.7.10 候选版 1 发布](http://feedproxy.google.com/~r/PythonInsider/~3/FTlNOgFndNo/python-2710-release-candidate-1.html)
    + core python, new release

嗯啍,欢迎下载测试

- [为你的工程自动生成 requirements.txt](http://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/)
    + python

任何应用都依赖一组特定的组件才能运行.
requirements.txt 就是声明这组依赖关系的文件,
并能为 pip 理解,自动完成部署.

可惜....多数情况下只能由人工编写.很不靠谱.

(`是也乎:`
必须用!

)


- [用 闭包 优化 Python ](https://wrongsideofmemphis.wordpress.com/2015/05/08/optimise-python-with-closures/)
    + core python

Dan Crosta 的分享非常有趣.
讨论了到底有多少次 Python 内部调用是不必要的,
以及如何用闭包来替代 OOP ,从而优化性能.

- [libbson 和 libmongoc 1.1.5 发布](http://feedproxy.google.com/~r/emptysquare/~3/WrU_HqoQEl0/)
    + mongodb

libbson是用于创建/分析和操作BSON文档的C库.
libmongoc是MongoDB的C驱动库.
用以构建与MongoDB沟通的C语言高性能应用程序.
同时也可以为其它高级语言使用.

- [用 K-Means 聚类算法来分析 Harry Potter 的内容主题](http://dogdogfish.com/2015/05/11/finding-topics-in-harry-potter-using-k-means-clustering/)
    + machine learning

I'll open up with the money-shot – these are all of the clusters that I was able to find using the whole Harry Potter and grouping by chapter. Find the repository associated with this article in our projects list.

- [主题建模的新手](http://feedproxy.google.com/~r/oreilly/radar/atom/~3/bZH8jjcd51A/topic-modeling-for-the-newbie.html)
    + machine learning

又一更加复杂的用户兴趣分析方法,
即所谓 Latent Dirichlet Analysis (LDA) 技术,
通过对一组文本的分析,得到其背后的共同主题利益.



## New Books

- [Hello Web App](http://hellowebapp.com/)
    + Tracy Osborn

"Hello Web App"
是为非程序猿设计,
会引导你完成构建 web 应用的所有过程,
不是通过特定的教程,
而是一个实际的通用实例,
由读者亲手在 Django 基础上创建自己兴趣的网站.

嗯啍,请关注 

http://importpython.com/blog/

有作者的访谈.


## 项目
~ 包/模块/库/片段...

- [django-hackathon-starter](https://github.com/DrkSephy/django-hackathon-starter)
    - 75 Stars, 12 Fork

又一个 Django 应用样板

- [ptf](https://github.com/trustedsec/ptf)
    - 28 Stars, 6 Fork

渗透测试框架(PTF ~ Penetration Testers Framework)
是先进的模块化测试工具.

PTF 为你的测试自动安装/编译/构建所有测试,
能安装/更新到你的所有主机上.


- [HarryPotterClusters](https://github.com/Kali89/HarryPotterClusters)
    - 21 Stars, 0 Fork

你应该想要的 哈利·波特集群!

- [isthisipbad](https://github.com/jgamblin/isthisipbad)
    - 15 Stars, 6 Fork

用 Python 脚本来检查 IP 地址污染问题,
基于一组流行的 IP/DNS 黑名单.
是 IP 坏了,还是其它什么问题?!

- [notebooks](https://github.com/censusreporter/notebooks)
    - 12 Stars, 0 Fork

收集的 Jupyter notebooks ,
有关人口普查问题的探查.
引用的是 Census 报告数据.
详细链接中有述.

- [aeneas](https://github.com/readbeyond/aeneas)
    - 10 Stars, 2 Fork

aeneas 收集了一组工具,
来对音频和文本进行同步.


- [brute_force_plotter](https://github.com/eyadsibai/brute_force_plotter)
    - 4 Stars, 0 Fork

用傻瓜化方式快速建立数据可视化.

- [gitini](https://github.com/saru95/gitini)
    - 3 Stars, 0 Fork

遗失的 git 仓库初始化工具.

- [youtube-dl-subscriptions](https://github.com/mewfree/youtube-dl-subscriptions)
    - 1 Stars, 0 Fork

从你的 youtube 订阅下载所有最新视频

(`是也乎:`

放心,从国内不可用.
)

- [ratex](https://github.com/jeffsp/ratex)
    - 1 Stars, 0 Fork

以 Flask 中间件实现的一个 web 应用,
能导入一次旅行的路线数据,
自动绘到地图上.

- [PageRank](https://github.com/ashkonf/PageRank)
    - 1 Stars, 0 Fork

用 Python 实现的 Google's 著名算法 PageRank .

(`是也乎:`

嗯啍?! 人家本来就是 Python 实现的哪,,,
是也乎,再制版, 原版是不给看的了...

)


## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)

### 工作

-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
四月急招 N 名有服务端开发经验的 **gopher**!


-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

-   [SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)  

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!

# 是也乎

- 150523 [Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150515 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

