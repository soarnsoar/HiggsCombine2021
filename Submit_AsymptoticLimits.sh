ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_MASS=(1000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
ARR_YEAR=(2016 2017 2018)
#ARR_YEAR=(2016)
ARR_WP=(0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95)
#ARR_WP=(0.0)
ARR_WP_BST=(0.0 0.7 0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79
0.8 0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89
0.9 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99)

ARR_WP_RES=(0.0 0.9 0.905 0.91 0.915 0.92 0.925 0.93 0.935 0.94 0.945 0.95 0.955
0.96 0.965 0.97 0.975 0.98 0.985 0.99 0.995
)


#ARR_YEAR=(2018)
#CondorSubmit_MakeWorkSpace.py
for MASS in ${ARR_MASS[@]};do
    #for BST in ${ARR_BST[@]};do
	for YEAR in ${ARR_YEAR[@]};do
	    for WP in ${ARR_WP_BST[@]};do
		##--interference
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f floating
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f ggfonly
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f vbfonly -w ${WP}
		##--no interference
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -f floating
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -f ggfonly
		python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b Boosted -f vbfonly -w ${WP}
	    done
	done
    #done
done



for MASS in ${ARR_MASS[@]};do
    #for BST in ${ARR_BST[@]};do
	for YEAR in ${ARR_YEAR[@]};do
	    for WP in ${ARR_WP_RES[@]};do
		##--interference
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f floating
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f ggfonly
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -i -f vbfonly -w ${WP}
		##--no interference
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -f floating
		#python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -f ggfonly
		python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b Resolved -f vbfonly -w ${WP}
	    done
	done
    #done
done
