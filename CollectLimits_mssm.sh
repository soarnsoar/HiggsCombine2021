ARR_DIR=($(ls -d AsymptoticLimits/2016/mh125_13_withVBF/*/*/))
for DIR in ${ARR_DIR[@]};do
    echo ${DIR}
    cd ${DIR}
    combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json
    cd -

done


