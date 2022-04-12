import ROOT
import sys
import os
__HC_RATEPARAMTEST__SOARNSOAR__=os.getenv('__HC_RATEPARAMTEST__SOARNSOAR__')
sys.path.append(__HC_RATEPARAMTEST__SOARNSOAR__+'/DrawNLL/python')
from ReadValErr import ReadValErr
from array import array



def GetRP(year,region,param):

        myjob=ReadValErr()
        param_year=param+"_"+year
        #print param_year
        bst=""
        if 'Boosted' in param:
            bst="Boosted"
        if 'Resolved' in param:
            bst="Resolved"
        #inputpath=__HC_RATEPARAMTEST__SOARNSOAR__+"/MultiDimFit/"+year+"/model_indep/"+bst+"/"+region+"/"+param_year+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"                                                                                                                                          
        inputpath=__HC_RATEPARAMTEST__SOARNSOAR__+"/MultiDimFit/"+year+"/model_indep/"+bst+"/"+region+"/"+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"
        myjob.SetInput(inputpath,"limit")
        myjob.SetParam(param_year)
        myjob.ReadTree()

        xm=myjob.GetValue(0)
        x0=myjob.GetValue(1)
        xp=myjob.GetValue(2)
        myjob.CloseInput()
        return xm,x0,xp

def GetGraph(ym,y0,yp,idx):
        
if __name__ == '__main__':

    dict_data={
        '2016':{
            'topnorm_Boosted_GGF0':[],
            'topnorm_Boosted_GGF1':[],
            'topnorm_Boosted_VBF':[],

            'Wjetsnorm_Boosted_GGF0':[],
            'Wjetsnorm_Boosted_GGF1':[],
            'Wjetsnorm_Boosted_VBF':[],


            'topnorm_Resolved_GGF0':[],
            'topnorm_Resolved_GGF1':[],
            'topnorm_Resolved_VBF':[],

            'Wjetsnorm_Resolved_GGF0':[],
            'Wjetsnorm_Resolved_GGF1':[],
            'Wjetsnorm_Resolved_VBF':[],
        },

        '2017':{
            'topnorm_Boosted_GGF0':[],
            'topnorm_Boosted_GGF1':[],
            'topnorm_Boosted_VBF':[],

            'Wjetsnorm_Boosted_GGF0':[],
            'Wjetsnorm_Boosted_GGF1':[],
            'Wjetsnorm_Boosted_VBF':[],


            'topnorm_Resolved_GGF0':[],
            'topnorm_Resolved_GGF1':[],
            'topnorm_Resolved_VBF':[],

            'Wjetsnorm_Resolved_GGF0':[],
            'Wjetsnorm_Resolved_GGF1':[],
            'Wjetsnorm_Resolved_VBF':[],
        },
        '2018':{
            'topnorm_Boosted_GGF0':[],
            'topnorm_Boosted_GGF1':[],
            'topnorm_Boosted_VBF':[],

            'Wjetsnorm_Boosted_GGF0':[],
            'Wjetsnorm_Boosted_GGF1':[],
            'Wjetsnorm_Boosted_VBF':[],


            'topnorm_Resolved_GGF0':[],
            'topnorm_Resolved_GGF1':[],
            'topnorm_Resolved_VBF':[],

            'Wjetsnorm_Resolved_GGF0':[],
            'Wjetsnorm_Resolved_GGF1':[],
            'Wjetsnorm_Resolved_VBF':[],
        },

    }

    #par="topnorm_Boosted_GGF0_2016"
    #inputpath="../../MultiDimFit/2016/model_indep/Boosted/0/"+par+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"
    #region=sys.argv[1]
    region='0'
    #for year in dict_data:
    year='2016'
    bst="Boosted"

    dict_rp={
            'top':{
                    'ggf0':[],
                    'ggf_m':[],
                    'ggf_p':[],

                    'vbf0':[],
                    'vbf_m':[],
                    'vbf_p':[],

                    'untag0':[],
                    'untag_m':[],
                    'untag_p':[],
            },
            'Wjets':{
                    'ggf0':[],
                    'ggf_m':[],
                    'ggf_p':[],

                    'vbf0':[],
                    'vbf_m':[],
                    'vbf_p':[],

                    'untag0':[],
                    'untag_m':[],
                    'untag_p':[],
            }
    }
    dict_gr={
            'top':{},
            'Wjets':{}
    }
    ymax=max(ggf_p,untag_p,vbf_p)*1.1
    ymin=min(ggf_m,untag_m,vbf_m)*0.9
    
    for proc in ['top','Wjets']:
            for cat in ['GGF0','GGF1','VBF']:
                    param=proc+'norm_'+bst+'_'+cat
                    y_list=[]
                    eyl_list=[]
                    eyh_list=[]
                    x_list=[]
                    exl_list=[]
                    exh_list=[]
                    
                    for region in [0,1,2,3]:
                            x_list.append(region)
                            exl_list.append(0)
                            exh_list.append(0)
                            
                            region=str(region)
                            m, f, p=GetRP(year,region,param)
                            
                            y_list.append(f)
                            eyl_list.append(f-m)
                            eyh_list.append(p-f)
                            
                    dict_tgr[proc][cat]=ROOT.TGraphAsymmErrors(len(y_list), array('f',x_list), array('f',y_list),\
                                               array('f',exl_list),array('f',exh_list),\
                                               array('f',eyl_list),array('f',eyh_list))
                            

    c=ROOT.TCanvas()

    for proc in ['top','Wjets']:
            for cat in ['GGF0','GGF1','VBF']
    tgr_ggf.Draw()
    tgr_ggf.GetHistogram().SetMaximum(ymax)
    tgr_ggf.GetHistogram().SetMinimum(ymin)

    tgr_ggf.SetMarkerStyle(24)
    tgr_ggf.SetLineColor(1)

    tgr_vbf.Draw("P SAMES")
    tgr_vbf.SetMarkerStyle(24)
    tgr_vbf.SetMarkerColor(2)
    tgr_vbf.SetLineColor(2)


    c.SaveAs('temp.pdf')
