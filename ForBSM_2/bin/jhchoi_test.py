import sys

sys.path.insert(0,'ForBSM_2/python')
sys.path.insert(0,'python')
sys.path.insert(0,'../python')

from Model import *
from MakeWorkspace import *
from ExportShellCondorSetup import Export

def Run(model_file,alias):
    
    list_mH=[115 ,120 ,124 ,125 ,126 ,130 ,135 ,140 ,145 ,150 ,155 ,160 ,165 ,170 ,175 ,180 ,190 ,200 ,210 ,230 ,250,270 ,300 ,350 ,400 ,450 ,500 ,550 ,600 ,650 ,700 ,750 ,800, 900,1000 ,1500 ,2000 ,2500 ,3000 ,4000 ,5000]
    mA=250
    tanb=0.5
    year=2016


    mymodel=Model(model_file,alias)
    mymodel.Set_mA(mA)
    mymodel.Set_tanb(tanb)
    mymodel.Eval()
    
    
    mH=mymodel.mH
    xsec_gghwwlnuqq=mymodel.xsec_gghwwlnuqq

    myws=MakeWorkspace(alias,year)
    myws.Set_mA(mA)
    myws.Set_tanb(tanb)
    myws.Get_mHs(mH,list_mH)
    myws.Set_xsec_gghwwlnuqq(mymodel.xsec_gghwwlnuqq)
    myws.Set_xsec_gghwwlnuqq_scaleupdown(mymodel.xsec_gghwwlnuqq_scaleup,mymodel.xsec_gghwwlnuqq_scaledown)
    myws.Set_xsec_gghwwlnuqq_pdfasupdown(mymodel.xsec_gghwwlnuqq_pdfasup,mymodel.xsec_gghwwlnuqq_pdfasdown)
    myws.Eval_Sys()

    workdir_low,command_low,jobname_low,submit_low,ncpu_low,  workdir_high,command_high,jobname_high,submit_high,ncpu_high=    myws.GetCommand()
    

    print "mH->",mH
    print 'workdir_low',workdir_low
    print 'command_low',command_low
    print 'jobname_low',jobname_low,
    print 'submit_low',submit_low
    print 'ncpu_low',ncpu_low

    print 'workdir_high',workdir_high
    print 'command_high',command_high
    print 'jobname_high',jobname_high,
    print 'submit_high',submit_high
    print 'ncpu_high',ncpu_high

    Export(workdir_low,command_low,jobname_low,submit_low,ncpu_low)

if __name__ == '__main__':
    Run('model_files/mh125_13_withVBF.root','mh125_13')
