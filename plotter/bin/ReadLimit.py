import glob
import ROOT
import os
def ReadLimit(hc_output):
    tfile=ROOT.TFile.Open(hc_output)
    ttree=tfile.Get('limit')
    ret=False
    for entry in ttree:
        _limit=entry.limit
        _quantileExpected=entry.quantileExpected
        #print '=='
        #print _limit
        #print _quantileExpected
        if _quantileExpected==0.5:ret=_limit
    tfile.Close()
    return ret
    ##
if __name__ == '__main__':    
    hc_output=glob.glob('/cms_scratch/jhchoi/DeepAK8WP_220422/HC/HiggsCombine2021/HP/Datacards_2016/Datacard_M1000/FullCutSR/WW_mass/higg*vbfonly*.root')[0]
    a=ReadLimit(hc_output)
    print a
