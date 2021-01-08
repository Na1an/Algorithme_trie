#!/usr/bin/env python3

from tp8 import *
from data import *

#
# A COMPLETER !
#
def parcoursPrefixe(arbre) :
  ''' retourne la liste des etiquettes en ordre prefixe '''
  res = []
  for i in range(len(arbre)):
      if arbre[i][0] == None:
          break
      #arbre[i][0] = (int)(arbre[i][0])
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
def minimumABR(arbre) :
  ''' retourne l'indice de l'etiquette minimale dans arbre (si c'est un ABR) '''
  if estVide(arbre):
          return None
  tmp = arbre[racine(arbre)] 
  while(tmp[1] != None):
    tmp = arbre[tmp[1]]
  return tmp[3]
  
#
# A COMPLETER !
#
def maximumABR(arbre) :
  ''' retourne l'indice de l'etiquette maximale dans arbre (si c'est un ABR) '''
  if estVide(arbre):
      return None
  tmp = arbre[racine(arbre)]
  while(tmp[2] != None):
      tmp = arbre[tmp[2]]
  return tmp[3]

#
# A COMPLETER !
#
def rechercheABR(arbre, elt) :
  ''' retourne le noeud contenant elt, ou la feuille ou la recherche
  echoue (si c'est un ABR) '''
  if estVide(arbre):
      return 0
  tmp = arbre[racine(arbre)]
  ind = 1
  while elt != tmp[0]:
      if tmp[0] == None:
          break
      if elt > tmp[0]:
          tmp = arbre[tmp[2]]
          ind = 2
      elif elt < tmp[0]:
          tmp = arbre[tmp[1]]
          ind = 1
  return arbre[tmp[3]][ind]



#
# A COMPLETER !
#
def contientABR(arbre, elt) :
  ''' teste is arbre contient elt (si c'est un ABR)'''
  for i in range(len(arbre)):
      if arbre[i][0] == elt:
          return True
  return False
  
#
# A COMPLETER !
#
def insertionABR(arbre, elt) :
  ''' insere correctement elt dans arbre si arbre ne contient pas encore
  elt (et si c'est un ABR) '''
  if contientABR(arbre,elt):
      return arbre
  else:    
      i = rechercheABR(arbre,elt)
      arbre[i][0] = elt
      arbre[i][1] = len(arbre)
      arbre[i][2] = len(arbre)+1
      arbre.append([None,None,None,i])
      arbre.append([None,None,None,i])
#
#reference
#

def exABR():

    return [['A',1,2,0],['B',3,4,0],[None,None,None,0],[None,None,None,1],[None,None,None,1]]


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



#####################################################################
##  TESTS
#####################################################################

def testData():
  return  [arbreVide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]

def testResults():
  return [[minimumABR, 0,[None, 1, 0, 2, 5, 3]],
          [maximumABR, 0, [None, 2, 2, 0, 16, 120]],
          [rechercheABR, 1, [1,27,3,57,100,200],[0,6,2,3,16,156]],
          [contientABR, 1, [1,27,3,57,100,200],[False,False,True,False,True,False]]                   
]

def testAll() :
  tst = testResults()
  arbres = testData()

  print('Arbres : ')
  for j in range(len(arbres)) :
    print(arbres[j])
    dessineArbreBinaire(arbres[j],"./arb_"+str(j))
 
  for i in range(len(tst)) :
    fname = tst[i][0]
    farg = tst[i][1]
    fres = tst[i][2 + farg]
    score = 0
    print('Test %s:' % fname.__name__)
    for j in range(len(arbres)) :
      a = arbres[j]
      print (' - test %d/%d: ' % (j + 1, len(arbres)), end='')
      res = fres[j]
      if (farg == 0) :
        res = fname(a)
      elif (farg == 1) :
        res = fname(a,tst[i][2][j])
      if (res == fres[j]) :
        print(' pass')
        score += 1
      else :
        print(" fail: obtenu ", res, end='')
        print(" <> attendu ", fres[j])
    print ('  score %d/%d ' % (score, len(arbres)))

def testInsertion():
  arbres = [arbreVide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]
  elements = [4,4,2,10,27,123]
  res = res_insertion()
  score = 0
  print('Test Insertion')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    a = copier(arbres[i])
    elt = elements[i]
    insertionABR(a,elt)
    if egalite(a,res[i]):
      print(' pass')
      score += 1
    else:
        print(" fail: obtenu ", print(a), end='')
        print(" <> attendu ", res[i])
  print ('  score %d/%d ' % (score, len(arbres)))
    
if __name__ == '__main__':
  testAll()
  testInsertion()
