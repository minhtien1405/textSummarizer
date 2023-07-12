import os
from box.exceptions import BoxValueError # Handleing errors
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  """
  Read a yaml file and return a ConfigBox object.

  Parameters
  ----------
  path_to_yaml : Path
    Path to the yaml file.

  Returns
  -------
  ConfigBox
    A ConfigBox object."""
  try:
    with open(path_to_yaml, 'r') as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f"Read {path_to_yaml} successfully.")
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError("Read {path_to_yaml} failed")
  except Exception as e:
    raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
  """
  Create a list of directories.

  Parameters
  ----------
  path_to_directories : list
    List of directories to create.
  verbose : bool, optional
    If True, print a message. The default is True.

  Returns
  -------
  None.
  """

  for path in path_to_directories:
    os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f"Created directory {path}")

@ensure_annotations
def get_size(path:Path) -> str:
  """
  Get the size of a file.

  Parameters
  ----------
  path : Path
    Path to the file.

  Returns
  -------
  str
    The size of the file."""
  size = os.path.getsize(path)
  if size < 1024:
    return f"{size} bytes"
  elif size < 1024 * 1024:
    return f"{size / 1024:.2f} KB"
  elif size < 1024 * 1024 * 1024:
    return f"{size / 1024 / 1024:.2f} MB"
  else:
    return f"{size / 1024 / 1024 / 1024:.2f} GB"