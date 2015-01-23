Title: 蠎加载 18
Slug: importpython-18
Date: 2015-01-23 17:17
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 18](http://importpython.com/newsletter/no/18/)


## 该读
~ 文章, Blog, 教程...



- [在 Django 框架中实现活动流](https://impythonist.wordpress.com/2015/01/18/implementing-activity-streams-in-django-web-framework/)

收集 Twitter 中 website.Like 的所有内容,
展示为类似 Gitlab 仪表盘或 LinkedIn 中的活动流.
一个用户专用一个流,
此文详细描述了怎么折腾的.

- [Python 性能剖析 - Google HOA 公告](https://plus.google.com/events/cl9lgl8bkpqabdgbnpdp0eko0h4)

1/22 下午,在 Google Hangout 空中视频中,
工程师分析了过往几年间 Python 的各种性能问题,
并在视频结束部分进行了QA.


- [蠎人中阶技法: 函式](http://intermediatepythonista.com/the-function)

Python 的函式表现为命名/匿名/表达式.
函式是 Python 中的第一公民,
这意味着其实没有什么可以限制函式的使用.
本质上, 函式完全可以表现的和任何值对象一样,
比如 字串/数字.

- [Django 1.8 alpha 1 发布](https://www.djangoproject.com/weblog/2015/jan/16/django-18-alpha-1-released/)

不同以往, 都是在 beta 后才发布,
alpha 里程碑的版本发布,标志着又一个完整的特性冻结了.
此版本更加接近最终发布版.

- [Python 循环中的索引值域](http://eli.thegreenplace.net/2015/the-scope-of-index-variables-in-pythons-for-loops/)

俺直接囧掉的, 试想以下函式作了什么?

def foo(lst): 
    a = 0 
    for i in lst: 
        a += i 
    b = 1 
    for t in lst: 
        b *= i 
    return a, b

...

(`是也乎:`
血淋淋的挖入运行时的汇编代码哪..
)

- [Coverage.py 更好的 Django 模板](http://nedbatchelder.com//blog/201501/coveragepy_for_django_templates.html)

经过长期的折腾,
终于 coverage.py 支持了 Django 的模板.
通过插件,
用 coverage.py 实现了可用的 Django 模板.


- [放弃 Python 作为教学语言](http://www.reddit.com/r/Python/comments/2t541k/retiring_python_as_a_teaching_language/)

论及为什么 Javascript 是种更好的教学语言?
并分析作为教学语言时, Python 有什么缺点.

(`是也乎:`
又一位被 pip 桑了心的老师,
而且学生们的第一要求是写个游戏...
)


- [用 `pypath_magic` 来作为你的 Python 环境路径呵 (v0.3)](http://tonysyu.github.io/pypath-magic-v03.html)

pypath-magic 为模块和包配置路径给出了一个简洁的管理界面.

(`是也乎:`
必然的, CLI 的 ;-)

- [Python 可视化工具纵览](http://pbpython.com/visualization-tools-1.html)

在 Python 世界,对于可视化, 当然也有很多选择.
这对选择困难症患者而言太痛苦了!
所以,作者进行了充分的对比.
用各种框架完成个简单的柱图来分析.

(`是也乎:`
其实使用面向浏览器的 JS 可视化框架也一样的
;-)

- [进入 Python 第一步](https://realpython.com/learn/python-first-steps/)

Derrick 为各种 Python 社区回答了这一月经帖.
认真解答了可能所有行者被问到次数最多的问题:
"如何开始使用 Python?"
他和 Michael Herman 基于真实的 Python 开发团队的经历,
给出了答案.

(`是也乎:`
简单的说:

    珍惜生命
    远离M$

另外,可以参考: [极简 Python 上手导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart)
)


- [来写 LLVM 专用 Python 吧!](http://dev.stephendiehl.com/numpile/)

目标是完成一个 Numba 样的 Python 编译器.
不完备,但是,演示出了如何针对 LLVM 进行思考,
可以解析相当于 Python 语言子集的自制 DSL ,
并和现行和洕计算库(比如 NumPy/SciPy)兼容!


- [ImportPython Weekly 宇宙国版本](http://weeklypythonkr.tumblr.com/)

哗!
Ayun Park 发布了韩语版本的
蠎加载周刊!

(`是也乎:`
大妈独自坚持了8周,当前只有 2~10 期没有翻译,
倡议大家共同快速完成,
通过: [合并请求 · CPyUG/weekly - GitCafe](https://gitcafe.com/CPyUG/weekly/pull?state=all)
也好向官方申请中文版本的链接过来
!-)

- [在 AWS 上部署 Flask 应用](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80)

端到端的实案,
用了 Amazon 的 Elastic Beanstalk 和 RDS. 

## 项目
~ 包/模块/库/片段...

- [httpscreenshot](https://github.com/breenmachine/httpscreenshot)
    - 18 Stars, 7 Fork

HTTPScreenshot 能高速抓取大量网络的截图.
工具目标是快准狠, 并能相互 oppose.

- [prettytable-mirror](https://github.com/mapio/prettytable-mirror)
    - 10 Stars, 1 Fork

prettytable 仓库的镜像 (on Google Code)

- [freesms](https://github.com/bfontaine/freesms)
    - 6 Stars, 0 Fork

免费的短信推送模块,
基于 `Free Mobile SMS API`
当然,你得先注册有关服务.

- [django-activity-stream-tutorial](https://github.com/narenaryan/django-activity-stream-tutorial)
    - 5 Stars, 0 Fork

简单的教程,
却能极大的提升我们使用 Django 仪表盘的功力

- [jonahnator](https://github.com/galarant/jonahnator)
    - 4 Stars, 0 Fork

Jonah Peretti 式语录发生器.

(`是也乎:`
用 bower 玩了很多前端技巧来发布.
)

- [flask-alchemy](https://github.com/lepture/flask-alchemy)
    - 3 Stars, 1 Fork

正如其名,
基于 SQLAlchemy 的 declarative_base,
专门为 Flask 开发,
对 主-从 东西方的数据库集群给予强力支持!

## 曰了
~ Tweets


# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150123 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150123 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
