import re
from fabric.api import env, run, hide, task
from envassert import detect, file, port, process, service, user
from hot.utils.test import get_artifacts

@task
def check():
  env.platform_family = detect.detect()

  assert port.is_listening(3306), 'port 3306/mysql is not listening'

  if (env.platform_family == "rhel"):
    assert process.is_up('mysql'), 'apache is not running'
  elif (env.platform_family == 'debian'):
    assert process.is_up('mysql'), ' is not running'

@task
def artifacts():
  env.platform_family = detect.detect()
  artifacts = ['/var/log/messages',
              '/var/log/syslog',
              '/var/log/cloud-init.log',
              '/var/log/cloud-init-output.log']
  get_artifacts(artifacts=artifacts)
