SFs=SF_Bin2,SF_Bin1,SF_Bin0
NP=1200
echo "--READ RANGE and 1st fit"
SF_Bin0_RANGE=`python ../script/GetSigmaInScanBranch.py SF_Bin0 0`
SF_Bin1_RANGE=`python ../script/GetSigmaInScanBranch.py SF_Bin1 0`
SF_Bin2_RANGE=`python ../script/GetSigmaInScanBranch.py SF_Bin2 0`

SF_Bin0_init=`python ../script/GetSigmaInScanBranch.py SF_Bin0 1`
SF_Bin1_init=`python ../script/GetSigmaInScanBranch.py SF_Bin1 1`
SF_Bin2_init=`python ../script/GetSigmaInScanBranch.py SF_Bin2 1`

echo "---DONE."
RANGE_ARG="${SF_Bin0_RANGE}:${SF_Bin1_RANGE}:${SF_Bin2_RANGE}"
INIT_ARG="${SF_Bin0_init},${SF_Bin1_init},${SF_Bin2_init}"
echo "---->${INIT_ARG}"
echo "---->$RANGE_ARG"


RANGE_ARG="${SF_Bin0_RANGE}:${SF_Bin1_RANGE}:${SF_Bin2_RANGE}"
INIT_ARG="${SF_Bin0_init},${SF_Bin1_init},${SF_Bin2_init}"


INIT_ARG="SF_Bin2=1,SF_Bin1=1,SF_Bin0=1"
##---SF_Bin0
echo SF_Bin0
POI="SF_Bin0"
POIRANGE="$SF_Bin0_RANGE"
#POIRANGE="SF_Bin0=0.4,2"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters ${INIT_ARG} -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&

echo SF_Bin1
POI="SF_Bin1"
POIRANGE="$SF_Bin1_RANGE"
#POIRANGE="SF_Bin1=0.4,2"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters ${INIT_ARG} -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&

echo SF_Bin2
POI="SF_Bin2"
POIRANGE="$SF_Bin2_RANGE"
#POIRANGE="SF_Bin2=0.4,2"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} --setParameters ${INIT_ARG} -n nll_${POI} --setParameterRanges ${POIRANGE}  &> NLL_${POI}.log&



