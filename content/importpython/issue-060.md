Title: 蠎加载 60
Slug: importpython-60
Date: 2016-02-05 21:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 60](http://importpython.com/newsletter/no/60/)

## 该读
~ 文章, Blog, 教程...


- [播客访问 Jupyter 和 IPython 项目](https://talkpython.fm/episodes/show/44/project-jupyter-and-ipython)
    + podcast

目下 Python 中增长最快的领域之一就是科学计算.
其中有几个关键包: NumPy / SciPy / 及其相关组件,
都集成在 IPython(更名为 Jupyter) 中,并能方便的可视化!
44期节目探讨了这方面的发展.


- [测试 Django Views](http://kracekumar.com/post/138492827565)
    + testing

移动和 SPA(单页应用)已经是 web 开发中 API 为中心的主要命题了.
这对于以往返回 html 页面的Django 应用而言,
测试这种 view 是困难的,
因为 REST 语义和 HTTP 状态码是关联的...


- [Your Django Story: Meet Safia Abdalla](http://blog.djangogirls.org/post/138480005403)
    + interview
Safia Abdalla is an energetic software engineer with an interest in data science for social good and delicious coffee. She is the organizer of PyData Chicago and the founder of dsfa, a consulting company providing data science services to small and medium local businesses. Safia is also a frequent conference speaker and open-source contributor who’s passionate about helping others to reach their maximum potential.

- [How to no-mincss links with django-pipeline](http://www.peterbe.com/plog/how-to-no-mincss-links-with-django-pipeline)

如题 :)

- [官方公告 - IPython 4.1.0 放出!](https://mail.scipy.org/pipermail/ipython-dev/2016-February/017056.html)
    + new release

前几天释放后,没有收到任何有效 bug 反馈,
所以,嗯哼! IPython 4.1.0 is now out !

- [实例理解 Python 中的 JSON Web 令牌](http://blog.apcelent.com/json-web-token-tutorial-example-python.html)

文章解析了如何使用 JSON Web Token 来保护我们的 REST 接口.
JSON 网络令牌是 RFC 7519 提出的双向安全方案,
JWT 已获得关键厂商的支持,包含 Firebase, Google, Microsoft, 以及 Zendesk.


- [高可扩展 - Cassandra 和 Gevent 实现 Python 的异步](http://rustyrazorblade.com/2016/02/async-python-and-cassandra-with-gevent/)
    + concurrency

Python 2.7 中的线程/GIL/异步锁等等导致异步代码很折腾.
好在艰难岁月中还是有靠谱方案的;
比如 IronPython 和 Jython 就没有 GIL 以及相关问题.
当然, 还有专用的 Stackless Python,
通过微进程管理,避免操作重量级的操作系统进程,以及其它功能.


- [django-ses/django-ses: Django 实现的 Amazon Simple Email Service 后端](https://github.com/django-ses/django-ses)
    + aws

Django-SES 是种 drop-in 邮件后台,
不用传统的 SMTP 服务,
而是基于很赞的 Amazon Simple Email Service (SES)


- [YPlan/django-ratelimit: 为 Django 提供基于缓存的限速](https://github.com/YPlan/django-ratelimit)
    + django

Django Ratelimit 
提供修饰器来声明限制,
可基于 IP 或请求, 无论 GET/POST 方法.

- [Smartyparse: 面向对象的动态二进制打包和解包](https://github.com/Muterra/py_smartyparse)

SmartyParse 
是面向 3.3 以上 Python 的二进制 打包/解包（又名建筑/解析）格式库.
如果需要定义二进制格式
(.tar, .bmp, 字节式网络数据包..)
或是开发专用格式,
SmartyParse 能直接从 Python 对象转换成拟定格式.
操作对象是 `Construct`



## 新书
~ New Books

- [Flask 蓝图](http://importpython.com/books/520/flask-blueprints/)

Structure, compose, 以及 build powerful Flask HTML-based 
应用,
基于高级应用设计模式完成 JSON/XML-based APIs .

- [Flask Framework Cookbook](http://importpython.com/books/447/flask-framework-cookbook/)

Flask Framework Cookbook 
帮助我们了解 Flask 框架真正强大的扩展能力.
能从不同途径理解 Flask 应用,
也能学习到 模板/ORM 以及视图层的细节.

- [用 Python 进行地理分析](http://importpython.com/books/526/geoprocessing-with-python/)

几乎所有的汽车，手机，或者相机具有GPS传感器
以及航空照片，卫星图像
的数据都包含 国家界限，道路，河流和溪流...
而且可以从很多网站免费下载!
地理处理就是读取，分析和编程方式呈现地理空间数据的科学!



## 项目
~ 包/模块/库/片段...



- [GraphvizAnim](https://github.com/mapio/GraphvizAnim)
    - 230 Stars, 12 Fork

闭关锁国 graphviz 生成有动态效果图片的工具.

(`是也乎:`

![dfv.gif](https://github.com/mapio/GraphvizAnim/raw/master/examples/dfv.gif)

仙品!

)


- [himawaripy](https://github.com/boramalper/himawaripy)
    - 130 Stars, 33 Fork

将几近实时的地球图片设定为桌面背景!

(`是也乎:`

基于 [Himawari 8 (ひまわり8号)](https://en.wikipedia.org/wiki/Himawari_8)
提供的图片资源...

日本的公开数据资源这么高端了哪!!!
)


- [K3SimSearch](https://github.com/BichengLUO/K3SimSearch)
    - 42 Stars, 0 Fork

简单的脚本,
用 Python 从 GRE 单词中指出指定单词的同义词等等...


- [tnote](https://github.com/prodicus/tnote)
    - 30 Stars, 7 Fork

:clipboard: 命令行记录本,
好用到老奶奶也稀饭...

(`是也乎:`

```
                            _________ _        _______ _________ _______ 
                            \__   __/( (    /|(  ___  )\__   __/(  ____ \
                               ) (   |  \  ( || (   ) |   ) (   | (    \/
                               | |   |   \ | || |   | |   | |   | (__    
                               | |   | (\ \) || |   | |   | |   |  __)   
                               | |   | | \   || |   | |   | |   | (      
                               | |   | )  \  || (___) |   | |   | (____/\
                               )_(   |/    )_)(_______)   )_(   (_______/
```

参考演示: [tnote: A dead simple note taking app : v0.0.2 - asciinema](https://asciinema.org/a/35557)
)


- [zika-data](https://github.com/BuzzFeedNews/zika-data)
    - 27 Stars, 8 Fork

Data — 以及数据指向
所有 2015–16 Zika 病毒相关的!

- [camp](https://github.com/mpdehaan/camp)
    - 15 Stars, 0 Fork

计算机辅助音乐创作

- [Tasker](https://github.com/t0mj/Tasker)
    - 12 Stars, 4 Fork

又一个日常任务管理 CLI 工具.

(`是也乎:`

![Tasker](https://cloud.githubusercontent.com/assets/7049067/12701187/d7bf58d6-c7c6-11e5-8e27-bbfc4f8ecc2e.png)

是的,我们就是忍不住创建各种 DSL
)

- [livemark.vim](https://github.com/miyakogi/livemark.vim)
    - 12 Stars, 0 Fork

实时预览 MD 的 vim 插件

- [spotify-music-downloader](https://github.com/xfilipe/spotify-music-downloader)
    - 9 Stars, 4 Fork

脚本能从 youtube 中下载音乐,
给 spotify(Linix 中) 播放.


- [PythonBackupSystem](https://github.com/msfidelis/PythonBackupSystem)
    - 6 Stars, 2 Fork

Rotinas de Backup Full e Diferencial feitas em Python #IndustriaFox


## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

### 工作

....


# 是也乎

- 160205 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160205 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


