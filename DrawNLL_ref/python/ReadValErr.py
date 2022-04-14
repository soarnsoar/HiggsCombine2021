import ROOT
from array import array
#deltaNLL
class ReadValErr:
    def __init__(self):
        True
    def CloseInput(self):
        self.tfile.Close()
    def SetInput(self,filepath,TreeName):
        True
        self.tfile=ROOT.TFile.Open(filepath)
        self.ttree=self.tfile.Get(TreeName)
    def SetParam(self,paramname):
        self.paramname=paramname


    def ReadTree(self):
        

        data2={}
        xlist=[]



        for entry in self.ttree:
            exec("x=entry."+self.paramname)
            xlist.append(x)
        self.xlist=sorted(list(set(xlist)))
        
        self.xm=self.xlist[0]
        self.x0=self.xlist[1]
        self.xp=self.xlist[2]

    def GetValue(self,index):
        return self.xlist[index]
        
    def Draw(self,savepath):

        c=ROOT.TCanvas()
        #self.tgr2.SetTitle("x : "+self.paramname+", y : 2#Delta(NLL)")
        #self.tgr2.Draw()
        #self.tgr.Draw('same')
        #self.tgr.SetLineColor(2)
        c.SaveAs(savepath)
if __name__ == '__main__':
    #par="Wjetsnorm_Boosted_GGF0_2016"
    par="topnorm_Boosted_GGF0_2016"
    inputpath="../../MultiDimFit/2016/model_indep/Boosted/0/"+par+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"

    myjob=deltaNLL_Parser()

    myjob.SetInput(inputpath,"limit")

    myjob.SetParam(par)

    myjob.ReadTree()
