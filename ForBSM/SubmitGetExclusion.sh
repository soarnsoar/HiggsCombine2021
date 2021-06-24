#    rf_model=sys.argv[1]
#    year=sys.argv[2]
#    #rf_model="mh125_13_withVBF.root"                                                                                                                         
#    suffix_model=rf_model.rstrip('.root')
#    #year=2016                                                                                                                                               
ARR_YEAR=(2016 2017 2018)
ARR_MODEL=(mh125EFT_13_withVBF.root     mh125_align_13_withVBF.root mh125EFT_lc_13_withVBF.root  mh125_lc_13_withVBF.root mh125_13_withVBF.root        mh125_ls_13_withVBF.root)

for YEAR in ${ARR_YEAR[@]};do
    for MODEL in ${ARR_MODEL[@]};do

	python GetExclusion.py ${MODEL} ${YEAR}

    done
done

