##--Procedure
1) Copy raw datacards
2) Submit_CombineCard.sh
3) Submit_Workspace.sh
4) Submit_AsymptoticLimits.sh



5)collect limits
combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json

6)RunJsonToTF1.sh