import os

def get_directories(root_dir: str):
    directories = []

    for entry in os.scandir(path=root_dir):
        if entry.is_dir():
            directories.append(entry.path)
    return directories
