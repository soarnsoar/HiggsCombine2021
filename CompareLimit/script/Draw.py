import sys
import os
__HC_VBFOPT__SOARNSOAR__=os.getenv("__HC_VBFOPT__SOARNSOAR__")
sys.path.append(__HC_VBFOPT__SOARNSOAR__+'/CompareLimit/python/')
from LimitReader import LimitReader
import ROOT
from array import array



def Draw(bst,year):
    year=str(year)
    name=bst+'__'+year
    if bst=="Boosted":
        masses=[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    if bst=="Resolved":
        masses=[200,210,230,250,270,300,350,400]

    #cuts=['nocut',0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    #cuts=[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    if bst=="Boosted":
        cuts=[0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98]
    else:
        cuts=[0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97,0.975,0.98,0.985,0.99,0.995]

    listmaxcut=[]

    ##---graph
    gr=ROOT.TGraph2D()


    idx=0
    for mass in masses:
        x=float(mass)
        maxpoint=0
        maxsensitive=1
        for cut in cuts:
            reader=LimitReader(mass,bst,year,'nocut')
            _limit0=reader.GetLimit()
            y=float(cut)
            reader=LimitReader(mass,bst,year,cut)
            _limit=reader.GetLimit()
            z=_limit0/_limit
            if z<1:z=0
            if z>maxsensitive: 
                maxsensitive=z
                maxpoint =cut
            #print mass,cut,_limit
            gr.SetPoint(idx,x,y,z)
            idx+=1
        listmaxcut.append(maxpoint)
    c=ROOT.TCanvas()
    #gr.Draw()
    ##----draw cut give max performance
    grmax=ROOT.TGraph(len(masses),array('f',masses),array('f',listmaxcut))
    grmax.SetLineColor(2)
    h=gr.GetHistogram()
    h.SetTitle('Exp.Limit(nocut)/Exp.Limit')
    h.GetXaxis().SetTitle("M(X) [GeV]")
    h.GetYaxis().SetTitle("isVBF score")
    h.Draw("colz")
    grmax.Draw('same')
    if bst=="Boosted":c.SetLogx()
    os.system('mkdir -p plots/')
    savepath='plots/'+name+'.pdf'
    c.SaveAs(savepath)
if __name__ == '__main__':
    #bst="Boosted"
    #year="2016"
    #bst=sys.argv[1]
    #year=sys.argv[2]
    bstlist=['Boosted','Resolved']
    yearlist=[2016,2017,2018]
    for year in yearlist:
        for bst in bstlist:
            Draw(bst,year)



    
