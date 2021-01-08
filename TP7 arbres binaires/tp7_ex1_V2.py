#!/usr/bin/env python3

from tp7 import *
from tp7_ex1_test import *

def estVide(arbre) :
    if arbre == [[None,None,None,None]] or arbre == []:
        return True
    else:
        return False

def etiquette(arbre, i) :
    if i < len(arbre) :
        if estVide(arbre):
            return None
        else:
            return arbre[i][0]
    else:
        return None

def filsGauche(arbre, i) :
    if i < len(arbre):
        if estVide(arbre):
            return None
        if arbre[i][1] == None:
            return None
        if arbre[i][1] < len(arbre):
            return arbre[i][1]
        else:
            return None
    else:
        return None

def filsDroit(arbre, i) :
    if i < len(arbre):
        if estVide(arbre):
            return None
        if arbre[i][2] == None:
            return None
        if arbre[i][2] < len(arbre):
            return arbre[i][2]
        else:
            return None
    else:
        return None
  
def pere(arbre, i) :
    if i < len(arbre):
        if estVide(arbre):
            return None
        if arbre[i][3] == None:
            return None
        if arbre[i][3] < len(arbre):
            return arbre[i][3]
        else:
            return None
    else:
        return None

def estRacine(arbre, i) :
    if i >= len(arbre):
        return False
    if arbre[i][3] == None:
        if arbre[i][0] == None:
            return False
        return True
    else:
        return False
  
def estFilsGauche(arbre, i) :
    if i >= len(arbre):
        return False
    if arbre[arbre[i][3]] != None and arbre[arbre[i][3]][1] == i:
        return True
    else:
        return False


def estFilsDroit(arbre, i) :
    if i >= len(arbre):
        return False
    if arbre[arbre[i][3]] != None and arbre[arbre[i][3]][2] == i:
        return True
    else:
        return False

def estFeuille1(arbre, i) :
    if i >= len(arbre):
        return False
    if estRacine(arbre,i):
        return True
    if arbre[i][0] != None :
        if arbre[i][1] == None and arbre[i][2] == None :
            return True
    if estRacine(arbre,i):
        return False
    return False

def estFeuille(arbre, i) :
    if i >= len(arbre):
        return False
    if arbre[i][3] != None :
        if arbre[i][1] == None and arbre[i][2] == None :
            return True
    
    return False
    
if __name__ == '__main__':
  testAll()
