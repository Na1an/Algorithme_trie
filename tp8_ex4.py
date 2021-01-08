#!/usr/bin/env python3

#importe indirectement tp8, data, et tp8_ex* pour * < 3
from tp8_ex3 import *

#
# A COMPLETER !
#
def generer2ABR(per):
    return arbreVide

#
# A COMPLETER !
#
def stat2ABR(n,m):
    return 0



#
# NE PAS MODIFIER
#
def tracer(limite,pas,m):
    l1 = []
    l2 = []
    for i in range(1,limite,pas):
        l1.append(i)
        print("Calcul pour n = %d"%i)
        l2.append(stat2ABR(i,m))
    plt.plot(l1,l2)
    plt.ylabel('hauteur(n)')
    plt.xlabel('n = nombre noeuds')
    plt.show()
    return ()

if __name__ == '__main__':
    tracer(100,10,10)
