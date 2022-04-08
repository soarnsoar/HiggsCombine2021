import sys
import os
__HC_RATEPARAMTEST__SOARNSOAR__=os.getenv('__HC_RATEPARAMTEST__SOARNSOAR__')
sys.path.append(__HC_RATEPARAMTEST__SOARNSOAR__+'/DrawNLL/python')
from ReadValErr import ReadValErr
if __name__ == '__main__':
    region=sys.argv[1]

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

    for year in dict_data:
        myjob=ReadValErr()
        for param in sorted(dict_data[year]):

            param_year=param+"_"+year
            print param_year
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

