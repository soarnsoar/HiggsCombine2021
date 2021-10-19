##--setup
git clone git@github.com:soarnsoar/python_tool.git
##--Procedure
1) Copy raw datacards
->Datacards_2016 Datacards_2017 Datacards_2018
1-1)Check Empty bins using
ValidateDatacards.py --printLevel 3 <card path>
Check "emptyBkgBin" in json or printed messages
2) Submit_CombineCard.sh
3) Submit_Workspace.sh
4) Submit_AsymptoticLimits.sh



5)collect limits
CollectLimits.sh

6)RunJsonToTF1.sh