ARR_YEAR=(2016 2017 2018)
ARR_MODEL=(mh125EFT_13_withVBF.root     mh125_align_13_withVBF.root mh125EFT_lc_13_withVBF.root  mh125_lc_13_withVBF.root mh125_13_withVBF.root        mh125_ls_13_withVBF.root)
for YEAR in ${ARR_YEAR[@]};do
    for MODEL in ${ARR_MODEL[@]};do
	python CollectModelR.py ${YEAR} ${MODEL}
    done
done
