# -*- coding: utf-8 -*-
#!usr/bin/env python3.6
import re
from token import *
from math import *


def recupVect(fic):
    """Cette fonction va nous serir à récupérer les valeurs de chaque clé du fichier
    Les fichiers mis en arguments seront ceux du types r'\w+Dico\.txt' créés par la classe token"""
    t2 = []
    data = dict()
    if re.match(r'\w+Dico\.txt',fic):
        with open(fic, encoding="utf8") as raw_data:
            val = raw_data.read()
            data = json.loads(val)
            for key, value in data.items() :
                t2.append(value)
    return t2


def creaVect(d1):
    #cette fonction permet de récupérer les coordonnées du vecteur en deux dimensions
    a,b = 1,0
    for i in range(len(d1)-1):
        j = i + 1
        for j in range(len(d1)):
            if(int(d1[i]) > int(d1[j])) and (int(d1[j]) < a):
                a = int(d1[j])
            elif(int(d1[i]) < int(d1[j])) and (int(d1[i]) < a):
                a = int(d1[i])
            if(int(d1[i]) < int(d1[j])) and (int(d1[j]) > b):
                b = int(d1[j])
            elif(int(d1[i]) > int(d1[j])) and (int(d1[i]) > b):
                b = int(d1[i])
    coord = (a,b)
    print("creaVect v1 : "+str(coord))
    return coord


def produitScal(d1,d2):
    """Il s'agit de la formule qui récupère les coordonnées des vecteurs. Ici, on fait attention à multiplier les coordonnées qui correspondent au même bigramme."""
    resultat = 0
    dic1 = lireDico(d1)
    dic2 = lireDico(d2)
    for key1,value1 in dic1.items():
        for key2,value2 in dic2.items():
            if(key1 == key2):
                resultat += value1*value2
    print("produit scalaire : " + str(resultat))
    return resultat

def normeVect(d1):
    #pour un vect a de coord (x,y), la norme ||a|| = (x²+y²)^1/2
    l,n = [],0
    l = recupVect(d1)
    for i in range(len(l)):
        n += int(l[i])**2
    return(sqrt(n))


def simCosinus(d1,d2):
    #pour deux vect a et b, la similarité cosinus cos(l) = (a*b)/(||a||*||b||)
    """Comme la valeur cos θ est comprise dans l'intervalle [-1,1], la valeur -1 indiquera des vecteurs résolument opposés, 0 des vecteurs indépendants (orthogonaux) et 1 des vecteurs similaires
    Les valeurs intermédiaires permettent d'évaluer le degré de similarité."""
    a = produitScal(d1,d2)
    b = normeVect(d1)
    c = normeVect(d2)
    print("sim cos : " + str(a/(b*c)))
    return(a/(b*c))
