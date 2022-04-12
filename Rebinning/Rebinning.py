import ROOT
import os
import sys
from numpy import array
import glob
class RebinShape:
    def __init__(self,inputfile,bins):
        self.BinsForRebinning=bins
        self.inputfile=inputfile
        self.Backup()
    def Backup(self):
        if not os.path.isfile(self.inputfile+'_backup'):
            os.system('cp '+self.inputfile+' '+self.inputfile+'_backup')
        else:
            os.system('cp '+self.inputfile+'_backup '+self.inputfile)
    def Read(self):
        self.mytfile=ROOT.TFile.Open(self.inputfile,'Update')
        
        self.histokeylist=self.mytfile.GetListOfKeys()
        self.histolist=[]
        for histokey in self.histokeylist:
            histoname=histokey.GetName()
            self.histolist.append(self.mytfile.Get(histoname))
    def GetOldBinning(self):
        self.oldbinning=[]
        self.nbins=self.histolist[0].GetNbinsX()
        print 'nbins=',self.nbins
        for i in range(1,self.nbins+2):
            x=self.histolist[0].GetBinLowEdge(i)
            #print x
            self.oldbinning.append(x)

        print self.oldbinning
        #print self.histolist[0].GetBinLowEdge(nbins)
        #print self.histolist[0].GetBinLowEdge(nbins+1)

        ##--for Check---##
        #for histo in self.histolist:
        #    print histo.GetName()
        #    print '0',histo.GetBinContent(0)
        #    print '1',histo.GetBinContent(1)
        #    print '2',histo.GetBinContent(2)
        #    print '3',histo.GetBinContent(3)
        #    print '4',histo.GetBinContent(4)
        #    print '5',histo.GetBinContent(5)
    def GetNewBinning(self):
        ###
        #1==1
        self.xToRemove=[]
        for i in self.BinsForRebinning:
            x=self.histolist[0].GetBinLowEdge(i+1) ##Right Edge
            #x=self.histolist[0].GetBinLowEdge(i) ##Left Edge

            self.xToRemove.append(x)
        self.newbinning=[]
        for b in self.oldbinning:
            if b in self.xToRemove:continue
            self.newbinning.append(float(b))
        if not self.oldbinning[-1] in self.newbinning: ##if total range is changed -> recover
            self.newbinning.pop()
            self.newbinning.append(self.oldbinning[-1])
        print self.newbinning
    def doRebinning(self):
        for h in self.histolist:
            integral_before=h.Integral()
            h=h.Rebin(len(self.newbinning)-1, h.GetName(),array(self.newbinning))
            integral_after=h.Integral()
            if integral_before!=integral_after and (integral_after-integral_before)/integral_after > 0.00001:
                print h.GetName(),integral_before,integral_after,(integral_after-integral_before)
        self.mytfile.Write()
        self.mytfile.Close()

class config:
    def __init__(self,path,regioncode):
        #../Datacards_2016/Datacard_M1000/__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01/WW_mass/
        #[jhchoi@ui20 Rebinning]$ ls ../Datacards_2016/Datacard_M500/__BoostedALL_SR_NoMEKDCut/WW_mass/shapes/histos___BoostedALL_SR_NoMEKDCut.root 

        #hww_lqq_bst_ggf_2016
        exec(open(path,'r'))
        self.rawconfig=config
        self.regioncode=regioncode
        self.config={}
        self.Parse()
    def Parse(self):
        #BoostedUNTAG_SR0
        for key in self.rawconfig:
            ##--Year
            if '2016' in key:
                Year='2016'
            elif '2017' in key:
                Year='2017'
            elif '2018' in key:
                Year='2018'
            else:
                1/0
            ##--Boosted
            if 'bst' in key:
                Boosted='Boosted'
            else:
                Boosted='Resolved'
            ##--GGF VBF UNTAG
            if 'ggf' in key:
                GGFVBF='GGF'
            elif 'untag' in key:
                GGFVBF='UNTAG'
            elif 'vbf' in key:
                GGFVBF='VBF'
            ##--SRCR region
            if 'sb' in key:
                REGION='SB'
                variable='WW_mass'
            elif 'top' in key:
                REGION='TOP'
                variable='WW_mass'
            else:
                REGION='SR'
                variable='WW_mass'
            formula='Datacards_'+Year+'/Datacard_M*/*'+Boosted+'*'+GGFVBF+'*'+REGION+self.regioncode+'*/'+variable+'/shapes/*.root'
            self.config[key]={
                'path':formula,
                'bintofix':self.rawconfig[key]
            }
        print self.config
if __name__=='__main__':
    #import argparse
    #parser = argparse.ArgumentParser()
    ####Set options###
    #parser.add_argument("--c", help="filename")
    #parser.add_argument("--b", help="binningtofix")
    confpath=sys.argv[1]
    #regioncode=sys.argv[2]
    #filename=args.f
    regioncode=confpath.split('_')[1].rstrip('.py')

    #bins=(args.b)
    #bins=bins.split(',')
    #bins_in_int=[]
    #for b in bins:
    #    bins_in_int.append(int)
    #myjob=RebinShape('histos___BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01.root',[1,2,3,4])
    myconfig=config(confpath,regioncode)
    for conf in myconfig.config:

        print '---',conf,'---'
        
        filelist=glob.glob(myconfig.config[conf]['path'])
        print 'nfiles=',len(filelist)
        bins=myconfig.config[conf]['bintofix']
        for filename in filelist:
            myjob=RebinShape(filename,bins)
            myjob.Read()
            myjob.GetOldBinning()
            myjob.GetNewBinning()
            myjob.doRebinning()
            
