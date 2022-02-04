import os
import json
import sys
sys.path.append('python')
from Interpolate import Interpolate
class CollectLimitCommand:
    def __init__(self,year,suffix):
        year=str(year)
        LimitDIR="AsymptoticLimits/"+year+"/"+suffix
        command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
        Collect="combineTool.py -M CollectLimits -i higgsCombine*.root"
        command_list.append(Collect)
        self.command= "&&".join(command_list)
        self.LimitDIR=os.getcwd()+'/'+LimitDIR
    def Set_mH(self,mH):
        self.mH=mH

    def ReadJson(self):
        myinfo={}
        myinfo_interpolate={}
        with open("limits.json","r") as handle:
            myinfo=json.load(handle)
        for _mH in myinfo:
            masslist.append(_mH)
        if len(masslist) !=2: return False
        for key in myinfo[masslist[0]]:
            keylist.append(key)
        interpolate_r=interpolate()
        for key in keylist: ##exp0,exp1,...
            m1=float(masslist[0])
            m2=float(masslist[1])
            if key in myinfo[masslist[0]]:
                r1=myinfo[masslist[0]][key]
            else:
                r1=2000.
            if key in myinfo[masslist[1]]:
                r2=myinfo[masslist[1]][key]
            else:
                r2=2000.
            r=interpolate_r.Eval(self.mH,m1,r1,m2,r2)
            myinfo_interpolate[self.mH][key]
        with open(LimitDIR+"limits_interpolate.json","w") as handle:
            json.dump(myinfo_interpolate,handle)

    def GetCommand(self):
        return self.command


