Title: 蠎加载 25
Slug: importpython-25
Date: 2015-03-20 21:12
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 25](http://importpython.com/newsletter/no/25/)

## 该读
~ 文章, Blog, 教程...


- [Python 中的并发和并行初学指南](http://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python)
    + concurrency

线程只是众多并发程序构建的姿势之一.
此文,描述了在 python 中构建并发的多种策略,
以及适用场景.

(`是也乎:`

![multiple processes](http://www.toptal.com/uploads/blog/image/954/toptal-blog-image-1426661499995.jpg)

- 单进单线, 自然流程
- 多进单线, 原子事务
- 单进多线, 烧脑控制
- 消息总线, 恢复自然

)


- [PSF 的 Python 工作榜恢复!](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/cv-ch89BeaU/psf-python-job-board-relaunched.html)

差不多停了快一年,
终于 Python 职位公告板原地满血复活!
新系统完全整合到  python.org 中.
职位提供方,可以自由注册一个帐户,自主登录并提交招聘启事,
通过 PSF 的求职团队评审后即可上榜.


- [免费运行 Python 职位 Free Community Run Python Job Board](http://importpython.com/blog/post/free-community-run-python-job-board)
    + job market

非官方 Py 职位板是完全免费和社区驱动的.
此工作板内容从 git 仓库自动生成,并用 github-pages 发布.

- [用 Python 分析 Twitter 数据 (Term Frequencies)](http://marcobonzanini.com/2015/03/17/mining-twitter-data-with-python-part-3-term-frequencies/)
    + machine learning

这是系列中第三篇了,
通过数据的采集和整理,终于可以折腾点结论出来了,
对讨论进行长期的频率分析,从中提取有意义的方面.

- [安装 Apache Kafka 并使用 Py 3 进行通讯](http://www.giantflyingsaucer.com/blog/?p=5541)
    + python3,apache,kafka


Apache Kafka 已经有很多应用案例了,在笔者的工作中也用上了.
虽然在很多 "云" 场景中, Kafka 获得了认可,但是,想构建运行起来一直不是容易的事儿,
于是,笔者想出了一个方法,可快速将 py 3 接入...

- [用 selenium 对 Django views 进行自动化测试 — Medium](https://medium.com/@unary/django-views-automated-testing-with-selenium-d9df95bdc926)
    + django,Selenium

Selenium 乃自动化测试套件,对 web 应用程序的自动化交互测试提供了丰富的接口,
当然可以用来测试 web 应用/网页抓取 等等枯燥的测试案例.


- [为毛 RapidSMS 专注短信应用开发?](http://www.caktusgroup.com/blog/2015/03/16/why-rapidsms-SMS-applications/)
    + django

首先,什么是 RapidSMS ?
开源,Django 扩展的 web 应用框架,
支持文本信息处理的,完全开源的.
自动根据收到短信触发回应,
并设计为一组可插抜的模块代码.兼顾从前端到后端.


(`是也乎:`
![UNICEF-Project-Mwana-Caktus-Group](https://caktus-website-production.s3.amazonaws.com/media/blog-images/UNICEF-Project-Mwana-Caktus-Group-ICT4D.JPG)

世界上没有 wifi 的国家海了去的, SMS 大有可为的!

)

- [你的 Django 故事: 遇到 Caroline Simpson](http://blog.djangogirls.org/post/113785663798)
    + django,interview

Caroline 是位爱 Python 的程序媛.
她在 International Governance Innovation 中心工作.
创建了本地的 Python 用户组,吸引爱好者来共同折腾.
当然的,喜欢有趣的新技术.

- [介绍用 Python 进行统计](http://www.reddit.com/r/pystats/comments/2z624k/introduction_to_statistics_using_python/)
    + python,statistics

俺在自个儿的领域中进行数据统计,
但是,经常受挫于两件事儿:
1) 没有足够的统计,
2) 相关图书只提供了理论背景,从来不给实际的帮助.

针对以上,俺完成了这本书(无论在手上还是电脑中),
都将解决以上两个问题.
嗯啍!

- [Python 已为 C++ 后,第二高薪职业](http://lifehacker.com/the-programming-skills-jobs-and-company-types-that-pa-1692152608)
    + job market

漂亮的数据可视化支撑!

- [实效 Python 第40条: 协同程序同时运行多种功能](http://www.informit.com/articles/article.aspx?p=2320938)
    + concurrency

虽然 Python 的线程有各种问题,
但是,总是能解决的,这令你的程序看起来同时具有多种功能.
Brett Slatkin 将其体验分享在了
实效 Python 第59条: `写出更好的 Python 程序`


- [中阶 Python : 下一步](http://www.skilledup.com/articles/intermediate-python-development-the-next-steps/)
    + core python

你已经通过艰难的方式学习了 Python.
比如上 Codecademy.
现在你的兴趣有所下降,
好象对编程的兴趣在减少.
哪里有超越 初级 的课程?
想变成 Pythonista ? 这儿有些中阶课程,可以挑战自我.


## 项目
~ 包/模块/库/片段...


- [electrum](https://github.com/spasmilo/electrum)
    - 516 Stars, 2 Fork

Bitcoin 的瘦客户端 client.

- [AstroBuild](https://github.com/lhartikk/AstroBuild)
    - 368 Stars, 15 Fork

基于 planet alignments 完成部署.

- [PyTricks](https://github.com/brennerm/PyTricks)
    - 53 Stars, 3 Fork

收集 Python 相关的冷门编程技艺和特性.

- [easy_store](https://github.com/juliarizza/easy_store)
    - 20 Stars, 9 Fork

是 web2py 模型的电子商务/其它存储平台的支持框架.
目标就是最快获得一个可用的电子门店..

- [quodlibet](https://github.com/quodlibet/quodlibet)
    - 15 Stars, 0 Fork

全平台音乐库管理/播放 库.

- [gprof2dot](https://github.com/jrfonseca/gprof2dot)
    - 14 Stars, 0 Fork

将分析输出为 dot 图谱文件.

(`是也乎:`

![gprof2dot sample](https://github.com/jrfonseca/gprof2dot/raw/master/sample.png)

跨语言的哪! 将各种标准的分析结果,
用 伟大的 `Graphviz` 图形脚本输出为漂亮的自动排版的关系图谱!
)

- [webapp-checklist](https://github.com/dhilipsiva/webapp-checklist)
    - 8 Stars, 0 Fork

web 应用的程序猿,在网站发布前,应该考虑的所有事务的检验表!

(`是也乎:`
最实用的一种作弊条了 
居然有中文版!(好象是伟大的 google 自动翻译的)
;-)


## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
最后一周急招5名 gopher/pythonista !

## DAMA
(`大妈私人无责任播报`)

~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎


- 150323 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150321 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
