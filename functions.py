from filecmp import dircmp
import hashlib
from operations import * 


def compare_files(source_file:str, replica_file:str):
    """
    Compares the content of two files to check if they are identical.

    Parameters:
    -----------
    source_file : string
        Path to the file in the source for comparison.
    replica_file : string
        Path to the file in the replica for comparison.

    Returns:
    --------
    bool
        True if the content of both files is identical, False otherwise.
    """
    # Define a list to store the MD5 hashes of the content of both files
    digests = []
    # Iterate over both files
    for file in [source_file, replica_file]:
        # Initialize an MD5 hasher
        hasher = hashlib.md5()
        # Open the file in binary mode
        with open(file, 'rb') as f:
            # Read the content of the file and update the hasher
            content = f.read()
            hasher.update(content)
            # Get the hexadecimal digest of the content
            h = hasher.hexdigest()
            # Append the digest to the list
            digests.append(h)
    # Return a boolean dependent of whether the files' content are identical 
    return digests[0] == digests[1]


def match_folders(source_directory:str, replica_directory:str):
    """
    Matches folders by checking if they have any subdirectories or files in common.

    Parameters:
    -----------
    source_directory : string
        Path to the folder in the source for comparison.
    replica_directory : string
        Path to the folder in the replica for comparison.

    Returns:
    --------
    String, string
        Returns two strings, corresponding to the paths for each folder, in case they are a match.
        That, is, if they have at least one subdirectory or file name in common. Otherwise, it 
        returns two strings correponding to "None".
    """

    # store in a list the names of common subdirectories and files in the two folders
    in_common = dircmp(source_directory, replica_directory).common
    # If they have anything in common, update the replica folder to resemble the source folder
    if in_common:
          update_folder(source_directory, replica_directory)
          return source_directory, replica_directory
    # If they have nothing in common, return None
    return "None", "None"