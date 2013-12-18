#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = u'Zoom.Quiet'
SITENAME = u'蠎周刊'
SITEDESC = u'汇集全球蠎事儿 !-)'
SITENOTE = u"pycoder's weekly 中译版"

SITEURL = 'http://weekly.pychina.org'
MARKUP = ('md', )#'rst', 'html', 
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime
LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'

###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins 
PLUGINS=['_plugins.sitemap', '_plugins.gzip_cache']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 1
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget
ADDTHIS_PROFILE = True
DISQUS_SITENAME = u"{weeklypychinaorg}" #填入你的Shortname
    
#GITHUB_USER = "ZoomQuiet"
MENUITEMS = (('PyChina', 'http://pychina.org')
          ,('Zoom.Quiet', 'http://zoomquiet.org')
          )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS= None
SOCIAL = (('GitHub', 'https://github.com/PyConChina')
        , ('CPyUG', 'https://gitcafe.com/CPyUG')
        , ('News', 'http://news.pychina.org')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/CPUG')
        , ('rss', SITEURL + '/' + FEED_ALL_ATOM)
        , ('weibo', 'http://weibo.com/pyconcn')
        , ('O.B.P', 'http://weibo.com/openbookproject')
        )
# Blogroll
LINKS =  None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = u'Chaos'

TEMPLATE_PAGES = {
        "404.html": "404.html",
        }

STATIC_PATHS = ['_images', '_files'
    , '_extra/robots.txt'
    , '_extra/favicon.ico'
    ]

EXTRA_PATH_METADATA = {
    '_extra/robots.txt': {'path': 'robots.txt'},
    '_extra/favicon.ico': {'path': 'favicon.ico'}
    }

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True





