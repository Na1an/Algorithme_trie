def fusionIterative(T1,T2):
    '''
    归并排列，所取的T1T2都是已经排列好的
    '''
    l1,l2 = len(T1),len(T2)
    res = [0]*(l1+l2)
    i1,i2 = 0,0
    nbInv = 0

    while i1<l1 and i2 < l2:
        if T1[i1]>T2[i2]:
            res[i1+i2] = T2[i2]
            i2+=1
            nbInv += l1 - i1
        else:
            res[i1+i2] = T1[i1]
            i1+=1
    while i1<l1:
        res[i1+i2] = T1[i1]
        i1+=1
    while i2<l2:
        res[i1+i2]=T2[i2]
        i2+=1
    return res,nbInv



def triFusionCompteInv(T):
    if len(T) == 1 :
        return [T[0]],0
    T1,T2 = T[:len(T)//2],T[len(T)//2:]
    res1,nb1 = triFusionCompteInv(T1)
    res2,nb2 = triFusionCompteInv(T2)

    res,nbFus = fusionIterative(res1,res2)
    return res,(nb1+nb2+nbFus)
