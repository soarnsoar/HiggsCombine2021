import sys
import os
__HC_MEKDOPT__SOARNSOAR__=os.getenv("__HC_MEKDOPT__SOARNSOAR__")
sys.path.append(__HC_MEKDOPT__SOARNSOAR__+'/CompareLimit/python/')
from LimitReader import LimitReader
import ROOT
from array import array



def GetXY(bst,year):
    year=str(year)
    name=bst+'__'+year
    if bst=="Boosted":

        masses=[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
        #masses=[200,210,230,250,270,300,350]+[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    if bst=="Resolved":
        masses=[200,210,230,250,270,300,350]+[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    #masses=[200,210,230,250,270,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    #cuts=['nocut',0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    #cuts=[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    masses=[160,180,200,210,230,250,270,300,350]+[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]

    ##---graph


    limitlist=[]
    idx=0
    for mass in masses:
        x=float(mass)
        reader=LimitReader(mass,bst,year,'nocut')
        _limit0=reader.GetLimit()
        limitlist.append(_limit0)
    return masses,limitlist

def Draw(year):

    xbst,ybst=GetXY("Boosted",year)
    xres,yres=GetXY("Resolved",year)
    c=ROOT.TCanvas()
    #gr.Draw()
    ##----draw cut give max performance
    grbst=ROOT.TGraph(len(xbst),array('f',xbst),array('f',ybst))
    grres=ROOT.TGraph(len(xres),array('f',xres),array('f',yres))
    _ymax=max(ybst+yres)
    _ymin=min(ybst+yres)
    grbst.SetMaximum(_ymax)
    grbst.SetMinimum(_ymin)
    grres.SetMaximum(_ymax)
    grres.SetMinimum(_ymin)
    grres.Draw()    
    grbst.Draw('same')

    grres.SetLineColor(2)
    os.system('mkdir -p plots_nocut/')
    savepath='plots_nocut/Boosted_Resolved'+str(year)+'.pdf'
    c.SetLogy()
    c.SaveAs(savepath)
if __name__ == '__main__':
    #bst="Boosted"
    #year="2016"
    #bst=sys.argv[1]
    #year=sys.argv[2]
    bstlist=['Boosted','Resolved']
    yearlist=[2016,2017,2018]
    for year in yearlist:
        Draw(year)



    
