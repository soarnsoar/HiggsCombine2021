
echo "--"

##--WS--##
while [ 1 ];do
    N=`ls WORKDIR/MakeWorkSpace/model_indep_NoI/*/*/*/*jid|wc -l`
    if [ $N -eq 0 ];then
	break
    fi    
    echo "sleep 180 @ WS"
    sleep 180
done

source Submit_HybridNew.sh &> Submit_HybridNew.log&
source Submit_AsymptoticLimits.sh &> Submit_AsymptoticLimits.log&
