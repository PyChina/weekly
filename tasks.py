import functools
import os

from invoke import task
#from fabric.api import env, lcd, local, task

# Local path configuration (can be absolute or relative to fabfile)
env = {
    "input_path": 'content',
    "deploy_path": 'output',
}


@task
def build(c, debug=False, verbose=False):
    ctx = dict(env)
    ctx['debug'] = ''
    ctx['verbose'] = ''
    if debug:
        ctx['debug'] = '-D'
    if verbose:
        ctx['verbose'] = '-v'
    c.run('pelican {debug} {verbose} -o {deploy_path} {input_path}'.format(**ctx), echo=True)

@task
def serve(c, bind='0.0.0.0', port=8000, debug=False):
    ctx = dict(env)
    ctx['port'] = port
    ctx['bind'] = bind
    ctx['debug'] = ''
    if debug:
        ctx['debug'] = '-D'
    c.run(
        'pelican {debug} -l -b {bind} -p {port} {deploy_path}'.format(**ctx), echo=True)


def reserve(c):
    build(c)
    serve(c)


def gh_pages(c):
    c.run('cd {deploy_path} && '
          'pwd && '
          'git st && '
          'git add --all . && '
          'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
          # 'git pu cafe gitcafe-page '
          'git pu && '
          'date '.format(**env)
          )

@task
def pub(c):
    pull_data(c)
    build(c)
    # CNAME()
    gh_pages(c)


def pull_data(c):
    c.run(
        'cd {deploy_path} && '
        'pwd && '
        'git pull'.format(**env)
    )


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
