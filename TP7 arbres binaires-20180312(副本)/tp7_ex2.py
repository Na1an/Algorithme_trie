#!/usr/bin/env python3

from tp7_ex1 import *
from tp56 import *
#
# A COMPLETER !
#
def profondeur(arbre, i) :
  ''' retourne la profondeur de i dans l'arbre '''
  if estRacine(arbre) or estVide(arbre):
      return 0
  elif estFilsGauche(arbre,i) or estFilsGauche(arbre,i):
      return 1 + prifondeur(pere(arbre,i),arbre[1][3])
  return -1
  
#
# NE PAS MODIFIER !
#
def hauteurNaive(arbre) :
  ''' retourne la hauteur de l'arbre '''
  if estVide(arbre) : return 0
  return max (profondeur(arbre, i) for i in range(len(arbre)) 
      if etiquette(arbre, i) != None)
  
#
# A COMPLETER !
#
def hauteur(arbre) :
  ''' retourne la hauteur de l'arbre '''
  if estVide(arbre):
      return 0
  else:
      for i in range(len(arbre)):
          if estRacine(arbre,i):
              return hauteurAux(arbre,i)

def hauteurAux(arbre,i):
    gauche = filsGauche(arbre,i)
    droite = filsDroit(arbre,i)
    if estFeuille(arbre,gauche) and estFeuille(arbre,droite):
        return 0
    if gauche == None and droite == None:
        return 0
    return max(hauteurAux(arbre,gauche),hauteurAux(arbre,droite))+1
#
# A COMPLETER !
#
def parcoursPrefixe(arbre) :
  ''' retourne la liste des etiquettes en ordre prefixe '''
  res = []
  for i in range(len(arbre)):
      if arbre[i][0] == None:
          break
      arbre[i][0] = (int)(arbre[i][0])
      res.append(arbre[i][0])
  return triInsertionEchange(res)
  
#
# A COMPLETER !
#
def estUnABR(arbre) :
  ''' teste si arbre est un ABR '''
  if estVide(arbre):
      return True
  #h = hauteur(arbre)
  for i in range(len(arbre)):
      if estRacine(arbre,i):
          indice = i
  res = inOrderTraversal(arbre,indice)
  if parcoursPrefixe(arbre) == res:
      for i in range(len(res)-1):
          if res[i] == res[i+1]:
              return False
      return True
  else:
      return False

def inOrderTraversal(arbre,i):
    if estFeuille(arbre,i):
        return [] 
    return inOrderTraversal(arbre,arbre[i][1])+[arbre[i][0]]+inOrderTraversal(arbre,arbre[i][2])

#
# A COMPLETER !
#

def testResults() :

    return [[hauteur,(arbreVide,0),(arbrePlanetesComplet,3),(arbreABR,2),(arbreFilsGaucheComplet,1)],[parcoursPrefixe,(arbreVide,[]),(arbreABR,[1,5,6,8,9,10])],[estUnABR,(arbreVide,True),(arbreABR,True),(arbreNABR,False)]]

#
# NE PAS MODIFIER
#

def testAll() :
  tst = testResults()

  for fname, *tests in tst :
    score = 0
    print('Test %s :' % fname.__name__)
    for j, test in enumerate(tests) :
      *farg, fres = test
      print (' - test %d/%d : ' % (j + 1, len(tests)), end='')
      res = fname(*farg)
      if (res == fres) :
        print(' ok')
        score += 1
      else :
        print(" échec sur", *farg)
        print("\t résultat obtenu :", res, end='')
        print(" <> attendu :", fres)
    print ('  score %d/%d ' % (score, len(tests)))
	
    
if __name__ == '__main__':
  testAll()
