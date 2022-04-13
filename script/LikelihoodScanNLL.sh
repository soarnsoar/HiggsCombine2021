SFs=SF_bin2,SF_bin1,SF_bin0
NP=1200
SF_bin0_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin0 0`
SF_bin1_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin1 0`
SF_bin2_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin2 0`

SF_bin0_init=`python ../script/GetSigmaInScanBranch.py SF_bin0 1`
SF_bin1_init=`python ../script/GetSigmaInScanBranch.py SF_bin1 1`
SF_bin2_init=`python ../script/GetSigmaInScanBranch.py SF_bin2 1`


RANGE_ARG="${SF_bin0_RANGE}:${SF_bin1_RANGE}:${SF_bin2_RANGE}"
INIT_ARG="${SF_bin0_init},${SF_bin1_init},${SF_bin2_init}"
echo "---->${INIT_ARG}"
echo "---->$RANGE_ARG"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${SFs} --setParameters r=1,${INIT_ARG} --freezeParameters r -n nll --setParameterRanges ${RANGE_ARG}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r,rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --freezeParameters ${SFs},rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT} 
