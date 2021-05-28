import os


def GetCardPath(mass,year):
    cats={}
    mass=str(mass)
    year=str(year)
    ##--Boosted
    cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_MEKDTAG_M1500_C0.01/Event/datacard.txt"
    cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_MEKDTAG_M1500_C0.01/Event/datacard.txt"
    cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01/WW_mass/datacard.txt"
    
    cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SB_NoMEKDCut/Event/datacard.txt"
    cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SB_NoMEKDCut/Event/datacard.txt"
    cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SB_NoMEKDCut/WW_mass/datacard.txt"
    
    cats["hww_lqq_bst_untag_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_UNTAGGED_M1500_C0.01/Event/datacard.txt"
    cats["hww_lqq_bst_untag_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_UNTAGGED_M1500_C0.01/Event/datacard.txt"
    cats["hww_lqq_bst_untag_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01/WW_mass/datacard.txt"

    ##--Resolved
    cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_MEKDTAG_M400_C0.01/Event/datacard.txt"
    cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_MEKDTAG_M400_C0.01/Event/datacard.txt"
    cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.01/WW_mass/datacard.txt"
    
    cats["hww_lqq_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SB_NoMEKDCut/Event/datacard.txt"
    cats["hww_lqq_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SB_NoMEKDCut/Event/datacard.txt"
    cats["hww_lqq_vbf_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SB_NoMEKDCut/WW_mass/datacard.txt"
    
    cats["hww_lqq_untag_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_UNTAGGED_M400_C0.01/Event/datacard.txt"
    cats["hww_lqq_untag_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_UNTAGGED_M400_C0.01/Event/datacard.txt"
    cats["hww_lqq_untag_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_UNTAGGED_M400_C0.01/WW_mass/datacard.txt"

    return cats

def GetCombineCardCommands(mass,year,bst='all'):

    cats=GetCardPath(mass,year)
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
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst

    

    cc_command=GetCombineCardCommands(mass,year,bst)+'> combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__"+year
    
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    jobname=workdir
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
