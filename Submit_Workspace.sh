ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=( Boosted Resolved)
ARR_YEAR=(2016 2017 2018)
ARR_WP=(0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)

#ARR_MASS=(5000)
#ARR_YEAR=(2016)
#ARR_WP=(0.05)

#ARR_WP=(0.0001 0.0002 0.0004 0.0006 0.0008
#    0.001 0.002 0.004 0.006 0.008
#    0.01 0.02 0.04 0.06 0.08
#    0.1 0.2 0.4 0.6 0.8
#    1.0)

#CondorSubmit_MakeWorkSpace.py
#    parser.add_option("-c", "--c", dest="c" , help="c")
#    parser.add_option("-a", "--mela_m", dest="mela_m" , help="mela_m")

for MASS in ${ARR_MASS[@]};do
    
    for YEAR in ${ARR_YEAR[@]};do
	for WP in ${ARR_WP[@]};do

            echo ${WP}
            BST=Boosted
            python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 1500 -c 0.05
            python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 900 -c 0.2
            #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 400 -c 0.02

            BST=Resolved

            #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 400 -c 0.005
            #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} --mela_m 200 -c 0.0008

	    
	    #python CondorSubmit_MakeWorkSpace.py -y ${YEAR} -m ${MASS} -b ${BST} -w ${WP} -c --mela_m
	done
    done
done

