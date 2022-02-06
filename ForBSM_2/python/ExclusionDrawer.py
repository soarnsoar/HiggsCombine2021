import CombineHarvester.CombineTools.plotting as plot
import os
import sys
sys.path.append('python/')
from Read_R import Read_R
import ROOT
import sys
from array import array
from Read_grid import Read_grid

class ExDrawer:
    def SetFigureConf(self):
        color_basic=ROOT.kAzure
        self.dict_color={
            'exp+2':color_basic-4,
            'exp+1':color_basic-3,
            'exp0':color_basic-1,
            'exp-1':color_basic-3,
            'exp-2':color_basic-4,
        }
        self.dict_lumi={
            '2016':'35.9',
            '2017':'41.5',
            '2018':'59.7',
        }
        self.dict_modeltag={
            'mh125_13_withVBF':'M^{h^{125}}',
            'mh125_13':'M^{h^{125}}',
            'mh125_lc_13':'M^{h^{125}(#tilde{#chi})}',
            'mh125_lc_13_withVBF':'M^{h^{125}(#tilde{#chi})}',
            'mh125_ls_13':'M^{h^{125}(#tilde{#tau})}',
            'mh125_ls_13_withVBF':'M^{h^{125}(#tilde{#tau})}',
            'mh125_align_13':'M^{h^{125}}_{alignment}',
            'mh125_align_13_withVBF':'M^{h^{125}}_{alignment}',
            'mh125EFT_13':'M^{h}^{125}_{EFT}',
            'mh125EFT_13_withVBF':'M^{h}^{125}_{EFT}',
            'mh125EFT_lc_13':'M^{h}^{125}_{EFT}(#tilde{#chi})',
            'mh125EFT_lc_13_withVBF':'M^{h}^{125}_{EFT}(#tilde{#chi})',
        }



    def __init__(self,year,model):

        self.SetFigureConf()
        self.year=year
        self.model=model
        self.list_mA,self.list_tanb,self.list_mH=Read_grid()
        ##------
        self.xlist=[]
        dmA0=self.list_mA[1]-self.list_mA[0]
        self.xlist.append(self.list_mA[0]-dmA0/2)
        for i_mA in range(len(self.list_mA)-1):
            dmA=self.list_mA[i_mA+1] - self.list_mA[i_mA]
            self.xlist.append(self.list_mA[i_mA] + dmA/2 )
        dmA1 = self.list_mA[-1]+self.list_mA[-2]
        self.xlist.append(self.list_mA[-1]+dmA1/2)

        self.ylist=[]
        dtanb0=self.list_tanb[1]-self.list_tanb[0]
        self.ylist.append(self.list_tanb[0]-dtanb0/2)
        for i_tanb in range(len(self.list_tanb)-1):
            dtanb=self.list_tanb[i_tanb+1] - self.list_tanb[i_tanb]
            self.ylist.append(self.list_tanb[i_tanb] + dtanb/2 )
        dtanb1 = self.list_tanb[-1]+self.list_tanb[-2]
        self.ylist.append(self.list_tanb[-1]+dtanb1/2)
        
        self.xlist=array('d',sorted(self.xlist))
        self.ylist=array('d',sorted(self.ylist))
        #self.xlist=array('d',sorted(self.list_mA))
        #self.ylist=array('d',sorted(self.list_tanb))
        ##-----
        self.keylist=['exp-2','exp-1','exp0']

        ##----set histogram
        self.dict_h={}
        for key in self.keylist:
            self.dict_h[key]=ROOT.TH2D(key,key,len(self.xlist)-1, self.xlist, len(self.ylist)-1, self.ylist)
            self.Fill(key)

        ##--SetContour
        self.SetContuor()
    def Fill(self,key):
        for mA in self.list_mA:
            mA=str(mA)
            for tanb in self.list_tanb:
                tanb=str(tanb)
                #reader=Read_R(2016,'mh125_13',200,1.0,'exp0')            
                reader=Read_R(self.year,self.model,mA,tanb,key)            
                r=reader.GetR()
                self.dict_h[key].Fill(float(mA),float(tanb),r)
    def SetContuor(self):
        ##---extract contour---##
        #dict_h['exp+1'].Draw("colz")
        #https://root-forum.cern.ch/t/th2d-contour-drawing-problem/19090/13 
        self.myconts={}
        for key in self.keylist:
            self.dict_h[key].SetStats(0)
            self.dict_h[key].Smooth()
            self.dict_h[key].SetContour(1,array('d',[1]))
            self.dict_h[key].Draw("cont list")
            ROOT.gPad.Update()
            contslist=ROOT.gROOT.GetListOfSpecials().FindObject("contours")
            #print contslist.GetSize()
            if contslist==None:
                print "No Contours are extracted"
            else:
                self.myconts[key]=contslist.At(0).Clone()
                #myconts.append(contslist.At(0).Clone())
        self.mg=ROOT.TMultiGraph()
        for key in self.keylist:
            cont=self.myconts[key]
            print key,'--->contuor size',cont.GetSize()
            for i in range(cont.GetSize()):
                _this_cont=cont[i]
                _this_cont.SetFillColor(self.dict_color[key])
                _this_cont.SetLineColor(self.dict_color[key])
                
                if key=="exp0":
                    _this_cont.SetLineColor(1)
                    _this_cont.SetLineStyle(7)
                    _this_cont.SetLineWidth(3)
                self.mg.Add(_this_cont.Clone())
        #print "len(self.myconts['exp0'])",len(self.myconts['exp0'])
    def Draw(self):
        c1=ROOT.TCanvas("c","c",2000,1500)
        self.mg.Draw("afl")
        self.mg.GetHistogram().GetYaxis().SetRangeUser(0.6,10)
        self.mg.GetHistogram().GetYaxis().SetTitle("tan#beta")
        self.mg.GetHistogram().GetXaxis().SetTitle("m(A) [GeV]")
        plot.ModTDRStyle()
        ROOT.gPad.Update()
        #def DrawCMSLogo(pad, cmsText, extraText, iPosX, relPosX, relPosY, relExtraDY, extraText2='', cmsTextSize=0.8):
        plot.DrawCMSLogo(c1, 'CMS', "preliminary", 11,    0.045,   0.03,     1.0,          '',             0.8)
        #def DrawTitle(pad, text, align, textOffset=0.2,textSize=0.6)
        plot.DrawTitle(c1,"13 TeV, "+self.dict_lumi[str(self.year)]+" fb^{-1}",3, 0.2, 0.45)
        plot.DrawTitle(c1,self.dict_modeltag[self.model]+" Scenario",  1, 0.2, 0.45)
        ##--Add Legend
        #def PositionedLegend(width, height, pos, offset, horizontaloffset=None):
        legend = plot.PositionedLegend(0.3, 0.15, 3, 0.001,0.001)
        if 'exp0' in self.keylist:
            if 'obs' in self.keylist:
                if len(self.myconts['exp0'])>0:
                    legend.AddEntry(self.myconts['exp0'][0], "Expected", "L")
            else:
                if len(self.myconts['exp0'])>0:
                    legend.AddEntry(self.myconts['exp0'][0], "Expected", "F")
        if 'exp-1' in self.keylist:
            if len(self.myconts['exp-1'])>0:
                legend.AddEntry(self.myconts['exp-1'][0], "68% expected", "F")
        if 'exp-2' in self.keylist:
            if len(self.myconts['exp-2'])>0:
                legend.AddEntry(self.myconts['exp-2'][0], "95% expected", "F")

        legend.Draw()
        c1.SetLogy()
        c1.SetLogz()
        plotdir="plots/"
        os.system("mkdir -p "+plotdir)
        c1.SaveAs(plotdir+self.model+'__'+str(self.year)+".pdf")
        c1.SaveAs(plotdir+self.model+'__'+str(self.year)+".png")


if __name__ == '__main__':

    #reader=Read_R(2016,'mh125_13',200,1.0,'exp0')#    def __init__(self,year,model,mA,tanb,key):
    #r=reader.GetR()

    #print r
    #    def __init__(self,year,model):
    mydraw=ExDrawer('2016','mh125_13')
    mydraw.Draw()
