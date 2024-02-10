import os
import threading
from functions import *
from filecmp import dircmp
from operations import update_file, update_name, create, delete


def compare_sync_folders(source_path:str, replica_path:str, synchronization_interval:float, log_file:str):
    """ 
    This function compares a source folders and replica folders. It creates, deletes and updates subfolders
    and files in the replica to sync it with the source, periodically.  
    
    Parameters:
    -----------
    source_path: string
        The path of the folder in the source. 
    replica_path: string
        The path of the folder in the replica.
    syncronization_interval: 
        Defines the period in seconds between two syncronizations. 
    log_file:
        Path to the file where the create operation should be logged. 
    """
    # compare the folders in the source and replica
    comparison = dircmp(source_path, replica_path)

    # define an empty list to keep in check of which subdirectories and files have been handled
    # among the ones not in common
    handled = []
    
        
    # If the source contains extra (not in common) files or subdirectories and the replica does not
    if comparison.left_only and not comparison.right_only:
        for subdir_left in comparison.left_only:
            # Create the subdirectory or file in the replica
            create(os.path.join(source_path, subdir_left), replica_path, log_file)
            handled = handled + [os.path.join(source_path, subdir_left)]


    # If the replica contains extra (not in common) files or subdirectories and the source does not
    if not comparison.left_only and comparison.right_only:
        for subdir_right in comparison.right_only:
            # Delete the subdirectory or file in the replica
            delete(os.path.join(replica_path, subdir_right), log_file)
            handled = handled + [os.path.join(replica_path, subdir_right)]

    # define a list which will store matching files or directories
    match = [] 

    # If there is both extra files or subdirectories in the source and replica
    if comparison.left_only and comparison.right_only:
        # list with names of the extra files and subdirectories in the source
        source_dirs = comparison.left_only
        # list with the names of the extra files and subdirectories in the replica
        replica_dirs = comparison.right_only
        # Iterate through the extra files and directories to compare them
        for source_subdir in source_dirs:
            for replica_subdir in replica_dirs:
                # defines strings with the path to each subdirectory or file
                src_subdir_path = os.path.join(source_path, source_subdir)
                rpl_subdir_path = os.path.join(replica_path, replica_subdir)
                # In case any subdirectory or file is included in the match list,
                # do not consider it for any further matching
                if (rpl_subdir_path or src_subdir_path) in match:
                     break
                # In case both source_subdir and replica_subdir are subdirectories, check if they have anything in common
                if os.path.isdir(rpl_subdir_path) and os.path.isdir(src_subdir_path):
                    folder1, folder2 = match_folders(src_subdir_path, rpl_subdir_path)
                    # append the matching subdiretories to the 'match' list
                    match = match + [folder1, folder2]
                # In case they are both files, check if they have the same content, and if not, update the replica one
                if os.path.isfile(rpl_subdir_path) and os.path.isfile(src_subdir_path):
                    if compare_files(src_subdir_path, rpl_subdir_path):
                        update_name(src_subdir_path, rpl_subdir_path, log_file)
                        update_file(src_subdir_path, os.path.join(replica_path, source_subdir), log_file)
                        # append the matching files to the 'match' list
                        match = match + [src_subdir_path, rpl_subdir_path]


    # if the two folderS have any sub directories or files in common
    if comparison.common:
        for subdir in comparison.common:
            # define the path of each subdirectory or file (in the source and replica, respectively)
            src_subdir_path = os.path.join(source_path, subdir)
            rpl_subdir_path = os.path.join(replica_path, subdir)
            # check if they are both files
            if os.path.isfile(src_subdir_path) and os.path.isfile(rpl_subdir_path):
                # check if the files in soure and replica are the same, and if not, update the replica one
                if not compare_files(src_subdir_path, rpl_subdir_path):
                    update_file(src_subdir_path, rpl_subdir_path, log_file)
                handled = handled + [src_subdir_path, rpl_subdir_path]
            # check if they are both directories
            if os.path.isdir(src_subdir_path) and os.path.isdir(rpl_subdir_path):
                compare_sync_folders(src_subdir_path, rpl_subdir_path, synchronization_interval = synchronization_interval, log_file = log_file)
                handled = handled + [src_subdir_path, rpl_subdir_path]

    # define a list of the paths of the extra files and subdirectories
    left_comparison =  [os.path.join(source_path, left_folder) for left_folder in comparison.left_only] 
    right_comparison =  [os.path.join(replica_path, right_folder) for right_folder in comparison.right_only]
    extra = left_comparison + right_comparison
    # define a list containing the subdirectories and files that still need to be handled
    not_handled = list(set(extra) - set(match) - set(handled))
    # while the list with subdirectories and files to be handled is not empty, handle them
    for subdir in not_handled:
        # If it is a subdirectory or file belonging to the source, create it in the replica
        if subdir in left_comparison:
            create(subdir, replica_path, log_file)
        # If it is a subdirectory or file belonging to the replica, delete it
        else:
            delete(subdir, log_file)


    # Set this function to be executed again in 'syncronization_interval' seconds
    threading.Timer(synchronization_interval, compare_sync_folders, args=(source_path, replica_path, synchronization_interval, log_file)).start()

