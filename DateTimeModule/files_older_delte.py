import os
import sys
from datetime import datetime
req_path=input("Enter a path")
a=3
if not os.path.exists(req_path):
    print("Please provide a valid path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide a path with directory")
    sys.exit(2)
day=datetime.now()
for i in os.listdir(req_path):
    f_d=os.path.join(req_path,i)
    if os.path.isfile(f_d):
        file_cre_date=datetime.fromtimestamp(os.path.getctime(f_d))
        diff_d=(day-file_cre_date).days
        if diff_d>3:
            print(f"{f_d}===={diff_d}")
