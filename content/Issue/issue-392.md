Title: Issue 392
Slug: issue-392
Date: 2019-10-30 11:42
Tags: Weekly,Python,pycoders,ZH

> 可期仙器 ->removestar ->自动替换*导入为显式导入

原文: [PyCoder's Weekly - Issue #392](https://pycoders.com/issues/392)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191030 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191030 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------




- [Black 19.10b0 发布](https://pycoders.com/link/2771/web)
    + GITHUB.COM/PSF

I've been using Black to automatically format most of my Python code since it came out last year, and it's been an incredibly helpful tool. Stable release coming soon. More about how to use Black here.


(`是也乎:`

不妥协的...何时 VSCode 们, 内置了 Black 才算得果位哪.

)


- [Python 和 PyQt: 构建GUI桌面计算器](https://pycoders.com/link/2768/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn how to create Graphical User Interface (GUI) applications with Python and PyQt. Once you've covered the basics, you'll build a fully-functional desktop calculator that can respond to user events with concrete actions.


(`是也乎:`

![PyQt](http://ydlj.zoomquiet.top/ipic/2019-10-30-ScreenShot%202019-10-30%2010.33.05.jpg)

真正上手就会发现, QtDesigner 生成的代码不如手工写的...

以及, 问题在 GUI 软件现在基本都向 WAP 转化了...
Electorn 面前, 以及 Flutter 的目标, 都是没 Qt 什么事儿的哪...

)


- [Python 3.8 中 System V式 共享内存性能](https://pycoders.com/link/2781/web)
    + VENKATESH-PRASAD RANGANATH

"To evaluate the performance gains from shared memory, I ran the following simple test—create a list of integers and double each integer in the list in parallel by chunking the list and processing each chunk in parallel." Surprising results!

- [何时切换为 Python 3.8](https://pycoders.com/link/2779/web)
    + PYTHONSPEED.COM

A quick rundown of the problems you might encounter when switching major Python versions.

(`是也乎:`

迁移不是问题, 问题是不兼容...

)


- [考虑使用 memoryview 和 bytearray 进行有字节零复制交互](https://pycoders.com/link/2765/web)
    + BRETT SLATKIN

- [用 Python 处理 TTF 字体文件](https://pycoders.com/link/2767/web)
    + READEVALPRINT.COM

## 讨论
> Discussions



NIL



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks



- [Python 类型检查入门](https://pycoders.com/link/2780/web)
    + REAL PYTHON 
    + video

Write better code with this step-by-step intro to Python type checking. Traditionally, types have been handled by the Python interpreter in a flexible but implicit way. Recent versions of Python allow you to specify explicit type hints that can be used by different tools to help you develop your code more efficiently.


(`是也乎:`


![Type chk](http://ydlj.zoomquiet.top/ipic/2019-10-30-ScreenShot%202019-10-30%2010.29.56.jpg)

可以说诚意了...

)


- [用 TensorFlow 2.0 创建 Keras 模型的3种姿势](https://pycoders.com/link/2766/web)
    + ADRIAN ROSEBROCK

Keras and TensorFlow 2.0 provide you with three methods to implement your own neural network architectures:, Sequential API, Functional API, and Model subclassing. Inside of this tutorial you'll learn how to utilize each of these methods, including how to choose the right API for the job.

- [直接在 Git工作流 中进行自动 Python 代码评论](https://pycoders.com/link/2749/web)
    + CODACY
    + sponsor

Codacy lets developers spend more time shipping code and less time fixing it. Set custom standards and automatically track quality measures like coverage, duplication, complexity and errors. Integrates with GitHub, GitLab and Bitbucket, and works with 28 different languages. Get started today for free →

(`是也乎:`

这个广告吃的舒心...

)



- [Python 社区专访 Al Sweigart](https://pycoders.com/link/2772/web)
    + REAL PYTHON

Al Sweigart is an accomplished developer, conference speaker, teacher, and origamist. But some may know him best for his numerous Python programming books, such as Automate the Boring Stuff with Python.


(`是也乎:`

![Interview](http://ydlj.zoomquiet.top/ipic/2019-10-30-ScreenShot%202019-10-30%2010.27.24.jpg)


采访...经常不爆料..

)


- [调试 TensorFlow 覆盖率](https://pycoders.com/link/2770/web)
    + NED BATCHELDER

"It started with a coverage.py issue: Coverage not working for TensorFlow Model call function. A line in the code is executing, but coverage.py marks it as unexecuted. How could that be?"


(`是也乎:`

有点儿象发动小说中人物来检查场景卫生一般...
)

- [用 Pandas 清理货币数据](https://pycoders.com/link/2769/web)
    + CHRIS MOFFITT

Tips on how to clean up messy currency data in Pandas so that you may convert the data to numeric formats for further analysis.

(`是也乎:`

数据清洗用 Pandas 本身, 有点累的...

)


- [用以科学可视化的 Python & OpenGL](https://pycoders.com/link/2757/web)
    + NICOLAS P. ROUGIER

An open-source book about Python and OpenGL for Scientific Visualization.


(`是也乎:`

开源图书, 完备阐述 GL 进行数据可视化时, Python 的嗯哼...

)


- [用 Postgres,Gunicorn 和 Nginx 对 Flask 进行 Docker化](https://pycoders.com/link/2758/web)
    + MICHAEL HERMAN

(`是也乎:`

Dockerizing -> Docker 化? 这个化字真的好用...
)


- [可以做的怪事儿,但最好嫑在 Python 里搞](https://pycoders.com/link/2759/web)
    + WILL CIPRIANO

(`是也乎:`

![python_int_cache](https://thoughts.willcipriano.com/content/images/2019/10/python_int_cache-1.gif)

这个演示动画非常有爱了...

)

- [Napari: Python 的快速 N维图像 查看器](https://pycoders.com/link/2776/web)
    + ILOVESYMPOSIA.COM

- [用 Python 为 Linux 创建 Keylogger](https://pycoders.com/link/2761/web)
    + DOTWEAK.COM

- [Obfuscating Python 代码](https://pycoders.com/link/2777/web)
    + GITHUB.COM/SHAKNA-ISRAEL

(`是也乎:`

混淆器...有一定作用, 但是和 golang 们编译出来的二进制发行包相比...聊胜于无了...

)


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [removestar: 自动替换*导入为显式导入](https://pycoders.com/link/2775/web)
    + ASMEURER.COM

(`是也乎:`

这可是救命般的好工具...
只是...这得分析每行代码, 找到任性引用的变量并合理完成针对性声明?

)


- [safe-assert: 安全且可组合的断言](https://pycoders.com/link/2762/web)
    + GITHUB.COM/SOBOLEVN 
    + • Shared by Nikita Sobolev

- [pydantic: 用 Python 类型提示进行数据解析和验证](https://pycoders.com/link/2778/web)
    + GITHUB.COM/SAMUELCOLVIN

- [pythonfuzz: 适用于 Python 的模糊覆盖测试](https://pycoders.com/link/2763/web)
    + GITHUB.COM/FUZZITDEV

(`是也乎:`

fuzz 测试, 很久没见相关工具出没了...
)


- [pygeos: 在 NumPy ufuncs 中包装 GEOS 几何函数](https://pycoders.com/link/2760/web)
    + GITHUB.COM/PYGEOS

- [ipynb-quicklook: 适用于 Jupyter/IPython notebook 的 macOS QuickLook 生成器](https://pycoders.com/link/2764/web)
    + GITHUB.COM/TUXU



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心


- [⋅ PyCon Sweden 2019](https://pycoders.com/link/2751/web)
    + October 31 to November 2, 2019

- [⋅ PyCon France 2019](https://pycoders.com/link/2752/web)
    + October 31 to November 4, 2019

- [⋅ PiterPy 2019](https://pycoders.com/link/2754/web)
    + November 1 to November 2, 2019
    + 俄国

- [⋅ Django Girls Groningen](https://pycoders.com/link/2755/web)
    + November 2 to November 3, 2019
    + 荷兰



- [⋅ PyCon Canada 2019](https://pycoders.com/link/2756/web)
    + November 16 to November 19, 2019 
    + in Toronto

(`是也乎:`

怪不得一直感觉 C 国亲切呢...年会也非常中国时段...

)

## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
    + 第3期
    + 101camp3py

> 第3期已开课, 为期6周;
**191103** 按时结束, 
届时启动 4py ;-)

- [2019 中国开源年会(COSCon'19)](https://kaiyuanshe.cn/activity/summit/coscon-2019/)
    + 教育分场
    + 大妈有约

# 是也乎
> NN 3816

- 首发: [Issue 392 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-392.html)
- 改进: [issue-392.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-392.md)


