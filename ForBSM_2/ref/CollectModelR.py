import json
import os
import sys
def CollectR(year,model,list_mA,list_tanb):
    #../AsymptoticLimits/2016/mh125_13_withVBF/mA_mA_110_tanb_1.5
    result={}
    for mA in list_mA :
        print "<mA=",mA,">"
        result[mA]={}
        for tanb in list_tanb:
            print "<tanb=",tanb,">"
            result[mA][tanb]={}
            #result[mA][tanb]
            temp_result={}
            input_json="../AsymptoticLimits/"+str(year)+"/"+model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb)+"/limits_interpolate.json"
            if not os.path.isfile(input_json):
                print "Not found->",input_json
                continue
            with open(input_json,"r") as handle:
                temp_result=json.load(handle)
                
                mHlist=[]

                for mH in temp_result:
                    mHlist.append(mH)
                mH=mHlist[0]

                keylist=[]##exp0 exp-1
                for key in temp_result[mH]:
                    _r=temp_result[mH][key]
                    
                    result[mA][tanb][key]=_r
    return result

    

if __name__ == '__main__':
    year=sys.argv[1]
    model=sys.argv[2]
    list_mA=[]
    list_tanb=[]
    list_mH=[]
    ##--read grid
    with open("config/mA_grid.json","r") as handle:
        list_mA=json.load(handle)
    ##--read grid
    with open("config/tanb_grid.json","r") as handle:
        list_tanb=json.load(handle)
        
    #year=2016
    #model="mh125_13_withVBF"
    model=model.rstrip('.root')
    result=CollectR(year,model,list_mA,list_tanb)

    ##--save result
    exportdir="Limits/"+model
    os.system("mkdir -p "+exportdir)
    with open(exportdir+"/"+str(year)+".json","w") as handle:
        json.dump(result,handle)
    
