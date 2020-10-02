#!/usr/bin/env python

from os import path, listdir
from shutil import copy
from random import sample

dirpath = input(">>> Please enter your source path: ")
destDirectory = input(">>> Please enter your destination path: ")
howMany = int(input(">>> How many files do you want to select? "))

try:
    filenames = sample(listdir(dirpath), howMany)
    for fname in filenames:
        srcpath = path.join(dirpath, fname)
        copy(srcpath, destDirectory)
except IsADirectoryError as erDir:
    # currently support for directory that
    # doesn't contain another directory.
    # Open to enhancement
    print(f">>> {erDir}")
    print(">>> Your source directory must not contain directory in it")
except Exception as e:
    print(f">>> Exception: {type(e).__name__} occurred.")
