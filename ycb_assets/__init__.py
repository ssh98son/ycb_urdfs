import os
from pathlib import Path


def get_data_path():
  resdir = os.path.join(os.path.dirname(__file__))
  return Path(resdir)


def get_object_names():
  dir = get_data_path()
  names = []
  for fpath in dir.glob("*.urdf"):
    # if "0" not in name:
    #   continue
    names.append(fpath.name)
  return names