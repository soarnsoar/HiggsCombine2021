from math import sqrt
import sys
sys.path.insert(0,'../')
sys.path.insert(0,'./')
from GetNearest_mH import GetNearest_mH
from CondorSubmit_MakeWorkSpace import MakeWorkSpaceCommand
import os


class MakeWorkspace:
    def __init__(self,alias,year):
        self.alias=alias
        self.doInterference=True
        self.year=year
        self.suffix_I=''
    def SetInterference(self,doI=True):
        self.doInterference=doI
        self.suffix_I=''
        if not doI:
            self.suffix_I='_NoI'

    def Set_mA(self,mA):
        self.mA=mA
    def Set_tanb(self,tanb):
        self.tanb=tanb
    def Get_mHs(self,mH,list_mH):
        self.mH_low, self.mH_high =GetNearest_mH(mH,list_mH)
    def Set_xsec_gghwwlnuqq(self,xsec_gghwwlnuqq):
        self.xsec_gghwwlnuqq=xsec_gghwwlnuqq
    def Set_xsec_gghwwlnuqq_scaleupdown(self,xsec_gghwwlnuqq_scaleup,xsec_gghwwlnuqq_scaledown):
        self.xsec_gghwwlnuqq_scaleup=xsec_gghwwlnuqq_scaleup
        self.xsec_gghwwlnuqq_scaledown=xsec_gghwwlnuqq_scaledown
    def Set_xsec_gghwwlnuqq_pdfasupdown(self,xsec_gghwwlnuqq_pdfasup,xsec_gghwwlnuqq_pdfasdown):
        self.xsec_gghwwlnuqq_pdfasup=xsec_gghwwlnuqq_pdfasup ##delta xsec
        self.xsec_gghwwlnuqq_pdfasdown=xsec_gghwwlnuqq_pdfasdown
    def Eval_Sys(self):
        self.ratio_scaleup=self.xsec_gghwwlnuqq_scaleup/self.xsec_gghwwlnuqq ##delta(rel)
        self.ratio_scaledown=self.xsec_gghwwlnuqq_scaledown/self.xsec_gghwwlnuqq
        
        self.ratio_pdfasup=self.xsec_gghwwlnuqq_pdfasup/self.xsec_gghwwlnuqq
        self.ratio_pdfasdown=self.xsec_gghwwlnuqq_pdfasdown/self.xsec_gghwwlnuqq

        self.ratio_totalup=sqrt(self.ratio_scaleup**2+self.ratio_pdfasup**2)
        self.ratio_totaldown=sqrt(self.ratio_scaledown**2+self.ratio_pdfasdown**2)
    ##220130
    def GetCommand(self):
        POlist=["input_ggH_xsec:"+str(self.xsec_gghwwlnuqq),
                "input_qqH_xsec:0",
                "delta_ggH_xsec:"+str(self.ratio_totalup)+","+str(self.ratio_totaldown)]

        if self.mH_low > 350 and self.mH_high>350: 
            self.bst='all'
        else:
            self.bst='Resolved'
        curdir=os.getcwd()
        os.chdir('../')
        workdir_low,command_low,jobname_low,submit_low,ncpu_low = MakeWorkSpaceCommand(self.year,self.mH_low,self.bst,self.doInterference,POlist,self.alias+self.suffix_I+"/"+"mA_"+str(self.mA)+"_tanb_"+str(self.tanb))
        workdir_high,command_high,jobname_high,submit_high,ncpu_high = MakeWorkSpaceCommand(self.year,self.mH_high,self.bst,self.doInterference,POlist,self.alias+self.suffix_I+"/"+"mA_"+str(self.mA)+"_tanb_"+str(self.tanb))
        

        os.chdir(curdir)
        return workdir_low,command_low,jobname_low,submit_low,ncpu_low,workdir_high,command_high,jobname_high,submit_high,ncpu_high


        

    
    
