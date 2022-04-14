import sys
import os
#__HC_RATEPARAMTEST_COMMON__SOARNSOAR__
__HC_RATEPARAMTEST_COMMON__SOARNSOAR__=os.getenv('__HC_RATEPARAMTEST_COMMON__SOARNSOAR__')
sys.path.append(__HC_RATEPARAMTEST_COMMON__SOARNSOAR__+'/DrawNLL/python')
from deltaNLL_Parser import deltaNLL_Parser
if __name__ == '__main__':

    #Wjetsnorm_Boosted_2018
    for year in dict_data:
        myjob=deltaNLL_Parser()
        for param in sorted(dict_data[year]):

            param_year=param+"_"+year
            print param_year
            bst=""
            if 'Boosted' in param:
                bst="Boosted"
            if 'Resolved' in param:
                bst="Resolved"
            #inputpath=__HC_RATEPARAMTEST__SOARNSOAR__+"/MultiDimFit/"+year+"/model_indep/"+bst+"/"+region+"/"+param_year+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"
            inputpath=__HC_RATEPARAMTEST_COMMON__SOARNSOAR__+"/MultiDimFit/"+year+"/model_indep/"+bst+"/"+region+"/"+"/model_indep_NoI/higgsCombineTest.MultiDimFit.mH1000.root"
            myjob.SetInput(inputpath,"limit")
            myjob.SetParam(param_year)
            myjob.ReadTree()
            #myjob.GetValue(1)
            savepath="plots/"+param_year+".pdf"
            myjob.Draw(savepath)
