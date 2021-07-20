import ROOT
from copy import deepcopy
class ExpectedLimitBand():

    def __init__(self,N):
        ###----- Draw center with dotted line
        ###-----band with green(1sigma) / yellow(2sigma)

        self.N=N
        self.tgr_center=ROOT.TGraph(N) ## expected limit
        self.tgr_pm1=ROOT.TGraphAsymmErrors(N) ## +-1sigma
        self.tgr_pm2=ROOT.TGraphAsymmErrors(N) ## +-2sigma


        self.SetStyle() ## defined within this class
        
        ##--for drawing
        self.lumi=''
        self.sqrtS=13
        self.modeltag=''
    def SetPointX(self, x_list):
        self.x_list=deepcopy(x_list)

    def SetPointCenter(self, center_list):
        self.center_list=deepcopy(center_list)

    def SetPointPm1(self, p1_list,m1_list):
        self.p1_list=deepcopy(p1_list)
        self.m1_list=deepcopy(m1_list)

    def SetPointPm2(self, p2_list,m2_list):
        self.p2_list=deepcopy(p2_list)
        self.m2_list=deepcopy(m2_list)

    def SetStyle(self):
        self.tgr_pm1.SetLineWidth(2)
        self.tgr_pm2.SetLineWidth(2)
        self.tgr_center.SetLineStyle(2)
        self.tgr_center.SetLineColor(ROOT.kBlack)
        self.tgr_pm1.SetLineColor(ROOT.kGreen)
        self.tgr_pm2.SetLineColor(ROOT.kYellow)
        self.tgr_pm1.SetFillColor(ROOT.kGreen)
        self.tgr_pm2.SetFillColor(ROOT.kYellow)

    def GenerateTGraphs(self):
        for i in range(self.N):
            self.tgr_center.SetPoint(i,self.x_list[i], self.center_list[i])
            self.tgr_pm1.SetPoint(i,self.x_list[i], self.center_list[i])
            self.tgr_pm2.SetPoint(i,self.x_list[i], self.center_list[i])
            
            ##SetPointError (Double_t exl, Double_t exh, Double_t eyl, Double_t eyh)
            self.tgr_pm1.SetPointError(i, 0, 0, self.center_list[i]-self.m1_list[i], self.p1_list[i]-self.center_list[i])
            self.tgr_pm2.SetPointError(i, 0, 0, self.center_list[i] - self.m2_list[i]  , self.p2_list[i]-self.center_list[i])


    def SetLumi(self,lumi):
        self.lumi=lumi
    def SetSqrtS(self,sqrtS):
        self.sqrtS=sqrtS
    def SetModelTag(self,modeltag):
        self.modeltag=modeltag
    def Draw(self):##You Don't Need to use this


        import tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        self.tcanvas = ROOT.TCanvas( 'tcanvas', 'distro',800,800)

        self.tcanvas.SetLogy()
        self.frame = ROOT.TH2F("frame","",self.N,min(self.x_list),max(self.x_list),100,min(self.m2_list)*0.1,max(self.p2_list)*10)
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

        self.leg.AddEntry(self.tgr_center,     "Expected Limit","l")
        self.leg.AddEntry(self.tgr_pm1, "Expected #pm 1#sigma","f");
        self.leg.AddEntry(self.tgr_pm2, "Expected #pm 2#sigma","f");
        
        self.leg.Draw('same')
        self.drawmodeltag= ROOT.TLatex(300,50, self.modeltag)#DrawLatex (Double_t x, Double_t y, const char *text)
        self.drawmodeltag.Draw("same")




        self.tgr_pm2.Draw('3 same')
        self.tgr_pm1.Draw('3 same')
        self.tgr_center.Draw('l same')




        
                
    def Print(self):
        ##--print objects
        print "tgr_center"
        print "tgr_pm1"
        print "tgr_pm2"
        print "N=",N
        print "--functions--"
        print "SetPointX(self, x_list)"
        print "SetPointCenter(self, center_list)"
        print "SetPointPm1(self, p1_list,m1_list)"
        print "SetPointPm2(self, p2_list,m2_list)"
        print "SetStyle(self)"
        print "GenerateTGraphs(self)"
if __name__ == '__main__':
    ##--test and how to run
    masslist=[100,300,500,700,900,1500]
    center_list=[1,2,3,4,5,6]

    p1_list=[1.1,2.1,3.1,4.1,5.1,6.1]
    p2_list=[1.2,2.2,3.2,4.2,5.2,6.2]

    m1_list=[1-0.1,2-0.1,3-0.1,4-0.1,5-0.1,6-0.1]
    m2_list=[1-0.2,2-0.2,3-0.2,4-0.2,5-0.2,6-0.2]

    test_band=ExpectedLimitBand(len(masslist))
    test_band.SetPointX(masslist)
    test_band.SetPointCenter(center_list)
    test_band.SetPointPm1(p1_list,m1_list)
    test_band.SetPointPm2(p2_list,m2_list)
    test_band.GenerateTGraphs()
    test_band.Draw()
    test_band.tcanvas.SaveAs("test.pdf")
