V=HadronicW_mass_zoom

YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    #combineCards.py -S PassBin0=PassingWtagger__200/${V}/datacard.txt PassBin1=PassingWtagger__300/${V}/datacard.txt PassBin2=PassingWtagger__400/${V}/datacard.txt AllBin0=NoWtagger__200/${V}/datacard.txt AllBin1=NoWtagger__300/${V}/datacard.txt AllBin2=NoWtagger__400/${V}/datacard.txt &> CombinedCard_${YEAR}.txt
    combineCards.py -S PassBin0=Datacards_DATA/PassingWtagger__200/${V}/datacard.txt PassBin1=Datacards_DATA/PassingWtagger__300/${V}/datacard.txt PassBin2=Datacards_DATA/PassingWtagger__400/${V}/datacard.txt FailBin0=Datacards_DATA/FailingWtagger__200/${V}/datacard.txt FailBin1=Datacards_DATA/FailingWtagger__300/${V}/datacard.txt FailBin2=Datacards_DATA/FailingWtagger__400/${V}/datacard.txt PassBin0m=Datacards_MC/PassingWtagger__200/Event/datacard.txt PassBin1m=Datacards_MC/PassingWtagger__300/Event/datacard.txt PassBin2m=Datacards_MC/PassingWtagger__400/Event/datacard.txt FailBin0m=Datacards_MC/FailingWtagger__200/Event/datacard.txt FailBin1m=Datacards_MC/FailingWtagger__300/Event/datacard.txt FailBin2m=Datacards_MC/FailingWtagger__400/Event/datacard.txt &> CombinedCard_${YEAR}.txt
    cd -
done
