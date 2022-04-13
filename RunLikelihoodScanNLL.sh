YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    source ../script/LikelihoodScanNLL.sh CombinedCard_${YEAR}.txt &> LikelihoodScanNLL.log&
    cd -
done
