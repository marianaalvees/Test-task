##### 1. specify the arguments #####
def syncronizer(source_path, replica_path, syncronization_interval, log_file):
    pass



### 2. check the first subdirectories and files
from filecmp import dircmp
import hashlib

source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"


# list of files and subdirectories in source
in_source = dircmp(source_path, replica_path).left_list

# list of files and subdirectories in replica
in_replica = dircmp(source_path, replica_path).right_list


in_common = dircmp(source_path, replica_path).common    

extra = [in_replica - in_common]

lacking = [in_source - in_common]


def compare_in_common(source_path, replica_path):
    # list of files and subdirectories both directories have in common
    in_common = dircmp(source_path, replica_path).common
    
    # list of files in both directories
    in_common_files = dircmp(source_path, replica_path).common_files

    # if there's any files in common, check if they contain the same
    if in_common:
        non_equal_files = compare_in_common_files(source_path, replica_path, in_common_files)
    
    # list of subdirectories in both directories
    in_common_subdir = in_common - in_common_files

    # if there's any subdirectories in common, check if they contain the same

    if in_common_subdir:
        non_equal_subdir = compare_in_common_subdir(source_path, replica_path, in_common_subdir)

    # return a list with the non equal files and subdirectories
    return non_equal_files + non_equal_subdir


def compare_in_common_files(source_path, replica_path, files):
    digests = []
    equal = []
    # maybe should be somewhere folder_path

    # iterating through the files with common names in source and replica
    for file in files:
        # iterating through the paths to the common files and comparing their contents
        for file in [source_path + file, replica_path + file]:
            hasher = hashlib.md5()
            with open(file, 'rb') as f:
                content = f.read()
                hasher.update(content)
                h = hasher.hexdigest()
                digests.append(h)
                print(h)
        equal.apend(digests[0] == digests[1])
        digests = []
   
    # returning the non equal files
    return [file for boolean in equal if boolean == 0]


def compare_in_common_subdir(source_path, replica_path, subdirs):
    pass

# seperate between folders and files


def compare_diff():
    pass



##### 3. try to optimize the for loop #####



# 4. functions for writting updates, deletions, ...