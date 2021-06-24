import json
mylist=[]
with open("mH_grid.json","r") as filehandle:
    mylist=json.load(filehandle)

print mylist
