import csv
rf="CSV\\data.csv"

fo=open(rf,'r')
data=csv.reader(fo)
header=next(data)
print(f'Header : {header}')
for i in list(data):
    print(i)