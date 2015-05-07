Title: 蠎加载 31
Slug: importpython-31
Date: 2015-05-07 22:22
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 31](http://importpython.com/newsletter/no/31/)

## 该读
~ 文章, Blog, 教程...


- [Using Docker and Docker Compose for local Django development (replacing virtualenv) | Calazan.com](https://www.calazan.com/using-docker-and-docker-compose-for-local-django-development-replacing-virtualenv/#.VULF_bAmduE.reddit)
    + django, flask
Django and Flask are two well known Python web frameworks. There are lot of benchmarks claim Flask is 2x faster for simple JSON Response, one such is Techempower. After looking into the source, it struck me Django can do better!

Using Docker and Docker Compose for local Django development (replacing virtualenv) | Calazan.com
django
I'm not going to go into detail on how Docker and Docker Compose (formerly known as Fig) work as the Docker website already covers these. But I will explain how I set this up for an open-source Django app I've built, YouTube Audio Downloader, so you can try it out as well.

- [Django Performance: 4 Simple Things](http://revsys.com/blog/2015/may/06/django-performance-simple-things/)
    + django, performance
    
Below are four simple things you can do to quickly and easily improve the performance of your sites. They’re so simple you should make them part of your standard setup.

- [Selenium Testcase with Nose in Python](http://scrolltest.com/selenium-testcase-with-nose-in-python/)
    + testing
Nose makes Testing with Python wonderful. It basically extends the Unittest and provides features such as running only failed test, skip Test cases, running test based on priorities, REGEX pattern that makes Tester’s life easy

- [PyCon India 2015 is happening on Oct 2, 3, 4. Call For Proposals is open!](https://in.pycon.org/cfp/pycon-india-2015/proposals/)
    + pycon
PyCon India, the premier conference in India on using and developing the Python programming language is conducted annually by the Python developer community. It attracts the best Python programmers across the country and abroad.

- [PyCon India 2015 Registration Opened](https://in.explara.com/e/pycon-india-2015)
    + pycon
Early Bird Tickets On Sale. Get them before they are over.


- [Jython 2.7.0 final released!](http://fwierzbicki.blogspot.com/2015/05/jython-270-final-released.html)
    + jython
On behalf of the Jython development team, I'm pleased to announce that the final release of Jython 2.7.0 is available! It's been a long road to get to 2.7, and it's finally here.

(`是也乎:`

JAVA 不死,他只是慢慢....
)

- [Update on the PSF Elections - new election starting](http://pycon.blogspot.com/2015/05/update-on-psf-elections-new-election.html)
    + PSF
Due to some procedural problems with the current election for the Board of the Python Software Foundation, the Foundation has taken some steps to make sure that the elections are freely open for nominations and that there are no conflicts of interest.


- [Wing IDE 5.1.4 released](http://wingware.blogspot.com/2015/05/wing-ide-514-released.html)
    + new release
Wingware has released version 5.1.4 of Wing IDE, our cross-platform integrated development environment for the Python programming language.Wing IDE features a professional code editor with vi, emacs, visual studio, and other key bindings, auto-completion, call tips, context-sensitive auto-editing, goto-definition, find uses, refactoring, a powerful debugger, version control, unit testing, search, project management, and many other features.

-[Accepting PEP 492 (async/await)](https://mail.python.org/pipermail/python-dev/2015-May/139844.html)
    PEP
I've been following Yury's efforts carefully and I am fully confident that we're doing the right thing here. There is only so much effort we can put into clarifying terminology and explaining coroutines. Somebody should write a tutorial. (I started to write one, but I ran out of time after just describing basic yield.)

- [Awesome Django](http://awesome-django.com/)
    + django
A curated list of awesome Django apps, projects and resources. Inspired by and based on awesome-python.

- [PyPy.js: A fast, compliant Python implementation for the web](http://www.reddit.com/r/Python/comments/351e8b/pypyjs_a_fast_compliant_python_implementation_for/)
    + new release
PyPy.js is an experiment in building a fast and compliant python environment for the web. It uses the PyPy python interpreter, compiled for the web via emscripten, with a custom JIT backend that emits asm.js code at runtime.

- [5 Reasons why Python is Powerful Enough for Google](http://www.reddit.com/r/Python/comments/355tph/5_reasons_why_python_is_powerful_enough_for_google/)
    + core python
You're getting ready to start a new company. What language should you choose to build it?

-  [Python & RSA algorithm](http://blog.brainattica.com/rsa-with-cryptography-python-library/)
    +  crypto
There are Python libraries that provide cryptography services: M2Crypto, PyCrypto, pyOpenSSL, python-nss, and Botan's Python bindings. Five criteria can be evaluated when you try to select one of them: which C backend, how well maintained, Python support, reviewed and completeness. All failed the "reviewed" category. e.g. PyCrypto (probably the most used cryptographic library for Python) don’t work on PyPy.

# New Books

- [Hello Web App](http://hellowebapp.com/)
    + Tracy Osborn
Hello Web App is written for non-programmers by a designer, and will walk you through every step you need before launching your web app live to real customers. This book doesn't walk you through a specific tutorial, but instead uses a generic example to allow you to create something using Python and Django that interests you. Check the http://importpython.com/blog/ for an interview with the author of Hello Web App. 

(`是也乎:`

![Tracy Osborn](http://static1.squarespace.com/static/547d23c6e4b0faf2ab43e004/t/54fe17f3e4b017e64ba523f3/1425938420339/?format=300w)

美女写的技术图书...

)

## 项目
~ 包/模块/库/片段...


- [Easy-Card](https://github.com/x43x61x69/Easy-Card)
    - 68 Stars, 10 Fork
Easy Card is a smart card system widely used by Taiwanese, mainly for transportation purpose. However, unlike the PASMO card in Japan or T-Money in Korea, the Easy Card was lock out from reading via normal NFC readers. In other words, you can't check your balance with an app. That'd be a big issue if you are usually in a hurry and don't have the time to go to the MRT station just for it.

- [Robinhood](https://github.com/rohanpai/Robinhood)
    - 37 Stars, 7 Fork
Python Framework to make trades with Robinhood Private API See Blog Post: https://medium.com/@rohanpai25/reversing-robinhood-free-accessible-automated-stock-trading-f40fba1e7d8b

- [HardenFlash](https://github.com/HaifeiLi/HardenFlash)
    - 19 Stars, 6 Fork
Patching Flash binary to stop Flash exploits and zero-days

- [wordcloudbot](https://github.com/decause/wordcloudbot)
    - 4 Stars, 0 Fork
A systemd service that listens to fedmsg for IRC meeting logs, generates a word cloud, and tweets it to http://twitter.com/fedobot

- [marvelous](https://github.com/dcloud/marvelous)
    - 3 Stars, 0 Fork
Python bindings for Marvel Comics API

- [pyrthon](https://github.com/tobgu/pyrthon)
    - 2 Stars, 0 Fork
Pyrthon is a utility library that substitutes python collection literals with their Pyrsistent counterparts.

- [pyqtconsole](https://github.com/marcus-oscarsson/pyqtconsole)
    - 2 Stars, 0 Fork
pyqtconosle is a light weight python console for Qt applications. Its made to be easy to embed in other Qt applications and comes with some examples that shows how this can be done. The interpreter can run in a separate thread, in the UI main thread or in a gevent task. Support for asyncio might also be added in the future.

- [python](https://github.com/mfrance0916/python)
    - 2 Stars, 0 Fork
personal python bioinformatics scripts

(`是也乎:`
项目名称选择这种和语言一样的,只能说
...作的一手好死

)

- [GRE.py](https://github.com/saru95/GRE.py)
    - 1 Stars, 0 Fork
GRE Word of the Day notifier for OSX .

- [pygments-markdown-lexer](https://github.com/jhermann/pygments-markdown-lexer)
    - 1 Stars, 0 Fork
A Markdown lexer for Pygments to highlight Markdown code snippets.

- [normalizr](https://github.com/davidmogar/normalizr)
     1 Stars, 2 Fork
Normalizr is a Python library for text normalization that allows the next actions: Remove accents. Remove extra whitespaces. Remove hyphens. Remove punctuation. Remove stop words (from 13 different languages). Remove symbols.

- [phrack_reader](https://github.com/Qingluan/phrack_reader)
    - 1 Stars, 0 Fork
this is for hacker easy read phrack ezine ,welcom to figure out bug . 




## DAMA
(`大妈私人无责任播报`)
 
~ 参考: [为毛又一个蠎周刊?](importpython-why)

### 工作

-   [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/)   
四月急招 N 名有服务端开发经验的 **gopher**!


-   [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...  
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

-   [SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)  

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!

# 是也乎

- 15050? spawnris/[Zoom.Quiet](http://zoomquiet.io) 联合完成
- 150507 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.

