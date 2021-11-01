####
import sys
import json

myjson=sys.argv[1]
with open(myjson) as f:
    data = json.load(f)
    print sorted(data)
    #u'largeNormEff', u'smallShapeEff', u'uncertTemplSame', u'uncertVarySameDirect']
    print sorted(data['largeNormEff'])
    print sorted(data['uncertVarySameDirect'])
