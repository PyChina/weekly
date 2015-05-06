Title: 蠎加载 30
Slug: importpython-30
Date: 2015-05-04 18:18
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 30](http://importpython.com/newsletter/no/30/)

## 该读
~ 文章, Blog, 教程...

-	[亲爱的Python:致Python和Python社区的一封信](http://anna-oz.tumblr.com/post/117173382150/dear-python-a-love-letter-to-python-and-the)
    - python  

老爹推荐,你值得拥有

-   [Django测试的最佳方式和案例 - Part 1](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)
    - django  

测试可以帮助你构建优秀的代码,发现错误,在documentation.In这篇文章中,在看案例之前我们将首先看一个简单的介绍,其中包括最佳实践. 

-   [本日播客: 和Mike Bayer一起通过Python使用SQLAlchemy访问数据](http://www.talkpythontome.com/episodes/show/5/sqlalchemy-and-data-access-in-python)
    - sql, podcast  

本期播客我们将和Mike Bayer对话.Mike在2005年创建了SQLAlchemy,并在过去的10年里不断完善了这个令人赞叹的RDBMS ORM和数据访问层. 

-   [你的Django故事: 与Lieke Boon相遇](http://blog.djangogirls.org/post/117515207353)
    - django, interview  

Lieke是European Codeweek的荷兰大使,同时也是阿姆斯特丹Rails Girls和PyLadies活动的组织者.她是一名历史学家,开发者. 现在工作于VHTO,一个荷兰的女性科学技术专家组织. 你可以在荷兰的阿姆斯特丹找到她:)

-	[Two Scoops of Django 1.8 发布](http://pydanny.com/two-scoops-of-django-1-8.html)
    - django   

与Audrey Roy Greenfeld共同撰写,1.8版的<< Two Scoops of Django>>
内容上全部是能帮助Django的项目更好的知识. 我们引进各种提示,技巧,模式,代码片段,而且我们已经拿起多年来的技术. 而我们不知道或不能肯定的将通过世界上最优秀的专家获取他们的答案. 然后,我们将结果打包成了一本500多页的书. 

-   [用Python解决"Cheryl's Birthday"难题](http://nbviewer.ipython.org/url/norvig.com/ipython/Cheryl.ipynb)
    - ipython  

Cheryl的拼图设计用铅笔解决了,这在数学史上解决最大问题的工具(虽然有些人喜欢笔,粉笔,标记,或贴在沙子上画). 但我将展示如何用另一个工具解决它:Python代码. 


-	[从事Python工作的初级开发者必备技能是什么?](http://kieczkowska.tumblr.com/post/117227214396/asking-twitter-what-skills-are-required-from-a)

前段时间,我在PyCon2015遇到一些在网络中成长优秀的年轻人提出了这个问题,我在推特上挂出这个问题,以揭开发展成初级Python开发者的神秘面纱. 那么,到底什么是预期?

-   [Django 1.8 T-shirt来了](https://www.djangoproject.com/weblog/2015/apr/28/django-18-release-shirt/)
    - django   

所有利润将归Django软件基金会所有,用于DjangoCon的路费和类似Django Girls集会的活动支出. 

-   [用Python编写Google Chrome插件](https://pythonspot.com/create-a-chrome-plugin-with-python/)

谷歌浏览器插件是用HTML,JavaScript和CSS编写的. 如果你以前从来没有尝试过,我建议通过阅读本教程来写了一个Chrome插件. 在本教程中我们将告诉你如何用Python代替JavaScript来开发一个插件. 

(`是也乎:`

别上当,就是用 iframe 嵌入一个 web 环境而已...
和 Chrome 本身是隔离的

)

-   [Python without an operating system](http://lwn.net/SubscriberLink/641244/5d1d6d20aeb0a647/)
    - core python  

Josh Triplett开始谈移植Python运行在一个没有操作系统的环境下的"笑点"是在PyCon 2015:他和他英特尔的同事们得到了GRUB引导加载程序的解释器来运行BIOS或EFI系统. 他有很多有趣的事情和一些有启发性的演示来展示. 

-	[Python for Android: 入门](http://www.checkio.org/blog/python-android-getting-started/)
    - android  

这篇文章的目的不只是要表明Python可以编写Android应用程序,而是要表明已经有稳定,流行的工具来使用你喜欢的Python来编写Android游戏和应用程序. 

(`是也乎:`

除国产的 QPython 外都是作游戏的...

)

-   [开始使用Whoosh吧,一个纯Python的搜索引擎](http://sowingseasons.com/blog/introduction-to-whoosh.html)

Whoosh是一种纯Python编写的可嵌入搜索引擎. 它拥有很多价值其大小的高级特性(分类,高亮,压缩等)并执行能够添加简单的高级搜索功能在较小的项目上. 

(`是也乎:`

这个可以有!
只是和 ES 相比有什么优势!?
以往 纯Py 的SE 有很多,但是,没有一个流行起来,为毛?!

)


## 项目
~ 包/模块/库/片段...

-	[GitHack](https://github.com/lijiejie/GitHack)
    - 55 Stars, 31 Fork  

GitHack 利用 `.git` 文件夹的已知漏洞,
通过 `.git` 重新构建源码树,
保持目录结构不变. 

-	[moult](https://github.com/tweekmonster/moult)
    - 19 Stars, 0 Fork  

Moult是个实用工具,可以帮助你找到那些不再使用的包. 它的建立是为了帮助我清理项目的requirements.txt文件在项目大的修改之后. 但并非完美,但却比使用pip freeze进行打印快的多

- [pydisque](https://github.com/ybrs/pydisque)
    - 11 Stars, 0 Fork  

DISQUE 客户端,一个内存,分布式作业队列. 


- [disq](https://github.com/ryansb/disq)
    - 8 Stars, 0 Fork  

又一 DISQUE 的 Python客户端. 使用redis-py的HiRedi实现并通过它切换Redis的指令

-	[djangocms-forms](https://github.com/mishbahr/djangocms-forms)
    - 10 Stars, 1 Fork  

最简单灵活的Django CMS表单生成器

- [idris-py](https://github.com/ziman/idris-py)
    - 8 Stars, 0 Fork  

Idris的Python后台(成功Python源码,而不是字节码)

- [funcparserlib](https://github.com/vlasovskikh/funcparserlib)
    - 6 Stars, 0 Fork  

基于Python功能组合的递归下降解析器. 解析器组合都只是高阶函数,把分析器作为它们的参数,并将其退回的结果值. 

(`是也乎:`

嗯啍! 这才是格调!

     def parse(seq):
     'Sequence(Token) -> object'
     ...
     n = lambda s: a(Token('Name', s)) >> tokval
     def make_array(n):
     if n is None:
     return []
     else:
     return [n[0]] + n[1]
     ...
     null = n('null') >> const(None)
     true = n('true') >> const(True)
     false = n('false') >> const(False)
     number = toktype('Number') >> make_number
     string = toktype('String') >> make_string
     value = forward_decl()
     member = string + op_(':') + value >> tuple
     object = (
             op_('{') +
             maybe(member + many(op_(',') + member)) +
             op_('}')
             >> make_object)
     array = (
             op_('[') +
             maybe(value + many(op_(',') + value)) +
             op_(']')
             >> make_array)
     value.define(
             null
             | true
             | false
             | object
             | array
             | number
             | string)
    json_text = object | array
	json_file = json_text + skip(finished)

	return json_file.parse(seq)


目测,有关特性,赖总早已自行折腾过.

)


- 	[Python自然语言处理](https://github.com/SequomicsResearch/Natural-Language-Processing-with-Python)
    - 2 Stars, 0 Fork  


## 工作

- 	[猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
四月急招 N 名有服务端开发经验的 **gopher**!


- 	[猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

- 	[SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)  

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!


## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 	150505 spawnris/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 	150504 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

