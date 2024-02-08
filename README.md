# Test-task

https://www.youtube.com/watch?v=lMAT-ePTzgg

https://tonyteaches.tech/detect-file-change-python/

file and directoriy comparisons
https://docs.python.org/3/library/filecmp.html

compared subdirectories functions based on this:
https://gist.github.com/pyrochlore/b754039446ef1583c258b4053cdaf2b4


shutil
https://docs.python.org/3/library/shutil.html




-- ainda tenho de ver dos paths que ando a dar + e aditionar o file, mas pode não funcionar



import os
import shutil
import urllib.request
from datetime import datetime
from hasher import sha1
from notifier import send_notification

def move_files(filename):
    shutil.copy(filename, '/root/campbell/updates/')
    os.rename(filename, '/root/campbell/latest.pdf')

def check_for_update():
    # get date and time as string
    now = datetime.now()
    filename = '/root/campbell/{}.pdf'.format(now.strftime("%Y%d%m%H%M%S"))
    
    # download file
    url = 'https://tonyteaches.tech/test.pdf'
    urllib.request.urlretrieve(url, filename)
    
    # get hashes
    try:
        hash_latest = sha1('/root/campbell/latest.pdf')
    except:
        move_files(filename)
        print('First file saved')
        return
    hash_new = sha1(filename)
    
    # compare hashes
    if hash_latest != hash_new:
        print('Found update')
        move_files(filename)
        send_notification(url)
    else:
        print('No update')
        os.remove(filename)

check_for_update()



# hasher

import hashlib

def sha1(filename):
    BUF_SIZE = 65536  # read stuff in 64kb chunks!
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()