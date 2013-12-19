from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'

env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path
# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
#env.cloudfiles_username = 'my_rackspace_username'
#env.cloudfiles_api_key = 'my_rackspace_api_key'
#env.cloudfiles_container = 'my_cloudfiles_container'

#def clean():
#    if os.path.isdir(DEPLOY_PATH):
#        local('rm -rf {deploy_path}/*'.format(**env))
#        #local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env))

#def rebuild():
#    clean()
#    build()

#def regenerate():
#    local('pelican -r -s pelicanconf.py')
#
def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

#def preview():
#    local('pelican -s publishconf.py')

#def cf_upload():
#    rebuild()
#    local('cd {deploy_path} && '
#          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#          '-U {cloudfiles_username} '
#          '-K {cloudfiles_api_key} '
#          'upload -c {cloudfiles_container} .'.format(**env))
#
#@hosts(production)
#def publish():
#    local('pelican -s publishconf.py')
#    project.rsync_project(
#        remote_dir=dest_path,
#        exclude=".DS_Store",
#        local_dir=DEPLOY_PATH.rstrip('/') + '/',
#        delete=True
#    )

# Remote server configuration
#   deploy in obp hosting
#env.hosts = ['cn.pycon.org']
#env.port = 9022
#env.user = 'pycon'
#code_dir = '/opt/www/PyChina'
#
#def deploy():
#    with cd(code_dir):
#        run('git pull')
#        run('/opt/sbin/_package_linux_amd64/qrsync -skipsym /opt/sbin/7niu4pychina.json')
