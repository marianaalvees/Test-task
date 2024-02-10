# Test-task

This repository contains a set of Python scripts for folder synchronization.

## Overview

The primary scripts included in this repository are:

- **functions.py**: Contains functions for comparing files, matching folders.
- **operations.py**: Includes operations such as creating, deleting, and updating files and directories.
- **sync.py**: Implements a synchronization algorithm to compare and sync folders.

## Scripts

### functions.py

This script contains functions for file and folder comparison:

- **compare_files**: Compares the content of two files to check if they are identical.
- **match_folders**: Matches folders by checking if they have any subdirectories or files in common.

### operations.py

This script provides operations for handling files and directories:

- **create**: Creates a folder or file in the destination based on the provided path.
- **delete**: Deletes a folder or file.
- **update_file**: Updates the contents of a file.
- **update_folder**: Updates the contents of a folder.
- **update_name**: Updates the name of a folder or file.

### sync.py

This script implements a synchronization algorithm to compare and synchronize folders:

- **compare_sync_folders**: Compares folders recursively and synchronizes their contents if they have common subdirectories or files.

## References

- [filecmp Python Library Documentation](https://docs.python.org/3/library/filecmp.html)
- [shutil Python Library Documentation](https://docs.python.org/3/library/shutil.html)
- [MD5 Hash Comparison](https://stackoverflow.com/questions/36873485/compare-md5-hashes-of-two-files-in-python)
- [Renaming a Directory in Python](https://www.geeksforgeeks.org/python-os-rename-method/)
- [Handling Paths in Python](https://www.pythoncheatsheet.org/cheatsheet/file-directory-path)
- [Logging Information to a File in Python](https://blog.enterprisedna.co/python-write-to-file/)
- [Threading in Python](https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679)

## Credits

The `compare_sync_folders` function was initially based on [this gist](https://gist.github.com/pyrochlore/b754039446ef1583c258b4053cdaf2b4).

## Additional Resources

- [YouTube Tutorial on Iterating Over Subfolders and Files](https://www.youtube.com/watch?v=lMAT-ePTzgg)
- [FreeCodeCamp Tutorial on Python File Handling](https://www.freecodecamp.org/news/python-delete-file-how-to-remove-files-and-folders/#:~:text=The%20shutil%20module%20has%20a,rmtree()%20on%20that%20variable.)

