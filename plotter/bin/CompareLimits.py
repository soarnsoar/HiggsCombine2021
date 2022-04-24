import os
##---SetMainPathForThisModule
__ROOT_PLOTTER__SOARNSOAR_GIT__=os.getenv('__ROOT_PLOTTER__SOARNSOAR_GIT__')
##---Add Path
import sys
sys.path.append(__ROOT_PLOTTER__SOARNSOAR_GIT__+'/python')
from DrawTGraphs import DrawTGraphs
from ReadLimit import ReadLimit
import ROOT
import glob
from array import array
from collections import OrderedDict
def CollectLimit(year,fvbf,wtag,masslist=[300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]):
    year=str(year)
    maindir=os.getenv('__HC_WTAGGER_COMPARE__SOARNSOAR__')
    #mass='1000'
    #HP/Datacards_2016/Datacard_M1000/FullCutSR/WW_mass/higgsCombineggfonly.AsymptoticLimits.mH1000.root

    limitlist=[]
    for mass in masslist:
        mass=str(mass)
        if year=='3yrs':
            search='/'.join([maindir,wtag,'higgsCombine*'+fvbf+'*mH'+mass+'.root'])
        else:
            search='/'.join([maindir,wtag,'Datacards_'+year,'Datacard_M'+mass,'FullCutSR','WW_mass','higgsCombine*'+fvbf+'*.root'])
        hc_output=glob.glob(search)[0]
        _limit=ReadLimit(hc_output)
        limitlist.append(_limit)
    return limitlist
def GetTGraph(xlist,ylist):
    n=len(xlist)
    _gr=ROOT.TGraph(n,array('f',xlist),array('f',ylist))
    return _gr

def Draw(year,fvbf,wtaggers):

    year=str(year)
    dict_gr={}
    xlist=[300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    for wtag in wtaggers:
        ylist=CollectLimit(year,fvbf,wtag,xlist)

        dict_gr[wtag]=GetTGraph(xlist,ylist)


        ##------Drawer------##
        #def AddGraph(self,h,name,color,linestyle):
        #def SetTitle(self,title):
        #def SetColorStyle(self):
        #def SetXTitle(self,xtitle):
        #def SetYTitle(self,ytitle):
        #def SetRangeX(self,xmin,xmax):
        #def UnzoomX(self):
        #def SetLegend(self,t="L"):
        #def SetMinMax(self):
        #def SetLogy(self,islogy=True):
        #def SetStats(self,showstat=True):
        #def ShowCMSLumi(self,showcms=True,lumi=0):
        #def Draw(self,SavePath,l="L"):##l ==legend location
    drawer=DrawTGraphs(year+'__'+fvbf)
    if str(year)=='2017':drawer.ShowCMSLumi(1,41.5)
    if str(year)=='2018':drawer.ShowCMSLumi(1,59.7)
    if str(year)=='3yrs':drawer.ShowCMSLumi(1,137)
    for wtag in wtaggers:
        _name=wtaggers[wtag]['name']
        _color=wtaggers[wtag]['color']
        _linestyle=wtaggers[wtag]['linestyle']
        drawer.AddGraph(dict_gr[wtag],_name,_color,_linestyle)
    if 'ggfonly' in fvbf:drawer.SetTitle('gg->X only')
    if 'vbfonly' in fvbf:drawer.SetTitle('vbfX only')

    drawer.SetLogy()
    drawer.SetLogx()
    drawer.SetRangeX(xlist[0]/2,xlist[-1]*2)
    os.system('mkdir -p plots/')
    drawer.Draw('plots/'+year+'__'+fvbf+'.pdf','R')
    del drawer.c
    del drawer



if __name__ == '__main__':

    wtaggers=OrderedDict([
        ('HP',{'name':'#tau_{21}','color':1,'linestyle':1}),
        ('HPddt',{'name':'#tau_{21} DDT','color':1,'linestyle':2}),

        ('WP5',{'name':'DeepAK8 WP5p0','color':2,'linestyle':1}),
        ('MDWP5',{'name':'DeepAK8MD WP5p0','color':2,'linestyle':2}),

        ('WP2p5',{'name':'DeepAK8 WP2p5','color':3,'linestyle':1}),
        ('MDWP2p5',{'name':'DeepAK8MD WP2p5','color':3,'linestyle':2}),

        ('WP1',{'name':'DeepAK8 WP1p0','color':4,'linestyle':1}),
        ('MDWP1',{'name':'DeepAK8MD WP1p0','color':4,'linestyle':2}),

        ('WP0p5',{'name':'DeepAK8 WP0p5','color':6,'linestyle':1}),
        ('MDWP0p5',{'name':'DeepAK8MD WP0p5','color':6,'linestyle':2}),
    ])
    for fvbf in ['ggfonly','vbfonly']:
        for year in [2016,2017,2018,'3yrs']:
        #for year in ['3yrs']:
            Draw(year,fvbf,wtaggers)
