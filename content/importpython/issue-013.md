Title: 蠎加载 13
Slug: importpython-13
Date: 2014-12-19 23:32
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/80)


原文: [Issue 13](http://importpython.com/newsletter/draft/13/)


## 该读
~ 文章, Blog, 教程...


- [构建扩展性足够好的 Python 3 REST 应用](http://importpython.com/click/track/09bc9e4d2ce0e61cf07d0dcf2d9a5fb606d0512f?source=www.giantflyingsaucer.com)

开发者经常在一行代码没写前, 就陷入讨论如何扩展应用,
当然,这有助思考每个应用的可扩展性....

- [性能12日](http://importpython.com/click/track/1fcd20104c53bcf03b5b886634608eaa2e3c0f5d?source=www.revsys.com)

可能有关性能你怎么着都知道一些技巧,
可惜, 可能你根本没有学到真正有用的,
尽管有丰富的在线信息,
但是,我们依旧被爱好者的无知而惊讶....

(`是也乎:`
是有12节的系列分享,刚刚完成了前8篇,
不过,有关 web 应用的整体效能建议,
mozilla 等等有完备的 checklist 值得收藏!)

- [Django 官网全新设计](http://importpython.com/click/track/4390bbe29543d39609809400af224c6190a869e7?source=www.djangoproject.com)
The Django project is excited to announce that after many years, we're launching a redesign of our primary website. Have a look.

- [别在 Python 中折腾的事儿](http://importpython.com/click/track/181cebdb4d179e84b805005ee5fa3ae232382352?source=www.airpair.com)

这是帮助Pythoneer 从 trolls 们营救出来的手册.

(`是也乎:`
看一次乐一次...

    "Premature optimization is the root of all evil 
    (or at least most of it) in programming." -- Donald Knuth
    "过早优化是一切罪恶的根源(在绝大多数情况中)在编程" ~ 高德纳
)

- [你的Django 故事: 遇见 Susan Tan](http://importpython.com/click/track/a228b436aa7b25ca8f3fff4064edf309be57c060?source=blog.djangogirls.org)

Susan 是位 Piston 的程序媛,
在三潘一家云计算公司.
Susan 很喜欢 Python 的 web 应用框架,
她是基于 Django 的应用 www.openhatch.org 核心提交者,
同时也在用 Rotten Tomatoes 来折腾.

- [json vs simplejson vs ujson](http://importpython.com/click/track/3871148d6d23f1ad9b0b9482af1bff2d740154b7?source=medium.com)

(`是也乎:`蠎周刊也曰了.)

Without argument, one of the most common used data model is JSON. There are two popular packages used for handling json?—?first is the stock json package that comes with default installation of Python, the other one is simplejson which is an optimized and maintained package for Python. The goal of this blog post is to introduce ultrajson or Ultra JSON, a JSON library written mostly in C and built to be extremely fast.

- [如何用 ast 从 python 文件中提取文档字串?](http://importpython.com/click/track/1c7c390b1f46d39276aa99e77da2598fd3038ae9?source=gabrielelanaro.github.io)

有关 ast 模块的具体案例,
问题来了: 什么是 ast ?
简单的说,这是个神奇的模块,
用来理解 python 代码语法的,
能将 代码分解为语法成分,
理解了她就可以基于 Py 开发自个儿的 DSL 了,
又有问题了: 什么是 DSL ?


- [Making a Mockery of Python](http://importpython.com/click/track/b2bba807ac155be3c91104121dbd30a89bca6a92?source=engineroom.trackmaven.com)


Mocking 是这样一种技术,
通过伪造模块的外围环境,来纯化我们的测试过程,加速测试,
这里探讨了 Py 世界中的 Mocking 技术.
分享如何令我们测试的多快好省.

- [应该用哪种 Python 代码检查器?](http://importpython.com/click/track/74491167a316bcf2bd6a22cf9766cd83cb308624?source=www.reddit.com)

有很多包可用的了 pylint, pyflakes, pep8, 和 pep257,
看起来 pep8 和 pep257 一样好,
但有些功能是包含在其它工具中的了.

- [Mochi a programming language using Python3 Interpreter](http://importpython.com/click/track/94ade11fe6521ef9549a9a40932be4fe6094c770?source=github.com)

(`是也乎:`蠎周刊曰了,这是个神奇的语言,值得期待)

Mochi is a dynamically typed programming language for functional programming and actor-style programming. Its interpreter is written in Python3. The interpreter translates a program written in Mochi to Python3's AST / bytecode.

- [The Python Concurrency Story, Part 1](http://importpython.com/click/track/97b5660ac9f5b6f5f27ea89eddfa8701a04951a0?source=migrateup.com)

未来是并发的,理解现代操作系统中的并发原语,不仅仅令你成为更好的 Python 程序猿,
而且有助于余生里掌握每一个语言更好的开端.

(`是也乎:`
无法直视的广告辞哪,为了余生,跟了!-)

## 项目
~ 包/模块/库/片段...


- [qutebrowser](http://importpython.com/click/track/f72fd9156811eef16bbe9e4bd28e7f30ae440573?source=github.com)
    - 129 Stars, 16 Fork


(`是也乎:`蠎周刊也曰了,纯geek 的浏览器, 小白退散!-)

qutebrowser is a keyboard-focused browser with with a minimal GUI. It's based on Python, PyQt5 and QtWebKit and free software, licensed under the GPL. It was inspired by other browsers/addons like dwb and Vimperator/Pentadactyl.

- [Dshell](http://importpython.com/click/track/1afb1846ffbd711807f26ff6a4781f707c63c639?source=github.com)
    - 13 Stars, 2 Fork

Dshell是网络取证分析框架

- [img-data-encode](http://importpython.com/click/track/693a6a2c2ab5be9a6c3482387f3478ebd0f56bbe?source=github.com)
    - 2 Stars, 0 Fork

在图像中嵌入数据,
发源自俺的小嗜好, 想探知,在不改变图像视觉效果基础上,
能的混入多少数据?

- [django-quill](http://importpython.com/click/track/dc6baf85e16f35bd6e05cd3a619d2eda3363acef?source=github.com) 
    - 3 Stars, 0 Fork

轻松嵌入  Quill.js 在 Django 管理器界面中.
Quill 是免费/开源的 WYSIWYG 编辑器.
通过接口你可以定制满足你的需要.


- [ansible-playbook-digitalocean](http://importpython.com/click/track/af9d4e0414a09bf07251e8b507f506293574e6f5?source=github.com)
    - 1 Stars, 0 Fork

针对 DigitalOcean 的简单 Ansible 剧本


- [elasticsearch_dsl](http://importpython.com/click/track/d992d78b7ecbb95bb7244b2b29160ace45ea4fa3?source=github.com)
    - 1 Stars, 0 Fork

用Python 实现的 针对 Elasticsearch 的 DSL

(`是也乎:`
哗咧! 需要!收!)

## 曰了
~ Tweets~ Tweets


- 俺到底应该用 Py2 还是 Py 3? `#python 综合对比表:` http://t.co/uwje8l8LOq

[@_marcelo_d](https://twitter.com/_marcelo_d/status/545723728869728256)

(`是也乎:`
![B5JOXCoIAAEjlrC.png(PNG 图像,459x303 像素)](https://pbs.twimg.com/media/B5JOXCoIAAEjlrC.png)

答案是这么的无法直视...
)

# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)

- 14121 用时 42 分钟完成快译.
- 141221 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
