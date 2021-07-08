##--setup
git clone git@github.com:soarnsoar/python_tool.git
##--Procedure
1) Copy raw datacards
->Datacards_2016 Datacards_2017 Datacards_2018
2) Submit_CombineCard.sh
3) Submit_Workspace.sh
4) Submit_AsymptoticLimits.sh



5)collect limits
combineTool.py -M CollectLimits -i higgsCombine*.root -o indep.json

6)RunJsonToTF1.sh