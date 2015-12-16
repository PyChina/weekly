Title: 蠎加载 53
Slug: importpython-53
Date: 2015-12-04 14:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 53](http://importpython.com/newsletter/no/53/)
- 嗯哼, 蠎加载终于又回归了,,,继续 happy 快译.
- (为什么说又!?)

## 该读
~ 文章, Blog, 教程...


- [Django 引擎盖下: 会议视频](https://opbeat.com/events/duth/)
    + video

Django: 引擎盖下 第二版.
侧重 Django 的本来策略.
如果你是位 Django 工程师, 应该认真看看.
感觉赞助商 OpBeat ~ 专注 Django 应用的监控平台.

- [优化缓慢的 Django REST 框架性能](https://ses4j.github.io/2015/11/23/optimizing-slow-django-rest-framework-performance/)
    + REST

看起来很简单的, REST 框架及其可嵌套的序列化,
就足以杀光接口性能.
记住,如果 Web 服务器将时间浪费在 REST 接口调用上,
那么整体性能必然下降.


- [Python 3.5 类型提示在 PyCharm 5](http://blog.jetbrains.com/pycharm/2015/11/python-3-5-type-hinting-in-pycharm-5/)
    + pycharm

Python 3.5 引入了类型提示,
以便支持 IDE , PyCharm 已经实现了对应功能.

- [基于Docker, Compose 和 Django 的开发入门 - howchoo](http://howchoo.com/g/y2y1mtkznda/getting-started-with-docker-compose-and-django)
    + django

展示了如何基于 Docker 构建 Django 开发环境


- [Python 的 '惊喜' 导入](http://blog.doismellburning.co.uk/pythons-surprise-imports/)
    + django


Django 有各种开发推荐,
比如, 用 `django.utils.timezone.now` 来获得当前日期,
但是, 实际上...

recommends that you use, for example, django.utils.timezone.now to ensure you always get “the right now” (i.e. timezone-aware). So you might, as with the code example above, extrapolate that timezone.datetime(2015, 1, 1) will give you a timezone-aware “1st of January 2015” datetime object.


(`是也乎:`

`django.utils.timezone.datetime` 的故事...
)

- [Django 1.9 发布](https://www.djangoproject.com/weblog/2015/dec/01/django-19-released/)

经过10个半月的开发,
Django 团队终于宣布 1.9 发布了.
和以往版本一样, 发布说明中包含了各种深入细节.
主要亮点在:

    支持执行后操作
    事务提交
    密码验证
    允许mix-in 基础类
    全新 contrib.admin 样式
    支持并行测试
    ...

- [如何求两个有序列表的交 (在 Python)](http://ptspts.blogspot.com/2015/11/how-to-compute-intersection-of-two.html)

文章解释了有序列表求交原理,
并展示了 Python 实现的快速版本.
时间复杂度仅为 : 

    O(min(n + m, n · log(m))
    其中 n 为最小列表长度
    m为列表长度最大值


- [你的 Django 故事: 遇见 Kinga Kiczkowska](http://www.reddit.com/r/pyladies/comments/3uu57j/your_django_story_meet_kinga_ki?czkowska/)
    + interview

Kinga 是 Django Girls 的教练/组织者,
同时也是 爱丁堡龙比亚大学 的计算机安全及取证系学生以.

- [Django 的安全性问题回答](http://kevinlondon.com/2015/10/16/answers-to-django-security-questions.html)
    + django

你知道多少 Django 安全性问题?
你有信心攻破 Django 应用嘛?


- [当周 PyDev: Nick Coghlan](http://feedproxy.google.com/~r/TheMouseVsThePython/~3/nm8O00hOGUc/)
    + interview

Nick Coghlan (@ncoghlan_dev) 
入选择当周蠎星.
他是 Python 语言核心开发者,
同时也发布有非常激烈的 Python 技术blog.
来听听他又说了什么.


### 工作

....

## 项目
~ 包/模块/库/片段...

- [microservices](https://github.com/umermansoor/microservices)
    - 237 Stars, 15 Fork

基于 Flask 构建微服务的实例.

- [musicbot](https://github.com/szastupov/musicbot)
    - 157 Stars, 9 Fork

Telegram 音乐目录机器人

- [char-rnn-tensorflow](https://github.com/sherjilozair/char-rnn-tensorflow)
    - 152 Stars, 17 Fork

多层回归神经网络（LSTM，RNN）
用 Python 实现的 Tensorflow 模型



- [vocabulary](https://github.com/prodicus/vocabulary)
    - 140 Stars, 8 Fork

Python 模块,
对给定的字 获得 语义/同义/反义/词性/用法示例/发音/断字...


- [article-date-extractor](https://github.com/Webhose/article-date-extractor)
    - 30 Stars, 2 Fork

自动提取和标准化在线文章/blog 的发表日期.


- [django-package-monitor](https://github.com/yunojuno/django-package-monitor)
    - 10 Stars, 0 Fork

Django 应用的依赖模块跟踪监控!

(`是也乎:`

细思恐极,Dajngo 应用的依赖已经复杂到需要专用服务来监察了了...

)


- [emailhunter-clone](https://github.com/alirezasamar/emailhunter-clone)
    - 8 Stars, 0 Fork

emailhunter.co 一个很赞服务的 Clone 

## DAMA 无责任推荐

- [GitHub 漫游指南](https://github.com/phodal/github-roam)

# 是也乎

- 151204 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 151204 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
