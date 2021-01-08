from random import randint
from time import process_time
import matplotlib.pyplot as plt
import math

MARQUE = (None, None)
A = (math.sqrt(5)-1)/2

def creer_table(puiss, h, taux):

    t = 2**puiss
    return [[None]*t,h,t,taux,0]

def rechercher(table, cle, flag=False):
    #A COMPLETER
    if flag == True:
        if table == None or table == [None,None,None,None,None]:
            return None
        for pos in gen_hash(hash1,hash2,cle,table[2]):
            if table[0][pos] == cle:
                return pos
        return cle%(table[2])
    else:
        for i in table[0][cle%table[2]]:
            if i == cle:
                return cle%table[2]
        return None


def inserer(table, cle):
    #A COMPLETER
    if table == None:
        return 
    #elif table[4] == 0:
    n = rechercher(table,cle,True)
    if table[0][n] == None: 
        table[0][n]= [cle]
    else:
        table[0][n] = table[0][n] + [cle]
    table[4] = table[4]+1
    if (table[4]/table[2]) >= table[3]:
        table = redimensionner(table,table[2]*2)
    return table

def supprimer(table, cle):
    #A COMPLETER
    if table == None:
        return None
    n = rechercher(table,cle,False)
    for i in range(len(table[0][n])):
        if table[0][n][i] == cle:
            table[0][n][i]= MARQUE
    table[4] = table[4]-1
    return table

def redimensionner(table,t):
    if table == None:
        return None
    table[2] = t
    tmp = []
    for i in table[0]:
        if i != None:
            tmp = tmp + i
    table[0] = [None]*t
    for cle in tmp:
        table = inserer(table,cle)
    return table


##############################################################
#
# fonctions de hachage
#

def gen_hash(h1, h2, cle, taille): 
    ind = h1(cle, taille) % taille
    pas = h2(cle, taille)
    for i in range(taille):
        yield ind
        ind = (ind+pas) % taille

def hash1(cle, taille):
    #A COMPLETER
    return (cle % taille)


def hash2(cle, taille):
    #A COMPLETER
    return 1


def hash3(cle, taille):
   #A COMPLETER
    return  ((A*cle) - (int)(A*cle))*taille


def hash4(cle, taille):
    #A COMPLETER
    return (2*cle+1)%taille


##############################################################
#
# Mesures
#

def random_liste(taille, maxi):
    L = []
    S = set()
    for i in range(taille):
        r = randint(0, maxi)
        while r in S:
            r = randint(0, maxi)
        S.add(r)
        L.append(r)
    return L

