import os

tmp_path = os.path.expanduser('~/.krzys/tmp')


def get_tmp_file(*args) -> str:
    return os.path.join(tmp_path, *args)
