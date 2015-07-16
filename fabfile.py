import functools
import os

from fabric.api import env, lcd, local, task

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
env.deploy_pages = 'pages'
env.deploy_7niu = '7niu'
env.qiniu_bin = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qiniu_conf = '../7niu4pychina.json'


def cd_app_root(func):
    app_root = os.path.dirname(os.path.realpath(__file__))

    @functools.wraps(func)
    def _to_app_root(*args, **kwargs):
        with lcd(app_root):
            return func(*args, **kwargs)
    return _to_app_root

@task
@cd_app_root
def pub7niu():
    build7niu()
    local('pwd && '
        '{qiniu_bin} {qiniu_conf} && '
        'date '.format(**env)
    )
@task
@cd_app_root
def build7niu():
    local(
        'pelican {input_path} -o {deploy_7niu} -s pelicanconf.py'.format(**env)
    )

@task
@cd_app_root
def pub2cafe():
    build()
    local(
        'cd {deploy_pages} && '
        'pwd && '
        # 'git pu && '
        'git add --all . && '
        # 'git st && '
        'git ci -am "upgraded in local. @MBP111216ZQ" && '
        # 'git pu cafe gitcafe-page '
        'git pu && '
        'pwd '.format(**env)
    )
@task
@cd_app_root
def build4cafe():
    local(
        'pelican {input_path} -o {deploy_pages} -s pelicanconf.py'.format(**env)
    )

'''
@task
@cd_app_root
def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))
@task
@cd_app_root
def reserve():
    build()
    serve()
'''


@task
def install_deps():
    local(
        'pip install '
        'beautifulsoup4 '
        'Markdown '
        'pelican'
    )
