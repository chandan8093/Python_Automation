#Find all files in adirectory with extension .py/.sh/.txt and so on 
import os
req_path=input("Enter a Path : ")
if os.path.isfile(req_path):
    print("The required path {req_path} is a file please pass directory path ")
else:
    d_f=os.listdir(req_path)
    if len(d_f)==0:
        print("The fiven path {req_path} is an empty path")
    else:
        req_ex=input("Enter a require extension [.py |.txt | .md ] :  ")
        req_files=[]
        for i in d_f:
            if i.endswith(req_ex):
                req_files.append(i)
        if len(req_files)==0:
            print(f'File with extension {req_ex} does not exists')
        else:
            print(f"Required path {req_path} with extension {req_ex} consists {len(req_files)} files and files are : \n")
            print(req_files)


