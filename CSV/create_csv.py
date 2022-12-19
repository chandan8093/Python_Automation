import csv
req_file="C:\\Users\\Admin\\Desktop\\Python Automation\\CSV\\demo.csv"
fo=open(req_file,'w',newline="" )
data=csv.writer(fo)

my_data=[['sno','name','age'],['1','chandan','24'],['2','Hi','25']]
data.writerows(my_data)
fo.close()