Title: 蠎加载 184
Slug: importpython-184
Date: 2018-09-08 12:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 184](http://importpython.com/newsletter/no/184/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...

- [探索 Python AST 生态 - YouTube](https://www.youtube.com/watch?v=Yq3wTWkoaYY)
    + video, AST

This session will introduce attendees to Python's rich ecosystem of abstract syntax tree tooling and libraries, with an emphasis on practical applications in static analysis and metaprogramming. Attendees should be fully comfortable with Python syntax and semantics, but familiarity with the ast module itself will not be necessary.

(`是也乎:`

Hummm... 可惜越来越 C+++++ 化的 Python 语法,已经气走了老爹, 
原先简洁的 AST 也难以嵌入到自制 DSL 中了哈?

)


- [给 python 程序猿的 React](https://www.softwarefactory-project.io/react-for-python-developers.html)
    + react

In this article I will present what I learned about React from a Python developer point of view.

(`是也乎:`

那什么, 可惜了 Ring 项目, 如果洪教授坚持到今天,
可能就没 React 什么事儿了吧..

)


- [对 op-ed 作者的语言学分析](http://maxberggren.se/2018/09/07/who-wrote-the-op-ed/)
    + stats, linguistics

David Robinson did a nice writeup of using his R package to analyze who wrote the “I Am Part of the Resistance Inside the Trump Administration” op-ed in NYTimes. His approach was with TF-IDF of the words. I wanted to try this with different text statsistics of the linguistic features instead, since I’m guessing word usage will not give the author away. And in Python of course.

(`是也乎:`

拼音类语言因为有天然的单词切分机制, 所以, 各种语言分析模块很充足,
中文光是分词, 就完杀现有伪 AI , 导致语音识别品质一直没实质嗯哼.

或是, 类似 ImageNet 的中文词性语料库, 能开发出来, 也是个坚实的开始哪...

> 可惜,汉语被和谐大神在高速演化中, 各种文字/词的含义几乎不可能稳定半年以上,没什么好策略来嗯哼

)



- [用 Doctor Thread 分析 Python 内存泄漏](https://engineering.citymapper.com/profiling-python-memory-leaks-with-doctor-thread.html)
    + debugging

(`是也乎:`

等等,什么时候 Py 也有内存泄漏问题了?

)


- [Running Python on your brain computer](https://www.youtube.com/watch?v=3elWlN0MzGw)
    + video, edtech

Reading and predicting what code will do is a fundamental coding skill. But when students read code are they executing it on their brain computer? Or do they only read the words?. This talk will explore learning to read and trace code, misconceptions and how to build a really good brain computer.

(`是也乎:`

YouTube 早已成为科技最前沿的展示平台了...

PyCon2018AU 上的嗯哼....



)


- [Python 在 2018 年 - JetBrains 的开发者生态系统状态](https://www.jetbrains.com/research/devecosystem-2018/python/)
    + python, jetbrains

(`是也乎:`


    Cookies and IP addresses allow us to deliver and improve our web content and to provide you with a personalized experience. Our website uses cookies and collects your IP address for these purposes.

    JetBrains may use cookies and my IP address to
    collect individual statistics and to provide me with
    personalized offers and ads subject to the Privacy
    Policy and the Terms of Use. JetBrains may use
    third-party services for this purpose. I can revoke
    my consent at any time by visiting the Opt-Out page.

    [Y]es, I agree[N]o, thanks
    ~ root#  

网页上嗯哼的提示窗, 非常 geek

)



- [机器学习的特征转换，初学者指南](https://medium.com/vickdata/four-feature-types-and-how-to-transform-them-for-machine-learning-8693e1c24e80)
    + machine learning

When first starting to learn how to optimise machine learning models I would often find, after getting to the model building stage, that I would have to keep going back to revisit the data to better handle the types of features present in the dataset. Over time I have found that one of the first steps to take before building the models is to carefully review the variable types present in the data, and to try to determine up front the best transformation process to take to achieve the optimal model performance.

- [用 Pandas 可视化财务数据 - Notebook](https://github.com/playgrdstar/financial_data_viz/blob/master/Visualising%20Financial%20Data.ipynb)
    + pandas

One of the best ways to demonstrate the usefulness of the Pandas library is to use it to analyse financial data.In this notebook, we will compute a few financial measures with Pandas?—?returns, volatilities and Value at Risk, and visualise/plot these measures.

- [介绍 Jupytext](https://medium.com/@marc.wouts/introducing-jupytext-9234fdff6c57)
    + juypter notebook

Jupyter notebooks are interactive documents that contain code, narratives, plots. They are an excellent place for experimenting with code and data. Notebooks are easily shared, and the 2.6M notebooks on GitHub just tell how popular notebooks are!

(`是也乎:`

对 .ipynb 的格式升级, 将代码反过来嵌入到 md 们中...

)



- [Linear Regression Using Least Squares](https://medium.com/@adarsh_menon_/linear-regression-using-least-squares-a4c3456e8570)
    + math

Linear Regression is the simplest form of machine learning out there. In this post, we will see how linear regression works and implement it in Python from scratch. This is the written version of the above video. Watch it if you prefer that.







## 好物
~ 包/模块/库/片段...

- [python-nubia](https://github.com/facebookincubator/python-nubia)
    - 425 Stars, 17 Fork

A command-line and interactive shell framework.

(`是也乎:`

![nubia](https://github.com/facebookincubator/python-nubia/raw/master/docs/interactive.gif?raw=true)

Fb 中 非洲兄弟们的项目?
看起来只是 fab 的升级交互界面, 
并不是为通用编程准备的...


)


- [lmdb-embeddings](https://github.com/ThoughtRiver/lmdb-embeddings)
    - 224 Stars, 12 Fork

Fast word vectors with little memory usage in Python

(`是也乎:`

NLP 的工具越来越多, 因为语音识别能力的上升, 
通过自然语言进行交互的场景在扩张...
可惜, 多数和中文没一毛銭关系...

)


- [pytorch-flows](https://github.com/ikostrikov/pytorch-flows)
    - 180 Stars, 8 Fork

PyTorch implementations of algorithms for density estimation

(`是也乎:`

PyTorch 和 TF 生态的攀比是开发者之福

)


- [0wned](https://github.com/mschwager/0wned)
    - 87 Stars, 17 Fork

Code execution via Python package installation.

(`是也乎:`

细思恐极, 这不是病毒又一攻击入口?

)

- [slither](https://github.com/trailofbits/slither)
    - 29 Stars, 2 Fork

Static Analyzer for Solidity

(`是也乎:`

Solidity 哈, 以太生态链也传染到 Python 世界了...

)

- [customized_nn](https://github.com/xieshuqin/customized_nn)
    - 18 Stars, 0 Fork

A flexible pytorch DataParallel module

(`是也乎:`

PyTorch 有了金主支持, 果断也开始爆裂了...

)


- [migration-sql](https://github.com/Workwell/migration-sql)
    - 4 Stars, 0 Fork

MySQL/MariaDB schema migration tool for Python 



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

- 180908 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180908 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


