Title: 蠎周刊 157: Martius
Slug: issue-157
Date: 2015-03-14 14:41
Tags: Weekly,Pycoder,Zh 


![Pycoder's Weekly](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #157): Martius](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=cf56544e52&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,


大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


## 新闻


- [Django: 功夫网!](http://djangowos.com/)

三月将继续 Py 3 的征程,
请检出 功夫网!

djangowos.com

Shared by @nathforge
 

- [Django 安全版本以及增益提案!](https://www.djangoproject.com/weblog/2015/mar/09/security-releases/)

Django 党必读!

djangoproject.com

Shared by @myusuf3
 


- [Python 发布 3.5.0a2](https://www.python.org/downloads/release/python-350a2/)

Alpha 版本第2号,
已经从 3.5.0 分支上发布.
3.4 基础上新增 矩阵乘运算符(`@`),
`%` 字节数组,等等.
细节点击进入.


python.org

Shared by @mgrouchy
 

- [EuroPython 2015: 主题召集启动](http://blog.europython.eu/post/113424757152/europython-2015-call-for-proposal-dates-available)

CFP 的 EuroPython 已经启动,
你应该抢先注册!

europython.eu

Shared by @mgrouchy
  


## 讨论

- [有哪些漂亮的 Py 脚本是你忍不住想分享的!?](http://www.reddit.com/r/Python/comments/2ysd91/what_are_some_nifty_python_snippets_that_you_have/)

reddit.com

Shared by @mgrouchy
  
(`是也乎:`
大爱好问, 值得逐一收藏下来!

最方便内置服务器:

> python3 -m http.server
> python -m SimpleHTTPServer

最方便内置 邮件 发送:

> python -m smtpd -c DebuggingServer -n

俺在哪儿:

> from os.path import expanduser
> home_dir = expanduser('~')

丫在哪儿:

    cdp () {
        cd "$(python -c "import os.path as _, ${1}; \
                print(_.dirname(_.realpath(${1}.__file__[:-1])))"
            )"
    }

    ~ $ cdp os
    /usr/lib/python2.7 $

    ~ $ cdp os.path
    /usr/lib/python2.7 $


人性化排序:

    >>> from distutils.version import StrictVersion
    >>> versions = ['1.3.12', '1.3.3', '1.2.5', '1.2.15', '1.2.3', '1.2.1']
    >>> versions.sort(key=StrictVersion)
    >>> print versions
    ['1.2.1', '1.2.3', '1.2.5', '1.2.15', '1.3.3', '1.3.12']


    >>> l = ['v1.3.12', 'v1.3.3', 'v1.2.5', 'v1.2.15', 'v1.2.3', 'v1.2.1']
    >>> l.sort(key=LooseVersion)
    >>> l
    ['v1.2.1', 'v1.2.3', 'v1.2.5', 'v1.2.15', 'v1.3.3', 'v1.3.12']



终端真数学:

    $ pmath '3 + 4'
    7
    $ pmath -f'.4f' 'pow(2000, 1/3)'
    12.5992
    $ pmath -f'.4f' 'sin(pi/2)'
    1.0000
    $ pmath -c 'exp(1j*pi).real'
    -1.0
    $ pmath 'x=3;x+2'
    5
    $ echo '3+4' | pmath
    7



最方便合成器:

> ''.join(itertools.islice(handle, lines))


最方便 实时分析:

> import pdb; pdb.set_trace()
> or in IPython:
> import ipdb; ipdb.set_trace()

...

)

## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...

## 项目

- [python-flamegraph](https://github.com/evanhempel/python-flamegraph)

能输出 FlameGraph 兼容的剖析统计数据.

github.com

Shared by @myusuf3
 
(`是也乎:`
简单的说,  Python 运行时也能用 火焰图来观察了!

![python-flamegraph](https://github.com/evanhempel/python-flamegraph/raw/master/docs/attic-create.png)

`<3`

)

- [django-api](https://github.com/bipsandbytes/django-api)

实用!
将你的 Django 接口整理在单一代码块中!

github.com

Shared by @mgrouchy
 

- [django-linguist](https://github.com/ulule/django-linguist)

专注管理 Django 模型转换的应用!

github.com

Shared by @myusuf3
 

- [pyhipku](https://github.com/lord63/pyhipku)

将任意 IP 转换为 俳句(hipku)  的包,
细节链接之内.

github.com

Shared by @mgrouchy
 

- [Wooey](https://github.com/mfitzp/wooey)


通过 web 界面自动化运行命令行脚本.

github.com

Shared by @mgrouchy



## 文章

- [通过 Docker 部署 Python 应用的建议](https://glyph.twistedmatrix.com/2015/03/docker-deploy-double-dutch.html)

针对用 Docker 来部署 Python 应用,给出了一个模板容器.

twistedmatrix.com

Shared by @myusuf3
 

- [Markowitz 投资优化组合](https://plot.ly/ipython-notebooks/markowitz-portfolio-optimization/)

为你和客户以及对 plotly 有兴趣的 IPython notebook 案例

plot.ly

Shared by @myusuf3
 

- [调试你的 Python 代码.](http://howchoo.com/g/zgi2y2iwyze/debugging-your-python-code)

对新人合理的介绍 pdb 进行调试.

howchoo.com

Shared by @myusuf3
 

-[Python 用 Numba 进行 GPU-加速的图形分析](http://devblogs.nvidia.com/parallelforall/gpu-accelerated-graph-analytics-python-numba/)

nvidia.com

Shared by @mgrouchy
 

- [治愈 "俺的工厂" 综合症](http://pythonforengineers.com/stop-the-works-on-my-machine-syndrome/)

每当你的代码只能在自个儿的机械中运行时,
那感觉总是无比苦涩的,
此文给出了一些策略,确保我们的代码是通行的.

pythonforengineers.com

Shared by @mgrouchy
 

- [用 Twilio 和手机制造语音日志](http://techstonia.github.io/twilio-voice-blog.html)

非常赞!
Twilio 加上一点点 Python 脚本,
你就拥有了一个音频博客!

github.io

Shared by @myusuf3
 

- [如何使用 Mechanical Turk 和 Boto 发布众包任务](http://scottlobdell.me/2015/03/use-mechanical-turk-python-boto-crowdsource-tasks/)

非常 COOL 的教程!
展示如何用 Django 构建应用,
在 Amazon 的 Mechanical Turk 中
组织廉价众包任务.

scottlobdell.me

Shared by @mgrouchy
 

- [来构建 web 服务吧 - 第一部分](http://ruslanspivak.com/lsbaws-part1/)

很赞的教程,
有关如何构建一个发布各种漫画的 web 服务.

ruslanspivak.com

Shared by @myusuf3
 

- [在 Python 中安装应用 monkey 补丁.](http://blog.dscpl.com.au/2015/03/safely-applying-monkey-patches-in-python.html)

嗯啍 monkey 补丁!
本文论及补丁的多种使用方式,
其中有一种是为当前应用追加监控仪表盘...

dscpl.com.au

Shared by @mgrouchy
 

- [项目 40: 协程运行多种功能](http://www.effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently/)

来及好书 `Effective Python` ,
讨论如何使用协程同时运行多个功能,
实例代码来自 Conway 的游戏人生.

effectivepython.com

Shared by @mgrouchy
 



## DAMA
(`大妈私人无责任播报`)

![PyCon Asia-Pacific 2015](http://zoomq.qiniudn.com/CPyUG/PyCon2015China/pycon-apac2015-logo.png)

- [亚太Py大会 6-5~7 在台北举行!](http://pycontw.blogspot.tw/2015/02/pycon-asia-pacific-2015-in-taiwan-save.html)

[PyCon APAC/Taiwan 2015 - Call for Proposals](https://tw.pycon.org/2015apac/en/call-for-proposals/) 议题召集已经释放,想去宝岛体验社区交流的,可以下手了!


# 是也乎

- 150316 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 150314 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
