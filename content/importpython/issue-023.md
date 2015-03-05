Title: 蠎加载 23
Slug: importpython-23
Date: 2015-02-27 20:20
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 23](http://importpython.com/newsletter/no/23/)

## 该读
~ 文章, Blog, 教程...

- [真实世界中的Py优化: NumPy, Numba, 和 NUFFT](https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/)
    + performance

经常见到各种不成体系的优化教程,
这里,将描述整个儿优化过程,介绍这一的算法,即**非均匀快速傅立叶变换**(NUFFT)
从一个相对简单的 Python 实现开始,
从 Numba 获得帮助,
再接近高度优化后的 Fortran 实现.


- [Finance Event Study in iPython Notebook (Quantopian)](https://www.quantopian.com/posts/research-looking-for-drift-an-event-study-with-share-buybacks-announcements)
    + ipython

之前, 已经分享过 IPython notebook 上进行股票回报交易详细的过程,
现在,在相同环境中,
可以对一次股票回购事件,进一步挖掘研究了.

- [Ludovic Gasc (GMLudo): 微比对 Django, Flask 和 AsyncIO (aiohttp.web+API-Hour)](http://blog.gmludo.eu/2015/02/macro-benchmark-with-django-flask-and-asyncio.html)
    + django,flask,async-io

今天,建议你认真对比一下 HTTP 守护进程,
在 AsyncIO/falsk/django 之上实现的效果.
对于那些没有按照 AsyncIO 标准实现的,
aiohttp.web 
是基于 aiohttp 的轻量框架,
类似 Flask 只用很少的层,
实现了 AsyncIO 样的 http.

- [Django Girls 获得 PSF 社区服务大奖](http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/O86y2zJoWyQ/psf-community-service-award-goes-to.html)
    + PSF

"决议, Python 软件基金会2014年四季度社区服务奖, 
授予 Ola Sitarska 以及 Ola Sendecka 姐妹
发起的 Django Girls 活动,
经过可观的发展,已经在十几个国家蓬勃发展起来."

- [中级行者: Classes 和 Objects 第一部分](http://intermediatepythonista.com/object-orientation-in-python)
    + core python

本教程, 忽略了类和对象编程的基础,
专注提供更好的 Python OOP 方面的理解.
如果想尝试新式类,
应该从其超类开始理解.

- [同时支持 Django 1.7 和 South - Trey Hunner](http://treyhunner.com/2014/03/migrating-to-django-1-dot-7/)
    + django

想迁移包含 Django 和 South 的应用?
并加入 Django 1.7 的支持?!
此文完备的描述了如何作到这些.


- [Django 1.8 beta 1 和 1.7.5 发布](https://www.djangoproject.com/weblog/2015/feb/25/releases/)
    + django,new release

这天, Django 团队同时发布两个版本, 1.8 b1 包含 预览/测试包,
在进入第二阶段前,给我们机会先尝试一些 1.8 的变化.
另外,又发布了 1.7 系列的 bug 修复版 1.7.5 


- [Python 3.4.3 释出!](https://www.python.org/downloads/release/python-343/)
    + python

Python 3.4.3 相对
3.4.2 包含了很多修订以及小特性.


## 项目
~ 包/模块/库/片段...

- [CCrush-Bot](https://github.com/AlexEne/CCrush-Bot)
    - 108 Stars, 9 Fork

python 制造的 bot 
专门来玩 candy crush

- [autocomplete](https://github.com/rodricios/autocomplete)
    - 87 Stars, 6 Fork

点赞32!
模拟人类如何预测哪些人将会说什么,
即 实现 [Bing,Google,Yahoo,等等]
的 "自动完成功能".
只需要机械学习的库,就能快速达成,
详情链接中.

- [audiogrep](https://github.com/antiboredom/audiogrep)
    - 57 Stars, 3 Fork

对音频文件创建 "超级切片" ,
利用 CMU Pocketsphinx 完成语音识别.
用 pydub 将所有功能粘合起来,
从而能对 音频进行文字搜索.


- [peach](https://github.com/shuoli84/peach)
    - 22 Stars, 0 Fork

Peach 是文件下载缓存服务,
解放你的时间来创新,而不是等待.

- [Email_Analysis](https://github.com/lettergram/Email_Analysis)
    - 14 Stars, 0 Fork

邮件中都有什么词?
俺想知道,于是就有了这个分析器!

- [ipython-pip](https://github.com/jdfreder/ipython-pip)
    - 7 Stars, 0 Fork

支持用 pip 来安装 IPython notebook 的扩展

- [PyLyrics](https://github.com/geekpradd/PyLyrics)
    - 5 Stars, 0 Fork

Pythonic 的歌词获取器,
从 lyrics.wikia.com .

- [pyza](https://github.com/alphapapa/pyza)
    - 3 Stars, 0 Fork

Songza 的命令行客户端,
调用 VLC 来播放音频. 

## DAMA
(`大妈私人无责任播报`)


![PyCon Asia-Pacific 2015](http://zoomq.qiniudn.com/CPyUG/PyCon2015China/pycon-apac2015-logo.png)

- [亚太Py大会 6-5~7 在台北举行!](http://pycontw.blogspot.tw/2015/02/pycon-asia-pacific-2015-in-taiwan-save.html)

[PyCon APAC/Taiwan 2015 - Call for Proposals](https://tw.pycon.org/2015apac/en/call-for-proposals/) 议题召集已经释放,想去宝岛体验社区交流的,可以下手了!


## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...



# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150305 [Zoom.Quiet](http://zoomquiet.io) 用时 42 分钟完成快译.
- 150228 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
