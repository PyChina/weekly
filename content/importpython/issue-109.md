Title: 蠎加载 109
Slug: importpython-109
Date: 2017-02-05 12:21
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 109](http://importpython.com/newsletter/no/109/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Pycon 2017 议题选择](https://us.pycon.org/2017/schedule/talks/list/)
    + pycon

The acceptance and rejection letters for pycon arrived this week and so did the final list of selected talks for Pycon US 2017.

(`是也乎:`

相对国外的 PyCon 都是年头儿对上年回顾,中国的总是挤在年尾回顾当年...
因为春节哈...
)


- [Python 异步 I/O 嗯哼](http://pgbovine.net/python-async-io-walkthrough.htm)
    + video, asyncio

In this 90-minute video series, I walk through a book chapter about asynchronous I/O in Python called A Web Crawler With asyncio Coroutines, which was co-authored by the creator of Python.

(`是也乎:`

直播读书?
)

- [Instagram 关闭了 Python 的 GC](https://engineering.instagram.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172)
    + memory management, garbage collection

By dismissing the Python garbage collection (GC) mechanism, which reclaims memory by collecting and freeing unused data, Instagram can run 10% more efficiently. Yes, you heard it right! By disabling GC, we can reduce the memory footprint and improve the CPU LLC cache hit ratio. If you’re interested in knowing why, buckle up!

(`是也乎:`

随着 Py 在生产线上越来越嗯哼,
对 GC 的怨念总是在积累,终于,这一天来了...
)

- [Python 中重塑数据](https://medium.com/@robinlinderborg/reshaping-data-in-python-fa27dda2ff77)

I want to focus exclusively on the process of reshaping data, i.e. converting or transforming data from one format to another.
data manipulation


(`是也乎:`

不仅仅是格式转换, 更要有垃圾清理...
)

- [Wolfram 的自动机, 用 Python 简单嗯哼出了一个](http://www.faingezicht.com/articles/2017/01/23/wolfram/)
    + 

Complexity science is one of my favourite topics, ever. Studying complexity is how I ended up in the computer science bandwagon in the first place, and I constantly find myself thinking about how individual agents’ decisions affect the overall state of systems. Self-organization and emergence are fundamental aspects of how the pieces of the complexity puzzle fit together, and Wolfram’s elementary cellular automata are a great way to understand them.


(`是也乎:`

Wolfram 安身立命的核心技术, 成熟运行20多年, 哪儿这么简单的可以嗯哼出来哪...
)

- [加速 Python](http://alimanfoo.github.io/2017/01/23/go-faster-python.html)
    + performance, benchmarking

This blog post gives an introduction to some techniques for benchmarking, profiling and optimising Python code.

(`是也乎:`

又一个收集各种技巧的 blog ,不过, Python 的本意就不是为了运行时速度哪,
而是开发时效率...
所以...
)


- [在 Sublime Text 中对 Python 3.6 代码进行 lint](https://janikarhunen.fi/three-steps-to-lint-python-3-6-in-sublime-text.html#three-steps-to-lint-python-3-6-in-sublime-text)
    + subl

Writing consistent, well-formed code is important. Of course the functionality of the code is paramount, yet in addition the styling and structure should follow a commonly accepted standards. Not only will it make the code more approachable to others, but also to yourself, when you return to an old piece of software, which you have not looked at for months or even years. You might even squash some bugs early on, by writing code in consistent manner. The process of styling and checking of these code qualities, is often referred as linting.

(`是也乎:`

历史一再证明,一个稳定又开放的系统,总是能孕育出各种神奇的小品来
)


- [Assert Statements in Python](https://dbader.org/blog/python-assert-tutorial#.)
    + core-python

How to use assertions to help automatically detect errors in your Python programs in order to make them more reliable and easier to debug.

(`是也乎:`

断言,断的好,测试跑的好.
)

- [黑客统计](http://christopherroach.com/articles/statistics-for-hackers/)
    + Jupyter notebook

I've chosen to start with Harvard's Data Science course. I'm currently on week 3 and one of the suggested readings for this week is Jake VanderPlas' talk from PyCon 2016 titled "Statistics for Hackers". As I was watching the video and following along with the slides, I wanted to try out some of the examples and create a set of notes that I could refer to later, so I figured why not create a Jupyter notebook.

(`是也乎:`

一份课堂作业,总是可以嗯哼到 ipynb 中来...
)

- [用 Python 来开始 Spark Streaming + Kafka](https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/)
    + kafka, spark

In this article I am going to look at Spark Streaming. This is one of several libraries that the Spark platform provides (others include Spark SQL, Spark MLlib, and Spark GraphX). Spark Streaming provides a way of processing "unbounded" data - commonly referred to as "streaming" data. It does this by breaking it up into microbatches, and supporting windowing capabilities for processing across multiple batches. You can read more in the excellent Streaming Programming Guide.

(`是也乎:`

**EK/LS** 越来越有标准相了,当然的 Python 的各种绑定也快速跟上了,
幸福.

)

- [Sheila Miguez 和 Will Kahn-Greene 以及他们对 Python 社区的爱: Community Service Award Quarter 3 2016 Winners](http://pyfound.blogspot.com/2017/01/shelia-miguez-and-will-kahn-greene-and_19.html)
    + pyvideos

Sheila Miguez and William Kahn-Greene for their monumental work in creating and supporting PyVideo over the years.

(`是也乎:`

静静等待华人获得..
)

- [列表推导和生成器表达式](https://medium.com/@djangostars/list-comprehensions-and-generator-expressions-caf122a34091?source=rss------python-5)
    + core-python

Do you know the difference between the following syntax? [x for x in range(5)] , (x for x in range(5)), tuple(range(5)) Let’s check it.

(`是也乎:`

细微处见真情
)


- [用Django 和 ngrok 处理 webhooks](https://hackernoon.com/handling-webhooks-using-django-and-ngrok-b7ff27a6fd47#.bwvmuhprr)

In this article we’ll go over how to handle webhooks using Django, create a webhook in GitHub, and test the webhook on your local machine using ngrok. But first a brief primer on webhooks.

- [Python 自测](http://quizbucket.org/quiz/python/list-questions)
    + quiz

Comprehensive Python quiz and questions from basic to advanced level that help you to review your Python knowledge and become the master of Python.

(`是也乎:`

又一个 Python 能力测试卷,,,在答案剧透前,可以嗯哼一下
)

- [100 行以内的算法代码](https://www.oreilly.com/learning/algorithmic-trading-in-less-than-100-lines-of-python-code)
    + algorithmic trading

If you're familiar with financial trading and know Python, you can get started with basic algorithmic trading in no time.

(`是也乎:`

值得收藏, 但是,其实,最好是变成一个内建模块哪
)

- [Python 101 在 Leanpub Permanently 免费了](http://www.blog.pythonlibrary.org/2017/01/23/python-101-now-free-on-leanpub-permanently/)
    + ebook

(`是也乎:`

可是,为什么呢? 哈! 因为 201 要来了

![Python201_cover20160330_sm](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/04/Python201_cover20160330_sm-237x300.jpg)

)

- [在 Django 表单中覆盖字段小部件属性或如何将占位符添加到属性?](https://medium.com/@timonweb/override-field-widget-attributes-in-a-django-form-or-how-to-add-placeholder-attribute-to-django-a8a1f4632a09)
    + django

Let’s say we have a contact form and we want to add placeholders to this form inputs so our rendered form has these cool input labels. How do we do that?




## 好物
~ 包/模块/库/片段...

- [pipenv](https://github.com/kennethreitz/pipenv)
    - 2204 Stars, 48 Fork

Sacred Marriage of Pipfile, Pip, & Virtualenv.

(`是也乎:`

将三个最常用的官方外模块合并了


[![kennethreitz](https://avatars0.githubusercontent.com/u/119893?v=3&s=460)](https://www.kennethreitz.org/values)

大神操刀!-)

)

- [glazier](https://github.com/google/glazier)
    - 701 Stars, 33 Fork

A tool for automating the installation of the Microsoft Windows operating system on various device platforms.

(`是也乎:`

专注在各种设备上自动安装 Win 系统?!真爱!
)

- [syntax_sugar_python](https://github.com/czheo/syntax_sugar_python)
    - 492 Stars, 18 Fork

A library adding some anti-pythonic syntatic sugar to Python

(`是也乎:`

各种反 Pythonic 的特性...
)

- [crayons](https://github.com/kennethreitz/crayons)
    - 94 Stars, 2 Fork

Text UI colors for Python.

(`是也乎:`

又一个 CLI 依赖症患者

![crayons](https://camo.githubusercontent.com/b154bd4a5abd9a38b1b98fd66b4dfff09bb46753/68747470733a2f2f64337676366c703535716a6171632e636c6f756466726f6e742e6e65742f6974656d732f3371304932393371317a3239335233613361336e2f53637265656e25323053686f74253230323031372d30312d32332532306174253230362e30302e3032253230504d2e706e673f582d436c6f75644170702d56697369746f722d49643d32353737)
)

- [destruction](https://github.com/adtac/destruction)
    - 79 Stars, 3 Fork

Break Python programs with a simple import. 

(`是也乎:`

为毛作者要折腾这个? `¯\_(ツ)_/¯`
)

### (￣▽￣)

新年好,,,随领导去宇宙国了9天,所以,嗯哼了两期补起来!


# 是也乎

- 170210 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170210 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


