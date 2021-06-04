#!/bin/bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export SCRAM_ARCH=slc7_amd64_gcc700
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Combinato/HighMassH/CMSSW_10_2_13
eval `scramv1 ru -sh`
cd /cms_scratch/jhchoi/HiggsComb/HiggsCombine2021/ForBSM/WORKDIR/MakeWorkSpace/200__all__2016__input_qqH_xsec:0
(cd /cms_scratch/jhchoi/HiggsComb/HiggsCombine2021/ForBSM;mkdir -p Workspaces_2016;text2workspace.py Datacards_2016/combine_hwwlnuqq_all_200_2016.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.XWWInterference_jhchoi:XWW --PO NoSMXsecAdded --PO input_qqH_xsec:0 -o Workspaces_2016/hwwlnuqq_all_200_2016_input_qqH_xsec:0.root)
myerr=$?
ntry=1
echo "myerr=$myerr"
while [ $myerr -ne 0 ]
do
ntry=`expr $ntry + 1`
(cd /cms_scratch/jhchoi/HiggsComb/HiggsCombine2021/ForBSM;mkdir -p Workspaces_2016;text2workspace.py Datacards_2016/combine_hwwlnuqq_all_200_2016.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.XWWInterference_jhchoi:XWW --PO NoSMXsecAdded --PO input_qqH_xsec:0 -o Workspaces_2016/hwwlnuqq_all_200_2016_input_qqH_xsec:0.root)
myerr=$?
echo ntry="$ntry"
echo "myerr=$myerr"
if [ $ntry -gt 3 ]
then
break
fi
done
echo "[ntry=$ntry]"
if [ $myerr -eq 0 ]
then
mv /cms_scratch/jhchoi/HiggsComb/HiggsCombine2021/ForBSM/WORKDIR/MakeWorkSpace/200__all__2016__input_qqH_xsec:0/run.jid /cms_scratch/jhchoi/HiggsComb/HiggsCombine2021/ForBSM/WORKDIR/MakeWorkSpace/200__all__2016__input_qqH_xsec:0/run.done
fi
