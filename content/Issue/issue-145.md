Title: 蠎周刊 Issue 145: Spa
Slug: issue-145
Date: 2014-12-13 23:23
Tags: Weekly,Pycoder,Zh 

![04_20AM9789bf](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #145): Spa](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=07a5f186be&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,


又一轮 TEE 活动已经结束,感谢购买的,下次请早 ;-)

大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)





## 新闻

- [github3.py 1.0.0a1 发布](http://www.coglib.com/~icordasc/blog/2014/12/github3py-100a1-released.html)


最新 alpha 版本发布了,
此文认真探讨了新版和开发方向.

coglib.com

Shared by @sigmavirus24
 

- [Python 2.7.9 发布](https://www.python.org/downloads/release/python-279/)


使用了 3.4 的 SLL 模块,以及补丁,
详进增补看变更日志去也.

python.org

Shared by @mgrouchy
 

- [Bokeh 0.7 发布](http://continuum.io/blog/bokeh-0.7)

制图库 Bokeh 最新版本释放!
类似 IPython 部件以及动画都能在没有 Bokeh 服务器情况下输出了.
触摸UI 也在支持中.

continuum.io

Shared by @mgrouchy
 

- [Django: Under the Hood Talks 发布!](http://www.djangounderthehood.com/talks/)

收集了各种 Django 的私用勾联, 赶紧研究吧.

djangounderthehood.com

Shared by @myusuf3
 

- [IronPython 2.7.5 发布](http://ironpython.codeplex.com/releases/view/169382)

如果是位令人敬仰的 .NET 程序猿,
有褔了.

codeplex.com

Shared by @mgrouchy
 

## 讨论
- [数据科学最佳学习路线?!](http://www.reddit.com/r/Python/comments/2p1uj3/best_way_to_learn_data_science/)

reddit.com

Shared by @myusuf3
 
(`是也乎:`
目击了超级感动的回答哪,怪不得 reddit 这么火...

数据科学,的确是科学和工程结合成本最低的一种了,无外乎:

- 数据收集
- 数据清理
- 分析统计
- 可视化
- 业务结合

不过,嘦是过来人都建议:

- 先学 R 来理解数据科学领域的常见问题思路
- 用 ggplot2 可视化
- 用 dplyr 操作数据
- 最后进入 机械学习领域,再结合 Python 事半功倍


)

## 项目


- [gitfs](https://github.com/PressLabs/gitfs)
Very cool, gitfs is a FUSE filesystem that integrates with Git fully. Some really great features in here, worth checking out.

COOL 的咧!
gitfs 作为一种 FUSE 文件系统,
全面整合 git,
包含真正伟大的功能,值得折腾!

github.com

Shared by @mgrouchy
 
(`是也乎:`
细思恐极...这得懒到什么境界哪,
不过,好象/貌似 git 本质上就是一 FS 哪,,,
)


- [dedupe](https://github.com/datamade/dedupe)

用机器学习对结构化数据进行自动重复数据删除和实体化解决的库.

github.com

Shared by @paulshannon
 

- [icdiff](https://github.com/jeffkaufman/icdiff)

给 Diff 增加了彩色

github.com

Shared by @mgrouchy

## 文章

- [最常见的有关 Python 在大数据分析中的误解](https://www.airpair.com/python/posts/top-mistakes-python-big-data-analytics)

对 Python 在大数据分析领域的工作进行了扫盲.

airpair.com

Shared by @elldudley

(`是也乎:`
简而言之, 用既有的专业库就好) 

- [Pandas 最赞的 14 个特性](http://www.bigdataexaminer.com/14-best-python-pandas-features/)


详细给出了可能是 Pandas 最值得使用的 14 种特性,你应该拥有!

bigdataexaminer.com

Shared by @mgrouchy

(`是也乎`:
言而简之:

- 数据加载
- 函式重构
- Map
- 可重用的 Map
- 列数据
- Unique 函式
- 交叉表
- 子表
- 图表
- 成组统计
- 集合函式
- Join
- 掩模
- 隐藏失效值
) 

- [Asyncio 资源](http://asyncio.org/)

Asyncio 模块相关的资源收集,
你值得拥有

asyncio.org

Shared by @mgrouchy
 

- [企业级 Python 的 10 个传说](https://www.paypal-engineering.com/2014/12/10/10-myths-of-enterprise-python/)

来自PayPal工程师的神话消解

paypal-engineering.com

Shared by @myusuf3

(`是也乎:`
简单的说,在长达15年的规模使用 Python 后,全然要面对以下传说:

- Python 是门新语言
- Python 不用编译
- Python 不安全
- Python 只是个脚本语言
- Python 是弱类型语言
- Python 很慢
- Python 不能平行扩容
- Python 缺乏良好的并发
- Python 程序猿很稀少
- Python 没有大项目
    + 美联行的Python项目是 5000人 1千行 代码
    + JP Morgan 类似
    + YouTube 只有 100万行代码
    + ... 嚓了个嚓!

`细思恐极` 的是,这么多年了,如此坚定的在固定的命题上不断的黑 Python 的是谁?
Perl 嘛? 不象, Ruby 嘛好象...
不过,大妈个人相信 `PHP是最好的语言`

) 

- [Python 中的朴素贝叶斯](http://blog.yhathq.com/posts/naive-bayes-in-python.html)

很赞的一篇文章,
介绍在 Python 中应用  Naive Bayes 进行分类.

yhathq.com

Shared by @myusuf3
 

- [在 Python 中制造 Mockery](http://engineroom.trackmaven.com/blog/making-a-mockery-of-python/)

一个简单的实例,有关在项目中伪造需要的环境.

trackmaven.com

Shared by @myusuf3
 

- [Django 和 Flask: 为毛以及何时用哪个?](https://www.hakkalabs.co/articles/django-and-flask)

残酷的讨论,
何时应该切换框架了...

hakkalabs.co

Shared by @myusuf3
 

- [用 Python 和 MoviePy 折腾动画数据](http://zulko.github.io/blog/2014/11/29/data-animations-with-python-and-moviepy/)


Python 有很多伟大的数据可视化模块,
但是,一直缺乏 gif/视频 的输出,
现在可以用 MoviePy 完成这一效果了!

github.io

Shared by @myusuf3

## DAMA
(`大妈私人无责任播报`)


# 是也乎

- 141215 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 141213 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
