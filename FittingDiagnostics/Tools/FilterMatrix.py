#####---------Usage----####
### python FilterMatrix.py <rootfile> <covariance_fit_b || covariance_fit_s>
import ROOT
def ReadMatrix(filename,histoname):
    tfile=ROOT.TFile.Open(filename)
    #tfile.ls()
    #h2=tfile.Get("covariance_fit_b")
    #h2=tfile.Get("covariance_fit_s")
    #h2_b.SetDirectory(0)
    #h2_s.SetDirectory(0)
    h2=tfile.Get(histoname)
    h2.SetDirectory(0)
    tfile.Close()
    #return h2_b,h2_s
    return h2
def FilterNuisances(nui_list):
    ##---
    print "FilterNuisances"

def GetLabels(axis):
    #GetBinLabel (Int_t bin) const
    #GetNbins
    label_list=[]
    N=axis.GetNbins()
    for i in range(1,N+1):
        label=axis.GetBinLabel(i)
        #print label
        label_list.append(label)
    return label_list
def GetMostCorrelatedIndices(h,Nmax=30):
    ####-------To Get Most correlated nuisances
    N=h.GetXaxis().GetNbins()
    print N
    max_cor_list=[]
    ##---Get maximum ocrrelation coefficient for each nuisance
    for i in range(1,N+1):
        ##--x=i , y=j
        cor_max=0

        for j in range(1,N+1):
            #print i,j,"-->",h.GetBinContent(i,j)
            if i+j-1==N:continue ### skip if diagonal element
        
            this_cor=h.GetBinContent(i,j)
            #print i,j,"==>",this_cor
            if abs(this_cor)>cor_max: 
                cor_max=this_cor
        max_cor_list.append(cor_max)
    ###----Sort the correlation list
    sorted_max_cor_list=sorted(max_cor_list)
    ####--reverse it
    sorted_max_cor_list.reverse()
    ###---cut of correlation for Nmax nuisances
    cor_cut=sorted_max_cor_list[Nmax-1]
    print "cor_cut=",cor_cut
    ##--Get list of nuisances passing the cut
    nuisance_list=[]
    nuisanceidx_list=[]
    for i in range(1,N+1):
        this_maxcor=max_cor_list[i-1]
        if this_maxcor < cor_cut : continue
        label=h.GetXaxis().GetBinLabel(i)
        nuisance_list.append(label)
        nuisanceidx_list.append(i)
    return nuisanceidx_list,nuisance_list

def GetFilteredTH2D(h,nuisanceidx_list,nuisance_list):
    N=len(nuisanceidx_list)
    N_orig=h.GetXaxis().GetNbins()
    #TH2D (const char *name, const char *title, Int_t nbinsx, Double_t xlow, Double_t xup, Int_t nbinsy, Double_t ylow, Double_t yup)
    hnew=ROOT.TH2D(h.GetName(),h.GetTitle(),N,0,N,N,0,N)
    for i in range(0,N):
        for j in range(0,N):
            _i=nuisanceidx_list[i] ##_i= bin xindex of orig histogram
            _j=N_orig-nuisanceidx_list[j]+1 ## _j = bin yindex of orig histogram
            correl=h.GetBinContent(_i,_j)

            i_new= i+1
            j_new= j+1
            hnew.SetBinContent(i_new,j_new,correl)
    for i_new in range(1,N+1):
        j_new=i_new
        label=nuisance_list[i_new-1]
        hnew.GetXaxis().SetBinLabel(i_new,label)
        hnew.GetYaxis().SetBinLabel(j_new,label)
    hnew.SetStats(0)
    return hnew
if __name__ == '__main__':
    import sys
    filename=sys.argv[1]
    histoname=sys.argv[2]
    #h2=ReadMatrix("fitDiagnostics.Test.root","covariance_fit_b")
    h2=ReadMatrix(filename,histoname)
    nuisanceidx_list,nuisance_list=GetMostCorrelatedIndices(h2)
    #print nuisanceidx_list
    #print len(nuisanceidx_list)
    h2_filter=GetFilteredTH2D(h2,nuisanceidx_list,nuisance_list)
    c=ROOT.TCanvas()
    h2_filter.Draw("colz")
    h2_filter.GetXaxis().SetLabelSize(0.02)
    h2_filter.GetYaxis().SetLabelSize(0.02)
    c.SetMargin(0.2,0.2,0.2,0.2)#SetMargin (Float_t left, Float_t right, Float_t bottom, Float_t top)
    c.Modified()
    c.Update()
    newfilename=filename.replace('.root','')+"_"+histoname+".pdf"
    #c.SaveAs("temp.pdf")
    c.SaveAs(newfilename)
    ##--To check row index == column index
    #for i in range(len(xlabels)):
    #    print i,xlabels[i],ylabels[i]
