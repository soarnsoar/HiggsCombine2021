import ROOT
import sys

rf=sys.argv[1]
proc=sys.argv[2]
tfile=ROOT.TFile.Open(rf)

BKG=[ 'DY', 'MultiBoson', 'Top','Wjets','QCD','WW','VH','qqWWqq','ggWW','ggH_hww','qqH_hww']

yb=0
#for b in BKG:
#    yb+=tfile.Get('histo_'+b).Integral()

#yd=tfile.Get('histo_Data').Integral()
print tfile.Get('histo_'+proc).Integral()


tfile.Close()


#print yb/yd