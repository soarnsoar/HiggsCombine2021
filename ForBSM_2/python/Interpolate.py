class Interpolate:
    def __init__(self):
        True
    def Eval(self,mH,m1,r1,m2,r2):
        #w1*m1+w2*m2=mH
        #w1+w2=1
        #w2=1-w1
        #w1*m1+(1-w1)*m2=mH
        #w1(m1-m2)+m2=mH
        w1=(mH-m2)/(m1-m2)
        w2=(m1-mH)/(m1-m2)
        r=w1*r1 + w2*r2
        return r
