import re
from fabric.api import env, run, hide, task
from envassert import detect, file, port, process, service, user
from hot.utils.test import get_artifacts

def verifyGalera():
  import MySQLdb
  dbConnect = MySQLdb.connect(read_default_file="~/.my.cnf")
  dbConnect.query("SHOW STATUS LIKE 'wsrep%'")
  results = dbConnect.store_result()
  resultsList = results.fetch_row(maxrows=0, how=1)

  for result in resultsList:
    if result['Variable_name'] == 'wsrep_evs_state':
      assert result['Value'] == "OPERATIONAL", 'Cluster is not ready'
    if result['Variable_name'] == 'wsrep_local_state_comment':
      assert result['Value'] == "Synced", 'Cluster is not synced'

@task
def check():
  env.platform_family = detect.detect()

  assert port.is_listening(3306), 'port 3306/mysql is not listening'

  if (env.platform_family == "rhel"):
    assert process.is_up('mysql'), 'apache is not running'
    assert service.is_enabled('mysql'), 'apache is not enabled'
  elif (env.platform_family == 'debian'):
    assert process.is_up('mysql'), ' is not running'
    assert service.is_enabled('mysql'), 'mysql is not enabled'
  verifyGalera()

@task
def artifacts():
  env.platform_family = detect.detect()
  get_artifacts()
