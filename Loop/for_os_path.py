#Loop for listing the directory and files from path
import os
import sys
path=input("Enter a path to be serach a directory/file : ")
if os.path.exists(path):
    dir_x=os.listdir(path)
    
else:
    print("path not exist")
    sys.exit()

print(f"ALL DIR AND FILE : {dir_x}\n\n")
for i in dir_x:
    f_d=os.path.join(path,i)
    if os.path.isfile(f_d):
        print(f'Files\n: {f_d}')
    else:
        print(f'Directory\n: {f_d}')