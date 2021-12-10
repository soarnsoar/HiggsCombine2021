import os
def FixRateParam(DC):
    f=open(DC,'r')
    fnew=open(DC+'_new','w')
    lines=f.readlines()
    for line in lines:

        if ("rateParam" in line) and not ('1 [0,5]' in line):
            newline_inlist=line.split()[:-1]+['1 [0,5]\n']
            line='  '.join(newline_inlist)

        fnew.write(line)
    f.close()
    fnew.close()
    os.system('mv '+DC+' '+DC+'_old_rateparam')
    os.system('mv '+DC+'_new'+' '+DC)
if __name__ == '__main__':
    import sys
    DCpath=sys.argv[1]
    FixRateParam(DCpath)
