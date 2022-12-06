x=[1,2,3,'chandan','x',9]
for i in x:
    print(i)
    if i==3:
        print("got it")
        break
print("Break Executed")
cnt=1
while True:
    print(cnt)
    if cnt==100:
        break
    cnt=cnt+1


for i in range(1,11):
    #print(i)
    if i==4:
        continue
        print("ji conti")
    print(i)


for i in range(5):
    pass