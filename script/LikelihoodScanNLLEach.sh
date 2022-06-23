NP=1200


##---SF_Bin0
echo slope
POI="slope"
#POIRANGE="SF_Bin0=0.4,2"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} -n nll_${POI} --setParameterRanges slope=-0.01,0 &> NLL_${POI}.log&

echo intercept
POI="intercept"
POIRANGE="$SF_Bin1_RANGE"
#POIRANGE="SF_Bin1=0.4,2"
combine -M MultiDimFit -d ${1} -m 1000 --algo grid --points ${NP}  --redefineSignalPOIs ${POI} -n nll_${POI} --setParameterRanges intercept=0,2 &> NLL_${POI}.log&




