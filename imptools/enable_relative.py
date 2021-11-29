import imptools


def enable_relative():
  """
  Enable relative imports for scripts that are not executed as module.

  Usually, scripts that are part of a module and use relative imports must be
  run as `python3 -m module.script`. However, this requires being in the
  correct working directory and can be annoying. The `enable_relative()`
  function allows to execute those scripts normally as `python3 script.py`.

  Since PEP 366, this can be achieved by setting the `__package__` variable in
  the script and importing the package or making it available on the Pyhton
  import path. The `enable_relative()` function hides this behind a simple
  function that can be imported and called inside the script, before any
  relative imports.

  Example:

  ```
  import imptools

  imptools.enable_relative()

  # Relative imports...
  ```

  Raises:

    ModuleNotFoundError: If the parent directory of the script that calls this
      function is not a module.
  """
  import pathlib
  import __main__

  # Skip if the script is executed as a module.
  if __main__.__package__ is not None:
    return

  # Skip if running from interactive interpreter.
  if not hasattr(__main__, '__file__'):
    return

  # Assume the module is simply the parent directory.
  root = pathlib.Path(__main__.__file__).parent

  # Import the module without polluting the Python import path.
  imptools.import_path(root)

  # Set the package variable so Python can resolve relative imports.
  __main__.__package__ = root.name
