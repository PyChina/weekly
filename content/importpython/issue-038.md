Title: 蠎加载 38
Slug: importpython-38
Date: 2015-07-03 14:41
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 38](http://importpython.com/newsletter/no/38/)


**翻译ing...**

## 该读
~ 文章, Blog, 教程...

- [用 Morepath + Jinja2 构建更好的用户界面](http://blog.startifact.com/posts/morepath-batching-example.html)
    - web framework

Morepath 是又一个 Python web 框架,
虽然 Morepath 非常适合打造 REST API,
其实也是很好的服务应用平台.
这里来展示如何基于 Morepath 创建批处理 UI.



- [pip -t: 对 virtualenv 的简洁替代](http://blog.zoomeranalytics.com/pip-install-t/)
    - pip

通常 virtualenv 是唯一的隔离不同 Python 项目环境依赖的方案.
现在有种神奇的替代方案.

(`是也乎:`

目测受 node_model 启发.

)

- [代理在 Docker 中运行的 Python web 应用.](http://blog.dscpl.com.au/2015/06/proxying-to-python-web-application.html)
    - docker

俺见过几个问题,都引发自在 Docker 运行的 Python web 应用,
用 Apache 难以合理代理.

其实,这都是以往在主机上习惯用 Apache/mod_wsgi 进行发布的结果.
其实,现在用 Docker 已经打破了,传统的部署思路.
改进了!

- [Python 101: 节目 #7 – 异常捕获](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/V8q86BPZaOs/)
    - core python, video

最新节目,介绍异常处理,希望大家喜欢.

- [用 Hypothesis 测试 Django 应用](https://skillsmatter.com/skillscasts/6475-testing-django-applications-using-hypothesis)
    - django, testing

David MacIver 
讨论如何用 Hypothesis 测试 Django 应用的
 

- [在 Docker 镜像中安装定制版本的 Python.](http://blog.dscpl.com.au/2015/06/installing-custom-python-version-into.html)
    - core python

对于 Linux 发行版本,内置的软件很快就会过时,
这个问题日益严重.
基于 Linux 的包管理策略,除非发行商,升级版本,否则,
我们无法通过包安装到最新版本软件.

必须解决了!

- [Django 故事: Iulia Chiriac](http://blog.djangogirls.org/post/122760203063)

Iulia 是位全桟式 web 工程师,
以及开源爱好者.
过去三年中每一分钟都沉浸在 Python 中.

之前,当然也体验过很多语言,包含 C/C++/C#/PHP 和 JAVA .
目前,就职于 总部在 Bucharest 的罗马尼亚公司 Eau de Web (http://www.eaudeweb.ro)

- [Django 安全顾问: simple_tag 不能 auto-escaping](https://www.djangoproject.com/weblog/2015/jun/29/simple_tag-security-advisory/)
    - django

文档中曰过,用以创建自定义模板的 simple_tag
修饰器,不能自动对其内容进行转义(Django 1.8).
这使得非常容易被 XSS 攻击.
具体示例链接中.

- [Python 学习中不同层次的经验和建议.](http://www.reddit.com/r/Python/comments/3bcfba/learning_resource_at_intermediate_to_advanced/)
    - core python

reddit 热议中,值得关注.

- [用 pylint 和 flask 远离错误](https://github.com/jschaf/pylint-flask)
    - flask

pylint-flask 是 Pylint 插件,
专注针对 Flask 应用进行分析,
基于 pylint-django 的启发.


- [EuroPython 2015: 网站义工召集](http://blog.europython.eu/post/122845271022)
    - community

EuroPython 也是由社区志愿者组织和运行的,
当然只需要少数给力的志愿者,所以,来吧!

- [令 Python 描述简单](http://www.smallsurething.com/python-descriptors-made-simple/)
    - core python

在 Python 2.2 引入了全新的对象属性管理方法,
以便在内置库和第三方库之间,
减少 `魔法` 情况出没.



### 工作

-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)
急招 N 名有服务端开发经验的 **gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...


- [cnn-vis](https://github.com/jcjohnson/cnn-vis)
    - 180 Stars, 18 Fork

受到谷歌最近 Inceptionism 
博客文章的启发,

cnn-vis 作为开源工具, 协助我们用 卷积神经网络来生成图像

![cnn-vis](https://camo.githubusercontent.com/2c76373d72fa266e8a4c614e4b301c48cf1c10b0/687474703a2f2f63732e7374616e666f72642e6564752f70656f706c652f6a636a6f686e732f636e6e2d7669732d6578616d706c65732f6578616d706c6531322e706e67)

- [autosub](https://github.com/agermanidis/autosub)
    - 72 Stars, 4 Fork

为任意视频自动生成字幕文件

(`是也乎:`

喂! 字幕组怎么办!
)

- [cli-github](https://github.com/harshasrinivas/cli-github)
    - 71 Stars, 9 Fork

github 的 CLI 版本

- [ascii_py](https://github.com/ProfOak/ascii_py)
    - 20 Stars, 0 Fork

ASCII 艺术创造工具

(`是也乎:`

![pizza_in](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/pizza_in.jpg)

变成:

![ascii_pizza](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/ayy_lmao_pizza.jpg)

)

- [django-rest-framework-braces](https://github.com/dealertrack/django-rest-framework-braces)
    - 13 Stars, 0 Fork

DRF(Django REST 框架) 实用工具集锦

- [geog](https://github.com/jwass/geog)
    - 10 Stars, 0 Fork

在 Python 中快速搞掂地理功能

- [scli](https://github.com/davecarpie/scli)
    - 7 Stars, 0 Fork

用 curses 构建的可选择/滚动的终端列表!

![scli](https://camo.githubusercontent.com/73a473a0193f8110b1e5fd53a126255c2a984527/687474703a2f2f692e696d6775722e636f6d2f504569335139382e706e67)

- [Stock_advisor](https://github.com/robbiebarrat/Stock_advisor)
    - 3 Stars, 0 Fork

基于
Yahoo_finance api 
获得公司股票基本信息,
然后综合给出购买建议.

## DAMA 无责任推荐

- [lvsoft/enhanced_logging](https://github.com/lvsoft/enhanced_logging)
    - 9 星, 0 支

当年就有人黑 print 哪....


# 是也乎

- 150717 [Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150707 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
