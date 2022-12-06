# loops for list,tuples,dictonieries,sring
# strign loop
'''
s="Chandan Gupta"
print(s)
print("\n".join(s))
for i in s:
    print(i)
'''

#tuple
t=[(1,2),(3,4),(5,6)]
for i,j in t:
    print(j)

#dictoneries
print("Dictoneries Ahead : \n")
dic={'fruit':'apple','book':'msd',"language":'python'}

for key,value in dic.items(): #dic.keys,dic.values,dic.items
    print(key,value)