Title: 蠎加载 52
Slug: importpython-52
Date: 2015-11-13 11:17
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 52](http://importpython.com/newsletter/no/52/)
- 嗯哼, 蠎加载终于回归了,,,继续 happy 快译.

## 该读
~ 文章, Blog, 教程...


- [你的 Django 故事: 遇见 Shauna Gordon-McKeon](http://blog.djangogirls.org/post/132875295693)

Shauna Gordon-McKeon 
是位开发/作家/研究员,
对开放科学以及自由软件保有持久的激情.
当前经营咨询业务 Galaxy Rise Consulting.



- [PyCon Brasil 2015 主题演讲: David Beazley ~ asyncio 和 异步/等待](http://www.youtube.com/watch?v=lYe8W04ERnY)

David 同时也是好几本 Py 图书的作者


- [防护罩下的 Django: Django 安全性 - Florian Apolloner](http://reinout.vanrees.org/weblog/2015/11/06/django-security.html)
    + django

如果你又以为发现了 Django 的安全漏洞?
看: https://djangoproject.com/security 
嘦联系 security@djangoproject.com. 
及时报告这种错误,才能令 Django 越来越好.


- [OpenStack Style Guidelines](http://docs.openstack.org/developer/hacking/)

对于大如 OpenStack 的工程,类似指南是必须的.
类似的提醒,俺也向 OpenOffice 吼过.
IMHO: OpenStack 在作死ing...


- [教程: ISS(国际空间站) 的短信开销, 用 Python, Redis-Queue, 以及 Twilio 实现](https://www.twilio.com/blog/2015/11/international-space-station-notifications-with-python-redis-queue-and-twilio-copilot.html)

With the new Star Wars trailer coming out, I’ve been really excited about space lately. This could be pretty obvious based on what I wore during my API demo at BostonHacks last weekend. Twilio also had private screenings of The Martian for community members recently in several different cities. Pretty cool topic.

- [格式化字串  str.format() 系列函式 -- Python 3.4 笔记](http://slott-softwarearchitect.blogspot.com/2015/11/formatting-strings-and-strformat-family.html)
    + core python

嗯哼, 远离 `%` ,
珍重 `str.format()` !
痴迷者的笔记, 发现 `vars()` 函式的新秘密.


- [DjangoCon 北美](http://www.djangocon.us/)
    + conference

DjangoCon US 
是为期6天的社区大会,
每年在北美举行.
讨论 Django 的方方面面,无论职业程序猿,还是业余用户.


- [如何从 Django 发送 Jabber (XMPP) 消息](https://alexmorozov.github.io/how-to-send-jabber-xmpp-messages-from-django.html)
    + django

是否想有个 Dajngo 的简单应用,
能从内网接收 Jabber 消息转发给你?
欢迎体验: django-jabber.

- [Beal 猜想再探 (Peter Norvig notebook)](http://nbviewer.ipython.org/url/norvig.com/ipython/Beal.ipynb)

1637 年 Pierre de Fermat (费马)
在一本书的边页上注释提及了他最著名的 "定理".

而直到 1995 年, 才由Andrew Wiles证明.

但是, Beal 猜想 至今无人能证明,
即使悬赏 $1,000,000。

虽然作者数学能力一般,但是,能用代码来自动判定是否完成证明.
2000年发布首个版本代码以来,
收到了很多邮件,指出各种 证据/反例.
至今没有人能通过测试,
在此编录了常见错误,包含作者本人的,
并发布更新版本.

In 1637, Pierre de Fermat wrote in the margin of a book that he had a proof of his famous "Last Theorem".Andrew Wiles proved Fermat's theorem in 1995, but Beal's offer of $1,000,000 for a proof or disproof of his conjecture remains unclaimed. I don't have the mathematical skills of Wiles, so all I can do is write a program to search for counterexamples. I first wrote that program in 2000, and my name got associated with Beal's Conjecture, which means I get a lot of emails with purported proofs or counterexamples (many asking how they can collect their prize money). So far, all the emails have been wrong. This page catalogs some of the more common errors—including two mistakes of my own—and shows an updated program.

- [Slackipy – 自动邀请用户 (用 Flask)](https://github.com/avinassh/slackipy)
    + security release

Slackipy 是个 web 服务,
可帮助你自动邀请用户加入 Slack 团队.
基于 Flask 以及使用 Jinja2 模板.
所以,非常易于定制.


- [持久队列 (Python)](http://code.activestate.com/recipes/579124-persistent-queue/)
    + code snippet

持久队列的类. Code Snippet.

- [DSF 董事会更替: 征集候选人](https://www.djangoproject.com/weblog/2015/nov/12/re-election-dsf-board-call-candidates/)
    + django

Historically, the board members of the Django Software Foundation have been elected by the DSF membership; however, once elected, they have sat on the board until they chose to stand down. To improve the accountability of the board, last year all board members were elected for one calendar year. The time has now come for the re-election of the board. 


### 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


- [为艺(Wegenart)教育科技 急召](https://github.com/ZoomQuiet/zoomquiet/wiki/Hr4Wegenart)

来自帝都 音乐教育领域 O2O 创业团队,颜值最高的创业团队;
急招 **前端** 和 **Python后端工程师** 若干名, 年薪280K 起,还有期权!

有意者及时邮件 `zoomquiet+hr[AT]gmail.com`


## 项目
~ 包/模块/库/片段...


- [TensorFlow-Tutorials](https://github.com/nlintz/TensorFlow-Tutorials)
    - 554 Stars, 49 Fork

Google's TensorFlow 框架的简单使用教程.

(`是也乎:`

喂! 人家刚刚开源没几天哪!
一定是早就准备好了!

)

- [caffe-tensorflow](https://github.com/ethereon/caffe-tensorflow)
    - 21 Stars, 3 Fork

TensorFlow 中 Caffe 模式的概念验证

- [nvda](https://github.com/nvaccess/nvda)
    - 12 Stars, 7 Fork

NVDA, 
用以 M$ Windows 的开源屏幕阅读器

- [ascii_art](https://github.com/jontonsoup4/ascii_art)
    - 12 Stars, 0 Fork

将图片转换为 ASCII art

(`是也乎:`

![cat_scale5_draw](https://github.com/jontonsoup4/ascii_art/raw/master/examples/cat_scale5_draw.png)

标准 PIL 系模块的综合应用之一...

)

- [gesture-pacman](https://github.com/vipul-sharma20/gesture-pacman)
    - 9 Stars, 1 Fork

用手势来玩 吃豆人

- [balise](https://github.com/kz26/balise)
    - 9 Stars, 2 Fork

便携,轻巧,本地托管的 IPv4 / IPv6
地理位置 接口/服务

- [url2markdown-cli](https://github.com/alice1017/url2markdown-cli)
    - 7 Stars, 1 Fork

基于 URL 将指定网站整个儿转换为 md! 
Powered by kennethreitz/url2markdown

- [canvas](https://github.com/canvasnetworks/canvas)
    - 7 Stars, 1 Fork

Canv.as 
前后端一起来!

- [autospec](https://github.com/clearlinux/autospec)
    - 7 Stars, 1 Fork

RPM 自动打包工具.


## DAMA 无责任推荐



# 是也乎

- 151112 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 151112 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
