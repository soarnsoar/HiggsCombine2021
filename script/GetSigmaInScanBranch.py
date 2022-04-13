import ROOT
import glob
import sys

param=sys.argv[1] ##

inputpath=glob.glob("higgsCombinescan.MultiDimFit**.root")[0]
tfile=ROOT.TFile.Open(inputpath)
ttree=tfile.Get("limit")
for i in ttree:
    exec("x=i."+param)
    print x
tfile.Close()
