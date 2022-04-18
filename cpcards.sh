#VBF_OPT_22_V10
ARR_BST=(Boosted Resolved)
for BST in ${ARR_BST[@]};do
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2016/Datacards_${BST} Datacards_${BST}_2016&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2017/Datacards_${BST} Datacards_${BST}_2017&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/2018/Datacards_${BST} Datacards_${BST}_2018&
    

done

    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2016/Datacards_Boosted Datacards_2016_Boosted_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR2017/Datacards_Boosted Datacards_2017_Boosted_SB&
    cp -r /cms_scratch/jhchoi/VBF_OPT_22_V10/WJETCR/2018/Datacards_Boosted Datacards_2018_Boosted_SB&
