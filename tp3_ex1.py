#!/usr/local/bin/python3

# Pour les fonctions mathematiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show

############################################################
# Exercice 1.1
#
# Calcule la plus petite puissance de 2 supérieure à k (et 0 si k == 0)
#


def minPuissanceDe2(k) :
  #A REMPLIR
  if k==0:
    return 0
  v = True
  tmp = 1
  while(v):
    if(tmp>=k):
      v = False
      return tmp
    tmp = tmp*2




############################################################
# Exercice 1.2
#
# Augmente le degré du polynome à k-1
#


def polyDegreAdapte(P,k) :
  #A REMPLIR
  while(len(P)<k):
    P.append(0)
  return P



############################################################
# Exercice 1.3
#
# Ajoute/Soustrait un polynôme S à un polynôme T
#    S doit pouvoir être ajouté avec un décalage
#     et être soustrait au lieu d'ajouté selon
#      la valeur du dernier paramètre
#
#   / \      La fonction doit modifier T sans
#  / ! \       créer de nouveau tableau !
# /_____\
#


def polyAjoute(T,S,dec=0, neg=False):
  #A REMPLIR

  S = polyDegreAdapte(S,len(T)-dec)

  for i in range(len(T)-dec):
    if(neg == False):
      T[dec+i]+=S[i]
    else:
      T[dec+i]=T[dec+i]-S[i]
    
  return T



############################################################
# Exercice 1.4
#
# Calcule le produit de polynômes par l'algorithme de Karatsuba
#


def polyProdKara(P, Q) :
  #A REMPLIR
  if len(P) == 1 or len(Q) == 1 : return [P[0]*Q[0]]

  l = minPuissanceDe2(len(P))
  l1 = l//2
  

  P = polyDegreAdapte(P,l)
  Q = polyDegreAdapte(Q,l)
  
  P0=P[:l1]
  P1=P[l1:]
  
  Q0=Q[:l1]
  Q1=Q[l1:]
  
  #------------------------
  # t1 = P0*Q0
  # t2 = (P0+P1)(Q0+Q1)
  # t3 = P1*Q1
  # t4 = (P0+P1)(Q0+Q1) - P0*Q0 - P1*Q1
  # t5 = [(P0+P1)(Q0+Q1) - P0*Q0 - P1*Q1]*x^(2^(k-1))
  # t6 = P1*Q1*x^(2^k)
  # t  = P0*Q0 + [(P0+P1)(Q0+Q1) - P0*Q0 - P1*Q1]*x^(2^(k-1)) + P1*Q1*x^(2^k)
  #------------------------
  
  t1 = polyProdKara(P0,Q0)
  t2 = polyProdKara(polyAjoute(P0,P1,dec=0,neg=False),polyAjoute(Q0,Q1,dec=0,neg=False))
  t3 = polyProdKara(P1,Q1)

  t4 = polyAjoute(polyAjoute(t2,t1,dec=0,neg=True),t3,dec=0,neg=True)

  t5 = [0]*(l1)
  t5 = t5+t4

  t = polyAjoute(t5,t1,dec=0,neg=False)
  t6 = [0]*l
  t6 = t6+t3
  t = polyAjoute(t6,t,dec=0,neg=False)

  return t



############################################################
# Exercice 1.5

############################################################
# Exercice 1.5
#
# Calcul des coûts
#


def polyProdKaraOps(P, Q) :
  #A remplir
  
  return polyProdKara(P,Q),25*pow((len(P)-1),1.6)



############################################################
# Exercice 1.6
#
# Petite économie en ne faisant plus:
#    P0,P1 = P[:m//2],P[m//2:]
#    Q0,Q1 = Q[:m//2],Q[m//2:]
#    


def polyAjoute2Ops(T,S,debS,finS,dec = 0,neg = False):
  #A remplir
  return [],0


def polyProdKara2Ops(P,Q) :
  #A remplir
  return [],0


def polyProdKara2SubOps(P,debP,finP,Q,debQ,finQ) :
  #A remplir
  return [],0



############################################################
# Exercice Bonus 1
#
# Grosse économie en stockant directement P0*Q0 et P1*Q1 dans le tableau du résultat
#


def polyProdKara3Ops(P,Q) :
  #A remplir
  return PQ,0


def polyProdKara3SubOps(P,debP,finP,Q,debQ,finQ,PQ,dec) :
  return PQ,0



############################################################
# Exercice Bonus 2
#
# Algo qui n'agrandit plus les polynômes
#


def polyProdKara4Ops(P,Q) :
  #A remplir
  return [],0



############################################################
# Exercice Bonus 3
#
# Algo qui combine produit de Karatsuba et produit naïf (pour taille < 16)
#


def polyProdOptiOps(P,Q,cut = 16) :
  #A remplir
  return [],0



############################################################
# TESTS - NE PAS MODIFIER !!!
#

from math import log2,ceil,fabs

