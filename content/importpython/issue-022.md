Title: 蠎加载 22
Slug: importpython-22
Date: 2015-02-20 20:20
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 22](http://importpython.com/newsletter/no/22/)

## 该读
~ 文章, Blog, 教程...

- [vdist, 通过 virtualenv, Docker 和 fpm 为 Python 应用构建 OS 包](http://vdist.readthedocs.org/en/latest/)
    + virtualenv

专注构建干净,自包含的 OS 包,
给 Python 应用,
综合使用了  virtualenv, Docker 和 fpm ,
并用 Jinja2 来渲染展示模板.

- [Py 调 Graph API 来获得 fb 上点赞数目](http://www.idiotinside.com/2015/02/13/get-number-of-likes-of-a-facebook-page-using-graph-api-in-python/)
    + facebook

教程中,展示了如何获得 facebook 页面上的点赞数据,
虽然还没有官方 SDK,
用 Python 调用 Graph API REST 方法即可.

- [Python 修饰器作弊条儿](http://pydanny.com/python-decorator-cheatsheet.html)
    + core python,decorator

总是记不住修饰器的写法?!
不用四处找了,收藏这个就对了.

(`是也乎:`
目测 dash 中就有?
)


- [Python + Elasticsearch.介绍/基础教程.](http://blog.tryolabs.com/2015/02/17/python-elasticsearch-first-steps/)
    + elasticsearch

`Elastic{ON}15`,
首届 ES 大会就要来了!
因为 ES 令大家看到了更多的可能,
趁机为 Python 开发者介绍 ES 的简单实例,
展示怎么开始...


- [Python: 技巧/诀窍和常识 - 第2部分 - 装饰和上下文管理](https://codefisher.org/catch/blog/2015/02/10/python-decorators-and-context-managers/)
    + core python

两周前,发布了此系列第一篇文章,
这周,聚焦到更加深入的领域.
首先是修饰器,当然没有包含所有技巧;
然后针对上下文管理,也只给了一个案例;
再次提醒代码都在  gist.github.com.

- [Django 测试入门 - howchoo](http://howchoo.com/g/mjkwmtu5zdl/getting-started-with-django-testing)
    + django,testing

虽然编程有日子了,
但是作者最近才实施测试.
所以,文章是真正的基础,对于有经验的可以跳过相关部分.
对于其它的,首先是整体的概述,希望有所帮助

- [DjangoCon Europe 2015 update](https://www.djangoproject.com/weblog/2015/feb/18/djangocon-eu-2015-update/)
    + django

2015's DjangoCon Europe 在威尔士的 Cardiff 进行,
5.31~6.5,整整6天,
官网刚刚更新了内容.

- [成为 Django Girls Patreon!](http://blog.djangogirls.org/post/111378603928)
    + django

短短7个月,Django Girls 教授了
包含 欧洲/非洲/亚洲/澳大利亚/北美 超过670位程序媛.
并越预期的收到了超过 3000 个应用!
免费开源教程有 30000 位读者,
平均阅读了350次! ~ 真心赞!

- [PyVmMonitor: 全新 Python 分析器](http://www.pyvmmonitor.com/)
    + debugging


PyVmMonitor 的目标很单纯:
成为最好的 Python 程序分析途径

- [在家/自由职业 Python 开发者需要什么?](http://www.reddit.com/r/Python/comments/2w7h7f/how_is_the_demand_for_python/)
    + job market

引发自 reddit.

- [Jython 2.7 beta4 发布!](http://fwierzbicki.blogspot.com/2015/02/jython-27-beta4-released.html)
    + new release

非常感谢 Amobee 的赞助,
令这个版本爽快的发布了!

## 项目
~ 包/模块/库/片段...


- [django-baker](https://github.com/krisfields/django-baker)
    - 68 Stars, 2 Fork

Django Baker 想助你加速项目的启动和运行.
嘦给定一个或一组项目名称,
Baker 就能自动生成 视图/表单/url/管理/模板...
所有生成文件都是 pep-8 兼容的.
(当然有几个规则是不同意的...比如说,最大行长)

- [nosebook](https://github.com/bollwyvl/nosebook)
    - 39 Stars, 2 Fork

IPython 3 notebooks 的插件,
自动探知 nose 测试案例.
协助你确保文档/代码一致性,
并支持多格式文档以及测试套件.

- [LaZagne](https://github.com/AlessandroZ/LaZagne)
    - 38 Stars, 6 Fork

LaZagne 是开源密码挽救工具,
通过各种手法(明文,API,定制算法...)
为本地软件找回你忘记的口令.
已经支持最常用软件,此刻在 windows 12 以及 linux 平台上可 挽救 22款软件的口令.


(`是也乎:`
![lazagne](https://github.com/AlessandroZ/LaZagne/raw/master/pictures/lazagne.png)

细思恐极...
)

- [carrot](https://github.com/jbowen7/carrot) 
    - 10 Stars, 0 Fork

为 Django 打造的 芹菜 替代品.

- [pyramid_services](https://github.com/mmerickel/pyramid_services)
    - 9 Stars, 1 Fork

pyramid 的服层.

- [SocialAuthDjangoTutorial](https://github.com/davisfreeman1015/SocialAuthDjangoTutorial)
    - 8 Stars, 0 Fork

适合初学者的 Django SNS 认证教程,
将逐一教授如何
从你的应用中 注册/登录 
facebook,titter, google.

- [captchasec](https://github.com/mmetince/captchasec)
    - 8 Stars, 0 Fork

Captchasec 是验证码测试器.
使用 de-captcher.com 作为 OCR 服务后背.


- [fuel](https://github.com/bartvm/fuel)
    - 7 Stars, 4 Fork

针对机械学习的流水线框架.


- [sqlite_sql_parser](https://github.com/motherapp/sqlite_sql_parser)
    - 3 Stars, 0 Fork

脚本能从 sqlite3 .dump 文件中导出兼容 MySQL 的 SQL 文件.



-[StockWatcherAPI](https://github.com/SaiWebApps/StockWatcherAPI)
    - 2 Stars, 0 Fork

通过金融/头条新闻等等渠道,为用户综合指定股票的信息.
通过这个接口,
提交股票编号,
返回一个标准 Py 字典,包含所有相关财务数据.


## DAMA
(`大妈私人无责任播报`)


![PyCon Asia-Pacific 2015](http://zoomq.qiniudn.com/CPyUG/PyCon2015China/pycon-apac2015-logo.png)

- [亚太Py大会 6-5~7 在台北举行!](http://pycontw.blogspot.tw/2015/02/pycon-asia-pacific-2015-in-taiwan-save.html)

[PyCon APAC/Taiwan 2015 - Call for Proposals](https://tw.pycon.org/2015apac/en/call-for-proposals/) 议题召集已经释放,想去宝岛体验社区交流的,可以下手了!

- 一个靠谱的微信群引发的: [极简编程导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistProgramStart#_5)

## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150304 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150228 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
