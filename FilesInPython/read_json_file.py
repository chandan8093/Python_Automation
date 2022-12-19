import json
fn="FilesInPython\\test.json"
fo=open(fn,"r")
#data=fo.readlines()
data=json.load(fo)
print(data)