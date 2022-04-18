mkdir -p Datacards

#VBF_OPT_22_V10
ARR_BST=(Boosted Resolved)
for BST in ${ARR_BST[@]};do
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2016/Datacards_${BST} Datacards/Datacards_${BST}_2016&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2017/Datacards_${BST} Datacards/Datacards_${BST}_2017&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2018/Datacards_${BST} Datacards/Datacards_${BST}_2018&
    

done

    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2016/Datacards_Boosted Datacards/Datacards_Boosted_2016_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2017/Datacards_Boosted Datacards/Datacards_Boosted_2017_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2018/Datacards_Boosted Datacards/Datacards_Boosted_2018_SB&
