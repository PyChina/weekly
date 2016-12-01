Title: 蠎加载 101
Slug: importpython-101
Date: 2016-12-01 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 101](http://importpython.com/newsletter/no/101/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Quiz Results](http://importpython.com/blog/post/quiz-results)
    + quiz

Thanks everyone for participating in the quiz. Nico Ekkart, Chad Heyne, Artem Bezukladichnii, Andrew Nester and Kyle Monson Congrats. Your copies of Writing Idiomatic Python is on its way. The Answers are on the blog post. ImportPython Subscribers can get a copy of Writing Idiomatic Python for a special price at https://jeffknupp.com/writing-idiomatic-python-ebook-importpython-q2vwt5/ . Thank you Jeff.

(`是也乎:`

上次的问卷结果出来了...
)


- [俺们如何部署 Python 代码 ? - Nylas](https://nylas.com/blog/packaging-deploying-python)
    + deployment

Building, packaging, and deploying Python using versioned artifacts in Debian packages. At Nylas, we’ve developed a better way to deploy Python code along with its dependencies, resulting in lightweight packages that can be easily installed, upgraded, or removed. And we’ve done it without transitioning our entire stack to a system like Docker, CoreOS, or fully-baked AMIs.

(`是也乎:`

老梗了,两年前就推荐过,这团队折腾到最后使用了 Debian 专用的 dh-virtualenv 工具,
对于多数团队而言,嗯哼的...
)

- [如何进行代码格式化令你的 Python 出色?](https://dbader.org/blog/python-code-linting#importpy)
    + code-quality

In Python code reviews I’ve seen over and over that it can be tough for developers to format their Python code in a consistent way: extra whitespace, irregular indentation, and other “sloppiness” then often leads to actual bugs in the program. Luckily automated tools can help with this common problem. Code linters make sure your Python code is always formatted consistently – and their benefits go way beyond that.

(`是也乎:`

Flake8+Sublime 的培训课程广告
)

- [在 Python 中检查所有条件匹配 - By Trey Hunner](http://treyhunner.com/2016/11/check-whether-all-items-match-a-condition-in-python/)
    + core-python

Use of any/all with generator expressions for improved readability and code clarity.

(`是也乎:`

运用内建函式 any/all
)

- [如何成为对冲基金的 Python 程序猿, by the CTO of AHL](http://nlp.hivefire.com/articles/share/68754/)
    + interview

We asked Collier what it takes to code in Python for a major quant fund. – And whether learning how to code as a second career after trading is actually viable. This is what he said.

(`是也乎:`

AHL?! 折腾宇宙奥密的 CTO 也转行基金了!?
突然理解了 洪教授...
)

- [计算科学和工程的 Python 3 ](http://www.southampton.ac.uk/~fangohr/teaching/python/book.html)
    + book

It's a free book available for download. This text summarises a number of core ideas relevant to Computational Engineering and Scientific Computing using Python. The emphasis is on introducing some basic Python (programming) concepts that are relevant for numerical algorithms. The later chapters touch upon numerical libraries such as `numpy` and `scipy` each of which deserves much more space than provided here. We aim to enable the reader to learn independently how to use other functionality of these libraries using the available documentation (online and through the packages itself).

(`是也乎:`

免费图书,用 py3 来演示计算科学领域中各种常见任务的解决,
也介绍了 numpy/scipy 等等关键库.
)

- [Django, fast: part 2](https://blog.mirumee.com/django-fast-part-2-d73a4ecd61f3#.bzhwna1v0)
    + django

In this second follow-up post Patryk Zawadzki makes use of wrk benchmarking tool and shows us the performance of gunicorn, uwsgi, PyPy. Besides benchmarking there is good insights into do's and don't of each deployment option.

(`是也乎:`

用标准的基准工具来测量 Django 的效能瓶颈
)


- [Python 内存管理](http://deeplearning.net/software/theano/tutorial/python-memory-management.html)
    + memory management

One of the things you should know, or at least get a good feel about, is the sizes of basic Python objects. Another thing is how Python manages its memory internally.

(`是也乎:`

其实吧,看中国原创的 Python 源代码鉴赏 更加能明白
)

- [Python 和虚拟环境](https://medium.com/@adityachhabra_73943/virtual-environments-f448f234271f)
    + virtual environment

A tour/tutorial of everything virtualenv.

(`是也乎:`

pyenv 早已是每天无法离开的命令了,当然, M$ 中嗯哼的.
)


- [聊哈对象 “优化”: __slots__ 以及 namedtuples.](https://oded.ninja/2016/11/30/__slots__-and-namedtuples/)
    + performance

- [用 HTRC 特性提取器在 Python 中折腾文本挖掘](http://programminghistorian.org/lessons/text-mining-with-extracted-features)
    + data mining

We introduce a toolkit for working with the 13.6 million volume Extracted Features Dataset from the HathiTrust Research Center. You will learn how to peer at the words and trends of any book in the collection, while developing broadly useful Python data analysis skills.

(`是也乎:`

基于 1360万卷文献资料的折腾... `可编程历史学`
国外各种领域的研究,除了论文发布,关联的重要发布就是一个个的开放数据包.
细思恐极.

当然也使用 ipynb 来组织和展示.
)

- [Awesome Django Admin](https://github.com/originalankur/awesome-django-admin)
    + django-admin
Curated list of awesome django resources aptly named Awesome Django Admin . If you have seen Awesome Python, it's on the same lines. Contribute to it.

(`是也乎:`

细思恐极哪, Awesome 系列是 github 中实事上的好物集锦前缀,
但是, `Django Admin` 只是一个框架中的一个功能,竟然也能攒出一个 Awesome 来...
这得复杂到什么地步哪...
)




## 好物
~ 包/模块/库/片段...


- [violentshell/rollmac](https://github.com/violentshell/rollmac)
    + 89 Stars, 13 Fork

Free networks often impose either a time or data restriction and this can be used quickly. When this happens you can change your mac address and reconnect, but this is annoying, and it takes time. In addition, most networks will ask you to re-accept the terms and conditions of the network in order to continue. Rollmac is designed to automate this process by using the WPAD protocol to discover the login page and automatically re-accept the terms and conditions.

(`是也乎:`

快速伪造 mac 地址来发起请求,以便加速测试,,,喂! 这也是 Spam/Spy 需要的哪!
)

- [dimmg/flusk](https://github.com/dimmg/flusk)
    + 52 Stars, 2 Fork

Flask - SQLAlchemy's declarative base - Docker - custom middleware.

(`是也乎:`

一次性将 SQLAlchemy+Flask+Docker 封装在了一起,形成完备的语义
)

- [amazon-polly-sample](https://github.com/awslabs/amazon-polly-sample)
    + 12 Stars, 2 Fork

This app allows you to easily convert any publicly available RSS content into audio Podcasts, so you can listen to your favorite blogs on mobile devices instead of reading them. 

(`是也乎:`

基于 AWS polly 服务,可以自动的将所有 RSS 内容转换为播客...
想听特川普每天为您播报天气嘛!? 嘦两行代码就可以了...
)


# 是也乎

- [The End Of Coder Influence \| Zed A\. Shaw](https://zedshaw.com/2016/11/24/the-end-of-coder-influence/)

(`嗯哼:`

这真是一个悲哀的故事...
)

- 161201 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 161201 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


