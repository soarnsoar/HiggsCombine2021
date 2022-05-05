ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)

YEAR=$1
BST=$2
ARR_CUT=()
ARR_CUT=(0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)
#ARR_CUT=(0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9)


#if [[ $BST == "Boosted" ]];then
#    ARR_CUT=(0.6 0.62 0.64 0.66 0.68 0.7 0.72 0.74 0.76 0.78 0.8 0.82 0.84 0.86 0.88 0.9 0.92 0.94 0.96 0.98 nocut)
#fi
#if [[ $BST == "Resolved" ]];then
#    #ARR_CUT=(0.9 0.905 0.91 0.915 0.92 0.925 0.93 0.935 0.94 0.945 0.95 0.955 0.96 0.965 0.97 0.975 0.98 0.985 0.99 0.995 nocut)
#    ARR_CUT=(0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 nocut)
#fi

if [[ $BST == "Boosted" ]];then
    echo " "
    #ARR_CUT=(0.6 0.62 0.64 0.66 0.68 0.7 0.72 0.74 0.76 0.78 0.8 0.82 0.84 0.86 0.88 0.9 0.92 0.94 0.96 0.98 nocut)
    #ARR_CUT=(0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99 nocut)
fi
if [[ $BST == "Resolved" ]];then
    echo " "
    #ARR_CUT=(0.9 0.905 0.91 0.915 0.92 0.925 0.93 0.935 0.94 0.945 0.95 0.955 0.96 0.965 0.97 0.975 0.98 0.985 0.99 0.995 nocut)                             
    #ARR_CUT=(0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 nocut)
    #ARR_CUT=(0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99 nocut)
fi

for MASS in ${ARR_MASS[@]};do
    python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut nocut
    for CUT in ${ARR_CUT[@]};do
	##--interference
	#python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -i
	##--no interference
	#python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -c ${CUT}
        if [[ $BST == "Boosted" ]];then
            MELACUT=_M900C0.01_$CUT
            python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
            #MELACUT=_M1500C0.0005_$CUT
            #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
        fi

        if [[ $BST == "Resolved" ]];then

            #MELACUT=_M400C0.001_$CUT
            #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
            MELACUT=_M200C0.0008_$CUT
            python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} --cut $MELACUT
        fi

    
    done
done
