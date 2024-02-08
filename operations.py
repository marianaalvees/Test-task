import shutil

import os
from functions1 import copy
from filecmp import dircmp

import os
import shutil
import urllib.request
from datetime import datetime
#from hasher import sha1
import hashlib

import os, shutil
### this still lacks the operations being written into a file

def create_dir(folder_path, destination):
    try:
        # get the name of the subdirectory through its path
        foldername = folder_path[folder_path.rindex("\\")+1:]
        shutil.copytree(folder_path, destination)
        print(f'Folder "{foldername}" created and its content copied from the source to {destination}.') 
    except:
        print(f'Folder "{foldername}" not created in replica.')


def create_file(file_path, destination):
    try:
        filename = file_path[file_path.rindex("\\")+1:]
        shutil.copy(file_path, destination)
        print(f'Folder "{filename}" created and its content copied from the source to {destination}.') 
    except:
        print(f'File "{filename}" not created.')


def delete_dir(folder_path):
    try:
        # get the name of the subdirectory through its path
        foldername = folder_path[folder_path.rindex("\\")+1:]
        shutil.rmtree(folder_path)
        print(f'Folder "{foldername}" and its content removed') # Folder and its content removed
    except:
        print(f'Folder "{foldername}" not deleted')


def delete_file(file_path):
    try:
        filename = file_path[file_path.rindex("\\")+1:]
        os.remove(file_path)
        print(f'File "{filename}" removed')
    except:
        print(f'File "{filename}" not deleted')


def update_name(old_path, new_path):
    """
    Changes the name of a directory or file by changing its path. 
    """
    try:
        os.rename(old_path, new_path)

        old_name = old_path[old_path.rindex("\\")+1:]
        new_name = new_path[new_path.rindex("\\")+1:]

        print(f"{old_name} remaned to {new_name} successfully.")
    except:
         print(f"{old_name} not remaned to {new_name}.")
