##--setup
git clone git@github.com:soarnsoar/python_tool.git
##--Procedure
1) Copy raw datacards
->Datacards_2016 Datacards_2017 Datacards_2018
2)CombineCards
source script/runCombineCards.sh
2-1)rm autoMCstat for MC bins
3-1)WS
source script/runWS.sh
3)Scan 1sigma roughly
source RunLikelihoodScan1Sigma.sh
4)Then, 2*nll scan
source RunLikelihoodScanNLLEach.sh