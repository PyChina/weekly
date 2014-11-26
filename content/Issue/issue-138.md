Title: Issue 138: 强壮
Slug: issue-138
Date: 2014-10-26 21:15
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Py万物 的周刊

亲,

大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


--

原文: [Pycoder's Weekly (Issue #138): Strong](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=e133864a0a&e=889f3f6a05)

## 新闻

- [PyPy3 2.4.0 发布!](http://morepypy.blogspot.ca/2014/10/pypy3-240-released.html)


是的终于发布了,更多细节官网去看!

blogspot.ca

Shared by @myusuf3

## 讨论

- [和Python 一齐更好](http://www.reddit.com/r/Python/comments/2k5uws/becoming_better_with_python/)

reddit.com

Shared by @myusuf3
  

(`是也乎:`
这其中 [ut2222 對 Becoming better with Python 的留言](http://www.reddit.com/r/Python/comments/2k5uws/becoming_better_with_python/clib3fw)
最有可操作性:

1. 变成专职 Py 程序猿
2. 学用更多好工具 ~ git 等等
3. 学用其它语言 ~ js 等等
4. 学习 SQL
5. 学习 NoSQL
6. 折腾点儿异步 ~ celery, websocket 什么的
7. 开始写大型项目, 百万行规模,各种优化/缓存/同步什么的..
)

## 项目

- [lenscap](https://github.com/honza/lenscap)

Lenscap 是用来生成照片流式静态网站的工具.

github.com

Shared by @myusuf3
 
(`是也乎:`
和今年 PyCon2014China 官网的改造思路一样,
也使用了 yaml 作为数据格式)

- [schematics](https://github.com/schematics/schematics)


Python 库基础上的类型描述组件,
能对数据类型进行对比/合成为新结构,并进行验证和转换!

github.com

Shared by @mgrouchy
 

- [prospector](https://github.com/landscapeio/prospector)


又一个 Python 代码分析器,
能发觉 违反约定/复杂 或是 潜在的问题!

github.com

Shared by @myusuf3
 

- [teleport.py](https://github.com/cosmic-api/teleport.py)

基于 JSON 的一个序列化系统,
支持输入验证.

github.com

Shared by @mgrouchy
 

- [flask-dance](https://github.com/singingwolfboy/flask-dance)

内置了 OAuth 支持,
以便我们的 Flask 应用接入 oauthlib 以及相关请求.

github.com

Shared by @mgrouchy
 

- [carbonate](https://github.com/jssjr/carbonate)

管理图形集合的一组工具集.

github.com

Shared by @mgrouchy
 

- [pixie](https://github.com/pixie-lang/pixie)

Pixie 是轻量级 lisp 样 shell 脚本包装器.
虽然处于 早期状态,但是,已经可以开始赏玩儿了.

github.com

Shared by @myusuf3
 

(`是也乎:`
喜大普奔的事儿哪!
基于 Clojure 的构想, 内置在 RPython 中...
这是要抢 Lisp 的饭碗哪,,,
)

- [django-html-validator](https://github.com/peterbe/django-html-validator)

工具用以对你 Django 应用生成的 HTML 进行验证.

github.com

Shared by @mgrouchy
 

- [djangae](https://github.com/potatolondon/djangae)

想在 GAE 中用 Django?
这是最佳选择!

github.com

Shared by @mgrouchy
 

- [vimswitch](https://github.com/priomsrb/vimswitch)

令 Vim 配置便携化,可以在任何地方切换为你的专有配置.

github.com

Shared by @mgrouchy
 
(`是也乎:`
就是 virtualenv 的思路哪,
可是,为毛 Vim 界没有先折腾出类似工具?)

- [cymem](https://github.com/syllog1sm/cymem)

为 Cython 提供了两种小的 内存管理助手.

github.com

Shared by @mgrouchy
 

- [gizeh](https://github.com/Zulko/gizeh)

简洁的矢量图形工具!
可以在 blog 中看到实际案例
(配置 MoviePy 作动画!)

github.com

Shared by @myusuf3
 
(`是也乎:`
基于 Cairo 折腾出来的.
![spiral](https://d13yacurqjgara.cloudfront.net/users/583436/screenshots/1692659/spiral.gif)

猜猜这个动画的生成脚本有几行?
)

- [wolf](https://github.com/slawekj/wolf)

交易平台,支持实时的金融数据可视化, 以及历史数据交互式查找!

github.com

Shared by @myusuf3
 

- [flaskbb](https://github.com/sh4nks/flaskbb)

用 Flask 写的论坛系统.

github.com

Shared by @myusuf3
 

- [echo](https://github.com/itsnauman/echo)

一个微型库,
只作一件事儿,
对失败的操作重试!

github.com

Shared by @itsnauman

(`是也乎:`
当然的在 web 领域最常用,
比如说对 google 网站反复尝试请求10次...

```
import requests
from pyecho import echo

@echo(10) # Retry function upto 10 times
def fetch():
    r = requests.get('http://google.com')
    return r.text

fetch()
```

)

## 文章
- [高性能 Python 扩展: 第一部分](https://www.crumpington.com/blog/2014/10-19-high-performance-python-extensions-part-1.html)
- [高性能 Python 扩展: 第二部分](https://www.crumpington.com/blog/2014/10-21-high-performance-python-extensions-part-2.html)

有关使用 C 来构建 Python 高性能扩展的系列文章.
笔者展示了如何使用 NumPy 的 C 接口来创建 Python 用的扩展组件.

crumpington.com

Shared by @mgrouchy
 

- [subprocess.Popen() 或滥用原生 Windows 执行文件?](http://pyright.blogspot.ca/2014/10/subprocesspopen-or-abusing-home-grown.html)

blogspot.ca

Shared by @mgrouchy
 

- [Flask 和视频流](http://blog.miguelgrinberg.com/post/video-streaming-with-flask)

如何通过你的 Flask 和 webcam 发布视频流的教程...

miguelgrinberg.com

Shared by @mgrouchy
 


- [Enlivepy 一种与众不同的方式来写 Py 的 HTML 模板](http://makkalot.github.io/posts/2014/Oct/22/enlivepy-html-transformation/)

基于Python 版本的 Clojure 库 Enlive,
在 Django 中用更加有趣的方式来折腾模板!

github.io

Shared by @mgrouchy

(`是也乎:`
听起来很有趣
但是,是否上的了手,看各自体验了.
是种无侵入式的 jQ 式的脚本注入...)

## DAMA
(`大妈私人无责任播报`)


# 是也乎

- 141021 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 141020 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
