import os
import sys
import json

sys.path.insert(0,'ForBSM_2/python')
sys.path.insert(0,'python')
sys.path.insert(0,'../python')

from Model import *
from MakeWorkspace import *
from ExportShellCondorSetup import Export
from AsymptoticLimitCommand import AsymptoticLimitCommand
from CollectLimitCommand import CollectLimitCommand
from Read_grid import Read_grid


class Run_model:
    def __init__ (self,model_file,alias,year):

        #list_mH=[115 ,120 ,124 ,125 ,126 ,130 ,135 ,140 ,145 ,150 ,155 ,160 ,165 ,170 ,175 ,180 ,190 ,200 ,210 ,230 ,250,270 ,300 ,350 ,400 ,450 ,500 ,550 ,600 ,650 ,700 ,750 ,800, 900,1000 ,1500 ,2000 ,2500 ,3000 ,4000 ,5000]
        self.list_mA,self.list_tanb,self.list_mH=Read_grid()

        ###-----Set model----##
        self.model_file=model_file
        self.alias=alias
        self.year=year

        self.mymodel=Model(model_file,alias)


    def Set_mA_tanb(self,mA,tanb):
        self.mymodel.Set_mA(mA)
        self.mymodel.Set_tanb(tanb)
        self.mymodel.Eval()
        self.do_qqH=False
        self.do_ggH=False
        if self.mymodel.xsec_gghwwlnuqq > 0.:
            self.do_ggH=True
    def Run(self):
        
        all_command_list=[]

        ###---Model--##
        mH=self.mymodel.mH
        xsec_gghwwlnuqq=self.mymodel.xsec_gghwwlnuqq
        
        ##---Workspace--##
        myws=MakeWorkspace(self.alias,self.year)
        myws.Set_mA(mA)
        myws.Set_tanb(tanb)
        myws.Get_mHs(mH,self.list_mH)
        if self.do_ggH:
            myws.Set_xsec_gghwwlnuqq(self.mymodel.xsec_gghwwlnuqq)
            myws.Set_xsec_gghwwlnuqq_scaleupdown(self.mymodel.xsec_gghwwlnuqq_scaleup,self.mymodel.xsec_gghwwlnuqq_scaledown)
            myws.Set_xsec_gghwwlnuqq_pdfasupdown(self.mymodel.xsec_gghwwlnuqq_pdfasup,self.mymodel.xsec_gghwwlnuqq_pdfasdown)
            myws.Eval_Sys()
        else:
            return 0
        mH_low=myws.mH_low
        mH_high=myws.mH_high
        
        workdir_low,command_low,jobname_low,submit_low,ncpu_low,  workdir_high,command_high,jobname_high,submit_high,ncpu_high=    myws.GetCommand()
        
        all_command_list.append(command_low)
        all_command_list.append(command_high)
        
        jobname=self.alias
        
        ##----Limit---##
        curdir=os.getcwd()
        os.chdir('../')
        wsd_suffix=self.alias+'/mA_'+str(mA)+'_tanb_'+str(tanb)
        command_low=AsymptoticLimitCommand(self.year,mH_low,wsd_suffix,myws.bst)
        command_high=AsymptoticLimitCommand(self.year,mH_high,wsd_suffix,myws.bst)
        
        all_command_list.append(command_low.GetCommand())
        all_command_list.append(command_high.GetCommand())
        
        os.chdir(curdir)
        
        os.chdir('../')
        
        collect=CollectLimitCommand(self.year,wsd_suffix)
        all_command_list.append(collect.GetCommand())
        os.chdir(curdir)

        limitdir=collect.LimitDIR

        command_interpolate_r="cd "+curdir+"&&python bin/InterpolateR.py "+str(mH)+' '+limitdir
        all_command_list.append(command_interpolate_r)
        
        
        
        final_command='&&'.join(all_command_list)
        #---combined job---#
        workdir="WORKDIR/Combined_JOB"+str(self.year)+"/"+wsd_suffix
        jobname=self.alias
        submit=True
        ncpu=1
        Export(workdir,final_command,jobname,submit,ncpu)

if __name__ == '__main__':
    model_file=sys.argv[1]
    alias=sys.argv[2]
    year=sys.argv[3]

    #model=Run_model('model_files/mh125_13_withVBF.root','mh125_13',2016)
    model=Run_model(model_file,alias,year)
    idx=0
    for mA in model.list_mA:
        #if str(mA)!='220':continue
        for tanb in model.list_tanb:
            #if idx>0:continue
            #if str(tanb)!='1.0':continue
            model.Set_mA_tanb(mA,tanb)
            model.Run()
            idx+=1
    print idx
