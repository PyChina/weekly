Title: 蠎加载 86
Slug: importpython-86
Date: 2016-08-29 22:22
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 86](http://importpython.com/newsletter/no/86/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [Python 打包现在不错了](https://glyph.twistedmatrix.com/2016/08/python-packaging.html)

Python packaging is not bad any more. If you’re a developer, and you’re trying to create or consume Python libraries, it can be a tractable, even pleasant experience. A historical perspective of how it's evolved and where it stands today.

(`是也乎:`

嗯哼?!谁说的?!
)

- [Python 3.6.0 alpha 4 预览版释放](http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html)
    + new release

Python 3.6.0a4 has been released. 3.6.0a4 is the last of four planned alpha pre-releases of Python 3.6, the next major release of Python. During the alpha phase, Python 3.6 remains under heavy development: additional features will be added and existing features may be modified or deleted. Please keep in mind that this is a preview release and its use is not recommended for production environments. Python 3.6.0 is planned to be released by the end of 2016. The first beta pre-release, 3.6.0b1, is planned for 2016-09-12.

(`是也乎:`

嗯哼,今年 PyCon16China 大会口号还有人提议: `就不用 Py3`
老爹太囧了...
)


- [每个人都要的 Python Library](https://glyph.twistedmatrix.com/2016/08/attrs.html)
    + core python

Do you write programs in Python? You should be using attrs.

(`是也乎:`

Limodou 就写过类似模块;-)
)


- [Django 技巧 #11 用 Chainable QuerySets 自定管理器](https://simpleisbetterthancomplex.com/tips/2016/08/16/django-tip-11-custom-manager-with-chainable-querysets.html)
    + django

In a Django model, the Manager is the interface that interacts with the database. By default the manager is available through the Model.objects property. The default manager every Django model gets out of the box is the django.db.models.Manager. It is very straightforward to extend it and change the default manager.

- [dis — Python 字节码反编译器 — PyMOTW 3](http://feeds.doughellmann.com/~r/DougHellmann/~3/5Xo7JUh8bNw/)
    + core python

The dis module includes functions for working with Python bytecode by “disassembling” it into a more human-readable form. Reviewing the bytecodes being executed by the interpreter is a good way to hand-tune tight loops and perform other kinds of optimizations. It is also useful for finding race conditions in multi-threaded applications, since it can be used to estimate the point in the code where thread control may switch.

(`是也乎:`

推荐用来估计代码中线程可切换点
)

- [Python 基金会寻求一位 blogger !](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/6pAlNacLd5g/the-python-software-foundation-is.html)
    + community

Are you the one ?

- [Andrew Ng 的机器学习练习在 Python](http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-1/)
    + machine learning

One of the pivotal moments in my professional development this year came when I discovered Coursera. I'd heard of the "MOOC" phenomenon but had not had the time to dive in and take a class. Earlier this year I finally pulled the trigger and signed up for Andrew Ng's Machine Learning class. I completed the whole thing from start to finish, including all of the programming exercises. The experience opened my eyes to the power of this type of education platform, and I've been hooked ever since.

- [Codementor: 如何使用 Python 上下文管理器制作 Sandwich](https://www.codementor.io/python/tutorial/how-to-make-a-sandwich-using-python-context-manager)
    + core python

Explains Context Manager using "Making a sandwich" as an example.

(`是也乎:`

![eEglAfJnT72Iw5chw0IT](https://www.filepicker.io/api/file/eEglAfJnT72Iw5chw0IT)
)

- [Micropython 以及如何在老屏幕上使用 esp8266.](http://garybake.com/wemos-oled-shield.html)
    + embedded systems

Wemos D1 mini is a 64x48 oled screen that can be mounted on the d1 really easily. The screen has an I2C interface and driven by a SSD1306 chip which is thankfully supported by micropython. Full details, code snippets, schematics can be found on this article.


(`是也乎:`

又见 I2C ...

![upy_logo](http://garybake.com/images/oled/upy_logo.jpg)


)

- [pyvideo is back](https://twitter.com/brandon_rhodes/status/764265053147148288)
    + video

Brandon Rhodes on Twitter: “Welcome to the new http://pyvideo.org !” Thanks to the original maintainers, the new, & the PSF for this site!





## 活动
~ Upcoming Conference / User Group Meet

- [Python Unconference 2016](http://www.pyunconf.de/)
- [Kiwi PyCon](http://kiwi.pycon.org/)
- [PyCon PL 2016](http://pl.pycon.org/2016/)
- [PyCon CZ 2016](https://cz.pycon.org/2016/)
- [PyCon DE 2016](http://pycon.de/)




## 项目
~ 包/模块/库/片段...


- [PokemonGo-TSP](https://github.com/tnlin/PokemonGo-TSP)
    - 65 Stars, 11 Fork

Solving TSP with Simulated Annealing

- [curlify](https://github.com/oeegor/curlify)
    - 15 Stars, 0 Fork

将 Python requests 的请求对象变成 curl 命令的库.

(`是也乎:`

win 用户受到 13206 点伤害
)


- [buildreport](https://github.com/orhanobut/buildreport)
    - 13 Stars, 1 Fork

对 android 的构建 github pr 生成总结报告


- [retry.it](https://github.com/seemethere/retry.it)
    - 8 Stars, 0 Fork

retry.it, 简单重试库

- [atom-tracer](https://github.com/OmarShehata/atom-tracer)
    - 8 Stars, 0 Fork

语言无关的 atom 包, 用以跟踪内联变量


- [pokemon-csv-to-map](https://github.com/asdfMaciej/pokemon-csv-to-map)
    - 8 Stars, 0 Fork

A tool useful for Pokemon Go maps, such as pogom or PokemonGo-Map.

- [geotagger](https://github.com/jkbrzt/geotagger)
    - 7 Stars, 0 Fork


通过智能手机的 GPS 记录为你的照片标记地理点


## DAMA
~ 无责任推荐


# 是也乎

- 160829 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 160829 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


