Title: Issue 8 ~ 蠎之禅 
Date: 2012-04-06 
Tags: Weekly,Pycoder,Zh 
Slug: issue-8 
# Hi Pythonistas. 


首家赞助商已落实!
正如大家所知, MailChimp 不便宜,
特别是我们的订阅量增长这么快!
所以,我们必须采取措施确保收支平衡,
因此决定启动赞助机制.
赞助方,必须是在Python 社区有突出信誉的公司.

嵌入的广告必须是清雅的, 不显眼的,
内容必须完全由我们自行策划, 而且一直这样.

如果针对赞助商,还有什么问题/意见,请回复邮件说明.

RSS 和归档在
[这儿](http://feeds.feedburner.com/pycodersweekly)
, 以及 
[这儿](http://pycoders.com/archive.html)
.


成为巾帼或英雄, 作对的事儿, 要Follow 
[@pycoders](http://twitter.com/pycoders)
如果你还不明白当期标题的含义,
进入命令行输入 

    python -m this



Enjoy!


--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #8) : Zen of Python](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=454b9dc99c)


## 新闻与开发动态

- [Circus 0.2 发布ed](http://pypi.python.org/pypi/circus/0.2)
Circus 是类似 supervisord 的进程监管工具,
现已发布0.1 版本,
项目很有意思,由
[@tarek_zaide](http://twitter.com/#!/tarek_ziade)
以及
[benoitc](http://twitter.com/#!/benoitc)
创建


- [rauth](https://github.com/litl/rauth)
恨写一遍又一遍相同的OAuth的代码吧?!
这儿是来自 LITL
包含完全测试的模块,
目测,这事儿可以了了!



## 讨论
- [字串重排的最佳方式?](http://www.reddit.com/r/Python/comments/rm3ii/whats_the_best_way_to_reorder_strings/)

这是在 rediit
[/r/python](http://reddit.com/r/python)
频道引发的一个伟大的讨论,
有关对字符串排序以及重新的最好方式,
以及在 Python 中如何得到各种排列组合,
包含大量的神奇代码,相当深入的对 itertools 的使用经验,
值得关注.

- [Python中最困难的?!](http://www.jeffknupp.com/blog/2012/03/31/pythons-hardest-problem/)
过去十年, 没有任何讨论能同时引发新手以及专家一置的挫折以及好奇.
这就是 全局锁!
相关文章,此篇甚佳, 评注也异常有料!



## 项目

- [Django Sampler](https://github.com/colinhowe/djangosampler)
引自仓库:"Django Sampler
允许对你的查询(SQL, Mongo,等)进行取样,给出慢执行.
并成组的指出在你的代码中哪里引发的查询.
"
目前支持:
Django SQL, Django Requests, Celery and MongoDB.



- [Melopy](http://prezjordan.github.com/Melopy/)
玩弄声音的Python 库!
是对音乐发烧友梦想中的好物!
通过简单的代码,支持对声音播放/渲染 等等操作,
作出你自个儿的音乐!


- [DCPU16py](https://github.com/jtauber/dcpu16py)
名为
[0x10c](http://0x10c.com/)
的工具,能在Notch的新游戏 中设计船舶,
虽然只能给每种船提供少数模拟资源,
但是
[James Tauber](https://twitter.com/#!/jtauber)
以前折腾过类似的模拟器,所以,这次很容易的整了出来.

## 文章

- [回调是数据过程的抽象](http://dreid.org/2012/03/30/deferreds-are-a-dataflow-abstraction/)
有趣的文章,
讨论如何使用 JavaScript 中的回调方式,
在 Python(
具体是[Twisted](http://twistedmatrix.com/trac/)
)中实现, 并使代码简洁,易读,好测试!



- [对运行中的 Python 和 Django 进行标记以及追踪](http://www.saltycrane.com/blog/2011/06/notes-tracing-code-execution-django-python/)
文章就如何使用
[trace](http://docs.python.org/library/trace.html)
来追踪Django 的执行
给出了一些注意事项,
还通过 [Django Plugin](https://github.com/saltycrane/django-trace)
提供了额外的管理命令,
来对 Django 项目进行执行跟踪!



- [Python HTTP的未来](http://kennethreitz.com/the-future-of-python-http.html)
[Kenneth Reitz](http://twitter.com/#!/kennethreitz)
探讨了Python 进行HTTP 响应的特性,
以及如何接入 
 [Werkzeug](http://werkzeug.pocoo.org/)
.
未来可以共享的核心 HTTP 库,
已经启动有关仓库在 
  [here](https://github.com/core)
  .


- [Python中的计数](http://rhodesmill.org/brandon/2012/counting-without-counting/)
非常有趣的讨论,
有关如何在Python 的通用循环体中,
使用 range() 或 xrange(),
甚至执行体本身并不需要这种整数.
作者探讨了其它可实现相同目标的选择,逐一讨论,
对比.



- [Python objects, types, classes and Instances - 辞汇](http://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary/)
继 [Python 可调用的内因](http://eli.thegreenplace.net/2012/03/23/python-internals-how-callables-work/)
之后,
作者对以往讨论的各种内部机制,进行了梳理,
重新说明了各种条目的含义,
对以往文章关注的朋友,这篇必须认真读哈!


# 是也乎

- 131020 [Zoom.Quiet](http://zoomquiet.org/) 用时42分钟完成快译.
