import ROOT
from array import array
#deltaNLL
class deltaNLL_Parser:
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

    def GetIntersectionTo1(self,x1,x2,y1,y2):
        ##y1 ---1 ----y2
        ##x1 ---?-----x2
        ## (1-y1)/(y2-1)=(x-x1)/(x2-x)
        ## (1-y1)(x2-x)=(x-x1)(y2-1)
        ## (1-y1)x2+(y2-1)x1 = (y2-1+1-y1)x
        ##x=[x2-x1 + x1y2 - x2y1]/(y2-y1)
        ##x=(    )
        x=(x2-x1+x1*y2 -x2*y1)/(y2-y1)
        return x
    def ReadTree(self):
        

        data2={}
        for entry in self.ttree:
            exec("x=entry."+self.paramname)
            y=2*entry.deltaNLL
            if y <4 :
                data2[x]=y
                if y==0:self.x0=x

        print sorted(data2)
        #print self.xlist
        #print self.ylist
        xlist2=[]
        ylist2=[]
        xlist=[]
        ylist=[]
        xmp=[]
        for i,x in enumerate(sorted(data2)):
            y=data2[x]
            xlist2.append(x)
            ylist2.append(y)
            
            if y<1:
                xlist.append(x)
                ylist.append(y)

            ##---------##
            if i>len(data2)-2:
                continue            
            xx=sorted(data2)[i+1]
            yy=data2[xx]
            if (y-1)*(yy-1)<0:
                xmp.append(x)
                xmp.append(xx)
            
        #print xlist[0],xlist[-1]
        self.tgr2=ROOT.TGraph(len(xlist2) , array('f',xlist2), array('f',ylist2))
        self.tgr=ROOT.TGraph(len(xlist) , array('f',xlist), array('f',ylist))
        xm1=xmp[0]
        xm2=xmp[1]
        #GetIntersectionTo1(x1,x2,y1,y2)
        self.xm=self.GetIntersectionTo1(xm1,xm2,self.tgr2.Eval(xm1),self.tgr2.Eval(xm2))
        xp1=xmp[2]
        xp2=xmp[3]
        self.xp=self.GetIntersectionTo1(xp1,xp2,self.tgr2.Eval(xp1),self.tgr2.Eval(xp2))

        xlist.insert(0,self.xm)
        ylist.insert(0,self.tgr2.Eval(self.xm))
        xlist.append(self.xp)
        ylist.append(self.tgr2.Eval(self.xp))

        self.tgr=ROOT.TGraph(len(xlist) , array('f',xlist), array('f',ylist))


        print self.xm,self.x0,self.xp
        if abs(self.tgr2.Eval(self.xm)-1)>0.01:
            print "low 2dnll->",self.tgr2.Eval(self.xm)
        if abs(self.tgr2.Eval(self.xp)-1)>0.01:
            print "low 2dnll->",self.tgr2.Eval(self.xp)
        self.sigma=(self.xp-self.xm)/2.
    
    
    def GetFitValue(self,direction):
        if direction==-1:
            return self.xm
        if direction==0:
            return self.x0
        if direction==1:
            return self.xp
    def Draw(self,savepath):

        c=ROOT.TCanvas()
        self.tgr2.SetTitle("x : "+self.paramname+", y : 2#Delta(NLL)")
        self.tgr2.Draw()
        self.tgr.Draw('same')
        self.tgr.SetLineColor(2)
        c.SaveAs(savepath)
if __name__ == '__main__':
    #par="Wjetsnorm_Boosted_GGF0_2016"
    par="topnorm_Boosted_GGF0_2016"
    inputpath="../../MultiDimFit/2016/model_indep/Boosted/0/"+par+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"

    myjob=deltaNLL_Parser()

    myjob.SetInput(inputpath,"limit")

    myjob.SetParam(par)

    myjob.ReadTree()
