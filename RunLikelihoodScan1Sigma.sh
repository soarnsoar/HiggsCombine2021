YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    cd Datacards_${YEAR}
    source ../script/LikelihoodScan1Sigma.sh CombinedCard_${YEAR}.txt &> LikelihoodScan1Sigma.log&
    cd -
done
