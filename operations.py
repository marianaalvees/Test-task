import shutil
import os
from pathlib import Path

def create(to_create_path:str, destination:str, log_file:str):
    """
    Creates a folder or file in the destination that resembles the one pointed to by the path 
    in "to_create_path".

    Parameters:
    -----------
    to_create_path: string
        Path to the folder or file meant to be copied. 
    destination: string
        Path to the folder where the new directory or file is meant to be created/copied to.
    log_file: string
        Path to the file where the create operation should be logged. 
    """
    # In case the "to_create_path" leads to a directory
    if os.path.isdir(to_create_path):
        try:
            # get the name of the directory through its path
            foldername = os.path.basename(to_create_path)
            # create the new directory in the destination
            os.mkdir(os.path.join(destination, foldername))
            # copy the contents of the original directory to the destination one
            shutil.copytree(to_create_path, os.path.join(destination, foldername), dirs_exist_ok=True)
            # Log the state of the operation to the console output
            print(f"Folder '{foldername}' created and its content copied from the source to {destination}.") 
            # Log the state of the operation to the "log_file"
            log_file = open(log_file, "w")
            log_file.write(f"Folder '{foldername}' created and its content copied from the source to {destination}.")
        except:
            # Log the state of the operation to the console output
            print(f"Folder '{foldername}' not created in replica.")

    # In case of a file 
    else:
        try:
            # get the name of the file through its path
            filename = os.path.basename(to_create_path)
            # copy the original file to the destination
            shutil.copy(to_create_path, destination)
            # Log the state of the operation to the console output
            print(f"File '{filename}' created and its content copied from the source to {destination}.") 
            # Log the state of the operation to the "log_file"
            log_file = open(log_file, "w")
            log_file.write(f"File '{foldername}' created and its content copied from the source to {destination}.")
        except:
            # Log the state of the operation to the console output
            print(f'File "{filename}" not created.')




def delete(to_delete_path:str, log_file:str):
    """
    Deletes a folder or file. 

    Parameters:
    -----------
    to_delete_path: string
        Path to the folder or file meant to be deleted. 
    log_file: string
        Path to the file where the create operation should be logged. 
    """
     # In case the "to_delete_path" leads to a directory and if it is not empty
    if os.path.isdir(to_delete_path) and os.listdir(to_delete_path):
        try:
            # get the name of the directory through its path
            foldername = os.path.basename(to_delete_path)
            # delete the directory and all its content
            shutil.rmtree(to_delete_path)
            # Log the state of the operation to the console output
            print(f"Folder '{foldername}' and its content deleted") 
            # Log the state of the operation to the "log_file"
            log_file = open(log_file, "w")
            log_file.write(f"Folder '{foldername}' and its content deleted")
        except:
            # Log the state of the operation to the console output
            print(f'Folder "{foldername}" not deleted')

    # works for files and empty folders, although the variable is called 'filename'
    else:
        try:
            # get the name of the file through its path
            filename = os.path.basename(to_delete_path)
            # delete the file
            os.unlink(to_delete_path)
            # Log the state of the operation to the console output
            if os.path.isfile(to_delete_path):
                print(f"File '{filename}' deleted")
                # Log the state of the operation to the "log_file"
                log_file = open(log_file, "w")
                log_file.write(f"File '{filename}' deleted")
            else:
                print(f"Folder '{foldername}' deleted") 
                # Log the state of the operation to the "log_file"
                log_file = open(log_file, "w")
                log_file.write(f"Folder '{foldername}' deleted")
        
        except:
            if os.path.isfile(to_delete_path):
                # Log the state of the operation to the console output
                print(f"File '{filename}' not deleted.")
            else:
                print(f"Folder '{filename}' not deleted.")


def update_file(original_file_path:str, to_update_path:str, log_file:str):
    """
    Updates the contents of a file. 

    Parameters:
    -----------
    original_file_path: string
        Path to the file whose contents will be used to update a given file.
    to_update_path: string
        Path to the file meant to be updated. 
    log_file: string
        Path to the file where the create operation should be logged. 
    """
    try:
        # get the name of the file through its path
        filename = os.path.basename(to_update_path)
        # copy content of the original file to 'to_update_path'
        shutil.copy(original_file_path, to_update_path)
        # Log the state of the operation to the console output
        print(f"File '{filename}' updated.")
        # Log the state of the operation to the "log_file"
        log_file = open(log_file, "w")
        log_file.write(f"File {filename} updated.")
    except:
         # Log the state of the operation to the console output
         print(f"File {filename} not updated.")



def update_folder(original_folder_path:str, to_update_path:str, log_file:str):
    """
    Updates the contents of a folder. 

    Parameters:
    -----------
    original_file_path: string
        Path to the file whose contents will be used to update a given file.
    to_update_path: string
        Path to the file meant to be updated. 
    log_file: string
        Path to the file where the create operation should be logged. 
    """
    try:

        foldername = os.path.basename(to_update_path)
        # Update the name of the folder in 'to_update_path' to resemble the one in 'folder_path'
        update_name(original_folder_path, to_update_path)
        # copy contents of the original folder to "to_update_path"
        shutil.copytree(original_folder_path, to_update_path, dirs_exist_ok=True)
        # Log the state of the operation to the console output
        print(f"{foldername} updated.")
        # Log the state of the operation to the "log_file"
        log_file = open(log_file, "w")
        log_file.write(f"{foldername} updated.")
    except:
         # Log the state of the operation to the console output
         print(f"{foldername} not updated.")


def update_name(source_path:str, replica_path:str, log_file:str):
    """
    Updates the name of a folder or file. 

    Parameters:
    -----------
    source_path: string
        Path to the folder or file in the source. 
    to_update_path: string
        Path to the folder or file in the replica whose name is meant to be updated. 
    log_file: string
        Path to the file where the create operation should be logged. 
    """
    try:
        # get the name that is being changed, "old_name", and the one replacing it, "new_name"
        old_name = os.path.basename(replica_path)
        new_name = os.path.basename(source_path)
        # get the path to the folder containing the respective file in the replica
        path = Path(replica_path).parent
        # change the name of the file
        os.rename(replica_path, os.path.join(path, new_name))
        # Log the state of the operation to the console output
        print(f"{old_name} remaned to {new_name}.")
        # Log the state of the operation to the "log_file"
        log_file = open(log_file, "w")
        log_file.write(f"{old_name} remaned to {new_name}.")
    except:
         # Log the state of the operation to the console output
         print(f"{old_name} not remaned to {new_name}.")


