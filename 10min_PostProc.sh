
echo "--"

while [ 1 ];do
    N=`ls done_cpcard_201*.token|wc -l`
    echo "N="$N
    if [ $N -eq 2 ];then
        break
    fi
    echo "sleep 180@cpcards"
    sleep 180

done
python Tools/FixRateParams_condor.py &> logs/FixRateParams_condor.log

##--CombineProc--##
while [ 1 ];do
    N=`ls WORKDIR_FixRateParam/Datacards_201*/*/*.jid|wc -l`
    if [ $N -eq 0 ];then
	break
    fi    
    echo "sleep 180 @ FixRateParam"
    sleep 180
done


