#Read a path and check if a given path is a file or directory

import os
path=input("Enter a path to be serched : ")
if os.path.exists(path):
    if os.path.isfile(path):
        print(f'The given {path} is a file')
    else:
        print(f'The given {path} is a directory')
else:
    print("not a valid path")
    