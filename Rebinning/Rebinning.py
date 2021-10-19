import ROOT
import os
import sys
from numpy import array
class RebinShape:
    def __init__(self,inputfile,bins):
        self.BinsForRebinning=bins
        self.inputfile=inputfile
        self.Backup()
    def Backup(self):
        if not os.path.isfile(self.inputfile+'_backup'):
            os.system('cp '+self.inputfile+' '+self.inputfile+'_backup')
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
            x=self.histolist[0].GetBinLowEdge(i+1)
            self.xToRemove.append(x)
        self.newbinning=[]
        for b in self.oldbinning:
            if b in self.xToRemove:continue
            self.newbinning.append(float(b))
        print self.newbinning
    def doRebinning(self):
        for h in self.histolist:
            h=h.Rebin(len(self.newbinning)-1, h.GetName(),array(self.newbinning))
        self.mytfile.Write()


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    ####Set options###
    parser.add_argument("--f", help="filename")
    parser.add_argument("--b", help="binningtofix")
    
    filename=args.f
    bins=(args.b)
    bins=bins.split(',')
    bins_in_int=[]
    for b in bins:
        bins_in_int.append(int)
    #myjob=RebinShape('histos___BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01.root',[1,2,3,4])
    myjob=RebinShape(filename,b)
    myjob.Read()
    myjob.GetOldBinning()
    myjob.GetNewBinning()
    myjob.doRebinning()
