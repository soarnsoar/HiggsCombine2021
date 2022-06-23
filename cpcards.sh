YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    mkdir -p Datacards_${YEAR}
    cp -r /cms_scratch/jhchoi/ANv11/MjjShape//${YEAR}/Datacards Datacards_${YEAR}/&

done


