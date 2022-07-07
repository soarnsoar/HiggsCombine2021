import ROOT
import os
path="Datacards_2017/Datacards_Resolved_2017/Datacard_M1000/Resolved__SR__GGF/WW_mass/shapes/histos_Resolved__SR__GGF.root"
#path="test//histos_Resolved__SR__GGF.root"
path_backup=path+"__backup_MET17Up"
if not os.path.isfile(path_backup): 
    os.system('cp '+path+" "+path_backup)
else:
    os.system('cp '+path_backup+" "+path)

tfile=ROOT.TFile.Open(path,"UPDATE")
hnom=tfile.Get("histo_qqH_hww1000_RelW002").Clone()
hup=tfile.Get("histo_qqH_hww1000_RelW002_CMS_scale_met_2017Up")
N=hnom.GetNbinsX()
for i in range(1,N+1):
    ynom=hnom.GetBinContent(i)
    hup.SetBinContent(i,ynom*0.001)
hup.Write()
tfile.Write()
