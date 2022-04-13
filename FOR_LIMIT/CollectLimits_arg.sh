#AsymptoticLimits/2016/model_indep/Boosted/0.05/vbfonly/model_indep_NoI/higgsCombineTest.AsymptoticLimits.mH1000.root
#AsymptoticLimits/2016/model_indep/Boosted/C0.0005__M1500_0.1/ggfonly/model_indep_NoI/
YEAR=${1}
ARR_DIR=($(ls -d AsymptoticLimits/${YEAR}/*/*/*/*/*/))
for DIR in ${ARR_DIR[@]};do
    echo ${DIR}
    cd ${DIR}
    combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json
    cd -

done


