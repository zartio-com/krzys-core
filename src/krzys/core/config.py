import os

krzys_path = os.path.expanduser('~/.krzys')
tmp_path = os.path.expanduser('~/.krzys/tmp')


def get_tmp_file(*args) -> str:
    return os.path.join(tmp_path, *args)


def file_path(*args) -> str:
    return os.path.join(krzys_path, *args)
