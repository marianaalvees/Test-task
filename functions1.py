import os, shutil

def syncronize(source_path, destination_path):
    # get a list of files and folders in the source
    files = os.listdir(source_path)
    #files.sort()
    # iteration through the source files
    for file in files:
            source = source_path + file
            destination = destination_path + file


            try:
                    # check the modification time
                    if os.stat(source).st_mtime < os.stat(destination).st_mtime:
                            continue
            except OSError:
                            if destination:
                                pass
                            # 
                            try:
                                shutil.copy(source, destination)
                            except FileNotFoundError as e:
                                print(f"Error: {e}. Source file '{source}' not found.")


    print('Files copied from'+ source_path +'to' + destination_path+ '!')





def copy(path_source, path_replica):
    # copy the file
    try:
        print("FROM: " + path_source + "TO: " + path_replica)
        shutil.copy(path_source, path_replica)
    except:
          print("File Exists")

def each_file(path_source, path_replica):

    # this loop will go through every folder and file
    for folder_name, subfolders, filenames in os.walk(path_source):
        print("The current folder is" + folder_name)
        # this will create the sub folders in the current folder
        for subfolder in subfolders:
            print("SUBFOLDER OF:" + folder_name + ": " + subfolder)
            try:
                # the current path of the source folder
                # is replaced with the path to the new destination
                new_path = folder_name.replace(path_source, path_replica)
                os.mkdir(new_path+"\\"+subfolder)
            except:
                  print("Folder Exists:" + subfolder)

        for filename in filenames:
            # every file is copied base on where the
            # os.walk parh function is
              
            # new_path is obtained by using the same method of subfolders
            new_path = folder_name.replace(path_source, path_replica)
            file = folder_name + "\\" + filename
            copy(file, new_path)


import os
import shutil
import urllib.request
from datetime import datetime
#from hasher import sha1
import hashlib


def move_files(filename):
    shutil.copy(filename, '/root/campbell/updates/')
    os.rename(filename, '/root/campbell/latest.pdf')

def check_for_update(source_path, replica_path):
    # get date and time as string
    now = datetime.now()
    
    # get hashes
    try:
        hash_latest = sha1(replica_path)
    except:
        move_files(source_path)
        print('First file saved')
        return
    hash_new = sha1(source_path)
    
    # compare hashes
    if hash_latest != hash_new:
        print('Found update')
        move_files(source_path)
    else:
        print('No update')
        os.remove(source_path)

#check_for_update()







import hashlib

source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"

print("-----------------------------------")



print(compare_files(source_path+"ho", replica_path+"ho"))



print("-----------------------------------")


import filecmp
print(filecmp.dircmp("C:\\Users\\maria\\Documents\\Others\\Test-task\\source", "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica").common_dirs)
source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"
#print([[folder_name, subfolders, filenames] for folder_name, subfolders, filenames in os.walk(source_path)])

def f(source_path, replica_path):
    filecmp.dircmp(source_path, replica_path).diff_files







# 1. get the paths




def copy(path_source, path_replica):
    # copy the file
    try:
        print("Copied from: " + path_source + "to: " + path_replica)
        shutil.copy(path_source, path_replica)
    except:
          print("File Exists")

def each_file(path_source, path_replica):

    # this loop will go through every folder and file
    for folder_name, subfolders, filenames in os.walk(path_source):
        print("The current folder is" + folder_name)
        # this will create the sub folders in the current folder
        for subfolder in subfolders:
            print("SUBFOLDER OF:" + folder_name + ": " + subfolder)
            try:
                # the current path of the source folder
                # is replaced with the path to the new destination
                new_path = folder_name.replace(path_source, path_replica)
                os.mkdir(new_path+"\\"+subfolder)
            except:
                  print("Folder Exists:" + subfolder)

        for filename in filenames:
            # every file is copied base on where the
            # os.walk parh function is
              
            # new_path is obtained by using the same method of subfolders
            new_path = folder_name.replace(path_source, path_replica)
            file = folder_name + "\\" + filename
            copy(file, new_path)



import os
from functions1 import copy
from filecmp import dircmp

source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"

