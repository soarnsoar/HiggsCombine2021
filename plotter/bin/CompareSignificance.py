import os
##---SetMainPathForThisModule
__ROOT_PLOTTER__SOARNSOAR_GIT__=os.getenv('__ROOT_PLOTTER__SOARNSOAR_GIT__')
##---Add Path
import sys
sys.path.append(__ROOT_PLOTTER__SOARNSOAR_GIT__+'/python')
from DrawTGraphs import DrawTGraphs
from GetYields import GetYields
import ROOT
import glob
import math
from array import array
from collections import OrderedDict


def CollectNevent(year,wtag,bkglist=[],masslist=[300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]):
    year=str(year)
    maindir=os.getenv('__HC_WTAGGER_COMPARE__SOARNSOAR__')
    
    dict_y={}
    ##--bkg first
    search='/'.join([maindir,wtag,'Datacards_'+year,'Datacard_M'+str(masslist[0]),'FullCutSR','WW_mass','shapes','*.root'])
    shape_output=glob.glob(search)[0]
    ybkg=GetYields(shape_output,bkglist)
    dict_y['bkg']=ybkg
    for mass in masslist:
        mass=str(mass)
        search='/'.join([maindir,wtag,'Datacards_'+year,'Datacard_M'+mass,'FullCutSR','WW_mass','shapes','*.root'])
        shape_output=glob.glob(search)[0]
        ##--ggf
        ggfname='ggH_hww'+mass+'_RelW002'
        yggf=GetYields(shape_output,[ggfname])
        ##--vbf
        vbfname='qqH_hww'+mass+'_RelW002'
        yvbf=GetYields(shape_output,[vbfname])

        dict_y[ggfname]=yggf
        dict_y[vbfname]=yvbf


    return dict_y
def GetTGraph(xlist,ylist):
    n=len(xlist)
    _gr=ROOT.TGraph(n,array('f',xlist),array('f',ylist))
    return _gr

def Draw(year,fvbf,wtaggers):

    year=str(year)
    dict_gr={}
    xlist=[300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    bkglist=[ 'DY', 'MultiBoson', 'Top','Wjets','QCD','WW','VH','qqWWqq','ggWW','ggH_hww','qqH_hww']

    for wtag in wtaggers:
        ylist=[]
        dict_y=CollectNevent(year,wtag,bkglist,xlist)
        _ybkg=dict_y['bkg']
        
        for mass in xlist:
            mass=str(mass)
            if fvbf=='ggfonly': _ysig=dict_y['ggH_hww'+mass+'_RelW002']
            if fvbf=='vbfonly': _ysig=dict_y['qqH_hww'+mass+'_RelW002']
            _significance=_ysig/math.sqrt(_ybkg)
            ylist.append(_significance)
            print _ybkg
            if mass=='1000':
                print '---',wtag,'---'
                print _ysig,_ybkg,_significance
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
    drawer=DrawTGraphs()
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
    os.system('mkdir -p plots/')
    drawer.Draw('plots/Significance__'+year+'__'+fvbf+'.pdf','RB')
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
        for year in [2016,2017,2018]:
        #for year in ['3yrs']:
            Draw(year,fvbf,wtaggers)
