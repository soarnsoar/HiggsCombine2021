ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)

YEAR=$1
BST=$2


for MASS in ${ARR_MASS[@]};do
    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} -f ggfonly
    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} -f vbfonly
    
    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} -f ggfonly -i
    python CondorSubmit_AsymptoticLimits.py -y ${YEAR} -m ${MASS} -b ${BST} -f vbfonly -i

    

done
