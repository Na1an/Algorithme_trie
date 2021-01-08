#!/usr/bin/env python3

#importe indirectement tp8, data, et tp8_ex* pour * < 2
from tp8_ex2 import *

    
#
# A COMPLETER !
#
def maximum2ABR(arbre,i): 
#retourne l'indice du noeud d'etiquette max du sous-arbre enracine en le noeud i 

  if estFeuille(arbre,arbre[i][1]) and estFilsDroit(arbre,arbre[i][3]):
      return arbre[i][3]
  elif estFeuille(arbre,arbre[i][1]) == False:
      return recMaxi(arbre,arbre[i][1])
  else:
      res = recMaxi2(arbre,i)
      if res == None: return i
      return recMaxi2(arbre,i)

def recMaxi(arbre,i):
  droite = arbre[i][2]
  if estFeuille(arbre,droite):
      return i
  return recMaxi(arbre,droite)

def recMaxi2(arbre,i):
    pere = arbre[i][3]
    if estFilsGauche(arbre,pere):
        return recMaxi2(arbre,pere)
    elif estRacine(arbre,pere):
        print("Pas de predecesseur")
        return None
    else:
        return pere
#
# A COMPLETER !
#
def relier(arbre, pere,fils,d):  
#relier pere et fils. Si d = 1, le fils est un fils gauche et si d =2, un droit.
  if d == 1:
      arbre[pere][1] = fils
  else:
      arbre[pere][2] = fils
  arbre[fils][3] = pere



#
# A COMPLETER !
#
def suppressionABR(arbre,elt) :
  ''' supprime le noeud d'étiquette elt dans l'arbre '''
  #cas0
  if contientABR(arbre,elt) == False:
      return arbre
  if elt == None:
      return arbre
  t = []
  ind = rechercheABR(arbre,elt)
  print(ind)
  gauche = arbre[ind][1]
  droite = arbre[ind][2]
  pere = arbre[ind][3]

  if estFilsGauche(arbre,ind):
      d = 1
  else:
      d = 2
  #cas1
  if estFeuille(arbre,gauche) and estFeuille(arbre,droite):
      t.append(gauche)
      t.append(droite)
      arbre[ind] = [None,None,None,arbre[ind][3]]
  
  #cas2
  elif estFeuille(arbre,droite):
      relier(arbre,pere,gauche,d)
      t.append(ind)
      t.append(droite)
  elif estFeuille(arbre,gauche):
      relier(arbre,pere,droite,d)
      t.append(ind)
      t.append(gauche)

  #cas3
  else:
      
      indM = maximum2ABR(arbre,gauche)
      arbre[ind][0] = arbre[indM][0]
      t.append(indM)
      
  suppr(arbre,t)
  
#####################################################################
##  TESTS
#####################################################################

def testSuppression():
  arbres = [arbre3ABR1, arbre3ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1]
  elements = [1,4,1,49,43,55]
  res = res_suppression()
  score = 0
  print('Test Suppression')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    a = copier(arbres[i])
    elt = elements[i]
    suppressionABR(a,elt)
    if egalite(a,res[i]):
      print(' pass')
      score += 1
    else:
        print(" fail: obtenu ", print(a), end='')
        print(" <> attendu ", res[i])
  print ('  score %d/%d ' % (score, len(arbres)))
    
if __name__ == '__main__':
  testSuppression()
