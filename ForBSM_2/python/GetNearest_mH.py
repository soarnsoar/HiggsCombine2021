def GetNearest_mH(mH,list_mH):
    mH_low=-9999
    mH_high=-9999

    for i in range(len(list_mH)-1):
        mH_i = list_mH[i]
        mH_i_1 = list_mH[i+1]
        if mH >=mH_i and mH < mH_i_1:
            mH_low=mH_i
            mH_high=mH_i_1

    return mH_low, mH_high
