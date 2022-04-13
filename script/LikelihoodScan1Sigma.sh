SFs=SF_bin2,SF_bin1,SF_bin0
combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r -n scan
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --redefineSignalPOIs ${SFs} --setParameters r=1 --freezeParameters r,rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT}
#combine -M MultiDimFit -d ${1} -m 1000 --algo singles --cl=0.68  --freezeParameters ${SFs},rgx{.*eff.*},rgx{.*btag.*},rgx{.*ACCEPT} 
