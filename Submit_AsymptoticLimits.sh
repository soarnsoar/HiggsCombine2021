ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
ARR_YEAR=(2016 2017 2018)
#Submit_AsymptoticLimits_arg.sh
for BST in ${ARR_BST[@]};do
    for YEAR in ${ARR_YEAR[@]};do
	source Submit_AsymptoticLimits_arg.sh ${YEAR} ${BST} &> logs/Submit_AsymptoticLimits_arg.${YEAR}.${BST}.log&
    done
done
for MASS in ${ARR_MASS[@]};do
    for YEAR in ${ARR_YEAR[@]};do
	continue
	##--nocut
	#BST=Boosted
	#python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
	#BST=Resolved
	#python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut


	#for CUT in ${ARR_CUT[@]};do
	#    #__BoostedALL_SB_VBFCUT_"+cut+"
	#    BST=Boosted
	#    MELACUT="C0.005__M900_${CUT}"
	#    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	#    MELACUT="C0.0005__M1500_${CUT}"
	#    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT

	#    BST=Resolved
	#    MELACUT="C0.001__M200_${CUT}"
	#    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	#    MELACUT="C0.01__M400_${CUT}"
	#    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	    
	#done
	
    done
done
