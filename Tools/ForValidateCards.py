####
import sys
import json

myjson=sys.argv[1]
if len(sys.argv)>2:
    onlysig=sys.argv[2]
with open(myjson) as f:
    data = json.load(f)
    print sorted(data)
    #u'largeNormEff', u'smallShapeEff', u'uncertTemplSame', u'uncertVarySameDirect']
    #cats=["largeNormEff","uncertVarySameDirect"]
cats=["uncertVarySameDirect"]

for cat in cats:
        #print "----largeNormEff---"
        print "---",cat,"---"
        #print sorted(data['largeNormEff'])
        for n in sorted(data[cat]):
            #print ">>",n
            for c in data[cat][n]:
                #print cat,'/',n,'/',c
                plist=[]
                for p in data[cat][n][c]:
                    if not 'RelW' in p : continue
                    #print p
                    plist.append(str(p))
                #print sorted(data[cat][n][c])
                if len(plist)>0:
                    print n,plist
    #print "----uncertVarySameDirect---"
    #print sorted(data['uncertVarySameDirect'])
    #for n in sorted(data['uncertVarySameDirect']):
    #    print n
