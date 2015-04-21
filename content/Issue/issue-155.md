Title: 蠎周刊 155: Nimoy
Slug: issue-155
Date: 2015-03-02 08:08
Tags: Weekly,Pycoder,Zh 


![Pycoder's Weekly](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #155): Nimoy](http://us4.campaign-archive1.com/?u=9735795484d2e4c204da82a29&id=2776ce7284&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,


大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


## 新闻

- [Pytest Month 就在四月](http://pytest.org/latest/adopt.html) 

Pytest 在小伙伴们的帮助下,准备在四月正式发布了.
详细链接中, 如果你的项目需要靠谱测试组件的,应该关注了!

pytest.org

Shared by @mgrouchy
 

- [Pyston 0.3: 自举充分](http://blog.pyston.org/2015/02/24/pyston-0-3-self-hosting-sufficiency/)

Pyston 0.3 已经发布,
所有内部脚本已经完全自我驱动.
对于全新的 Python 实现, 这是一个巨大的里程碑.

pyston.org

Shared by @mgrouchy
 

- [Django 1.8 beta 1 和 1.7.5 发布!](https://www.djangoproject.com/weblog/2015/feb/25/releases/)

Django 1.8 已经指定为第二个 `长期支持`(LTS)版本.
另外,也发布了一个 1.7 的 bugfix 分支.

djangoproject.com

Shared by @myusuf3
 

- [Python 3.4.3 发布](https://www.python.org/downloads/release/python-343/)

Python 3.4.3 包含很多问题修订,
以及对 3.4.2 的小改进.
链接包含了详进的改变记录.


python.org

Shared by @mgrouchy
 



## 讨论


- [PEP 448 (追加 Unpacking Generalizations) 已为 Python 3.5 接受](http://www.reddit.com/r/Python/comments/2x8d64/pep_448_additional_unpacking_generalizations/)

reddit.com

Shared by @myusuf3
 

## 工作

- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...

## 项目

- [geocoder](https://github.com/DenisCarriere/geocoder)

geocoder 为地理编码库,
python 完成的, 简洁和一致的.

github.com

Shared by @myusuf3
 

- [argcomplete](https://github.com/kislyuk/argcomplete)

为你的 Python 脚本提供简洁,可扩展命令选项支持,
无须运用 docopt 之类.


github.com

Shared by @myusuf3
 
(`是也乎:`

可引入  IPython, 能自动完成!

    #!/usr/bin/env python
    # PYTHON_ARGCOMPLETE_OK
    import argcomplete, argparse, requests, pprint

    def github_org_members(prefix, parsed_args, **kwargs):
        resource = "https://api.github.com/orgs/{org}/members".format(org=parsed_args.organization)
        return (member['login'] for member in requests.get(resource).json() if member['login'].startswith(prefix))

    parser = argparse.ArgumentParser()
    parser.add_argument("--organization", help="GitHub organization")
    parser.add_argument("--member", help="GitHub member").completer = github_org_members

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    pprint.pprint(requests.get("https://api.github.com/users/{m}".format(m=args.member)).json())


然后就能:

    ./describe_github_user.py --organization heroku --member <TAB>

)

- [unicode_mayo](https://github.com/eyalr/unicode_mayo)


非常有用, 专注 unicode 字符串问题,
嘦在开发环境中, 对你的字符串进行包装,
就能感知是否已经失常.

github.com

Shared by @mgrouchy
 

- [compose](https://github.com/docker/compose)

Compose 是用来将应用定义/运行在 Docker 中的工具.

github.com

Shared by @myusuf3
 

- [py2deb](https://github.com/paylogic/py2deb)


Python 实现的 Debian 包含转换器.

github.com

Shared by @mgrouchy
 

- [audiogrep](https://github.com/antiboredom/audiogrep)

恰如其名, 能对音频文件内容进行关键词搜索的神奇工具.
值得体验!

github.com

Shared by @myusuf3
 

- [reinforce](https://github.com/NathanEpstein/reinforce)

`即插即用` 型学习库,
用马尔可夫决策过程的进行数据和求解最优策略推断.

github.com

Shared by @mgrouchy
 

- [django-hijack](https://github.com/arteria/django-hijack)

Django-hijack 允许超级用户劫持帐号(等若用户登录)
模拟用户操作,而不需要用户的凭据.

github.com

Shared by @myusuf3

## 文章

- [介绍一种友好的线性回归](http://www.dataschool.io/linear-regression-in-python/)

非常可爱的 IPython notebook 文书,
展现了如何舒服的折腾出线性回归情景

dataschool.io

Shared by @myusuf3
 

- [真实生活中的 Mocking](http://engineroom.trackmaven.com/blog/real-life-mocking/)

非常漂亮的示范,
如何用 mock 来绕过缓慢的 HTTP 请求.


trackmaven.com

Shared by @myusuf3
 

- [Django, Flask 和 AsyncIO 的微对比 (aiohttp.web+API-Hour)](http://blog.gmludo.eu/2015/02/macro-benchmark-with-django-flask-and-asyncio.html)

很有趣的对比,
详情链接中.
包含结论和方法.

gmludo.eu

Shared by @mgrouchy
 

- [设计客户端 Python 应用 (也适用其它语言实现)](http://pydev.blogspot.ca/2015/02/design-for-client-side-applications-in.html)

一些很好的概念和考虑,
有助于创建一个好用的客户端.

blogspot.ca

Shared by @mgrouchy
 

- [Python 打包的问题](http://blog.ionelmc.ro/2015/02/24/the-problem-with-packaging-in-python/)

对Python 中打包的系列问题思考.
也对比了各种可选方案和期待的情景.

ionelmc.ro

Shared by @mgrouchy
 
(`是也乎:`
细思恐极的事儿,
所有开放语言的相同命题:`如何才能挖一个自个儿填的了的坑?!`
)

- [现实世界的 Python 优化: NumPy, Numba, 以及 NUFFT](https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/)

由 Jake 授权发布! 
依用 Python 完成了 NUFFT(非均匀快速傅立叶变换)!
并讨论了如何进行优化.

github.io

Shared by @myusuf3


## DAMA
(`大妈私人无责任播报`)

![PyCon Asia-Pacific 2015](http://zoomq.qiniudn.com/CPyUG/PyCon2015China/pycon-apac2015-logo.png)

- [亚太Py大会 6-5~7 在台北举行!](http://pycontw.blogspot.tw/2015/02/pycon-asia-pacific-2015-in-taiwan-save.html)

[PyCon APAC/Taiwan 2015 - Call for Proposals](https://tw.pycon.org/2015apac/en/call-for-proposals/) 议题召集已经释放,想去宝岛体验社区交流的,可以下手了!

- [IPython3时代到来 - 小明明s à domicile](http://www.dongwm.com/archives/ipython3shi-dai-dao-lai/)


`WoW!`

![kernel_selector_screenshot](http://ipython.org/ipython-doc/3/_images/kernel_selector_screenshot.png)

参考:官方文档 [3.x Series — IPython 3.0.0 documentation](http://ipython.org/ipython-doc/3/whatsnew/version3.html)
 

# 是也乎

- 150302 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 150228 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
