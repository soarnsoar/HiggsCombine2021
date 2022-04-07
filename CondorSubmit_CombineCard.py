import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,cut):
    cats={}
    mass=str(mass)
    year=str(year)

    if cut=="nocut":
        cats["hww_lqq_bst_sb_"+year]="Datacard_M"+mass+"/__BoostedALL_SB_nomekdcut/Event/datacard.txt"
        cats["hww_lqq_bst_top_"+year]="Datacard_M"+mass+"/__BoostedALL_TOP_nomekdcut/Event/datacard.txt"
        cats["hww_lqq_bst_"+year]="Datacard_M"+mass+"/__BoostedALL_SR_nomekdcut/WW_mass/datacard.txt"

        ##nocut
        cats["hww_lqq_res_sb_"+year]="Datacard_M"+mass+"/___ResolvedALL__SB_nomekdcut/Event/datacard.txt"
        cats["hww_lqq_res_top_"+year]="Datacard_M"+mass+"/___ResolvedALL__TOP_nomekdcut/Event/datacard.txt"
        cats["hww_lqq_res_"+year]="Datacard_M"+mass+"/___ResolvedALL__SR_nomekdcut/WW_mass/datacard.txt"
    else:
        #BoostedGGF_SB0
        cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/BoostedGGF_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/BoostedGGF_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/BoostedGGF_SR"+cut+"/WW_mass/datacard.txt"

        cats["hww_lqq_bst_untag_sb_"+year]="Datacard_M"+mass+"/BoostedUNTAG_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_untag_top_"+year]="Datacard_M"+mass+"/BoostedUNTAG_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_untag_"+year]="Datacard_M"+mass+"/BoostedUNTAG_SR"+cut+"/WW_mass/datacard.txt"

        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/BoostedVBF_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/BoostedVBF_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/BoostedVBF_SR"+cut+"/WW_mass/datacard.txt"


        cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/ResolvedGGF_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/ResolvedGGF_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/ResolvedGGF_SR"+cut+"/WW_mass/datacard.txt"

        cats["hww_lqq_untag_sb_"+year]="Datacard_M"+mass+"/ResolvedUNTAG_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_untag_top_"+year]="Datacard_M"+mass+"/ResolvedUNTAG_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_untag_"+year]="Datacard_M"+mass+"/ResolvedUNTAG_SR"+cut+"/WW_mass/datacard.txt"

        cats["hww_lqq_vbf_sb_"+year]="Datacard_M"+mass+"/ResolvedVBF_SB"+cut+"/Event/datacard.txt"
        cats["hww_lqq_vbf_top_"+year]="Datacard_M"+mass+"/ResolvedVBF_TOP"+cut+"/Event/datacard.txt"
        cats["hww_lqq_vbf_"+year]="Datacard_M"+mass+"/ResolvedVBF_SR"+cut+"/WW_mass/datacard.txt"
        
        
        



        
    return cats

def GetCombineCardCommands(mass,year,bst,cut=True):
    cats={}

    cats=GetCardPath(mass,year,cut)
    

    command="combineCards.py -S "
    for cat in cats:
        if bst!="all":
            if not bst in cats[cat] : continue
        command+=cat+"="+cats[cat]+" "


    print command
    return command

if __name__ == '__main__':
    #GetCommands(1000,2016)
    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option("-y", "--year", dest="year" , help="year")
    parser.add_option("-m", "--mass", dest="mass" , help="mass")
    parser.add_option("-b", "--bst", dest="bst" , help="bst")
    parser.add_option("-c", "--cut", dest="cut" , help="cut")
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    cut=(options.cut)
    ##--fix mass
    mass='1000'
    

    cc_command=GetCombineCardCommands(mass,year,bst,cut)+'> combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'__CUT_'+cut+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__cut_"+cut+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    jobname=workdir
    jobname='CombineDatacards'
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
