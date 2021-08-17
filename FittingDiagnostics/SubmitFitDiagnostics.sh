#####
#ARR_Year=(2016 2017 2018 3yrs)
#ARR_Year=(2016 2017 2018)
ARR_Year=(2016)
#ARR_Year=(3yrs)
#ARR_Region=(Boosted)
ARR_Region=(all)
#ARR_Mass=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_Mass=(400 1000 3000)
ARR_Mass=(1000)

#####

model=smlike

for Year in ${ARR_Year[@]};do
    for Region in ${ARR_Region[@]};do
	for Mass in ${ARR_Mass[@]};do
	    
	    WORKDIR=FitDiagnosticsDir_Sig1_${Region}_${Mass}_${Year}
	    mkdir -p ${WORKDIR}
	    cd ${WORKDIR}
	    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
	    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics -m ${Mass} -t -1 --expectSignal=1 --setParameterRanges r=0,10" -d WORDIR_CONDOR_TEST2 -n ${WORKDIR} -m 1 -s 
	    cd -


	    WORKDIR=FitDiagnosticsDir_Sig0_${Region}_${Mass}_${Year}
	    mkdir -p ${WORKDIR}
	    cd ${WORKDIR}
	    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
	    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M FitDiagnostics -m ${Mass} -t -1 --expectSignal=0 --setParameterRanges r=0,10" -d WORDIR_CONDOR_TEST2 -n ${WORKDIR} -m 1 -s 
	    cd -
	done
    done	
done
