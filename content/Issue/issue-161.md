Title: 蠎周刊 161: PYCON 2015
Slug: issue-161
Date: 2015-04-11 17:17
Tags: Weekly,Pycoder,Zh 


![Pycoder's Weekly](https://gallery.mailchimp.com/9735795484d2e4c204da82a29/images/Image_202014_01_22_20at_2010.45.04_20AM9789bf.png)


- 原文: [Pycoder's Weekly (Issue #161): PYCON 2015](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=8f8d4bc674&e=889f3f6a05)

##  搜罗Py万物 的周刊

亲,

Mahdi is at PYCON 2015 in Montreal! Say hi if you see him! Now on to the newsletter


大家多分享[文章](http://pycoders.com/submissions/) 
俺们才折腾的出又一周的美好呢.

喜欢就
在 [Gratipay](https://www.gratipay.com/PycodersWeekly)
支持俺们吧!
当然的,俺们也在[twitter](http://www.twitter.com/pycoders)


## 新闻

- [PyCon APAC/Taiwan 2015](https://tw.pycon.org/2015apac/en/registration/)

早鸟注册已经开放, 只到本月 21 号.

pycon.org

Shared by @mgrouchy
 
- [PyCon 2015 Videos](https://www.youtube.com/channel/UCgxzjK6GuOHVKR_08TT4hJQ)

实时发布哪...

youtube.com

Shared by @mgrouchy
 
- [DjangoCon US 2015 议题召唤](https://www.djangoproject.com/weblog/2015/apr/02/djangocon-us-2015-call-for-proposals/)

是时间提交你的议题了.

djangoproject.com

Shared by @mgrouchy
 
- [发布 PyMongo 3](http://emptysqua.re/blog/announcing-pymongo-3/)

PyMongo 3 已发布,
细节链接中.

emptysqua.re

Shared by @mgrouchy



## 讨论


- [Python 在 GIS](http://www.reddit.com/r/Python/comments/31znqr/python_in_gis/)

reddit.com

Shared by @myusuf3
 
- [有关 hack 和安全的 Py 图书](http://www.reddit.com/r/Python/comments/31q3x0/books_on_hacking_and_security_using_python/)

reddit.com

Shared by @mgrouchy
 




## 工作


- [猎豹深圳团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmSzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) 
四月急招 N 名有服务端开发经验的 **gopher**!


- [猎豹广州团队急召](https://github.com/cheetahmobile/CMBM/wiki/BmGzHr)

来自 [猎豹移动 - 全球最大的移动工具开发商](http://www.cmcm.com/zh-cn/cm-backup/) ...
四月急招 5+ 名有服务端开发经验的 **Pythonista/gopher**!


## 项目


- [barf-project](https://github.com/programa-stic/barf-project)

多平台开源二进制分析和逆向工程框架.

github.com

Shared by @mgrouchy
 
- [boltons](https://github.com/mahmoud/boltons)

Boltons是拥有超过100个BSD许可的纯Python实用工具集合,
[文档在此](https://boltons.readthedocs.org/en/latest/)

github.com

Shared by @mgrouchy

(`是也乎:`
细思恐极哪,,,
pip 不招人待见的事儿太多了,,
)

 
- [serpy](https://github.com/clarkduvall/serpy)

能对类似 Django 模块/自定类 等 复杂数据类型进行高速序列化.


github.com

Shared by @mgrouchy
 
- [NCutil](https://github.com/jacobsalmela/NCutil)

非常赞的, 支持 Mavericks 和 Yosemite ,
针对 OSX 提醒中心,
允许 追加/删除应用也支持 app store 的提醒接入.

github.com

Shared by @mgrouchy
 
- [soupy](https://github.com/ChrisBeaumont/soupy)

对 BeautifulSoup 的完整包装,
支持对 web 数据构建复杂的查询.

github.com

Shared by @mgrouchy

(`是也乎:`

```
from soupy import Soupy, Q

html = """
<div id="main">
  <div>The web is messy</div>
  and full of traps
  <div>but Soupy loves you</div>
</div>"""

print(Soupy(html).find(id='main').children
      .each(Q.text.strip()) # extract text from each node, trim whitespace
      .filter(len)          # remove empty strings
      .val())               # dump out of Soupy

# ['The web is messy', 'and full of traps', 'but Soupy loves you']
```

果断 jQ 样哪...

)

- [nameko](https://github.com/onefinestay/nameko)

又一个微服务构建框架.

github.com

Shared by @myusuf3
 
- [guardrail](https://github.com/jmcarp/guardrail)

对象级权限管理库,
和db 无关,可独立使用的.

github.com

Shared by @myusuf3


## 文章

- [Nameko for Microservices](http://lucumr.pocoo.org/2015/4/8/microservices-with-nameko/)

Nameko(滑菇) 的详细介绍,
支持用户快速构建微服务,
专注业务逻辑,
将各种协议细节都给简化了.

pocoo.org

Shared by @mgrouchy
 
(`是也乎:`

![Nameko](http://img3.douban.com/lpic/s24587198.jpg)

小而美味;
支持 AMQP 上的 RPC;
内置测试框架...

强化的 bottle,好象
)


- [Py 应用的自动补丁.](http://blog.dscpl.com.au/2015/04/automatic-patching-of-python.html)

对 猴式 补丁的最后一篇讨论

dscpl.com.au

Shared by @myusuf3
 
- [Numba vs Cython: 如何选择](http://eng.climate.com/2015/04/09/numba-vs-cython-how-to-choose/)

用 Python 进行数学处理时,
如何在 Numba 和 Cython 之间选择?!
作者给出了一些建议.

climate.com

Shared by @mgrouchy
 
- [vim-yapf](https://github.com/mindriot101/vim-yapf#why-you-may-not-need-this-plugin)

为 vim 准备的 yapf Python 格式化

github.com

Shared by @mgrouchy
 
- [Classy CBV](http://ccbv.co.uk/)


Django Class Based Views 相关资源和迷失的文档

ccbv.co.uk

Shared by @mgrouchy
 
- [实例体验 Py3 的 Asyncio](http://www.giantflyingsaucer.com/blog/?p=5557)

如果对 Py3 中的 Asyncio 开发有兴趣,
此篇大善.

giantflyingsaucer.com

Shared by @mgrouchy
 
- [构建 Web 服务: 第二部分.](http://ruslanspivak.com/lsbaws-part2/)

Ruslan 重启这一系列,
此篇包含了精美插图.

ruslanspivak.com

Shared by @myusuf3
 
- [Python 中的随机过程](http://www.stuartreid.co.za/random-walks-down-wall-street-stochastic-processes-in-python/)

使用 Quants 处理随机过程的好文章.

stuartreid.co.za

Shared by @myusuf3
 




## DAMA
(`大妈私人无责任播报`)



# 是也乎

- 150411 [Zoom.Quiet](http://zoomquiet.org/) 用时 42 分钟 完成快译.
- 150411 [Zoom.Quiet](http://zoomquiet.org/) 用时 7 分钟 完成格式转抄.

    
 
