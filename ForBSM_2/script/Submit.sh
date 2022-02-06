ARR_year=(2016 2017 2018)
#ARR_year=(2017 2018)

'''
mh125EFT_13_withVBF.root     mh125_align_13_withVBF.root  thdm_type1_0.1cba.root       thdm_type1_mH400.root        thdm_type2_mH200.root        thdm_type2_mH500.root
mh125EFT_lc_13_withVBF.root  mh125_lc_13_withVBF.root     thdm_type1_mH200.root        thdm_type1_mH500.root        thdm_type2_mH300.root        
mh125_13_withVBF.root        mh125_ls_13_withVBF.root     thdm_type1_mH300.root        thdm_type2_0.1cba.root       thdm_type2_mH400.root        

'''
for year in ${ARR_year[@]};do
    #python bin/SubmitLimit.py model_files/mh125_13_withVBF.root mh125_13 $year
    python bin/SubmitLimit.py model_files/mh125EFT_lc_13_withVBF.root mh125EFT_lc_13 $year
    python bin/SubmitLimit.py model_files/mh125EFT_13_withVBF.root mh125EFT_13 $year
    python bin/SubmitLimit.py model_files/mh125_align_13_withVBF.root mh125_align_13 $year
    python bin/SubmitLimit.py model_files/mh125_lc_13_withVBF.root mh125_lc_13 $year
    python bin/SubmitLimit.py model_files/mh125_ls_13_withVBF.root mh125_ls_13 $year
    python bin/SubmitLimit.py model_files/thdm_type1_0.1cba.root thdm_type1_0.1cba $year
    

done 
