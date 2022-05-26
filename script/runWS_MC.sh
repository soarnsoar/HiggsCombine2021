YEARS=(2016 2017 2018)


for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}

    PO=`python ../data/PrintPO.py ../data/${YEAR}.root`
    text2workspace.py CombinedCard_MC_${YEAR}.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HC_model_WJetsWTAG.WTAG_EFF_MC:WTAGSF -o WS_MC_${YEAR}.root ${PO} &> WS_MC.log&

    cd -
done
