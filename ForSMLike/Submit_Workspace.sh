ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_MASS=(1000)
ARR_BST=(all Boosted Resolved)
ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(3yrs)
#CondorSubmit_MakeWorkSpace.py
pushd ../

#ForSMLike]$ mv myrun.py run_smlike.py
for MASS in ${ARR_MASS[@]};do
    for BST in ${ARR_BST[@]};do
	for YEAR in ${ARR_YEAR[@]};do
	    ##--interference
	    python ForSMLike/run_workspace_smlike.py -y ${YEAR} -m ${MASS} -b ${BST} -i
	    ##--no interference
	    python ForSMLike/run_workspace_smlike.py -y ${YEAR} -m ${MASS} -b ${BST}
	done
    done
done
popd
