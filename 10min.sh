

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

source Submit_Workspace.sh
sleep 60
while [ 1 ];do
    N=`ls WORKDIR/MakeWorkSpace/model_indep_NoI/*/*jid|wc -l`
    if [ $N -eq 0 ];then
        break
    fi
    echo $N
    echo "sleep 180@WS"
    sleep 180
    
done
source Submit_AsymptoticLimits.sh
sleep 60
while [ 1 ];do
    N=`ls WORKDIR/AsymptoticLimits/model_indep_NoI/*/*/*jid|wc -l`
    if [ $N -eq 0 ];then
        break
    fi
    echo $N
    echo "sleep 180@Asymp"
    sleep 180
    
done
source CollectLimits.sh

