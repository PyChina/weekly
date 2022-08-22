__version__ = 'v.210526.1158'
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2021-05'

import functools
import os

from invoke import task
#from fabric.api import env, lcd, local, task

# Local path configuration (can be absolute or relative to fabfile)
env = {"input_path" : 'content'
    , "deploy_path" : 'output'
    }

SROOT = os.path.dirname(os.path.abspath(__file__))
print(SROOT)


@task
def ver(c):
    '''echo crt. verions
    '''
    print('\n ~> powded by {} <~'.format(__version__))

#   support stuff func.
def cd(c, path2, echo=True):
    os.chdir(path2)
    if echo:
        print('\n\t crt. PATH ===')
        c.run('pwd')
        c.run('echo \n')


@task
def build(c):
    print("\t>>> base Pelican build-out html")
    c.run('pelican {input_path} -o {deploy_path} -s pelicanconf.py --debug'.format(**env))


def serve(c):
    c.run('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))


@task
def reserve(c):
    build(c)
    serve(c)

def gh_up(c):
    print("\t>>> git pu all .md update")
    c.run('pwd && '
        'git st && '
        'git add --all . && '
        'git ci -am "push all new words for markdoc build" && '
        # 'git pu cafe gitcafe-page '
        'git pu && '
        'date '.format(**env)
        )


def gh_pages(c):
    print("\t>>> jump-into gh-pages to publish results")
    #print(env['deploy_path'])
    cd(c, env['deploy_path'])
    c.run('git st && '
        'git add --all . && '
        'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
        # 'git pu cafe gitcafe-page '
        'git pu && '
        'date '.format(**env)
        )
    cd(c, SROOT)

def pull_data(c):
    #cd(c, env['deploy_path'])
    print("\t>>> git pull all others doc.")
    c.run('git pull'.format(**env)
    )
    cd(c, SROOT)


@task
def pub(c):
    pull_data(c)
    build(c)
    gh_up(c)
    # CNAME()
    gh_pages(c)




'''
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
    build4cafe()
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

@task
@cd_app_root
def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))
@task
@cd_app_root
def reserve():
    build()
    serve()

@task
def install_deps():
    local(
        'pip install '
        'beautifulsoup4 '
        'Markdown '
        'pelican'
    )
'''
