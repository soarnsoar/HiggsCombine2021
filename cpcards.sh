mkdir -p Datacards_2016
mkdir -p Datacards_2017
mkdir -p Datacards_2018

#/cms_scratch/jhchoi/ANv10/FinCut/FinCut__15Job__BtagModuleSplit
MAINDIR=/cms_scratch/jhchoi/ANv11/FinalCut/

BST=Resolved
cp -r ${MAINDIR}/2016/Datacards_${BST} Datacards_2016/Datacards_${BST}_2016&
cp -r ${MAINDIR}/2017/Datacards_${BST} Datacards_2017/Datacards_${BST}_2017&
cp -r ${MAINDIR}/2018/Datacards_${BST} Datacards_2018/Datacards_${BST}_2018&
    



BST=Boosted
cp -r ${MAINDIR}/2016/Datacards_${BST} Datacards_2016/Datacards_${BST}_2016&
cp -r ${MAINDIR}/2017/Datacards_${BST} Datacards_2017/Datacards_${BST}_2017&
cp -r ${MAINDIR}/2018/Datacards_${BST} Datacards_2018/Datacards_${BST}_2018&

cp -r ${MAINDIR}/WJETCR/2016/Datacards_Boosted Datacards_2016/Datacards_Boosted_2016_SB&
cp -r ${MAINDIR}/WJETCR/2017/Datacards_Boosted Datacards_2017/Datacards_Boosted_2017_SB&
cp -r ${MAINDIR}/WJETCR/2018/Datacards_Boosted Datacards_2018/Datacards_Boosted_2018_SB&

