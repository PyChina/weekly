Title: Issue 9 ~ >>> 
Date: 2012-04-13 
Tags: Weekly,Pycoder,Zh 
Slug: issue-9 
# Hi Pythonistas. 

It's that time again, tons of super useful open source projects this week. We enjoyed hearing from everyone last week really makes writing this newsletter that much more enjoyable. Let's get to business. 

又到点儿唠嗑了!
本周有成吨的好项目!
我们真心稀饭上周大家的欢叫.
让我们继续...

RSS 和归档在
[这儿](http://feeds.feedburner.com/pycodersweekly)
, 以及 
[这儿](http://pycoders.com/archive.html)
.

成为巾帼或英雄, 作对的事儿, 要Follow 
[@pycoders](http://twitter.com/pycoders)

如果没明白本周的标题,
在终端里打开 Python ,
你首先看到的是什么?!

Enjoy!


--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #9): >>>](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=d7c6c25c6c)

## 新闻与开发动态
-[Python 2.6.8, 2.7.3, 3.1.5, and 3.2.3 Released](http://mail.python.org/pipermail/python-list/2012-April/1290792.html)
一系列的版本已经发布,
包含了基础类型 hash,dict,set 相关的安全修复.
更多细节在链接指向的文档.

- [Gevent 1.0b2](https://bitbucket.org/denis/gevent/src/tip/changelog.rst#cl-7)
Gevent 的1.0 Beta 2 版本已发布.
是时候给你的 sockets 打上 [monkey patching](http://www.gevent.org/intro.html#monkey-patching) 了!


- [pandas v.0.7.3](http://pandas.pydata.org/pandas-docs/dev/whatsnew.html)
虽然相比 0.7.2 只是个小版本升级,
但是,真的修复了好些 bug,并增加了不错的新特性.
值得一用,
来自 [Wes](https://twitter.com/#!/wesmckinn)
的美好贡献!


- [Virtualenvwrapper 3.2](http://blog.doughellmann.com/2012/04/virtualenvwrapper-32.html)
最新版本,已能很好的支持 非 CPython 的环境管理,
例如: pypy, Jython 等等!




## 讨论

- [第一门语言最应该学哪个, Python or JavaScript?](http://www.quora.com/Is-it-better-to-learn-Python-or-JavaScript-as-a-first-language)

在Quora 上激荡讨论的一个好问题,
学习编程,最应该从哪们语言入手? Python 还是 JavaScript ?


- [[Python-Dev] 在 CPython 中实验 STM](http://mail.python.org/pipermail/python-dev/2012-April/118665.html)
这是在 [Python-Dev] 列表进行中的,很有意义的讨论,
有关是否能用 STM(软件事务性内存,Software Transactional Memory)
替代 
[GIL](http://en.wikipedia.org/wiki/Global_Interpreter_Lock)
应用在 CPython!
如果关心 Python 语言本身的发展,这一线索值得关注!


## 项目

- [docopt -- 能令你微笑的 pythonic 参数解析方式.](https://github.com/halst/docopt)
非常COOL 的模块,
使用 docopt 来处理参数,
你只需在模块的文档字串部分,自然的描述就好,
其它的交给 docopt 完成解析.
牛叉极了!


- [curlish](http://packages.python.org/curlish/)
安装只需在终端输入:
`curl -L http://bit.ly/curlish | bash` 
Curlish 是支持 Oauth 2.0 的 cUrl .
允许你作各种NB 的事儿,
比如,注册 OAuth 2.0 的网站,
并记忆身份令牌. 非常 COOL,现在就用之!

- [Inline Styler](https://github.com/dlanger/inlinestyler)
包含HTML 样式的电子邮件,属于黒科技!
CSS能工作,
但是只能使用内嵌的各种元素(还不一定管问!)
足以令人沮丧, 调试也慢.
现在不用丧气了!
这侦支持外部CSS以及直接元素.
任何人都能搞出漂亮的 HTML 邮件了!



- [PyV8 Packaged for OSX](https://github.com/brokenseal/PyV8-OS-X)
PyV8 是对 Google 
[V8引擎](http://code.google.com/apis/v8/)
的一个Python 包装!
在 JavaScript 以及 Python 对象之间打通了桥梁.
如果你在 MAC 环境中,赶紧体验一下吧!

- [Jeeves Framework](https://github.com/silent1mezzo/jeeves-framework)
Jeeves 是个框架,
能用一个命令创建 IRC 机器人.
类似大家知道的群应答机器人,
或是 [hubot](http://hubot.github.com/).
但是,非常COOL 的是,支持各种 IRC 的选项.


- [Snippets](http://trilandev.com/snippets/)
Snippets 是个代码片段生成器,
就象用 Jekyll/Pelican 等生成 Blog,
不过,它只生成 代码片段.

- [Slumber](http://slumber.in/)
Slumber 是个专门为定制 RESTful 接口而创建的库.
Slumber 帮忙抽象掉网址,序列化和处理请求.
看起来很有用,现在就体验一下吧!

## 文章
- [Python 作弊条儿](http://imgur.com/tpze9)
我总是会不断寻找各种好用的Python 技巧.
精心制作的作弊条儿,
能阻止我搜索类似日期格式化等等小事儿,
绝对值得下载并打印出来!



- [Python Decorators入门](http://www.thumbtack.com/engineering/a-primer-on-python-decorators/)
对 Python 的修饰器进行了完备的描述,
那些想写类似文章的,应该先看一下这篇,就没有然后了.

- [基于Brewery的数据流式处理](http://blog.databrewery.org/post/21021110882/data-streaming-basics-in-brewery)
Brewery 是个进行数据分析/审计的Python 框架.
基本原理是通过分布式的节点来处理结构化数据.
本文带领你亲自完成一个节点的建立,并进行数据流处理.


- [用C 扩展来增强Python 的 generator/yield.
](http://eli.thegreenplace.net/2012/04/05/implementing-a-generatoryield-in-a-python-c-extension/)
如果你在折腾 Python 的C 扩展接口,
本文肯定对你胃口!
重点在如何使用 C 扩展来提高 Python Generator/Yield 的运算效率,
文章通过彻底的演进,最后给出了完备的代码!



# 是也乎

- 131020 [Zoom.Quiet](http://zoomquiet.org/) 用时42分钟完成快译.

