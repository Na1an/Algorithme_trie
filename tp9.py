#!/usr/bin/env python3

from os import system
from random import shuffle

class Bnoeud :

    # constructeur : le premier paramètre est l'objet à construire;
    # il s'appelle self par convention
    def __init__(self, cles=[], fils=None, pere=None, p=1) :
        ''' ce constructeur ne fait pas de vérification de cohérence
        (entre p et les nbs de clés et de fils) '''
        self.nbCles = len(cles)
        self.nbFils = 0 if fils == None else len(fils)
        # normalement, nbFils = nbCles+1 (sauf pour les feuilles), mais
        # cela peut momentanément ne pas être le cas au cours d'une opération
        self.cles = cles + [None] * (2*p-self.nbCles)
        self.fils = None if fils == None else fils + [None] * (2*p+1-self.nbFils)
        self.attache_les_fils()
        self.pere = pere
    
    # les feuilles n'ont pas de fils
    # comme pour le constructeur, les méthodes ont l'objet concerné comme
    # premier paramètre
    def estFeuille(self) :
        return (self.fils == None)

    def attache_les_fils(self) :
        ''' met à jour le champ pere de tous les fils '''
        if self.fils != None :
          for f in self.fils[:self.nbFils] : 
            f.pere = self
    
    def supprime_cle(self, i) :
        ''' supprime la clé d'indice i et met à jour le nombre de clés '''
        if i<0 or i>=self.nbCles : return None
        res = self.cles[i]
        self.cles[i:self.nbCles] = self.cles[i+1:self.nbCles] + [None]
        self.nbCles -= 1
        return res

    def supprime_fils(self, i) :
        ''' supprime le fils d'indice i et met à jour le nombre de fils '''
        if i<0 or i>=self.nbFils : return None
        res = self.fils[i]
        self.fils[i:self.nbFils] = self.fils[i+1:self.nbFils] + [None]
        self.nbFils -= 1
        return res

    def insere_cle(self, i, x) :
        ''' insère la clé x en position i et met à jour le nombre de clés 
        (vérifie que le nombre de clés permet l'insertion, 
        mais pas que la position i est adaptée) '''
        if self.nbCles >= len(self.cles): return None
        if i<0 or i>self.nbCles : return None
        self.cles[i:self.nbCles+1] = [x] + self.cles[i:self.nbCles]
        self.nbCles += 1
        return x

    def insere_fils(self, i, noeud) :
        ''' insère un noeud comme fils en position i et met à jour le
        nombre de fils
        (vérifie que le nombre de fils permet l'insertion, 
        mais pas que la position i est adaptée) '''
        if self.nbFils >= len(self.fils): return None
        if i<0 or i>self.nbFils : return None
        self.fils[i:self.nbFils+1] = [noeud] + self.fils[i:self.nbFils]
        self.nbFils += 1
        noeud.pere = self
        return noeud

    def contient(self, x) :
        ''' teste si le noeud contient la clé x
        retourne (True, i) si cles[i]==x et (False, i) si cles[i-1] < x < cles[i]
        '''
        #
        # À COMPLÉTER
        #
        return False, 0

    def cherche(self, x) : 
        ''' cherche x dans le sous-arbre de racine self '''
        #
        # À COMPLÉTER
        #
        return False, None, 0



class Barbre :

    def __init__(self, bnoeud=None, p=1) :
        self.racine = bnoeud if bnoeud != None else Bnoeud(p=p)
        self.ordre = p


    def dessine(self, fname = '/tmp/arbre') :
        ''' crée un fichier fname.dot et un fichier fname.pdf représentant l'arbre ''' 
        
        # creation du fichier .dot
        fic = open(fname+".dot", 'w')
        fic.write("graph arbre {\n")
        
        cpt = 0
        todo = [(cpt, self.racine)]
        aretes = []
        
        while todo != [] :
            numero, tmp = todo.pop(0)
            fic.write("\t" + str(numero) +'[label="'+ str(tmp.cles[0]))
            for k in tmp.cles[1:tmp.nbCles] : fic.write(', ' + str(k))
            fic.write('"];\n')
            if tmp.fils != None :
                for f in tmp.fils[:tmp.nbFils] :
                    cpt += 1
                    aretes.append((numero, cpt))
                    todo.append((cpt, f))
                        
        for i,j in aretes :
            fic.write("\t" + str(i) + " -- " + str(j) + ";\n")
           
        fic.write("}\n")
        fic.close()
       
        # transformation en .pdf
        system("dot -Tpdf -o " + fname + ".pdf " + fname + ".dot")
  

    def cherche(self, x) :
        ''' retourne (True, noeud, i) si x == noeud.cles[i]
        et (False, feuille, i) si x n'est pas dans l'arbre mais devrait
        être inséré en feuille.cles[i] '''
        return self.racine.cherche(x)


    def ajoute(self, x) : 
        ''' ajoute la clé x dans l'arbre (si elle ne s'y trouve pas
        encore '''
        #
        # À COMPLÉTER
        #
        pass


def test_1() :
    ## un B-arbre d'ordre p=1
    f1_1 = Bnoeud([1])
    f1_2 = Bnoeud([3, 4])
    f1_3 = Bnoeud([6])
    racine_1 = Bnoeud([2, 5], [f1_1, f1_2, f1_3])
    A_1 = Barbre(racine_1)
    A_1.dessine("/tmp/petitBarbre1")
    return A_1

def test_2() :
    ## un B-arbre d'ordre p=2
    f2_1 = Bnoeud([1, 2], p=2)
    f2_2 = Bnoeud([4, 5], p=2)
    f2_3 = Bnoeud([7, 8], p=2)
    racine_2 = Bnoeud([3, 6], [f2_1, f2_2, f2_3], p=2)
    A_2 = Barbre(racine_2, p=2)
    A_2.dessine("/tmp/petitBarbre2")
    return A_2

def test(n=50, p=1) :
    A = Barbre(p=p)
    L = list(range(n))
    shuffle(L)
    for i in L : A.ajoute(i)
    A.dessine()
    return L, A


if __name__ == '__main__':
    A1 = test_1()
    A2 = test_2()
    A2.racine.contient(6)
    A2.racine.contient(5)
    A2.cherche(5)
    A2.cherche(9)
    test(10)
    # test()
    # test(200, 2)
  
