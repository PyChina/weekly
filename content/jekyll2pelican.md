Title: How to from Jekyll jump into Pelican
Date: 2013-12-19 10:42
Tags: howto, pelican
Slug: jekyll-to-pelican
Author: Zoom.Quiet


[TOC]

# 如何从 Jekyll 转进入 Pelican
简述静态网站从 Jekyll 环境中迁移为 纯 Python 
[Pelican](http://getpelican.com/)...

![;](https://0.gravatar.com/avatar/0cb9d9d7e6b152d24d2b78c6464502a6?d=https%3A%2F%2Fidenticons.github.com%2Fc0b8694f59232c6681a92c4c9fec3e18.png&r=x&s=440)

## 为毛
社区在发展, 原先的 蠎周刊,为方便,使用了 gitcafe 内置的 Jekyll 服务,
所以,其实在使用 Ruby 自动编译和发布.

总是感觉不够纯粹 Pythonic ...

故而, 下决心完成迁移


# 整体

忽然发现,俺感觉很直觉的事儿,也写了文档,
但是,其它人真正首次上手全然一头雾水...

所以
[学习学习再学习 - xiaolai](http://xiaolai.github.io/alpha/on-learning/)
提出的,俺实在无法同意更多..

![Impossible_staircase](http://upload.wikimedia.org/wikipedia/commons/3/34/Impossible_staircase.svg)

这是最难的知识结构——它往往看起来跟线性结构没什么区别，但，最终令人迷惑，甚至懊恼。
用最直白的话来描述，就是：

    初级的知识需要对高级知识深入了解才能真正深入了解

——你看看这句话多拗口就多少有点概念了。

所以,还是按照 easy 模式来,
先简单的说,再往死里说折腾的技术细节...

## 已知条件

[User, Organization and Project Pages](https://help.github.com/articles/user-organization-and-project-pages)

github 的 所谓 `pages` 服务的本质:

- 云端的 Jekell 服务
- 对约定的仓库,感知变化时,就尝试进行编译
- 并自动完成发布(现在是到 github.io)

这里的约定仓库,只有两种情况:

1. 用户/组织: 
    - 比如, 注册成的用户/组织 为 https://github.com/foo
    - 则, github 尝试进行 `pages` 发布的仓库为:
    - https://github.com/foo/foo.github.io
    - 发布到:  https://foo.github.io
1. 项目
    - 任意一个项目仓库,比如, https://github.com/foo/foobar
    - 则, githuba 支持自动对此仓库的 `gh-pages` 分支进行 `pages` 编译
    - 而发布为: https://foo.github.io/foobar

## Pelican行为

[Pelican](http://getpelican.com/) 呢其实也只是
Python 世界中大堆静态网站发布工具中的一个,
为毛选中这个?
只是因为 42分钟里,大妈将其折腾起来了,
而且官方的文档/案例/样式,的确足够丰富,
给人信心...

而其本身对网站的约定非常简单:

- 配置好 `pelicanconf.py`
- 在 `content` 目录中写作
- 一键命令编译完成静态网络的生成,组织到 `output`

## 所以?方案!

基于以上的整体理解, 就可以决策怎么基于 github 的 `pages` 服务,
来进行免费的网站发布了;

目测也就两招:

1. 在用户/组织 的 `pages` 仓库中直接部署 Pelican 工程
    - 只是要在根目录部署一个自动跳转到 `output` 子目录的 `index.html` 页面
    - 以便发布后可以略过根目录来访问编译结果的内容
    - 发布成 https://foo.github.io/output
1. 用两个仓库, 将用户/组织 的 `pages` 仓库部署为 `output` 子目录
    - 这样就能自动发布为 https://foo.github.io

很明显,第二种逼格较髙,所以,就这样办了!

## 宏观流程

1. 首次建立本地撰写环境:
    1. 安装好 [Pelican](http://getpelican.com/)
    1. 分别clone 出两个仓库:
        - qpython-android.pelican 
        - qpython-android.github.io 
    1. 先在 `qpython-android.pelican` 中测试确认好 pelical 工程可用,并尝试编译
    1. 一切正确的话,将 `qpython-android.github.io` 复制覆盖为 `qpython-android.pelican/output`
1. 以后,日常的维护就再也不需要 `qpython-android.github.io` 了!
    1. 进入 `qpython-android.pelican/content` 创建/增补/修订 文章
    1. 回到 `qpython-android.pelican` 执行 `fab build`
    1. 本地到 `output` 打开对应页面检查效果
    1. 还是在 `qpython-android.pelican` 执行 `fab pub2hub` 
        - 完成对 `qpython-android.github.io` 仓库实际的 push 
        - 即, 发布成网站: http://qpython-android.github.io
    1. 最后,在 `qpython-android.pelican` 进行正常的 `git add->ci->pu`
        - 对文章源文本完成到 `qpython-android.pelican` 仓库的提交

收功!

# 细节

然后, 再分享俺的折腾过程...

## 过程
整体上,其实就三步:

1. 选择一个 theme ,完成本地 demo 整明白怎么使用 Pelican
1. 将原先 Jekyll 格式的文章声明部分文本, 批量转化为 Pelican 的
1. 改进发布流程,自动化

### theme

综合对比了官网收集的一堆样式,选择了 [DandyDev](https://github.com/DandyDev/pelican-bootstrap3) 的,根据说明,立即就完成了编译,本地检阅 ;-)

### meta

果断使用 Python 脚本,快速完成转换
[jekyll2pelican.py](https://gitcafe.com/CPyUG/weekly/blob/master/_plugins/jekyll2pelican.py)

### fab

果断使用 `fabric` 进行自动化处理!

- 参考: [fabfile.py](https://gitcafe.com/CPyUG/weekly/blob/master/fabfile.py)
- 定制了 `pub2cafe` 完成自动化发布

因为 `gitcafe` 只有用户同名-pages 服务,所以,对于当前 `蠎周刊` 的 Pelican 工程,
用两个仓库,配合完成:


    :::text
    https://github.com/qpython-android/qpython-android.pelican.git
        +- ..
        +- pelicanconf.py   主配置文件
        +- content          内容目录  
        +- output           编译输出目录
        |    `- https://github.com/qpython-android/qpython-android.github.io.git 
        |                          |
        |                          \-- 即合法的
        +- .gitignore       配置忽略 output 目录
        +- ...



这样一来,目录,就不用进入 `output` 目录进行 git 操作了
平时的发布流程就是:

1. 在 `content` 目录对应分类子目录中创建 `*.md` 文本,组织文章
1. `fab build` 完成编译,本地检阅文章效果
1. `git add . && git ci && git pu` 将增补提交
1. `fab pub2cafe` 自动完成进入 `output` 后的一系列 git 操作

对应的 配置中:

    :::ini
    #DELETE_OUTPUT_DIRECTORY = True 

就绝对不能打开注释
不然 `output` 目录清除,就没有了 `.git` 也就无法发布了...

## 坑

整个过程中,遇到没有找到文档的小麻烦,自个儿解决了的....

### DISQUS

果断遇到了 DISQUS 配置了,不生效的问题,上下折腾, 才发现很多人都遇到了这个问题,
追踪到代码:


    :::javascript
    //... pelican-themes/pelican-bootstrap3/templates/includes/comments.html
    //...
    var disqus_shortname = '{{ DISQUS_SITENAME }}'; // required: replace example with your forum shortname
    var disqus_identifier = '{{ article.slug }}';
    var disqus_url = '{{ SITEURL }}/{{ article.url }}';


才发现 `SITEURL` 的配置是决定性的,
一定要同 `DISQUS` 申请时的一致;
本地编译后, 看一眼源代码,就知道是否靠谱了...

### pages

突然发现 `content/pages` 目录中的文本,是种特殊文章,不但可以出现在导航,而且使用专用的模板,
所以,默认是没有 `DISQUS` 槽接的!

- 参考,俺的[page.html](https://gitcafe.com/CPyUG/weekly/blob/master/_themes/pelican-bootstrap3/templates/page.html) 
- 追加了仿制的: [includes/page_comments.html](https://gitcafe.com/CPyUG/weekly/blob/master/_themes/pelican-bootstrap3/templates/includes/page_comments.html)

fixed!

### CATEGORY_FEED_ATOM
一时手賎,打开了:

    
    :::ini
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'


结果,发现不能在模板里简单的完成分类子 RSS 的链接!


    :::html
        <i class="icon-th icon-large"></i>Categories</h4></li>
    {% for cat, null in categories %}
        <li class="list-group-item">
            <a href="{{ SITEURL }}/{{ cat.url }}">
                <i class="icon-folder-open icon-large"></i>{{ cat }}
            </a>
            <a href="{{ SITEURL }}/feeds/{{ cat }}.atom.xml">
                <i class="icon-rss-sign"></i>
            </a>
        </li>
    {% endfor %}


因为这儿的 `{{ cat }}` 是分类的名称,可能包含大小写字母,
而配置指导下生成的 RSS 文件是全小写的...

纠结了一会儿,也没有查到对应的文档,突然想到各种内置对象都有的 `sulg` 属性!

于是就猜对了...
参考:
[includes/sidebar.html#22](https://gitcafe.com/CPyUG/weekly/blob/master/_themes/pelican-bootstrap3/templates/includes/sidebar.html#L22)

### author

原样式作者因为是个人网站,所以,无所谓 `Author` 的信息,
但是,作为社区用共笔环境,就必须有所体现,
在 [includes / article_info.html](https://gitcafe.com/CPyUG/weekly/blob/master/_themes/pelican-bootstrap3/templates/includes/article_info.html)
先打开作者的属性输出,

然后,从别的 theme 工程中抄一个模板:
[author.html](https://gitcafe.com/CPyUG/weekly/blob/master/_themes/pelican-bootstrap3/templates/author.html)

即好!


### TOC
是的,以往 rST/t2t 时,甚至于 Word 时都有的 

    TOC ~ 章节索引

肿么可以没有?!

果断: [pelican-plugins/extract_toc at master · getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins/tree/master/extract_toc) 

只是这货竟然是依赖 `beautifulsoup4` 的! 对于非 `UNIX/Linux/MAC` 用户而言,
人艰不拆哪!!!




## 参考:

- [使用 Pelican + GitCafe Page 创建 Blog](http://riku.gitcafe.com/pelican-gitcafe.html)
- [吐槽一下DISQUS的thread链接错误问题 | Ley's blog](http://blog.imley.net/2013/01/03/disqus-thread-url-issue/#content)
- [Alex Raichev - Blog - Blohg to Pelican](http://raichev.net/blohg-to-pelican.html)

## Changelog

- 140127 ZoomQuiet 增补宏观理解
- 140120 ZoomQuiet 复制到 QPython 的 Pelican 工程
- 131219 ZoomQuiet 为 [CPyUG/weekly - GitCafe](https://gitcafe.com/CPyUG/weekly/blob/master/README.md) 创建
