V=HadronicW_mass_zoom

YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    combineCards.py -S Bin0=TOPCutVetoHighScore__200/${V}/datacard.txt Bin1=TOPCutVetoHighScore__300/${V}/datacard.txt Bin2=TOPCutVetoHighScore__400/${V}/datacard.txt &> CombinedCard_${YEAR}.txt
    cd -
done
