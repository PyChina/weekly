Title: 蠎加载 31
Slug: importpython-31
Date: 2015-05-07 22:22
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 31](http://importpython.com/newsletter/no/31/)

## 该读
~ 文章, Blog, 教程...


- [使用 Docker 和 Docker Compose 来替代 virtualenv 搭建本地 Django 开发环境](https://www.calazan.com/using-docker-and-docker-compose-for-local-django-development-replacing-virtualenv/#.VULF_bAmduE.reddit)
    + django, flask

Django 和 Flask 是众所周知的两个 Python Web框架. 
有很多项目使 Flask 对简单的 JSON 响应提高2倍,比如techempower. 
在了解过这些项目后, 真心觉得Django可以做的更好!

所以, 不会讲 Docker 官网已有的各种原理知识. 
只是展示, 我是如何建立为 YouTube 音频下载的 Django 应用建立专发环境的.


- [提升Django性能四件事儿](http://revsys.com/blog/2015/may/06/django-performance-simple-things/)
    + django, performance

给出让你网站性能轻松提高的四件事儿. 

- [使用 Python 的 Nose 编写 Selenium 测试用例](http://scrolltest.com/selenium-testcase-with-nose-in-python/)
    + testing

Nose让Python测试变得更美好. 
基本上它扩展了Unittest和提供的特性,如只运行失败的测试,跳过测试用例,运行测试基于优先级,正则表达式模式等,
现在将 Selenium 结合进来, 令测试人员的生活更美好.


- [PyCon India 2015将在十月二三四号举办!](https://in.pycon.org/cfp/pycon-india-2015/proposals/)
    + pycon

PyCon India,Python开发者社区为印度Pythonista举办的开发者盛会,会有大批Python大神前来.

- [PyCon India 2015公开注册](https://in.explara.com/e/pycon-india-2015)
    + pycon

票已开始预售,不要错过

- [Jython 2.7.0最终版发布!](http://fwierzbicki.blogspot.com/2015/05/jython-270-final-released.html)
    + jython

代表Jython开发团队,我很高兴地宣布,
Jython 2.7.0可用的最终版本在经历了一个漫长的道路后终于发布了!

(`是也乎:`

JAVA 不死,他只是慢慢....
)

- [更新的PSF选举 ~ 新的选举开始](http://pycon.blogspot.com/2015/05/update-on-psf-elections-new-election.html)
    + PSF

由于目前的 Python软件基金会 董事会选存在一些程序上的问题,
基金会已经采取了一些措施,以确保选举是自由开放的提名,没有利益冲突的. 


- [Wing IDE 5.1.4发布](http://wingware.blogspot.com/2015/05/wing-ide-514-released.html)
    + new release

Wingware 发布了 5.1.4 版本的 Wing IDE,
作为面向 Python 跨平台集成开发环境. 
Wing IDE集成了专业代码编辑器vi,emacs,visual studio 的快捷键,
以及 自动补全,信息提示,上下文联想,跳转源码,重构,强大的调试器,版本控制,单元测试,搜索,项目管理,以及许多其他功能. 


- [Accepting PEP 492 (async/await)](https://mail.python.org/pipermail/python-dev/2015-May/139844.html)
    + PEP

感谢尤里一直以来的努力认真,
正是他坚持作正确的事,我们才可以投入到澄清术语和解释协同程序中.

- [Awesome Django](http://awesome-django.com/)
    + django

优秀的Django项目资源列表,灵感来源于awesome-python

- [PyPy.js: 快速的,兼容Python的Web实现](http://www.reddit.com/r/Python/comments/351e8b/pypyjs_a_fast_compliant_python_implementation_for/)
    + new release

构建快速并兼容 Python 的Web环境. 
使用 PyPy 解释器,通过 emscripten 编译,在运行时由
JIT
发出
asm.js 代码. 

- [Google选择Python的五个理由](http://www.reddit.com/r/Python/comments/355tph/5_reasons_why_python_is_powerful_enough_for_google/)
    + core python

准备创业的你. 应该选择什么语言?

-  [Python & RSA 算法](http://blog.brainattica.com/rsa-with-cryptography-python-library/)
    +  crypto

Python由很多的库提供加密服务,比如 M2Crypto, PyCrypto, pyOpenSSL, python-nss和 Botan的Python bindings. 如果你试图选择其中之一有五个标准可以评估:是否c实现,可维护性,对Python的支持,可读性和完整性. 是所有失败的"审查"的范畴. 例如PyCrypto(Python最常用加密库)在PyPy上失效. 


# New Books

- [Hello Web App](http://hellowebapp.com/)
    + Tracy Osborn
    
Hello Web 应用程序是由一个设计师为非程序员编写的,
从启动web 应用,到真正获得用户.
每一步都有完备的指导.

本书并没有使用特定的教程,
而是通过的示例来指引你通过 Python 和 Django
实现你感兴趣的东西. 

参考作者的采访: http://importpython.com/blog/


(`是也乎:`

![Tracy Osborn](http://static1.squarespace.com/static/547d23c6e4b0faf2ab43e004/t/54fe17f3e4b017e64ba523f3/1425938420339/?format=300w)

美女写的技术图书...

当年可爱的 Python 范儿.
)

## 项目
~ 包/模块/库/片段...


- [Easy-Card](https://github.com/x43x61x69/Easy-Card)
    - 68 Stars, 10 Fork

在台湾大规模使用的智能卡系统, 主要用于交通. 然而和日本的PASMO卡,韩国的T-Money不同,它是通过NFC来锁定读取数据的. 换而言之,当你没空去地铁站的时候你将没法通过app等查询你卡内的余额,这是一个多么蛋疼的问题. 


(`是也乎:`

`悠遊卡餘額明細查詢` ~ 嗯啍?! 台湾弟兄的作品...
)

- [Robinhood](https://github.com/rohanpai/Robinhood)
    - 37 Stars, 7 Fork

通过Robinhood接口进行交易的Python框架

- [HardenFlash](https://github.com/HaifeiLi/HardenFlash)
    - 19 Stars, 6 Fork

修复Flash exploits和zero-days的补丁

- [wordcloudbot](https://github.com/decause/wordcloudbot)
    - 4 Stars, 0 Fork

一种 systemd 服务,
监听 fedmsg 的 IRC 会议记录,
生成单词云, 并自动发推到 http://twitter.com/fedobot

- [marvelous](https://github.com/dcloud/marvelous)
    - 3 Stars, 0 Fork

绑定Marvel Comics的API

- [pyrthon](https://github.com/tobgu/pyrthon)
    - 2 Stars, 0 Fork

代替Pyrsistent的工具库.


- [pyqtconsole](https://github.com/marcus-oscarsson/pyqtconsole)
    - 2 Stars, 0 Fork

QT 实现的轻量级 Python 控制台. 
通过一些例子说明如何可以轻松的将其嵌入在其他的Qt应用程序中. 
解释器可以运行在一个单独的线程,在 UI 主线程或在 Gevent 任务. 
未来也可能增加对 asyncio 的支持. 

(`是也乎:`
Qt ...
)

- [python](https://github.com/mfrance0916/python)
    - 2 Stars, 0 Fork

个人写的生物信息学脚本

(`是也乎:`
项目名称选择这种和语言一样的,只能说
...作的一手好死

)

- [GRE.py](https://github.com/saru95/GRE.py)
    - 1 Stars, 0 Fork

Mac上的GRE单词学习小软件

- [pygments-markdown-lexer](https://github.com/jhermann/pygments-markdown-lexer)
    - 1 Stars, 0 Fork

Pygments 对 Markdown 代码进行高亮的词法解释器.

- [normalizr](https://github.com/davidmogar/normalizr)
     1 Stars, 2 Fork

Python对文本进行规范化的库.现有删除多余的空格,删除连字符,删除标点符号,(来自13个不同的语言)删除停用词,删除符号功能. 下一步准备实现消除口音的功能. 

- [phrack_reader](https://github.com/Qingluan/phrack_reader)
    - 1 Stars, 0 Fork

方便大神们阅读phrack ezine的东东,欢迎提bug


## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)

### 工作

-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
四月急招 N 名有服务端开发经验的 **gopher**!


-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

-   [SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)  

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!

# 是也乎

- 150512 spawnris/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150507 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

