Title: 蠎加载 Issue 15
Slug: importpython-15
Date: 2015-01-03 15:15
Tags: Weekly,ImportPython,Zh 

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/80)


原文: [Issue 15](http://importpython.com/newsletter/draft/15/)


## 该读
~ 文章, Blog, 教程...

- [Django vs Flask vs Pyramid: Choosing a Python Web Framework](http://importpython.com/click/track/7df2176d1067ab71eb3f42d0fbf7b7ed3fe13dc7?source=www.airpair.com)
Ryan built three identical apps in Django, Flask and Pyramid to illustrate the strengths and weaknesses of each one of them.

- [Python - subtle little performance boosts in Python](http://importpython.com/click/track/0e1df236ae20aeaf23b11909aedcd615e814e954?source=pythonfasterway.uni.me)

Subtle little performance boosts in Python. Tricks for your code to run faster.

- [Reviewing my marathon training using MapMyFitness and Pandas](http://importpython.com/click/track/41d80d16a0509387d8161ecbd49fb7358efe7734?source=www.davidketcheson.info)
I’m training for a marathon and I use MapMyFitness (MMF) on my iPhone to track my mileage and pace for each workout. MMF has a public API and Jason Sanford has written a Python front end for it. Which means that I can easily get hold of all my data in Python and explore it with Pandas!

- [Things which aren't magic - Flask and @app.route - Part 1](http://importpython.com/click/track/94cce063476e459710067f28e90be9337981a031?source=ains.co)

"Things which aren't magic", where I show how some of the nicer APIs provided by popular open source packages are constructed from the primitives of their respective languages. In this post we're going to take a look at Flask, and more specifically how Flask makes it possible to write "@app.route()" at the top of the function and expose its result to the internet.

- [Things which aren't magic - Flask and @app.route - Part 2](http://importpython.com/click/track/31f8e37f28e6253d801a2597a3a3d526dc9572ba?source=ains.co)
Part II of Things which aren't magic - Flask and @app.route. In this post we're going to turn up the difficulty level a tiny bit and add the ability to have variable parameters in our URLs, by the end of this blog post we'll be able to support the expected behavior for the following piece of code.

- [Your Django Story: Meet Claire Reynaud](http://importpython.com/click/track/5051ea34d27ce6168983eb101009c722292e2772?source=blog.djangogirls.org)

Claire is an iOS and Django developer. She works as a freelancer from Saint Etienne, in France. She started to work as a Java developer at Trango, a mobile virtualization company. She later joined Epyx in Switzerland, where she discovered iOS and Django. You can follow her @ClaireReynaud.


- [Terrible choices: MySQL | ionel's codelog](http://importpython.com/click/track/49f5f80db162ef146b57568825ee2a0d146330cd?source=blog.ionelmc.ro)
I've used MySQL for a while now, and there were lots of surprising things I needed to cater for. This is from a Django and MySQL 5.5 perspective [*]. Later on you'll see the horrible things I did to work around. It was a terrible experience, as I've also used PostgreSQL. Handy tip for making MySQL behave more like a real database (specifically, with Django).

- [Playing with Functions in Python](http://importpython.com/click/track/fda184262fc41e49f6f7f41f89c9c3b9d0457139?source=speedfulpanic.net)
Python is an extremely versatile language. It allows us to work in any of our favorite programming paradigms, including procedural programming. Procedural programming is subtly different from functional programming in that procedures are not strictly prohibited from changing a shared state implicitly. That is, callables may alter elements other than their arguments.

- [Python Twitter tutorial - 5 steps to tweet a message from python script](http://importpython.com/click/track/3d6fd7bb56134419e4351994191288523037d424?source=nodotcom.org)

In this tutorial, you will learn how to send tweets using Python. It includes Step By Step instructions to register your app with twitter.

- [Programming Computer Vision with Python](http://importpython.com/click/track/9669baa0a90cb0329e220eb0f7a074edef826211?source=programmingcomputervision.com)
image processing
The final pre-production draft of the book "Programming Computer Vision with Python" by Jan Erik Solem. (as of March 18, 2012) is available under a Creative Commons license. Note that this version does not have the final copy edits and last minute fixes. PCV is a pure Python library for computer vision based on the book "Programming Computer Vision with Python" by Jan Erik Solem.

- [Saving 9 GB of RAM with Python's __slots__](http://importpython.com/click/track/ccf8cbe90aeecbc771a4594719bc10b203b640b7?source=tech.oyster.com)

By default Python uses a dict to store an object’s instance attributes. However, for small classes that have a few fixed attributes known at “compile time”, the dict is a waste of RAM, and this makes a real difference when you’re creating a million of them. You can tell Python not to use a dict, and only allocate space for a fixed set of attributes, by settings __slots__ on the class to a fixed list of attribute names:

- [PyBoxes Tutorial / A Physics Driven Game Tutorial.](http://importpython.com/click/track/aa75dac13c51e1e08fb9e990eac6dd216fac402b?source=www.reddit.com)

Features that we will implement Basic Physics Simulation, GUI, Pseudo-wind, Pseudo-liquid, Anti-aliased drawing of circles (using GFXDraw), Customization of circles and colors.Goals achieved are learn the basics of Pymunk, Pygame, how a physics engine such as PyMunk would works with a library such as PyGame.

- [A curated list of awesome Django apps, projects and resources.](http://importpython.com/click/track/a5e05213b5e6467f92139cea2f6c4e9fe2301f2f?source=github.com)

Title says it all :)

- [Displaying Django User Messages with Angular.js](http://importpython.com/click/track/5227bf7f1cebfa5e6ce7f0d98736409f68072cdc?source=birdhouse.org)
Django’s Messages framework is an elegant workhorse, and I’ve never built a Django site that didn’t use it for displaying success/failure/info messages to users after certain actions are taken (like logging in successfully or adding an item to a cart). 

## 项目
~ 包/模块/库/片段...

- [relational](http://importpython.com/click/track/24f1cc20b803aea58990a35553aadf61f615712c?source=github.com)
    - 40 Stars, 0 Fork
SQL-Alchemy for Humans (and data nerds).

- [quicksafe](http://importpython.com/click/track/2935d9a0a3fe6ff15a1f12fdf7b52766eee2bf83?source=github.com)
    - 14 Stars, 0 Fork
quicksafe is a tiny Python script that provides a GUI text editor to edit notes that are then encrypted and stored within the script file itself.

- [pollywog](http://importpython.com/click/track/287abd7c13defa7536e283c3efcb549b6a8e5a43?source=github.com)
    - 11 Stars, 1 Fork
Syntactic sugar for working with regular expressions in Python.

- [twizhoosh](http://importpython.com/click/track/410a68c5d593a23d3cd4d6f530258f994e024401?source=github.com)
    - 6 Stars, 3 Fork
Twizhoosh is a smart Persian twitter-bot, written in Python and aimed to be easily readable and contributable.

- [walrus](http://importpython.com/click/track/e2ec92bf31342b1776bd4673ad4b2844ba26250d?source=github.com)
    - 5 Stars, 0 Fork
Lightweight Python utilities for working with Redis

- [django-descriptors](http://importpython.com/click/track/252e316b402a9e1efa23c5789a0c69bb89af82b8?source=github.com)
    - 4 Stars, 1 Fork
Demonstration of using Python Descriptors to Enhance Django Models and Fields

- [zeroless](http://importpython.com/click/track/cfd8240764b5ab5c8ac283709ee82c3ab1fa81d1?source=github.com)
    - 4 Stars, 2 Fork
Yet another ZeroMQ wrapper for Python. However, differing from pyzmq, which tries to stay very close to the C++ implementation, this project aims to make distributed systems employing 0MQ as pythonic as possible.

- [python-taipei-metro](http://importpython.com/click/track/e1506bff755aaee5a37eb9a672bca275552243ff?source=github.com)
    - 3 Stars, 0 Fork
Taipei MRT interchange route python library. Must see for our ImportPython Users from Taiwan.

- [Machine-Learning-Tasks](http://importpython.com/click/track/042f32bf164fd9d7d725e12078547caa2d291893?source=github.com)
    - 2 Stars, 0 Fork
Simple implementation of KNN Algorithm, COS Similarity, Logistic Regression in Python.

- [python-libshorttext](http://importpython.com/click/track/ba297c3890dfa0dae235c54dd1dd13f92ac8f6a8?source=github.com)
    - 4 Stars, 0 Fork
LibShortText is a high-performance classifier for short-text such as titles, questions, sentences, and short messages. This script provides a easy way to install LibShortText.

- [spotify-backup](http://importpython.com/click/track/eb422620428be6c4d2fab84d74da4a6a709e41e7?source=github.com)
    - 1 Stars, 0 Fork
A Python script that exports all of your Spotify playlists.

- [GetUserAgent](http://importpython.com/click/track/538a9f11a9a25d3ae2915cd1133c25f9a72e14ad?source=github.com)
    - 1 Stars, 0 Fork
This project give you random user agent from known user agents.

- [PyDictionary](http://importpython.com/click/track/f119f60ec5d740267a9ecfe6d25114d9b2752910?source=github.com)
    - 1 Stars, 0 Fork
PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses Google for getting meanings and translations, and thesaurus.com for getting synonyms and antonyms. 

## 曰了
~ Tweets~ Tweets


# 国货

# 是也乎
~ 参考: [为毛又一个蠎周刊?](importpython-why)


- 150103 用时 42 分钟完成快译.
- 150103 [Zoom.Quiet](http://zoomquiet.io) 用时7分钟完成格式化.
