doRound=True
import ROOT
import sys
path=sys.argv[1]
tfile=ROOT.TFile.Open(path)

PassBin0=tfile.Get("PassingWtagger__200/Event/histo_ALLPROC").Integral()
PassBin1=tfile.Get("PassingWtagger__300/Event/histo_ALLPROC").Integral()
PassBin2=tfile.Get("PassingWtagger__400/Event/histo_ALLPROC").Integral()

FailBin0=tfile.Get("FailingWtagger__200/Event/histo_ALLPROC").Integral()
FailBin1=tfile.Get("FailingWtagger__300/Event/histo_ALLPROC").Integral()
FailBin2=tfile.Get("FailingWtagger__400/Event/histo_ALLPROC").Integral()

if doRound:
    PassBin0=round(PassBin0)
    PassBin1=round(PassBin1)
    PassBin2=round(PassBin2)

    FailBin0=round(FailBin0)
    FailBin1=round(FailBin1)
    FailBin2=round(FailBin2)


EffBin0m=float(PassBin0)/(float(PassBin0)+float(FailBin0))
EffBin1m=float(PassBin1)/(float(PassBin1)+float(FailBin1))
EffBin2m=float(PassBin2)/(float(PassBin2)+float(FailBin2))


#print "--PO=Ninit_Bin0:"+str(PassBin0)+" --PO=Ninit_Bin1:"+str(PassBin1)+" --PO=Ninit_Bin2:"+str(PassBin2)+" --PO=EffBin0m:"+str(EffBin0m)+" --PO=EffBin1m:"+str(EffBin1m)+" --PO=EffBin2m:"+str(EffBin2m)

print "--PO=Ninit_PassBin0:"+str(PassBin0)+" --PO=Ninit_PassBin1:"+str(PassBin1)+" --PO=Ninit_PassBin2:"+str(PassBin2)+" --PO=Ninit_FailBin0:"+str(FailBin0)+" --PO=Ninit_FailBin1:"+str(FailBin1)+" --PO=Ninit_FailBin2:"+str(FailBin2)

