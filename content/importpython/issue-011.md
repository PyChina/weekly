Title: 蠎加载 11
Slug: importpython-11
Date: 2014-12-11 23:32
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/80)


原文: [ImportPython Newsletter Issue 11 - 4th December](http://importpython.com/static/files/issue11.html)



## 该读
~ 文章, Blog, 教程...

- [字符编码和伟大的 Unicode](http://agiliq.com/blog/2014/11/character-encoding-and-unicode/)


所有 Python 程序猿总有一天会遇到这个问题的.
读这篇文章吧,开开天眼.


- [为小白介绍 Python 的 *args 和 **kwargs – 第一部分](http://www.unixmen.com/introduction-python-args-kwargs-beginners-part-1/)

对 Python 函式参数的 `*args` 和 `**kwargs` 变参形式, 
是很多新人困惑的地方,此文进行了详进的论述.
并给出了很多实用建议.

- [Python 中的修饰和描述符](http://h3manth.com/new/blog/2014/descriptor-decorator-in-python/)

Decorators 和 Descriptor 
是 Python 中两个独立的功能,
而且,一起运用时,最爽!


-[基于 Apache/mod_wsgi 模块用 Docker 来部署 Python WSGI 应用.](http://blog.dscpl.com.au/2014/12/hosting-python-wsgi-applications-using.html)

目测这是第一篇, 用 Docker 部署 Apache/mod_wsgi 发布的 Python 应用的文章,
为此作者还提供了预先包装好的镜像.

(`是也乎:`
不过, Apache/mod_wsgi ? 你确定是认真的?)

- [用 Python 扩展 SQLite](http://charlesleifer.com/blog/extending-sqlite-with-python/)

蠎周刊曰过了...

SQLite is an embedded database, which means that instead of running as a separate server process, the actual database engine resides within the application. This post describes how to extend SQLite with Python, adding functions and aggregates that will be callable directly from any SQL queries you execute.

- [用 Signals 和 Redis 进行简单分析](http://jibreel.me/blog/4/)

Signals 能对你指定的部分代码暴露 hook 出来,
这儿有一些实例, 展示如何对 Django/Flask 应用,
通过 hooks 对网站运行进行分析.

-[你的 Django : 遭遇 Patrycja Szabłowska](http://blog.djangogirls.org/post/104071168043/your-django-story-meet-patrycja-szablowska)

`Your Django Story` 系列文章,
这期是 程序媛 的极赞介绍.


- [在瑞典/挪威/芬兰僵尸爆发模型分析](http://maxberggren.com/2014/11/27/model-of-a-zombie-outbreak/)

疾病传播模式的研究,
造型为某种虚构的僵尸爆发;-)
当然, 可读性来自 numpy 和数据科学技巧.

- [IBM, Databricks, GraphLab 支持 Notebooks 问以建立预测应用!](http://www.infoq.com/news/2014/12/ipython-notebooks)

为毛应该学习 IPython?
因为 notebook 已经成为新型电子表格,可运行的那种.


- [sprints 有啥特殊的?](http://pycon.blogspot.com/2014/12/whats-so-special-about-sprints.html)

什么是 sprints?
在 PyCon 之后,
大家周一~四,每天进行的冲次开发,
可以进行 功能增加/bug修复/应用|库移植.


## 代码
~ 包/模块/库/片段...

- [prygress](https://github.com/dboudwin/prygress)
    - 8 Stars, 3 Fork

进度条

- [FacebookSearcher](https://github.com/shreyashirday/FacebookSearcher) 
    - 9 Stars, 2 Fork

自动识别 fb 消息中的 url/电话号码/邮件地址...

- [jitpy](https://github.com/fijal/jitpy) 
    - 8 Stars, 0 Fork

CPython 中嵌入 PyPy 的库.瞬间提速 20x

- [ssdb-ya](https://github.com/pyloque/ssdb-ya)
    - 8 Stars, 1 Fork

又一个 ssdb 的 Python 客户端.
用来替代 Redis 的 NoSQL 数据库.

- [TextRank4ZH](https://github.com/someus/TextRank4ZH) 
    - 6 Stars, 8 Fork

TextRank 可以从文章中提取摘要和关键字,
TextRank4ZH 则是能用 TextRank 的算法处理中文文章.

- [django-invitations](https://github.com/bee-keeper/django-invitations)
    - 6 Stars, 0 Fork

为 django-allauth 集成的邀请模块.

- [SkypeBot](https://github.com/Vilsol/SkypeBot)
    - 6 Stars, 6 Fork

用来记录开发交流的 Skype 机械人

- [pysswords](https://github.com/marcwebbie/pysswords)
    - 4 Stars, 3 Fork

Pysswords 用 scrypt 加密本地文件.


- [delete_tweets](https://github.com/mazlumagar/delete_tweets)
    - 2 Stars, 0 Fork

用 Python 删除推文.

- [python-requirements-generator](https://github.com/sarunks/python-requirements-generator)
    - 1 Stars, 0 Fork

扫描所有目录和文件,自动生成安装模块依赖描述文本

(`是也乎:`
这个异常有用哪!-)


- [price-alert](https://github.com/eyalzek/price-alert)
    - 1 Stars, 1 Fork

私人比价助理!
当商品价格低于事先设定时,立即邮件提醒
(已测试过 Amazon 可用)




## 曰了
~ Tweets


- [社区成员/管理员应该有什么素质? 例如 为毛知识应该分享?](https://twitter.com/importpython/status/539742644759707649)

@importpython

- [学习哪种语言收益最大? 目测是 Python](https://twitter.com/slashdot/status/540206177930334208)

@slashdot 

(`是也乎:`
无法同意更多!-)


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)

- 141208 用时 42 分钟完成快译.
- 141207 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
