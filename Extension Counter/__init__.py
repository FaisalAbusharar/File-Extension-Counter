import os
import sys

EXENSTION_FILE = ".py"  # Change it to what type of file you want to search

# to make it easier to read, i put this here to show how many files i have in Python instead of .py
EXENSTION_FILE_FULL = "Python"

# CHANGE THIS TO WHERE YOU WANT TO SEARCH IN YOUR FOLDER, IF NONE, REMOVE IT FROM HERE AND FROM THE CODE
FOLDER_TO_CHECK = "files"


dirname = "./"


def count_py_files_repos(dirname):
    if os.path.exists(os.path.join(dirname, FOLDER_TO_CHECK)):
        count = 0
        for root, dirs, files in os.walk(dirname):
            count += len([f for f in files if f.endswith(EXENSTION_FILE)])

        # Why minus one you may ask, well, if you want to count this file has one of them, remove the minus one, in the code below

        print(f"{dirname} has {count-1} {EXENSTION_FILE_FULL} Files")

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            count_py_files_repos(path)


# PUT THE DIR NAME/WHERE TO SEARCH FOR YOUR FILES
count_py_files_repos(dirname)
