SFs=SF_bin2,SF_bin1,SF_bin0
NP=1200
SF_bin0_RANGE=`python ../script/LikelihoodScanNLL.py SF_bin0`
SF_bin1_RANGE=`python ../script/LikelihoodScanNLL.py SF_bin1`
SF_bin2_RANGE=`python ../script/LikelihoodScanNLL.py SF_bin2`


RANGE_ARG="${SF_bin0_RANGE}:${SF_bin1_RANGE}:${SF_bin2_RANGE}"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r -n nll --setParameterRanges ${RANGE_ARG}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r,rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --freezeParameters ${SFs},rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT} 
