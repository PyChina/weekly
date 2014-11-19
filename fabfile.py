import functools
import os

from fabric.api import env, lcd, local, task

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
env.deploy_path = 'output'


def cd_app_root(func):
    app_root = os.path.dirname(os.path.realpath(__file__))

    @functools.wraps(func)
    def _to_app_root(*args, **kwargs):
        with lcd(app_root):
            return func(*args, **kwargs)
    return _to_app_root


@task
@cd_app_root
def build():
    local(
        'pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env)
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
@cd_app_root
def pub2cafe():
    build()
    local(
        'cd {deploy_path} && '
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
def install_deps():
    local(
        'pip install '
        'beautifulsoup4 '
        'Markdown '
        'pelican'
    )
