ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
ARR_YEAR=(2016 2017 2018)
#__BoostedALL_SR_MEKDCUT_C0.005__M900_0.95
#__BoostedALL_SR_nomekdcut
#__BoostedALL_TOP_MEKDCUT_C0.0005__M1500_0.05

#___ResolvedALL__SB_MEKDCUT_C0.001__M200_0.45
#___ResolvedALL__SR_MEKDCUT_C0.001__M200_0.85
#___ResolvedALL__SB_nomekdcut
#___ResolvedALL__TOP_MEKDCUT_C0.01__M400_0.75
#___ResolvedALL__SR_MEKDCUT_C0.01__M400_0.25

#ARR_CUT=(0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)
#ARR_CUT=(nocut)
for BST in ${ARR_BST[@]};do
    for YEAR in ${ARR_YEAR[@]};do
	source Submit_CombineCard_arg.sh ${YEAR} ${BST} &> logs/Submit_CombineCard_arg.${YEAR}.${BST}.log&
    done
done
for MASS in ${ARR_MASS[@]};do
    for YEAR in ${ARR_YEAR[@]};do
	continue
	##--nocut
	#BST=Boosted
	#python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
	#BST=Resolved
	#python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut


	#for CUT in ${ARR_CUT[@]};do
	#    #__BoostedALL_SB_VBFCUT_"+cut+"
	#    BST=Boosted
	#    MELACUT="C0.005__M900_${CUT}"
	#    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	#    MELACUT="C0.0005__M1500_${CUT}"
	#    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT

	#    BST=Resolved
	#    MELACUT="C0.001__M200_${CUT}"
	#    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	#    MELACUT="C0.01__M400_${CUT}"
	#    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	    
	#done
	
    done
done
