import json
import sys
import os
sys.path.append('python')
from Interpolate import Interpolate
def ReadJson(jsondir,mH):
    mH=float(mH)
    curdir=os.getcwd()
    os.chdir(jsondir)
    masslist=[]
    keylist=[]
    myinfo={}
    myinfo_interpolate={
        mH:{}
    }
    #print "os.getcwd()=",os.getcwd()
    with open("limits.json","r") as handle:
        myinfo=json.load(handle)
    for _mH in myinfo:
        masslist.append(_mH)
    if len(masslist) !=2: return False
    for key in myinfo[masslist[0]]:
        keylist.append(key)
    interpolate_r=Interpolate()
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
        r=interpolate_r.Eval(mH,m1,r1,m2,r2)
        myinfo_interpolate[mH][key]=r
    with open("limits_interpolate.json","w") as handle:
        json.dump(myinfo_interpolate,handle)
    os.chdir(curdir)
if __name__ == '__main__':
    mH=sys.argv[1]
    jsondir=sys.argv[2]
    ReadJson(jsondir,mH)
