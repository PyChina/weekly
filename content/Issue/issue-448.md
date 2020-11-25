Title: Issue 448
Slug: issue-448
Date: 2020-11-25 11:42
Tags: Weekly,Python,pycoders,ZH


> 格式化 Python 字符串/越来越复杂.


原文: [PyCoder's Weekly - Issue #448](https://pycoders.com/issues/448)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201125 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201125 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Synthetic Data Vault (SDV): 用于数据集建模的Python库](https://pycoders.com/link/5247/web)
    + ESMAEIL ALIZADEH

Creating realistic data for testing applications can be difficult, especially when you have complex data requirements and privacy concerns make using real data problematic. Enter Synthetic Data Vault, a tool for modeling datasets that closely preserves important statistics, like mean and standard variation.

- [Python enumerate(): 简化计数器循环](https://pycoders.com/link/5239/web)
    + REAL PYTHON

Once you learn about for loops in Python, you know that using an index to access items in a sequence isn’t very Pythonic. So what do you do when you need that index value? In this tutorial, you’ll learn all about Python’s built-in enumerate(), where it’s used, and how you can emulate its behavior.

(`是也乎:`


![enumerate](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.53.51.jpg)

enumerate 是强力模块, 
但是名字太复杂, 以至大家下意识的选择无视?



)

- [可复制和可升级的Conda环境: 带 conda-lock 的依赖项管理](https://pycoders.com/link/5240/web)
    + ITAMAR TURNER-TRAURING

If your application uses Conda to manage dependencies, you face a dilemma. On the one hand, you want to pin all your dependencies to specific versions, so you get reproducible builds. On the other hand, once you’ve pinned everything, upgrades become difficult. Enter conda-lock.

(`是也乎:`

conda 也值得有专用依赖管理工具.

)


- [Python 中的正则表达式和构建正则表达式](https://pycoders.com/link/5257/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn how to perform more complex string pattern matching using regular expressions, or regexes, in Python. You’ll also explore more advanced regex tools and techniques that are available in Python.

(`是也乎:`

![Regular](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.52.38.jpg)

为什么真蟒出课这么快?
流水线?


)


- [PyInstaller 4.1 支持了 Python 3.8 and 3.9](https://pycoders.com/link/5228/web)
    + PYINSTALLER.READTHEDOCS.IO



## 探讨/吐糟
> Discussions


- [学生要求我编写最小的图形用户界面,还得包括实际的用户](https://pycoders.com/link/5252/web)
    + REDDIT

(`是也乎:`

![wx](http://ydlj.zoomquiet.top/ipic/2020-11-25-lRYoanKZ258gnPosR1AW7v8Z1leCT0hfYQW1a03I52Y.jpg)

所以, 当然用现成的.


)


- [模式匹配的优势: 简单的比较分析](https://pycoders.com/link/5251/web)
    + PYTHON.ORG

(`是也乎:`

描述式编程和指令式编程...

)


## 文章/教程/嗯哼 
> Articles, Tutorials and Talks




- [在 Bootcamp 中不会教的 10 项 Python 技巧](https://pycoders.com/link/5250/web)
    + NICOLE JANEWAY BILLS

Here are ten practical and little-known pandas tips to help you take your skills to the next level.

- [使用 Python 的 bisect 模块](https://pycoders.com/link/5237/web)
    + JOHN LEKBERG

Python’s bisect module has tools for searching and inserting values into sorted lists. It’s one of his “batteries-included” features that often gets overlooked, but can be a great tool for optimizing certain kinds of code.


- [如何在Django Python Web框架中使用 Serializers](https://pycoders.com/link/5245/web)
    + RENATO OLIVEIRA

Serialization transforms data into a format that can be stored or transmitted and then reconstructs it for use. There are some quick-and-dirty ways to serialize data in pure Python, but you often need to perform more complex actions during the serialization process, like validating data. The Django REST Framework has some particularly robust and full-featured serializers.

- [情感分析/傅立叶变换和更多 Python 数据科学](https://pycoders.com/link/5229/web)
    + REAL PYTHON 
    + podcast

Are you interested in learning more about Natural Language Processing? Have you heard of sentiment analysis? This week on the show, Kyle Stratis returns to talk about his new article titled, Use Sentiment Analysis With Python to Classify Movie Reviews. David Amos is also here, and all of us cover another batch of PyCoder’s Weekly articles and projects.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.49.53.jpg)

群口

)


- [格式化 Python 字符串](https://pycoders.com/link/5234/web)
    + REAL PYTHON 
    + course

In this course, you’ll see two items to add to your Python string formatting toolkit. You’ll learn about Python’s string format method and the formatted string literal, or f-string. You’ll learn about these formatting techniques in detail and add them to your Python string formatting toolkit.

(`是也乎:`


C 语言只能一种格式化,
Python 发展到现在已经有无数姿势了,
但是, 我们还是不满足...

所以, 还是 LISP 们比较聪明?

)




- [当导入 Python 包时为空](https://pycoders.com/link/5235/web)
    + PETR ZEMEK

Did you know Python has two different kinds of packages: regular packages and namespace packages? It turns out that trying to import a regular package when you don’t have the right permissions causes Python to import it as a namespace package, and some unexpected things happen.

(`是也乎:`

这也是 Pythonista 几大常见困惑...

![ZEMEK](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.48.11.jpg)

作者 blog 的标签, 所以, 很难遇见只有 Python 体验的 Pythonista ?

)



- [用 Rust 和 Go 扩展 Python](https://pycoders.com/link/5236/web)
    + BRUCE ECKEL

Python extensions are a great way to leverage performance from another language while keeping a friendly Python API. How viable are Rust and Go for writing Python extensions? Are there reasons to use one over the other?

(`是也乎:`

俺感觉马上将有 Julia 加入这个扩展阵营...

)


- [用 scikit-learn 的 train_test_split( ) 分割数据集](https://pycoders.com/link/5253/web)
    + REAL PYTHON

In this tutorial, you’ll learn why it’s important to split your dataset in supervised machine learning and how to do that with train_test_split() from scikit-learn.

(`是也乎:`

![Dataset](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.44.25.jpg)

发型真不错.

)



- [适用于 Web 开发的 IPython](https://pycoders.com/link/5241/web)
    + ERIC HAMITER

This free, open-source book will help you learn more about IPython, a rich toolkit that helps you make the most out of using Python interactively.

(`是也乎:`

所以, Python 终于找到了 PHP-体位?

![Web](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.43.27.jpg)

)


- [用 Python 给照片添加新维度](https://pycoders.com/link/5230/web)
    + DYLAN ROY

Learn how to add some motion and a third dimension to a photo using depth estimation and inpainting.



   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [klio: 更智能的音频数据管道](https://pycoders.com/link/5256/web)
    + GITHUB.COM/SPOTIFY

(`是也乎:`

后来俺才知道, 
音频和图像没什么区别, 
都是矩阵运算...

![klio](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.40.23.jpg)

GitHub 自从上岸后, 第一时间关闭了针对大陆的图床解析,
果然 M$ 更加懂中国.


)


- [nbdev: 用 Jupyter 笔记本创建愉快的 Python 项目](https://pycoders.com/link/5254/web)
    + GITHUB.COM/FASTAI

(`是也乎:`

全新的项目脚手架思路...

)


- [pyo3: Python 解释器的 Rust 绑定](https://pycoders.com/link/5238/web)
    + GITHUB.COM/PYO3


(`是也乎:`

叕一个 Rust 绑定,
其实嘦用 GCC 类编译为机器码的语言, 都可以外挂给 Py 来耍...

)


- [yappi: 叕一个 Python Profiler](https://pycoders.com/link/5233/web)
    + GITHUB.COM/SUMERC

(`是也乎:`

Ya~哑, 

这个名称前缀真的可以千秋万代了...

)


- [topalias: Linux Bash/ZSH 别名生成器](https://pycoders.com/link/5244/web)  
    + GITHUB.COM/CSREDRAT

(`是也乎:`

![acts](http://ydlj.zoomquiet.top/ipic/2020-11-25-ScreenShot%202020-11-25%2010.36.46.jpg)

现在 github 项目没几个图标都不敢用了...

等等, 为什么要在多种 shell 中反复切换?


)


- [eff: 用于处理代数效应的库](https://pycoders.com/link/5255/web)
    + GITHUB.COM/ORSINIUM-LABS

- [SDV: 用于生成 表格/关系/时序数据 的合成数据](https://pycoders.com/link/5242/web)
    + GITHUB.COM/SDV-DEV



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5260/web)
    + November 25, 2020

(`是也乎:`

真蟒 找到赢利模式后,
就开始稳定开放了...

)


- [⋅ Pyjamas 2020 (Virtual)](https://pycoders.com/link/5231/web)
    + December 5, 2020

- [⋅ BelPy 2021 (Virtual)](https://pycoders.com/link/5249/web)
    + January 30 – 31, 2021


![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)

- PyCon2020中国
    + 11.28~29
    + 在线
- [⋅ Python Brasil 2020](https://pycoders.com/link/5113/web)
    + November 2 to November 9, 2020


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

None 

# PS:
- 首发: [Issue 448 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-448.html)
- 修订: [issue-448.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-448.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 创始组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------
>> NN 4208


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/448)






