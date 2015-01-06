Title: 蠎加载 15
Slug: importpython-15
Date: 2015-01-03 15:15
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/80)


原文: [Issue 15](http://importpython.com/newsletter/draft/15/)


## 该读
~ 文章, Blog, 教程...

- [Django vs Flask vs Pyramid: Python Web 框架选择](http://importpython.com/click/track/7df2176d1067ab71eb3f42d0fbf7b7ed3fe13dc7?source=www.airpair.com)

(`是也乎`: 蠎周刊早已曰过)

Ryan built three identical apps in Django, Flask and Pyramid to illustrate the strengths and weaknesses of each one of them.

- [Python - 细微的性能提高](http://importpython.com/click/track/0e1df236ae20aeaf23b11909aedcd615e814e954?source=pythonfasterway.uni.me)

一些提高代码运行速度的建议.

- [用 MapMyFitness 和 Pandas 改进马拉松训练](http://importpython.com/click/track/41d80d16a0509387d8161ecbd49fb7358efe7734?source=www.davidketcheson.info)

使用 iPhone 上的 MapMyFitness (MMF) 来追踪里程和速度,
通过 API Jason Sanford 完成了这一 Python 前端,
可以轻松的通过 Pandas 进行探索!

- [事儿不该介神奇 - Flask 和 @app.route - 第一部分](http://importpython.com/click/track/94cce063476e459710067f28e90be9337981a031?source=ains.co)

"Things which aren't magic", 
这一系列文章,通过分享流行开源软件的 API ,
来从源语言角度分析,为什么!
第一部分, 分析了 Flask 为毛出现了
`"@app.route()"`
这种形式,以及显露函式的思考.

- [事儿不该介神奇 - Flask 和 @app.route - 第二部分](http://importpython.com/click/track/31f8e37f28e6253d801a2597a3a3d526dc9572ba?source=ains.co)

第二部分, 则调髙难度,
加入网址可变参数的能力支持,
在文章末尾我们将能支持预期的各种变化.

- [你的 Django 故事: 遇见 Claire Reynaud](http://importpython.com/click/track/5051ea34d27ce6168983eb101009c722292e2772?source=blog.djangogirls.org)

Claire 是位 iOS 和 Django 程序媛. 
她是法国 Saint Etienne 的自由职业者,
起初作为 JAVA 程序员在 Trango 工作,一个虚拟化办公公司.
后来进入了瑞士的 Epyx 公司,
在那里她遇见了 iOS 和 Django.
可以自行 flow 她 @ClaireReynaud



- [可怕的选择: MySQL | ionel's codelog](http://importpython.com/click/track/49f5f80db162ef146b57568825ee2a0d146330cd?source=blog.ionelmc.ro)

俺现在大量使用 MySQL, 
才发现,俺得照顾令人惊讶事儿.
基于 Django 和 MySQL 5.5 的背景,
对比 PorstgreSQL 的体验,这实在是可怕的经历.
俺不得不进行的各种折腾,以便令 MySQL 的行为更像一个真正的数据库.
(当然,针对 Django)

- [愉快的和 Python 一起玩函式](http://importpython.com/click/track/fda184262fc41e49f6f7f41f89c9c3b9d0457139?source=speedfulpanic.net)

Python 实在是种非常任性的语言,
允许我们进行各种范型的开发,包含函数式编程.
和过程式编程不同,
函数式编程甚至于明文禁止改变一个共享状态,
必须显式的调用改变元素的函式...

- [Python Twitter 教程 - 5 步实现通过 Python 发推](http://importpython.com/click/track/3d6fd7bb56134419e4351994191288523037d424?source=nodotcom.org)

一步步教会你使用 Python 完成脚本化的发推.

- [用 Python 实现计算机视觉](http://importpython.com/click/track/9669baa0a90cb0329e220eb0f7a074edef826211?source=programmingcomputervision.com)

Jan Erik Solem 的新书已经完成草稿:
"Programming Computer Vision with Python"
(截止 2012-3-12)以 创作共用许可发布.
注意: 此版本不包含最后的修订.

`PCV` 是基于此书发布的纯 Python 库.

- [用 Python 的 __slots__ 在内存中保存 9G 数据](http://importpython.com/click/track/ccf8cbe90aeecbc771a4594719bc10b203b640b7?source=tech.oyster.com)

默认情况 Python 用字典来保存对象的实例属性,
但是,此对象在编译时,只有很少的几个固定属性,
当你创建一百万个对象时,就显的浪费内存了.
不过,实际上你可以告诉 Python 不用字典,
而只分配固定空间的属性集,
通过 `__slots__` 来声明...


- [PyBoxes 教程 / 游戏的物理驱动.](http://importpython.com/click/track/aa75dac13c51e1e08fb9e990eac6dd216fac402b?source=www.reddit.com)

基本的物理引擎模拟 风/液体/圆的抗锯齿绘制(用 GFXGraw)/ colors.Goals 控制等等,
描述类似 Pymunk 的物理库,
如何应用在 PyGame 中.

- [又一个 awesome Django 列表,包含应用/项目/资源.](http://importpython.com/click/track/a5e05213b5e6467f92139cea2f6c4e9fe2301f2f?source=github.com)

Title says it all :)

- [用 Angular.js 来展示 Django 用户消息](http://importpython.com/click/track/5227bf7f1cebfa5e6ce7f0d98736409f68072cdc?source=birdhouse.org)

Django 的消息框架是个优雅的方案,
但是,俺从未使用它在 Django 网站上显示用户消息,
比如得芇 成功/失败/信息,
以便引导用户进一步操作.
直到...

## 项目
~ 包/模块/库/片段...

- [relational](http://importpython.com/click/track/24f1cc20b803aea58990a35553aadf61f615712c?source=github.com)
    - 40 Stars, 0 Fork

SQL-Alchemy 样儿更加人性化的 ORM

- [quicksafe](http://importpython.com/click/track/2935d9a0a3fe6ff15a1f12fdf7b52766eee2bf83?source=github.com)
    - 14 Stars, 0 Fork

quicksafe 是个很小的脚本,
提供了一个 GUI 的文本编辑界面来管理加密的笔记.
并存储在脚本自身.


- [pollywog](http://importpython.com/click/track/287abd7c13defa7536e283c3efcb549b6a8e5a43?source=github.com)
    - 11 Stars, 1 Fork

在正则表达式上将 Python 语法糖用起来,好味道!

(`是也乎:`
![camo](https://camo.githubusercontent.com/e31877f0c3809a9103c32aefc9b5cb1dcd110dd0/687474703a2f2f6d656469612e636861726c65736c65696665722e636f6d2f626c6f672f70686f746f732f70313431393832323431352e31392e706e67)

logo 太任性了,和代码一样...

    from pollywog import R
    ...
    url = raw_input('Enter a URL: ')
    if R/simple_url_re/url:
        print 'You entered a valid URL'
    else:
        print 'That URL appears to be invalid.'

)

- [twizhoosh](http://importpython.com/click/track/410a68c5d593a23d3cd4d6f530258f994e024401?source=github.com)
    - 6 Stars, 3 Fork

Twizhoosh 聪明的私人 twitter-bot,
纯 Python 写成,
主要用以改良可读性并快速增补功能.

- [walrus](http://importpython.com/click/track/e2ec92bf31342b1776bd4673ad4b2844ba26250d?source=github.com)
    - 5 Stars, 0 Fork

又一个轻量的 Redis 工具.

- [django-descriptors](http://importpython.com/click/track/252e316b402a9e1efa23c5789a0c69bb89af82b8?source=github.com)
    - 4 Stars, 1 Fork

在 Django 模型和字段中使用描述符来加强.

- [zeroless](http://importpython.com/click/track/cfd8240764b5ab5c8ac283709ee82c3ab1fa81d1?source=github.com)
    - 4 Stars, 2 Fork

然也,又一个 ZeroMQ 的包装,
不同 pyzmq,
力求接近 C++ 的实现,
目标是分布式系统用的最爽!


- [python-taipei-metro](http://importpython.com/click/track/e1506bff755aaee5a37eb9a672bca275552243ff?source=github.com)
    - 3 Stars, 0 Fork

Taipei MRT interchange route python library. Must see for our ImportPython Users from Taiwan.

台北捷运转乘路线Python库!
必须有来自台湾的 ImportPython 亲们哪...

(`是也乎:`
先汗一个, 大陆的 Pythonista 不是不想作哪,
而是根本没有这种公共服务的接口,无从包装哪,
而且, `合法爱国` 是铁律...)

- [Machine-Learning-Tasks](http://importpython.com/click/track/042f32bf164fd9d7d725e12078547caa2d291893?source=github.com)
    - 2 Stars, 0 Fork

Python 实现的简单 KNN 算清, COS 相似度, Logistic 回归...

- [python-libshorttext](http://importpython.com/click/track/ba297c3890dfa0dae235c54dd1dd13f92ac8f6a8?source=github.com)
    - 4 Stars, 0 Fork

LibShortText 是种高性能短消息分类器,
针对 标题/提问/句子...
脚本提供了一个简单的方式来安装此库.

- [spotify-backup](http://importpython.com/click/track/eb422620428be6c4d2fab84d74da4a6a709e41e7?source=github.com)
    - 1 Stars, 0 Fork

快速导出你所有 Spotify 播放列表.

- [GetUserAgent](http://importpython.com/click/track/538a9f11a9a25d3ae2915cd1133c25f9a72e14ad?source=github.com)
    - 1 Stars, 0 Fork

允许你从已知用户代理中随机抽取.

- [PyDictionary](http://importpython.com/click/track/f119f60ec5d740267a9ecfe6d25114d9b2752910?source=github.com)
    - 1 Stars, 0 Fork

PyDictionary 是兼容 Python 2/3 的字典库,
能翻译/同义/反义,
使用 Google 获得含义完成翻译,
通过 thesaurus.com 获得 同义/反义.


(`是也乎:`
废的,在天朝...)

## 曰了
~ Tweets~ Tweets

- `#BigData` 相关工作,2015 哪儿找? IT PM 职位有 `#BigData` 要求的 `#Python` http://t.co/HRIs96E9k2 http://t.co/wmmyjm7qOv

[@kdnuggets](https://twitter.com/kdnuggets/status/550377408814387200)

# 国货

# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150104 用时 51 分钟完成快译.
- 150103 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
