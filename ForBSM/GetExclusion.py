####mh125_13_withVBF.root
import ROOT
import os
from array import array
from copy import deepcopy
from math import log,sqrt
import json
import sys
sys.path.insert(0,"../")
sys.path.insert(0, "../python_tool/")
from ExportShellCondorSetup import Export

def mH_xsec_for_mA_tanb(input_file,mA,tanb):
    #input_file="mh125_13_withVBF.root"
    tfile=ROOT.TFile.Open(input_file)
    
    ##---list of histo object names
    #xs_gg_H,br_H_WW,m_H
    ##--sys
    ##---xs_gg_H_scaleup/xs_gg_H_scaledown/xs_gg_H_pdfasup/xs_gg_H_pdfasdown
    h_xs_gg_H=tfile.Get("xs_gg_H")
    ##--Theoretical systematic
    h_xs_gg_H_scaleup=tfile.Get("xs_gg_H_scaleup")
    h_xs_gg_H_scaledown=tfile.Get("xs_gg_H_scaledown")

    h_xs_gg_H_pdfasup=tfile.Get("xs_gg_H_pdfasup")
    h_xs_gg_H_pdfasdown=tfile.Get("xs_gg_H_pdfasdown")


    h_br_H_WW=tfile.Get("br_H_WW")
    h_m_H=tfile.Get("m_H")
    
    _brlnuqq=0.1086*3*0.6741
    _mH=h_m_H.GetBinContent(h_m_H.FindBin(mA,tanb))
    _br_H_WW=h_br_H_WW.GetBinContent(h_br_H_WW.FindBin(mA,tanb))
    _xs_gg_H=h_xs_gg_H.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))
    _xs_gg_H_scaleup=h_xs_gg_H_scaleup.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))
    _xs_gg_H_scaledown=h_xs_gg_H_scaledown.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))
    _xs_gg_H_pdfasup=h_xs_gg_H_pdfasup.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))
    _xs_gg_H_pdfasdown=h_xs_gg_H_pdfasdown.GetBinContent(h_xs_gg_H.FindBin(mA,tanb))


    _xsec_gghwwlnuqq=_xs_gg_H*_br_H_WW*0.1086*3*0.6741*2

    _xsec_gghwwlnuqq=_xs_gg_H*_br_H_WW*_brlnuqq
    _xsec_gghwwlnuqq_scaleup=_xs_gg_H_scaleup*_br_H_WW*_brlnuqq
    _xsec_gghwwlnuqq_scaledown=_xs_gg_H_scaledown*_br_H_WW*_brlnuqq
    _xsec_gghwwlnuqq_pdfasup=_xs_gg_H_pdfasup*_br_H_WW*_brlnuqq
    _xsec_gghwwlnuqq_pdfasdown=_xs_gg_H_pdfasdown*_br_H_WW*_brlnuqq
    
    
    return _mH,_xsec_gghwwlnuqq,_xsec_gghwwlnuqq_scaleup,_xsec_gghwwlnuqq_scaledown,_xsec_gghwwlnuqq_pdfasup,_xsec_gghwwlnuqq_pdfasdown

def GetNearest_mH(mH,list_mH):
    mH_low=-9999
    mH_high=-9999
    for i in range(len(list_mH)-1):
        mH_i = list_mH[i]
        mH_i_1 = list_mH[i+1]
        if mH >=mH_i and mH < mH_i_1:
            mH_low=mH_i
            mH_high=mH_i_1

    return mH_low, mH_high
            
#def MakeWorkspaceCommand(mH,xsec_gghwwlnuqq,PO,year):
#    #os.chdir("../")
#    #os.system("python CondorSubmit_MakeWorkSpace.py -y "+str(year)+" -m "+str(mH)+" -b all --PO input_ggH_xsec:"+str(xsec_gghwwlnuqq)+",input_qqH_xsec:0")


def AsymptoticLimitCommand(year,mH,suffix):
    #
    ##---WS path = Workspaces_2016/hwwlnuqq_all_270_2016_mA_100_tanb_0.5.root                                                                     
    #combine -M AsymptoticLimits -d combine_hwwlnuqq_all_200_2016_test.root -t -1 --run expected -m 200 --trackParameters deltaTheory_ggH_hww_xsec,deltaTheory_qqH_hww_xsec -n nom --verbose 2 &> Asymptotic_combine_hwwlnuqq_all_200_2016_test.log&


    year=str(year)
    mH=str(mH)
    WSpath=os.getcwd()+"/Workspaces_"+year+"/"+suffix+"/hwwlnuqq_all_"+mH+"_"+year+".root"
    LimitDIR="AsymptoticLimits/"+year+"/"+suffix
    command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
    LimitOptions=" -t -1 --run expected -m "+mH
    Asymptotic="combine -M AsymptoticLimits -d "+WSpath+" "+LimitOptions+" "
    command_list.append(Asymptotic)
    return ";".join(command_list)

