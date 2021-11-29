import pathlib
import sys

import imptools
import pytest


def test_absolute_path():
  sys.modules.pop('directory_module', None)
  with pytest.raises(ImportError):
    import directory_module
  path = pathlib.Path(__file__).parent.parent / 'directory_module'
  imptools.import_path(path)
  import directory_module  # noqa
  assert directory_module.hello() == 'Directory Module!'


def test_directory_module():
  sys.modules.pop('directory_module', None)
  with pytest.raises(ImportError):
    import directory_module
  imptools.import_path('../directory_module')
  import directory_module  # noqa
  assert directory_module.hello() == 'Directory Module!'


def test_single_file_module():
  sys.modules.pop('single_file_module', None)
  with pytest.raises(ImportError):
    import single_file_module
  imptools.import_path('../single_file_module')
  import single_file_module  # noqa
  assert single_file_module.hello() == 'Single File Module!'


def test_sibling_sub_module():
  sys.modules.pop('sub_module', None)
  with pytest.raises(ImportError):
    import sub_module
  imptools.import_path('sibling/sub_module')
  import sub_module  # noqa
  assert sub_module.hello() == 'Sibling Sub Module!'


def test_name():
  sys.modules.pop('directory_module', None)
  with pytest.raises(ImportError):
    imptools.import_path('../directory_module', name='different_name')
  imptools.import_path('../directory_module', name='directory_module')
  import directory_module  # noqa
  assert directory_module.hello() == 'Directory Module!'


def test_reload():
  sys.modules.pop('directory_module', None)
  imptools.import_path('../directory_module')
  imptools.import_path('wrong/path', name='directory_module')
  with pytest.raises(ImportError):
    imptools.import_path('wrong/path', reload=True)


def test_notfound():
  sys.modules.pop('directory_module', None)
  with pytest.raises(ImportError):
    imptools.import_path('wrong/path')
  with pytest.raises(ImportError):
    imptools.import_path('../directory_module', name='wrong_name')
  imptools.import_path('wrong/path', notfound='ignore')
  imptools.import_path('../directory_module', 'wrong_name', notfound='ignore')
