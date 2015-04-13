Title: Issue 29: 追忆
Slug: issue-29
Date: 2012-08-31
Tags: Weekly,Pycoder,Zh

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)

##  搜罗Py万物 的周刊

亲,

上周蟒社区有个坏消息. [Matplotlib](http://matplotlib.sourceforge.net/)的作者, [NumFOCUS](http://numfocus.org/)创始董事会成员, John Hunter去世了. NumFOCUS创立了[John Hunter 纪念基金](http://numfocus.org/johnhunter./)来帮助支付其子女的教育开支. 你可以通过这个[站点](http://numfocus.org/johnhunter./)来进行捐助.


如果你想要一个贴纸, 寄给我们回邮信封就好(送完为止):

    44 Byward Market Square, Suite 210
    Ottawa, Ontario Canada
    K1P 7A2


想跟上所有 蠎界 新闻? [@pycoders](http://twitter.com/pycoders).

--

Mahdi and Mike
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)


## 新闻

- [Python 3.3.0 release candidate 1 发布!](https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/rF6eG-NB_9w) (google.com)

离正式发布越来越近了. Python 3.3.0 rc1 已经发布. 猛击查看变更列表, 务必试一试并及时上报bug吧.

- [Django入门](http://www.kickstarter.com/projects/657368266/getting-started-with-django/) (kickstarter.com)

[Kenneth Love](https://twitter.com/kennethlove)在Kickstarter上为他的`Django入门`系列视频教程发起了一个众筹. 如果你感兴趣, 请飞奔去支持.

- [Human.io](http://human.io/) (human.io)

通过Human.io, 你可以用Python Api来快速的开发IOS或Android应用并部署. 超赞, 点击查看更多信息和演示.

- [PyData NYC 2012](http://nyc2012.pydata.org/)

PyData NYC现已开放注册. 活动将于10月26至28日在曼哈顿中城区的[国际灯塔](http://www.lighthouse.org/about/)举办. 你可以在这个网站找到更多信息.


## 讨论

- [恩, 聊一聊你用bottle.py做了什么?](http://www.reddit.com/r/Python/comments/ywodm/ask_rpython_so_what_have_you_built_with_bottlepy/)


## 项目

- [django-sqlpaginator](https://github.com/bulkan/django-sqlpaginator) (github.com)

这个django app让你直接生成sql来获取分页获取结果, 而不通过ORM. 支持`LIMIT`和`OFFSET`及`ORDER_BY` 语句. 如果你不想在你的django项目里用[ORM](http://en.wikipedia.org/wiki/Object-relational_mapping)的话, 这个就很好用了啊, 是不是?

- [numba](https://github.com/numba/numba) (github.com)

很赞的想法, Numba 是使用[LLVM](http://llvm.org/)的为Numpy准备的动态Python编译器. Numba的目标是"将使用NumPy运行时和SciPy模组的Python字节码编译成机器码"

- [Python Books](http://pythonbooks.revolunet.com/) (revolunet.com)

赞! 这个美妙的站点列出了许多Python的免费书籍. 很多好东西, 你可以在 Github 上看到它的[源码](https://github.com/revolunet/PythonBooks).


- [maze](https://github.com/daleobrien/maze) (github.com)

很酷的小项目. 又有谁在小时候没有痴迷过迷宫呢. [Dale](https://github.com/daleobrien) 肯定入了迷. 在家工作的时候, 这个小东西能让熊孩子们好好忙活一阵了.

- [marisa-trie](https://github.com/kmike/marisa-trie) (github.com)

可以用在Python (2.x 和 3.x)上的静态内存空间优化Trie结构. 相较于使用标准库字典来存放字符串, 使用marisa-trie后, 可以节约50-100倍的内存.


- [pixeltable](https://github.com/discountgenius/pixeltable) (github.com)

将任意图片转为html图片. 看看这个[纯html版本](http://pycoders.com/python.html)的python官方logo. 精巧的小玩意儿.
`译注: 链接失效, github项目没有申明依赖, 一时没有跑起来`

- [otrace](https://github.com/mitotic/otrace) (github.com)

`译注: 一个面向对象的debugger`


## 文章

- [用Selenium和Jenkins测试Django 1.4+](http://www.shiningpanda.com/blog/2012/08/23/selenium-tests-django-14-jenkins/) (shiningpanda.com)


- [高效的找出列表中的前K项](http://stevehanov.ca/blog/index.php?id=122) (stevehanov.ca)

如果你要处理海量数据集, 或者你想了解一下超酷的算法. 那这篇帖子探讨的如何使用heap而不是简单的使用列表, 相信会带给你带来一丝灵光.


- [RedHat OpenShift 入门](http://www.pythondiary.com/tutorials/getting-started-redhats-openshift.html) (pythondiary.com)

RedHat OpenShift 是一个刚加入PAAS战场的新生. Kevin Veroneau对如何让Django跑在RedHat的服务上做了一个很棒的介绍.


- [利用Python的import钩子让配置文件像代码一样好用](http://www.taricorp.net/2012/treating-configuration-as-code-with-pythons-import-hooks) (taricorp.net)


- [Numba VS Cython](http://jakevdp.github.com/blog/2012/08/24/numba-vs-cython/) (github.com)

很棒的文章! 它比较了纯python, [numba](https://github.com/numba/numba), 和 cpython 在分析计算上的差异. Numba绝对值得好好看一看.


- [托管在Github上的顶级Python项目分析](http://mjp.github.com/2012/08/29/github-python-analysis.html)(github.com)

聚焦于蟒社区开源现状的超酷文章. 我们爱死这篇眼光独到的干货了. 用到了[pyflakes](https://launchpad.net/pyflakes/) 和 [pep8](http://pypi.python.org/pypi/pep8/).


- [用 Puppet 部署 WSGI 应用](http://uggedal.com/journal/deploying-wsgi-applications-with-puppet/) (uggedal.com)


- [用 Ubuntu, Ansible, Nginx, Supervisor 和 uWSGI 来部署 WSGI 应用](http://mattupstate.github.com/python/devops/2012/08/07/flask-wsgi-application-deployment-with-ubuntu-ansible-nginx-supervisor-and-uwsgi.html) (github.com)

- [用 AppFog 部署 Pyramid 应用](http://antoineleclair.ca/2012/08/28/deploying-a-pyramid-app-on-appfog/) (antoineleclair.ca)


## 是也乎
- 来自: [SkyLothar](https://gitcafe.com/SkyLothar) 的 `PR`
