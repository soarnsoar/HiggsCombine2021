SFs=SF_bin2,SF_bin1,SF_bin0
NP=1200
echo "--READ RANGE and 1st fit"
SF_bin0_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin0 0`
SF_bin1_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin1 0`
SF_bin2_RANGE=`python ../script/GetSigmaInScanBranch.py SF_bin2 0`

SF_bin0_init=`python ../script/GetSigmaInScanBranch.py SF_bin0 1`
SF_bin1_init=`python ../script/GetSigmaInScanBranch.py SF_bin1 1`
SF_bin2_init=`python ../script/GetSigmaInScanBranch.py SF_bin2 1`

echo "---DONE."
RANGE_ARG="${SF_bin0_RANGE}:${SF_bin1_RANGE}:${SF_bin2_RANGE}"
INIT_ARG="${SF_bin0_init},${SF_bin1_init},${SF_bin2_init}"
echo "---->${INIT_ARG}"
echo "---->$RANGE_ARG"


##---SF_bin0
echo SF_bin0
POI="SF_bin0"
POIRANGE="$SF_bin0_RANGE"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters r=1,${INIT_ARG} --freezeParameters r -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&

echo SF_bin1
POI="SF_bin1"
POIRANGE="$SF_bin1_RANGE"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters r=1,${INIT_ARG} --freezeParameters r -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&

echo SF_bin2
POI="SF_bin2"
POIRANGE="$SF_bin2_RANGE"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters r=1,${INIT_ARG} --freezeParameters r -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&



