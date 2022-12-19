import json

req_file="FilesInPython\python_file.json"
data={"Name":"Chandan","Skills":"Devops","Platform":["AWS","GCP","AZURE"]}
fo=open(req_file,"w")
json.dump(data,fo,indent=4)

fo.close()