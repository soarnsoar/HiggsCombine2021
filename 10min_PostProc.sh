
echo "--"

while [ 1 ];do
    N=`ls done_cpcard_201*.token|wc -l`
    echo "N="$N
    if [ $N -eq 3 ];then
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

source Submit_CombineCard.sh &> logs/Submit_CombineCard.log
##---CombineCard
while [ 1 ];do
    N=`ls WORKDIR/CombineCard/*/*jid|wc -l`
    if [ $N -eq 0 ];then
	break
    fi    
    echo "sleep 180 @ CombineCard"
    sleep 180
done


source Submit_Workspace.sh &> logs/Submit_Workspace.log

##---WorkSpace
while [ 1 ];do
    N=`ls WORKDIR/MakeWorkSpace/model_indep_NoI/M*/*/*/*jid|wc -l`
    if [ $N -eq 0 ];then
	break
    fi    
    echo "sleep 180 @ WorkSpace"
    sleep 180
done


source Submit_AsymptoticLimits.sh &> logs/Submit_AsymptoticLimits.log&
source Submit_HybridNew.sh &> logs/Submit_HybridNew.log&
