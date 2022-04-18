import ROOT
import sys


#Datacards_2016/Datacard_M1000/__BoostedALL_SB_VBFCUT_0.9/WW_mass/shapes/histos___BoostedALL_SB_VBFCUT_0.9.root
#procs=['Wjets','Top']
proc='ggH_hww1000_RelW002'
SBSR=['SB','SR']
years=['2016','2017','2018']
cuts=['0.7','0.8','0.9']
for year in years:
    for cut in cuts:
        print '----',year,'->',cut,'----'
        for R in SBSR:

            rf="Datacards_"+year+"/Datacard_M1000/__BoostedALL_"+R+"_VBFCUT_"+cut+"/WW_mass/shapes/histos___BoostedALL_"+R+"_VBFCUT_"+cut+".root"
            #rf=sys.argv[1]
            #proc=sys.argv[2]
            tfile=ROOT.TFile.Open(rf)

        
            print R,tfile.Get('histo_'+proc).Integral()
    

            tfile.Close()


#print yb/yd
