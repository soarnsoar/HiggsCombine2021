import sys
sys.path.insert(0,'Tools')
sys.path.insert(0,'../Tools')

from ExpectedLimitBand import ExpectedLimitBand
import ROOT

def GetLimitListsByPath(path,xlist):
    #AsymptoticLimits/2016/model_indep/Boosted/floating/model_indep/
    tfile=ROOT.TFile.Open(path)
    gr_exp0=tfile.Get("TGraph_exp0")
    gr_exp_p1=tfile.Get("TGraph_exp_p1")
    gr_exp_p2=tfile.Get("TGraph_exp_p2")
    gr_exp_m1=tfile.Get("TGraph_exp_m1")
    gr_exp_m2=tfile.Get("TGraph_exp_m2")


    list_exp0=[]
    list_exp_p1=[]
    list_exp_p2=[]
    list_exp_m1=[]
    list_exp_m2=[]
    for i in range(len(xlist)):
        x=xlist[i]
        list_exp0.append(gr_exp0.Eval(x))
        list_exp_p1.append(gr_exp_p1.Eval(x))
        list_exp_p2.append(gr_exp_p2.Eval(x))
        list_exp_m1.append(gr_exp_m1.Eval(x))
        list_exp_m2.append(gr_exp_m2.Eval(x))

    return list_exp0,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2

def GetPath(year,interference,fvbf,region):
    path="../AsymptoticLimits/"+str(year)+"/model_indep/"+region+"/"+fvbf+"/model_indep"
    if interference==False:
        path+="_NoI"
    path+="/indep.root"
    return path
def GetLimitList(xlist,year,interference,fvbf,region):
    path=GetPath(year,interference,fvbf,region)

    list_exp0,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitListsByPath(path,xlist)
    return list_exp0,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2

def getlumi(year):
    lumi=1.
    if str(year)=='2016':
        lumi=35.9

    elif str(year)=='2017':
        lumi=41.5

    elif str(year)=='2018':
        lumi=59.7
    return lumi
def Run(masslist,year,interference,fvbf,region):

    center_list,p1_list,p2_list,m1_list,m2_list=GetLimitList(masslist,year,interference,fvbf,region)
    print masslist
    band=ExpectedLimitBand(len(masslist))
    band.SetPointX(masslist)
    band.SetPointCenter(center_list)
    band.SetPointPm1(p1_list,m1_list)
    band.SetPointPm2(p2_list,m2_list)
    band.GenerateTGraphs()
    
    band.lumi=str(getlumi(year))
    band.modeltag="ggfonly"
    band.Draw()
    band.tcanvas.SaveAs("test.pdf")
if __name__ == '__main__':
    masslist=[400,500,600,700,800,900,1000,1200,1500,2000,2500,3000,4000,5000]
    year=2016
    interference=False
    fvbf='ggfonly'
    region="Boosted"
    

    Run(masslist,year,interference,fvbf,region)
