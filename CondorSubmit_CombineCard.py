import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year,cut):
    cats={}
    mass=str(mass)
    year=str(year)
    #__BoostedALL_SB_VBFCUT_0.3
    CRVAR="WW_mass"
    SRVAR="WW_mass"
    #Datacards_Boosted_2016/Datacard_M1000/SR__VBFCUT0.1
    #TOPCR__VBFCUT0.1
    #Datacards_Boosted_2016_SB/Datacard_M1000/WJETCR__VBFCUT0.1
    #Datacards_2016/Datacards_Boosted_2016/Datacard_M1000/SR__VBFCUT0.1
    #Datacards_2016/Datacards_Boosted_2016_SB/Datacard_M1000/WJETCR__VBFCUT0.1
    #Datacards_2016/Datacards_Resolved_2016/Datacard_M1000/SR__VBFCUT0.8
    if cut=="nocut":
        cats["hww_lqq_bst_vbf_sb_"+year]="Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/WJETCR/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/TOPCR/"+ CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/SR/"+ CRVAR+"/datacard.txt"


        #notcut
        cats["hww_lqq_res_vbf_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/WJETCR/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_res_vbf_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/TOPCR/" +CRVAR+"/datacard.txt"
        cats["hww_lqq_res_vbf_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/SR/"    +CRVAR+"/datacard.txt"
    else:

        cats["hww_lqq_bst_vbf_sb_"+year]= "Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/WJETCR__VBFTAG"+cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_vbf_top_"+year]="Datacards_Boosted_"+year+    "/Datacard_M"+mass+"/TOPCR__VBFTAG" +cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_vbf_"+year]=    "Datacards_Boosted_"+year+    "/Datacard_M"+mass+"/SR__VBFTAG"    +cut+"/"+CRVAR+"/datacard.txt"

        cats["hww_lqq_res_vbf_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/WJETCR__VBFTAG"+cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_res_vbf_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/TOPCR__VBFTAG" +cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_res_vbf_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/SR__VBFTAG"   +cut+"/"+CRVAR+"/datacard.txt"
        ##--untag
        cats["hww_lqq_bst_untag_sb_"+year]= "Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/WJETCR__VBFUNTAG"+cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_untag_top_"+year]="Datacards_Boosted_"+year+    "/Datacard_M"+mass+"/TOPCR__VBFUNTAG" +cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_bst_untag_"+year]=    "Datacards_Boosted_"+year+    "/Datacard_M"+mass+"/SR__VBFUNTAG"    +cut+"/"+CRVAR+"/datacard.txt"

        cats["hww_lqq_res_untag_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/WJETCR__VBFUNTAG"+cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_res_untag_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/TOPCR__VBFUNTAG" +cut+"/"+CRVAR+"/datacard.txt"
        cats["hww_lqq_res_untag_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/SR__VBFUNTAG"   +cut+"/"+CRVAR+"/datacard.txt"


        



        
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
