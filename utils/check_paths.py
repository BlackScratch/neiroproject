import os
from typing import List

def check_paths(paths: List[str]):
    for path in paths:
        if os.path.isdir(path):
            if not os.path.exists(path):
                raise FileNotFoundError(f'Directory not found: {path}')
        elif os.path.isfile(path):
            if not os.path.exists(path):
                raise FileNotFoundError(f'File not found: {path}')
        else:
            raise FileNotFoundError(f'Invalid path: {path}')