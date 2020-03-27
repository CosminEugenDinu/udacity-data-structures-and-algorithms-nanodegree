#! /usr/bin/env python3.8

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
    suffix(str): suffix of the file name to be found
    path(str): path of the file system

    Returns:
        a list of paths
    """
    

    files = []
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            if file.endswith(suffix):
                files.append(filepath)
        else:
            rec_files = find_files(suffix, filepath)
            files.extend(rec_files)

    return files

current_dir = os.getcwd()
testdir = os.path.join(current_dir, 'testdir')

files = find_files('.c', testdir)
for file in files:
    # print(file.split('/')[-1])
    print('------------')
    print(file)


