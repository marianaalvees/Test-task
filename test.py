import filecmp

source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"

comparison = filecmp.dircmp(source_path, replica_path)

#comparison.left_only = comparison.left_only - ["mu"]


import itertools
from functools import reduce
import numpy as np
import shutil
import hashlib

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


print(compare_files(source_path+"\\ha\\hu\\tu", replica_path+"\\ha\\ho"))