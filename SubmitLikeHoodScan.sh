#ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
#ARR_BST=(all Boosted Resolved)
ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
ARR_YEAR=(2016 2017 2018)
ARR_CUT=(0 1 2 3)
MASS=1000

#CondorSubmit_LikelihoodScan.py
for YEAR in ${ARR_YEAR[@]};do

    #Wjetsnorm_Boosted_GGF0_2016  rateParam hww_lqq_bst_ggf_top_2016 Wjets 1 [0,50]
    #topnorm_Boosted_GGF0_2016  rateParam hww_lqq_bst_ggf_top_2016 Top 1 [0,50]
    #topnorm_Boosted_VBF_2016
    
    #            python CondorSubmit_AsymptoticLimits.py  -y ${YEAR} -m ${MASS} -b ${BST} -f ggfonly  -c $MELACUT
    for CUT in ${ARR_CUT[@]};do
	BST=Boosted
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF0_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF1_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_VBF_${YEAR} --cut $CUT

        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_GGF0_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_GGF1_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_VBF_${YEAR} --cut $CUT

	python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF0_${YEAR},Wjetsnorm_${BST}_GGF1_${YEAR},Wjetsnorm_${BST}_VBF_${YEAR},topnorm_${BST}_GGF0_${YEAR},topnorm_${BST}_GGF1_${YEAR},topnorm_${BST}_VBF_${YEAR} --cut $CUT

	BST=Resolved

        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF0_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF1_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_VBF_${YEAR} --cut $CUT

        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_GGF0_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_GGF1_${YEAR} --cut $CUT
        #python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi topnorm_${BST}_VBF_${YEAR} --cut $CUT
	python CondorSubmit_LikelihoodScan.py -y ${YEAR} -m ${MASS} -b ${BST} --poi Wjetsnorm_${BST}_GGF0_${YEAR},Wjetsnorm_${BST}_GGF1_${YEAR},Wjetsnorm_${BST}_VBF_${YEAR},topnorm_${BST}_GGF0_${YEAR},topnorm_${BST}_GGF1_${YEAR},topnorm_${BST}_VBF_${YEAR} --cut $CUT
    done
done