def prettyPrint(P):
  s =''
  if(len(P))>0:
    s=str(P[0])
    for i,c in enumerate(P[1:]):
      s+=" + " + str(c)+"*X^"+str(i+1)
  return s

#
# Calcul naïf du produit de polynômes
#
def polyProdNaif(P, Q) :
  R = [0] * (len(P) + len(Q) - 1)
  for i in range(len(P)) :
    for j in range(len(Q)) :
      R[i + j] += P[i] * Q[j]
  return R

#
# Calcul naïf du produit de polynômes, avec calcul du nombre d'opérations
#
def polyProdNaifOps(P, Q) :
  R = [0] * (len(P) + len(Q) - 1)
  ops = len(P) + len(Q) - 1
  for i in range(len(P)) :
    for j in range(len(Q)) :
      R[i + j] += P[i] * Q[j]
      ops += 3
  return R,ops


def test_minPuissanceDe2Data():
  return [[0, 0],
          [1, 1],
          [2, 2],
          [3, 4],
          [16, 16],
          [96, 128],
          [200, 256],
          [1024, 1024],
          [1023, 1024],
          [1025, 2048]]


def test_minPuissanceDe2 () :
  print('Test minPuissanceDe2:')
  score = 0
  data = test_minPuissanceDe2Data()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    k = dt[0]
    ref = dt[1]
    res = minPuissanceDe2(k)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %d' % k)
      print('    calcule : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


def test_polyDegreAdapteData():
  return [[[],5,[0,0,0,0,0]],
          [[0,1,2,3,4,5,6],7,[0,1,2,3,4,5,6]],
          [[1,-1,0,0],8,[1,-1,0,0,0,0,0,0]],
          [[0,1,0],5,[0,1,0,0,0]],
          [[0,1,2,3,4],8,[0,1,2,3,4,0,0,0]]]

def test_polyDegreAdapte():
  print('Test polyDegreAdapte:')
  score = 0
  data = test_polyDegreAdapteData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    k = dt[1]
    res = polyDegreAdapte(P,k)
    ref = dt[2]
    if res == ref :
        score += 1
        print('ok')
    else :
      pP = prettyPrint(P)
      pRes = prettyPrint(res)
      pRef = prettyPrint(ref)
      print('ECHEC')
      print('    P  : %s' % pP)
      print('    k  : %d' % k)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pRef)
  print('* Score : %d/%d\n' % (score, ldata))

  
  
def test_polyAjouteData():
  return [[[0,0,0,0], [1,2], 0, False, [1, 2, 0, 0]],
          [[0,0,0,0], [1], 2, False, [0, 0, 1, 0]],
          [[0,0,0,0], [1], 3, True, [0, 0, 0, -1]],
          [[3,2,1,0,0], [1,2,3], 0, True, [2, 0, -2, 0, 0]],
          [[0,1,0,1,0,1,0,1,0,1], [1,0,1], 3, True, [0,1,0,0,0,0,0,1,0,1]]]

#
# Teste si la fonction polyAjoute fonctionne
#  Notamment, vérifie si un nouveau tableau a été déclaré ou non
#  Accepte à la fois si polyAjoute ne renvoie rien, et si polyAjoute renvoie le
#  même tableau T que celui passé en entrée
#
def test_polyAjoute():
  print('Test polyAjoute:')
  score = 0
  data = test_polyAjouteData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    S = dt[1]
    dec = dt[2]
    neg = dt[3]
    res = polyAjoute(T,S,dec,neg)
    if (type(res)==type(None)):
      res = T
    ref = dt[4]
    #test : T et res même tableau ?
    #Il est important de ne pas déclarer un nouveau tableau
    b = (res == T)
    T[0] += 1
    b = b and (res == T)
    T[0] -= 1
    if b and polyEq(res, ref) :
        score += 1
        print('ok')
    else :
      pT = prettyPrint(T)
      pS = prettyPrint(S)
      pRes = prettyPrint(res)
      pRef = prettyPrint(ref)
      print('ECHEC')
      if(b):
        print('    T       : %s' % pT)
        print('    S       : %s' % pS)
        print('    dec,neg : %d%s' % (dec,neg))
        print('    calcule : %s' % pRes)
        print('    attendu : %s' % pRef)
      if (not b) :
        print ('    /!\ ne pas créer un nouveau tableau !')
  print('* Score : %d/%d\n' % (score, ldata))



  
def test_polyProdData() :
  return [[[0, 1, 1], [0, 2], [0, 0, 2, 2], [142,132,105]],
          [[1, 2, 3], [1, 0, 1], [1, 2, 4, 2, 3], [142,132,105]],
          [[1, 2, 3, 0], [1, 0, 1, 0], [1, 2, 4, 2, 3, 0, 0], [134,124,97]],
          [[0, 0, 0, 3], [2, -1], [0, 0, 0, 6, -3], [138,128,101]],
          [[0, 0, 0, 3], [2, -1, 0, 0], [0, 0, 0, 6, -3, 0, 0], [134,124,97]],
          [[1, 1, 1, 1, 1, 1], [0, 1], [0, 1, 1, 1, 1, 1, 1], [535,497,374]],
          [[0, 1], [0, 2], [0, 0, 2], [27,25,22]],
          [[1, 2, 3, 1], [1, 1, 1, 1],[1, 3, 6, 7, 6, 4, 1], [134,124,97]],
          [[1, 2, 3, 1], [2, -1, 2, 4], [2, 3, 6, 7, 13, 14, 4], [134,124,97]],
          [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 1], [519,481,358]]]





