V=HadronicW_mass_zoom

YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    #combineCards.py -S PassBin0=PassingWtagger__200/${V}/datacard.txt PassBin1=PassingWtagger__300/${V}/datacard.txt PassBin2=PassingWtagger__400/${V}/datacard.txt AllBin0=NoWtagger__200/${V}/datacard.txt AllBin1=NoWtagger__300/${V}/datacard.txt AllBin2=NoWtagger__400/${V}/datacard.txt &> CombinedCard_${YEAR}.txt
    text2workspace.py CombinedCard_${YEAR}.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HC_model_WJetsWTAG.WTAG_SF:WTAGSF -o WS_${YEAR}.root

    cd -
done
