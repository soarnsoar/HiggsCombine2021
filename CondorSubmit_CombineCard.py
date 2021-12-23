import os

#__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.2     ___ResolvedGGFDNN__SB_MEKDTAG_M400_C0.2
##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,MELA_MASS,C,WP,isBoosted):
    cats={}
    mass=str(mass)
    year=str(year)
    if isBoosted:
        ##--Boosted
        #__BoostedGGFDNN_TOP_UNTAGGED_M400_C0.02_cut0.0
        #__BoostedGGFDNN_SB_MEKDTAG_M1500_C0.0001_cut0.85
        cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/WW_mass/datacard.txt"
        if WP!='0.0':
            cats["hww_lqq_bst_untag_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SB_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
            cats["hww_lqq_bst_untag_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_TOP_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
            cats["hww_lqq_bst_untag_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN_SR_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/WW_mass/datacard.txt"
    else:
        ##--Resolved
        cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_MEKDTAG_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/WW_mass/datacard.txt"
        if WP!='0.0':
            cats["hww_lqq_untag_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
            cats["hww_lqq_untag_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/Event/datacard.txt"
            cats["hww_lqq_untag_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_UNTAGGED_M"+MELA_MASS+"_C"+C+"_cut"+WP+"/WW_mass/datacard.txt"



        
    return cats
#GetCombineCardCommands(mass,year,mela_m,c,wp,bst)
def GetCombineCardCommands(mass,year,mela_m,c,WP,bst):
    cats={}
    '''
    if year=="3yrs":
        cats2016=GetCardPath(mass,2016,WP,isDNN)
        cats2017=GetCardPath(mass,2017,WP,isDNN)
        cats2018=GetCardPath(mass,2018,WP,isDNN)
        

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
        print "year=",year
        cats=GetCardPath(mass,year,WP,isDNN)
    '''
    #GetCardPath(mass,year,MELA_MASS,C,WP,isBoosted)
    if "Boosted" in bst:
        isBoosted=True
    else:
        isBoosted=False
    #def GetCardPath(mass,year,MELA_MASS,C,WP,isBoosted):
    cats=GetCardPath(mass,year,mela_m,c,WP,isBoosted)
    print "cats=",cats
    print "bst=",bst
    command="combineCards.py -S "
    for cat in cats:
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
    parser.add_option("-w", "--wp", dest="wp" , help="wp")
    parser.add_option("-c", "--c", dest="c" , help="c")
    parser.add_option("-p", "--mela_m", dest="mela_m" , help="mela_m")
    #    parser.add_option("-d", "--dnn", dest="dnn" , help="dnn",action='store_true',)

    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    wp=options.wp
    c=options.c
    mela_m=options.mela_m
    
    #def GetCardPath(mass,year,MELA_MASS,C,WP,isBoosted):
    #def GetCombineCardCommands(mass,year,mela_m,c,WP,bst):
    cc_command=GetCombineCardCommands(mass,year,mela_m,c,wp,bst)+'> combine_hwwlnuqq_'+bst+'_M'+mela_m+"_"+"c"+c+"_"+wp+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__M"+mela_m+"__C"+c+"__"+wp+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    #jobname=workdir
    jobname="combinecard"
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
