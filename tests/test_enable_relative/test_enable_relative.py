import pathlib
import subprocess
import sys


def test_run_good_as_module():
  code, stdout, stderr = sh(
      f'{sys.executable} -m test_enable_relative.good_script')
  assert code == 0
  assert stdout == 'Helper!'
  assert stderr == ''


def test_run_bad_as_module():
  code, stdout, stderr = sh(
      f'{sys.executable} -m test_enable_relative.bad_script')
  assert code == 0
  assert stdout == 'Helper!'
  assert stderr == ''


def test_run_good_as_script():
  code, stdout, stderr = sh(
      f'{sys.executable} test_enable_relative/good_script.py')
  print(stderr)
  assert code == 0
  assert stdout == 'Helper!'
  assert stderr == ''


def test_run_bad_as_script():
  code, stdout, stderr = sh(
      f'{sys.executable} test_enable_relative/bad_script.py')
  assert code == 1
  assert stdout == ''
  assert 'ImportError' in stderr
  message = 'attempted relative import with no known parent package'
  assert message in stderr


def sh(command):
  repo = pathlib.Path(__file__).parent.parent.parent
  process = subprocess.run(
      command,
      cwd=str(repo / 'tests'),
      shell=True,
      check=False,
      env={'PYTHONPATH': str(repo)},
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
  )
  stdout = process.stdout.decode().strip()
  stderr = process.stderr.decode().strip()
  code = process.returncode
  return code, stdout, stderr