def liste_collisions(taille, ite):
    L = [1]
    for i in range(10):
        pas = (i+ite)*taille
        L += [j+pas for j in range(taille//10)]
    return L

def taille_max_cluster(table):
    cles, h, taille, taux, nbCles = table
    maxi = 0
    max_tmp = 0
    for i in range(taille):
        if cles[i] == None:
            maxi = max_tmp if max_tmp > maxi else maxi
            max_tmp = 0
        else:
            max_tmp += 1
    return maxi

def stats(h, taille_max, taux, alea=False, rep=1, pas=10, redim=False):
    t_crea = [None] * (taille_max//pas)
    clust = [None] * (taille_max//pas)
    t_rech = [None] * (taille_max//pas)
    if not redim:
        p = 1
    for i in range(0,taille_max,pas):
        cluster = 0
        tps = 0
        max_cl = 0
        tr = 0
        for j in range(rep):
            if alea: L = random_liste(i+1, 100000)
            else: L = liste_collisions(i+1, j+1)
            if redim: table = creer_table(6, h, taux)
            else: table = creer_table(p, h, taux)
            for cle in L:
                deb = process_time()
                table = inserer(table, cle)
                tps += process_time() - deb
            cluster += taille_max_cluster(table)
            tr += test_recherche(table, L)
        t_crea[i//pas] = tps/rep
        clust[i//pas] = cluster/rep
        t_rech[i//pas] = tr/rep
        if not redim:
            p += 1
    return t_crea, clust, t_rech



def test_recherche(table, L):
    tps = 0
    for cle in L: 
        deb = process_time()
        rechercher(table, cle)
        tps += process_time() - deb
    return tps/len(L)
    
##############################################################
#
# Courbes
#

def mesure(algo, T) :
    debut = process_time()
    algo(T)
    return process_time() - debut

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y']


def courbes(liste_h, taille_max, taux, alea=False, styleLigne='-', rep=1, pas=10, redim=False):
    x = [i for i in range(0,taille_max,pas)]
    s = [None] * len(liste_h)
    for i, h in enumerate(liste_h):
        s[i] = stats(h, taille_max, taux, alea, rep, pas, redim)
    for i in range(len(s)):
        tps = s[i][0]
        plt.plot(x, tps, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][0].__name__+"_"+liste_h[i][1].__name__[-1])        
    affiche("temps d'execution")
    for i in range(len(s)):
        clust = s[i][1]
        plt.plot(x, clust, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][0].__name__+"_"+liste_h[i][1].__name__[-1])
    affiche("taille moyenne du cluster max")
    for i in range(len(s)):
        clust = s[i][2] 
        plt.plot(x, clust, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][0].__name__+"_"+liste_h[i][1].__name__[-1])
    affiche("temps d'execution moyen pour une recherche reussie")

def affiche(label) :
  plt.xlabel('taille du tableau')
  plt.ylabel(label)
  plt.legend(loc='upper left')
  plt.show()
  
##############################################################
#
# Main
#

if __name__ == '__main__':
    L = [5, 28, 19, 15, 20, 33, 37, 17, 26, 10]
    table = creer_table(2, [hash1, hash2], 0.5)
    for cle in L:
        table = inserer(table, cle)
    table2 = creer_table(2, [hash4, hash2], 0.5)
    for cle in L:
        table2 = inserer(table2, cle)
    
    print()
    print("liste de cles :",L)
    print()
    if table != None:
        print("table obtenue avec hash1 :", table[0], "taille de la table :", table[2])
        print()
    if table2 != None:
        print("table obtenue avec hash2 :", table2[0], "taille de la table :", table2[2])

    print()
    print("##############################################################")
    print()
    
    L = [13, 15, 28, 18, 20, 5, 32, 4, 6]
    table = creer_table(3, [hash1, hash2], 0.5)
    for cle in L:
        table = inserer(table, cle)
    table2 = creer_table(2, [hash4, hash2], 0.5)
    for cle in L:
        table2 = inserer(table2, cle)
    print("liste de cles :",L)
    print()
    if table != None:
        print("table obtenue avec hash1 :", table[0], "taille de la table :", table[2])
        print()
    if table2 != None:
        print("table obtenue avec hash2 :", table2[0], "taille de la table :", table2[2])
        print("\n")
    if table != None:
        print("suppression de l'element 6:\n")
        print("table obtenue avec hash1 :", supprimer(table, 6)[0])
        print()
    if table2 != None:
        print("table obtenue avec hash2 :", supprimer(table2, 6)[0])
        print()

    #A COMPLETER
    liste_hash = [[hash1,hash2],[hash3,hash2],[hash1,hash4],[hash3,hash4]]

    # #Tests avec jusqu'a 2000 (par pas de 100) clés de valeurs consécutives par plages, taux=0,5.
    # #Pour chaque taille, on fait des tests sur rep=10 listes.
    # courbes(liste_hash, 2000, 0.5, rep=10, pas=100)

    # #Tests avec jusqu'a 2000 (par pas de 100) clés aléatoires, taux=0,5.
    # #Pour chaque taille, on fait des tests sur rep=10 listes.
    #courbes(liste_hash, 2000, 0.5, True, rep=10, pas=100)

    # #Tests avec jusqu'a 2000 (par pas de 100) clés de valeurs consécutives par plages, taux=0,5.
    # #Pour chaque taille, on fait des tests sur rep=10 listes.
    courbes(liste_hash, 300, 0.9, rep=10, pas=10, redim=True)

    # #Tests avec jusqu'a 2000 (par pas de 100) clés aléatoires, taux=0,5.
    # #Pour chaque taille, on fait des tests sur rep=10 listes.
    # courbes(liste_hash, 2000, 0.8, True, rep=10, pas=100, redim=True)
