import sys
import os
__HC_VBFOPT__SOARNSOAR__=os.getenv("__HC_VBFOPT__SOARNSOAR__")
sys.path.append(__HC_VBFOPT__SOARNSOAR__+'/CompareLimit/python/')
from LimitReader import LimitReader
import ROOT
from array import array


def GetOptCut(cuts,listmaxcut,dict_gr,name):
    ###---Condition
    ##1) <increase/max(increase)> (avg for mass) is maximised
    ##2) increase > 1 ( cut must improve sensitivity )
    dict_IncreaseOverMax={}
    dict_Increase={}
    ListAvgIncreaseOverMax=[]
    MaxAvgIncreaseOverMax=-1
    i_OptCut=-1
    OptCut=0
    for ic,cut in enumerate(cuts):
        dict_IncreaseOverMax[cut]=[]
        dict_Increase[cut]=[]
        SkipThisCut=False
        SumOfIncreaseOverMax=0
        for im,mass in enumerate(sorted(dict_gr)):
            maxcut=listmaxcut[im]
            increase=dict_gr[mass].Eval(cut)
            maxincrease=dict_gr[mass].Eval(maxcut)
            dict_IncreaseOverMax[cut].append(increase/maxincrease)
            dict_Increase[cut].append(increase)
            if increase<1:
                SkipThisCut=True
                break
            SumOfIncreaseOverMax+=increase/maxincrease

        if not SkipThisCut:
            AvgIncreaseOverMax=SumOfIncreaseOverMax/len(dict_gr)
        else:
            AvgIncreaseOverMax=0
            continue
        ListAvgIncreaseOverMax.append(AvgIncreaseOverMax)
        if AvgIncreaseOverMax>MaxAvgIncreaseOverMax:
            OptCut=cut
            i_OptCut=ic
            MaxAvgIncreaseOverMax=AvgIncreaseOverMax
    #print 'OptCut=',OptCut
    #print 'MaxAvgIncreaseOverMax',MaxAvgIncreaseOverMax
    #print '<List IncreaseOverMax>'
    #print dict_IncreaseOverMax[OptCut]
    #print '<List Increase>'
    #print dict_Increase[OptCut]

    ##----SaveALL Shapes
    for im,mass in enumerate(sorted(dict_gr)):
        
        c2=ROOT.TCanvas("c__"+name,"c__"+name,800,600)
        dict_gr[mass].Draw()
        dict_gr[mass].SetTitle('')
        dict_gr[mass].GetXaxis().SetTitle('isVBF Cut')
        dict_gr[mass].GetYaxis().SetTitle('Increase of Sensitivity')

        tline=ROOT.TLine(OptCut,0,OptCut,dict_gr[mass].GetYaxis().GetXmax())#TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        tline.SetLineStyle(2)
        tline.SetLineColor(2)
        
        tline.Draw('same')
        _leg=ROOT.TLegend(0.1,0.7,0.3,0.9)#x,y,x,y
        _leg.AddEntry(tline,'Opt. Cut','l')
        _leg.Draw()
        savedir='plots/cut_increase/'+name
        os.system('mkdir -p '+savedir)
        c2.SaveAs(savedir+'/'+str(mass)+'.pdf')
        del c2
        del tline
        del _leg

    ##----x : mass y:ratio to maximum
    masslist=sorted(dict_gr)
    ratio_to_max_list=[]
    for im, mass in enumerate(sorted(dict_gr)):
        dict_IncreaseOverMax[OptCut]
        maxcut=listmaxcut[im]
        increase=dict_gr[mass].Eval(OptCut)
        maxincrease=dict_gr[mass].Eval(maxcut)
        ratio_to_max=increase/maxincrease
        ratio_to_max_list.append(ratio_to_max)
    ##--Graph
    gr_ratio=ROOT.TGraph(len(dict_gr),array('f',masslist),array('f',ratio_to_max_list))
    c3=ROOT.TCanvas("c__"+name,"c__"+name,800,600)
    gr_ratio.Draw()
    gr_ratio.SetTitle('')
    gr_ratio.GetXaxis().SetTitle("M(X) [GeV]")
    gr_ratio.GetYaxis().SetTitle("Ratio to max. increase")

    tline=ROOT.TLine(gr_ratio.GetXaxis().GetXmin(),MaxAvgIncreaseOverMax,gr_ratio.GetXaxis().GetXmax(),MaxAvgIncreaseOverMax)#TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
    tline.SetLineStyle(2)
    tline.SetLineColor(2)
    tline.Draw('same')
    _leg=ROOT.TLegend(0.1,0.9,0.3,1.0)#x,y,x,y                                                                                                                                
    _leg.AddEntry(tline,'Avg. = '+str(round(MaxAvgIncreaseOverMax,2)),'l')
    _leg.Draw()

    savedir='plots/ratio_to_maxincrease/'
    os.system('mkdir -p '+savedir)
    c3.SaveAs(savedir+'/'+name+'.pdf')
    return OptCut,MaxAvgIncreaseOverMax

