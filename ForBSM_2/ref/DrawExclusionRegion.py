import CombineHarvester.CombineTools.plotting as plot
import json
import os
#from numpy import array
import ROOT
import sys
from array import array    


##--lumi--##
dict_lumi={
    '2016':'35.9',
    '2017':'41.5',
    '2018':'59.7',
}
##---color---##
#color_basic=ROOT.kBlue
color_basic=ROOT.kAzure
dict_color={
    #'exp+2':color_basic-10,
    #'exp+1':color_basic-8,
    #'exp0':color_basic-5,
    #'exp-1':color_basic-8,
    #'exp-2':color_basic-10,
    ##--Azure
    'exp+2':color_basic-4,
    'exp+1':color_basic-3,
    'exp0':color_basic-1,
    'exp-1':color_basic-3,
    'exp-2':color_basic-4,
    
}

##---model tag---##
dict_modeltag={
    'mh125_13_withVBF':'M^{h^{125}}',
    'mh125_13':'M^{h^{125}}',
    'mh125_lc_13':'M^{h^{125}(\tilde \chi)}',
    'mh125_lc_13_withVBF':'M^{h^{125}(\tilde \chi)}',
    'mh125_ls_13':'M^{h^{125}(\tilde\tau)}',
    'mh125_ls_13_withVBF':'M^{h^{125}(\tilde\tau)}',
    'mh125_align_13':'M^{h^{125}}_{alignment}',
    'mh125_align_13_withVBF':'M^{h^{125}}_{alignment}',
    'mh125EFT_13':'M^{h}^{125}_{EFT}',
    'mh125EFT_13_withVBF':'M^{h}^{125}_{EFT}',
    'mh125EFT_lc_13':'M^{h}^{125}_{EFT}(\tilde \chi)',
    'mh125EFT_lc_13_withVBF':'M^{h}^{125}_{EFT}(\tilde \chi)',
}
if __name__ == '__main__':


    ##----Load grid of mA/tanb---##
    list_mA=[]
    list_tanb=[]
    list_mH=[]
    ##--read grid
    with open("config/mA_grid.json","r") as handle:
        list_mA=json.load(handle)
    ##--read grid
    with open("config/tanb_grid.json","r") as handle:
        list_tanb=json.load(handle)
        
    ##---year and model---##
    #year=2016
    #model="mh125_13_withVBF"
    year=sys.argv[1]
    model=sys.argv[2]
    model=model.rstrip('.root')
    print "----",year,model,"----"
    ##--load result
    result={}
    resultdir="Limits/"+model
    with open(resultdir+"/"+str(year)+".json","r") as handle:
        result=json.load(handle)
        
    #print sorted(list(list_mA))
    #print sorted(list(list_tanb))
    xlist=array('d',sorted(list_mA))
    ylist=array('d',sorted(list_tanb))
    #keylist=['exp-2','exp-1','exp0','exp+1','exp+2']
    keylist=['exp-2','exp-1','exp0']
    #keylist=['exp0']
    #keylist=['exp0','exp+1','exp+2','exp-1','exp-2']
    

    ##----2D Histogram for exclusion region
    dict_h={}
    for key in keylist:
        dict_h[key]=ROOT.TH2D(key,key,len(xlist)-1, xlist, len(ylist)-1, ylist)

    #print xlist
    #print ylist
    #h.Fill(250,1.1,3)
    #---Fill histogram
    for mA in list_mA:
        #continue
        mA=str(mA)
        
        for tanb in list_tanb:

            tanb=str(tanb)
            for key in keylist:
                if not mA in result : 
                    r=2000.
                elif not tanb in result[mA]:
                    r=2000.
                elif key in result[mA][tanb]:
                    r=result[mA][tanb][key]
                else:
                    #print "not found ",key,"mA",mA,"tanb",tanb
                    r=2000.
                if r<1: r=0
                dict_h[key].Fill(float(mA),float(tanb),r)

    c1=ROOT.TCanvas("c","c",2000,1500)


    ##---extract contour---##
    #dict_h['exp+1'].Draw("colz")
    #https://root-forum.cern.ch/t/th2d-contour-drawing-problem/19090/13
    myconts={}
    #myconts=[]
    for key in keylist:
        #continue
        dict_h[key].SetStats(0)
        dict_h[key].Smooth()
        dict_h[key].SetContour(1,array('d',[1]))
        dict_h[key].Draw("cont list")
        ROOT.gPad.Update()
        contslist=ROOT.gROOT.GetListOfSpecials().FindObject("contours")
        #print contslist.GetSize()
        if contslist==None:
            print "No Contours are extracted"
        else:
            myconts[key]=contslist.At(0).Clone()
            #myconts.append(contslist.At(0).Clone())

    mg=ROOT.TMultiGraph()
    for key in keylist:
        cont=myconts[key]
        for i in range(cont.GetSize()):
            #
            _this_cont=cont[i]
            _this_cont.SetFillColor(dict_color[key])
            _this_cont.SetLineColor(dict_color[key])
            
            if key=="exp0": 
                _this_cont.SetLineColor(1)
                _this_cont.SetLineStyle(7)
                _this_cont.SetLineWidth(3)
            mg.Add(_this_cont.Clone())
        
    ##---Draw Contours
    mg.Draw("afl")

    ##----Style of contours
    mg.GetHistogram().GetYaxis().SetRangeUser(0.6,10)
    mg.GetHistogram().GetYaxis().SetTitle("tan#beta")
    mg.GetHistogram().GetXaxis().SetTitle("m(A) [GeV]")
    plot.ModTDRStyle()
    ROOT.gPad.Update()
    #def DrawCMSLogo(pad, cmsText, extraText, iPosX, relPosX, relPosY, relExtraDY, extraText2='', cmsTextSize=0.8):
    plot.DrawCMSLogo(c1, 'CMS', "preliminary", 11,    0.045,   0.03,     1.0,          '',             0.8)

    #def DrawTitle(pad, text, align, textOffset=0.2,textSize=0.6)
    plot.DrawTitle(c1,"13 TeV, "+dict_lumi[str(year)]+" fb^{-1}",3, 0.2, 0.45)
    plot.DrawTitle(c1,dict_modeltag[model]+" Scenario",  1, 0.2, 0.45)
    ##--Add Legend
    #def PositionedLegend(width, height, pos, offset, horizontaloffset=None):
    legend = plot.PositionedLegend(0.3, 0.15, 3, 0.001,0.001)

    if 'exp0' in keylist:
        if 'obs' in keylist:
            legend.AddEntry(myconts['exp0'][0], "Expected", "L")
        else:
            legend.AddEntry(myconts['exp0'][0], "Expected", "F")
    if 'exp-1' in keylist:
        legend.AddEntry(myconts['exp-1'][0], "68% expected", "F")
    if 'exp-2' in keylist:
        legend.AddEntry(myconts['exp-2'][0], "95% expected", "F")

    legend.Draw()
    c1.SetLogy()
    c1.SetLogz()
    ##---Save Plots
    plotdir="plots/"
    os.system("mkdir -p "+plotdir)
    c1.SaveAs(plotdir+model+str(year)+".pdf")
    c1.SaveAs(plotdir+model+str(year)+".png")
