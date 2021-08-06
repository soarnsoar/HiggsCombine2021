#####
ARR_Year=(2016 2017 2018 3yrs)
#ARR_Year=(3yrs)
#ARR_Region=(Boosted Resolved all)
ARR_Region=(all)
#ARR_Mass=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
ARR_Mass=(400 1000 3000)

#####

model=smlike

for Year in ${ARR_Year[@]};do
    for Region in ${ARR_Region[@]};do
	for Mass in ${ARR_Mass[@]};do
	    
	    WORKDIR=ImpactDir_${Region}_${Mass}_${Year}

	    #((mkdir -p ${WORKDIR})&&(cd ${WORKDIR})&&(combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doInitialFit --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10)&&(combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doFits --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10 --job-mode condor --dry-run --sub-opts "accounting_group=group_cms")&&(condor_submit condor_combine_task.sub)&&(cd ../))
	    mkdir -p ${WORKDIR}
	    cd ${WORKDIR}
	    Workspace=../../../Workspaces_${Year}/${model}/hwwlnuqq_${Region}_${Mass}_${Year}.root
	    #((combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doInitialFit --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10)&&(combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doFits --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10 --job-mode condor --dry-run --sub-opts "accounting_group=group_cms")&&(condor_submit condor_combine_task.sub)) &> log.txt&
	    ##   parser = optparse.OptionParser(usage)
	    #parser.add_option("-c","--command",   dest="command", help="command to run")
	    #parser.add_option("-d","--workdir",   dest="workdir", help="workarea")
	    #parser.add_option("-n","--jobname",   dest="jobname", help="jobname")
	    #parser.add_option("-m","--ncpu",   dest="ncpu", help="number of multicores",default=1)
	    #parser.add_option("-s","--submit",   dest="submit",action="store_true", help="submit",default=False)
	    
	    #python ../python_tool/ExportShellCondorSetup.py
	    python ../../python_tool/ExportShellCondorSetup.py -c "combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doInitialFit --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10&&combineTool.py -d ${Workspace} -M Impacts -m ${Mass} --doFits --robustFit 1 -t -1 --expectSignal=1 --setParameterRanges r=0,10 --job-mode condor --dry-run --sub-opts \"accounting_group=group_cms\"" -d WORDIR_CONDOR_TEST2 -n ${WORKDIR} -m 1 -s 
	    cd -
	done
    done	
done
