# [weekly.PyChina.org](http://weekly.pychina.org/)

in fact from 2003 there is CZUG.org ~ the 1st(and only one) focus Zope tech community be set up;

so years ago, there is soooooooo many python tech abt. commuity in China

but never group as one unify community brand,
like as: perl-china/ruby-china etc. 

so after PyCon2013China, some `old` Chinese Pythonista together and building:

![](PyChina_logo_131217_zq_h200.png)

## goal

- by Pythonner in China Operations
- as Pythonner in China Deleloping
- for Pythonista in Global support events organizing srvice


## organizer

- Zoom.Quiet

## path

- 基于 `gh-pages` 专用分支发布
- 所以, 本地要复制出两个仓库
    + `master` 分支进行内容撰写
    + 另外一个仓库, 切换为 `gh-pages` 分支
        * 并链接为 `output` 输出目录
        * 这样, 才可以合理使用 `fab` 指令来完成自动化本地编译和发布


## usage
How to update the site contents

main loop:

1. git clone
1. edit some .md in `content/`
1. `fab build && fab serve` for test local
1. `cd output` this is another repo. yet!
1. mark the article you have applied on GitCafe Ticket
1. git add->ci->push
1. `fab deploy` published all

### writing

- fork https://gitcafe.com/CPyUG/PyChina into local
- or becamed https://gitcafe.com/CPyUG member hold the repo. ACL
- cd into content/
- the sub-dir means:

        content/
            +- Events       首字母大写的是分类目录 收集对应文章
            +- Volunteer    ...志愿者
            +- _extra       扩展功能文件 e.g robots.txt
            +- _files       站内文件
            +- _images      站内图片
            `- pages        类似 about 的导航栏文档

#### 文章格式
- 标准 Markdown 格式
- 以 .md 为后缀
- 文件名不得使用中文/空格/符号
- 内容模板:

    Title: 中E可以混杂的标题
    Date: 2013-12-09
    Tags: people, shanghai
    Slug: sting-chen
    Author: Zoom.Quiet

- 其中:
    - `Date:` 如果没有将使用文件的系统时间
    - `Tags:` 使用逗号作间隔, 不宜过多,建议三个为界,以人物/行为/目标领域 为方向进行定义
        - 参考: [如何规划blog的标签（tag）和分类 - 心内求法 - 博客园](http://www.cnblogs.com/holbrook/archive/2012/11/05/2755268.html)
    - `Slug:` 是实际输出的页面文件名, 建议全部小写E文, 使用中划线, 不使用特殊符号


### deploy

支持本地调试! 使用 `fabric` 进行管理, 支持的命令:

    fab 
    Available commands:

        build       编译所有页面
        deploy      向主机部署所有页面
        reserve     重编译所有页面再启动本地服务
        serve       启动本地服务 localhost:8000


`注意!` 向主机部署,需要有相关权限,并在本地配置好对应 SSH 信息

### design

基于 [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) 深度定制

- 配置: `pelicanconf.py`
- 样式: `_themes/pelican-bootstrap3/`
- 插件: `_plugins/`


### 贡献

提交你的贡献到`CPyUG / weekly`，先确保自己的仓库与上游仓库同步

    # 在 Fork 的代码库中添加上游代码库的 remote 源，（操作一次就可以，以后不必每次添加）
    git remote add upstream https://gitcafe.com/CPyUG/weekly.git

    # 查看添加的上游仓库
    git remote -v

    # 提交本地修改
    git add .
    git commit -m "****"

    # 同步上游版本
    git remote update upstream
    git rebase upstream/master

    # push代码到gitcafe
    git push origin master

    # pull request
    在自己gitcafe项目仓库下提交pull request到上游仓库

 

## changelog

- 191028 ZQ 提醒本地发布环境
- 190818 ZQ ++ CNZZ WA support
- 131219 base pelican build and through qiniu.com publish

