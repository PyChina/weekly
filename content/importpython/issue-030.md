Title: 蠎加载 30
Slug: importpython-30
Date: 2015-05-04 18:18
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)


- 原文: [Import Python Weekly Newsletter - Issue No 30](http://importpython.com/newsletter/no/30/)

## 该读
~ 文章, Blog, 教程...

-[Dear Python: A (Love) Letter to Python and the Python Community](http://anna-oz.tumblr.com/post/117173382150/dear-python-a-love-letter-to-python-and-the)
python
guido van rossum tweeted this, so I guess you have to read it.

- [Testing in Django Best practices and examples - Part 1](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)
django
Testing helps you structure good code, find bugs, and write documentation.In this post, we’ll be first looking at a brief introduction that includes best practices before looking at a few examples.

- [New Podcast Episode: SQLAlchemy and data access in Python with Mike Bayer](http://www.talkpythontome.com/episodes/show/5/sqlalchemy-and-data-access-in-python)
sql
, podcast
In this episode we speak with Mike Bayer. Mike created SQLAlchemy in 2005 and over the past 10 years has been building and refining this amazing RDBMS ORM and data access layer.

- [Your Django Story: Meet Lieke Boon](http://blog.djangogirls.org/post/117515207353)
django
, interview
Lieke is a Dutch Ambassador for European Codeweek, (co-)organizer of different Rails Girls events in the Netherlands and PyLadies in Amsterdam. She is a historian, a developer and currently working at VHTO, the Dutch national expert organisation on girls/women and science/technology. You can find her in Amsterdam, the Netherlands :)

- [Two Scoops of Django 1.8 is Out!](http://pydanny.com/two-scoops-of-django-1-8.html)
django
Co-authored with Audrey Roy Greenfeld, the 1.8 edition of Two Scoops of Django is filled to the brim with knowledge to help make Django projects better. We introduce various tips, tricks, patterns, code snippets, and techniques that we've picked up over the years. What we didn't know or weren't certain about, we found the best experts in the world and asked them for the answers. Then we packed the result into a 500+ page book.

- [Solving "Cheryl's Birthday" in Python](http://nbviewer.ipython.org/url/norvig.com/ipython/Cheryl.ipynb)
ipython
Cheryl's puzzle was designed to be solved with a pencil, the greatest problem-solving tool in the history of mathematics (although some prefer a pen, chalk, marker, or a stick for drawing in the sand). But I will show how to solve it with another tool: Python code.

-[What skills are required from a candidate for a junior Python developer job?](http://kieczkowska.tumblr.com/post/117227214396/asking-twitter-what-skills-are-required-from-a)
Some time ago, counting on my recently grown network of great people met @ PyCon 2015, I tweeted this open question to unveil the mystery which has grown around the position of a junior Python developer. So, what exactly is expected ?

- [Django 1.8 release shirt](https://www.djangoproject.com/weblog/2015/apr/28/django-18-release-shirt/)
django
All profits from the campaign go to the Django Software Foundation, to help fund activities like sprints, travel grants to DjangoCon, and supporting events like Django Girls workshops.

- [Create a Google Chrome plugin with Python](https://pythonspot.com/create-a-chrome-plugin-with-python/)
Google Chrome plugins are written in HTML, JavaScript and and CSS. If you have never written a Chrome plugin before I suggest reading this. We want to use Python instead of JavaScript and in this tutorial we will show you how to do that.

- [Python without an operating system](http://lwn.net/SubscriberLink/641244/5d1d6d20aeb0a647/)
core python
Josh Triplett started out with "the punchline" for his PyCon 2015 talk on porting Python to run without an operating system: he and his Intel colleagues got the interpreter to run in the GRUB boot loader for either BIOS or EFI systems. But that didn't spoil the rest of the talk by any means. He had plenty of interesting things to say and a number of eye-opening demos to show as well.

-[Python for Android: Getting Started](http://www.checkio.org/blog/python-android-getting-started/)
android
The purpose of this article is not just to show that it's possible to write applications for android, but to show that there's already stable and popular tools to write Android games and applications using your favorite language — Python.

- [Getting started with Whoosh, an all-Python Search Engine](http://sowingseasons.com/blog/introduction-to-whoosh.html)
Whoosh (source)is an embeddable search engine written in pure Python. It boasts many advanced features (faceting, stemming, highlights, compression, etc) for its size, and is perform-able enough to add simple-to-advanced search functionality on smaller projects.



## 项目
~ 包/模块/库/片段...

- [GitHack](https://github.com/lijiejie/GitHack)
    - 55 Stars, 31 Fork
GitHack is a .git folder disclosure exploit. It rebuild source code from .git folder while keep directory structure unchanged.

- [moult](https://github.com/tweekmonster/moult)
    - 19 Stars, 0 Fork
Moult is a utility that can assist you in finding packages that may not be in use any more. It was created to help me clean up a project's requirements.txt file after a major overhaul. It's far from perfect, but it's a lot faster than figuring out what's actually needed in a pip freeze print out.

-[pydisque](https://github.com/ybrs/pydisque)
    - 11 Stars, 0 Fork
Client for Disque, an in-memory, distributed job queue.

-[djangocms-forms](https://github.com/mishbahr/djangocms-forms)
    - 10 Stars, 1 Fork
The easiest and most flexible Django CMS Form builder!

-[disq](https://github.com/ryansb/disq)
    - 8 Stars, 0 Fork
A disque Python client. Under the hood, this used redis-py's HiRedis implementation and switches out Redis commands with the disque ones

- [idris-py](https://github.com/ziman/idris-py)
    - 8 Stars, 0 Fork
Python backend for Idris (generates Python source, not bytecode).

- [funcparserlib](https://github.com/vlasovskikh/funcparserlib)
    - 6 Stars, 0 Fork

Recurisve descent parsing library for Python based on functional combinators. Parser combinators are just higher-order functions that take parsers as their arguments and return them as result values.

(`是也乎:`

嗯啍! 这才是格调!

    def parse(seq):
        'Sequence(Token) -> object'
        ...
        n = lambda s: a(Token('Name', s)) >> tokval
        def make_array(n):
            if n is None:
                return []
            else:
                return [n[0]] + n[1]
        ...
        null = n('null') >> const(None)
        true = n('true') >> const(True)
        false = n('false') >> const(False)
        number = toktype('Number') >> make_number
        string = toktype('String') >> make_string
        value = forward_decl()
        member = string + op_(':') + value >> tuple
        object = (
            op_('{') +
            maybe(member + many(op_(',') + member)) +
            op_('}')
            >> make_object)
        array = (
            op_('[') +
            maybe(value + many(op_(',') + value)) +
            op_(']')
            >> make_array)
        value.define(
              null
            | true
            | false
            | object
            | array
            | number
            | string)
        json_text = object | array
        json_file = json_text + skip(finished)

        return json_file.parse(seq)


目测,有关特性,赖总早已自行折腾过.

)


- [Natural-Language-Processing-with-Python](https://github.com/SequomicsResearch/Natural-Language-Processing-with-Python)
    - 2 Stars, 0 Fork
Working with Natural Language Processing with Python. 

## 工作

- [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
四月急招 N 名有服务端开发经验的 **gopher**!


- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!

- [SeaSun 珠海急招](https://github.com/cheetahmobile/CMBM/wiki/SeaSunZh)

四月急招 10+名 有服务端开发经验的 **工程师** 待遇上不封顶!


## DAMA
(`大妈私人无责任播报`)

~ 参考: [为毛又一个蠎周刊?](importpython-why)


# 是也乎

- 1505?? [Zoom.Quiet](http://zoomquiet.io) 进行标点清查, Pelican 编译发布
- 1505?? gaojunteng 完成翻译, spawnris 接受 PR
- 150504 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
