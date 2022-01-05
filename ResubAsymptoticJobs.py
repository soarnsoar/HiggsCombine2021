##---For Kisti...
import glob
import os
import sys
sys.path.insert(0, "python_tool/latino/")

from GetNJobs import GetNJobs,GetNJobsByName,GetN_RUNNING_IDLE_JobsByName

nmaxjob=1200

def GetJid(jidfile):
    if not os.path.isfile(jidfile):
        jidfile=jidfile.replace(".jid",".done")
    f=open(jidfile,'r')
    lines=f.readlines()
    jid=False
    for line in lines:
        #submitted to cluster 15064801
        if "submitted to cluster" in line:
            jid=int(line.split("to cluster")[1].replace(".",""))
    f.close()
    return jid

def CheckLog(logfile, jid):
    f=open(logfile,'r')
    lines=f.readlines()
    Terminated=False
    Evicted=False
    for line in lines:
        if 'Job was evicted' in line and str(jid) in line:
            Evicted=True
        if 'Job terminated' in line and str(jid) in line:
            Terminated=True
        if 'Job was aborted' in line and str(jid) in line:
            Terminated=True
    return Evicted, Terminated



##-----START----##
logger=open("logs/ResubLog.txt","w")
DIRLIST=glob.glob("WORKDIR/*Limits/*/*/")

#ncurrentjob=int(GetN_RUNNING_IDLE_JobsByName('mkShapes'))

for DIR in DIRLIST:
    print DIR    
    SHLIST=glob.glob(DIR+"/"+"*/*/*sh")
    njobs=len(SHLIST)
    print "njobs=",njobs
    ndone=0
    nresub=0
    resublist=[]
    for SH in SHLIST:
        #print SH
        name=SH.rstrip(".sh")
        jidfile=name+".jid"
        jdsfile=name+".jds"
        donefile=name+".done"
        logfile=name+".log"
        jid=GetJid(jidfile)
        Evicted, Terminated=CheckLog(logfile,jid)
        Done=os.path.isfile(donefile)
        if Done :
            ndone+=1
            continue
        if Evicted:
            resublist.append(name)
            print "---Evicted---"
            print name
            condor_rm="condor_rm "+str(jid)
            print condor_rm
            os.system(condor_rm)
            #resub="condor_submit "+jdsfile + " > " +jidfile
            #print resub
            #os.system(resub)
            #nresub+=1
            print "-------------"
        elif Terminated:
            resublist.append(name)
            print "---Terminated---"
            print name
            condor_rm="condor_rm "+str(jid)
            print condor_rm
            os.system(condor_rm)
            #resub="condor_submit "+jdsfile + " > " +jidfile
            #print resub
            #os.system(resub)
            nresub+=1
            print "-------------"
    print "ndone=",ndone
    print "nresub=",nresub
    ncurrentjob=int(GetN_RUNNING_IDLE_JobsByName('AsymptoticLimits'))
    print "ncurrentjob=",ncurrentjob
    print "nmaxjob=",nmaxjob
    logger.write("ncurrentjob="+str(ncurrentjob)+"\n")
    logger.write("nmaxjob="+str(nmaxjob)+"\n")
    if ncurrentjob<nmaxjob:
        for name in resublist:
            logger.write("----"+name+"----\n")
            jidfile=name+".jid"
            jdsfile=name+".jds"
            donefile=name+".done"
            logfile=name+".log"
            jid=GetJid(jidfile)
            condor_rm="condor_rm "+str(jid)
            print condor_rm
            logger.write(condor_rm+"\n")

            os.system(condor_rm)


            resub="condor_submit "+jdsfile + " > " +jidfile
            print resub
            logger.write(resub+"\n")

            os.system(resub)
