YEARS=(2016 2017 2018)


for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    text2workspace.py Datacards/Resolved__WJETCR/HadronicW_mass/datacard.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HC_MjjShape.MjjShape:mjjshape -o WS_${YEAR}.root &> WS.log&
    cd -
done
