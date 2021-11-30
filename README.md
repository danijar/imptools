[![PyPI](https://img.shields.io/pypi/v/imptools.svg)](https://pypi.python.org/pypi/imptools/#history) &nbsp;
[![Docs](https://readthedocs.org/projects/imptools/badge)](https://imptools.readthedocs.org)

# imptools

Tools for improving Python imports.

## Installation

```sh
pip3 install imptools
```

## Overview

[Detailed docs](https://imptools.readthedocs.io/)

### import_path

Import a module from any path on the filesystem.

```python
import imptools

my_module = imptools.import_path(
    '../path/to/my_module',  # Path to a module directory or single file.
    notfound='error',        # Raise 'error' or 'ignore' if not found.
    reload=False,            # Whether to import if already available.
)

import my_module  # Import statement also works.
```

### enable_relative

Enable relative imports for scripts that are not executed as module.

```python
import imptools

imptools.enable_relative()

# Relative imports...
```

## Tests

```
python3 -m pytest tests
```
