from random import randint


def hash_mot(w):
    #A COMPLETER
    return

def creer_ens_mots(taille=0):
    #A COMPLETER
    return

def ajouter(S,w):
    #A COMPLETER
    return

def retirer(S,x):
    #A COMPLETER
    return

def dans_ens(S,x):
    #A COMPLETER
    return

##############################################################
#
# creer des liste de mots
#

if __name__ == '__main__':

def lire_fichier(fic):
    L=[]
    for ligne in open(fic, encoding="utf-8").readlines():
        L.append(ligne.strip())
    return L

def random_liste(mots, taille):
    L = []
    S = set()
    for i in range(taille):
        r = randint(0, len(mots))
        while r in S:
            r = randint(0, len(mots))
        S.add(r)
        L.append(mots[r])
    return L

def liste_collisions(mots, taille, saut=0):
    L = [mots[0]]
    for i in range(10):
        pas = (i+saut)*taille
        print("pas ", pas)
        L += [mots[(j+pas)  % len(mots)] for j in range(taille//10)]
    return L

##############################################################
#
# Main
#

if __name__ == '__main__':
    mots = lire_fichier("mots.txt")
    L1 = random_liste(mots, 50)
    L2 = liste_collisions(mots, 50, 70)

    #completez avec vos tests...
