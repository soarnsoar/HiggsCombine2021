ARR_DIR=($(ls -d AsymptoticLimits/201*/*/*/*/*/))
for DIR in ${ARR_DIR[@]};do
    echo ${DIR}
    cd ${DIR}
    combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json
    cd -

done


