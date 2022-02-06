import json
def Read_grid():
    with open("config/mA_grid.json","r") as handle:
        list_mA=json.load(handle)
    ##--read grid
    with open("config/tanb_grid.json","r") as handle:
        list_tanb=json.load(handle)
    ##--read grid
    with open("config/mH_grid.json","r") as handle:
        list_mH=json.load(handle)
    return list_mA,list_tanb,list_mH
