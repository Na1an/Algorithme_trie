from time import process_time
from random import randint

def mesure_temps(f, *param, rep=1, cle=True):
    tps = 0
    for i in range(rep):
      if cle:
        x = randint(1,1000000)
        deb = process_time()
        f(x, *param)
        tps += (process_time() - deb)
      else:
        deb = process_time()
        f(*param)
        tps += (process_time() - deb)
    return tps/rep
    
def cherche1(x, I):
    #A COMPLETER
    for i in I:
        if i == x:
            return True
    return False
def cherche(x,I):
    return (x in I)

def nb_elts_diff_liste(L):
    #A COMPLETER
    
    res = triRapide(L)
    return len(res)


def partition(T):
    # les éléments sont supposés destincts
    pivot = T[0]
    gauche = [elt for elt in T if elt < pivot]
    droite = [elt for elt in T if elt > pivot]

    return pivot, gauche, droite

def triRapide(T):
    # A COMPLETER
    # 有pivot

    if len(T) < 2:
        return T
    pivot, gauche, droite = partition(T)
    return triRapide(gauche) + [pivot] + triRapide(droite)


def nb_elts_diff_ens(E):
    #A COMPLETER
    s = set()
    for i in E:
        s.add(i)
    return len(s)

def comparaison_rech(L, E):
    print()
    print("##############################################################")
    print()
    print("temps moyen d'acces a une liste de longeur", len(L),":", mesure_temps(cherche,L,rep=10))
    print("temps moyen d'acces a un ensemble de longueur", len(L),":", mesure_temps(cherche,E,rep=10))

  
def comparaison_nb_elts(L, E):
    print()
    print("##############################################################")
    print()
    print("temps moyen pour compter les elements distincts dans une liste de longeur", len(L),":", mesure_temps(nb_elts_diff_liste, L, rep=10, cle=False))
    print("temps moyen pour compter les elements distincts dans un ensemble de longueur", len(L),":", mesure_temps(nb_elts_diff_ens, E, rep=10, cle=False))
    print()
    print("##############################################################")
    print()

if __name__ == '__main__':
    L=[randint(1,1000000) for i in range(1000000)]
    E=set(L)
    comparaison_rech(L, E)
    comparaison_nb_elts(L, E)
