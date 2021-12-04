import os

#__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01__cut_0.0
#___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.001__cut0.0
##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,WP,isDNN=True):
    cats={}
    mass=str(mass)
    year=str(year)
    if isDNN:
        ##--Boosted
        cats["hww_lqq_bst_ggf_sb_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN__SB_MEKDTAG_M1500_C0.01__cut_/"+WP+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_top_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN__TOP_MEKDTAG_M1500_C0.01__cut_/"+WP+"/Event/datacard.txt"
        cats["hww_lqq_bst_ggf_"+year]="Datacard_M"+mass+"/__BoostedGGFDNN__SR_MEKDTAG_M1500_C0.01__cut_/"+WP+"/WW_mass/datacard.txt"

        ##--Resolved
        cats["hww_lqq_ggf_sb_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SB_MEKDTAG_M400_C0.001__cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_ggf_top_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__TOP_MEKDTAG_M400_C0.001__cut"+WP+"/Event/datacard.txt"
        cats["hww_lqq_ggf_"+year]="Datacard_M"+mass+"/___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.001__cut"+WP+"/WW_mass/datacard.txt"

    else:
        print 1/0
        
    return cats

def GetCombineCardCommands(mass,year,bst,WP,isDNN=True):
    cats={}
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
    
    print "cats=",cats
    print "bst=",bst
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
    parser.add_option("-w", "--wp", dest="wp" , help="wp")
    parser.add_option("-d", "--dnn", dest="dnn" , help="dnn",action='store_true',)
    (options, args) = parser.parse_args()

    year=options.year
    mass=options.mass
    bst=options.bst
    wp=options.wp
    dnn=bool(options.dnn)

    

    cc_command=GetCombineCardCommands(mass,year,bst,wp,dnn)+'> combine_hwwlnuqq_'+bst+'_'+wp+'_'+mass+'_'+year+'.txt'

    
    #Export(workdir,command,jobname,submit,ncpu)
    import sys
    sys.path.insert(0, "python_tool/")
    from ExportShellCondorSetup import Export
    workdir="WORKDIR/CombineCard/"+mass+"__"+bst+"__"+wp+"__"+year
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]
    command=';'.join(commands)
    
    #jobname=workdir
    jobname="combinecard"
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
