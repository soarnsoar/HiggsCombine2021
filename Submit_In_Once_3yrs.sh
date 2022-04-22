ARR_MASS=(115 120 124 125 126 130 135 140 145 150 155 160 165 170 175 180 190 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)

WTAG=$1

CURDIR=$PWD
for MASS in ${ARR_MASS[@]};do
    #HP/Datacards_2016/Datacard_M1000/FullCutSR/WW_mass/
    command="cd ${CURDIR}/${WTAG}/&&combineCards.py -S y2016=Datacards_2016/Datacard_M${MASS}/FullCutSR/WW_mass/datacard.txt y2017=Datacards_2017/Datacard_M${MASS}/FullCutSR/WW_mass/datacard.txt y2018=Datacards_2018/Datacard_M${MASS}/FullCutSR/WW_mass/datacard.txt &> combine_M${MASS}.txt &&text2workspace.py combine_M${MASS}.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.XWWInterference_jhchoi:XWW  --PO noInterference -o WS_M${MASS}.root&&combine -M AsymptoticLimits -d WS_M${MASS}.root -m ${MASS} --freezeParameters fvbf --setParameters fvbf=0 --rAbsAcc 0 -n ggfonly&&combine -M AsymptoticLimits -d WS_M${MASS}.root -m ${MASS} --freezeParameters fvbf --setParameters fvbf=1 --rAbsAcc 0 -n vbfonly"
    python python_tool/ExportShellCondorSetup.py -c "$command" -d "WORKDIR/${WTAG}/3yrs/M${MASS}" -n "asymp" -m 1 -s 
done
