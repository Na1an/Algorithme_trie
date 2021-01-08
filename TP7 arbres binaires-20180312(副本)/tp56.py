#!/usr/bin/env python3

import random
from time import clock
import matplotlib.pyplot as plt

# Exercice 1

##################
# Tri selection  #
##################
def trouveLePlusPetit(T):
    min = T[0]
    indice = 0
    for i in range(len(T)):
        if T[i] <= min :
            min = T[i]
            indice = i
    return indice

def triSelection(T):
    # A COMPLETER
    tmp = 0
    ind = 0
    for i in range(len(T)):
        ind = trouveLePlusPetit(T[i:])+i
        tmp = T[i]
        T[i] = T[ind]
        T[ind] = tmp
    return T

def randomPerm(n):
    # A COMPLETER
    T = [0]*n
    for i in range(n):
        T[i] = i+1
    for i in range(len(T)):
        ind = random.randint(i+1,len(T)) - 1
        tmp = T[i]
        T[i] = T[ind]
        T[ind] = tmp
    return T

def testeQueLaFonctionTrie(f):
    # A COMPLETER
    T = []
    for i in range(2,100):
        T = randomPerm(i)
        Tcop = T[:]
        T = f(T)
        for j in range(i):
            if (T[j] != (j+1)):
                print(Tcop)
                print(T)
                return False
    return True



def randomTab(n,a,b):
    # A COMPLETER
    T = []
    for i in range(n):
        T.append(random.randint(a,b))

    return T

def derangeUnPeu(n,k,rev):
    # A COMPLETER
    T = []
    if rev == False:
        for i in range(n):
            T.append(i+1)
    else:
        for i in range(n,0,-1):
            T.append(i+1)
    for j in range(k):
        p1 = random.randint(0,n-1)
        p2 = random.randint(0,n-1)
        tmp = T[p1]
        T[p1] = T[p2]
        T[p2] = tmp

    return T

# Exercice 2

#########################
# Tri insertion echange #
#########################
def echange(a,b):
    tmp = a
    a = b
    b = tmp 

def triInsertionEchange(T):
    # A COMPLETE
    # 把表格看做两个部分，左边是已经排序的区域，右边是未排序区域，代码每次运行都选右边第一个，把它安插到
    # 已排序的区域，然后找到他应该在的位置，而且是在左侧区域中从后到前一个个换。

    for i in range(len(T)):
        for g in range(i-1,-1,-1):
            if T[g] >= T[g+1]:
                tmp = T[g]
                T[g] = T[g+1]
                T[g+1] = tmp
            else:
                break
    return T

##########################
# Tri insertion rotation #
##########################

def triInsertionRotation(T):
    # A COMPLETER
    # 方法与上边置换方法一样，只不过是通过找到应该插入左侧区域的位置，然后减少操作量

    if len(T) == 0:
        return None
    for i in range(len(T)):
        for g in range(i):
            if T[g] > T[i]:
                tmp = T[i]
                for j in range(i,g,-1):
                    T[j] = T[j-1]
                T[g] = tmp
                break
    return T
###########################
# Tri Rapide -- TP6       #
###########################

# ex1

###############
# Tri rapide  #
###############

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

#########################
# Tri rapide aleatoire  #
#########################
# 这里需要做一下说明，为什么Tri rapide aleatoire 比 tri rapide更慢，这种情况适用于表格完全混乱；
# 而当表格差不多已经完成排序，那么tri aleatoire 就比 正常从0开始更快，后者浪费时间。

def partitionAlea(T):
    # les éléments sont supposés destincts

    alea = random.randint(0,len(T)-1)
    pivot = T[alea]
    gauche = [elt for elt in T if elt < pivot]
    droite = [elt for elt in T if elt > pivot]

    return pivot, gauche, droite

def triRapideAlea(T):
    # A COMPLETER
    # 有pivot

    if len(T) < 2:
        return T
    pivot, gauche, droite = partitionAlea(T)
    return triRapideAlea(gauche) + [pivot] + triRapideAlea(droite)

########################
# Tri rapide en place  #
########################

def partitionEnPlace(T, debut, fin):

    if fin - debut  == 2 and T[debut] < T[debut+1]:
        return debut+1
    pivot, gauche, droite = T[debut], debut + 1, fin - 1

    while gauche <= droite : 
        if T[gauche] < pivot : gauche += 1
        elif T[droite] > pivot : droite -= 1
        else : T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite

def triRapideEnPlace(T,debut,fin):
    if fin - debut < 2: return 
    
    indice_pivot = partitionEnPlace(T, debut, fin)
    triRapideEnPlace(T,debut, indice_pivot) 
    triRapideEnPlace(T,indice_pivot + 1,fin)

