###
import glob
import sys
import ROOT
def Plot(dict_all,alias):
  #hist_fit_b  = ROOT.TH1F("fit_b"   ,"B-only fit Nuisances;;%s "%title,prefit.getSize(),0,prefit.getSize())
  dict_hist={}
  color={
    400:2,
    1000:3,
    3000:4,
  }
  c=ROOT.TCanvas("post_fit_errs", "post_fit_errs", 900, 600)
  leg=ROOT.TLegend(0.6,0.7,0.89,0.89)
  
  for im,mass in enumerate(sorted(dict_all)):
    offset=im*0.2
    size=len(dict_all[mass])
    dict_hist[mass]=ROOT.TH1F("fit_b"+alias+"_"+str(mass)   ,"B-only fit Nuisances",size+1,0,size)
    for b in range(1,size+1):
      syslist=sorted(dict_all[mass])
      sysname=syslist[b-1]
      print dict_all[mass][sysname]
      dict_hist[mass].SetBinContent(b,dict_all[mass][sysname])
      dict_hist[mass].SetBinError(b,0)
      dict_hist[mass].GetXaxis().SetBinLabel(b,sysname)
    dict_hist[mass].SetFillColor(color[mass])
    dict_hist[mass].SetBarWidth(0.1)
    dict_hist[mass].SetBarOffset(offset)
    dict_hist[mass].GetYaxis().SetTitle("#sigma_{#theta}/(#sigma_{#theta} prefit)")
    dict_hist[mass].SetTitle("Nuisance Parameter Uncertainty Reduction")
    dict_hist[mass].SetMaximum(1.5)
    dict_hist[mass].SetMinimum(0)
    dict_hist[mass].Draw("barsame")
    dict_hist[mass].SetStats(0)
    
    leg.AddEntry(dict_hist[mass],"M"+str(mass),"F")
  leg.SetFillColor(0)
  leg.SetTextFont(42)
  leg.Draw()
  c.SaveAs(alias+".pdf")
def Print(YEAR):

    YEAR=str(YEAR)
    MASSLIST=[400,1000,3000]
    #pyLIST=glob.glob("FitDiagnosticsDir_Sig0_all*"+str(MASS)+"*"+YEAR+"_smlike_NOFREEZEMYSTAT__cminDefaultMinimizerStrategy0/*/sigma_variation.py")
    
    dict_all={}
    for MASS in MASSLIST:
        print YEAR,MASS
        
        if YEAR=="2017":
            #FitDiagnosticsDir_Sig0_all_1000_2017_smlike_NOFREEZEMYSTAT
            py=glob.glob("FitDiagnosticsDir_Sig0_all*"+str(MASS)+"*"+YEAR+"_smlike_NOFREEZEMYSTAT/*/sigma_variation.py")[0]
        else:
          py=glob.glob("FitDiagnosticsDir_Sig0_all*"+str(MASS)+"*"+YEAR+"_smlike_NOFREEZEMYSTAT__cminDefaultMinimizerStrategy0/*/sigma_variation.py")[0]
        exec(open(py))
        #sigma_var    
        dict_all[MASS]=sigma_var


    for sys in sorted(dict_all[400]):
        s400=dict_all[400][sys]
        s1000=dict_all[1000][sys]
        s3000=dict_all[3000][sys]
        d1000=abs(s400-s1000)/s400
        d3000=abs(s400-s3000)/s400
        if d1000 > 0.10 or d3000 > 0.10:
            print '---',sys,'----'
            print s400
            print s1000
            print s3000
            
            print "!!!!"
            print 'd1000=',d1000
            print 'd3000=',d3000
    Plot(dict_all,YEAR)
if __name__ == '__main__':
    YEAR=sys.argv[1]
    Print(YEAR)
    
