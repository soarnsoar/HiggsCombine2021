#SFs=SF_Bin2,SF_Bin1,SF_Bin0
#POI="r_Bin0m,r_Bin1m,r_Bin2m"
#POI="r_PassBin0m,r_PassBin1m,r_PassBin2m"
#POI="r_FailBin0m,r_FailBin1m,r_FailBin2m"
#POI="r_Bin0m"
#EffBin0m

######-------check r_Pass
#POI="r_PassBin0m,r_PassBin1m,r_PassBin2m"
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${POI} -n scan --freezeParameters SF_Bin0,SF_Bin1,SF_Bin2,rgx{CMS.*},rgx{PS.*},rgx{.*ACCEPT},rgx{.*norm},rgx{lumi.*},rgx{prop_bin.*},r_FailBin0m,r_FailBin1m,r_FailBin2m,r_PassBin0,r_PassBin1,r_PassBin2 --verbose 3
# --robustFit 1 --verbose 3
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r,rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --freezeParameters ${SFs},rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT} 

######-------check r_Fail
POI="r_FailBin0m,r_FailBin1m,r_FailBin2m"
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${POI} -n scan --freezeParameters SF_Bin0,SF_Bin1,SF_Bin2,rgx{CMS.*},rgx{PS.*},rgx{.*ACCEPT},rgx{.*norm},rgx{lumi.*},rgx{prop_bin.*},r_PassBin0m,r_PassBin1m,r_PassBin2m,r_PassBin0,r_PassBin1,r_PassBin2 --verbose 3
combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${POI} -n scan --freezeParameters rgx{CMS.*},rgx{PS.*},rgx{.*ACCEPT},rgx{.*norm},rgx{lumi.*},rgx{prop_bin.*} --verbose 3
