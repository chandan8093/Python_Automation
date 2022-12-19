sfile="test.txt"
dfile="test_destination.txt"

sfo=open(sfile,"r")
data=sfo.read()
print(data)
sfo.close()

dfo=open(dfile,"w")
dfo.write(data)
dfo.close()