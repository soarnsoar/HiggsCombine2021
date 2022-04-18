import ROOT
import sys


#Datacards_2016/Datacard_M1000/__BoostedALL_SB_VBFCUT_0.9/WW_mass/shapes/histos___BoostedALL_SB_VBFCUT_0.9.root
procs=['Wjets','Top']
years=['2016','2017','2018']
cuts=['0.7','0.8','0.9']
for year in years:
    for cut in cuts:
        print '----',year,'->',cut,'----'
        rf="Datacards_"+year+"/Datacard_M1000/__BoostedALL_SB_VBFCUT_"+cut+"/WW_mass/shapes/histos___BoostedALL_SB_VBFCUT_"+cut+".root"
        #rf=sys.argv[1]
        #proc=sys.argv[2]
        tfile=ROOT.TFile.Open(rf)
        for proc in procs:
        
            print proc,tfile.Get('histo_'+proc).Integral()
    

        tfile.Close()


#print yb/yd
