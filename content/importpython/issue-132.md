Title: 蠎加载 132
Slug: importpython-132
Date: 2017-07-07 10:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 132](http://importpython.com/newsletter/no/132/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [将 Python 和 Assembly 的力量联合起来](https://medium.com/@AntiSec_Inc/combining-the-power-of-python-and-assembly-a4cf424be01d)
    + asm

We can’t just copy/paste ASM directly into a Python script. Instead, python reads the machine code in as a bytearray of shellcode where the binary data is represented by a hex value where the \x represents the offset.

(`是也乎:`

ASM ...
)

- [pythonbooks.org](http://pythonbooks.org/)
    + books

Discover the best books in every Python book category.

(`是也乎:`

太实用了...当然的, 没有一本中国原创的.
)


- [用 Hydrogen 进行交互](https://softwaremill.com/interactive-programming-for-machine-learning-in-2017/)
    + IDE

Hydrogen is a package for Atom editor that allows interactive programming in different languages. I would call it a bridge, or even a sweet spot, between Jupyter Notebooks and a full blown IDE (like IntelliJ IDEA).

(`是也乎:`

桥件,能将 Jupyter 和 IDE 粘合起来
)


- [深入 Closures 和 Decorators - 第一部分](https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr)
    + closures

- [使用进程池加速您的Python数据处理脚本](https://medium.com/@ageitgey/quick-tip-speed-up-your-python-data-processing-scripts-with-process-pools-cf275350163a)
    + futures

With the concurrent.futures library, Python gives you a simple way to tweak your scripts to use all the CPU cores in your computer at once. Don’t be afraid to try it out. Once you get the hang of it, it’s as simple as using a for loop, but often a whole lot faster.

(`是也乎:`

问题是前提,你的数据是可原子切分处理的
)

- [设置 Sublime Text 3 为 Python 进行类型检查](https://medium.com/@erika_dike/setting-up-sublime-text-3-for-python-type-checking-85af5ce1a1ee)
    + sublime

- [GANs N’ Roses](https://medium.com/@rnaresh.n/gans-n-roses-c6652d513260)
    + machine learning

Imagine one day wherein we had a neural network which could watch movies and generate it’s own movies, or listen to songs and compose new ones. This network would learn from what it sees and hears without you explicitly telling it. This way of letting a neural network learn is known as unsupervised learning.

(`是也乎:`

无监督学习系统的嗯哼

)

- [PyPy 究竟是什么?](https://medium.com/@mindfiresolutions.usa/what-is-pypy-e34625eb1036)
    + pypy

- [PyBay 奖学金计划发布](https://medium.com/pybay/announcing-pybays-scholarships-program-4c8632146882)
    + conference

In the spirit of increasing the Python community’s inclusivity and diversity, PyBay is pleased to announce this year’s conference scholarships. Our scholarships are designed to support members of our community for whom attending PyBay would present a financial challenge.


- [开始 Jupyter Notebook 的5个最佳技巧](https://medium.com/arcgis-api-for-python-developers-corner/a-few-tips-to-get-you-started-with-jupyter-notebook-8f9b172d98cb)
    + jupyter

We’ve discussed a few reasons to use Jupyter Notebooks as a GIS user. From visualization of your data to the recent integration with the ArcGIS platform, Jupyter Notebooks are quickly becoming a crucial component of GIS and data science workflows. In spite of these benefits, coming up to speed and getting comfortable with Jupyter Notebooks can be a daunting task for a new user. There is nuance to the way Jupyter Notebooks operate that can take some time to comprehend.

(`是也乎:`

简单的说 ipynb 不是 IDE 也不是编辑器,
而是一个能方便的记录并同时积累我们思考的环境

)

- [机器学习和深度学习工程师的基础作弊书](https://startupsventurecapital.com/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5)
    + machine learning

CheatSheets for Pandas, numpy etc.


- [collections.Counter - Weekly Python Chat](https://www.crowdcast.io/e/counter/register)
    + counter

You want to count the number of times each thing occurs in your list. How do you do it? We'll talk about the many ways to solve this problem, concluding with the most Pythonic way: Counter.


- [scrapy 中的 404 链接检测器](https://gist.github.com/mdamien/7b71ef06f49de1189fb75f8fed91ae82)
    + code snippets

- [高级 Python 功能](https://tech.io/playgrounds/500/advanced-python-features/content/advanced-python-features)
    + core-python






## 好物
~ 包/模块/库/片段...


- [Susanoo](https://github.com/ant4g0nist/Susanoo)
    - 89 Stars, 12 Fork

A REST API security testing framework.

(`是也乎:`

看名字象日本人作品...
对 REST 接口进行安全性检验的框架
)

- [ssl_logger](https://github.com/google/ssl_logger)
    - 88 Stars, 13 Fork

Decrypts and logs a process's SSL traffic.



- [csvtotable](https://github.com/vividvilla/csvtotable)
    - 19 Stars, 0 Fork

Simple command-line utility to convert CSV files to searchable and sortable HTML table.

(`是也乎:`


![csvtotable](https://raw.githubusercontent.com/vividvilla/csvtotable/master/sample/table.gif)

嚓,根本就是 web 版本的 excel

)

- [CORStest](https://github.com/RUB-NDS/CORStest)
    - 13 Stars, 4 Fork

A simple CORS misconfigurations checker

- [unarcrypto](https://github.com/lclevy/unarcrypto)
    - 5 Stars, 0 Fork

unarcrypto is an educational tool to depict cryptography usage in zip, rar and 7zip archives

(`是也乎:`

少见的教学工具...

)

- [sukhoi](https://github.com/iogf/sukhoi)
    - 4 Stars, 0 Fork

Minimalist and powerful Web Crawler.

(`是也乎:`

基于原创的 [EHP](https://github.com/iogf/ehp) 模块
进行 pythonic 式的网页操作...

)

- [vault](https://github.com/gabfl/vault)
    - 0 Stars, 0 Fork

Python password manager 

(`是也乎:`

![vault](https://github.com/gabfl/vault/raw/master/img/demo.gif)

CLI 版本的 1Password

)


### (￣▽￣)

- [被忽视的攻击面：Python package 钓鱼](http://paper.seebug.org/326/)
    + pypi

(`是也乎:`

嚓了个嚓...
)


# 是也乎

- 170707 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170707 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


