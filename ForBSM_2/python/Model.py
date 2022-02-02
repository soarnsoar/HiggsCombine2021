import ROOT

class Model:
    def __init__(self,rootfile,alias):
        self.rootfile=rootfile
        self.OpenFile()
        self.alias=alias
    

    def OpenFile(self):
        self.tfile=ROOT.TFile.Open(self.rootfile)

        #mA,tanb
    def Set_mA(self,mA):
        self.mA=mA
    def Set_tanb(self,tanb):
        self.tanb=tanb

    def Eval(self):
        
        h_xs_gg_H=self.tfile.Get("xs_gg_H")
        ##--Theoretical systematic
        h_xs_gg_H_scaleup=self.tfile.Get("xs_gg_H_scaleup")
        h_xs_gg_H_scaledown=self.tfile.Get("xs_gg_H_scaledown")
        
        h_xs_gg_H_pdfasup=self.tfile.Get("xs_gg_H_pdfasup")
        h_xs_gg_H_pdfasdown=self.tfile.Get("xs_gg_H_pdfasdown")
        
        
        h_br_H_WW=self.tfile.Get("br_H_WW")
        h_m_H=self.tfile.Get("m_H")

        _brlnuqq=0.1086*3*0.6741*2##constant

        _mH=h_m_H.GetBinContent(h_m_H.FindBin(self.mA,self.tanb))
        _br_H_WW=h_br_H_WW.GetBinContent(h_br_H_WW.FindBin(self.mA,self.tanb))
        _xs_gg_H=h_xs_gg_H.GetBinContent(h_xs_gg_H.FindBin(self.mA,self.tanb))
        _xs_gg_H_scaleup=h_xs_gg_H_scaleup.GetBinContent(h_xs_gg_H.FindBin(self.mA,self.tanb))
        _xs_gg_H_scaledown=h_xs_gg_H_scaledown.GetBinContent(h_xs_gg_H.FindBin(self.mA,self.tanb))
        _xs_gg_H_pdfasup=h_xs_gg_H_pdfasup.GetBinContent(h_xs_gg_H.FindBin(self.mA,self.tanb))
        _xs_gg_H_pdfasdown=h_xs_gg_H_pdfasdown.GetBinContent(h_xs_gg_H.FindBin(self.mA,self.tanb))


        _xsec_gghwwlnuqq=_xs_gg_H*_br_H_WW*_brlnuqq
        _xsec_gghwwlnuqq_scaleup=_xs_gg_H_scaleup*_br_H_WW*_brlnuqq
        _xsec_gghwwlnuqq_scaledown=_xs_gg_H_scaledown*_br_H_WW*_brlnuqq
        _xsec_gghwwlnuqq_pdfasup=_xs_gg_H_pdfasup*_br_H_WW*_brlnuqq
        _xsec_gghwwlnuqq_pdfasdown=_xs_gg_H_pdfasdown*_br_H_WW*_brlnuqq
        

        ##---done---##
        self.mH=_mH
        self.xsec_gghwwlnuqq=_xsec_gghwwlnuqq
        self.xsec_gghwwlnuqq_scaleup=_xsec_gghwwlnuqq_scaleup
        self.xsec_gghwwlnuqq_scaledown=_xsec_gghwwlnuqq_scaledown
        self.xsec_gghwwlnuqq_pdfasup=_xsec_gghwwlnuqq_pdfasup
        self.xsec_gghwwlnuqq_pdfasdown=_xsec_gghwwlnuqq_pdfasdown


