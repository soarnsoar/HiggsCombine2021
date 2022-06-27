#####
#ARR_Year=(2016 2017 2018)
#ARR_Year=(3yrs)
ARR_Year=(2016 2017 2018)
#ARR_Year=(2016)
#ARR_Year=(3yrs)
#ARR_Region=(Boosted)
ARR_Region=(Boosted Resolved all)
#ARR_Mass=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
ARR_Mass=(400 900 1000 3000)
#ARR_Mass=(1000)
#ARR_model=(smlike smlike_NoI model_indep model_indep_NoI) 
ARR_model=(smlike smlike_NoI)
#####
ARR_expectedSig=(0 0.1 0.3 1)


for Year in ${ARR_Year[@]};do
    for Region in ${ARR_Region[@]};do
	for Mass in ${ARR_Mass[@]};do
	    for model in ${ARR_model[@]};do
		for sig in ${ARR_expectedSig[@]};do
		    #freeze bbb
		    WORKDIR=FitDiagnosticsDir_Sig${sig}_${Region}_${Mass}_${Year}_${model}_FreezeMCStat
		    mkdir -p ${WORKDIR}
		    cd ${WORKDIR}
		    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
		    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics --plots -m ${Mass} -t -1 --expectSignal=${sig} --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*},rgx{prop_.*},rgx{deltaTheory.*xsec},rgx{.*_stat} --setParameterRanges r=0,10&&python ../../diffNuisances.py fitDiagnostics.Test.root -g outputfile.root" -d WORDIR_CONDOR_TEST3 -n ${WORKDIR} -m 1 -s 
		    cd -


		    #not freeze bbb
		    WORKDIR=FitDiagnosticsDir_Sig${sig}_${Region}_${Mass}_${Year}_${model}
		    mkdir -p ${WORKDIR}
		    cd ${WORKDIR}
		    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
		    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics --plots -m ${Mass} -t -1 --expectSignal=${sig} --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*},rgx{deltaTheory.*xsec},rgx{.*_stat} --setParameterRanges r=0,10&&python ../../diffNuisances.py fitDiagnostics.Test.root -g outputfile.root" -d WORDIR_CONDOR_TEST3 -n ${WORKDIR} -m 1 -s 
		    cd -
		    ##not freeze my stat
		    WORKDIR=FitDiagnosticsDir_Sig${sig}_${Region}_${Mass}_${Year}_${model}_NOFREEZEMYSTAT
		    mkdir -p ${WORKDIR}
		    cd ${WORKDIR}
		    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
		    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics --plots -m ${Mass} -t -1 --expectSignal=${sig} --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*},rgx{deltaTheory.*xsec} --setParameterRanges r=0,10&&python ../../diffNuisances.py fitDiagnostics.Test.root -g outputfile.root" -d WORDIR_CONDOR_TEST3 -n ${WORKDIR} -m 1 -s 
		    cd -


		    ##not freeze my stat__cminDefaultMinimizerStrategy0
		    WORKDIR=FitDiagnosticsDir_Sig${sig}_${Region}_${Mass}_${Year}_${model}_NOFREEZEMYSTAT__cminDefaultMinimizerStrategy0
		    mkdir -p ${WORKDIR}
		    cd ${WORKDIR}
		    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
		    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics --plots -m ${Mass} -t -1 --expectSignal=${sig} --freezeParameters rgx{prop_.*qqWWqq.*},rgx{prop_.*ggWW.*},rgx{prop_.*ggH_hww.*},rgx{prop_.*qqH_hww.*},rgx{deltaTheory.*xsec} --setParameterRanges r=0,10 --cminDefaultMinimizerStrategy 0&&python ../../diffNuisances.py fitDiagnostics.Test.root -g outputfile.root" -d WORDIR_CONDOR_TEST3 -n ${WORKDIR} -m 1 -s 
		    cd -
		done
	    done
	done
    done	
done