for source_folder_path, source_subfolders, source_filenames in zip(os.walk(source_path), os.walk(source_path)):
    # this will create the sub folders in the current folder
    for subfolder in subfolders:
        if dircmp(folder_path + subfolder, )
        print("SUBFOLDER OF:" + folder_path + ": " + subfolder)
        try:
            # the current path of the source folder
            # is replaced with the path to the new destination
            new_path = folder_path.replace(source_path, replica_path)
            os.mkdir(new_path+"\\"+subfolder)
        except:
                print("Folder Exists:" + subfolder)

    for filename in filenames:
        # every file is copied base on where the
        # os.walk parh function is
            
        # new_path is obtained by using the same method of subfolders
        new_path = folder.replace(source_path, replica_path)
        file = folder + "\\" + filename
        copy(file, new_path)







def compare_files(source_file, replica_file):
    digests = []
    for file in [source_file, replica_file]:
        hasher = hashlib.md5()
        with open(file, 'rb') as f:
            content = f.read()
            hasher.update(content)
            h = hasher.hexdigest()
            digests.append(h)
            print(h)
    return digests[0] == digests[1]

def copy_dir(folder_path, destination):
    try:
        # get the name of the subdirectory through its path
        foldername = folder_path[folder_path.rindex("\\")+1:]
        shutil.copytree(folder_path, destination)
        print(f'Folder "{foldername}" and its content copied to {destination}') # Folder and its content removed
    except:
        print(f'Folder "{foldername}" not copied')


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


def match_directories(source_directory, replica_directory):
     """
     If the two directories have any common subdirectories or files, the
     one from the replica is renamed to have the same name as the one in 
     the source.     

     - maybe if they have any matching directories or files.
     This function compares directories with different names to check whether
     they correspond to a renamed version of the other. 
     Returns a list with the two matching directories if it is the case.
     Otherwise it returns an empty list. 
     """
     in_common = filecmp.dircmp(source_directory, replica_directory).common_subdirs
     
     if in_common:
          # Rename the replica directory to correspond to the source directory
          new_name = source_directory[source_directory.rindex("\\")+1:]
          new_path = replica_directory + new_name
          update_name(source_directory, new_path)
          compare_sync_directories(source_directory, new_path)
          return source_directory, replica_directory
     return None, None
          

from functools import reduce
def compare_sync_directories(source_path, replica_path):
    """ 
    This method compares directories. If there is a common directory, the
    algorithm must compare what is inside of the directory by calling this
    recursively.
    - they are mostly all reffered as directories, but can be files.
    """
    comparison = filecmp.dircmp(source_path, replica_path)
    if comparison.common_subdirs:
        for subdirs in comparison.common_dirs:
            if os.path.isdir(subdirs):
                compare_files(source_dirs + subdirs, replica_dirs + subdirs)
            compare_sync_directories(os.path.join(source_path, subdirs), os.path.join(replica_path, subdirs))

    if comparison.left_only and not comparison.right_only:
        for subdir_left in comparison.left_only:
            # It is defined as dir, but it can be a file
            if os.path.isdir(subdir_left):
                copy_dir(source_path + subdir_left, replica_path)
            else:
                shutil.copyfile(source_path + subdir_left, replica_path)

        # here should be some function to compare
        #copy(comparison.left_only, left, right)

    if not comparison.left_only and comparison.right_only:
         for subdir_right in comparison.right_only:
            if os.path.isdir(subdir_right):
                delete_dir(replica_path + subdir_right)
            else:
                 # removing the file
                 delete_file(subdir_right)
   
    if comparison.left_only and comparison.right_only:
        match = []
        source_dirs = comparison.left_only
        replica_dirs = comparison.right_only
        for source_subdir in source_dirs:
            for replica_subdir in replica_dirs:
                if ((replica_path + replica_subdir) or (source_path + source_subdir)) in match:
                     break
                folder1, folder2 = match_directories(source_subdir, replica_subdir)
                match = match.append(folder1)
                match = match.append(folder2)
         
        #copy(comparison.right_only, right, left)





    left_newer = []
    right_newer = []
    if comparison.diff_files:
        for d in comparison.diff_files:
            l_modified = os.stat(os.path.join(left, subdirs)).st_mtime
            r_modified = os.stat(os.path.join(right, subdirs)).st_mtime
            if l_modified > r_modified:
                left_newer.append(d)
            else:
                right_newer.append(d)
    copy(left_newer, left, right)
    copy(right_newer, right, left)