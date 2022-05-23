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

EffBin0m=PassBin0/(PassBin0+FailBin0)
EffBin1m=PassBin1/(PassBin1+FailBin1)
EffBin2m=PassBin2/(PassBin2+FailBin2)


print "--PO=Ninit_Bin0:"+str(PassBin0)+" --PO=Ninit_Bin1:"+str(PassBin1)+" --PO=Ninit_Bin2:"+str(PassBin2)+" --PO=EffBin0m:"+str(EffBin0m)+" --PO=EffBin1m:"+str(EffBin1m)+" --PO=EffBin2m:"+str(EffBin2m)

