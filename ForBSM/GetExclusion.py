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

def CollectLimitCommand(year,mH,suffix):
    year=str(year)
    mH=str(mH)
    LimitDIR="AsymptoticLimits/"+year+"/"+suffix
    command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
    Collect="combineTool.py -M CollectLimits -i higgsCombine*.root"
    command_list.append(Collect)
    return ";".join(command_list)

def Interpolate_r(year,mH,suffix):
    year=str(year)
    
    LimitDIR="AsymptoticLimits/"+year+"/"+suffix+"/"
    #command_list=["cd "+os.getcwd(),"mkdir -p "+LimitDIR,"cd "+LimitDIR]
    ##--Interpolate r
    myinfo={}
    myinfo_interpolate={}
    myinfo_interpolate[mH]={}
    with open(LimitDIR+"limits.json","r") as handle:
        myinfo=json.load(handle)


    masslist=[]
    keylist=[]
    for _mH in myinfo:
        #_mH=float(_mH)
        masslist.append(_mH)
    
    if len(masslist) !=2: return False

    for key in myinfo[masslist[0]]:
        keylist.append(key)

    for key in keylist: ##exp0,exp1,...
        m1=float(masslist[0])
        m2=float(masslist[1])
        #w1*m1+w2*m2=mH
        #w1+w2=1
        #w2=1-w1
        #w1*m1+(1-w1)*m2=mH
        #w1(m1-m2)+m2=mH
        w1=(mH-m2)/(m1-m2)
        w2=(m1-mH)/(m1-m2)
        if key in myinfo[masslist[0]]:
            r1=myinfo[masslist[0]][key]
        else:
            r1=2000.
        if key in myinfo[masslist[1]]:
            r2=myinfo[masslist[1]][key]
        else:
            r2=2000.
        myinfo_interpolate[mH][key]=w1*r1 + w2*r2
    
    with open(LimitDIR+"limits_interpolate.json","w") as handle:
        json.dump(myinfo_interpolate,handle)
    

    return True

if __name__ == '__main__':
    ##---
    import sys
    rf_model=sys.argv[1]
    year=sys.argv[2]
    #rf_model="mh125_13_withVBF.root"
    suffix_model=rf_model.rstrip('.root')
    #year=2016

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

            DoneAsymptoticLimit_low=False
            DoneAsymptoticLimit_high=False


            os.chdir(curdir)
            print "<mA=",mA,"tanb=",tanb,'>'
            mH,xsec_gghwwlnuqq,xsec_gghwwlnuqq_scaleup,xsec_gghwwlnuqq_scaledown,xsec_gghwwlnuqq_pdfasup,xsec_gghwwlnuqq_pdfasdown=mH_xsec_for_mA_tanb(rf_model,mA,tanb)

            if not xsec_gghwwlnuqq:
                print "Skip->",mA,tanb,"due to xsec==0"
                continue
            mH_low, mH_high=GetNearest_mH(mH,list_mH)
            if -9999==mH_low or -9999==mH_high : 
                print "Skip->",mH_low,mH_high
                continue
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
                if os.path.isfile(workdir+"/run.sh") : 
                    print "Not Finished Job->",workdir
                    continue
                print "---Submit---",command
                Export(workdir,command,jobname,submit,ncpu)
            else:
                DoneWS_low=True
            workdir,command,jobname,submit,ncpu = MakeWorkSpaceCommand(year,mH_high,"all",True,POlist,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            if not os.path.isfile(workdir+"/run.done"):
                if os.path.isfile(workdir+"/run.sh") : 
                    print "Not Finished Job->",workdir
                    continue
                print "---Submit---",command
                Export(workdir,command,jobname,submit,ncpu) 
            else:
                DoneWS_high=True

            if not DoneWS_high or not DoneWS_low: continue

            ##--go to Asymptotic limit
            ##---WS path = Workspaces_2016/hwwlnuqq_all_270_2016_mA_100_tanb_0.5.root
            #combine -M AsymptoticLimits -d combine_hwwlnuqq_all_200_2016_test.root -t -1 --run expected -m 200 --trackParameters deltaTheory_ggH_hww_xsec,deltaTheory_qqH_hww_xsec -n nom --verbose 2 &> Asymptotic_combine_hwwlnuqq_all_200_2016_test.log&

            command=AsymptoticLimitCommand(year,mH_low,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            suffix=suffix_model+"/mA_"+str(mA)+"_tanb_"+str(tanb)
            workdir="WORKDIR/AsymptoticLimits/"+str(year)+"/"+suffix+"/"+str(mH_low)
            jobname=workdir
            submit=True
            ncpu=1
            if not os.path.isfile(workdir+"/run.done"):
                if os.path.isfile(workdir+"/run.sh") : 
                    print "Not Finished Job->",workdir
                    continue
                print "--Submit AsymptoticLimit for mH_low"
                Export(workdir,command,jobname,submit,ncpu)
            else:
                DoneAsymptoticLimit_low=True


            command=AsymptoticLimitCommand(year,mH_high,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            workdir="WORKDIR/AsymptoticLimits/"+str(year)+"/"+suffix+"/"+str(mH_high)
            jobname=workdir
            submit=True
            ncpu=1
            if not os.path.isfile(workdir+"/run.done"):
                if os.path.isfile(workdir+"/run.sh") :
                    print "Not Finished Job->",workdir
                    continue
                print "--Submit AsymptoticLimit for mH_high"
                Export(workdir,command,jobname,submit,ncpu)
            else:
                DoneAsymptoticLimit_high=True


            ##---CollectLimit
            if not DoneAsymptoticLimit_low or not DoneAsymptoticLimit_high: continue
                
            command=CollectLimitCommand(year,mH_high,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            workdir="WORKDIR/CollectLimit/"+str(year)+"/"+suffix+"/"
            jobname=workdir
            submit=True
            ncpu=1
            DoneCollect=False
            if not os.path.isfile(workdir+"/run.done"):
                if os.path.isfile(workdir+"/run.sh") :
                    print "Not Finished Job->",workdir
                    continue
                print "--Collect Limit--"
                Export(workdir,command,jobname,submit,ncpu)
            else:
                DoneCollect=True

            if not DoneCollect: continue
            ##--interpolate
            DONE_interpolate=Interpolate_r(year,mH,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
            continue
            if not DONE_interpolate:
                print "Resubmit Asymptotic Limit"
                command=AsymptoticLimitCommand(year,mH_high,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
                workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+str(mH_high)
                jobname=workdir
                submit=True
                ncpu=1
                Export(workdir,command,jobname,submit,ncpu)

                command=AsymptoticLimitCommand(year,mH_low,suffix_model+"/"+"mA_"+str(mA)+"_tanb_"+str(tanb))
                suffix=suffix_model+"/mA_"+str(mA)+"_tanb_"+str(tanb)
                workdir="WORKDIR/AsymptoticLimits/"+suffix+"/"+str(mH_low)
                jobname=workdir
                submit=True
                ncpu=1
                Export(workdir,command,jobname,submit,ncpu)
