Title: Issue 427
Slug: issue-427
Date: 2020-07-01 11:42
Tags: Weekly,Python,pycoders,ZH


> 机器狗已在公开发售,支持用 Python 对其编程...


原文: [PyCoder's Weekly - Issue #427](https://pycoders.com/issues/427)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200701 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200701 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [PEP 622: 结构模式匹配](https://pycoders.com/link/4373/web)
    + PYTHON.ORG

This PEP proposes adding pattern matching—a sort of enhanced switch statement—to the Python language. Read the PEP at the link above and follow the discussion on Reddit.


(`是也乎:`

```python
def is_tuple(node: Node) -> bool:
    match node:
        case Node(children=[LParen(), RParen()]):
            return True
        case Node(children=[Leaf(value="("), Node(), Leaf(value=")")]):
            return True
        case _:
            return False
```


这非常 Elixir 了.


)


- [Clinging to Memory: Python 函数调用如何增加内存使用量](https://pycoders.com/link/4366/web)
    + ITAMAR TURNER-TRAURING

One of the advantages Python has over a language like C is that you don’t have to worry about how memeory is freed up during program execution. But sometimes Python’s memory management doesn’t work the way you’d expect.


- [Python的 reduce(): 从实用风格到 Pythonic 风格](https://pycoders.com/link/4370/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how Python’s reduce() works and how to use it effectively in your programs. You’ll also learn some more modern, efficient, and Pythonic ways to gently replace reduce() in your programs.

(`是也乎:`

![reduce...](http://ydlj.zoomquiet.top/ipic/2020-07-01-py-map-filter-reduce-diff.jpeg)

用 eomji 来解释...

![reduce](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2012.07.02.jpg)

)


- [Python 语言的核心是什么?](https://pycoders.com/link/4390/web)
    + BRETT CANNON

What makes Python… Python? Is it the language semantics? A set of features? What could you strip away and still have something you’d call Python? Everyone needs a little programming language existentialism now and then.

(`是也乎:`

![RustPython](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2012.04.38.jpg)

这 logo 也忒萌了吧...

)


- [Python 模式匹配: 守卫和其他模式可能不会以您期望的方式进行交互](https://pycoders.com/link/4398/web)
    + NICK ROBERTS

There’s an implementation of PEP 622 that you can try out here. But it has some potentially confusing effects.

- [Boston Dynamics 现在向公众出售机器狗，您可以使用Python对其进行编程](https://pycoders.com/link/4392/web)
    + RON AMADEO

It only took 28 year, but now you can have your very own robot dog. If you can stomach the price tag, that is. But hey, it’s got a Python SDK!

(`是也乎:`

![Boston](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2012.25.55.jpg)

嗯哼?大众也可以拥有军事级机械人了?


)


- [如何在Python 3中欺骗神经网络](https://pycoders.com/link/4368/web)
    + ALVIN WAN

Is that a corgi or a goldfish?







## 讨论
> Discussions



- [Pandas 中浮点索引的目的是什么?](https://pycoders.com/link/4383/web)
    + STACK OVERFLOW

Considering issues like floating-point representation error, is it ever a good idea to use a float as an index?

- [为什么 math.sqrt 幂计算慢那么多?](https://pycoders.com/link/4372/web)
    + STACK OVERFLOW

Is it, though? The square root of 2 might not be a good value for timing comparisons.




## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [The Python heapq 模块: 使用 Heaps 和优先级队列](https://pycoders.com/link/4389/web)
    + REAL PYTHON

Explore the heap and priority queue data structures. You’ll learn what kinds of problems heaps and priority queues are useful for and how you can use the Python heapq module to solve them.


(`是也乎:`

![heapq](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2011.54.52.jpg)

)


- [在 Python 中仅一行就可以加速函数调用](https://pycoders.com/link/4393/web)
    + HACKEREGG.GITHUB.IO

The lru_cache decorator allows you to take advantage of memoization to optimize function calls.


- [Unicode 在 Python: 使用字符编码](https://pycoders.com/link/4381/web)
    + REAL PYTHON

In this course, you’ll get a Python-centric introduction to character encodings and Unicode. Handling character encodings and numbering systems can at times seem painful and complicated, but this guide is here to help with easy-to-follow Python examples.


(`是也乎:`

![Unicode](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2011.53.59.jpg)


用无线电载波来形容 Unicode 流程, 好赞.

)


- [PEP 620: 从 C API 隐藏实现详细信息](https://pycoders.com/link/4388/web)
    + PYTHON.ORG

Author Victor Stinner argues that Python’s C API is too close to the CPython implementation, which limits available optimizations and hinders the addition of new features. PEP 622 proposes hiding implementation details from the C API.



- [正则表达式/Pandas中的视图与副本等...](https://pycoders.com/link/4371/web)
    + REAL PYTHON 
    + podcast

Have you wanted to learn Regular Expressions in Python, but don’t know where to start? Have you stumbled into the dreaded pink SettingWithCopyWarning in Pandas? Then check out this episode of the Real Python Podcast.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-07-01-ScreenShot%202020-07-01%2011.50.59.jpg)

)


- [测试发出 HTTP 请求的 Python 代码](https://pycoders.com/link/4378/web)
    + ROMAN TOMJAK

The Dependency Inversion Principle helps you design code that is more extensible and easier to test. You can use it to test code that makes HTTP requests without using mocks.

(`是也乎:`

随着微服务的扩张,
RPC 盛大回归,
基于 HTTP 的请求越来越少的了...

)


- [Red Hat Enterprise Linux 8.2 带来更快的 Python 3.8 运行速度](https://pycoders.com/link/4379/web)
    + TOMAS OROSAVA

Red Hat explains how they compiled CPython with GCC’s -fno-semantic-interposition flag to get run time speed improvements up to 30% faster than normal.




- [可变默认值: 可变默认参数的逆向视图](https://pycoders.com/link/4387/web)
    + A. COADY 
    + opinion

Should you use mutable objects for default function arguments? Conventional wisdom says no, but has the risk been overstated?

- [Street Lanes Finder: 检测无人驾驶汽车的街道车道[2019]](https://pycoders.com/link/4375/web)
    + GREG SURMA

Learn how to use OpenCV to detect street lanes in an image of a road.



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [spot-sdk: Spot SDK Repo](https://pycoders.com/link/4384/web)
    + GITHUB.COM/BOSTON-DYNAMICS

- [Nuitka: Nuitka是用Python写的Python编译器](https://pycoders.com/link/4395/web)
    + GITHUB.COM/NUITKA

(`是也乎:`

好久没见这位的消息了,
还活着, 甚好.


)

- [pypareto: 排序链以进行 帕累托 边界提取](https://pycoders.com/link/4385/web)
    + GITHUB.COM/KUMMAHIIH

- [TextAttack: NLP 中用于对抗性攻击/数据增强和模型训练的 Python 框架](https://pycoders.com/link/4394/web)
    + GITHUB.COM/QDATA

(`是也乎:`

NLP 相关项目越来越多,
说明 AI 落地首先是这个方向?

)


- [konlpy: 用于 朝鲜语 自然语言处理的 Python软件包](https://pycoders.com/link/4396/web)
    + GITHUB.COM/KONLPY

(`是也乎:`


嗯哼, 很少见的小语种 NLP 模块哪...
目测是国家项目?
)


- [pyperclip: 跨平台 剪贴板 功能的 Python 模块](https://pycoders.com/link/4367/web)
    + GITHUB.COM/ASWEIGART

(`是也乎:`

这个可以有,
通过Py 就可以和远程主机进行 剪贴板 自动同步操作了?

)


- [magnum: 轻量级和模块化 C++11/C++14 图形中间件，用于通过Python绑定进行游戏和数据可视化](https://pycoders.com/link/4374/web)
    + GITHUB.COM/MOSRA

(`是也乎:`

反正 Python 从内核就设计的异常亲 C,
所以, 各种 C++ 的模块进行包装很自然.
)



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ FlaskCon (Online)](https://pycoders.com/link/4377/web)
    + July 4 to July 6, 2020

- [⋅ SciPy 2020 (Online)](https://pycoders.com/link/4376/web)
    + July 6 to July 13, 2020



(`是也乎:`

中国也已经接到有关通知, 允许线下集会申报了...

而且今年程序员节(10.24)可能有超级大会.

)







## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


101camp10py 开始报名

![报名](ydlj.zoomquiet.top/ipic/2020-06-22-200622reg10py-zip.jpg)

```

课程规划:
    报名截止 2020.7.20
    正式开课 2020.7.26
    课程结束 2020.9.06

```
详情 => [蟒营™ Python 入门班第10期](https://py.101.camp/)

> 提醒: 首周报名再优惠 420 元.


# PS:
- 首发: [Issue 427 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-427.html)
- 修订: [issue-427.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-427.md)


-------------
>> NN 4061

好文笔,感叹号年度配额: **1/3**

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

![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/427)






