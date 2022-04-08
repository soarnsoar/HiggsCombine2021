#ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
ARR_YEAR=(2016 2017 2018)
ARR_CUT=(0 1 2 3)
MASS=1000
for YEAR in ${ARR_YEAR[@]};do

    ##--nocut
    #BST=Boosted
    #python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
    #BST=Resolved
    #python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
    
    
    for CUT in ${ARR_CUT[@]};do
	#CondorSubmit_MakeWorkSpace.py
	BST=Boosted
        python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $CUT
	BST=Resolved
        python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $CUT    
    done
done
