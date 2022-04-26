

while [ 1 ];do
    N=`ls WORKDIR/CombineCard/*//*jid|wc -l`
    if [ $N -eq 0 ];then
        break
    fi
    echo $N
    echo "sleep 180@CombineCard"
    sleep 180
    
done
python Tools/FixRateParamsCombinedCard.py

source Submit_Workspace.sh &> logs/Submit_Workspace.log

while [ 1 ];do
    N=`ls WORKDIR/MakeWorkSpace/model_indep_NoI/*/*jid|wc -l`
    if [ $N -eq 0 ];then
        break
    fi
    echo $N
    echo "sleep 180@WS"
    sleep 180
    
done
source Submit_AsymptoticLimits.sh &> logs/Submit_AsymptoticLimits.log

source CollectLimits.sh &> logs/CollectLimits.log

