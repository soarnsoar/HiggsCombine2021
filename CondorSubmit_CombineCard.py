import os

##---------------------------------Card Config----------------------##
def GetCardPath(mass,year):
    cats={}
    mass=str(mass)
    year=str(year)

    CRVAR="WW_mass"
    SRVAR="WW_mass"


    #Boosted
    cats["hww_lqq_bst_vbf_sb_"+year]="Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/Boosted__WJETCR__VBF/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_vbf_top_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__TOPCR__VBF/"+ CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_vbf_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__SR__VBF/"+ CRVAR+"/datacard.txt"

    cats["hww_lqq_bst_ggf_sb_"+year]="Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/Boosted__WJETCR__GGF/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_ggf_top_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__TOPCR__GGF/"+ CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_ggf_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__SR__GGF/"+ CRVAR+"/datacard.txt"

    cats["hww_lqq_bst_untag_sb_"+year]="Datacards_Boosted_"+year +"_SB/Datacard_M"+mass+"/Boosted__WJETCR__UNTAG/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_untag_top_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__TOPCR__UNTAG/"+ CRVAR+"/datacard.txt"
    cats["hww_lqq_bst_untag_"+year]="Datacards_Boosted_"+year+   "/Datacard_M"+mass+"/Boosted__SR__UNTAG/"+ CRVAR+"/datacard.txt"


    

    #Resolved
    cats["hww_lqq_res_vbf_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__WJETCR__VBF/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_res_vbf_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__TOPCR__VBF/" +CRVAR+"/datacard.txt"
    cats["hww_lqq_res_vbf_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__SR__VBF/"    +CRVAR+"/datacard.txt"

    cats["hww_lqq_res_ggf_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__WJETCR__GGF/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_res_ggf_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__TOPCR__GGF/" +CRVAR+"/datacard.txt"
    cats["hww_lqq_res_ggf_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__SR__GGF/"    +CRVAR+"/datacard.txt"

    cats["hww_lqq_res_untag_sb_"+year]= "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__WJETCR__UNTAG/"+CRVAR+"/datacard.txt"
    cats["hww_lqq_res_untag_top_"+year]="Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__TOPCR__UNTAG/" +CRVAR+"/datacard.txt"
    cats["hww_lqq_res_untag_"+year]=    "Datacards_Resolved_"+year+"/Datacard_M"+mass+"/Resolved__SR__UNTAG/"    +CRVAR+"/datacard.txt"




        



        
    return cats

def GetCombineCardCommands(mass,year,bst):
    cats={}

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
    os.system('mkdir -p Datacards_'+year)
    commands=["cd "+os.getcwd()+'/Datacards_'+year,cc_command]


    ##--Add Validation and Rebinning
    cardpath='combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'.txt'
    vjson='combine_hwwlnuqq_'+bst+'_'+mass+'_'+year+'.json'
    #--1)Validation
    valcom='ValidateDatacards.py '+cardpath+' --jsonFile '+vjson
    commands.append(valcom)
    #--2)Rebinning
    RebinningScript=os.getcwd()+'/python_tool/HC/RebinningTool.py'
    rebincom='python '+RebinningScript+' '+cardpath+' '+vjson
    commands.append(rebincom)


    command='&&'.join(commands)
    
    jobname=workdir
    jobname='CombineDatacards'
    submit=True
    ncpu=1


    Export(workdir,command,jobname,submit,ncpu)