##################################
# Tri rapide en place aleatoire  #
##################################

def partitionEnPlaceAlea(T, debut, fin):

    if fin - debut  == 2 and T[debut] < T[debut+1]:
        return debut+1
    alea = random.randint(debut, fin-1)
    T[debut], T[alea] = T[alea], T[debut]
    
    pivot, gauche, droite = T[debut], debut + 1, fin - 1

    while gauche <= droite : 
        if T[gauche] < pivot : gauche += 1
        elif T[droite] > pivot : droite -= 1
        else : T[gauche], T[droite] = T[droite], T[gauche]
    T[debut], T[droite] = T[droite], pivot
    return droite

def triRapideEnPlaceAlea(T,debut,fin):
    if fin - debut < 2: return 
    
    indice_pivot = partitionEnPlaceAlea(T, debut, fin)
    triRapideEnPlaceAlea(T,debut, indice_pivot) 
    triRapideEnPlaceAlea(T,indice_pivot + 1,fin)


# ex2

###########################
# Tri rapide ameliore     #
###########################

def partition(T):
    # les éléments sont supposés destincts
    pivot = T[0]
    gauche = [elt for elt in T if elt < pivot]
    droite = [elt for elt in T if elt > pivot]

    return pivot, gauche, droite

def triRapideAmeliore(T):
    # A COMPLETER
    # 有pivot

    if len(T) < 15:
        return triInsertionRotation(T)
    pivot, gauche, droite = partition(T)
    return triRapide(gauche) + [pivot] + triRapide(droite)


##########################
# Tri rapide incomplet   #
##########################

def partition(T):
    # les éléments sont supposés destincts
    pivot = T[0]
    gauche = [elt for elt in T if elt < pivot]
    droite = [elt for elt in T if elt > pivot]

    return pivot, gauche, droite

def triRapideIncomplet(T):

    if len(T) < 15:
        return T
    pivot, gauche, droite = partition(T)
    return triRapideIncomplet(gauche) + [pivot] + triRapideIncomplet(droite)


###################
# Tri sedgewick   #
###################

def triSedgewick(T):
    T = triRapideIncomplet(T)

    return triInsertionRotation(T)

##############
# Tri fusion #
##############

def fusion(L1,L2):
    if len(L1) == 0: return L2
    elif len(L2) == 0: return L1
    elif L1[0] < L2[0]:
        return [L1[0]] + fusion(L1[1:],L2)
    else:
        return [L2[0]] + fusion(L1,L2[1:])

def triFusion(T) :
    # A COMPLETER
    if len(T)<2: return T
    else:
        milieu = len(T)//2
        gauche = triFusion(T[:milieu])
        droite = triFusion(T[milieu:])
    return fusion(gauche,droite)


##############
# tri bulles #
##############

def triBulles(T) :
    # A COMPLETER
    n = len(T)
    for i in range(n):
        for j in range(n):
            if T[i] < T[j]:
                T[i], T[j], = T[j], T[i]
    return T


##############################################################
#
# Mesure du temps
#

def mesure(algo, T) :
    debut = clock()
    algo(T)
    return clock() - debut

def mesureMoyenne(algo, tableaux) :
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-') :
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos) :
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesureMoyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche() :
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution')
  plt.legend(loc='upper left')
  plt.show()
  
##############################################################
#
# Main
#
##############################################################

if __name__ == '__main__':
  # LIGNE A COMPLETER
  algos = [] # chaque case contient un algorithme de tri différent
  algos.append(triSelection)
  algos.append(triInsertionEchange)
  algos.append(triInsertionRotation)
  algos.append(triRapide)
  algos.append(triRapideAlea)
  algos.append(triFusion)
  algos.append(triBulles)
  algos.append(triSedgewick)
  algos.append(triRapideAmeliore)
  for tri in algos :
      if testeQueLaFonctionTrie(tri):
          print(tri.__name__ + ": OK")
      else:
          print(tri.__name__ + ": échoue")
  taille = 1000 # taille maximale des tableaux à trier
  pas = 100 # pas entre les tailles des tableaux à trier
  ech = 5 # taille de l'échantillon pris pour faire la moyenne
  print()
  print("Comparaison à l'aide de randomPerm")
  tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche()
  print()
  print("Comparaison à l'aide de randomTab")
  # A COMPLETER
  print()
  print("Comparaison à l'aide de derangeUnPeu (rev = False)")
  # A COMPLETER
  print()
  print("Comparaison à l'aide de derangeUnPeu (rev = True)")
  # A COMPLETER
