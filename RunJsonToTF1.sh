#JsonToTF1.py

ARR_JSON=($(ls AsymptoticLimits/201*/*/*/*/*/*.json))

for JSON in ${ARR_JSON[@]};do
    
    python Tools/JsonToTF1.py ${JSON}

done
