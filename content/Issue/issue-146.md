Title: 蠎周刊 Issue 146: Adorn
Slug: issue-146
Date: 2014-12-21 14:14
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #146): Adorn](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=d973d8a93e&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,


这将是 2014 最后一期了,
我们将休假一周,
然后开始准备 2014总回顾,
感谢伟大的一年,
期望明年能更好.

大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)



## 新闻

- [PyCon 2015 教程议程发布](http://pycon.blogspot.ca/2014/12/pycon-2015-tutorial-schedule-announced.html)

PyCon 2015 的教程安排已经发布,
请及时调整你的行程.


blogspot.ca

Shared by @mgrouchy
 

- [注意 Django 官网的新设计](https://www.djangoproject.com/weblog/2014/dec/15/announcing-django-website-redesign/)

10年了, 丫的终于升级设计了!

djangoproject.com

Shared by @mgrouchy

## 讨论

- [俺有机会给25位机构工程师教 Python ,几小时以内应该吼什么?](http://www.reddit.com/r/Python/comments/2pop8a/i_have_a_few_hours_to_teach_python_to_25/)

reddit.com

Shared by @myusuf3

(`是也乎:`
满满的爱哪,,,,)


## 项目
- [iterstuff](https://github.com/mobify/iterstuff)

有关用迭代来干活的工具集.

github.com

Shared by @benlast
 

- [qutebrowser](https://github.com/The-Compiler/qutebrowser)

基于 PyQt5 和 QtWebKit 的浏览器,
键盘驱动,vim 样绑定!
想了解怎折腾出来的? 看代码吧.

github.com

Shared by @the_compiler
 

- [mochi](https://github.com/i2y/mochi)
A dynamically typed programming language for functional programming and actor-style programming. Its interpreter is written in Python 3. Worth checking out, even if only you are interested in how an interpreter is written.

动态类型的函式语言,
其解释器使用 Py3 完成!
值得体验, 即使你只是对完成一个编译器有兴趣.

github.com

Shared by @mgrouchy

(`是也乎:`
目测是原先那帮用 erlang 写游戏的团队折腾出来的,
如果你对 Py3 各种不兼容的小特性很难忍受,
那就用一种全新的语言来运行 Py 3 吧;-)

- [fake2db](https://github.com/emirozer/fake2db)


实用,支持 sqlite/mysql/postgresql/mongo 主要DB,
协助你为测试创建对应的徦数据库(但是真实可用!-)

github.com

Shared by @myusuf3
 

- [addict](https://github.com/mewwts/addict)

提供了完备的 settable/gettable 语法和属性的库.

github.com

Shared by @mgrouchy
 
(`是也乎:`
因为 Python 的开放,
这样任意追加底层数据库类型好嘛?)


- [deeppy](https://github.com/andersbll/deeppy)

对 state-of-the-art 深度学习提供了一个不错的 Python 接口.

github.com

Shared by @mgrouchy
 

- [clip.py](https://github.com/willyg302/clip.py)

又一个组合式 CLI 创建工具,
可以轻松的设立命令/子命令,并传递参数.

github.com

Shared by @mgrouchy
 
(`是也乎:`
感受一下相关的 logo 
![githubusercontent](https://camo.githubusercontent.com/bd0c2916fdd6b11fe20382d4d5e724ff0e66e2e4/68747470733a2f2f7261772e6769746875622e636f6d2f77696c6c79673330322f636c69702e70792f6d61737465722f636c69702d6c6f676f2e706e67)

![click.png(PNG 图像,420x175 像素)](http://click.pocoo.org/3/_static/click.png)

对于这种使用装饰符来名声的,
大家好象更加喜欢使用基于文档的 [docopt](http://docopt.org/)
为什么?
...
)

- [pypgTAP](https://github.com/itissid/pypgTAP)

简化你的 pg 开发周期,
自动化测试存储过程什么的...

github.com

Shared by @mgrouchy

(`是也乎:`
随着 pg 9.x 系列的发布,
明显的针对 pg 的工具增加了,这说明什么?
说明 pg 的春天的确到来了!-)

## 文章

- [Python 的 `NotImplemented` 类型](http://shahriar.svbtle.com/python-notimplemented-type)

一切你想到(没想到)的有关 `NotImplemented` 类型的事儿,都在这儿了

svbtle.com

Shared by @STajbakhsh
 

- [混淆 "Hello world!"](http://benkurtovic.com/2014/06/01/obfuscating-hello-world.html)
Ever wonder how some of these crazy obfuscated python programs work? Check out this detailed explanation of how it all works.

benkurtovic.com

Shared by @mgrouchy

(`是也乎:`
真心是个自虐又 bigger 的思路,可以折腾个标准库出来,
这下网络传送数据就有安全保证了...
感受一下....谁说用 Python 写不出来难懂的代码的!?

    #...
    (
        *(lambda _, __, ___: _(_, __, ___))(
            (lambda _, __, ___:
                [__(___[(lambda: _).func_code.co_nlocals])] +
                _(_, __, ___[(lambda _: _).func_code.co_nlocals:]) if ___ else []
            ),
            lambda _: _.func_code.co_argcount,
            (
                lambda _: _,
                lambda _, __: _,
                lambda _, __, ___: _,
                lambda _, __, ___, ____: _,
                lambda _, __, ___, ____, _____: _,
                lambda _, __, ___, ____, _____, ______: _,
                lambda _, __, ___, ____, _____, ______, _______: _,
                lambda _, __, ___, ____, _____, ______, _______, ________: _
            )
        )
    )

)

- [json vs simplejson vs ujson](https://medium.com/@jyotiska/json-vs-simplejson-vs-ujson-a115a63a9e26)

非常详尽的 PK 测试,
对流行的几个 Py JSON 解析库,
结论是: ujson 最快

medium.com

Shared by @mgrouchy

(`是也乎:`
俺只想说 medium 越来越靠谱了哪,,,
虽然不兼容 md 也越来越多人使用了,,,)

- [令 Python 认证更快](https://stormpath.com/blog/making-python-authentication-fast/)

爽文, 解释了如何选择框架来架应用中用户认证.

stormpath.com

Shared by @rdegges
 

- [编程令机械人玩 "Sushi Go Round" Flash 游戏](http://inventwithpython.com/blog/2014/12/17/programming-a-bot-to-play-the-sushi-go-round-flash-game/)

非常伟大的,
很漂亮的代码,构建一机械人, 通过 PyAutoGUI 玩 flask 游戏.

inventwithpython.com

Shared by @mgrouchy
 
(`是也乎:`
细思恐极,意思是以后游戏代打产业必须升级了?!)

- [用 Python 检测面部关键点](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)
俺非常沉迷 Kaggle 比赛中的各种故障解决.
这次,我们用 Python 搞定了检测面部关键点 !

检测面部关键点

danielnouri.org

Shared by @myusuf3
 

## DAMA
(`大妈私人无责任播报`)


# 是也乎

- 141221 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 141221 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
