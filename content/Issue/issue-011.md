Title: Issue 11 ~ Turn it Up 
Date: 2012-04-27 
Tags: Weekly,Pycoder,Zh 
Slug: issue-11 
## Hi Pythonistas!


Lots to cover this week. Last week mentioned we ordered some stickers, we are still trying to figure out how to best get them out to you guys. We hope in the meantime you guys reach out and let us know, what you think of the newsletter and if missed anything. We greatly appreciate your feedback.



想跟上所有 蠎界 新闻?
 [@pycoders](http://twitter.com/pycoders).

请用
[Gittip](https://www.gittip.com/PycodersWeekly)
支持俺们吧!

--
[Mahdi](https://twitter.com/#!/myusuf3) and [Mike](https://twitter.com/#!/mgrouchy)

原文: [Pycoder's Weekly (Issue #11) : Turn it Up](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=4f9b37c501)


## 新闻与开发动态

- [Cliff 0.1-0.2](http://blog.doughellmann.com/2012/04/cliff-command-line-interface_26.html) (doughellmann.com)
[Doug Hellmann](https://twitter.com/#!/doughellmann)
 of 
 [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
  and 
  [Python Module of the Week](http://www.doughellmann.com/PyMOTW/)
  fame, has a new project called Cliff. "Cliff is a framework for building command line programs. It uses setuptools entry points to provide subcommands, output formatters, and other extensions".  Check it out.

- [Octogit 0.1](http://myusuf3.github.com/octogit/) (github.com)
[Mahdi](http://twitter.com/#!/myusuf3)
 the other(very modest) half of the Pycoders team did the first release of a tool he has been working on called octogit. Octogit aims to provide a command line interface to github which allows you to create new repositories on github, as well as read/close new issues and a bunch of other neat things. Check it out.



## 讨论
- [What are the advantages of Python over Ruby?](http://www.quora.com/What-are-the-advantages-of-Python-over-Ruby) (quora.com)
I don't know if we want to get too involved in this discussion as it can be a controversial topic all around, but this is a pretty good discussion on Quora  about the advantages of Python over Ruby and some of the differences in each language and their communities.

- [I'm sick of PyCharm. It's insanely slow. r/python, what IDE do you recommend?](http://www.reddit.com/r/Python/comments/sqc0q/im_sick_of_pycharm_its_insanely_slow_rpython_what/) (reddit.com)
We are Vim(Mike) and Sublime Text(Mahdi) guys over here at Pycoders, so we don't really see what the fuss is all about, but there is a really in depth discussion on r/python about alternatives to the Pycharm IDE, if you are in the market for a new editor/ide or just want to see what's out there, it is worth taking a look at this discussion.



## 项目

- [python-bna](https://github.com/adys/python-bna) (github.com)
For all you python coders who also partake in Blizzard's games this is probably of interest to you. This is a Python implementation of Blizzard's Battle.net Mobile Authenticator.


- [python-mode](https://github.com/klen/python-mode) (github.com)
This is one of Mike's favorite things. Python-Mode for vim, it supports PyLint, Rope and Pydoc, as well as custom Python movement commands and a bunch of useful python addons. If you use Vim and Python together, this should be in your list of Vim plugins.

- [MongoAdmin](http://thomasst.ch/mongoadmin/) (thomasst.ch)
This is neat. This is an administration panel built with Django and Twitter's bootstrap for administering MongoDB databases. Currently the feature set is limited to JSON object editing and querying collections, but looks like there is more to come.

- [tornado-threadpool](https://github.com/rabidsnail/tornado-threadpool) (github.com)
This is a small, but novel library. Its essentially a threadpool for tornado. From the repo , Tornado-Threadpool is "A declarative library to make blocking code play nicely with the tornado ioloop"

- [pyfilesystem](http://code.google.com/p/pyfilesystem/) (code.google.com)
pyfilesystem is a python module that provides a common interface to many different file systems such as WebDav, FTP, SFTP, S3, Zip files and many others. This seems like a pretty great tool to add to your toolbox, definitely worth giving a look. Via @psnj

- [Micawber](http://charlesleifer.com/blog/micawber-a-python-library-for-extracting-rich-content-from-urls/)(charlesleifer.com)
Micawber is a library designed for embedding rich content using the oembed API, the basic workflow is that it supports a low level api that allows you to request rich metadata for a URL from a given endpoint, extract metadata from a block of text or html then parse a block of text or HTML and replace the urls with that rich content. If you are working on a project that requires embedding items with oembed, this is likely the library for you.

- [PyPI Mirror Status](http://www.pypi-mirrors.org/) (pypi-mirrors.com)
Ever have Pypi go down when you needed to develop some code? Nevermind don't answer that we all know you have. Here is a site listing alternatives and when they were last updated by Ken Cochrane


- [pinry - The self hosted Pinterest clone](http://overshard.github.com/pinry/) (github.com)
Like pinterest, but want to own and control all of your data? This may be the ticket for you. Pinry is a Pinterest-like app written in Django. If you have some Django experience and are interested in getting involved it looks like Isaac is looking for contributors.


## 文章

- [3D Programming in Python - Part 1](http://greendalecs.wordpress.com/2012/04/21/3d-programming-in-python-part-1/) (wordpress.com)
This is the first in a series of posts about 3D programming in Python. In this post the author explains how to do OpenGL calls with Pyglet and how to draw points and some basic geometric shapes with OpenGL.

- [Django Signals and the Observer Design Pattern](http://www.shutupandship.com/2012/04/django-signals-and-observer-design.html) (shutupandship.com)
This is a great article about how Signals work in Django and how they are used to implement the Observer pattern.

- [Python Deployment Anti-Patterns](http://hynek.me/articles/python-deployment-anti-patterns/)s (hynek.me)
Deploying application is hard. Hynek outlines some mistakes people make. He states deploying so many diverse applications requires solid and consistent deployment standards if you don't want to go crazy.

- [Python Iteration](http://nedbatchelder.com/text/iter.html) (nedbatchelder.com)
This is a short talk for a Boston Python night called "Fundamental Topics." by Ned Batchelder   It's intended to help beginners understand Python at a deeper level and this time he covered Python Iteration.

- [Heroku - Python Dependencies via pip](https://devcenter.heroku.com/articles/python-pip) (heroku.com)
Heroku is beefing up their docs for other languages besides ruby now and this is a great help page about dealing with Python dependencies via pip. This page covers all the basis and is a great primer for anyone who is using pip to install packages and manage dependencies in your python projects.

- [Python GUI Development [video]](http://www.youtube.com/playlist?list=PLA955A8F9A95378CE&feature=mh_lolz) [video] (youtube.com)
'Bo' takes us through building a GUIs with python using PySide (GUI builder for python). These videos are targeted at seasoned python developers who want to get into GUI development with Python.

- [Signpic - Signing Pictures with PIL](http://blog.ziade.org/2012/04/14/signpic-signing-pictures-with-pil/) (zaide.org)
This is a cool little library that allows you to watermark a photo with an image you provide. It also allows you to add the watermark to a directory of photos. Pretty awesome tool for the amateur photographers out there or anyone who is interested in image processing in Python.

- [Crawl a website with scrapy](http://isbullsh.it/2012/04/Web-crawling-with-scrapy/) (isbullsh.it)
Scraping allows you get any piece of information off a publicly available site.  Scrapy, a very powerful, and yet simple, scraping and web-crawling framework plans to make easier than ever.

- [One-line Tree in Python](https://gist.github.com/2012250) (github.com)
Nice little write up on writing a tree in a single line in python. You can do a few cool things like creating structure with assignment as well as nested dictionaries without explicitly creating sub-dictionaries.

- [History of Python development since 1990 with Gource [video]](http://www.youtube.com/watch?v=aPk1BqK8zzI) [video] (youtube.com)
Pretty cool visualization, of the development history of Python since 1990. It's cool seeing how the project has grown and developed since its infancy. 



# 是也乎

- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 131105 [Zoom.Quiet](http://zoomquiet.org/) 用时 4.2 分钟 完成原文 md 格式化.
