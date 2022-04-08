#python Rebinning/Rebinning.py Rebinning/RP/Boosted2016_0.py 
ARR_CONF=( $(ls Rebinning/RP/*.py))

for CONF in ${ARR_CONF[@]};do
    python Rebinning/Rebinning.py ${CONF}
done
