mkdir -p Datacards_2016
mkdir -p Datacards_2017
mkdir -p Datacards_2018

#VBF_OPT_22_V10
ARR_BST=(Boosted Resolved)
for BST in ${ARR_BST[@]};do
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2016/Datacards_${BST} Datacards_2016/Datacards_${BST}_2016&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2017/Datacards_${BST} Datacards_2017/Datacards_${BST}_2017&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2018/Datacards_${BST} Datacards_2018/Datacards_${BST}_2018&
    

done

    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2016/Datacards_Boosted Datacards_2016/Datacards_Boosted_2016_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2017/Datacards_Boosted Datacards_2017/Datacards_Boosted_2017_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2018/Datacards_Boosted Datacards_2018/Datacards_Boosted_2018_SB&
