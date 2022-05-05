ARR_BST=(Boosted Resolved)
#ARR_BST=(Resolved)
ARR_YEAR=(2016 2017 2018 )

for YEAR in ${ARR_YEAR[@]};do
    for BST in ${ARR_BST[@]};do
	source Submit_Workspace_arg.sh ${YEAR} ${BST} &> logs/Submit_Workspace_arg.${YEAR}.${BST}.log&

    done
done
