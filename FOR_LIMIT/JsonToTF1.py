import ROOT
import json
from array import array
import sys
##---1st, read json file
#
#myinput="AsymptoticLimits/2016/all/floating/indep.json"
myinput=sys.argv[1]
print myinput
data_in_float={}
with open(myinput) as f:
    data = json.load(f)
    
    #print data
    #xlist=[] ##mass
    #exp0list=[] ##exp0
    #exp_p1list=[] ##exp_p1
    #exp_p2list=[] ##exp_p2
    #exp_m1list=[] ##exp_m1
    #exp_m2list=[] ##exp_m2

    xlist=array('d')
    exp0list=array('d')
    exp_p1list=array('d')
    exp_p2list=array('d')
    exp_m1list=array('d')
    exp_m2list=array('d')

    for mass in data:
        if not 'exp0' in data[mass] : continue

        exp0=float(data[mass]['exp0'])
        exp_p1=float(data[mass]['exp+1'])
        exp_p2=float(data[mass]['exp+2'])
        exp_m1=float(data[mass]['exp-1'])
        exp_m2=float(data[mass]['exp-2'])
        mass=float(mass)

        data_in_float[mass]={}
        data_in_float[mass]['exp0']=exp0
        data_in_float[mass]['exp_p1']=exp_p1
        data_in_float[mass]['exp_p2']=exp_p2
        data_in_float[mass]['exp_m1']=exp_m1
        data_in_float[mass]['exp_m2']=exp_m2

    for mass in sorted(data_in_float):
        if mass < 160:continue
        exp0=float(data_in_float[mass]['exp0'])
        exp_p1=float(data_in_float[mass]['exp_p1'])
        exp_p2=float(data_in_float[mass]['exp_p2'])
        exp_m1=float(data_in_float[mass]['exp_m1'])
        exp_m2=float(data_in_float[mass]['exp_m2'])

        xlist.append(float(mass))
        exp0list.append(float(exp0))
        exp_p1list.append(float(exp_p1))
        exp_p2list.append(float(exp_p2))
        exp_m1list.append(float(exp_m1))
        exp_m2list.append(float(exp_m2))

    

#print data_in_float
#print xlist
#print exp0list
TGraph_exp0=ROOT.TGraph(len(exp0list),xlist,exp0list)
TGraph_exp0.SetName("TGraph_exp0")
TGraph_exp_p1=ROOT.TGraph(len(exp_p1list),xlist,exp_p1list)
TGraph_exp_p1.SetName("TGraph_exp_p1")
TGraph_exp_p2=ROOT.TGraph(len(exp_p2list),xlist,exp_p2list)
TGraph_exp_p2.SetName("TGraph_exp_p2")
TGraph_exp_m1=ROOT.TGraph(len(exp_m1list),xlist,exp_m1list)
TGraph_exp_m1.SetName("TGraph_exp_m1")
TGraph_exp_m2=ROOT.TGraph(len(exp_m2list),xlist,exp_m2list)
TGraph_exp_m2.SetName("TGraph_exp_m2")

outputpath=myinput.replace('.json','.root')
print "output->",outputpath
f_output=ROOT.TFile(outputpath,"RECREATE")
TGraph_exp0.Write() 
TGraph_exp_p1.Write() 
TGraph_exp_p2.Write() 
TGraph_exp_m1.Write() 
TGraph_exp_m2.Write() 
f_output.Close()
