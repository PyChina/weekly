Title: 蠎周刊 : 2013最赞
Date: 2014-01-03 
Tags: Weekly,Pycoder,Zh 
Slug: issue-top2013

[TOC]

# Hi Pythonistas!

   
这周咱们作点儿不同的 ;-)
本文根据大家过去对周刊文章的点击量分析出的 2013年度顶级Python项目.
希望大家喜欢.
如果怕我们错过2014年的最佳项目,请及时邮件知会一下.
次周我们将恢复 #98 期周刊.


新年新折腾,
我们发布了:
[Pycoders Weekly Job board](http://pythonjobshq.com/)
现在开始到一月底,
使用优惠码 `pycoders2014` 发布职位信息可以获得 25% 的折扣!



才看到这一页的小伙伴们,
及时订阅2014 的蠎周刊吧.

一如往常, 任何疑问/意见/抱怨/建议只需点击回复此电子邮件.

想跟上所有 蠎界 新闻?
 [@pycoders](http://twitter.com/pycoders).

也可用
[Gittip](https://www.gittip.com/PycodersWeekly)
来支持俺们!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly - Top Python Projects of 2013](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=384b699bca)



## 测试和调试 Testing & Debugging
 

- [python_koans](https://github.com/gregmalcolm/python_koans) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Python Koans 算 "Ruby Koans" 的一部分,
作为交互式教程,
学习
[TDD](http://en.wikipedia.org/wiki/Test-driven_development) 
技巧,并令测试通过.

 

- [sure](https://github.com/gabrielfalcao/sure) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Sure 是最适合自动化测试的 Python 工具.
包含流利的断言,深度选择器等等特性.
推荐查阅 README 深入了解.

- [responses](https://github.com/dropbox/responses) (github.com)

用 responses 能令测试更加轻松,
这是一个可以伪装各种请求的库. 

- [boom](https://github.com/tarekziade/boom) (github.com)

Boom! 
[Apache Bench](http://httpd.apache.org/docs/2.2/programs/ab.html)
的替代品. 
作为一个命令行工具, Boom 能对你的应用进行快捷的
[smoke test](http://en.wikipedia.org/wiki/Smoke_testing) .

 

- [cricket](https://github.com/pybee/cricket) (github.com)

[BeeWare](http://pybee.org/) 套件的一部分,
cricket 是种图形化工具,
协助你进行案例测试
.
 

- [bugjar](https://github.com/pybee/bugjar) (github.com)

[BeeWare](http://pybee.org/) 套件的一部分,
bugjar 是种针对 Python 的图形化交互式调试器.

 

- [pudb](https://pypi.python.org/pypi/pudb) (python.org)

pudn 是针对Python 的全屏命令行调试器.


- [voltron](https://github.com/snarez/voltron) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

更好的 gdb 界面. 


## 框架及Web Frameworks & Web
 

- [django-stronghold](https://github.com/mgrouchy/django-stronghold) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

试过将 login_required 装饰器四处乱放?
在你的堡垒中令所有 Django 视图有默认 login_required 呗.
 

- [Falcon Framework](http://falconframework.org/) (falconframework.org)

Falcon自称为髙性能云接口框架.
号称能在相同硬件条件下提高服务端性能30倍!
听起来有点儿意思? 检出来使用吧!


- [django-xadmin](http://sshwsfc.github.io/django-xadmin/) (github.io)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

用bootstrap 对 django-admin进行了深度升级.
提供了可插件安装的仪表盘.
 

- [clay](https://github.com/uber/clay) (github.com)

基于 [Flask](http://flask.pocoo.org/) 
的包装,
能令我们轻松的创建 RESTful 后端服务.
完整文档在[这儿](http://uber.github.io/clay/).
 

- [flask-restful](https://github.com/twilio/flask-restful) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

基于 Flask 的简单框架,
用以创建 REST 接口.

- [sandman](https://github.com/jeffknupp/sandman) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Sandman 希望通过REST 接口暴露你现有的app.
相关
[blog post](http://www.jeffknupp.com/blog/2013/07/23/sandman-a-boilerplatefree-python-rest-api-for-existing-databases/) 也值得一读.
 

- [Django Unchained](http://nahimnasser.github.com/django-unchained/) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

名字很髙大上,
也的确是 Python Django 初学者的靠谱引导.


## 并发 Concurrency
 

- [pulsar](https://github.com/quantmind/pulsar) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

部件新web 服务器走起!
有趣的事件驱动的并发框架 ! 兼容从2.6+到pypy 的所有python 版本!

- [toro](https://github.com/ajdavis/toro) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

同步化的Tornado 协程支持
 

- [offset](https://github.com/benoitc/offset) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Offset 
[Go](http://golang.org/) 的
并发模式在 Python 中的实现.
请参考相关演讲
[幻灯](https://docs.google.com/file/d/0B2gNkR7hgkIRVFgwSWR4Y2JaZHc/edit?hl=en&forcehl=1). 
来理解!


## 任务调度 Job Schedulers
 

- [pyres](https://github.com/binarydud/pyres) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

从 
[resque](http://github.com/defunkt/resque)
获得灵感的 纯Python 任务调度模块,
是 芹菜(celery) 的不错替代物.

 
- [dagobah](https://github.com/tthieman/dagobah) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Dagobah 是Python 完成的简单 关系依赖为基础的任务调度模块.
还包含很COOL 的关联任务工作流图形工具.
 

- [schedule](https://github.com/dbader/schedule) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

使用生成器模式,来为定期任务生成配置的进程调度模块.

## 实用工具 Utilities & Tools
 

- [howdoi](https://github.com/gleitz/howdoi) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

发觉你总在 Google 一些简单的最简单的编程任务?
howdoi 能让你远离浏览器,就解决这类事儿!
 

- [delorean](https://github.com/myusuf3/delorean) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

时间旅行?简单!
Delorean 的目标就是令你的Python 项目在处理时间/日期时轻而易举!
检出工程并查阅完备的
[文档](http://delorean.readthedocs.org/en/latest/)
吧.

 

- [powerline-shell](https://github.com/milkbikis/powerline-shell) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

对于那些想让常用工具漂亮起来人,
一定要用 powerline-bash.
能打造漂亮的shell提示符,增加力线(powerline),兼容 Bash/Zsh.

(`译注:` 好吧,对于 zsh/fish 而言这个模块就 Naive 了 ;-)

- [fn.py](https://github.com/kachayev/fn.py) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

在Python 中谈及函式编程时失落的那节"电池"终于出现了!
如果对
[Python函式编程](http://ua.pycon.org/static/talks/kachayev/#/)
有兴趣的立即下手安装体验吧!

- [lice](https://github.com/jcarbaugh/lice) (github.com)

为你的开源工程方便的追加许可证, 而不用自个儿去 Google.
支持 BSD, MIT, and GPL 以及变种.


- [usblock](https://github.com/Svenito/usblock) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

基于 USB 钥匙来锁定或是解锁你的笔记本!
 

- [Matchbox](https://github.com/Max00355/MatchBox) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


MatchBox 能在你自个儿的服务器上提供 dropbox 风格的备份服务!
基于 Flask 并通过 http 协议进行文件传输,很得趣的样子!


- [cleanify](https://github.com/kirang89/cleanify) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


用cleanify能异步美化你项目的所有 html/css/js 文件.

- [locksmith](https://github.com/ehazlett/locksmith) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Locksmith 是AES加密的口令管理器.
看起来不错,完全开源. 源代码/截屏都有.

- [storm](https://github.com/emre/storm) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

在Storm的命令行界面,
管理你所有的SSH 连接,就"象头BOSS"!
非常有用!


- [sqlparse](https://github.com/andialbrecht/sqlparse/) (github.com)


这个很给力!
sqlparse 是个 SQL 有效性分析器.
支持解析/分裂/格式化SQL 语句.
 

- [autopep8](https://github.com/hhatto/autopep8) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

能自动化以
[pep8](http://www.python.org/dev/peps/pep-0008/)
规约来格式化你的代码.

https://www.gittip.com/hhatto/
 

- [colout](https://github.com/nojhan/colout) (github.com)

colout用以在命令行中色彩化输出.
这就从其 [github page](http://nojhan.github.io/colout/) 检出实例来体验吧.


- [bumpversion](https://github.com/peritus/bumpversion) (github.com)


版本号冲撞总是恼人的,
而每个人总是忘记给发行版本打tag.
bumpversion 用一条简单的命令简化了这方面的操作.
 

- [pyenv](https://github.com/yyuu/pyenv) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


需要更好的管理你Python的多版本 环境 ?
pyenv 让你能简洁的作到!

(甚至超出你的预期!有插件能将 VirtualEnv 也无缝结合进来!)

- [pip-tools](https://github.com/nvie/pip-tools)  (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

一整套能令你的Python 项目保持清爽的工具.
 

- [cdiff](https://github.com/ymattw/cdiff) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Cdiff是种非常 nice 的工具,
可以用彩色输出统一diff 格式信息,或用双栏形式来展示.
感觉对味的话,点击 README 获得更多细节!


## 科学科学及可视化 Data Science & Visualization
 

- [data_hacks](https://github.com/bitly/data_hacks) (github.com)


由[bitly](http://bitly.com/)发布的一堆数据分析用命令行工具.
这些工具接受命令行或是其它工具输入的数据,
轻易的生成柱图以及直方图等等.



- [给黒客的概率编程和贝叶斯方法](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


这书是极好的,
介绍如何用贝叶斯方法和概率编程进行数据分析.
而且,每章都提供了用以 iPython Notebooks 的示例.


- [simmetrica](https://github.com/o/simmetrica) (github.com)
 
想对自个儿的应用基于时间的数据序列,
进行展示/汇总/分享嘛?
赶紧上 simmetrica 吧,同时还提供了可定制的仪表盘.

- [vincent](https://github.com/wrobstory/vincent) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

所有喜爱数据以及Python 的人哪,
一定也爱 vincent.
Python构建的,专为运用D3.js 进行可视化 vega转换工具.

 

- [bamboo](https://github.com/SEL-Columbia/bamboo) (github.com)

一种简洁的实时数据分析应用.
bamboo 提供了一个进行 合并/汇总/数值计算 的数据实时接口. 


- [dataset](https://github.com/pudo/dataset) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


难以置信的工具,
dataset让对数据库的读写简单的象对 JSON 文件的操作.
没有其它杂七杀八的文件配置,
顷刻间就让你在BOSS 面前高大上起来.
 

- [folium](https://github.com/wrobstory/folium) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


喜欢地图?也爱Python?
Folium 让你在地图上自在操纵数据.
 

- [prettyplotlib](https://github.com/olgabot/prettyplotlib) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


用prettyplotlib来强化你的 matplotlib,
让你默认的matplotlib输出图片更加漂亮.
 

- [lifelines](https://github.com/CamDavidsonPilon/lifelines) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

有兴趣在Python 中研究[生存分析](http://zh.wikipedia.org/zh-cn/%E7%94%9F%E5%AD%98%E5%88%86%E6%9E%90)
的话,
不用观望了,用lifelines!
包含对 Kaplan-Meier, Nelson-Aalen 和生存回归分析.


## 编辑器及其改善 Editors & Editor Enhancements
 

- [sublime-snake](https://github.com/jf8073/sublime-snake) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

想在无尽的coding 中喘口气?
当然是这种经典游戏了...
 

- [spyderlib](https://code.google.com/p/spyderlib/) (google.com)

又一个用Python 写的开源 IDE. 

- [vimfox](https://github.com/dbsr/vimfox) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


对于 Vim 党最贴心的web 专发工具.
VimFox 能让 vim 实时的看到 css/js/html 的修改效果.
能神奇的让 vim 中的修订,立即在浏览器中看到...

(`译注:`图样图森破, 越来越多的渠道可以让浏览器和编辑器联动了...不过,的确真心是程序猿必备)
 

- [pcode](https://github.com/fortharris/Pcode) (github.com)

基于 Py3 的IDE, 通过简单的UI,提供了重构/工程管理等.



## 持续交付 Devops

- [metrology](https://github.com/cyberdelia/metrology) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


这个库很酷,
支持你对应用进行多种测量,并轻松的输出给类似
[graphite](http://graphite.wikidot.com/)
的外部系统.

 

- [python-lust](https://github.com/zedshaw/python-lust) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


支持在Unix 系统中用Python 实现一个守护进程.
 

- [scales](https://github.com/Cue/scales) (github.com)

Scales 对你的Python 应用进行持续状态和统计,
并发送数据到
[graphite](http://graphite.wikidot.com/). 
详情/实例 查阅官方 README.

- [glances](https://github.com/nicolargo/glances) (github.com)

跨平台基于
[curses](http://en.wikipedia.org/wiki/Curses_(programming_library)) 
命令行的系统监视工具.

(`译注:`htop 的纯Python 替代, 大妈已经用上;-)

- [ramona](https://github.com/ateska/ramona) (github.com)


企业级的应用监管.
Ramona 保证每个进程在值,
一但需要立即重启,
并有监控/日志输出, 查觉要糟时,会发送邮件提醒.
 

- [salmon](https://github.com/lincolnloop/salmon) (github.com)

Salmon 是基于 
[Salt Stack](http://saltstack.com/community.html)
的多服务监视系统.
即能作报警系统,也能当监控系统,
[README](https://github.com/lincolnloop/salmon/blob/master/README.rst) 
有截屏以及详细说明.

- [graph-explorer](https://github.com/vimeo/graph-explorer) (github.com)

Graph-explorer 是对
[Graphite](http://graphite.wikidot.com/)
面板的增强.
比原版的好很多,值得体验.


- [sovereign](https://github.com/al3x/sovereign) (github.com)

Sovereign 是一系列
[ansible](https://github.com/ansible/ansible)
的攻略手册,
基于之,能为自个儿建造个私人云.

(`译注:`Ansible, Fabric, SlatStack, 这是Python 实现的类似 Puppet 的持续部署管理系统
但是,更加简洁,直觉,值得关注)
 

- [shipyard](https://github.com/ehazlett/shipyard) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

(shipyard,船坞)
名很倩的web 应用,可以显示给定机器上的docker实例.
也支持创建,删除等操作.

- [docker-py](https://github.com/dotcloud/docker-py) (github.com)

An API client for the amazing 

疯狂的[docker](https://github.com/dotcloud/docker) 
工程接口的Python
包装.

(`译注:` 不没听说过 Docker? 忒 out了,参考:
[无责任报道~ECUG2013Con](http://blog.zhgdg.org/2013-12/et-ecugcon-sz/);
这是准备将应用部署连操作系统环境也一并抄底儿统一快照/回滚/分发/版本 管理的系统)
 

- [dockerui](https://github.com/crosbymichael/dockerui) (github.com)

基于
[docker](https://github.com/dotcloud/docker)
接口通过web 界面进行交互操作的工具.

 

- [django-docker](https://github.com/kencochrane/django-docker) (github.com)


如果想知道怎么将Djnago 应用同 Docker 结合?
学习这个 demo 吧.
 

- [diamond](https://github.com/BrightcoveOS/Diamond) (github.com)

Python 实现的守护进程,
自动从你的服务或是其它指定数据源中提取数值,
并向
[graphite](http://graphite.wikidot.com/)
[以及其它支持的](https://github.com/BrightcoveOS/Diamond/wiki/Handlers) 
状态面板/收集 系统输出.



## Git

- [git-workflow](https://github.com/jvns/git-workflow) (github.com)

可视化你的 git 工作流程的工具,
示例在
[这儿](http://visualize-your-git.herokuapp.com/display/2).
 很COOL的说.

- [gitto](https://github.com/bhuztez/gitto) (github.com)

简洁的库,
协助你建立自个儿的 git 主机.

- [git-imerge](https://github.com/mhagger/git-imerge) (github.com)


git-imerge 能让 git 进行增量合并.
本质上是允许你在进行 `imerge`
有冲突时,
有机会先合并掉,再继续.
 
##  Mail & Chat
 

- [mailbox](https://github.com/martinrusev/mailbox) (github.com)

Mailbox 是对Python 的IMAP 一个人性化的再造.
基于简单即是美的态度,
作者对 IMAP 接口给出了一个简单又好理解的形式.


- [deadchat](https://github.com/jeztek/deadchat) (github.com)

deadchat 
旨在不安全的网络环境中
提供安全的 `单一房间` 群聊服务以及客户端.

 

- [Mailpile](https://github.com/pagekite/Mailpile) (github.com)

Mailpile 
是针对邮件的索引及搜索引擎
.

 
## 音频和视频  Audio & Video
 
- [pms](https://github.com/np1/pms) (github.com)

穷人的 [Spotify](https://www.spotify.com/)
搜索和收集音乐流!


- [dejavu](https://github.com/worldveil/dejavu) (github.com)


在琢磨 Shazam 的原理?
音频指纹识别算法的Python实现在此!

(`译注:`[Shazam](http://www.shazam.com/) 是个神奇的音乐识别应用,
嘦对她啍个几秒调子,就能精确告诉你是什么歌曲,作者,歌词...)

 
- [HTPC-Manager](https://github.com/styxit/HTPC-Manager) (github.com)

为[HTPC](http://en.wikipedia.org/wiki/Home_theater_PC) 
粉丝准备的工具,
提供了完备的界面来管理所有家庭媒体服务器上的好物.

 

- [cherrymusic](http://fomori.org/cherrymusic/) (fomori.org)


Python 实现的一个音乐流媒体服务器.
流化输出你的音乐到所有设备上.

(`译注:`即私人 iTunes 服务)
 

- [moviepy](http://zulko.github.io/moviepy/) (github.io)


脚本化的电影剪辑包,
神马 切/串/插入标题 等等基本操作,
几行就搞掂!

## 其它好物 Other Awesomeness.
 

- [emit](https://github.com/BrianHicks/emit) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


用 redis 为你的函式追加可订阅能力,
很有趣.
 

- [zipline](https://github.com/quantopian/zipline) (github.com)

Zipline 是种
很Pythonic 
的交易算法库.

 

- [raspberry.io](http://raspberry.io/) (raspberry.io)

Raspberry.io 
是树莓派的社区实现.
刚刚发布,汇集了各种创意想法,
有兴趣的话立即检出折腾吧.

 

- [NewsBlur](https://github.com/samuelclay/NewsBlur) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Google Reader 已经关张儿了.
Newsblur 已经发布了有段日子了,
开源的 RSS 阅读器,
这绝对是应该首先体验的.

 

- [macropy](https://github.com/lihaoyi/macropy) (github.com)

Macropy 
是在 Python 中实现
[macros](http://en.wikipedia.org/wiki/Macro_(computer_science)#Syntactic_macros)的库.
检出文档,参考所有功能,
看怎么用上了.

 

- [mini](https://github.com/halst/mini) (github.com)



对编译器以及语言设计有兴趣的,
一定要看看这个仓库,以及配套的录像!
 

- [parsimonious](https://github.com/erikrose/parsimonious) (github.com)

Parsimonious 的目标
是最快的 `arbitrary-lookahead` 解析器.
用Python 实现,基本可用.
足够COOL,
检出样例折腾吧.



- [isso](https://github.com/posativ/isso) (github.com)


Disqus 的开源替代,
从demo 看很不错,而且提供了更好的隐私设置.

- [deaddrop](https://github.com/deaddrop/deaddrop) (github.com)

Deaddrop 
能为新闻机构或是其它人
提供在线投递箱.
详细信息参考其 [github page](http://deaddrop.github.io/)
.
 

- [E.V.E](https://github.com/thomasweng15/E.V.E.) (github.com)

If you have been envious of seeing Jarvis the computer in Iron Man or would like to interact with your computer like the one on Star Trek this project is right up your alley. Click through to check out all the awesome.

如果你一直羡慕
钢铁侠里 Jarvis 的电脑,
或是 星际迷航 里星舰主机,
让你的电脑也能理解你的语音指令?
检出这儿的妙物吧!

 

- [nude.py](https://github.com/hhatto/nude.py) (github.com)

裸体检测 的Python 实现,
是 nude.js 的仿制.

 

- [kaptan](https://github.com/emre/kaptan) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Kaptan 
是你应用的配置管理器!

(`译注:`通吃常见配置文本格式 

    dict
    json
    yaml
    .ini
    .py

)

 

- [luigi](https://github.com/spotify/luigi) (github.com)

Luigi 
帮你构建复杂的管道
来完成批处理.


- [gramme](https://github.com/waawal/gramme) (github.com)

Gramme 
以简单而优雅的方式,
通过 UDP 接口对易失数据完成消息包装序列化.


- [q](https://github.com/zestyping/q) (github.com)


为你的Python 程序提供快速而随性的日志.
有一系列帮手来追踪你的函式参数,
并能在控制台快速交互式加载.

(`译注:` 很实用的工具, 但是,选择了一摧悲的工程名, 几乎不可能搜索出来的过短名字...)
 

- [fuqit](https://github.com/zedshaw/fuqit) (github.com)

来自伟大的
[Zed Shaw](http://twitter.com/zedshaw)
最新作品, 
fuqit 试图令你忘记 MVC 的经验,
用全新的方式专注简洁一切.



- [simplicity](https://github.com/pydanny/simplicity) (github.com)

基于靠谱的
[pydanny](http://twitter.com/pydanny)
将你的 ReStructuredText 转换为 JSON 格式.

 

- [lassie](https://github.com/michaelhelmick/lassie) (github.com)

Lassie 允许你轻松的从网站检索出内容来.
 

- [paperwork](https://github.com/jflesch/paperwork) (github.com)

Paperwork 
是个 OCR 文档并完成可搜索转化的工具,
用GTK/Glade实现了友好的界面.

 

- [cheat](https://github.com/chrisallenlane/cheat) (github.com)


cheat 允许你创建并查阅
命令行上的交互式备忘.
设计目的是帮助
`*nix` 的系统管理员们在习惯的环境中,
快速调阅不易记忆的常用命令.
 

- [cookiecutter](https://github.com/audreyr/cookiecutter)  (github.com)


良心模块!
提供一堆有用但是不常写,
所以记不下来的代码模板,
也支持自制代码模板.


- [pydown](https://github.com/isnowfy/pydown) (github.com)


支持用Python 构建亮丽的HTL5 效果幻灯,

[这儿](http://isnowfy.github.io/pydown/)
有demo.

 

- [Ice](https://github.com/scottrice/Ice) (github.com)

模拟器粉丝们现在能用 Ice
向
[Steam](http://store.steampowered.com/) 
里塞 ROMs 来玩了.

 

- [pants](https://github.com/ecdavis/pants) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


用以编写异步网络应用的轻量级框架.
Pants 是单线程,回调服务,
也包含支持Websockets 的 HTTP 服务,
WSGI 支持, 和一个简单的web 框架.



- [pipeless](https://github.com/asperous/pipeless) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)

Pipeless 
是一个构建简单
[数据管道](http://en.wikipedia.org/wiki/Pipeline_(software))
的框架.
 

- [marshmallow](https://github.com/sloria/marshmallow) (github.com)
![<3](https://lh6.googleusercontent.com/3C_maRgJSN4L8CJv9k6CHcNpTGQANwYY_9QpAx5uJBoefG9jlrw3ERDPC1yKKkPiOUwuAu04EXfH7G-q9mQPufvxkmq7Yx2dDAasfFgIl2H2VH7LpXQjSPxt-g)


marshmallow 是个 ORM 无关的库,
能将复杂的数据类型转换为Python 原生类型对象,
以便容易的转换为JSON 提供接口使用.


- [twosheds](https://github.com/Ceasar/twosheds/) (github.com)

Python 实现的库,
用来构造命令或是shell 解释器.
twosheds 让你用 Python 来定制自个儿的 shell 环境.

# 是也乎

- 140110 [Zoom.Quiet](http://zoomquiet.io/) 用时 86 分钟完成所有.
- 140109 发现有同好: [pythoner.cn Pycoder's Weekly - Issue #2013](http://www.pythoner.cn/pycoders/weekly/2013/) 只是图样图森破的,只是翻译了一部分...
- 140107 [Zoom.Quiet](http://zoomquiet.io/) 用时 45 分钟完成到77%.
- 140106 [Zoom.Quiet](http://zoomquiet.io/) 用时 100 分钟完成到40%.
- 140105 [Zoom.Quiet](http://zoomquiet.io/) 用时 47 分钟 完成快译20%.
- 140104 [Zoom.Quiet](http://zoomquiet.io/) 用时 27 分钟 完成格式转抄.
 
