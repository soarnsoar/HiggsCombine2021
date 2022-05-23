#####
ARR_Year=(2016 2017 2018)
#ARR_Year=(2016)
Mass=1000
#SF_Bin2,SF_Bin1,SF_Bin0
ARR_POI=(SF_Bin0 SF_Bin1 SF_Bin2)


#combineTool.py -M Impacts -d htt_tt.root -m 125 -o impacts.json

#plotImpacts.py -i impacts.json -o impacts


for Year in ${ARR_Year[@]};do
    Workspace=${PWD}/../Datacards_${Year}/WS_${Year}.root

    #python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doInitialFit --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10  --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*} &&combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doFits --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10  --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*} --job-mode condor --dry-run --sub-opts \"accounting_group=group_cms\"" -d WORDIR_CONDOR_TEST2 -n ${WORKDIR} -m 1 -s 

    for POI in ${ARR_POI[@]};do
	WORKDIR=${Year}__${POI}
	mkdir -p $WORKDIR
	cd ${WORKDIR}
	#(combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doInitialFit  --redefineSignalPOIs ${POI} --robustFit 1 -n Impact${Year}&&combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doFits --robustFit 1 -n Impact${Year} --redefineSignalPOIs ${POI}) &> impact.log&
	combineTool.py -M Impacts -d ${Workspace} -m 1000 -n Impact${Year} --redefineSignalPOIs ${POI} -o impacts.json
	plotImpacts.py -i impacts.json -o impacts
	cd -
    done

done
