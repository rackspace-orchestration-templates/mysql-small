import re
from fabric.api import env, run, hide, task
from envassert import detect, file, port, process, service, user
from hot.utils.test import get_artifacts

@task
def check():
  env.platform_family = detect.detect()

  assert port.is_listening(80), 'port 80/apache is not listening'

  if (env.platform_family == "rhel"):
    assert process.is_up('httpd'), 'apache is not running'
    assert process.is_up('php'), 'php is not running'
    assert service.is_enabled('httpd'), 'apache is not enabled'
    assert service.is_enabled('php'), 'php is not enabled'
  elif (env.platform_family == 'debian'): 
    assert process.is_up('apache2'), 'apache is not running' 
    assert process.is_up('php5'), 'php is not running'
    assert service.is_enabled('apach2e'), 'apache is not enabled'
    assert service.is_enabled('php5'), 'php is not enabled' 
  if ("secondary" not in socket.gethostname()):
    assert process.is_up('lsyncd'), 'lsyncd is not running'
    assert service.is_enabled('lsyncd'), 'lsyncd is not enabled'

@task
def artifacts():
  env.platform_family = detect.detect()
  get_artifacts()
