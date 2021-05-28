####mh125_13_withVBF.root
import ROOT
import os
from array import array
from copy import deepcopy
from math import log
import json
def GetIntersectionTGraphs(xmin,xmax,n,tg1,tg2):
    xlist=[]
    for i in range(n):

        _x1=xmin+(xmax-xmin)/n*i
        _x2=xmin+(xmax-xmin)/n*(i+1)
        #print _x1
        
        _tg1_y1=tg1.Eval(_x1)
        _tg1_y2=tg1.Eval(_x2)

        _tg2_y1=tg2.Eval(_x1)
        _tg2_y2=tg2.Eval(_x2)

        _dy1=(_tg1_y1-_tg2_y1)
        _dy2=(_tg1_y2-_tg2_y2)

        _ry1=(_tg1_y1/_tg2_y1)
        _ry2=(_tg1_y2/_tg2_y2)
        if _ry1<=0 or _ry2<=0:
            continue
        if log(_ry1)*log(_ry2)<=0:
            #print "Find!"
            x=(_x1+_x2)/2
            xlist.append(x)
    return xlist

def GetTGraph_xsec_mA_for_fixed_tanb(input_file,tanb):
    #input_file="mh125_13_withVBF.root"
    tfile=ROOT.TFile.Open(input_file)
    
    ##---list of histo object names
    #xs_gg_H,br_H_WW,m_H
    h_xs_gg_H=tfile.Get("xs_gg_H")
    h_br_H_WW=tfile.Get("br_H_WW")
    h_m_H=tfile.Get("m_H")
    

    ##--first, let's draw x=mH y=xsec for given tanb (y value)
    mA_list=[]
    #tanb=1.0

    ##--make grid
    N_mA=100
    max_mA=3000.
    #min_mA= h_m_H.GetXaxis().GetBinCenter(1)+h_m_H.GetXaxis().GetBinWidth(0)
    min_mA=0.
    #print min_mA
    for i in range(N_mA+1):
        _mA=min_mA+(max_mA-min_mA)/N_mA*i
        mA_list.append(_mA)
        #print _mA
    array_mH=array('d')
    array_xsec=array('d')
    array_mA=array('d')
    for mA in mA_list:
        #h->GetBinContent(h->FindBin(mphi,tanb));
    
        _mH=h_m_H.GetBinContent(h_m_H.FindBin(mA,tanb))
        if _mH<150:continue
        _br_H_WW=h_br_H_WW.GetBinContent(h_br_H_WW.FindBin(mA,tanb))
        _xs_gg_H=h_xs_gg_H.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))
        array_mH.append(_mH)
        #print _mH
        _xsec_gghwwlnuqq=_xs_gg_H*_br_H_WW*0.1086*3*0.6741*2
        #print _xsec_gghww
        array_xsec.append(_xsec_gghwwlnuqq)

        array_mA.append(mA)
    if len(array_xsec)==0:
        return False
    ##---TGraph

    tg_xsec=ROOT.TGraph(len(array_mH),array_mH,array_xsec)
    tg_mA=ROOT.TGraph(len(array_mA),array_mH,array_mA)
    tfile.Close()
    return tg_xsec, tg_mA, array_mA[0]

def GetExclusion_mA_fixed_tanb(rf_model,tanb,rf_limit,alias):

    #tg_xsec, tg_mA, min_mA=GetTGraph_xsec_mA_for_fixed_tanb("mh125_13_withVBF.root",1.0)
    if False==GetTGraph_xsec_mA_for_fixed_tanb(rf_model,tanb):return False
    tg_xsec, tg_mA, min_mA=GetTGraph_xsec_mA_for_fixed_tanb(rf_model,tanb)

    ##---Measured limit
    #rf_limit="../AsymptoticLimits/2016/all/ggfonly/indep.root"
    tfilelimit=ROOT.TFile.Open(rf_limit)
    tg_exp0=tfilelimit.Get("TGraph_exp0")
    tg_exp_p1=tfilelimit.Get("TGraph_exp_p1")
    tg_exp_p2=tfilelimit.Get("TGraph_exp_p2")
    tg_exp_m1=tfilelimit.Get("TGraph_exp_m1")
    tg_exp_m2=tfilelimit.Get("TGraph_exp_m2")
    
    ##--1) Get intersection between exp and theory xsec
    mHinter_list=deepcopy(GetIntersectionTGraphs(min_mA,2000,2000,tg_exp0,tg_xsec))
    #print mHinter_list
    
    ##--2)Convert to mA
    mAinter_list=[]
    for _mH in mHinter_list:
        _mA=tg_mA.Eval(_mH)
        mAinter_list.append(_mA)

    #print mAinter_list

    c1=ROOT.TCanvas()
    c1.SetLogy()
    c1.SetLogx()
    tg_exp0.Draw("AL")
    tg_xsec.Draw("L")
    tg_xsec.SetLineColor(2)
    os.system("mkdir -p plots/")
    c1.SaveAs("plots/"+alias+".pdf")


    tfilelimit.Close()

    return deepcopy(mAinter_list),deepcopy(mHinter_list)

rf_model="mh125_13_withVBF.root"
#tanb=1.0
year=2016
rf_limit="../AsymptoticLimits/"+str(year)+"/all/ggfonly/indep.root"



tanb_list=[]
#for i in range(10):
#    tanb_list.append(0.4+i*0.1)
#for i in range(1,10):
#    tanb_list.append(i+1)

for i in range(200):
    if i<100:
        tanb_list.append(0.4+i*0.01)
    else:
        tanb_list.append(1.4+(i-100)*0.1)

exclusion_region={}

for tanb in tanb_list:
    alias="mh125_13_withVBF__tanb_"+str(tanb)+"__"+str(year)
    if False == GetExclusion_mA_fixed_tanb(rf_model,tanb,rf_limit,alias): continue
    mAinter_list,mHinter_list=GetExclusion_mA_fixed_tanb(rf_model,tanb,rf_limit,alias)
    print "<<<   tanb=",tanb,"   >>>>"
    if len(mAinter_list)!=2 or len(mHinter_list)!=2:
        print "[Warning]# of Intersections is not 2!!!"
    
    print mAinter_list
    print mHinter_list

    if len(mAinter_list)==2:
        exclusion_region[tanb]=mAinter_list

os.system("mkdir -p exregion_json/")
with open("exregion_json/"+alias+".json","w") as make_file:
    json.dump(exclusion_region,make_file,)
