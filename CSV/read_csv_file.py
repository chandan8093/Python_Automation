#using csv module 

import csv
req_file="CSV\\data.csv"

fo=open(req_file,'r')
data=csv.reader(fo,delimiter=",")
for i in data:
    print(i)

fo.close()


#using withoput csv module 
import csv
req_file="CSV\\data.csv"

fo=open(req_file,'r')
data=fo.readlines()
for i in data:
    print(i.strip('\n').split(","))

fo.close()