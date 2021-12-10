from ReadLimit import Limit
import os
import sys
#OptimizationLatino/python/Plotter.py
sys.path.insert(0,"OptimizationLatino/python")
from Plotter import *
from ReadYield import Yield
class CompareLimit:
    def __init__(self,title,year,IsInterference,ltype):
        
        self.title=title
        self.year=str(year)
        self.IsInterference=IsInterference
        if IsInterference:
            self.interference=""
        else:
            self.interference="_NoI"
        if "Asym" in ltype:
            self.ltype="AsymptoticLimits"
        elif "Hybrid" in ltype:
            self.ltype="HybridNewLimits"
        else:
            self.ltype=""
        #self.CollectLimit()
    def SetScore(self,score):
        self.score=score
    def CollectLimit(self):
        #os.system("combineTool.py -M CollectLimits -i "+self.filepath+" -o "+self.jsonpath)
        
        score=str(self.score)
        self.dirpath='/'.join([self.ltype,self.year,'model_indep',self.bst,score,"vbfonly","model_indep"+self.interference])
        self.dirpath="../"+self.dirpath
        #higgsCombineTest.AsymptoticLimits.mH1000
        self.filepath=self.dirpath+"/higgsCombine*.mH*.root"
        self.jsonpath=self.dirpath+"/limit.json"
        os.system("combineTool.py -M CollectLimits -i "+self.filepath+" -o "+self.jsonpath)
    def SetMassList(self,path,minmass=0,maxmass=100000):
        exec(open(path)) ##List_MX_VBF
        self.xlist=[]
        for mass in sorted(List_MX_VBF):
            if mass < minmass:continue
            if mass > maxmass:continue
            self.xlist.append(mass)
    def SetMyGraph(self):
        '''
        class myGraph:

    def __init__(self,xlist,ylist):
        self.xlist=xlist
        self.ylist=ylist
        self.N=len(xlist)
        self.tgr  = ROOT.TGraph(self.N)

    def SetName(self,Name):
        self.Name=Name
        self.tgr.SetTitle(self.Name)
        self.tgr.SetName(self.Name)
    def SetPoint(self):
        for idx in range(0,self.N):
            x=self.xlist[idx]
            y=self.ylist[idx]
            self.tgr.SetPoint(idx,x,y)

        '''
        ReadLimit=Limit()
        self.xlist_bst=[]
        self.xlist_res=[]

        self.ylist_bst=[]
        self.ylist_res=[]

        for mass in sorted(self.xlist):
            ReadLimit.LoadInOneStep(mass,self.year,True,self.IsInterference,self.score,self.ltype)
        
            if "Asym" in self.ltype:
                _limit=ReadLimit.ReadLimit('exp0')
            elif "Hybrid" in self.ltype:
                _limit=ReadLimit.ReadLimit('exp0')
            else:
                _limit=0
            if _limit>0:
                self.ylist_bst.append(_limit)
                self.xlist_bst.append(mass)
            else:
                print "Negavie limit@mass",mass,"Boosted",_limit
            ReadLimit.LoadInOneStep(mass,self.year,False,self.IsInterference,self.score,self.ltype)
            if "Asym" in self.ltype:
                _limit=ReadLimit.ReadLimit('exp0')
            elif "Hybrid" in self.ltype:
                _limit=ReadLimit.ReadLimit('exp0')
            else:
                _limit=0
            if _limit>0:
                self.ylist_res.append(_limit)
                self.xlist_res.append(mass)
            else:
                print "Negavie limit@mass",mass,"Resolved",_limit

        self.mygraph_bst=myGraph(self.xlist_bst,self.ylist_bst)
        self.mygraph_bst.SetName("Boosted")
        self.mygraph_bst.SetPoint()
        print self.xlist_bst
        print self.ylist_bst
        print "min(self.ylist_bst)",min(self.ylist_bst)
        self.mygraph_res=myGraph(self.xlist_res,self.ylist_res)
        self.mygraph_res.SetName("Resolved")
        self.mygraph_res.SetPoint()
        print self.xlist_res
        print self.ylist_res
        print "min(self.ylist_res)",min(self.ylist_res)
    def Draw(self,savepath):
        #c=ROOT.TCanvas()

        #self.mygraph_bst.tgr.Draw("")
        #self.mygraph_res.tgr.Draw("")
        myplotter=Plotter()
        myplotter.AddGraph(self.mygraph_bst.tgr,"Boosted",1)
        myplotter.AddGraph(self.mygraph_res.tgr,"Resolved",3)
        myplotter.SetMultiGraph()
        myplotter.SetCanvas()
        myplotter.SetXaxisTitle("M(X)")
        myplotter.SetYaxisTitle("xsec")
        myplotter.pad1.SetLogx()
        myplotter.pad1.SetLogy()
        myplotter.Draw()

        savedir='/'.join(savepath.split('/')[:-1])
        if savedir:
            os.system('mkdir -p '+savedir)
        #c.SaveAs(savepath)
        myplotter.Save(savepath)
    def DrawInOneStep(self,MXVBFpath,minmass,maxmass,score,savepath,doCollectLimit=True):
        self.SetMassList(MXVBFpath,minmass,maxmass)
        self.SetScore(score)
        if doCollectLimit:self.CollectLimit()
        self.SetMyGraph()
        self.Draw(savepath)
if __name__ == '__main__':
    ltype="Hybrid"

    for year in [2016,2017,2018]:
        #for year in [2016]:
        year=str(year)
        test=CompareLimit("Boosted vs Resolved "+year,year,False,ltype)
        scorelist=[]
        #for i in range(20):
        #    score=0.05*i
        #    scorelist.append(score)
        name="__".join([year])
        test.DrawInOneStep("etc/List_MX_VBF.py",0,10000,0.0,"Plot_BoostedResolved/"+name+"_"+ltype+".pdf",False)
        del test
