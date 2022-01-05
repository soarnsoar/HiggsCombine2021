#__BoostedVBFDNN_0.45_SR_NoMEKDCut

ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_MASS=(5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Boosted)
ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(2016 2017)
#ARR_YEAR=(2016)
#MELA_C_BOOST=['0.0001','0.0002','0.0004','0.0006','0.0008',\
#    '0.001','0.002','0.004','0.006','0.008',\
#    '0.01','0.02','0.04','0.06','0.08',\
#    '0.1', '0.2', '0.4','0.6','0.8', '1.0']

#parser.add_option("-y", "--year", dest="year" , help="year")
#parser.add_option("-m", "--mass", dest="mass" , help="mass")

#parser.add_option("-b", "--bst", dest="bst" , help="bst")
#parser.add_option("-w", "--wp", dest="wp" , help="wp")
#parser.add_option("-c", "--c", dest="c" , help="c")
#parser.add_option("-p", "--mela_m", dest="mela_m" , help="mela_m")

ARR_WP=(0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)
#ARR_WP=(0.05)
for MASS in ${ARR_MASS[@]};do
    for YEAR in ${ARR_YEAR[@]};do
	for WP in ${ARR_WP[@]};do
	    echo ${WP}
	    BST=Boosted
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 1500 -c 0.002
	    python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 900 -c 0.02
	    #python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 400 -c 0.02

	    BST=Resolved

	    #python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 400 -c 0.005
	    #python CondorSubmit_CombineCard.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 200 -c 0.0008
	done
    done
done
