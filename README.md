[![PyPI](https://img.shields.io/pypi/v/imptools.svg)](https://pypi.python.org/pypi/imptools/#history)

# imptools

Tools for improving Python imports.

## Installation

```sh
pip3 install imptools
```

## Docs

### `import_path()`

Import a module from any path on the filesystem.

Usually, this would be achieved by adding the parent directory of the module to
`sys.path` or the `PYTHONPATH` environment variable and then importing it
normally. However, this pollutes Python's import path, which can lead to
accidentally importing the wrong modules. The function `import_path()` avoids
this problem by importing a package from a path on the filesystem without
modifying the Python import path.

The module can be either a directory containing `__init__.py` or a single file.

Relative paths are resolved relative to the directory of the source file that
calls `import_path()`.

```python
import imptools

my_module = imptools.import_path(
    '../path/to/my_module',  # Path to a module directory or single file.
    notfound='error',        # Raise 'error' or 'ignore' if not found.
    reload=False,            # Whether to import if already available.
)

import my_module  # Import statement also works.
```

### `enable_relative()`

Enable relative imports for scripts that are not executed as module.

Usually, scripts that are part of a module and use relative imports must be run
as `python3 -m module.script`. However, this requires being in the correct
working directory and can be annoying. The `enable_relative()` function allows
to execute those scripts normally as `python3 script.py`.

Since PEP 366, this can be achieved by setting the `__package__` variable in
the script and importing the package or making it available on the Pyhton
import path. The `enable_relative()` function hides this behind a simple
function that can be imported and called inside the script, before any relative
imports.

```python
import imptools

imptools.enable_relative()

# Relative imports...
```

## Tests

```
python3 -m pytest tests
```
