#!/usr/local/bin/python3

############################################################
# Exercice 1.1
#
# Calcule le nombre d'elements de T egaux à x
#
def occurrence(T, x) :
  res = 0
  # À remplir

  for i in range(len(T)):
    if T[i] == x:
      res += 1
  return res

############################################################
# Exercice 1.2
# Compte le nombre d comparaisons effectuées lors de l'exécution de "occurrence"

def occurrenceOps(T,x) :
    res,ops=0,0
    # A remplir
    for i in range(len(T)):
      ops += 1 
      if T[i] == x:
        res += 1
    return res,ops


############################################################
# Exercice 1.3
#
# Compte les occurrences des nombres de 0..m-1 en T
#    en utilisant la fonction occurence
#

def compteNaif(T, m) :
  res = [0] * m
  # À remplir
  for i in range(m):
    res[i] = occurrence(T,i)
  return res



############################################################
# Exercice 1.4
#
# Compte les occurrences des nombres de 0..m-1 en T
#    et le nombre d'operations
#

def compteNaifOps(T, m) :
  res = [0] * m
  ops = 0
  # À remplir
  for i in range(m):
    res[i],temp = occurrenceOps(T,i)
    ops += temp
  
  return res, ops







############################################################
# TESTS 
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"


############################################################
#
# Tests : occurence
#


def test_occurrenceData() :
  return [[[4,3,1], 2, 0],
          [[1,2,3,1,2,3,1,2,3], 2, 3],
          [[2] * 1000000, 2, 1000000],
          [[3] * 10000000, 2, 0]]


def test_occurrence () :
  print('Test occurrence:')
  score = 0
  data = test_occurrenceData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = occurrence(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %d' % res)
      print('    attendu : %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))



############################################################
#
# Tests : occurenceOps
#


def test_occurrenceOpsData() :
  return [[[4,3,1], 2, 3],
          [[1,2,3,1,2,3,1,2,3], 2, 9],
          [[2] * 1000000, 2, 1000000],
          [[3] * 10000000, 2, 10000000]]


def test_occurrenceOps () :
  print('Test occurrenceOps:')
  score = 0
  data = test_occurrenceOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    opsdata = dt[2]
    res,ops = occurrenceOps(T,x)
    if opsdata == ops :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    opérations comptabilisées  : %d' % res)
      print('    attendu : %d' % opsdata)
############################################################
#
# Tests : compteNaif
#

def test_compteNaifData():
  return [[[4,3,1], 2, [0,1]],
          [[1,2,3,1,2,3,1,2,3], 3, [0,3,3]],
          [[2] * 1000000, 3, [0,0,1000000]],
          [[3] * 10000000, 2, [0,0]]]


def test_compteNaif () :
  print('Test compte:')
  score = 0
  data = test_compteNaifData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = compteNaif(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


############################################################
#
# Tests : compteOps
#


def test_compteNaifOpsData():  
  return [[[4,3,1], 2, [0,1], 6],
          [[1,2,3,1,2,3,1,2,3], 3, [0,3,3], 27],
          [[2] * 1000000, 3, [0,0,1000000], 1000000*3],
          [[3] * 10000000, 2, [0,0], 10000000*2]]




def test_compteNaifOps () :
  print('Test compteNaifOps:')
  score = 0
  data = test_compteNaifOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    refOps = dt[3]
    res,ops = compteNaifOps(T,x)
    if res == ref  and refOps <= ops:
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %s (en %d ops)' % (str(res),ops))
      print('    attendu : %s (en au moins %d ops)' % (str(ref),refOps))
  print('* Score : %d/%d\n' % (score, ldata))


    





if __name__ == '__main__':
  test_occurrence()
  test_occurrenceOps()
  test_compteNaif()
  test_compteNaifOps()

