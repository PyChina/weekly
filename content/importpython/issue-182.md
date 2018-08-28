Title: 蠎加载 182
Slug: importpython-182
Date: 2018-08-28 11:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 182](http://importpython.com/newsletter/no/182/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [PEP 505 -- None-aware operators](https://www.python.org/dev/peps/pep-0505/)
    + PEP

Several modern programming languages have so-called "null-coalescing" or "null- aware" operators, including C# , Dart, Perl, Swift, and PHP (starting in version 7). These operators provide syntactic sugar for common patterns involving null references.


(`是也乎:`

越来越多的语法糖,在老爹离开后开始嗯哼...不怕牙痛嘛?

    (a ?? 2 ** b ?? 3) == a ?? (2 ** (b ?? 3))
    (c() ?? c() ?? True) == True
    (True ?? ex()) == True
    (c ?? ex)() == c()

)


- [应该用哪些 Python 静态分析工具?](https://www.codacy.com/blog/which-python-static-analysis-tools-should-i-use/)
    + static analysis

In this review, we’ll be taking a look at our favorite options and explain which ones to use.



- [Python 和 Pandas 匿名化数据的简单方法](https://dev.to/r0f1/a-simple-way-to-anonymize-data-with-python-and-pandas-79g)
    + pandas

Recently, I was given a dataset that contained sensitive information about customers and that should not under any circumstance be made public. The dataset resided on one of our servers which I deem to be a reasonably secure location. I wanted to copy the data to my local drive, in order to work with the data more comfortably and at the same time not having to fear that the data is less save. So, I wrote a little script that changes the data, while still preserving some key information. I will detail all the steps that I have taken, and highlight some handy tricks along the way.

- [AWS Lambda + Serverless Framework + Python—  第1部分：循序渐进“Hello World”](https://hackernoon.com/aws-lambda-serverless-framework-python-part-1-a-step-by-step-hello-world-4182202aba4a)
    + aws lamda

I am creating a series of blog posts to help you develop, deploy and run (mostly) Python applications on AWS Lambda using Serverless Framwork.




- [SIP Telephony 在 Python - pdf 文件](http://39peers.net/download/doc/report.pdf)
    + SIP

Implementer’s Guide to Scalable and Robust Internet Telephony with Session Initiation Protocol in ClientServer and Peer-to-Peer modes in Python




- [2018 年顶级编程语言 - IEEE Spectrum](https://spectrum.ieee.org/at-work/innovation/the-2018-top-programming-languages)
    + ranking

Python extends its lead, and Assembly enters the Top Ten

- [线性压缩在 python: PCA vs 无监督的特征选择](http://efavdb.com/unsupervised-feature-selection-in-python-with-linselect/)
    + data science

We illustrate the application of two linear compression algorithms in python: Principal component analysis (PCA) and least-squares feature selection. Both can be used to compress a passed array, and they both work by stripping out redundant columns from the array. The two differ in that PCA operates in a particular rotated frame, while the feature selection solution operates directly on the original columns. As we illustrate below, PCA always gives a stronger compression. However, the feature selection solution is often comparably strong, and its output has the benefit of being relatively easy to interpret — a virtue that is important for many applications.

- [OpenCV 数人头](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
    + image processing

In this tutorial you will learn how to build a “people counter” with OpenCV and Python. Using OpenCV, we’ll count the number of people who are heading “in” or “out” of a department store in real-time.

(`是也乎:`


![opencv_people_counter_result02](https://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/people-counting/opencv_people_counter_result02.gif)


)


- [Salmon Run:用 Python dedupe library 嗯哼重复关键字](http://sujitpal.blogspot.com/2018/08/keyword-deduplication-using-python.html)
    + topic modeling

I have been experimenting with keyword extraction techniques against the NIPS Papers dataset, consisting of titles, abstracts and full text of all papers from the Neural Information Processing Systems (NIPS) conference from 1987-2017, and contributed by Ben Hamner. The collection has 7239 papers written by 9785 authors. The reason I preferred this dataset to others such as Reuters or Medline is because it is smaller, and I can be both programmer and domain expert, and because I might learn interesting things while combing through the text of the papers looking for patterns to exploit.

- [市长来自哪 : 用 Python 和 SPARQL 查询维基数据 - 参数化思想](https://janakiev.com/blog/wikidata-mayors/)
    + datascience, sparkql

In this article, we will be going through building queries for Wikidata with Python and SPARQL by taking a look where mayors in Europe are born.





## 好物
~ 包/模块/库/片段...


- [Deep-Learning-World](https://github.com/astorfi/Deep-Learning-World)
    - 1373 Stars, 95 Fork

Organized Resources for Deep Learning Researchers and Developers

- [kefir](https://github.com/yogurt-cultures/kefir)
    - 288 Stars, 21 Fork

Kefir is a natural language processing kit for Turkic languages

(`是也乎:`

等等土耳其语言分析为什么是波兰工程师在嗯哼?

)


- [zalo_landmark](https://github.com/tiepvupsu/zalo_landmark)
    - 139 Stars, 19 Fork

Zalo landmark identification challenge, 103 classes, > 100k images (PyTorch)



- [SMBetray](https://github.com/quickbreach/SMBetray)
    - 135 Stars, 15 Fork

SMB MiTM tool with a focus on attacking clients through file content swapping, lnk swapping, as well as compromising any data passed over the wire in cleartext.

(`是也乎:`

> The code is ugly, but it has a great personality.

等等, 是那个 SMB ?


)

- [img_term](https://github.com/JonnoFTW/img_term)
    - 76 Stars, 5 Fork

Display image and video camera in your ANSI terminal!

(`是也乎:`

叕一个 CLI 界面看图工具

![rina](https://github.com/JonnoFTW/img_term/raw/master/screenshot2.png)

)


- [PaperTTY](https://github.com/joukos/PaperTTY)
    - 72 Stars, 3 Fork

PaperTTY - Python module to render a TTY on e-ink

(`是也乎:`

![萌](https://github.com/joukos/PaperTTY/raw/master/pics/terminus.jpg)

)

- [gluon-reid](https://github.com/xiaolai-sqlai/gluon-reid)
    - 72 Stars, 4 Fork

A code gallery for person re-identification with mxnet-gluon, and I will reproduce many STOA algorithm.

- [fagan](https://github.com/akanimax/fagan)
    - 36 Stars, 11 Fork

A variant of the Self Attention GAN named: FAGAN (Full Attention GAN)

- [django-vue-template](https://github.com/gtalarico/django-vue-template)
    - 32 Stars, 3 Fork

Django Rest + Vue JS Template

- [django-deployment-book](https://github.com/djangodeployment/django-deployment-book)
    - 20 Stars, 4 Fork

The Unix system administration guide for Django developers

- [decli](https://github.com/Woile/decli)
    - 9 Stars, 0 Fork

Minimal, easy-to-use, declarative cli tool

(`是也乎:`

叕一个 CLI 解释工具, 但是, 还是 click 好


)


- [aira](https://github.com/qpalzmqaz123/aira)
    - 8 Stars, 0 Fork

Aira is a simple script language based on python3

(`是也乎:`

这名字和那个下载器太象了...

而且, 一看语法就知道是 ruby 社区的人干的

)


- [csv-position-reader](https://github.com/loisaidasam/csv-position-reader)
    - 5 Stars, 0 Fork

A custom CSV reader implementation with direct file access

(`是也乎:`

> Why? / Who Cares?

这种开发态度, 大赞

)


- [cookiecutter-django-shop](https://github.com/awesto/cookiecutter-django-shop)
    - 3 Stars, 0 Fork

Cookiecutter django-SHOP is a blueprint for an e-commerce site based on django-CMS.

- [ews](https://github.com/sonakshs/ews)
    - 3 Stars, 1 Fork

Ethereum Web Service 

(`是也乎:`

这个实用哪, 只是 `django==1.9` 嗯哼?
)

### (￣▽￣)

- [PyCon 2018 China](http://cn.pycon.org/2018/)
    + 来了, 真的来了
- [phobal/ivideo](https://github.com/phobal/ivideo)
    + 神器,Electron

(`是也乎:`

万望低调嗯哼...

)


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180828 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180828 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


