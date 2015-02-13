Title: 蠎加载 21
Slug: importpython-21
Date: 2015-02-13 17:17
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 21](http://importpython.com/newsletter/no/21/)

## 该读
~ 文章, Blog, 教程...

- [Python metaclasses 理解](http://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/)
    - core python

元类一直是 Py 中很有争议的话题,
很多用户在着意避免使用.
作者认为, 这很大程度上是因为其属性太过任性不好解释定位规则和流程.
其实,你嘦理解几个关键概念就可以上手的.
嘦能运用元类,
就能完成更好的接口.你值得尝试.

- [PyCon Sweden 的议题征集只余一周了](http://blaag.haard.se/PyCon-Sweden-Call-For-Proposals---Less-Than-a-Week-Left)
    - pycon

上次 PyCon 瑞典非常成功,
今年能更好.
议题征集将开放到 2.16 号,
会场迁移到 斯德哥尔摩市中心滨水区的 Hilton Slussen 大酒店,
日期定在梦幻般美好的春天,
5月12-13号,

- [你的 Django 故事: 遇到 Emily Manders](http://blog.djangogirls.org/post/110542266858)
    - django,interview


Emily 进入 web 开发前,是 PM 以及 UX,
她设计过临床的 IVR 试验系统,
教授过 Py 初学者,
出席过 CHI,
领导过精益用户研讨会,
调研了日本的 CAD 用户....
目前专注为 Django 提供国际化模板.
并为 Django 文档维护在作贡献.


- [Django 设计模式及最佳实践 - 好书来也](http://arunrocks.com/django-design-patterns-and-best-practices-book-coming-soon/)
    - django

有大事儿哪,
在上次 PyCon 有提及,
题为 "Django 设计模式及最佳实践" 的书,
已完成首校,将在三月上市,
可以先在这儿预订.

- [在 IIS 上安装 Django: 手把手教程](http://www.toptal.com/django/installing-django-on-iis-a-step-by-step-tutorial)
    - django

虽然 Django 广泛运行在 Liunx 平台上,
并没有什么机会必须跑在 IIS 下.
不过, Toptal 工程师 Ivan Voras 发布了怎么在 IIS 上部署 Django 的详细教程,
给 M$ 的真爱们.


- [转换 Python AST 到 XML ( Code Snippet )](http://code.activestate.com/recipes/579019-python-ast-to-xml/)
    - core python

转换 Python AST 到 XML 文档,
以便其它语言使用.


(`是也乎:`

AST ~ 抽象语法树(abstract syntax tree), 
其实就是一个语言语法的规则描述,
有了 Py 的 AST, 意味着我们可以用其它语言来理解 Py 脚本,
并用原生语言环境来最终运行.

PS:

代码片段来自 activestate.com 的 recipes 仓库,
这条已经是第 579019 个了!

PPS:

这个 AST 的输出,完全没有第三方依赖,
使用 Py 内建模块就完成了,
这也是 为什么有 PyPy 项目的动因.
)

## 项目
~ 包/模块/库/片段...



- [API-Hour](https://github.com/Eyepea/API-Hour)
    - 13 Stars, 0 Fork

API-Hour 是种轻易守护进程框架.
专注建立能长期稳定运行的髙响应/简单/强力 守护进程.
其中 API-Hour Starter Kit (Cookiecutter) 为你的服务创建 HTTP 守护.
通过 API-Hour 你可以快速将同步 IO 的服务,
变成多守护进程运行, 为生产环境上线作好准备.

(`是也乎:`
在 CPyUG 列表,最近有一个线索讨论: `Py是否能开发7x24小时运行的守护服务?`

这类 daemon 框架很好的回答了这类疑问.
嗯啍, `눈_눈_`
)

- [deployapp](https://github.com/mardix/deployapp)
    - 12 Stars, 1 Fork

Deployapp 用来在 virtualenv 中部署多个 Py 网站/应用.
其实也支持你来部署 PHP/HTML 应用,
并通过 Supervisor 来调度.


- [ghmarkdown](https://github.com/lukedmor/ghmarkdown)
    - 11 Stars, 4 Fork

针对 GitHub-flavored markdown 的完全命令行工具.

(`是也乎:`

![ghmarkdown live show](https://camo.githubusercontent.com/0d0e0635dc5c3aca3d9f9c23c8a3dce0a1a33111/687474703a2f2f692e696d6775722e636f6d2f57554357704f4d2e676966)

可以理解为单文件静态网站生成器.
活的.
)

- [dictaphone](https://github.com/shbhrsaha/dictaphone)
    - 7 Stars, 1 Fork

可随时断/续的命令行录音工具.


-[services-to-wordcloud](https://github.com/vdmitriyev/services-to-wordcloud)
    - 6 Stars, 7 Fork

专注的小工具,
爬数据分析并组织为 单词云.

- [meteora](https://github.com/raulcd/meteora)
    - 6 Stars, 0 Fork

Py 完成的 web 应用性测试工具

- [two-factor-auth-flask](https://github.com/miguelgrinberg/two-factor-auth-flask)
    - 6 Stars, 0 Fork

文章 "用 Flask 进行双步身份验证"
的实验代码.


- [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes)
    + 5 Stars, 1 Fork

检索任何 Wikiquotes 页面.


## DAMA
(`大妈私人无责任播报`)

- [小米运维—互联网企业级监控系统实践 - 简书](http://www.jianshu.com/p/b2f77285266c?comment=159685#comment-159685)


(`是也乎:`

哗! go+py 当前最时尚的组合!
管理端同时提供了 php/node 版本!
真心用心了.

)

- [分享ipython notebook - 小明明s à domicile](http://dongweiming.github.io/blog/archives/ji-jiang-zai-bpugfen-xiang/)

(`是也乎:`

BPUG 的小伙伴, 深入折腾了 IPython notebook 爽到飞溅出自个儿的教材来
值得学习!
当然的视频在墙外.
)


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150213 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150213 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
