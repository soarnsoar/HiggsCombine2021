import ROOT
#def GetLimitListsByPath(path,xlist):
from DrawIndepLimit import GetLimitListsByPath
from copy import deepcopy
import sys
sys.path.insert(0,"../Tools/")


def GetPath(year,interference,fvbf,region,dnn):
    #HiggsCombine2021/script
    if dnn==False:
        maindir="HiggsCombine2021"
    else:
        maindir="HiggsCombine2021_DNN"
    path="../../"+maindir+"/AsymptoticLimits/"+str(year)+"/model_indep/"+region+"/"+fvbf+"/model_indep"
    if interference==False:
        path+="_NoI"
    path+="/indep.root"
    return path
def GetLimitList(xlist,year,interference,fvbf,region,dnn):
    path=GetPath(year,interference,fvbf,region,dnn)
    list_exp0,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitListsByPath(path,xlist)
    return list_exp0,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2


class CompareLimit():
    def __init__(self,x_list,list_ylist,list_name):
        print ""
        self.Set(x_list,list_ylist,list_name)
        self.dict_color={
            0:1,
            1:2,
            2:4,
            3:6,
        }
        self.MakeTgr()
        self.year=""
    def Set(self,x_list,list_ylist,list_name):
        self.x_list=deepcopy(x_list)
        self.list_name=deepcopy(list_name)
        self.tgr_list=[]
        self.y_dict={}

        print "len(list_ylist)",len(list_ylist)
        print "len(list_name)",len(list_name)
        for i in range(len(self.list_name)):
            self.y_dict[list_name[i]]=list_ylist[i]
        #self.list_name=deepcopy(list_name)
        self.ymin=999999999999
        self.ymax=-99999999999
        for ylist in list_ylist:
            for y in ylist:
                if y>=self.ymax : self.ymax=y
                if y<self.ymin : self.ymin=y


    def MakeTgr(self):
        for i in range(len(self.list_name)):
            self.tgr_list.append(ROOT.TGraph(len(self.x_list)).Clone())
            name=self.list_name[i]
            self.tgr_list[i].SetTitle(name)
            self.tgr_list[i].SetName(name)
            color=self.dict_color[i]
            self.tgr_list[i].SetLineColor(color)
            for j in range(len(self.x_list)):
                x=self.x_list[j]
                y=self.y_dict[name][j]
                self.tgr_list[i].SetPoint(j,x, y)
                

    def Run(self):
        import tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        self.tcanvas = ROOT.TCanvas( 'tcanvas', 'distro',800,800)

        self.tcanvas.SetLogy()
        self.frame = ROOT.TH2F("frame","",len(self.x_list),min(self.x_list),max(self.x_list),100,self.ymin*0.1,self.ymax*10)
        self.frame.GetYaxis().SetTitleSize(0.05)
        self.frame.GetYaxis().SetLabelSize(0.03)
        self.frame.SetXTitle("m_{X} (GeV)")
        self.frame.GetXaxis().SetTitleSize(0.035)
        self.frame.GetXaxis().SetLabelSize(0.03)
        self.frame.GetXaxis().SetTitleOffset(1.5)

        self.frame.Draw()
        self.frame.SetStats(0)

        import CMS_lumi as CMS_lumi

        CMS_lumi.lumi_13TeV=self.lumi+' fb^{-1}'
        CMS_lumi.writeExtraText=1
        CMS_lumi.extraText="Preliminary"
        CMS_lumi.relPosX = 0.12
        CMS_lumi.lumi_sqrtS = self.sqrtS
        iPeriod = 4
        iPos  = 0
        CMS_lumi.CMS_lumi(self.tcanvas, iPeriod, iPos)


        self.leg= ROOT.TLegend(0.5,0.75,0.95,0.94)
        self.leg.SetFillColor(0)
        self.leg.SetBorderSize(1)
        self.leg.SetTextFont(8)
        self.leg.SetTextSize(20)


        for i in range(len(self.list_name)):
            name=self.list_name[i]
            #self.leg.AddEntry(self.tgr_center,     "Expected Limit","l")
            #self.leg.AddEntry(self.tgr_pm1, "Expected #pm 1#sigma","f");
            #self.leg.AddEntry(self.tgr_pm2, "Expected #pm 2#sigma","f");
            self.leg.AddEntry(self.tgr_list[i],name,'l')
        self.leg.Draw('same')
        self.drawmodeltag= ROOT.TLatex(600,10, self.modeltag)#DrawLatex (Double_t x, Double_t y, const char *text)                                                                                          
        self.drawmodeltag.Draw("same")




        for i in range(len(self.list_name)):
            #self.tgr_center.Draw('l same')
            self.tgr_list[i].Draw('l same')
        

        self.tcanvas.SaveAs("_".join(self.list_name+[self.modeltag,str(self.year)])+".pdf")
    

def Compare_DNN_CB():
    ##
    masslist=[400,500,600,700,800,900,1000,1200,1500,2000,2500,3000,4000,5000]
    dict_lumi={
        2016:'35.9',
        2017:'41.5',
        2018:'59.7'
    }
    interference=False
    fvbf='vbfonly'
    region="Boosted"

    for year in dict_lumi:
        list_exp0_dnn,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitList(masslist,year,interference,fvbf,region,True)
        list_exp0_cb,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitList(masslist,year,interference,fvbf,region,False)
        
        print list_exp0_dnn
        print list_exp0_cb
        list_ylist=[list_exp0_dnn,list_exp0_cb]
        list_name=["DNN","CB"]
        myCompare=CompareLimit(masslist,list_ylist,list_name) #(self,x_list,list_ylist,list_name)
        myCompare.lumi=dict_lumi[year]
        myCompare.sqrtS="13"
        myCompare.year=str(year)
        myCompare.modeltag=fvbf
        myCompare.Run()
        del myCompare
def Compare_I_NoI(dnn=True):
    masslist=[400,500,600,700,800,900,1000,1200,1500,2000,2500,3000,4000,5000]
    dict_lumi={
        2016:'35.9',
        2017:'41.5',
        2018:'59.7'
    }
    interference=False
    fvbf='vbfonly'
    region="Boosted"

    for year in dict_lumi:
        list_exp0_I,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitList(masslist,year,True,fvbf,region,dnn)
        list_exp0_NoI,list_exp_p1,list_exp_p2,list_exp_m1,list_exp_m2=GetLimitList(masslist,year,False,fvbf,region,dnn)
        
        print list_exp0_I
        print list_exp0_NoI
        list_ylist=[list_exp0_I,list_exp0_NoI]
        list_name=["with_I","NoI"]
        myCompare=CompareLimit(masslist,list_ylist,list_name) #(self,x_list,list_ylist,list_name)
        myCompare.lumi=dict_lumi[year]
        myCompare.sqrtS="13"
        myCompare.year=str(year)
        myCompare.modeltag=fvbf

        myCompare.Run()
        del myCompare
if __name__ == '__main__':
    Compare_I_NoI(False)
