#__BoostedVBFDNN_0.45_SR_NoMEKDCut

ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_MASS=(5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Boosted)
ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(2016)

ARR_WP=(0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)

#ARR_WP=(0.0)

for MASS in ${ARR_MASS[@]};do
    for BST in ${ARR_BST[@]};do
	for YEAR in ${ARR_YEAR[@]};do
	    for WP in ${ARR_WP[@]};do
		echo ${WP}
		python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --dnn
	    done
	done
    done
done
