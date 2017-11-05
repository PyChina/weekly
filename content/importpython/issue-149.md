Title: 蠎加载 149
Slug: importpython-149
Date: 2017-11-05 17:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 149](http://importpython.com/newsletter/no/149/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



 - [Python 技巧: 丹书](https://dbader.org/products/python-tricks-book/)
     + book

With Python Tricks: The Book you'll discover Python's best practices with simple, yet practical examples. You'll get one step closer to mastering Python, so you can write beautiful and idiomatic code that comes to you naturally.

- [PySpark 用 UDF 引入矢量化](https://databricks.com/blog/2017/10/30/introducing-vectorized-udfs-for-pyspark.html)
    + pyspark

This blog post introduces the Vectorized UDFs feature in the upcoming Apache Spark 2.3 release that substantially improves the performance and usability of user-defined functions (UDFs) in Python.



- [Pipfile 和 Pipenv : 依赖管理的未来](https://medium.com/@djiit/pipfile-and-pipenv-the-future-of-python-dependencies-management-8c0c5b6ec99b)
    + pipenv

Yes, I heared you. pip is a great tool and has been around for quite a long time. But for 3 years or so, people (contributors) have been looking for a way to enhance our packages management experience. Think about the superpowers of composer, npm (or better, yarn) in your favorite tool. What they offer is (more or less) a replacement for the age-old requirements.txt file : the Pipfile.


(`是也乎:`

是的, pip 的潜力远没有挖尽, 毕竟软件生命周期中部署和升级比开发要长的多...

)


- [用 Python 对排序算法进行可视化 - Python 艺术](https://www.makeartwithpython.com/blog/visualizing-sort-algorithms-in-python/)
    + visualization

Last week there was a great sorting algorithm post by morolin, where they showed an animation of quite a few different sorting algorithms. Morolin built their visualization in Golang. Today, we’ll try implementing our own version, using Python 3. We’ll end up with the following visualizations.


(`是也乎:`

![bubble_s](https://s3-us-west-2.amazonaws.com/makeartwithpython/bubble_s.gif)
![heap_s](https://s3-us-west-2.amazonaws.com/makeartwithpython/heap_s.gif)
![quick_s](https://s3-us-west-2.amazonaws.com/makeartwithpython/quick_s.gif)

三种排序算法的动态示意...

)


- [有蒙板的词云示例](https://medium.com/@dudsdu/an-example-of-word-cloud-with-mask-4cbbd699fb14)
    + visualization

A word cloud is a pretty traditional, and maybe already old fashioned way to depict the content of a text or a corpus (a set of texts). Nevertheless it is still a good way to convey the general idea of the text. This form of communication can be further improved by generating a word cloud image which resembles the general idea of the text. This article intends to demonstrate how to generate such a word cloud.




- [了解分布式 Tensorflow](https://medium.com/@manvithaponnapati/understanding-distributed-tensorflow-2cdbd9881d9b)
    + tensorflow

One of the biggest/best updates so far on tensorflow is the Distributed Tensorflow functionality. It allows you to scale your training to multiple machines. The tutorial here ?— https://www.tensorflow.org/deploy/distributed is great for folks who are very familiar with in’s and out’s of how tensorflow works. But it doesn’t really explain a lot of the terminology. This post is my journey of struggle with it.

- [为毛不能用 Python 列表过滤替代 SQL 过滤](https://medium.com/@jasperverbeet/how-you-cannot-replace-sql-filtering-for-python-list-filtering-b4ef57968ff0)
    + benchmark

Please don’t filter huge amounts of data in Python when trying to make a dashboard. But instead use a database, because in the end that is what it’s made for.


(`是也乎:`

DBA 是 Py 的一个常设领域,只是没有JS 嗯哼的快..

)

- [在调查数据集上实践聚类技术](https://medium.com/@blazetamareborn/practicing-clustering-techniques-on-survey-dataset-f7d7a322e6ff)
    + clustering

We have practiced Regression problem last time, which is a category of Supervised learning.

- [数据检索器2.1：Python界面，自动完成和更多](https://jabberwocky.weecology.org/2017/11/02/data-retriever-2-1-python-interface-autocomplete-more/)  
    + new release

We are exited to announce a new release of the Data Retriever, our software for making it quick and easy to get clean, ready to analyze, data.


- [PyPy 状态博客：如何令您的代码快 80 倍](https://morepypy.blogspot.ae/2017/10/how-to-make-your-code-80-times-faster.html)
    + pypy

I often hear people who are happy because PyPy makes their code 2 times faster or so. Here is a short personal story which shows PyPy can go well beyond that.

(`是也乎:`

从快5倍开始优化的, 现在80倍了, 基本追上 golang 的基本线了?
)


- [SQLAlchemy 中的多表过滤器](https://engineering.shopspring.com/multi-table-filters-in-sqlalchemy-d64e2166199f)
    + SQLAlchemy

For my team at Spring, one of the benefits of moving from Go to Python was being able to use a mature, field-tested ORM library such as SQLAlchemy. When the system you’re putting together grows over fifty tables, you learn to appreciate this powerful tool.

(`是也乎:`

SQLAlchemy 终于多年的媳妇熬成婆了

)


- [Python 中更快的物理库](https://blog.openai.com/faster-robot-simulation-in-python/)
    + robotics, simulation

We’re open-sourcing a high-performance Python library for robotic simulation using the MuJoCo engine, developed over our past year of robotics research.

(`是也乎:`

机械人工厂也是 py 进入的领域了

)


- [用 Python 探索美国警务数据](https://blog.patricktriest.com/police-data-python/)
    + data science

(`是也乎:`

等等, 这种操作合法嘛?
)


- [从Postgres 到 Python 的 1M行/秒](https://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/)
    + async

asyncpg is a new fully-featured open-source Python client library for PostgreSQL. It is built specifically for asyncio and Python 3.5 async / await. asyncpg is the fastest driver among common Python, NodeJS and Go implementations.


(`是也乎:`

只能说 Pg 太屌了...

)


- [用 Python 收集 Twitter 数据 - Alexander Galea的博客](https://galeascience.wordpress.com/2016/03/18/collecting-twitter-data-with-python/)
    + twitter

This post explains generally how my Python 3 tweet searching script works. Twitter limits the maximum age of searchable tweets to roughly a week. As such, the script can search for tweets posted up to just over a week ago. Twitter also limits the maximum number of tweets downloaded in every 15 minute interval.


(`是也乎:`

嗯哼?好象有开放接口可以直接获得的?
)



## 好物
~ 包/模块/库/片段...



- [curequests](https://github.com/guyskk/curequests)
    - 136 Stars, 3 Fork

Curio + Requests: Async HTTP for Humans

(`是也乎:`

叕一个 HTTP 工具,面向 Py3 的...

    from curio import run
    from curequests import get, post

    async def main():
        r = await get('https://httpbin.org/get')
        print(r.json())
        r = await post('https://httpbin.org/post', json={'hello': 'world'})
        print(r.json())

    run(main)

好吧, 简单的说还是太简单...

)


- [intro_ds_algo_py](https://github.com/tamim/intro_ds_algo_py)
    - 52 Stars, 16 Fork

Programs from my upcoming book, introduction to data structures and algorithms in Python.

(`是也乎:`

新书发布前先宣传有关示例代码?

)


- [scrapy-admin](https://github.com/liangWenPeng/scrapy-admin)
    - 8 Stars, 1 Fork

A django admin site for scrapy.




- [html-similarity](https://github.com/matiskay/html-similarity)
    - 0 Stars, 0 Fork

Compare html similarity using structural and style metrics

(`是也乎:`

直接给出两段 HTML 文本间的相似度
)

- [statically](https://github.com/AlanCristhian/statically)
    - 0 Stars, 0 Fork

Compiles a function or class with Cython. Use annotations for static type declarations. 

(`是也乎:`

很少见到 Cython 相关的嗯哼
)

### (￣▽￣)

- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

关键响应非常敏捷, 10.1 长徦期间嗯哼了一下, 立即追加了两个功能:
[pyheatmap/test.py at 31d80c89529e194e743e3125d56a189712186c55 · oldj/pyheatmap](https://github.com/oldj/pyheatmap/blob/31d80c89529e194e743e3125d56a189712186c55/examples/test.py#L49)

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)

- [Calysto/calysto_scheme: A Scheme kernel for Jupyter that can use Python libraries](https://github.com/Calysto/calysto_scheme)
    + scheme.ipynb

屌炸天的 Jupyter 能力扩展思路...


## 是也乎

- 171105 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171105 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


