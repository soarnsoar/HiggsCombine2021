import sys
import ROOT
#   cutlist=f.GetListOfKeys()
def doFilter(path)
    #path=sys.argv[1]
    tfile=ROOT.TFile.Open(path)
    ##
    keylist=tfile.GetListOfKeys()
    for key in keylist:
        name=key.GetName()
        if 'SBI' in name : continue
        h=tfile.Get(name)
        Nbins=h.GetNbinsX
        for ibin in range(0,Nbins+1):
            y=h.GetBinContent(ibin)
            yerr=h.GetBinError(ibin)
            
            if y <=0:
                h.SetBinContent(ibin,0.0)
                h.SetBinError(ibin,0.0)
        ROOT.gDirectory.WriteObject(h,name)
    ##
    tfile.Close()
if __name__ == '__main__':
    ##
    True
