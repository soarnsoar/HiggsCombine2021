import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,isDNN=True):
    cats={}
    mass=str(mass)
    year=str(year)
    if isDNN:
        dict_MEKDWP={
            'Boosted':{
                '2016':'M1500_C0.05',
                '2017':'M900_C0.2',
                '2018':'M1500_C0.05',
            },
            'Resolved':{
                '2016':'M200_C0.0008',
                '2017':'M200_C0.0008',
                '2018':'M200_C0.0008',
            }
        }
        ##--Boosted
        #M1500_C0.05
        #M900_C0.2
        #M1500_C0.05
        cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_MEKDTAG_"+dict_MEKDWP['Boosted'][year]+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_MEKDTAG_"+dict_MEKDWP['Boosted'][year]++"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_MEKDTAG_"+dict_MEKDWP['Boosted'][year]++"/WW_mass/datacard.txt"
        
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedVBFDNN_SR_NoMEKDCut/WW_mass/datacard.txt"
        
        cats["hww_lqq_bst_untag_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_UNTAGGED_"+dict_MEKDWP['Boosted'][year]++"/Event/datacard.txt"
        cats["hww_lqq_bst_untag_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_UNTAGGED_"+dict_MEKDWP['Boosted'][year]++"/Event/datacard.txt"
        cats["hww_lqq_bst_untag_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_UNTAGGED_"+dict_MEKDWP['Boosted'][year]++"/WW_mass/datacard.txt"
        
        ##--Resolved
        #M200_C0.0008
        #M200_C0.0008
        #M200_C0.0008
        cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_MEKDTAG_"+dict_MEKDWP['Resolved'][year]+"/Event/datacard.txt"
        cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_MEKDTAG_"+dict_MEKDWP['Resolved'][year]+"/Event/datacard.txt"
        cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_MEKDTAG_"+dict_MEKDWP['Resolved'][year]+"/WW_mass/datacard.txt"
        
        cats["hww_lqq_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_"+year]="Datacard_M"+mass+"/___ResolvedVBFDNN__SR_NoMEKDCut/WW_mass/datacard.txt"
        
        cats["hww_lqq_untag_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_UNTAGGED_"+dict_MEKDWP['Resolved'][year]+"/Event/datacard.txt"
        cats["hww_lqq_untag_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_UNTAGGED_"+dict_MEKDWP['Resolved'][year]+"/Event/datacard.txt"
        cats["hww_lqq_untag_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_UNTAGGED_"+dict_MEKDWP['Resolved'][year]+"/WW_mass/datacard.txt"
    else:
        ##--Boosted
        cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/__BoostedGGF_SB_MEKDTAG_M1500_C0.01/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/__BoostedGGF_TOP_MEKDTAG_M1500_C0.01/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/__BoostedGGF_SR_MEKDTAG_M1500_C0.01/WW_mass/datacard.txt"
        
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacard_M"+mass+"/__BoostedVBF_SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacard_M"+mass+"/__BoostedVBF_TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacard_M"+mass+"/__BoostedVBF_SR_NoMEKDCut/WW_mass/datacard.txt"
        
        cats["hww_lqq_bst_untag_sb_"+year]="Datacard_M"+mass+"/__BoostedGGF_SB_UNTAGGED_M1500_C0.01/Event/datacard.txt"
        cats["hww_lqq_bst_untag_top_"+year]="Datacard_M"+mass+"/__BoostedGGF_TOP_UNTAGGED_M1500_C0.01/Event/datacard.txt"
        cats["hww_lqq_bst_untag_"+year]="Datacard_M"+mass+"/__BoostedGGF_SR_UNTAGGED_M1500_C0.01/WW_mass/datacard.txt"
        
        ##--Resolved
        cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGF__SB_MEKDTAG_M400_C0.0025/Event/datacard.txt"
        cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/___ResolvedGGF__TOP_MEKDTAG_M400_C0.0025/Event/datacard.txt"
        cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/___ResolvedGGF__SR_MEKDTAG_M400_C0.0025/WW_mass/datacard.txt"
        
        cats["hww_lqq_vbf_sb_"+year]="Datacard_M"+mass+"/___ResolvedVBF__SB_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_top_"+year]="Datacard_M"+mass+"/___ResolvedVBF__TOP_NoMEKDCut/Event/datacard.txt"
        cats["hww_lqq_vbf_"+year]="Datacard_M"+mass+"/___ResolvedVBF__SR_NoMEKDCut/WW_mass/datacard.txt"
        
        cats["hww_lqq_untag_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGF__SB_UNTAGGED_M400_C0.0025/Event/datacard.txt"
        cats["hww_lqq_untag_top_"+year]="Datacard_M"+mass+"/___ResolvedGGF__TOP_UNTAGGED_M400_C0.0025/Event/datacard.txt"
        cats["hww_lqq_untag_"+year]="Datacard_M"+mass+"/___ResolvedGGF__SR_UNTAGGED_M400_C0.0025/WW_mass/datacard.txt"
        
    return cats

def GetCombineCardCommands(mass,year,bst,isDNN=True):
    cats={}
    if year=="3yrs":
        cats2016=GetCardPath(mass,2016,isDNN)
        cats2017=GetCardPath(mass,2017,isDNN)
        cats2018=GetCardPath(mass,2018,isDNN)
        

        for cat in cats2016:
            cats2016[cat]="../Datacards_2016/"+cats2016[cat]
        for cat in cats2017:
            cats2017[cat]="../Datacards_2017/"+cats2017[cat]
        for cat in cats2018:
            cats2018[cat]="../Datacards_2018/"+cats2018[cat]

        cats.update(cats2016)
        cats.update(cats2017)
        cats.update(cats2018)
    else:
        cats=GetCardPath(mass,year,isDNN)
    

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
    parser.add_option("-d", "--dnn", dest="dnn" , help="dnn",action='store_true',)
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    dnn=bool(options.dnn)

    

    cc_command=GetCombineCardCommands(mass,year,bst,dnn)+'> combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    jobname=workdir
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
