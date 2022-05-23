YEARS=(2016 2017 2018)
for YEAR in ${YEARS[@]};do
    mkdir -p Datacards_${YEAR}
    cp -r /cms_scratch/jhchoi/ANv9Base/SBWTAGSF_MEASURE/FATJETBASE/${YEAR}/Datacards_MC Datacards_${YEAR}/&
    cp -r /cms_scratch/jhchoi/ANv9Base/SBWTAGSF_MEASURE/FATJETBASE/${YEAR}/Datacards_DATA Datacards_${YEAR}/&
done


