ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)

ARR_CUT=(0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)
#ARR_CUT=(nocut)
YEAR=$1
BST=$2



for MASS in ${ARR_MASS[@]};do
    #for YEAR in ${ARR_YEAR[@]};do
    ##--nocut
    #BST=Boosted
    if [[ $BST == "Boosted" ]];then
	python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
    fi
    if [[ $BST == "Resolved" ]];then
    #BST=Resolved
	python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
    fi
    
    for CUT in ${ARR_CUT[@]};do
	#__BoostedALL_SB_VBFCUT_"+cut+"
	#BST=Boosted
	if [[ $BST == "Boosted" ]];then

	    MELACUT="C0.005__M900_${CUT}"
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	    MELACUT="C0.0005__M1500_${CUT}"
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	fi

	if [[ $BST == "Resolved" ]];then
	    #BST=Resolved
	    MELACUT="C0.001__M200_${CUT}"
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	    MELACUT="C0.01__M400_${CUT}"
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
	fi

    done
done
