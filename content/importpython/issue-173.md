Title: 蠎加载 173
Slug: importpython-173
Date: 2018-05-14 16:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 173](http://importpython.com/newsletter/no/173/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...



- [集合理论与实践: Grok Pythonic收集类型](https://www.youtube.com/watch?v=NeeO14QBW-s)
    + core-python, set

Sets and logic are strongly related. That's why proper use of set operations can eliminate lots of nested loops and ifs, producing code that is more readable and faster. Let's talk about using sets in practice, and learn great API design ideas from Python's set types. Luciano covered: - Python collection types - Theory and algebraic logic behind set-less and set types - Python protocols and operations for collections - Code examples for implementations of kinds of sets

(`是也乎:`

善用 set 可以有效减少不必要的 循环和 if 判定

)



- [Pyre: Python 的快速类型检查](https://www.facebook.com/notes/protect-the-graph/pyre-fast-type-checking-for-python/2048520695388071/)
    + pyre

Today, we're excited to announce Pyre, a static type checker for Python. Pyre is designed to help improve the quality and development speed in large Python codebases by flagging type errors interactively in your favorite editor. It checks the gradual type annotations that are already part of the Python programming language (PEP484).


(`是也乎:`


项目名字起的忒挫,以为是正则表达式相关的...

)



- [Mike Driscoll: PyCon 2018 – Conference Day 1 (May 11)](http://www.blog.pythonlibrary.org/2018/05/12/pycon-2018-conference-day-1-may-11/)
    + pycon, 2018

PyCon 2018 in Cleveland, Ohio kicked off their first conference day with an introduction from one of Cleveland’s natives, Ernest W. Durbin III. Then we moved on to the keynote of the morning which was given by Dan Callahan from Mozilla. He talked about tooling and how Python currently doesn’t have a big presence on the web. It was actually quite interesting and also a bit disappointing as there wasn’t really a true solution given. However his talk was quite good and insightful.


(`是也乎:`

那什么... PyConChina 今年, 俺依然无法全情投入推进了...

)


- [Python 类型注释的又一个(很好的)好处](https://medium.com/@shamir.stav_83310/the-other-great-benefit-of-python-type-annotations-896c7d077c6b)
    + annotations

Coming from statically typed languages, C and Java, I felt a little insecure writing Python code. Suddenly, silly type mismatch errors which I was used to catch during compilation were only caught (if at all, in the best case scenario) at runtime. This became especially annoying while learning new APIs or diving into a new large codebase, and made me completely reliant on documentation. While reading the docs is important on its own, I truly missed the comfortable and time-saving code completion on typing ‘.’ using IDEs such as IntelliJ.


(`是也乎:`

叕一则鼓吹 C++ 化 Py3 的嗯哼...

)


- [Python vs NumPy vs Nim](https://narimiran.github.io/2018/05/10/python-numpy-nim.html)
    + python, nim

Yesterday I’ve stumbled on the article Pure Python vs NumPy vs TensorFlow Performance Comparison where the author gives a performance comparison of different implementations of gradient descent algorithm for a simple linear regression example. Lately I’ve been experimenting with the Nim programming language, which promises to offer a Python-like easy to read syntax, while having C-like speeds. This seemed like a nice and simple example to compare speed between Nim and Python.


(`是也乎:`

![Nim](https://nim-lang.org/assets/img/logo.svg)

[Nim programming language \| Nim](https://nim-lang.org/) ~ 叕一个长的象 Py 但是更快的通用语言....

    # Compute average line length
    var
      sum = 0
      count = 0

    for line in stdin.lines:
      sum += line.len
      count += 1

    echo("Average line length: ",
         if count > 0: sum / count else: 0)


问题是, Numpy/Pandas/Jupyter/... 等等组成的数据科学生态,
Nim 语言根本无从对应生态来 PK ,
怎么可能仅仅因为几个排序速度就切换主力开发语言?

)


- [My Open Sourced Python Django Based CMS for Youtube Videos](https://medium.com/@mahmudahsan/my-open-sourced-python-django-based-cms-for-youtube-videos-9682e78e61d7?source=rss------python-5)
    + cms, video hosting

For last 3 months I regularly publish programming related youtube video tutorials for Bengali speaking people. After having 30+ videos I decided to make a website so that people can easily find my content, and can play the videos in my site. To solve this problem, I developed a small web application and made the code open sourced. The contents can easily add, modify or update from admin panel which will be reflected in the home page automatically.

- [How to make fail-safe APIs in Django?](https://medium.com/@kdpisda/how-to-make-fail-safe-apis-in-django-54fddb2a1679?source=rss------python-5)
    + django, API

While making APIs we must ensure that whatever happens, we must give proper response to the called API. I will be sharing my approach to make fail-safe APIs in Django. By fail-safe, I mean that no matter what, if an API is called it must be responded with a proper JSON or XML.

- [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py)
    + user submission

The shortest yet efficient Python implementation of the sequential pattern mining algorithm PrefixSpan, closed sequential pattern mining algorithm BIDE, and generator sequential pattern mining algorithm FEAT. https://git.io/prefixspan




- [PySiddhi](https://wso2.github.io/PySiddhi/)
    + streaming

PySiddhi is a Python wrapper for Siddhi. Which can listens to events from data streams, detects complex conditions described via a Streaming SQL language, and triggers actions. It performs both Stream Processing and Complex Event Processing on streaming data. Its Siddhi core is written in Java library.

(`是也乎:`


![PySiddhi](https://raw.githubusercontent.com/wso2/siddhi/master/docs/images/siddhi-overview.png?raw=true)

>  Sanskrit and Pali : सिद्धि; Kannada: ಸಿದ್ಧಿ; Telugu: సిద్ధి; Sinhala: සිද්දි; Tamil: சித்தி; Tibetan: དངོས་གྲུབ, THL: ngödrup

一看名字就知道是印度工程师哦哦的项目,
基于原有 JAVA 产品包装为 py 模块来完成海量数据流的功能扩展


)

- [Backdoored Python Library Caught Stealing SSH Credentials](https://www.bleepingcomputer.com/news/security/backdoored-python-library-caught-stealing-ssh-credentials/)
    + ssh, library

Barely a week has passed from the last attempt to hide a backdoor in a code library, and we have a new case today. This time around, the backdoor was found in a Python module, and not an npm (JavaScript) package. The module's name is SSH Decorator (ssh-decorate), developed by Israeli developer Uri Goren, a library for handling SSH connections from Python code.

(`是也乎:`

少见的白帽攻防案例嗯哼

)

- [发布 glom: 为 Python 重组数据](https://sedimental.org/glom_restructured_data.html)
    + glom

In the Python world, there's a saying: "Flat is better than nested." Maybe times have changed or maybe that adage just applies more to code than data. In spite of the warning, nested data continues to grow, from document stores to RPC systems to structured logs to plain ol' JSON web services. After all, if "flat" was the be-all-end-all, why would namespaces be one honking great idea? Nobody likes artificial flatness, nobody wants to call a function with 40 arguments.


(`是也乎:`

![comet_multi](https://sedimental.org/uploads/illo/comet_multi.png)

快速格式化数据集的 CLI 工具, 叕一种


)


## 好物
~ 包/模块/库/片段...

- [heap-viewer](https://github.com/danigargu/heap-viewer)
    - 181 Stars, 20 Fork

An IDA Pro plugin to examine the glibc heap, focused on exploit development

- [emojify](https://github.com/EvilPort2/emojify)
    - 146 Stars, 50 Fork

Turn your facial expression into an emoji

(`是也乎:`

emoji 已经是世界通用语言之一了

将表情识别对应为11种 emoji

)


- [Raspberry-Pi-Camera-Motion-Detection.](https://github.com/WillPhillipsCVdemo/Raspberry-Pi-Camera-Motion-Detection.)
    - 68 Stars, 8 Fork

Using Python code with a Raspberry-Pi, PIR motion and a Picamera, you can create a device which will email you a snapshot image when someone enters your room.


(`是也乎:`

叕一则 树莓派 上用 Python 进行机械视觉应用的案例

)


- [Dota2_Data_Analyst](https://github.com/CharlesLiuyx/Dota2_Data_Analyst)
    - 37 Stars, 0 Fork

A python project to process the data from Stratz.com and build machine learning model to predict the outcome of games

(`是也乎:`

专门为一家公司的对外数据进行可视化的工具

)


- [nx_altair](https://github.com/Zsailer/nx_altair)
    - 24 Stars, 2 Fork

Draw NetworkX graphs with Altair

(`是也乎:`


![nx_altair](https://github.com/Zsailer/nx_altair/raw/master/docs/_img/readme2.png)

)


- [pyinrail](https://github.com/nikhilkumarsingh/pyinrail)
    - 19 Stars, 7 Fork

A python wrapper for Indian Railways Enquiry API!

(`是也乎:`

印度铁路实时查询API ...

)


- [InternetSpeedNagger](https://github.com/crlsmnzs/InternetSpeedNagger)
    - 15 Stars, 3 Fork

Nags at my internet provider if my download/upload speeds aren't close to what they are supposed to be!


(`是也乎:`


基于 [Twitter Apps](https://apps.twitter.com/) 的实用工具

)


- [linux-kernel-code-reader](https://github.com/Alan-Lee123/linux-kernel-code-reader)
    - 13 Stars, 0 Fork

Draw the traces of linux kernel functions in a graph and link graph nodes to the source codes

(`是也乎:`

![kernel](https://github.com/Alan-Lee123/linux-kernel-code-reader/raw/master/trace.png)


果断叕一则基于 Graphviz 的应用工具

)



- [pytorch-coviar](https://github.com/chaoyuaw/pytorch-coviar)
    - 7 Stars, 2 Fork

Compressed Video Action Recognition

(`是也乎:`

![coviar](https://github.com/chaoyuaw/pytorch-coviar/raw/master/figs/coviar.png)

喂给 PyTorch 的嗯哼...国人参与的嗯哼

)



- [Internet-Speed-Tracker](https://github.com/mlcoursework/Internet-Speed-Tracker)
    - 4 Stars, 0 Fork

Logs your connection speed to a Google sheet.


(`是也乎:`

叕一个网络速度自动检测工具, 不同的是将日志吐给 docs.google 当前的大陆用不了

)


- [setdict](https://github.com/arthurmoreno/setdict)
    - 4 Stars, 0 Fork

Python dict-like interface for merging dicts with add to set property

(`是也乎:`

MongoDB 的单特性嗯哼

)


- [assert_types](https://github.com/matthew-sochor/assert_types)
    - 3 Stars, 0 Fork

Python decorator to assert types hints for python functions


(`是也乎:`

叕一个 py3 新功能的增强

)


- [apple-status-api](https://github.com/macadmins/apple-status-api)
    - 3 Stars, 0 Fork

Publish Apple service status notifications as a simple REST API


(`是也乎:`

这工具神了...

)


- [google-domain](https://github.com/yuzhoujr/google-domain)
    - 2 Stars, 0 Fork

available google domain from fortune 1000 companies

(`是也乎:`

手工支持公司域名本地解析?

)


- [akio](https://github.com/effyn/akio)
    - 2 Stars, 0 Fork

A Discord bot written in Python, with goals to simplify server setup for streamlined administration, include all essential features so that end users feel that one bot is enough, and to expand and re-imagine the purpose of Discord bots. 

(`是也乎:`

200行, 单文件完成的一个 bot

)


### (￣▽￣)


- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
    + 新年, events
    + [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...


*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...


<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...


## 是也乎

- 180514 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180514 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