def polyEq(P,Q):
  lP,lQ = len(P),len(Q)
  topP,topQ = max(0,lQ-lP),max(0,lP-lQ)
  return P+[0]*topP == Q+[0]*topQ

#
# Teste si l'algo 'algo' calcule bien un produit de polynômes
#   Marche aussi si l'algo renvoie un 'tuple' avec le résultat en premier élément du tuple, comme tous les algos polyProd****Ops
#
def test_polyProd (algo) :
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_polyProdData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    R = dt[2]
    res = algo(P,Q)
    if type(res) == type(([],0)):
      res = res[0]
    if polyEq(res,R) :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR = prettyPrint(R)
      pRes = prettyPrint(res)
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pR)
  print('* Score : %d/%d\n' % (score, ldata))

karaProds = [polyProdKaraOps,polyProdKara2Ops,polyProdKara3Ops]
def test_polyProdKaraOps (num=1) :
  print('Test polyProdKara%sOps' % ("" if num<=1 else str(num)))
  score = 0
  fullPrec = 0
  data = test_polyProdData()
  ldata = len(data)
  num -= 1
  algo = karaProds[num]
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    R = dt[2]
    refOps = dt[3][num]
    res,ops = algo(P,Q)
    if polyEq(res,R) and ops == refOps :
      score += 1
      fullPrec += 1
      print('parfait')
    elif polyEq(res,R) :
      precision = 1-fabs(ops - refOps)/refOps
      fullPrec += precision
      if precision > 0.9:
        score +=1
        print('très bien')
      else :
        print("mauvais nombre d'opérations")
      print('    calcul du produit : ok')
      print('    opérations : %d' % ops)
      print('    attendu :  %d' % refOps)
    else :
      print('ECHEC')
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR = prettyPrint(R)
      pRes = prettyPrint(res)
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    opérations : %d' % ops)
      print('    attendu : %s (en %d ops)' % (pR,refOps))
  print('* Score : %d/%d' % (score, ldata))
  
  encouragement = "" if fullPrec/ldata > 0.90 else " -> essaie d'atteindre 90% !"
  print('* Precision : %d%%%s\n' % (ceil(100*fullPrec/ldata),encouragement))



def colors() :
  return ['ro', 'co', 'go', 'bo', 'mo', 'yo']
def sparseRange(n,detail = 32) :
  res = []
  i = 1
  step = 1
  while i < n:
    res = res + [i]
    i += step
    if i == detail * step:
      step *= 2
  return res
def powerRange(n) :
  return [2**i for i in range(n)]
def courbes_smooth_ops(n, algos) :
  ''' affiche les courbes des additions effectuees pour le calcul de coefficients binomiaux (n,n//2) par les différents algos '''
  alg = len(algos)
  ops = [[]] * alg

  sR = sparseRange(n)
  for k in range(alg) :
    ops[k] = [ algos[k]([1]*i,[1]*i)[1] for i in sR ]
  
  col = colors()
  for i in range(0,alg) :
    plot(sR, ops[i], col[i])
    
  show()

def courbes_powers_ops(n, algos) :
  ''' affiche les courbes des additions effectuees pour le calcul de coefficients binomiaux (n,n//2) par les différents algos '''
  alg = len(algos)
  ops = [[]] * alg

  pR = powerRange(n)
    
  for k in range(alg) :
    ops[k] = [ algos[k]([1]*i,[1]*i)[1] for i in pR ]

  col = colors()
  for i in range(0,alg) :
    plot(pR, ops[i], col[i])
  show()

allProds = [polyProdNaifOps,polyProdKaraOps,polyProdKara2Ops,polyProdKara3Ops,polyProdKara4Ops,polyProdOptiOps]

if __name__ == '__main__':
  test_minPuissanceDe2()
  test_polyDegreAdapte()
  test_polyAjoute()
  test_polyProd(polyProdKara)
  test_polyProdKaraOps()
  print('Comparaison graphique de Karatsuba (bleu) avec la méthode naïve (rouge)...')
  courbes_powers_ops(10,[polyProdNaifOps,polyProdKaraOps])
  courbes_smooth_ops(512,[polyProdNaifOps,polyProdKaraOps])
  #Affichage pour les questions 6 et 7 :
  #test_polyProdKaraOps(2)
  #test_polyProdKaraOps(3)
  #print('Comparaison graphique totale...')
  #courbes_powers_ops(10,allProds)
  #courbes_smooth_ops(512,allProds)
