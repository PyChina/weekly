Title: 蠎加载 14
Slug: importpython-14
Date: 2014-12-27 18:18
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/80)


原文: [Issue 14](http://importpython.com/newsletter/draft/14/)


## 该读
~ 文章, Blog, 教程...

- [eBook 预览: Flask 框架Cookbook](http://importpython.com/click/track/6b86e87342d1ffde10d78241b591332a6837c0ff?source=feedproxy.google.com)
    - flask,book review

Packt 出版社刚刚发送俺了一份复本,
是 Shalabh Aggarwal 写的 "Flask Framework Cookbook" 电子版,
值得关注.

- [面向 Django web 程序猿的简要 Docker 容器介绍](http://importpython.com/click/track/c3e8dde1e669b0aae197cf80042817d9eab78977?source=www.rkblog.rk.edu.pl)
    + django,docker

Docker 是种能隔离应用运行的环境.
使用 Linux 容器可以将软件层从基础体系中分离出来.
不在依赖硬件虚拟环境,比如 Virtualbox.
Docker 能在帮助开发者完成 web 应用的开发和服务部署,
让作者展示怎么来的..

- [pdb - 在 Django 中进行 Python 调试.](http://importpython.com/click/track/7fd138567117c0a5aaa484e8431f2a5c10236e64?source=mike.tig.as)
    - django,pdb,debugging

这是一个使用交互式调试环境来折腾你的应用的简要概述,
并提供了实例表述了最基本的调试情景,值得由此入门.


- [在 M$ 中编译 Python](http://importpython.com/click/track/608702fc4920934473e6f2cb97b8f3d749fe486e?source=blog.ionelmc.ro)
    - windows

如何在 Windows 中通过 VS 的Python 扩展用 C++ 完成编译?
而且兼容 Py 2.x 和 3.x

- [将 SQL 对 pandas 进行双向解析](http://importpython.com/click/track/8038e707fb1aa448f827c63537a2b6fa28d88745?source=www.gregreda.com)
    - pandas,sql

当俺开始学习 pandas 时 (并从后台数据库的背景),
发现将 SQL 和 pandas 并列等价对比时,能加速理解,
重要的是,这种形式,适用俺的工工作流.

- [Python's `NotImplemented` Type](http://importpython.com/click/track/fc186fe3cf9bf4a9838d5a238640c0b0d08bef0e?source=shahriar.svbtle.com)
    - exception

(`是也乎:`上周的蠎周刊已经曰过了,,,很神奇的数据类型..)

This post discusses Python's NotImplemented built-in constant/type; what it is, what it means and when it should be used.

- [你的 Django 故事: 遇见 Dori Czapari](http://importpython.com/click/track/a63acf3afd6a77e38ce715cc683c238359006c28?source=blog.djangogirls.org)
    - django,interview
Dori 是布达佩斯 Allmyles 的程序媛.
她参加了 Berlin 第一届 Django 程序媛工作坊,
现在是 Django Girls 阿姆斯特丹 的教官,
布达佩斯 Django Girls 的组织者.

- [来自 Packt 的 $5 Python 图书](http://importpython.com/click/track/562b178dd710d08f238fe37e3e8710aab2426dd9?source=feedproxy.google.com)
    - ebook

Packt 出版社联系了俺,
说他们能在各大平台上以 5$ 发信 电子书和视频,
目测他们有很多不同的 Python 和 Python 相关好物,统一 5$ ,值得一看.

- [如何在 DigitalOcean 上 Nginx 身后用 Gunicorn 作服务器发布 Python 应用](http://importpython.com/click/track/b2ce6f32869b26c455d5585a39caf12f42d53179?source=www.digitalocean.com)
    - gunicorn,wsgi,nginx

很赞的手册,
将 Python WSGI 应用的部署说了个通透.
如果你想使用 Gunicorn 作为 Web 服务器来部署,
此文必须看哪.

- [混淆 "Hello world!"](http://importpython.com/click/track/41b99ea928c2df4262afb23f18fb491bc37550eb?source=benkurtovic.com)

(`是也乎:` 上周蠎周刊就曰过了,的确很 brain break 的思路.)

How complicated can one make print "Hello World" ?. This entry got first place in this Code Golf contest to create the weirdest obfuscated program that prints the string "Hello world!". The Author decided to write up an explanation of how the hell it works. So, here's the entry, in Python 2.7.

- [Why zip when you can map ?](http://importpython.com/click/track/57ebdf0ad4f6daeebcdcd321a1e0268c3c0aadac?source=wordaligned.org)

如果你有一组列表,想合并后输出,
当然可以用 zip.
只是别忘了,咱们还有 map 哪,
这货天生就是并行的,能接受多个对象输入!
根本用不到 zip 出场的了.


- [Django 2014 的开发失误](http://importpython.com/click/track/73d36edef0a7ca8f75da1c46416590a89cf75f09?source=medium.com)
    - django

俺花了点时间,
以 Django 为背景, 从发展的角度再思考2014...

(`是也乎:`
绝对髙能,这种级别的吐糟就不是俺能理解的了,
请高人点评...)

## 项目
~ 包/模块/库/片段...

- [eatiht](http://importpython.com/click/track/941e60c9ea66b89e2995ed3092158eaa569d6e72?source=github.com)
    - 114 Stars, 6 Fork

从 html 文档提取文章内容的小工具.

(`是也乎:`
又一个,随着 H5 的发布,以及各种 AJAX 的折腾,
早年类似工具都无力化了,
记得 好看薄 创始人的老婆都写过一个类似的.)

- [loggy](http://importpython.com/click/track/a8eed0ae73150fdc747d959f280ddbc8b7b8c9e6?source=github.com)
    - 16 Stars, 0 Fork

修饰器样的日志工具,
每当函式调用时激发.

- [MetalAPI](http://importpython.com/click/track/16bad88b336baca30be908e05ff17bfb3e840a6a?source=github.com)
    - 15 Stars, 0 Fork

the Metal Archives(http://www.metal-archives.com/) 的 REST 接口,
世界上最大的重金属音乐百科式全书资源库!
此接口可从 "Encyclopaedia Metallum" 查询到所有重金属乐队的元数据,
包含专辑/成员/从属...
现在所有 metalhead hackers 或是 data enthusiasts
能开发各种赞的事儿了!

- [KindleGate](http://importpython.com/click/track/efe4b656beeac705f67a9a7bbf3fdc57b9882663?source=github.com) 
    - 12 Stars, 1 Fork

KindleGate 是个简单的 Flask 应用,
通过 Calibre 的 "ebook-convert" 命令行应用,
自动将 `*.epub` 图书,转换为 `*.mobi` 格式,
以供 Kindle 实验浏览器下载.

- [s3plz](http://importpython.com/click/track/e1ef8354beded0cd00a8ba64db02fef193db38c6?source=github.com) 
    - 4 Stars, 0 Fork

友好/极简的接口,
用以对 Amazon S3 写入/读出 Python 对象.

- [pymdstat](http://importpython.com/click/track/38434d5e17387c553c25210eb9e76ca171bb0ac7?source=github.com)
    - 3 Stars, 1 Fork

解析 /proc/mdstat 文件的 pythonic 库

- [PyChess](http://importpython.com/click/track/c340af62d671b92ebe97e195b31257799385d66b?source=github.com) 
    - 2 Stars, 0 Fork

Pygame 象棋, 国际的. 


## 曰了
~ Tweets~ Tweets

- Python: 从函式表中提取对象来调用函式  http://t.co/b4xaeEvgs6 http://t.co/hcDQs9KEG7 `#Python` via @dv_geek

[@Python_Quest](https://twitter.com/Python_Quest/status/548043013620916225)


# 国货

- [retsyo/libbpg-py](https://github.com/retsyo/libbpg-py)

全新 [BPG 图像格式](http://bellard.org/bpg/) 的纯 Py 实现!
作者在 CPyUG 列表中公开,自个儿曰没想出用什么...


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 141221 用时 42 分钟完成快译.
- 141221 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
