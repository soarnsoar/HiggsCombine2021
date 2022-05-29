ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=(all Boosted Resolved)
#ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
#ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(2016 2018 3yrs)
#ARR_YEAR=(2017)

YEAR=$1
BST=$2
#ARR_CUT=()

for MASS in ${ARR_MASS[@]};do
    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -i
    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST}
done