if __name__ == '__main__':
    ##---
    rf_model="mh125_13_withVBF.root"
    suffix_model=rf_model.rstrip('.root')
    year=2016

    list_mA=[]
    list_tanb=[]
    list_mH=[]
    ##--read grid
    with open("config/mA_grid.json","r") as handle:
        list_mA=json.load(handle)
    ##--read grid
    with open("config/tanb_grid.json","r") as handle:
        list_tanb=json.load(handle)
    ##--read grid
    with open("config/mH_grid.json","r") as handle:
        list_mH=json.load(handle)

    
    from CondorSubmit_MakeWorkSpace import MakeWorkSpaceCommand
    #def MakeWorkSpaceCommand(year,mass,bst,interference,POlist):
    curdir=os.getcwd()
    #list_mA=[200]
    #list_tanb=[1.0]
    for mA in list_mA:
        for tanb in list_tanb:
            #continue
            DoneWS_low=False
            DoneWS_high=False
            os.chdir(curdir)
            print "<mA=",mA,"tanb=",tanb,'>'
            mH,xsec_gghwwlnuqq,xsec_gghwwlnuqq_scaleup,xsec_gghwwlnuqq_scaledown,xsec_gghwwlnuqq_pdfasup,xsec_gghwwlnuqq_pdfasdown=mH_xsec_for_mA_tanb(rf_model,mA,tanb)
            mH_low, mH_high=GetNearest_mH(mH,list_mH)
            print mH_low,mH,mH_high
            os.chdir(curdir+"/../")
            ##---syst in ratio
            ratio_scaleup=xsec_gghwwlnuqq_scaleup/xsec_gghwwlnuqq
            ratio_scaledown=xsec_gghwwlnuqq_scaledown/xsec_gghwwlnuqq

            ratio_pdfasup=xsec_gghwwlnuqq_pdfasup/xsec_gghwwlnuqq
            ratio_pdfasdown=xsec_gghwwlnuqq_pdfasdown/xsec_gghwwlnuqq

            ratio_totalup=sqrt(ratio_scaleup**2+ratio_pdfasup**2)
            ratio_totaldown=sqrt(ratio_scaledown**2+ratio_pdfasdown**2)

            
            print "sysup=",ratio_totalup
            print "sysdown=",ratio_totaldown

            POlist=["input_ggH_xsec:"+str(xsec_gghwwlnuqq),
                    "input_qqH_xsec:0",
                    "delta_ggH_xsec:"+str(ratio_totalup)+","+str(ratio_totaldown)]
            workdir,command,jobname,submit,ncpu = MakeWorkSpaceCommand(year,mH_low,"all",True,POlist,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            if not os.path.isfile(workdir+"/run.done"):
                print "---Submit---",command
                Export(workdir,command,jobname,submit,ncpu)
            else:
                DoneWS_low=True
            workdir,command,jobname,submit,ncpu = MakeWorkSpaceCommand(year,mH_high,"all",True,POlist,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            if not os.path.isfile(workdir+"/run.done"):
                print "---Submit---",command
                Export(workdir,command,jobname,submit,ncpu) 
            else:
                DoneWS_high=True

            if DoneWS_high and DoneWS_low:
                ##--go to Asymptotic limit
                ##---WS path = Workspaces_2016/hwwlnuqq_all_270_2016_mA_100_tanb_0.5.root
                #combine -M AsymptoticLimits -d combine_hwwlnuqq_all_200_2016_test.root -t -1 --run expected -m 200 --trackParameters deltaTheory_ggH_hww_xsec,deltaTheory_qqH_hww_xsec -n nom --verbose 2 &> Asymptotic_combine_hwwlnuqq_all_200_2016_test.log&
                print "--Submit AsymptoticLimit for mH_low"
                command=AsymptoticLimitCommand(year,mH_low,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
                suffix=suffix_model+"/mA_"+str(mA)+"_tanb_"+str(tanb)
                workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+str(mH_low)
                jobname=workdir
                submit=True
                ncpu=1
                Export(workdir,command,jobname,submit,ncpu)
                print "--Submit AsymptoticLimit for mH_high"
                command=AsymptoticLimitCommand(year,mH_high,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
                workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+str(mH_high)
                jobname=workdir
                submit=True
                ncpu=1
                Export(workdir,command,jobname,submit,ncpu)
                
