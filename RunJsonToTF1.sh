#JsonToTF1.py

ARR_JSON=($(ls AsymptoticLimits/201*/*/*/*.json))

for JSON in ${ARR_JSON[@]};do
    
    python JsonToTF1.py ${JSON}

done
