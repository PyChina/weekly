Title: 蠎加载 155
Slug: importpython-155
Date: 2017-12-17 18:42
Tags: Weekly,ImportPython,Zh

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 155](http://importpython.com/newsletter/no/155/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读
~ 文章, Blog, 教程...


- [开源 MonkeyType - 来自 Instagram](https://engineering.instagram.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881)
    + instagram, opensource

Today we are excited to announce we’re open-sourcing MonkeyType, our tool for automatically adding type annotations to your Python 3 code via runtime tracing of types seen.

(`是也乎:`

简单的说, 凡是深入大规模部署 Python 几年后,
无人忍受的了官方版本, 都在根据自己的业务来嗯哼出新的分支...
)


- [Dict to now retain insertion order](https://twitter.com/raymondh/status/941709626545864704)
    + core-python

Tweet



- [介绍为 Python 的 PrettyPrinter](http://tommikaikkonen.github.io/introducing-prettyprinter-for-python/)
    + prettify

PrettyPrinter is a powerful, syntax-highlighting, and declarative pretty printer for Python 3.6+. It uses a modified Wadler-Leijen layout algorithm, similar to those used in Haskell pretty printer libraries prettyprinter and ansi-wl-pprint, JavaScript's Prettier, Ruby's prettyprinter.rb and IPython's IPython.lib.pretty. It combines the best parts of each and builds more on top to produce the most powerful pretty printer in Python to date.


(`是也乎:`

叕一个对象输出美化模块,
只是, 这种只能满足程序猿私人观赏需求的,能存活多久?

![prettyprinterscreenshot](https://github.com/tommikaikkonen/prettyprinter/raw/master/prettyprinterscreenshot.png)

)



- [Python – 正则表达式实用指南](http://devarea.com/python-regular-expressions-practical-guide/#.WjU0WemWY8p)
    + regular expression

Regular Expressions are commonly used in Linux command line tools like sed, awk, grep etc. Most programming languages support them in either built – in or through an external library. The main problem of using them is that they difficult to understand, but they are well worth the effort to learn. Using a regular expression can save you a lot of time.

(`是也乎:`

啊...伟大精致易沉迷的 正则表达式 哪...


)


- [Kenneth Reitz – Episode 139 – Podcast.__init__](https://www.podcastinit.com/kenneth-reitz-episode-139/)
    + kenneth

Kenneth Reitz has contributed many things to the Python community, including projects such as Requests, Pipenv, and Maya. He also started the community written Hitchhiker’s Guide to Python, and serves on the board of the Python Software Foundation. This week he talks about his career in the Python community and digs into some of his current work.


(`是也乎:`

kenneth 老爹继承者之一...

)



- [enlighten](https://pypi.python.org/pypi/enlighten)
    + command line

Enlighten Progress Bar is a console progress bar module for Python. (Yes, another one.) The main advantage of Enlighten is it allows writing to stdout and stderr without any redirection.

(`是也乎:`

![multiple_logging](https://raw.githubusercontent.com/Rockhopper-Technologies/enlighten/master/doc/_static/multiple_logging.gif)

叕一个 CLI 进度条模块


)




- [Twitter 上的 Python 技巧日报](https://twitter.com/python_tip/status/940506518042169350)
    + tweet

Compare two floats with math.isclose() to see if they are nearly equal #python https://t.co/y9QiKtpbNP"

(`是也乎:`

早已订阅, 然后,无法分享...

)


- [Microsoft 考虑将 Python 作为正式脚本语言添加到 Excel 中](https://www.bleepingcomputer.com/news/microsoft/microsoft-considers-adding-python-as-an-official-scripting-language-to-excel/)
    + excel

Microsoft is considering adding Python as one of the official Excel scripting languages, according to a topic on Excel's feedback hub opened last month.

(`是也乎:`

迟了20年了....

)


- [专家 - Cartoon](http://turnoff.us/geek/the-specialist/)
    + humor

(`是也乎:`


![specialist](http://turnoff.us/image/en/the-specialist.png)


又一个伪装成程序猿的职业漫画家

)


- [Django Girls 的三潘市嗯哼](https://djangogirls.org/sanfrancisco/)
    + django-girls

If you’ve never coded before and want to learn how to make websites, we have good news for you: we are holding a one-day workshop for beginners! It will take place on February 25, 2018 at Collective Health in San Francisco.

(`是也乎:`

去年获得老爹认可的传教活动...

)


- [HereIsWally](https://github.com/tadejmagajna/HereIsWally)
    + tensorflow

HereIsWally is a Tensorflow project that includes a model for solving Where's Wally puzzles. It uses Faster RCNN Inception v2 model initially trained on COCO dataset and retrained for finding Wally using transfer learning with Tensorflow Object Detection API.

(`是也乎:`

COCO 数据集? 那个电影的?

)


## 好物
~ 包/模块/库/片段...


- [Anubis](https://github.com/jonluca/Anubis)
    - 347 Stars, 21 Fork

Subdomain enumeration and information gathering tool.

(`是也乎:`


            d8888                   888      d8b
           d88888                   888      Y8P
          d88P888                   888
         d88P 888 88888b.  888  888 88888b.  888 .d8888b
        d88P  888 888 "88b 888  888 888 "88b 888 88K
       d88P   888 888  888 888  888 888  888 888 "Y8888b.
      d8888888888 888  888 Y88b 888 888 d88P 888      X88
     d88P     888 888  888  "Y88888 88888P"  888  88888P'


哈, 这就是将经验嗯嗯嗯成了工具的结果.


)


- [robot-detect](https://github.com/robotattackorg/robot-detect)
    - 132 Stars, 26 Fork

Detection script for the ROBOT vulnerability

- [django-heroku](https://github.com/heroku/django-heroku)
    - 122 Stars, 6 Fork

A Django library for Heroku apps.

(`是也乎:`

叕一个专门为 Heroku 嗯哼的

)


- [pytorch-pose-hg-3d](https://github.com/xingyizhou/pytorch-pose-hg-3d)
    - 47 Stars, 3 Fork

PyTorch implementation for 3D human pose estimation.

(`是也乎:`

国人 PyTorch 实用嗯哼:

用机械学习来分析人体姿态, 主创是 寒羽良 的粉丝...

不过是在 USA 攻读的小组...

)


- [minipos](https://github.com/simon-v/minipos)
    - 22 Stars, 2 Fork

A self-hosted, 0-confirmation Bitcoin Cash point-of-sale server.

(`是也乎:`

叕一个 Btc 本地服务了...
)

- [Barcode-generator](https://github.com/bzimor/Barcode-generator)
    - 16 Stars, 8 Fork

Desktop app to generate EAN-13, EAN-8 and EAN-5 barcodes (other types are coming soon) automatically and save them as PDF or PNG, JPEG GIF image files with several sizes.

(`是也乎:`

是的, 不得不为 win 环境专门嗯哼一个版本...
)


- [retox](https://github.com/tonybaloney/retox)
    - 10 Stars, 0 Fork

For running a local continuous testing environment with tox.

(`是也乎:`

tox 应用的很广, 只是真心名气不显
)


- [LinkedInCommentAnalyzer](https://github.com/rozester/LinkedInCommentAnalyzer)
    - 10 Stars, 11 Fork

Extracting LinkedIn comments from any post and export it to Excel file.

(`是也乎:`

Excel 的确是 LinkedIn 气质
)


- [Twitter-API-Account-Manager-Python](https://github.com/smmtaheri/Twitter-API-Account-Manager-Python)
    - 5 Stars, 3 Fork

Python 3 script for managing of your twitter account using twitter official api's


(`是也乎:`

所以, 原先 Py2 成功的各种管理工具,将用 Py3 重制?
只是, 依然和中国无关 94 了.
)

- [machine-learning-microservice-python](https://github.com/yu-iskw/machine-learning-microservice-python)
    - 5 Stars, 0 Fork

Example to implement machine learning microservice with gRPC and Docker in Python 


(`是也乎:`

所以, 继 ipynb 成为标准教程发布形式后,
Docker 将成为标准示例发布形式了?

)


### (￣▽￣)

- [重大改革：Python 语言将被加入高考科目，VB 惨被淘汰！](https://mp.weixin.qq.com/s/kaEUp2q0K3a_huQa9m_LZg) 为了孩子,中国家长们得开始学习 Python 了... 
    + 传说 高考 编程
- [oldj/pyheatmap: python heat map library](https://github.com/oldj/pyheatmap)
    + 国货 heatmap 生成

只需要给出散点数据, 自动生成漂亮的热力图

神奇的是作者同时果断也是位 SiFi 作家:
[地球上的背包客 - Backpackers_on_Earth.pdf](https://oldj.net/static/writer/2015/Backpackers_on_Earth.pdf)


## 是也乎

- 171217 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 171217 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.


