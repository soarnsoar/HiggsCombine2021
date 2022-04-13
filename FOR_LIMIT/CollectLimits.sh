#AsymptoticLimits/2016/model_indep/Boosted/0.05/vbfonly/model_indep_NoI/higgsCombineTest.AsymptoticLimits.mH1000.root
#ARR_DIR=($(ls -d AsymptoticLimits/201*/*/*/*/*/*/))
ARR_YEAR=(2016 2017 2018)
for YEAR in ${ARR_YEAR[@]};do
    source CollectLimits_arg.sh ${YEAR} &> logs/CollectLimits_arg.${YEAR}.log&
done

for DIR in ${ARR_DIR[@]};do
    continue
    echo ${DIR}
    cd ${DIR}
    combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json
    cd -

done