def Draw(bst,year):
    year=str(year)
    name=bst+'__'+year
    if bst=="Boosted":
        masses=[400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]
    if bst=="Resolved":
        masses=[200,210,230,250,270,300,350,400]

    #cuts=['nocut',0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    #cuts=[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
    if bst=="Boosted":
        True
        cuts=[0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99]
        #cuts=[0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98]
    else:
        #cuts=[0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97,0.975,0.98,0.985,0.99,0.995]
        #cuts=[0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
        cuts=[0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99]
    listmaxcut=[]

    ##---graph
    gr=ROOT.TGraph2D()


    idx=0
    dict_gr={} ## x: cut y:sensitivity increase
    for mass in masses:
        #print mass
        x=float(mass)
        maxpoint=0
        maxincrease=1
        increases=[]
        for cut in cuts:
            reader=LimitReader(mass,bst,year,'nocut')
            _limit0=reader.GetLimit()
            y=float(cut)
            reader=LimitReader(mass,bst,year,cut)
            _limit=reader.GetLimit()
            z=_limit0/_limit
            #if z<1:z=0
            if z>maxincrease: 
                maxincrease=z
                maxpoint =cut
            increases.append(z)
            #print mass,cut,_limit
            gr.SetPoint(idx,x,y,z)
            idx+=1
        listmaxcut.append(maxpoint)
        dict_gr[mass]=ROOT.TGraph(len(cuts),array('f',cuts),array('f',increases))
    c=ROOT.TCanvas()
    #gr.Draw()
    ##----draw cut give max performance
    optcut,MaxAvgIncreaseOverMax=GetOptCut(cuts,listmaxcut,dict_gr,bst+'__'+year)
    listoptcut=[optcut]*len(masses)
    #print listoptcut
    gropt=ROOT.TGraph(len(masses),array('f',masses),array('f',listoptcut))
    gropt.SetLineColor(2)

    grmax=ROOT.TGraph(len(masses),array('f',masses),array('f',listmaxcut))
    grmax.SetLineColor(2)
    h=gr.GetHistogram()
    h.SetTitle('Exp.Limit(nocut)/Exp.Limit')
    h.GetXaxis().SetTitle("M(X) [GeV]")
    h.GetYaxis().SetTitle("isVBF score")
    h.Draw('colz')
    gropt.Draw('same')
    if bst=="Boosted":c.SetLogx()
    ##---Add Box
    txtbox=ROOT.TPaveText(masses[0],cuts[0],masses[int(len(masses)/3)],cuts[int(len(cuts)/5)])#TPaveText (Double_t x1, Double_t y1, Double_t x2, Double_t y2, Option_t *option="br")
    txtbox.AddText("Opt.Cut="+str(optcut))
    txtbox.Draw()
    #c.SetLogz()
    os.system('mkdir -p plots/')
    savepath='plots/'+name+'.pdf'
    c.SaveAs(savepath)


if __name__ == '__main__':

    bstlist=['Boosted','Resolved']
    yearlist=[2016,2017,2018]
    for year in yearlist:
        for bst in bstlist:
            print '-----------'
            print year,bst
            Draw(bst,year)



    
