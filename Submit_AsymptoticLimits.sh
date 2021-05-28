ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_MASS=(1000)
ARR_BST=(all Boosted Resolved)
ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(2018)
#CondorSubmit_MakeWorkSpace.py
for MASS in ${ARR_MASS[@]};do
    for BST in ${ARR_BST[@]};do
	for YEAR in ${ARR_YEAR[@]};do
	    ##--interference
	    python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i False -f floating
	    python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i False -f ggfonly
	    python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i False -f vbfonly
	    ##--no interference
	    #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -i False
	done
    done
done
